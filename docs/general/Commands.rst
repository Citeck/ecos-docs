Команды
=========

**Команда** — декларативное описание действия, которое нужно сделать на удаленном сервисе или локально.

 .. image:: _static/commands/Commands_1.png
       :width: 600
       :align: center

**Команды** в Citeck ECOS в качестве транспорта используют очереди RabbitMQ. Использование команд возможно как в синхронном, так и в асинхронном режиме.

Целью команд могут быть:

    1. Тип сервиса (ecos-process, ecos-uiserv, alfresco и др.). Команду исполняет один из инстансов данного сервиса.

    2. Инстанс сервиса (у каждого типа сервиса может быть много инстансов).

    3. Все типы сервисов (широковещательные команды). Сервис-источник команды отправляет широковещательную команду в RabbitMQ и её обрабатывают все сервисы, которые в данный момент активны.

Выполнение команды осуществляется с помощью сервиса **CommandService**. В частности его методом **execute** и **executeSync**:

Команды могут быть как локальными (т.е. исполняются в рамках одного сервиса), так и удаленными (команда отправляется в другой микросервис, в этом случае необходимо указать **id микросервиса**, куда отправится команда)

Для реализации удаленной команды:

1. Создать DTO в сервисе, ИЗ которого будет отправлена команда и там где она будет исполняться,  например, если необходимо отправить команду из alfresco в микросервис интеграций, то необходимо создать 2 идентичных класса, один в alfresco, а второй в микросервис интеграций:

.. code-block::

    @Data
    @CommandType("execute-spark-method")
    public class SparkServiceMethodCommand {
        private String dataSourceId;
        private String methodName;
        private Map<String, String> methodAttributes;
    }

Обязательно указать аннотацию **CommandType** с уникальным именем команды (по ней определяется какому **Executorу** будет отдана данная команда (см. пункт 3)).

2. Также необходим DTO с ожидаемым ответом, его также необходимо реализовать в обоих сервисах.

По сути отправляем DTO c данными, который конвертируется в json, затем отправляется в нужный микросервис, там конвертируется обратно в DTO и с ним уже работает executor, после обработки executorом снова необходимо отдать DTO c ответом, который также конвертируется в json и отсылается обратно в то место, откуда была вызвана команда, там он опять трансформируется из json в ResponseDTO.
Например, ответ, который ожидаем от исполнения команды высланным выше DTO:

.. code-block::

    @AllArgsConstructor
    @NoArgsConstructor
    @Data
    public class SparkServiceMethodCommandResponse {
        private String status;
        private String xmlContent;
    }

3. В сервисе, КУДА отсылается команда, необходимо реализовать **Executor**, который будет обрабатывать DTO.

В executor необходимо имплиментировать интерфейс **CommandExecutor<E>** , где **E** - входящий DTO (п.1)

Также необходимо реализовать метод **execute(E)**, в котором собственно и заключается обработка самой команды. Т.е. принимаем на вход DTO c запросом (п.1), берем из него данные, обрабатываем, затем формируем DTO с ответом в этом методе и возвращаем его.

Пример:

.. code-block::

    public class CallSparkServiceCommandExecutor implements CommandExecutor<SparkServiceMethodCommand> {

        @Override
        public SparkServiceMethodCommandResponse execute(SparkServiceMethodCommand executeServiceMethodCommand) {
            String statusString = "Error";
            String methodName = executeServiceMethodCommand.getMethodName();
            if (methodName.equals("Complete")) {
                statusString = "Done";
            }
            
            SparkServiceMethodCommandResponse response = new SparkServiceMethodCommandResponse();
            response.setStatus(statusString);
            response.setXmlContent("<?xml version=\"1.0\" encoding=\"UTF-8\"?><TestTag>Test</TestTag>");
            return response;
        }

    }

Пример логики, где просто проверяем имя метода и формируем ответную DTO.

1. В сервисе, ИЗ которого отправляем командный запрос, используем **CommandService** для отправки команды, пример:

.. code-block::

    public String sendSparkRequest(String dataSourceId, String methodName, Map<String, String> attributes) {
            SparkServiceMethodCommand command = new SparkServiceMethodCommand();
            command.setDataSourceId(dataSourceId);
            command.setMethodName(methodName);
            command.setMethodAttributes(attributes);
            SparkServiceMethodCommandResponse result = commandsService.executeSync(command, "integrations")
                    .getResultAs(SparkServiceMethodCommandResponse.class);
            return result.getXmlContent();
        }

В данном примере формируем DTO (также можно использовать builder) и отправляем команду в микросервис интеграций, явно указывая это во втором параметре.

В ответе ожидаем **SparkServiceMethodCommandResponse** DTO и используем метод **.getResultAs** для автоматической конвертации ответа в удобный DTO.


