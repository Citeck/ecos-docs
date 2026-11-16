.. _OSGI:

Функционал загрузки OSGI пакетов
================================

.. note::

    Доступно только в Enterprise версии.

.. contents::
   :depth: 3

Начиная с версии 1.16.0 в микросервис была добавлена возможность загружать кастомный код, реализованный согласно спецификации **OSGI** для пакетов. Это позволяет расширять микросервис без изменения базового функционала.

В ecos-integrations 2.40.0-SNAPSHOT используются ``ecos-osgi-loader`` 3.1.0, OSGi Core 8.0.0, Apache Felix 7.0.5 и Camel 4.14.8. Зависимости бандла и импортируемые пакеты должны соответствовать целевой версии микросервиса.

Загрузка самих пакетов производится через журнал **OSGI пакеты** в разделе администратора. Чтобы загрузить пакет, переходим в этот журнал и нажимаем кнопку создания. Появляется модальное окно с предложением загрузки файла. Подкладываем туда свой скомпилированный jar файл и нажимаем **Создать**. Пакет загружен и проинсталлирован, если никаких проблем при инсталляции не возникло. В самом журнале всегда можно найти актуальный статус пакета, имя загруженного файла, символическое имя пакета, а так же, скачать сам jar файл пакета.

Что доступно "из коробки" при реализации нового пакета:

* **ApplicationContext ecos-integrations** передаётся OSGi-фабрике в свойстве ``SpringApplicationContext``. Для получения бинов используется обёртка ``ApplicationContextReflection`` из ``ecos-osgi-loader``. При обращении к Spring API необходимо согласовать версии и OSGi imports/exports: доступность библиотеки в микросервисе сама по себе не гарантирует её доступность бандлу.

Полезные ссылки для реализации OSGI пакетов:

1. `http://java-online.ru/osgi.xhtml <http://java-online.ru/osgi.xhtml>`_ – Описание работы OSGI с подробными примерами реализации самих пакетов

2. `https://felix.apache.org/ <https://felix.apache.org/>`_  – Официальный сайт фреймворка Apache Felix, который был использован в качестве реализации спецификации OSGI

3. `https://felix.apache.org/documentation/subprojects/apache-felix-maven-bundle-plugin-bnd.html <https://felix.apache.org/documentation/subprojects/apache-felix-maven-bundle-plugin-bnd.html>`_ – Более подробное описание работы с плагином для создания OSGI пакетов.

При реализации бандла используйте зависимости API, совместимые с целевым микросервисом. В самом ecos-integrations ``ecos-osgi-loader``, **Felix** и **OSGi Core** объявлены отдельными зависимостями. Состав транзитивных зависимостей проекта бандла проверяйте через ``mvn dependency:tree``. API, предоставляемые микросервисом, должны использовать те же классы, что и host; состав зависимостей со scope ``provided`` и экспортируемых пакетов проверяется для конкретной поставки.

В примере ниже используется версия плагина для сборки пакетов 5.1.1. Это пример настройки, а не требование к любой версии микросервиса.

Шаблон настройки плагина; имена активатора и пакеты импорта/экспорта замените значениями своего проекта:

.. code-block:: xml

    <plugin>
        <groupId>org.apache.felix</groupId>
        <artifactId>maven-bundle-plugin</artifactId>
        <version>5.1.1</version>
        <extensions>true</extensions>
        <configuration>
            <instructions>
                <Bundle-SymbolicName>${project.groupId}.test-spring-bundle</Bundle-SymbolicName>
                <Bundle-Name>${project.name}</Bundle-Name>
                <Bundle-Version>${project.version}</Bundle-Version>
                <Bundle-Activator>${project.groupId}.TestSpringAppActivator</Bundle-Activator>
                <Import-Package>org.osgi.framework.*</Import-Package>
                <Export-Package>org.apache.*, org.slf4j.*, ru.citeck.*, lombok.*</Export-Package>
            </instructions>
        </configuration>
    </plugin>

Пример создания бандла
-----------------------

В данной статье будет рассмотрено пошаговое создание бандла, а так же внедрение этого бандла в микросервис интеграций.

Пример, на котором рассмотрим - `ecos-edi-kontur-lib <https://gitlab.citeck.ru/citeck-projects/ecos-edi-kontur-lib/-/tree/develop>`_

1. Сборка
~~~~~~~~~~

**Бандл** — JAR-файл с OSGi-метаданными в ``META-INF/MANIFEST.MF``. Самого наличия manifest недостаточно: для загрузки нового пакета сервису требуется ``Bundle-SymbolicName``, а зависимости бандла должны разрешаться OSGi-фреймворком. Для бандла с активатором указывается ``Bundle-Activator``.

Чтобы получить подобную сборку, делаем следующее:

1.1. Указываем **packaging** свойство в **pom.xml** в значение **bundle**. Пример с контекстом:

.. code-block:: xml

    <project xmlns="http://maven.apache.org/POM/4.0.0"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    ...
        <groupId>ru.citeck.ecos</groupId>
        <artifactId>ecos-edi-kontur-lib</artifactId>
        <version>1.2.0-SNAPSHOT</version>
        <packaging>bundle</packaging>
    ...
    </project>

1.2. В разделе ``build/plugins`` добавляем ``maven-bundle-plugin`` по шаблону выше и настраиваем его для своего проекта.

Тут стоит остановиться поподробнее на настройке этого плагина. Bundle имеет свой **ClassLoader**, зависящий от других бандлов. Для него не свойственны правила наследования ClassLoader'ов в Java. По этой причине, чтобы класс из какой-то либы был доступен в вашем бандле - его надо импортировать (а другой бандл, соответственно, должен его экспортировать). Если импорта не будет - произойдет **ClassNotFoundException** или **NoClassDefFoundError** в рантайме (в зависимости от контекста запроса к классу). Если импорт будет, но подобная зависимость не может быть найдена в фреймворке из других бандлов (ни один не экспортировал) - будет исключение о том, разрешения зависимостей (wiring) при старте бандла.

При настройке импортов учитывайте не только имена пакетов, но и версии, экспортируемые целевым runtime.

Бандл может не стартовать, если пакет экспортируется в версии, не входящей в диапазон импорта. Например, ``com.google.common.*;version="[1.0,26.0)"`` задаёт диапазон от 1.0 включительно до 26.0 исключительно. Выбирайте диапазон по фактически совместимым версиям API; расширение диапазона само по себе не обеспечивает совместимость кода.

1.3. Сборка выполняется командой ``mvn clean package``. При необходимости установки в локальный Maven-репозиторий используйте ``mvn clean install``, для публикации — ``mvn clean deploy``.

2. Активатор
~~~~~~~~~~~~~~~~~~

**Активатор** - аналог main метода для бандла. Он вызывается при старте бандла и при его остановке (методы start и stop).

Либа из примера, используется для того, чтоб создать объекты, зарегистрировать их в микросервисе. Под регистрацией тут подразумевается - добавление по ключу **KONTUR** сервиса обработки событий **Diadoc** и **Kontur.EDI**. Таким образом, подключив бандл - можем пользоваться обработкой событий (и прочими фишками библиотеки) из микросервиса.

3. Загрузка в микросервис
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Заходим в **Рабочее пространство "Раздел администратора" → Журнал OSGI пакеты**. Загружаем через кнопку + свой бандл.

.. image:: _static/OSGI/OSGI_1.png
   :width: 600
   :align: center

Если все ок, увидим следующую картину:

.. image:: _static/OSGI/OSGI_2.png
   :width: 600
   :align: center

Важный факт, что статус - **ACTIVE**, это означает, что бандл зарезолвен, установлен и фреймворк его успешно стартанул.

Если есть ошибка загрузки - необходимо корректировать либо код, либо настройки бандла (импорт и экспорт).

Обязательно проверьте, что в рантайме нет ошибок при работе бандла. Как писалось выше, отсутствующие импорты могут привести к ошибкам рантайма.

.. important::
    
    При ошибке загрузки сначала проверьте логи установки, разрешение зависимостей и выполнение ``start``/``stop`` активатора. В ``stop`` освобождайте созданные ресурсы и снимайте регистрации, выполненные бандлом.

    При некоторых ошибках установки сервис пытается восстановить предыдущую версию бандла. Это не гарантирует очистку всех ресурсов после частично выполненного ``start``. Если после исправления и повторной загрузки сохраняется некорректное состояние runtime, может потребоваться перезапуск микросервиса; после каждой ошибки он не обязателен.

Сохранённые бандлы повторно устанавливаются после запуска микросервиса: установка планируется через 30 секунд после первого события обновления Spring-контекста.

Способы расширения микросервиса интеграций с помощью бандлов
------------------------------------------------------------

1. Регистрация своего RecordsDao
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Подготовительная часть - импортировать зависимости records с помощью maven в своем бандле.

Пример пакетов для импорта; окончательный список определяется используемой версией Records и экспортами OSGi runtime:

.. code-block:: text

    kotlin.*,
    ecos.com.fasterxml.jackson210.*,
    ru.citeck.ecos.records2.*,
    ru.citeck.ecos.records3.*,
    ru.citeck.ecos.commons.*

Дальше - написать ``RecordsDao`` под свои потребности.

``RecordRef`` и ``getRecordsServiceV1()`` используются в Records API, включая сервис из пакета ``records3``. Имя ``V1`` в getter не означает, что этот API необходимо автоматически заменить. Аналогично ``ecos.com.fasterxml.jackson210`` используется в предоставляемой библиотеке Records; пакет аннотаций должен соответствовать её JSON mapper.

После написания - в ``BundleActivator`` можно получить с помощью ``ApplicationContextReflection`` бин класса ``RecordsService`` и вызываем у него метод **register**, передав свой ``RecordsDao``.

Теперь, запросы по указанному **sourceId** будут попадать в ваш ``RecordsDao``.

2. Регистрация новых команд
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Подготовительная часть - импортировать зависимости commands с помощью maven в своем бандле.

Импортировать пакеты в бандл (в конфиге):

.. code-block:: text

    ecos.com.fasterxml.jackson210.*,
    kotlin.*,
    ru.citeck.ecos.commons.*,
    ru.citeck.ecos.commands.*

Дальше объявить свою ``CommandDto``, указать аннотацией ``@CommandType`` тип для нее. Создать ``CommandExecutor`` для этой dto.

После написания - в ``BundleActivator`` можно получить с помощью ``ApplicationContextReflection`` бин класса ``CommandsService`` и вызвать у него метод **addExecutor**, передав свою реализацию ``CommandExecutor``.

Теперь, команды с указанным типом будут попадать в ваш **CommandExecutor**.

3. Возможность работы с camel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

В основном пока что это используется для ЭДО-интеграций, но бывает проще использовать camel для некоторых вещей.

Чтобы его использовать - добавить зависимости camel, которые нужны с помощью maven в своем бандле.

Импортировать пакеты в бандл (в конфиге):

.. code-block:: text

    org.apache.camel.*

Дальше - в ``BundleActivator`` создать ``DefaultCamelContext``. Добавить в него необходимые маршруты. Запустить контекст.

Для Camel 4 нельзя использовать ``direct-vm``: компонент удалён при переходе на эту версию. Выбирайте поддерживаемый способ обмена с учётом того, находятся ли маршруты в одном контексте или в разных. ``direct`` не следует считать автоматической заменой межконтекстного обмена. См. `руководство миграции Camel 4 <https://camel.apache.org/manual/camel-4-migration-guide.html>`_.

Пока что возможности Camel вроде динамичного добавления ендпоинтов и тд не тестировались, но до кролика или иного сервиса (исходящий запрос) - очень даже удобно ходить.

4. Регистрация нового endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Добавляем зависимость ``spring-webmvc`` со scope ``provided``. Свойство ``spring-framework.version`` в примере должно быть задано в проекте бандла согласно версии Spring целевого микросервиса:

.. code-block:: xml

    <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>${spring-framework.version}</version>
    <scope>provided</scope>
    </dependency>

Добавляем в импорт пакеты:

.. code-block:: text

    org.springframework.web.*,
    org.springframework.http.*

В бандле создаем класс(ы) содержащий(ие) методы для обработки запросов. 

Возможные варианты реализации такого метода - использование `RequestEntity  <https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/http/RequestEntity.html>`_, `ResponseEntity  <https://www.baeldung.com/spring-response-entity>`_, использование `@RequestBody  <https://www.baeldung.com/spring-request-response-body>`_, `пример  <https://www.logicbig.com/tutorials/spring-framework/spring-web-mvc/request-response-entity.html>`_.  Также методы могут принимать переменные пути запроса `@PathVariable  <https://www.baeldung.com/spring-pathvariable>`_ и переменные заголовка `@RequestHeader <https://www.baeldung.com/spring-rest-http-headers>`_.

В ``start`` активатора получаем ``RequestMappingHandlerMapping`` через ``ApplicationContextReflection``. Для Spring MVC с поддержкой ``getBuilderConfiguration()`` используем конфигурацию действующего mapping, чтобы согласовать правила сопоставления путей. См. `API RequestMappingHandlerMapping <https://docs.spring.io/spring-framework/docs/6.2.x/javadoc-api/org/springframework/web/servlet/mvc/method/annotation/RequestMappingHandlerMapping.html>`_.

Ниже — фрагмент регистрации ``/ecos/message``. ``controller`` — экземпляр вашего контроллера с методом ``postLoad(String, CreateDocsRequest)``; ``CreateDocsRequest`` — DTO вашего проекта. ``handlerMapping`` и ``info`` сохраните в полях активатора для последующего удаления регистрации:

.. code-block:: java

    handlerMapping = ApplicationContextReflection.getBean(RequestMappingHandlerMapping.class);
    info = RequestMappingInfo
        .paths("/ecos/message")
        .methods(RequestMethod.POST)
        .consumes(MediaType.APPLICATION_JSON_VALUE)
        .produces(MediaType.APPLICATION_JSON_VALUE)
        .options(handlerMapping.getBuilderConfiguration())
        .build();

    handlerMapping.registerMapping(info, controller,
        controller.getClass().getDeclaredMethod("postLoad", String.class, CreateDocsRequest.class));

В методе ``stop`` предусматриваем отключение endpoint при помощи вызова ``handlerMapping.unregisterMapping(info)``.

Имя Spring-бина, доступность API из бандла и обработку параметров контроллера необходимо проверить на целевой поставке с используемой версией ``ecos-osgi-loader``.

Использование RecordsService через DTO
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Для изменения записей в Citeck можно использовать ``RecordsService``. Есть следующие особенности при работе с сервисом через DTO:

Создание ObjectData из DTO-объекта
""""""""""""""""""""""""""""""""""

.. code-block:: java

    ObjectData targetAttributesData = ObjectData.create(dtoObject);

Псевдоним свойства через JsonProperty
"""""""""""""""""""""""""""""""""""""

Для задания JSON-имени свойства при преобразовании DTO можно использовать ``ecos.com.fasterxml.jackson210.annotation.JsonProperty``, если этот пакет аннотаций соответствует версии JSON mapper вашей библиотеки Records/Commons. Это отличается от задания выражения Records-атрибута через ``@AttName`` при чтении DTO.

.. code-block:: java

    @JsonProperty("nsdb_author")
    private String author;
    ...
    ObjectData targetAttributesData = ObjectData.create(dtoObject);

Свойство с типом ASSOC
""""""""""""""""""""""

Свойство с типом ``ASSOC: private RecordRef nsdb_counterparty``

.. code-block:: java

    ObjectData targetAttributesData = ObjectData.create();
    targetAttributesData.set("nsdb_counterparty", assocRecordRef);
    RecordAtts recordAtts = new RecordAtts(targetRecordRef, targetAttributesData);
    RecordRef result = recordsService.mutate(recordAtts);

Свойство с типом CONTENT
""""""""""""""""""""""""

Следующий фрагмент относится к Alfresco-адаптеру и не является универсальным форматом CONTENT для всех источников Records. Набор полей и тип значения ``base64content`` необходимо согласовать с версией используемого адаптера.

Свойство с типом ``CONTENT: private ObjectData nsdb_content``

.. code-block:: java

    ObjectData contentData = ObjectData.create();
    contentData.set("mimetype", "application/xml");
    contentData.set("filename", filename);
    contentData.set("base64content", base64content.getBytes());
    nsdb_content = contentData;

Свойства FileRepresentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Далее приведены примеры для Alfresco-классов ``ru.citeck.ecos.records.source.alf.file.FileRepresentation`` и ``AlfNodeRecord``. Их наличие и импорт в бандле зависят от поставки Alfresco-модуля; эти классы не определяются самим ``ecos-records``.

Ссылка на родителя из ASSOC
""""""""""""""""""""""""""""

.. code-block:: java

    @AttName("_parent?id")
    RecordRef parentRef;

Свойство на основе атрибута с двоеточием в имени
""""""""""""""""""""""""""""""""""""""""""""""""

Объявление свойства, которое базируется на атрибуте типа с двоеточием (cm:name, idocs:inn)

.. code-block:: java

    @AttName("idocs:inn")
    private String inn;
    @AttName("idocs:fullOrganizationName")
    private String organizationName;

Указание alfresco-типа для родителя
""""""""""""""""""""""""""""""""""""

Указание определенного alfresco-типа для родителя при создании записи

.. code-block:: java

    targetAttributesData.set(AlfNodeRecord.ATTR_TYPE, "dl:dataListItem");
    RecordAtts recordAtts = new RecordAtts(targetRecordRef, targetAttributesData);
    RecordRef result = recordsService.mutate(recordAtts);

где ``ru.citeck.ecos.records.source.alf.meta.AlfNodeRecord.ATTR_TYPE = “type“``

Указание типа связи родитель-потомок
""""""""""""""""""""""""""""""""""""

Указать определенный тип связи между родителем и дочерней записью

.. code-block:: java

    targetAttributesData.set(RecordConstants.ATT_PARENT_ATT, "icase:documents");
    RecordAtts recordAtts = new RecordAtts(targetRecordRef, targetAttributesData);
    RecordRef result = recordsService.mutate(recordAtts);

где ``ru.citeck.ecos.records2.RecordConstants.ATT_PARENT_ATT = “_parentAtt“;``

Тестирование
^^^^^^^^^^^^^

Тестирование работоспособности методов можно проверить, реализовав в тесте интерфейсы ``RecordMutateDao``, ``RecordAttsDao``, ``RecordsQueryDao`` и имитировав работу ``RecordsService``, например:

.. code-block:: java

    RecordsServiceFactory recordsServiceFactory = new RecordsServiceFactory() {
        @Override
        protected RecordsProperties createProperties() {
            RecordsProperties properties = super.createProperties();
                properties.setAppInstanceId("162037");
                properties.setAppName("alfresco");
                return properties;
            }
        };
    recordsServiceFactory.getRecordsServiceV1().register(this);
    RecordsService recordsService = recordsServiceFactory.getRecordsServiceV1();

В этом фрагменте **this** — тестовый DAO, реализующий необходимые для сценария интерфейсы из используемой версии Records API. Сам ``getRecordsServiceV1()`` возвращает сервис ``ru.citeck.ecos.records3.RecordsService``.

Особенности
~~~~~~~~~~~~~~~~

.. warning::

    ``JsonProperty`` задаёт имя свойства при JSON-преобразовании, а ``AttName`` — выражение атрибута для схемы Records. При несовпадении alias схемы и ожидаемого JSON-имени свойство может не заполниться. Результат зависит от структуры DTO, расположения аннотаций и версии mapper; общего правила «любое сочетание даёт null» нет.

    Например, следующее сочетание требует проверки на используемой версии:

    .. code-block:: java

        @JsonProperty("nsdb_author")
        @AttName("nsdb_author")
        private String author;
        ...
        RecsQueryRes<Dto> docRes = recordsService.query(query, Dto.class);
        ...
        if (!docRes.getRecords().isEmpty()) {
            System.out.println(docRes.getRecords().get(0).getAuthor());
        }

    Проверьте схему запроса и десериализацию результата. Для DTO чтения используйте ``AttName`` с согласованным alias, для DTO записи через ``ObjectData`` — JSON-имена, соответствующие mapper. При разных требованиях к чтению и записи используйте отдельные DTO.
