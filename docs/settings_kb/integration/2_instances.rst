Общение между двумя и более инстансами ECOS'а через команды и события
======================================================================

Требования
-----------

1. Инстансы ECOS должны быть самодостаточны. Т.е. в каждом ECOS должен быть развернут полный список необходимых микросервисов для полноценной работы.

2. Микросервис интеграции в каждом контуре ECOS должен иметь доступ по сети к RabbitMQ и Zookeeper удаленного ECOS.

3. В каждом контуре ECOS должен быть микросервис интеграции версии 1.15.0+ (пока SNAPSHOT) 

.. note::

    доступ к Zookeeper нужен для работы событий, но они пока в TODO, а для работы команд достаточно доступа к RabbitMQ. 

Настройка
----------

Схема подключения двух инстансов ECOS'а: 

 .. image:: _static/2_instances/2_instances_1.png
       :width: 600
       :align: center

Подключение пунктирными линиями настраиваются в central-config для микросервиса интеграции (в дальнейшем подключение к Zookeeper будет в connections под ключом “zookeeper”):

.. code-block::

    # Пример конфигурации для main-ecos. Для second-ecos изменится this-app-name и возможно host/user/pass у rabbitmq 
    ecos-integrations:
    extecos:
        - this-app-name: main-ecos
        connections:
            rabbitmq:
            host: localhost
            username: admin
            password: admin
        commands:
            apps:
            - alfresco

**extecos** - массив из подключений к различным контурам ECOS (поддерживается неограниченное кол-во подключений).

**extecos[].this-app-name** - имя текущего контура экос. Будет использоваться при отправке команд и событий из внешней системы в текущую

**extecos[].connections** - раздел с подключениями к RabbitMQ и Zookeeper

**extecos[].commands** - настройка команд;

**extecos[].commands.apps** - локальные приложения, которым будет возможность отправлять команды из внешней системы.

**Регистрация исполнителя команд**

Инжектим **CommandsService** и вызываем:

.. code-block::

    commandsService.addExecutor(new SomeExecutor());

Пример исполнителя команд:

.. code-block::

    public class SomeExecutor implements CommandExecutor<SomeBody> { // SomeBody - любой DTO тип, который будет передаваться в Body команды. DTO тип должен иметь аннотацию CommandType для определения типа команды

        @Nullable
        @Override
        public Object execute(SomeBody someBody) {
            //выполняем необходимые действи
            return "OK";
        }
    }

    @Data
    @CommandType("some-command-type") // тип команды. С отправляющей стороны задается как builder.setType("some-command-type") или так же через аннотацию на типе тела команды, которое передается как builder.setBody(...)
    public class SomeBody {
        private String strField = "str-field";
        private byte[] bytesField;
    }

**SomeExecutor** - принимающая сторона, а отправляющая сторона будет там где вызовется commandsService.execute (пример в разделе “отправка команд”)

**SomeBody** класс должен быть описан на отправляющей стороне и на принимающей (Дстаточно чтобы имена полей и типы полей совпадали. Пакеты при этом не важны. Jackson позаботится о приобразовании данных).

Отправка команды во внешнюю систему (из ECOS 1 (second-ecos) в ECOS 0 (main-ecos))
-----------------------------------------------------------------------------------

**Из java кода**

Инжектим **CommandsService** и вызываем отправку команды:

.. code-block::

    commandsService.executeSync(builder -> { // вместо executeSync можно вызвать просто execute, чтобы не дожидаться ответа. 
        builder.setTargetApp("main-ecos/alfresco"); // целевое приложение. Является значением this-app-name из конфигурации целевого контура ECOS + "/" + индентификатор целевого приложения 
        builder.setType("some-command-type"); // тип события. по нему будет выбран CommandExecutor для выполнения. Вместо данной строки тип можно указать через аннотацию @CommandType
        builder.setBody(new SomeBody()); // любой инстанс DTO класса. Преобразуется в байты и обратно с помощью библиотеки Jackson
        builder.setTtl(Duration.of(1, ChronoUnit.MINUTES)); //время жизни сообщения в RabbitMQ. Если за это время сообщение никто не обработает, то оно удалится из очередей. 
        return Unit.INSTANCE;
    })

Если предположим, что отправка осуществляется из alfresco (ECOS 1 - second-ecos) в alfresco (ECOS 0 - main-ecos), то ход команды будет следующим:

 .. image:: _static/2_instances/2_instances_2.png
       :width: 600
       :align: center

Тестирование отправки команд
-----------------------------

Отправка команд в удаленный ECOS и локальный отличается только аргументом в **setTargetApp**. Т.о. отлаживать механизм можно без учета нескольких инстансов ECOS.

Отправка команды в локальный RabbitMQ через Java тест (можно размещать в **ecos-integrations**):

.. code-block::

    public class CommandsTest {

        @Test
        public void test() {

            // подключаемся к нужному RabbitMQ
            RabbitMqConnProps props = new RabbitMqConnProps();
            props.setUsername("admin");
            props.setPassword("admin");
            props.setHost("localhost");

            RabbitMqConnFactory factory = new RabbitMqConnFactory();
            RabbitMqConn conn = factory.createConnection(props, 0);

            conn.waitUntilReady(5000);

            CommandsServiceFactory commFactory = new CommandsServiceFactory() {

                @NotNull
                @Override
                protected CommandsProperties createProperties() {
                    CommandsProperties props = new CommandsProperties();
                    props.setAppName("alfresco1"); // "представляемся" в системе как приложение с именем "alfresco1" 
                    props.setAppInstanceId("alfresco1-123"); // идентификатор инстанса приложения
                    props.setListenBroadcast(false); // указываем, что широковещательные команды нам исполнять не нужно
                    return props;
                }

                @NotNull
                @Override
                protected RemoteCommandsService createRemoteCommandsService() {
                    return new RabbitCommandsService(this, conn);
                }
            };

            commFactory.getRemoteCommandsService();
            CommandsService commandsService = commFactory.getCommandsService();

            System.out.println(commandsService.executeSync(builder -> { // выполняем команду синхронно и выводим результат в консоль
                builder.setTargetApp("alfresco"); // отправляем команду в alfresco
                builder.setType("some-command-type"); // тип команды
                builder.setBody(new SomeBody()); // тело команды
                builder.setTtl(Duration.of(1, ChronoUnit.MINUTES));
                return Unit.INSTANCE;
            }));

            conn.close();
        }

        @Data
        @CommandType("some-command-type")
        public static class SomeBody {
            private String strField = "str-field";
            private byte[] bytesField;
        }
    }

Локальное тестирование отправки команд на удаленный инстанс (имеет смысл после отладки через обычную отправку команд):

1. Добавляем настройку удаленного контура ECOS как описано в разделе **“Настройка”**. В  качестве целевого RabbitMQ выбираем localhost. Т.о. можно локально тестировать работу с удаленными инстансами подняв только один инстанс RabbitMQ. Конфликтов при этом не возникнет.

2. Немного меняем аргумент в методе **setTargetApp** при отправке команды в тесте:

.. code-block::

    ... здесь все аналогично предыдущему блоку кода, который описывает класс CommandsTest ...
            System.out.println(commandsService.executeSync(builder -> {
                builder.setTargetApp("main-ecos/alfresco"); // единственное отличие при отправке команд - добавляется идентификатор контура ECOS со слэшем
                builder.setType("some-command-type");
                builder.setBody(new SomeBody());
                builder.setTtl(Duration.of(1, ChronoUnit.MINUTES));
                return Unit.INSTANCE;
            }));
    ... здесь все аналогично предыдущему блоку кода, который описывает класс CommandsTest ...

При желании можно подключиться и к реальному удаленному ECOS, но для этого должен быть доступ к RabbitMQ извне. При этом достаточно будет исправить параметры в **RabbitMqConnProps**

Отправка файлов в командах и событиях
--------------------------------------

Для отправки файлов в командах и событиях следует использовать поля с типом byte[] (сообщения сжимаются перед отправкой. Т.е. доп. оптимизация не нужна).

Для удобной работы с файлами есть утилитные классы **EcosMemFile EcosMemDir** и **ru.citeck.ecos.commons.utils.ZipUtils**, который может легко упаковывать много файлов в один поток байт и обратно.

Пример:

.. code-block::

    SomeBody body = new SomeBody();

    EcosMemDir dir = new EcosMemDir();
    dir.createFile("firstFile.txt", "content");
    dir.createFile("secondFile.docx", new byte[10]);
    body.setBytesField(ZipUtils.writeZipAsBytes(dir));

    commandsService.executeSync(builder -> {
        builder.setTargetApp("main-ecos/alfresco");
        builder.setType("some-command-type");
        builder.setBody(body);
        builder.setTtl(Duration.of(1, ChronoUnit.MINUTES));
        return Unit.INSTANCE;
    });