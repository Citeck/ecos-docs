.. _OSGI:

Функционал загрузки OSGI пакетов
================================

Начиная с версии 1.16.0 в микросервис была добавлена возможность загружать кастомный код, реализованный согласно спецификации **OSGI** для пакетов. Это позволяет расширять микросервис без изменения базового функционала.

Загрузка самих пакетов производится через журнал **“OSGI пакеты”** в системных журналах. Чтобы загрузить пакет, переходим в этот журнал и нажимаем кнопку создания. Появляется модальное окно с предложением загрузки файла. Подкладываем туда свой скомпилированный jar файл и нажимаем **“Создать”**. Пакет загружен и проинсталлирован, если никаких проблем при инсталляции не возникло. В самом журнале всегда можно найти актуальный статус пакета, имя загруженного файла, символическое имя пакета, а так же, скачать сам jar файл пакета.

Что доступно “из коробки” при реализации нового пакета:

* **ApplicationContext ecos-integrations** микросервиса, но просто так с ним работать не получится, потому что пакеты не могут “переварить” зависимость от spring библиотек, поэтому в библиотеке **ecos-osgi-loader** была реализована обертка, принимающая в себя объект **ApplicationContext** и позволяющая получать из него бины

Полезные ссылки для реализации OSGI пакетов:

1. `http://java-online.ru/osgi.xhtml <http://java-online.ru/osgi.xhtml>`_ – Описание работы OSGI с подробными примерами реализации самих пакетов

2. `https://felix.apache.org/ <https://felix.apache.org/>`_  – Официальный сайт фреймворка Apache Felix, который был использован в качестве реализации спецификации OSGI

3. `https://felix.apache.org/documentation/subprojects/apache-felix-maven-bundle-plugin-bnd.html <https://felix.apache.org/documentation/subprojects/apache-felix-maven-bundle-plugin-bnd.html>`_ – Более подробное описание работы с плагином для создания OSGI пакетов.

При реализации пакетов можно не прописывать пакеты **Felix** и **OSGI Core** в свои проекты, а просто добавить зависимость на ecos-osgi-loader. Все необходимые библиотеки OSGI придут оттуда, как и обертка для работы с **ApplicationContext**.

Версия плагина для сборки пакетов: 5.1.1

Пример настроенного плагина:

.. code-block::

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

**Бандл** -  стандартный **jar файл** с добавлением в него **MANIFEST.MF** файла.

Чтобы получить подобную сборку, делаем следующее:

1.1. Указываем **packaging** свойство в **pom.xml** в значение **bundle**. Пример с контекстом:

.. code-block::

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

1.2. Указываем в области **build** следующий плагин (у меня получился довольно большой объем):

Тут стоит остановиться поподробнее на настройке этого плагина. Bundle имеет свой **ClassLoader**, зависящий от других бандлов. Для него не свойственны правила наследования ClassLoader'ов в Java. По этой причине, чтобы класс из какой-то либы был доступен в вашем бандле - его надо импортировать (а другой бандл, соответственно, должен его экспортировать). Если импорта не будет - произойдет **ClassNotFoundException** или **NoClassDefFoundError** в рантайме (в зависимости от контекста запроса к классу). Если импорт будет, но подобная зависимость не может быть найдена в фреймворке из других бандлов (ни один не экспортировал) - будет исключение о том, разрешения зависимостей (wiring) при старте бандла.

По комментариям в xml должно быть понятно что есть что. Опишу некоторые подводные камни.

Бывает ситуация, когда бандл при старте будет жаловаться на отсутствие зависимости, но вы только что загрузили эту зависимость в другом бандле (или эта зависимость есть в системном бандле). Данная проблема может быть из-за того, что зависимость экспортировалась без версии (или со стандартной версией ``1.0.0``) из-за отсутствия этой информации в рантайме при экспорте, а импорт требует, например, ``25.1.0``. Примером решения подобной проблемы - может быть указание минимальной поддерживаемой версии самостоятельно в манифесте. Для этого, вместо строки в импорте ``com.google.common.*`` пишем следующее: ``com.google.common.*; version="[1.0,26.0)"`` , что означает, что мы будем рады любой версии от 1.0.0 до 26.0.

1.3. Сама сборка после предыдущих приготовлений выполняется стандартной командой ``mvn clean package (install|deploy)``

2. Активатор
~~~~~~~~~~~~~~~~~~

**Активатор** - аналог main метода для бандла. Он вызывается при старте бандла и при его остановке (методы start и stop).

Либа из примера, используется для того, чтоб создать объекты, зарегистрировать их в микросервисе. Под регистрацией тут подразумевается - добавление по ключу **KONTUR** сервиса обработки событий **Diadoc** и **Kontur.EDI**. Таким образом, подключив бандл - можем пользоваться обработкой событий (и прочими фишками библиотеки) из микросервиса.

3. Загрузка в микросервис
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Заходим в **системные журналы → Журнал OSGI пакеты**. Загружаем через кнопку + свой бандл.

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
    
    Если вы получили ошибку, поправили бандл, загружаете новый бандл и получаете эту же ошибку - сделайте рестарт микросервиса интеграций после каждого неудачного старта бандла.

Способы расширения микросервиса интеграций с помощью бандлов
------------------------------------------------------------

1. Регистрация своего RecordsDao
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Подготовительная часть - импортировать зависимости records с помощью maven в своем бандле.

Импортировать пакеты в бандл (в конфиге):

.. code-block::

    kotlin.*,
    ecos.com.fasterxml.jackson210.*,
    ru.citeck.ecos.records2.*,
    ru.citeck.ecos.records3.*,
    ru.citeck.ecos.commons.*

Дальше - написать ``RecordsDao`` под свои потребности.

После написания - в ``BundleActivator`` можно получить с помощью ``ApplicationContextReflection`` бин класса ``RecordsService`` и вызываем у него метод **register**, передав свой ``RecordsDao``.

Теперь, запросы по указанному **sourceId** будут попадать в ваш ``RecordsDao``.

2. Регистрация новых команд
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Подготовительная часть - импортировать зависимости commands с помощью maven в своем бандле.

Импортировать пакеты в бандл (в конфиге):

.. code-block::

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

.. code-block::

 org.apache.camel.*

Дальше - в ``BundleActivator`` создать ``DefaultCamelContext``. Добавить в него необходимые маршруты. Запустить контекст.

Теперь у вас работает Camel в вашем бандле. Camel позволяет не только в рамках контекста обмениваться сообщениями, но и в рамках JVM, что может быть особенно полезно (direct-vm компонент).

Пока что возможности Camel вроде динамичного добавления ендпоинтов и тд не тестировались, но до кролика или иного сервиса (исходящий запрос) - очень даже удобно ходить.

4. Регистрация нового endpoint
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Добавляем зависимость: 

.. code-block::

    <dependency>
    <groupId>org.springframework</groupId>
    <artifactId>spring-webmvc</artifactId>
    <version>5.0.12.RELEASE</version>
    <scope>provided</scope>
    </dependency>

Добавляем в импорт пакеты:

.. code-block::

    org.springframework.web.*,
    org.springframework.http.*

В бандле создаем класс(ы) содержащий(ие) методы для обработки запросов. 

Возможные варианты реализации такого метода - использование `RequestEnitity  <https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/http/RequestEntity.html>`_, `ResponseEntity  <https://www.baeldung.com/spring-response-entity>`_, использование `@RequestBody  <https://www.baeldung.com/spring-request-response-body>`_, `пример  <https://www.logicbig.com/tutorials/spring-framework/spring-web-mvc/request-response-entity.html>`_.  Также методы могут принимать переменные пути запроса `@PathVariable  <https://www.baeldung.com/spring-pathvariable>`_ и переменные заголовка `@RequestHeader <https://www.baeldung.com/spring-rest-http-headers>`_.

В ``start`` методе активатора при помощи ``ApplicationContextReflection`` получаем ``RequestMappingHandlerMapping``, настраиваем ``RequestMappingInfo.BuilderConfiguration``, создаем ``RequestMappingInfo`` и регистрируем его в  ``RequestMappingHandlerMapping``. Пример для регистрации нового endpoint ``"ecos/message"``:

.. code-block::

    RequestMappingHandlerMapping requestMappingHandlerMapping = ApplicationContextReflection.getBean(RequestMappingHandlerMapping.class);
    handlerMapping = (AbstractHandlerMethodMapping) requestMappingHandlerMapping;

    RequestMappingInfo.BuilderConfiguration config = new RequestMappingInfo.BuilderConfiguration();
    config.setUrlPathHelper(requestMappingHandlerMapping.getUrlPathHelper());
    config.setPathMatcher(requestMappingHandlerMapping.getPathMatcher());
    config.setSuffixPatternMatch(requestMappingHandlerMapping.useSuffixPatternMatch());
    config.setTrailingSlashMatch(requestMappingHandlerMapping.useTrailingSlashMatch());
    config.setRegisteredSuffixPatternMatch(requestMappingHandlerMapping.useRegisteredSuffixPatternMatch());
    config.setContentNegotiationManager(requestMappingHandlerMapping.getContentNegotiationManager());

    RequestMappingInfo.Builder builder = RequestMappingInfo
                    .paths("ecos/message")
                    .methods(RequestMethod.POST)
                    .consumes(MediaType.APPLICATION_JSON_VALUE)
                    .produces(MediaType.APPLICATION_JSON_VALUE);

    RequestMappingInfo requestMappingInfo = builder.options(config).build();
    handlerMapping.registerMapping(requestMappingInfo, controller, DocumentController.class.getDeclaredMethod("postLoad", String.class, CreateDocsRequest.class));

В методе ``stop`` предусматриваем отключение endpoint при помощи вызова ``handlerMapping.unregisterMapping(info)``.

Для изменения записей в ECOS можно использовать ``RecordsService``. Есть следующие особенности при работе с сервисом через DTO:

* Создание ObjectData из DTO-объекта:

.. code-block::

 ObjectData targetAttributesData = ObjectData.create(dtoObject);

* Для использования псевдонима в свойствах можно использовать ``ecos.com.fasterxml.jackson210.annotation.JsonProperty``

.. code-block::

    @JsonProperty("nsdb_author")
    private String author;
    ...
    ObjectData targetAttributesData = ObjectData.create(dtoObject);

* Свойство с типом ``ASSOC: private RecordRef nsdb_counterparty``

.. code-block::

    ObjectData targetAttributesData = ObjectData.create();
    targetAttributesData.set("nsdb_counterparty", assocRecordRef);
    RecordAtts recordAtts = new RecordAtts(targetRecordRef, targetAttributesData);
    RecordRef result = recordsService.mutate(recordAtts);

* Свойство с типом ``CONTENT: private ObjectData nsdb_content``

.. code-block::

    ObjectData contentData = ObjectData.create();
    contentData.set("mimetype", "application/xml");
    contentData.set("filename", filename);
    contentData.set("base64content", base64content.getBytes());
    nsdb_content = contentData;

Возможные свойства для установки ``ru.citeck.ecos.records.source.alf.file.FileRepresentation``

* Ссылка на родителя из ASSOC

.. code-block::

    @AttName("_parent?id")
    RecordRef parentRef;

* Объявление свойства, которое базируется на атрибуте типа с двоеточием (cm:name, idocs:inn) 

.. code-block::

    @AttName("idocs:inn")
    private String inn;
    @AttName("idocs:fullOrganizationName")
    private String organizationName;

* Указание определенного alfresco-типа для родителя при создании записи

.. code-block::

    targetAttributesData.set(AlfNodeRecord.ATTR_TYPE, "dl:dataListItem");
    RecordAtts recordAtts = new RecordAtts(targetRecordRef, targetAttributesData);
    RecordRef result = recordsService.mutate(recordAtts);
    
где ``ru.citeck.ecos.records.source.alf.meta.AlfNodeRecord.ATTR_TYPE = “type“``

* Указать определенный тип связи между родителем и дочерней записью

.. code-block::

    targetAttributesData.set(RecordConstants.ATT_PARENT_ATT, "icase:documents");
    RecordAtts recordAtts = new RecordAtts(targetRecordRef, targetAttributesData);
    RecordRef result = recordsService.mutate(recordAtts);

где ``ru.citeck.ecos.records2.RecordConstants.ATT_PARENT_ATT = “_parentAtt“;``

Тестирование работоспособности методов можно проверить, реализовав в тесте интерфейсы ``RecordMutateDao``, ``RecordAttsDao``, ``RecordsQueryDao`` и имитировав работу ``RecordsService``, например:

.. code-block::

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

где **this** реализует ``RecordMutateDao``, ``RecordsQueryDao``.

Особенности
~~~~~~~~~~~~~~~~

Одновременное использование аннотаций JsonProperty и AttName приводит к тому, что при чтении DTO из RecordsService свойство не заполняется.

.. code-block::

    @JsonProperty("nsdb_author")
    @AttName("nsdb_author")
    private String author;
    ...
    RecsQueryRes<Dto> docRes = recordsService.query(query, Dto.class);
    ...
    System.out.println(queryResultDto.getAuthor());

Выведет на консоль null.