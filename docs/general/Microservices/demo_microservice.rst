Демо микросервис
===================

.. _demo_microservice:

.. contents:: 
   :depth: 2

Репозиторий `ecos-demo-app <https://github.com/Citeck/ecos-demo-app>`_ содержит приложение, демонстрирующее возможности Citeck.

Вы можете познакомиться с:

    - пользовательским :ref:`RecordsDAO<new_RecordsDAO>`;
    - работой с :ref:`RecordsService<ecos_RecordsService>`;
    - :ref:`действиями<ui_actions>`;
    - :ref:`командами<ecos_commands>`;
    - :ref:`событиями<ecos_events>`;
    - бизнес-процессом с  :ref:`Внешней задачей<ecos_bpmn_external_task>`;
    - созданием :ref:`дочерних ассоциаций<datatypes_associations>`.

См. подробнее про :ref:`артефакты Citeck<ecos_artifacts>`, :ref:`приложения<applications>`, :ref:`разработку и создание микросервисов<service_develop_setup>`.

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

.. code-block:: text

    ./mvnw spring-boot:run

Если ваша IDE поддерживает запуск приложений Spring Boot напрямую, вы можете легко запустить класс ru.citeck.ecos.webapp.demo.EcosDemoApp без дополнительной настройки.

Сценарий
-----------

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

.. code-block:: text

    ./mvnw -Pprod clean package jib:dockerBuild -Djib.docker.image.tag=custom 

После сборки вы можете запустить контейнер **ecos-demo-app:custom** с помощью docker.

Тестирование
--------------

Для запуска тестов вашего приложения, выполните:

.. code-block:: text

    ./mvnw clean test


Примеры
---------

.. raw:: html

   <details>
   <summary><a>Как задать DTO</a></summary>

.. code-block:: js

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

.. raw:: html

   </details>
   <details>
   <summary><a>Как задать команду</a></summary>

Например, вызвать созданное выше DTO и вывести его в консоль:

.. code-block:: js

    public Object execute (SimpleDto SimpleDto ) {
            log.info("Command received: " + SimpleDto);
            return null;
        }

.. raw:: html

   </details>
   <details>
   <summary><a>Как вызвать действие</a></summary>

.. code-block:: js

    let rec = Records.getRecordToEdit('ecos-simple-app/send-simple-email@');
    rec.att('entityRef', 'emodel/simple-type@629fbd31-788a-4232-9de9-d737e5b07795'); // any EntityRef
    rec.att('comment', 'any comment');
    await rec.save();

где 

* **ecos-simple-app** - наименование приложения
* **send-simple-email** - идентификатор RecordsDAO. Используется для определения того, какой DAO должен обрабатывать запрос на мутацию.
* **EntityRef** - уникальный идентификатор сущности в системе Citeck. 