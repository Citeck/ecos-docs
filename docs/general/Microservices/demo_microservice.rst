Демо микросервис
===================

.. _demo_microservice:

.. contents:: 
   :depth: 5

Репозиторий `ecos-demo-app <https://github.com/Citeck/ecos-demo-app>`_ содержит приложение, демонстрирующее возможности Citeck.

Вы можете познакомиться с:

    - пользовательским :ref:`RecordsDAO<new_RecordsDAO>`;
    - работой с :ref:`RecordsService<ecos_RecordsService>`;
    - :ref:`действиями<ui_actions>`;
    - :ref:`командами<ecos_commands>`;
    - :ref:`событиями<ecos_events>`;
    - бизнес-процессом с  :ref:`Внешней задачей<ecos_bpmn_external_task>`;
    - созданием :ref:`дочерних ассоциаций<datatypes_associations>`.

См. подробнее про :ref:`артефакты Citeck<ecos_artifacts>`, :ref:`приложения<applications>`, :ref:`разработку и создание микросервисов<mcs_develop_setup>`.

При запуске приложения в левом меню по умолчанию появится раздел **«Демо тип/Demo type»** с двумя журналами:

    - **Журнал демо типа/Demo type journal** — основной демо журнал с процессом BPMN и различными демонстрационными действиями. Написанный ниже сценарий основан на этом типе.
    - **in-memory демо тип/Demo in-memory type** — журнал с сущностями в памяти для демонстрации работы с пользовательским **RecordsDAO**, определенным в *ru.citeck.ecos.webapp.demo.records.DemoInMemRecordsDao*. Вы можете создавать/просматривать/редактировать/удалять записи в этом журнале и смотреть, что изменилось в **DemoInMemRecordsDao**.

С чего начать
--------------

Если вы не знакомы с платформой Citeck, и хотите запустить программное обеспечение локально, мы рекомендуем вам загрузить Dockerized версию `Community demo <https://github.com/Citeck/ecos-community-demo>`_ Подробно :ref:`об установке<docker_compose>`

Зависимости
--------------

Для запуска этого приложения необходимы следующие приложения из развертывания Citeck:

    -	zookeeper; 
    -	rabbitmq;
    -	ecos-model;
    -	ecos-registry.

Запуск
-------

Клонируйте репозиторий в свою среду разработки. Для запуска приложения выполните:

.. code-block:: bash

    ./mvnw spring-boot:run

Если ваша IDE поддерживает запуск приложений Spring Boot напрямую, вы можете легко запустить класс ru.citeck.ecos.webapp.demo.EcosDemoApp без дополнительной настройки.

Описание сущностей микросервиса
------------------------------------

Артефакты
~~~~~~~~~

В папке **.../src/main/resources/eapps/artifacts** расположены артефакты проекта. Первые два уровня каталогов соответствуют типу артефакта. Например: 

* app/artifact-patch
* model/type
* notification/template
* process/bpmn
* ui/action, /form, /journal 

Подробнее про :ref:`артефакты Citeck<ecos_artifacts>`

Классы
~~~~~~

Records
"""""""

https://github.com/Citeck/ecos-demo-app/blob/master/src/main/java/ru/citeck/ecos/webapp/demo/records/DemoInMemRecordsDao.java

**Запись (Record)** – сущность с набором атрибутов и идентификатором записи (RecordRef).

Ниже разобран простой пример RecordsDAO с хранением сущностей в памяти. Данный RecordsDAO демонстрирует простые базовые операции CRUD в API Records и не реализует такие функции,  как ассоциации, хранение контента, проверку разрешений и т. д.

См. подробное описание :ref:`операций CRUD<ecos_RecordsService>` 

**Внимание:** Все данные будут потеряны после перезапуска приложения. Не используйте для продакшн-среды.

.. code-block:: java

    @Component
    public class DemoInMemRecordsDao extends AbstractRecordsDao
            implements RecordsQueryDao, RecordAttsDao, RecordMutateDao, RecordDeleteDao {

        public static final String ID = "demo-inmem-data";

        /**
        * Создание простого хранилища для записей. Все данные будут потеряны после рестарта приложения. 
        */
        private final Map<String, SimpleDto> records = new ConcurrentHashMap<>();

        /**
        * Запрос Query records поддерживает только язык «предикатов».
        * @param recordsQuery – параметры запроса, отправляемые с фронта
        * @return найденные записи и информацию об общем количестве без пагинации
        */
        @Nullable
        @Override
        public RecsQueryRes<?> queryRecords(@NotNull RecordsQuery recordsQuery) {

            // О предикатах подробно можно прочитать по ссылке
            // https://citeck-ecos.readthedocs.io/ru/latest/general/%D0%AF%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%B5%D0%B4%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D0%B2.html
            if (!PredicateService.LANGUAGE_PREDICATE.equals(recordsQuery.getLanguage())) {
                return null;
            }

            Predicate predicate = recordsQuery.getQuery(Predicate.class);

            QueryPage page = recordsQuery.getPage();
            List<SimpleDto> fullResult = predicateService.filterAndSort(
                    records.values(),
                    predicate,
                    recordsQuery.getSortBy(),
                    page.getSkipCount(),
                    page.getMaxItems()
            );

            RecsQueryRes<SimpleDto> recsQueryRes = new RecsQueryRes<>();
            recsQueryRes.setTotalCount(records.size());
            recsQueryRes.setRecords(fullResult);

            return recsQueryRes;
        }

        /**
        * Получить данные рекорда по localId.
        * @return сам рекорд или null
        */
        @Nullable
        @Override
        public Object getRecordAtts(@NotNull String localId) {
            return records.get(localId);
        }

        /**
        * Создание или обновление рекорда.
        * Если recordAtts.getId() пустая строка, то создается новый рекорд со сгенерированным localId 
        * @param recordAtts localId (String) и key-value map (ObjectData) с атрибутами сущности
        * @return localId существующего или созданного рекорда.
        */
        @NotNull
        @Override
        public String mutate(@NotNull LocalRecordAtts recordAtts) {
            SimpleDto recToMutate;
            if (recordAtts.getId().isEmpty()) { //создание
                // Обычно в других не демо-версиях RecordsDao, когда getId() пустой, 
                // id можно указать в атрибутах, но здесь мы не реализуем эту логику.
                // Вы можете просмотреть исходный код ru.citeck.ecos.records3.record.dao.impl.mem.InMemDataRecordsDao
                // чтобы проверить правильную реализацию метода mutate.
                recToMutate = new SimpleDto(UUID.randomUUID().toString());
            } else {
                recToMutate = records.get(recordAtts.getId()); // обновление
                if (recToMutate == null) {
                    throw new IllegalArgumentException("Record with id " + recordAtts.getId() + " is not found");
                }
                recToMutate = new SimpleDto(recToMutate);
                recToMutate.modified = Instant.now();
            }
            Json.getMapper().applyData(recToMutate, recordAtts.getAtts());
            if (recToMutate.id.isBlank()) {
                throw new IllegalArgumentException("Record id is empty after mutation. Atts: " + recordAtts);
            }
            records.put(recToMutate.id, recToMutate);
            return recToMutate.id;
        }

        /**
        * Удаление определенных рекордов.
        * @param localId удаленной записи
        * @return localId существующего или созданного рекорда.
        */
        @NotNull
        @Override
        public DelStatus delete(@NotNull String localId) {
            records.remove(localId);
            return DelStatus.OK;
        }

        @NotNull
        @Override
        public String getId() {
            return ID;
        }

        /**
        * Создание DTO
        */
        @Data
        @NoArgsConstructor
        @AllArgsConstructor
        public static class SimpleDto {

            private String id;
            private String textField;
            private int numField;

            private Instant created;
            private Instant modified;

            public SimpleDto(String id) {
                this.id = id;
                created = Instant.now();
                modified = created;
            }

            public SimpleDto(SimpleDto other) {
                this.id = other.id;
                this.textField = other.textField;
                this.numField = other.numField;
                this.created = other.created;
                this.modified = other.modified;
            }

            /**
            * Данный метод вызывается, когда скаляр '?disp' загружается из рекорда.
            * Подробно о скалярах https://citeck-ecos.readthedocs.io/ru/latest/general/ECOS_Records.html#id11
            * 'getDisplayName' специальное имя в DTO для скаляра '?disp'
            */
            public MLText getDisplayName() {
                Map<Locale, String> nameData = new HashMap<>();
                nameData.put(I18nContext.ENGLISH, "Demo in-mem '" + textField + "'");
                nameData.put(I18nContext.RUSSIAN, "Демо in-mem '" + textField + "'");
                return new MLText(nameData);
            }

            /**
            * Данный метод вызывается, когда атрибут '_type' attribute загружается из рекорда.
            * 'getEcosType' специальное имя в DTO  для атрибута DTO for '_type' .
            * Движок добавляет дополнительную логику для данного метода:
            * Если результат метода EntityRef или строка, начинающаяся с 'emodel/type@', то результат будет EntityRef.valueOf(methodResult).
            * Если результат метода строка и она не начинается с 'emodel/type@', то движок добавляет префикс 'emodel/type@' и возвращает результат EntityRef.valueOf.
            */
            public String getEcosType() {
                // type config: src/main/resources/eapps/artifacts/model/type/demo-inmem-type.yaml
                return "demo-inmem-type";
            }

            /**
            * Простой геттер для атрибута _created.
            * Аннотация AttName требуется, чтобы изменить имя атрибута по умолчанию "created" на "_created".
            * '_created' специальный мета атрибут для любого рекорда, который должен информировать, когда рекорд был создан. 
            */
            @AttName(RecordConstants.ATT_CREATED)
            public Instant getCreated() {
                return created;
            }

            /**
            * Простой геттер для атрибута _modified.
            * Аннотация AttName требуется, чтобы изменить имя атрибута по умолчанию "modified" на "_modified".
            * '_modified' специальный мета атрибут для любого рекорда, который должен информировать, когда рекорд был изменен последний раз.
            */
            @AttName(RecordConstants.ATT_MODIFIED)
            public Instant getModified() {
                return modified;
            }
        }
    }

Actions
""""""""

https://github.com/Citeck/ecos-demo-app/blob/master/src/main/java/ru/citeck/ecos/webapp/demo/actions/SendDemoEmailAction.java 

:ref:`Действия<ui_actions>` - артефакты Citeck в формате json или yaml с типом ui/action.

Артефакты действий расположены в папке **…/src/main/resources/eapps/artifacts/ui/action**

.. code-block:: java

    @Component
    @RequiredArgsConstructor
    public class SendDemoEmailAction extends AbstractRecordsDao implements ValueMutateDao<SendDemoEmailAction.ActionData> {

        /**
        * Идентификатор RecordsDAO. Используется для определения того, какой DAO должен обрабатывать запрос на мутацию. Это вторая половина EntityRef после'/' и до '@' 
        * Это 'send-demo-email'  в составе ecos-demo-app/send-demo-email@ 629fbd31-788a-4232-9de9-d737e5b07795
        * В запросах API этот идентификатор сочетается с appName называемым sourceId. Например: 'ecos-demo-app/send-demo-email'
        */
        public static final String ID = "send-demo-email";

        /**
        * Шаблон email 
        * Загружается из src/main/resources/eapps/artifacts/notification/template/demo-email.html.ftl
        */
        private static final EntityRef TEMPLATE_REF = EntityRef.create(
                AppName.NOTIFICATIONS,
                "template",
                "demo-email"
        );

        private final NotificationService notificationService;

        @Nullable
        @Override
        public Object mutate(@NotNull ActionData actionData) {

            String currentUser = AuthContext.getCurrentUser();
            EntityRef currentUserRef = AuthorityType.PERSON.getRef(currentUser);
            String email = recordsService.getAtt(currentUserRef, "email").asText();
            if (StringUtils.isBlank(email)) {
                throw new RuntimeException("Current user doesn't have email. Please open user profile and change it");
            }

            // Дополнительные метаданные могут использоваться для добавления пользовательских данных при отправке уведомления.
            // Шаблон уведомления может загружать любое значение из этих данных, используя '$' как префикс перед ключом
            // Например:
            // Template model = {"anyAliasWhichCanBeUsedInFtlTemplate": "$additionalStr"}
            // Ftl template   = "Some text ${anyAliasWhichCanBeUsedInFtlTemplate}"
            // Result         = "Some text additional-string-value"
            Map<String, Object> additionalMeta = new HashMap<>();
            additionalMeta.put("additionalStr", "additional-string-value");
            // Переменные могут содержать простые скаляры (string/number/boolean/etc.) или ссылки на любые объекты в системе
            // Например, мы добавляем сюда ссылку на текущего пользователя.
            additionalMeta.put("additionalUserRef", EntityRef.create(AppName.EMODEL, "person", currentUser));
            // Также можно использовать значения DTO, и шаблон может извлекать из них данные.
            additionalMeta.put("actionData", actionData);

            // NotificationService используется для ручной отправки уведомлений
            // Шаблон уведомления определяет модель с атрибутами, которые следует загрузить из рекорда и additionalMeta
            // Сервис работает следующим образом:
            // 1. Загрузить список атрибутов, необходимый для предоставленного templateRef
            // 2. Загрузить необходимые атрибуты из предоставленной записи и additionalMeta
            // 3. Отправить команду с загруженными данными в приложение уведомлений через RabbitMQ
            // Метод 'send' не ждет пока сообщение действительно будет отправлено
            notificationService.send(new Notification.Builder()
                    .addRecipient(email)
                    .record(actionData.entityRef)
                    .notificationType(NotificationType.EMAIL_NOTIFICATION)
                    .additionalMeta(additionalMeta)
                    .templateRef(TEMPLATE_REF)
                    .build());

            // с настройками по умолчанию отправленный email можно увидеть в mailhog - http://localhost:8025/
            return null;
        }

        @NotNull
        @Override
        public String getId() {
            return ID;
        }

        @Data
        public static class ActionData {
            private EntityRef entityRef;
            private String comment;
        }
    }

На фронте действие вызывается следующим образом:

.. code-block::

    let rec = Records.getRecordToEdit('ecos-demo-app/send-demo-email@');
    rec.att('entityRef', 'emodel/demo-type@629fbd31-788a-4232-9de9-d737e5b07795'); // any EntityRef
    rec.att('comment', 'any comment');
    await rec.save();

где 

  * **ecos-demo-app** - appName
  * **send-demo-email** - идентификатор RecordsDAO. Используется для определения того, какой DAO должен обрабатывать запрос на мутацию (см. SendDemoEmailAction.ID).
  * **EntityRef** - уникальный идентификатор сущности в системе Citeck. 

Commands
"""""""""

:ref:`Команды<ecos_commands>` в Citeck ECOS в основном используются для асинхронного обмена сообщениями между приложениями.

**Executor**

https://github.com/Citeck/ecos-demo-app/blob/master/src/main/java/ru/citeck/ecos/webapp/demo/commands/DemoCommandExecutor.java

В сервисе, куда отсылается команда, необходимо реализовать **Executor**, который будет обрабатывать DTO.

В данном demo executor рассматриваются понимания основные концепции. Тип команды будет рассчитываться на основе аннотации CommandType для универсального типа CommandExecutor.

.. code-block:: java

    @Slf4j
    @Component
    public class DemoCommandExecutor implements CommandExecutor<DemoCommandExecutor.DemoCommandDto> {

        public static final String TYPE = "demo-command";

        @Nullable
        @Override
        public Object execute(DemoCommandDto demoCommandDto) {
            log.info("Command received: " + demoCommandDto);
            return null;
        }

        @Data
        @CommandType(TYPE)
        public static class DemoCommandDto {
            private EntityRef entityRef;
            private String comment;
        }
    }

**Сама команда**

https://github.com/Citeck/ecos-demo-app/blob/master/src/main/java/ru/citeck/ecos/webapp/demo/commands/SendDemoCommandAction.java

В сервисе, из которого отправляем командный запрос, используем **CommandService** для отправки команды.

.. code-block:: java

    @Component
    @RequiredArgsConstructor
    public class SendDemoCommandAction extends AbstractRecordsDao implements ValueMutateDao<SendDemoCommandAction.ActionData> {

        public static final String ID = "send-demo-command";

        private final CommandsService commandsService;

        @Nullable
        @Override
        public Object mutate(@NotNull ActionData actionData) {

            Map<String, Object> body = new HashMap<>(); 
            body.put("entityRef", actionData.entityRef);
            body.put("comment", actionData.comment);

            // Command execution result you can see in logs
            commandsService.execute(b -> {
                b.withTargetApp("ecos-demo-app"); // эта команда отправляется в приложение
                b.withBody(body); // body может быть любой объект Map или DTO
                b.withType("demo-command"); // command executor будет выбран по этому типу
                return Unit.INSTANCE;
            });

            return null;
        }

        /**
        * переопределение DAO
        */

        @NotNull
        @Override
        public String getId() {
            return ID;
        }

        /**
        * Фронт отправляет 2 атрибута и создается инстанс ActionData	
        */


        @Data
        public static class ActionData {
            private EntityRef entityRef;
            private String comment;
        }
    }

Exttask
""""""""

:ref:`Внешние задачи<ecos_bpmn_external_task>` позволяют выполнять задачи с помощью внешних систем.

Пример внешней задачи для демо BPMN процесса: https://github.com/Citeck/ecos-demo-app/blob/master/src/main/java/ru/citeck/ecos/webapp/demo/exttask/DemoExternalTask.java

Артефакт бизнес-процесса расположен в папке **…/src/main/resources/eapps/artifacts/process/bpmn**

.. code-block:: java

    @Slf4j
    @Component
    @RequiredArgsConstructor
    @ExternalTaskSubscription("demo-ext-task")
    public class DemoExternalTask implements ExternalTaskHandler {

        private final RecordsService recordsService;

        @Override
        // Если вы обернете метод выполнения в RunInTransaction, то внешняя задача
        //  в процессе должен быть флаг asyncAfter, чтобы избежать ошибок транзакций
        @RunInTransaction
        @ExternalTaskRetry(retries = 10, retryTimeout = 10_000) // // настройка повторной обработки задачи, если в процессе обработки возникла техническая ошибка
        public void execute(ExternalTask externalTask, ExternalTaskService externalTaskService) {

            String documentRef = externalTask.getVariable("documentRef"); // получить ссылку на документ

            log.info("External task for document: " + documentRef); // вывести в лог полученную ссылку на документ 

            String textField = recordsService.getAtt(documentRef, "textField").asText(); // получить данные поля textField

            log.info("Text field: '" + textField + "'"); // вывести в лог полученные данные поля

            /*
            Вы можете использовать простую мутацию одного атрибута, используя метод mutateAtt 
            или используйте расширенный метод с RecordAtts. Например, обновить данные в поле extTaskField:

            RecordAtts record = new RecordAtts(documentRef);
            record.setAtt("extTaskField", "TextField: " + textField);
            record.setAtt("otherAttribute", "otherValue");
            recordsService.mutate(record);
            */
            recordsService.mutateAtt(documentRef, "extTaskField", "TextField: " + textField);

            // Здесь можно указать бизнес-ошибку. Эта ошибка должна быть правильно обработана в процессе
            // externalTaskService.handleBpmnError(externalTask, "error-code", "error-message");

            externalTaskService.complete(externalTask);
        }
    }

Job
"""""

Job позволяет запланировать однократное или регулярное выполнение заданий.

https://github.com/Citeck/ecos-demo-app/blob/master/src/main /java/ru/citeck/ecos/webapp/demo/job/SimpleAnnotatedJob.java 


.. code-block:: java

    @Slf4j
    @Component
    @RequiredArgsConstructor
    public class SimpleAnnotatedJob {

        private final AtomicInteger counter = new AtomicInteger();

        private final RecordsService recordsService;

        /**
        * Задание будет выполнено как системное.
        * @see Scheduled
        */
        @Scheduled(fixedDelayString = "${ecos.demo.simple-annotated-job.delay}") // задержка настраивается в application.yml
        void doSomeWork() {
            RecsQueryRes<EntityRef> queryRes = recordsService.query(
                    RecordsQuery.create()
                            .withEcosType("demo-type") // Запрос всех записей с типом demo-type, у которых есть childEntities
                            // sourceId будет загружен из ecosType по умолчанию,
                            // но вы можете указать это явно
                            //.withSourceId(AppName.EMODEL + "/demo-type")
                            .withQuery(Predicates.notEmpty("childEntities"))
                            .withMaxItems(0) // Query for totalCount without records
                            .build()
            );
            log.info("Simple annotated job example #" + counter.incrementAndGet() +
                    ". Demo records with children: " + queryRes.getTotalCount()); // вывод количества в лог
        }
    }

Сценарий работы
-----------------

1.	Запустите **ecos-demo-app**.
2.	В Citeck в верхнем левом углу нажмите **«Создать/Create»**.
3.	Выберите **«Демо тип/Demo type»** -> **«Демо тип/Demo type»**.
4.	Введите в поле **«Имя/Name»** значение **«ошибка»** и нажмите кнопку **«Сохранить/Save»**. Вы должны увидеть ошибку от транзакционного listener, определенного в *ru.citeck.ecos.webapp.demo.events.DemoEcosEventListener*.
5.	Измените значение поля **«Имя/Name»** на любое другое и заполните остальные поля.
6.	После создания вы увидите информацию о созданной записи:

    -	Статус будет **«Новый/New»**. Это определено в свойстве *defaultStatus* в конфигурации типа — *src/main/resources/eapps/artifacts/model/type/demo-type.yml*.
    -	Виджеты задач будут отображать активную задачу для текущего пользователя. Процесс BPMN запущен, поскольку у нас есть определение процесса в *src/main/resources/eapps/artifacts/process/bpmn/demo-process.bpmn.xml* с флагами *ecos:enabled="true"* и *ecos:autoStartEnabled="true"*.

7.	Нажмите кнопку **«Готово/Done»** в виджете текущей задачи.
8.	Задача исчезнет и будет запущена внешняя задача — *ru.citeck.ecos.webapp.demo.exttask.DemoExternalTask*.
9.	Примерно через 5–10 секунд вы сможете обновить вкладку браузера и увидеть новый статус **«Завершенный/Completed»** и заполненное поле **«Поле сгенерированное во внешней задаче/Field generated in external task»**. На этом этапе процесс BPMN завершается.
10.	Вы можете нажать **«Отправить демо письмо/Send demo email»**, чтобы протестировать специальное действие для отправки электронного письма.

    -	Класс действия: *ru.citeck.ecos.webapp.demo.actions.SendDemoEmailAction*
    -	Определение действия: *src/main/resources/eapps/artifacts/ui/action/send-demo-email-action.yml*
    -	Шаблон электронного письма: *src/main/resources/eapps/artifacts/notification/template/demo-email.html.ftl.*
    -	Письмо с результатом можно найти в mailhog (если вы не меняли настройки электронной почты по умолчанию) — http://localhost:8025/

11.	После тестирования отправки письма вы можете нажать **«Создать дочернюю сущность/Create child entity»**, чтобы проверить возможность создания связанных объектов по действию.

    -	Определение действия: *src/main/resources/eapps/artifacts/ui/action/create-child-entity-action.yml*

Сборка
-------

Для сборки docker образа с микросервисом выполните команду:

.. code-block:: bash

    ./mvnw -Pprod clean package jib:dockerBuild -Djib.docker.image.tag=custom 

После сборки вы можете запустить контейнер **ecos-demo-app:custom** с помощью docker.

Тестирование
--------------

Для запуска тестов вашего приложения, выполните:

.. code-block:: bash

    ./mvnw clean test

