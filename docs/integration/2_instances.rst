.. _two_instances:

Обмен командами между двумя и более контурами Citeck
===========================================================================

.. contents::
   :depth: 3

Требования
-----------

Микросервис integrations создаёт мост команд между контурами через настройку ``ecos-integrations.extecos``. Для каждого указанного локального приложения мост слушает RabbitMQ удалённого контура и перенаправляет полученные команды в локальное приложение.

1. В каждом участвующем контуре должны работать необходимые для операции приложения и транспорт команд. В целевом приложении должен быть зарегистрирован исполнитель нужного типа команды.

2. Микросервис integrations целевого контура должен иметь сетевой доступ и учётные данные для RabbitMQ контура, из которого отправляются команды.

3. Для обмена в обоих направлениях необходимо настроить мосты с обеих сторон.

.. note::

   Эта настройка относится к командам. В текущей реализации ``extecos`` подключение к Zookeeper и пересылка событий не предусмотрены. Механизм :ref:`событий<ecos_events>` настраивается отдельно.

Настройка
----------

Подключения integrations при обмене в обоих направлениях:

.. mermaid::

   flowchart LR
       subgraph MAIN["main-ecos"]
           I0["integrations"]
           R0["RabbitMQ"]
           I0 -->|"локальный транспорт команд"| R0
       end
       subgraph SECOND["second-ecos"]
           I1["integrations"]
           R1["RabbitMQ"]
           I1 -->|"локальный транспорт команд"| R1
       end
       I0 -.->|"extecos: приём для main-ecos"| R1
       I1 -.->|"extecos: приём для second-ecos"| R0

Пунктирные подключения задаются в central-config для микросервиса integrations. Пример на стороне **main-ecos**, принимающей команды от **second-ecos**:

.. code-block:: yaml

    ecos-integrations:
      extecos:
        - this-app-name: main-ecos
          connections:
            rabbitmq:
              host: rabbitmq.second-ecos.example
              username: admin
              password: admin
          commands:
            apps:
              - alfresco

Замените адрес и учётные данные RabbitMQ значениями удалённого контура. ``alfresco`` — пример локального приложения, принимающего команды; укажите приложения своей установки.

При такой настройке приложение в **second-ecos** отправляет команду через свой локальный транспорт на адрес ``main-ecos/alfresco``. Мост в **main-ecos** получает её из RabbitMQ контура **second-ecos** и перенаправляет в локальный ``alfresco``.

Для обратного направления в **second-ecos** указываются ``this-app-name: second-ecos``, RabbitMQ контура **main-ecos** и список локальных приложений **second-ecos**.

.. list-table::
   :widths: 10 30
   :header-rows: 1
   :class: tight-table
   :align: center

   * - Поле
     - Описание
   * - **extecos**
     - Список подключений к внешним контурам. Можно задать несколько подключений; каждое использует ресурсы соединения и сервисов команд.
   * - **extecos[].this-app-name**
     - Обязательное имя текущего контура, под которым его локальные приложения представлены на удалённом RabbitMQ. Внешний адрес приложения: ``this-app-name/имя-приложения``.
   * - **extecos[].connections**
     - Параметры подключения к RabbitMQ удалённого контура в разделе ``rabbitmq``. Поле ``rabbitmq.host`` обязательно.
   * - **extecos[].commands**
     - Настройка команд.
   * - **extecos[].commands.apps**
     - Локальные приложения, принимающие команды из удалённого контура. Пустой список не создаёт мостов приложений.

Дополнительные параметры подключения задаются внутри ``extecos[].connections.rabbitmq``:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Параметр
     - Описание
   * - ``port``, ``virtual-host``
     - Порт и виртуальный хост RabbitMQ.
   * - ``executor``
     - Параметр исполнителя, передаваемый библиотеке подключения RabbitMQ.
   * - ``tls.enabled``
     - Включение TLS.
   * - ``tls.client-key``, ``tls.trusted-certs``
     - Настройки клиентского ключа и доверенных сертификатов.
   * - ``tls.protocol``, ``tls.verify-hostname``
     - Протокол TLS и проверка имени сервера.

Для неуказанных параметров используются значения по умолчанию из библиотеки RabbitMQ. Параметры сервиса команд задаются в ``extecos[].commands.props``: ``command-timeout-ms``, ``concurrent-command-consumers`` и ``channel-qos``.

.. important::

   Мост принудительно отключает приём широковещательных команд: ``commands.props.listen-broadcast=true`` не переопределяет это поведение.

   Конфигурация мостов считывается один раз при инициализации контекста приложения. После изменения настроек перезапустите integrations.

При перенаправлении команды мост задаёт локальное целевое приложение и заменяет ``sourceApp``/``sourceAppId`` своими значениями. На эти поля нельзя полагаться для сохранения исходной идентичности внешнего отправителя.

Регистрация исполнителя команд
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Инжектим **CommandsService** и вызываем:

.. code-block:: java

    commandsService.addExecutor(new SomeExecutor());

Пример исполнителя команд:

.. code-block:: java

    public class SomeExecutor implements CommandExecutor<SomeBody> {

        @Nullable
        @Override
        public Object execute(SomeBody someBody) {
            // Выполняем необходимые действия.
            return "OK";
        }
    }

    @Data
    @CommandType("some-command-type")
    public class SomeBody {
        private String strField = "str-field";
        private byte[] bytesField;
    }

- **SomeExecutor** - принимающая сторона, а отправляющая сторона будет там где вызовется commandsService.execute (пример в разделе "отправка команд").
- **SomeBody** — DTO тела команды. На отправляющей и принимающей сторонах должна быть согласована схема тела: имена полей, типы и правила сериализации. Совместимость DTO необходимо проверять при изменении схемы или версий библиотек.
- **@CommandType("some-command-type")** - аннотация на типе тела команды, определяющая тип команды. С отправляющей стороны тип можно также задать явно через ``builder.setType("some-command-type")``.

Отправка команды во внешнюю систему (из Citeck 1 (second-ecos) в Citeck 0 (main-ecos))
-----------------------------------------------------------------------------------------

Из java кода
~~~~~~~~~~~~

Инжектим **CommandsService** и вызываем отправку команды:

.. code-block:: java

    CommandResult result = commandsService.executeSync(builder -> {
        builder.setTargetApp("main-ecos/alfresco");
        builder.setType("some-command-type");
        builder.setBody(new SomeBody());
        builder.setTtl(Duration.ofMinutes(1));
        return Unit.INSTANCE;
    });

    if (result.getPrimaryError() != null) {
        throw new RuntimeException(result.getPrimaryError());
    }
    String value = result.getResultAs(String.class);

Здесь ``CommandResult`` — ``ru.citeck.ecos.commands.dto.CommandResult``, ``Duration`` — ``java.time.Duration``, ``Unit`` — ``kotlin.Unit``. ``executeSync`` возвращает объект результата команды; значение, возвращённое исполнителем, извлекается через ``getResultAs``.

.. list-table::
   :widths: 10 30
   :header-rows: 1
   :class: tight-table
   :align: center

   * - Параметр
     - Описание
   * - **executeSync**
     - Вместо ``executeSync`` можно вызвать просто ``execute``, чтобы не дожидаться ответа.
   * - **setTargetApp**
     - Целевое приложение. Является значением ``this-app-name`` из конфигурации целевого контура Citeck + "/" + идентификатор целевого приложения.
   * - **setType**
     - Тип команды, по которому будет выбран ``CommandExecutor`` для выполнения. Вместо этого вызова тип можно указать через аннотацию ``@CommandType``.
   * - **setBody**
     - Тело команды, совместимое со схемой DTO принимающего исполнителя.
   * - **setTtl**
     - Время жизни команды, передаваемое библиотеке команд. TTL не следует использовать как механизм отмены уже выполняемой операции.

Если предположим, что отправка осуществляется из alfresco (Citeck 1 - second-ecos) в alfresco (Citeck 0 - main-ecos), то ход команды будет следующим:

.. mermaid::

   sequenceDiagram
       participant S as alfresco (second-ecos)
       participant R1 as RabbitMQ (second-ecos)
       participant I0 as integrations (main-ecos)
       participant R0 as RabbitMQ (main-ecos)
       participant T as alfresco (main-ecos)
       S->>R1: Команда для main-ecos/alfresco
       R1->>I0: Получение команды мостом extecos
       I0->>R0: Перенаправление в локальный alfresco
       R0->>T: Выполнение команды
       T-->>R0: Результат
       R0-->>I0: Результат локального вызова
       I0-->>R1: Ответ на внешнюю команду
       R1-->>S: Результат

Тестирование отправки команд
-----------------------------

Сначала проверьте отправку команды локальному приложению по адресу ``alfresco``. Затем настройте мост и повторите проверку с адресом ``main-ecos/alfresco``.

Пример ручного интеграционного теста в **ecos-integrations** использует ``CommandsService`` из контекста приложения. Перед запуском настройте локальный RabbitMQ и остальные зависимости приложения, запустите целевой ``alfresco`` и зарегистрируйте в нём ``SomeExecutor`` из примера выше. Снимите ``@Disabled`` для ручного запуска на подготовленном окружении.

.. code-block:: java

    package ru.citeck.ecos.integrations;

    import java.time.Duration;
    import java.util.Map;
    import kotlin.Unit;
    import org.junit.jupiter.api.Disabled;
    import org.junit.jupiter.api.Test;
    import org.junit.jupiter.api.extension.ExtendWith;
    import org.springframework.beans.factory.annotation.Autowired;
    import org.springframework.boot.test.context.SpringBootTest;
    import ru.citeck.ecos.commands.CommandsService;
    import ru.citeck.ecos.commands.dto.CommandResult;
    import ru.citeck.ecos.webapp.lib.spring.test.extension.EcosSpringExtension;

    import static org.junit.jupiter.api.Assertions.assertEquals;
    import static org.junit.jupiter.api.Assertions.assertNull;

    @Disabled("Run manually with configured RabbitMQ and target executor")
    @ExtendWith(EcosSpringExtension.class)
    @SpringBootTest(classes = IntegrationsApp.class)
    public class CommandsTest {

        @Autowired
        private CommandsService commandsService;

        @Test
        public void testLocalCommand() {
            CommandResult result = commandsService.executeSync(builder -> {
                builder.setTargetApp("alfresco");
                builder.setType("some-command-type");
                builder.setBody(Map.of("strField", "str-field"));
                builder.setTtl(Duration.ofMinutes(1));
                return Unit.INSTANCE;
            });

            assertNull(result.getPrimaryError());
            assertEquals("OK", result.getResultAs(String.class));
        }
    }

Тело в этом тесте задано как объект с полем ``strField``, соответствующим DTO ``SomeBody`` принимающей стороны. Подключение к RabbitMQ и контекст приложения предоставляет приложение; создавать собственные ``CommandsProperties`` и ``CommandsServiceFactory`` в тесте не требуется.

.. dropdown:: Локальное тестирование отправки команд на удаленный инстанс
   :color: secondary

   Выполняйте после проверки локального исполнителя.

   1. Добавьте настройку ``extecos`` из раздела **Настройка**, указав тестовый RabbitMQ, доступный процессу integrations. Для проверки адресации моста можно использовать один RabbitMQ и уникальный префикс контура ``main-ecos``. Убедитесь, что другие мосты не регистрируют тот же адрес ``main-ecos/alfresco``.

   2. Перезапустите integrations. В тесте замените ``builder.setTargetApp("alfresco")`` на:

      .. code-block:: java

          builder.setTargetApp("main-ecos/alfresco");

   3. Повторите тест и проверьте результат. Такая проверка не подтверждает сетевую доступность и настройки отдельного удалённого RabbitMQ.

Для проверки с двумя контурами настройте в целевом integrations доступ к RabbitMQ отправителя, а тест запускайте в контуре отправителя с адресом целевого приложения ``main-ecos/alfresco``.

Отправка файлов в командах
--------------------------------------

Файлы можно передавать в полях DTO типа ``byte[]``. При выборе размера тела учитывайте ограничения RabbitMQ и затраты на сериализацию. Не следует рассчитывать на обязательное автоматическое сжатие всех сообщений.

Для удобной работы с файлами есть утилитные классы **EcosMemFile EcosMemDir** и **ru.citeck.ecos.commons.utils.ZipUtils**, который может легко упаковывать много файлов в один поток байт и обратно.

Пример:

.. code-block:: java

    SomeBody body = new SomeBody();

    EcosMemDir dir = new EcosMemDir();
    dir.createFile("firstFile.txt", "content");
    dir.createFile("secondFile.docx", new byte[10]);
    body.setBytesField(ZipUtils.writeZipAsBytes(dir));

    commandsService.executeSync(builder -> {
        builder.setTargetApp("main-ecos/alfresco");
        builder.setType("some-command-type");
        builder.setBody(body);
        builder.setTtl(Duration.ofMinutes(1));
        return Unit.INSTANCE;
    });
