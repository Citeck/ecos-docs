===============
Сервисы Docker
===============

onlyoffice-ds-app
-----------------

Назначение:
~~~~~~~~~~~
Образ, включающий набор инструментов для развертывания onlyoffice-ds

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
*onlyoffice-ds:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    container_name: onlyoffice-ds
    hostname: onlyoffice-ds
    image: onlyoffice/documentserver:latest
    restart: unless-stopped
    stop_grace_period: 1m
    networks:
      - app_network
    expose:
      - '80'
      - '443'
    volumes:
      - /opt/onlyoffice/document_data:/var/www/onlyoffice/Data
      - /opt/onlyoffice/document_log:/var/log/onlyoffice
      - /opt/onlyoffice/document_fonts:/usr/share/fonts/truetype/custom
      - /opt/onlyoffice/document_forgotten:/var/lib/onlyoffice/documentserver/App_Data/cache/files/forgotten

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

onlyoffice-ds               |  * Starting PostgreSQL 10 database server

onlyoffice-ds               |    ...done.

onlyoffice-ds               |  * Starting RabbitMQ Messaging Server rabbitmq-server

onlyoffice-ds               |    ...done.

onlyoffice-ds               | Starting redis-server: redis-server.

onlyoffice-ds               | Starting supervisor: supervisord.

onlyoffice-ds               |  * Starting periodic command scheduler cron

onlyoffice-ds               |    ...done.

onlyoffice-ds               |  * Starting nginx nginx

onlyoffice-ds               |    ...done.

onlyoffice-ds               | Generating AllFonts.js, please wait...Done

onlyoffice-ds               | Generating presentation themes, please wait...Done

onlyoffice-ds               | ds:docservice: stopped

onlyoffice-ds               | ds:docservice: started

onlyoffice-ds               | ds:converter: stopped

onlyoffice-ds               | ds:converter: started

onlyoffice-ds               |  * Reloading nginx configuration nginx

onlyoffice-ds               |    ...done.

onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/converter/err.log <==

onlyoffice-ds               | 

onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/converter/out.log <==

onlyoffice-ds               | [2020-05-14T20:35:52.505] [WARN] nodeJS - update cluster with 1 workers

onlyoffice-ds               | [2020-05-14T20:36:27.586] [WARN] nodeJS - update cluster with 1 workers

onlyoffice-ds               | [2020-05-14T20:36:27.604] [WARN] nodeJS - worker 903 started.

onlyoffice-ds               | [2020-05-14T20:36:27.605] [WARN] nodeJS - update cluster with 1 workers

onlyoffice-ds               | [2020-05-15T09:48:03.094] [WARN] nodeJS - update cluster with 1 workers

onlyoffice-ds               | [2020-05-15T09:48:03.125] [WARN] nodeJS - worker 861 started.

onlyoffice-ds               | [2020-05-15T09:48:03.126] [WARN] nodeJS - update cluster with 1 workers

onlyoffice-ds               | [2020-05-15T09:48:35.735] [WARN] nodeJS - update cluster with 1 workers

onlyoffice-ds               | [2020-05-15T09:48:35.746] [WARN] nodeJS - worker 926 started.

onlyoffice-ds               | [2020-05-15T09:48:35.748] [WARN] nodeJS - update cluster with 1 workers

onlyoffice-ds               | 

onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/docservice/err.log <==

onlyoffice-ds               | 

onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/docservice/out.log <==

onlyoffice-ds               | [2020-05-14T20:36:05.671] [WARN] nodeJS - error description: docId = 0a2955d7-9505-421b-8e14-4bfaa68d994a_1.0 errorId = Other error

onlyoffice-ds               | [2020-05-14T20:36:26.944] [WARN] nodeJS - Express server starting...

onlyoffice-ds               | [2020-05-14T20:36:26.947] [WARN] nodeJS - Plugins watch exception (https://nodejs.org/docs/latest/api/fs.html#fs_availability).

onlyoffice-ds               | [2020-05-14T20:36:27.185] [WARN] nodeJS - Express server listening on port 8000 in production-linux mode

onlyoffice-ds               | [2020-05-15T09:48:04.094] [WARN] nodeJS - Express server starting...

onlyoffice-ds               | [2020-05-15T09:48:04.100] [WARN] nodeJS - Plugins watch exception (https://nodejs.org/docs/latest/api/fs.html#fs_availability).

onlyoffice-ds               | [2020-05-15T09:48:04.354] [WARN] nodeJS - Express server listening on port 8000 in production-linux mode

onlyoffice-ds               | [2020-05-15T09:48:34.897] [WARN] nodeJS - Express server starting...

onlyoffice-ds               | [2020-05-15T09:48:34.901] [WARN] nodeJS - Plugins watch exception (https://nodejs.org/docs/latest/api/fs.html#fs_availability).

onlyoffice-ds               | [2020-05-15T09:48:35.083] [WARN] nodeJS - Express server listening on port 8000 in production-linux mode

onlyoffice-ds               | 

onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/gc/err.log <==

onlyoffice-ds               | 

onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/gc/out.log <==

onlyoffice-ds               | 

onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/metrics/err.log <==

onlyoffice-ds               | 

onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/metrics/out.log <==

onlyoffice-ds               |   gauges: { 'statsd.timestamp_lag': 0 },

onlyoffice-ds               |   timer_data: {},

onlyoffice-ds               |   counter_rates:

onlyoffice-ds               |    { 'statsd.bad_lines_seen': 0,

onlyoffice-ds               |      'statsd.packets_received': 0,

onlyoffice-ds               |      'statsd.metrics_received': 0 },

onlyoffice-ds               |   sets: {},

onlyoffice-ds               |   pctThreshold: [ 90 ] }

onlyoffice-ds               | 15 May 09:48:02 - [796] reading config file: ./config/config.js

onlyoffice-ds               | 15 May 09:48:02 - server is up INFO

ecos-gateway-app
----------------
Назначение:
~~~~~~~~~~
Образ одного из центральных компонентов микросервисной архитектуры. Приложение реализует API шлюз взаимодействия с остальными микросервисами

Теги:
~~~~~

`Nexus_gateway <http://nexus.citeck.ru/ecos-gateway:>`_<tag> - сборка проекта ecos-gateway 

Базовые образы:
~~~~~~~~~~~~~~~

**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gateway-app:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    image: nexus.citeck.ru/ecos-gateway:<GATEWAY_APP_IMAGE
    container_name: gateway-app
    hostname: gateway-app
    restart: unless-stopped
    stop_grace_period: 1m
    environment:
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - _JAVA_OPTIONS=-Xmx512m -Xms256m
      - SPRING_PROFILES_ACTIVE=prod,swagger
      - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
      - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/config
      - SPRING_DATASOURCE_URL=jdbc:postgresql://micro-postgresql:5432/gateway
      - JHIPSTER_SLEEP=30 # gives time for the JHipster Registry to boot before the application
    expose:
      - 8085/tcp
    networks:
      - app_network
    depends_on:
      - jhipster-registry
      - micro-postgresql
  micro-postgresql:
    image: postgres:10.4
    container_name: micro-postgresql
    hostname: micro-postgresql
    restart: unless-stopped
    stop_grace_period: 1m
    environment:
      - POSTGRES_USER=gateway
      - POSTGRES_PASSWORD=
    networks:
      - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~

*	**_JAVA_OPTIONS** - параметры для **jvm**
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**
*	**SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**
*	**JHIPSTER_SLEEP **- **таймаут** перед развертыванием микросервиса

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	cloud config и eureka load balancer используют один и тот же пароль

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gateway-app                 | ----------------------------------------------------------
gateway-app                 |   Application 'gateway' is running! Access URLs:
gateway-app                 |   Local:          http://localhost:8085/
gateway-app                 |   External:       http://172.25.0.22:8085/
gateway-app                 |   Profile(s):     [prod, swagger]
gateway-app                 | ----------------------------------------------------------
gateway-app                 | 2020-05-13 07:17:43.131  INFO 1 --- [           main] ru.citeck.ecos.GatewayApp                : 
gateway-app                 | ----------------------------------------------------------
gateway-app                 |   Config Server:  Connected to the JHipster Registry running in Docker
gateway-app                 | ----------------------------------------------------------


ecos-notifications-app
----------------------

Назначение:
~~~~~~~~~~~
Образ микросервиса рассылки нотификаций

Базовые образы:
~~~~~~~~~~~~~~~
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
notifications-app:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    image: nexus.citeck.ru/ecos-notifications:<NOTIFICATIONS_APP_IMAGE
    container_name: notifications-app
    hostname: notifications-app
    restart: unless-stopped
    stop_grace_period: 1m
    depends_on:
      - notifications-postgresql
    environment:
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - _JAVA_OPTIONS=-Xmx256m -Xms256m
      - SPRING_PROFILES_ACTIVE=prod,swagger
      - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
      - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/config
      - SPRING_DATASOURCE_URL=jdbc:postgresql://notifications-postgresql:5432/notifications
      - JHIPSTER_SLEEP=140 # gives time for the JHipster Registry to boot before the application
      - ECOS-NOTIFICATIONS_EVENT_HOST=<ECOS-NOTIFICATIONS_EVENT_HOST
      - ECOS-NOTIFICATIONS_EVENT_PORT=<ECOS-NOTIFICATIONS_EVENT_PORT
      - ECOS-NOTIFICATIONS_EVENT_USERNAME=<ECOS-NOTIFICATIONS_EVENT_USERNAME
      - ECOS-NOTIFICATIONS_EVENT_PASSWORD=<ECOS-NOTIFICATIONS_EVENT_PASSWORD
      - ECOS-NOTIFICATIONS_ALFRESCO_URL=<ECOS-NOTIFICATIONS_ALFRESCO_URL
      - ECOS-NOTIFICATIONS_ALFRESCO_AUTHENTICATION_USERNAME=<ECOS-NOTIFICATIONS_ALFRESCO_AUTHENTICATION_USERNAME
      - ECOS-NOTIFICATIONS_ALFRESCO_AUTHENTICATION_PASSWORD=<ECOS-NOTIFICATIONS_ALFRESCO_AUTHENTICATION_PASSWORD
    ports:
      - 8013:8013
    volumes:
      - /opt/alfresco/logs/notifications:/tmp
      - /opt/micro/credentials:/credentials
    networks:
      - app_network
  # NOTIFICATIONS PSQL
  notifications-postgresql:
    image: postgres:10.4
    container_name: notifications-postgresql
    hostname: notifications-postgresql
    restart: unless-stopped
    stop_grace_period: 1m
    environment:
      - POSTGRES_USER=notifications
    volumes:
      - /opt/micro/postgresql/notifications:/var/lib/postgresql/data
    networks:
      - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~
*	**_JAVA_OPTIONS** - параметры для **jvm**
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**
*	**SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**
*	**JHIPSTER_SLEEP **- **таймаут** перед развертыванием микросервиса
*	**ECOS-NOTIFICATIONS_EVENT_HOST** - fqdn/ip диспетчера очередей rabbitmq
*	**ECOS-NOTIFICATIONS_EVENT_PORT** - amqp порт диспетчера очередей rabbitmq
*	**ECOS-NOTIFICATIONS_EVENT_USERNAME** - пользователь диспетчера очередей rabbitmq
*	**ECOS-NOTIFICATIONS_EVENT_PASSWORD** - пароль диспетчера очередей rabbitmq
*	**ECOS-NOTIFICATIONS_ALFRESCO_URL** - fqdn развернутого приложения ecos
*	**ECOS-NOTIFICATIONS_ALFRESCO_AUTHENTICATION_USERNAME** - пользователь в ecos для интеграции с микросервисом нотификации
*	**ECOS-NOTIFICATIONS_ALFRESCO_AUTHENTICATION_PASSWORD** - пароль пользователя в ecos для интеграции с микросервисом нотификации

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	cloud config и eureka load balancer используют один и тот же пароль
*	Монтирование firebase credentials как волюма
*	Часть app properties (ECOS-NOTIFICATIONS*) нужно вынести в spring cloud config

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

notifications-app           | ----------------------------------------------------------
notifications-app           |   Application 'notifications' is running! Access URLs:
notifications-app           |   Local:          http://localhost:8013/
notifications-app           |   External:       http://172.26.0.22:8013/
notifications-app           |   Profile(s):     [prod, swagger]
notifications-app           | ----------------------------------------------------------
notifications-app           | 2020-05-14 05:59:30.204  INFO 1 --- [           main] r.c.ecos.notifications.NotificationsApp  : 
notifications-app           | ----------------------------------------------------------
notifications-app           |   Config Server:  Connected to the JHipster Registry running in Docker
notifications-app           | ----------------------------------------------------------

ecos-mongo-app
--------------

Назначение:
~~~~~~~~~~~
Образ для развертывания контейнера с mongodb с преконфигурированными настройками датасорсов для микросервисов

Базовые образы:
~~~~~~~~~~~~~~~
*	`mongo_4 <https://hub.docker.com/layers/mongo/library/mongo/4.0/images/sha256-ccd97bd444338973ac143a22753e6b73a3e707a6a3edd512311a418a3e432cdb?context=explore>`_ - Официальный образ mongodb v 4.0.x

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
mongo-app:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    container_name: mongo-app
    hostname: mongo-app
    restart: unless-stopped
    stop_grace_period: 1m
    image: nexus.citeck.ru/mongo:4.0
    env_file:
     - ./env_dir/mongo-app.env
    expose:
      - 27017/tcp
    volumes:
      - /opt/mongo-app:/data/db/
    networks:
      - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~

*	**MONGO_INITDB_ROOT_USERNAME** - логин пользователя, который будет создан в **admin db с root** привилегиями
*	**MONGO_INITDB_ROOT_PASSWORD** - пароль привилегированного пользователя
*	**MONGO_INITDB_DATABASE** - определение базы данных, используемой в скриптах развертывания в /docker-entrypoint-initdb.d/*.js/sh. Для понимания:
This variable allows you to specify the name of a database to be used for creation scripts in /docker-entrypoint-initdb.d/*.js (see Initializing a fresh instance below). MongoDB is fundamentally designed for "create on first use", so if you do not insert data with your JavaScript files, then no database is created.
*	**ECOS_HISTORY_APP_DATASOURCE_DATABASE** - db микросервиса истории **(ecos-history)**
*	**ECOS_HISTORY_APP_DATASOURCE_USERNAME** - логин для мкр истории, роль dbOwner **(ecos-history)**
*	**ECOS_HISTORY_APP_DATASOURCE_PASSWORD** - пароль для мкр истории **(ecos-history-password)**
*	**ECOS_PROCESS_APP_DATASOURCE_DATABASE** - db микросервиса ecos-process **(ecos-process)**
*	**ECOS_PROCESS_APP_DATASOURCE_USERNAME **- логин для мкр ecos-process, роль dbOwner **(ecos-process)**
*	**ECOS_PROCESS_APP_DATASOURCE_PASSWORD** - пароль для мкр ecos-process **(ecos-process-password)**

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
2020-05-06T07:44:14.752+0000 I STORAGE [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
2020-05-06T07:44:14.752+0000 I STORAGE [initandlisten] ** See `mongo_prodnotes_filesystem <http://dochub.mongodb.org/core/prodnotes-filesystem>`_ 

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

MongoDB shell version v4.0.18
connecting to: mongodb://127.0.0.1:27017/test?gssapiServiceName=mongodb
2020-05-06T07:44:13.565+0000 I NETWORK  [listener] connection accepted from 127.0.0.1:42378 #3 (1 connection now open)
2020-05-06T07:44:13.565+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:42378 conn3: { application: { name: "MongoDB Shell" }, driver: { name: "MongoDB Internal Client", version: "4.0.18" }, os: { type: "Linux", name: "Ubuntu", architecture: "x86_64", version: "16.04" } }
Implicit session: session { "id" : UUID("3cb7f158-dfaa-4ffd-896f-b36052828f19") }
MongoDB server version: 4.0.18
2020-05-06T07:44:13.593+0000 I ACCESS   [conn3] Successfully authenticated as principal root_user on admin from client 127.0.0.1:42378
1
ecos-process
Successfully added user: {
        "user" : "ecos-process",
        "roles" : [
                {
                        "role" : "dbOwner",
                        "db" : "ecos-process"
                }
        ]
}
ecos-history
Successfully added user: {
        "user" : "ecos-history",
        "roles" : [
                {
                        "role" : "dbOwner",
                        "db" : "ecos-history"
                }
        ]
}
bye

mailhog-app
-----------

Назначение:
~~~~~~~~~~~
Образ инструмента для e-mail тестирования

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mailhog:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    restart: unless-stopped
    stop_grace_period: 1m
    container_name: mailhog
    hostname: mailhog
    expose:
      - 8025/tcp
    environment:
      - MH_UI_WEB_PATH=mailhog
    image: mailhog/mailhog
    networks:
      - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~
*	**MH_UI_WEB_PATH** - web path для использования mailhog за проксирующим ecos-proxy (mailhog)

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

mailhog                     | [HTTP] Binding to address: 0.0.0.0:8025
mailhog                     | 2020/05/14 06:43:07 Using in-memory storage
mailhog                     | 2020/05/14 06:43:07 [SMTP] Binding to address: 0.0.0.0:1025
mailhog                     | 2020/05/14 06:43:07 Serving under http://0.0.0.0:8025/mailhog/
mailhog                     | Creating API v1 with WebPath: /mailhog
mailhog                     | Creating API v2 with WebPath: /mailhog

ecos-registry-app
-----------------

Назначение:
~~~~~~~~~~~
Образ одного из центральных компонентов микросервисной архитектуры. Приложение объединяет eureka REST сервис (load balancing, registering, service discovery) и Spring Cloud Config server для централизации конфигурации.

Теги:
~~~~~
jhipster/jhipster-registry:v4.1.1 - официальный образ

 `nexus_ecos_registry <http://nexus.citeck.ru/ecos-registry:>`_  - собственная сборка

Базовые образы:
~~~~~~~~~~~~~~~
openjdk:8-jre-alpine - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
jhipster-registry:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    image: jhipster/jhipster-registry:<JHIPSTER_APP_IMAGE
    container_name: jhipster-registry
    hostname: jhipster-registry
    restart: unless-stopped
    stop_grace_period: 1m
    volumes:
      - /opt/micro/central-server-config:/central-config
    environment:
      - _JAVA_OPTIONS=-Xmx512m -Xms256m -Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.port=10004 -Dcom.sun.management.jmxremote.authenticate=true -Dcom.sun.management.jmxremote.access.file=/central-config/jmxremote.access -Dcom.sun.management.jmxremote.password.file=/central-config/jmxremote.password -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.rmi.port=10004  -Djava.rmi.server.hostname=<HOST_IP
      - SPRING_PROFILES_ACTIVE=dev,swagger
      - SPRING_SECURITY_USER_PASSWORD=alfr3sc0
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - SPRING_CLOUD_CONFIG_SERVER_COMPOSITE_0_TYPE=native
      - SPRING_CLOUD_CONFIG_SERVER_COMPOSITE_0_SEARCH_LOCATIONS=file:/central-config/docker-config/
    expose:
      - 8761/tcp
      - 10004/tcp
    networks:
      - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~
*	**_JAVA_OPTIONS** - параметры для jvm
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**SPRING_SECURITY_USER_PASSWORD** - пароль пользователя для аутентификации в cloud config
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
*	Документация по `spring cloud config <https://cloud.spring.io/spring-cloud-config/reference/html/#_spring_cloud_config_server>`_

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
*	Требуется закончить переход на ecos-registry проект
*	Утилизации цпу
*	Требуется конфигурация registry как экспортера метрик микросервисов в Prometheus
*	Использование localPath расположения конфигурационного файла
*	Не реализован доступ к ui registry через location
*	Не используется JWT token

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
jhipster-registry                    | ----------------------------------------------------------
jhipster-registry                    |  Application 'jhipster-registry' is running! Access URLs:
jhipster-registry                    |  Local:          http://localhost:8761
jhipster-registry                    |  External:       http://172.18.0.11:8761
jhipster-registry                    |  Profile(s):     [composite, dev, swagger]
jhipster-registry                    | ----------------------------------------------------------
jhipster-registry                    | 2020-04-28 20:35:36.017  INFO 1 --- [           main] i.g.j.registry.JHipsterRegistryApp       : 
jhipster-registry                    | ----------------------------------------------------------
jhipster-registry                    |  Config Server:  Connected to the JHipster Registry running in Docker
jhipster-registry                    | ----------------------------------------------------------

ecos-postgresql-app
-------------------
Назначение:
~~~~~~~~~~~
Образ, собранный на официальном образе postgresql 9.4.x с добавлением скрипта инициализации баз данных и пользователей

Теги:
~~~~~
`nexus_alpine <http://nexus.citeck.ru/ecos-postgres:9.4-alpine>`_

Базовые образы:
~~~~~~~~~~~~~~~
postgres:9.4-alpine - официальный образ postgresql 9.4.x на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
ecos-postgresql:
    container_name: ecos-postgresql
    restart: unless-stopped
    ports:
      - 127.0.0.1:50432:5432/tcp
    environment:
      - POSTGRES_PASSWORD=alfr3sc0
      - DB_NAME=alfresco
      - FLOWABLE_DBNAME=alf_flowable
      - HISTORY_DBNAME=history_service
      - CASE_MODEL_DBNAME=alfresco_case_model
    hostname: ecos-postgresql
    image: nexus.citeck.ru/ecos-postgres:9.4-alpine
    stop_grace_period: 1m
    volumes:
      - /opt/alfresco/postgresql/:/var/lib/postgresql/data
    networks:
      - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~

*	**POSTGRES_PASSWORD **- обязательный параметр за исключением 
*   **POSTGRES_HOST_AUTH_METHOD=trust**, пароль рутового пользователя
*	**POSTGRES_USER** - переопределение дефолтного пользователя **postgres**
*	**POSTGRES_DB **- переопределение дефолтной базы данных
*	**POSTGRES_INITDB_ARGS** - дополнительные параметры для инициализации кластера
*	**POSTGRES_INITDB_WALDIR** - переопределение дефолтной директории хранения логов транзакций
*	**POSTGRES_HOST_AUTH_METHOD** - метод аутентификации host подключений для всех бд, пользователей и адресов в **pg_hba.conf**. Дефолтное значение **md5**
*	**PGDATA** - переопределение дефолтной директории хранения фалов инициируемого кластера
*	**DB_NAME** - определение базы данных **ecos**
*	**DB_USERNAME** - определение пользователя для базы данных **ecos/flowable/ecos-history**
*	**DB_PASSWORD** - пароль создаваемого пользователя
*	**FLOWABLE_DBNAME** - определение базы данных **flowable**
*	**HISTORY_DBNAME** - определение базы данных для ecos-history-app (устаревший параметр, базы данных мкр вынесены в отдельный инстанс)
*	**CASE_MODEL_DBNAME** - определение базы данных **ecos-case-model-app**

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
*	EOL версии postgresl
*	Используется один пользователь для баз данных
*	Отсутствие конфигурации postgresql.conf, pg_hba.conf
*	Отсутствие конфигурации используемых схем

Типовой вывод принятых настроек в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The files belonging to this database system will be owned by user "postgres".
This user must also own the server process.

The database cluster will be initialized with locale "en_US.utf8".
The default database encoding has accordingly been set to "UTF8".
The default text search configuration will be set to "english".

Data page checksums are disabled.

fixing permissions on existing directory /var/lib/postgresql/data ... ok
creating subdirectories ... ok
selecting default max_connections ... 100
selecting default shared_buffers ... 128MB
selecting default timezone ... UTC
selecting dynamic shared memory implementation ... posix
creating configuration files ... ok
creating template1 database in /var/lib/postgresql/data/base/1 ... ok
initializing pg_authid ... ok
setting password ... ok
initializing dependencies ... ok
creating system views ... ok
loading system objects' descriptions ... ok
creating collations ... sh: locale: not found
ok
No usable system locales were found.
Use the option "--debug" to see details.
creating conversions ... ok
creating dictionaries ... ok
setting privileges on built-in objects ... ok
creating information schema ... ok
loading PL/pgSQL server-side language ... ok
vacuuming database template1 ... ok
copying template1 to template0 ... ok
copying template1 to postgres ... ok
syncing data to disk ... ok

Success. You can now start the database server using:

    postgres -D /var/lib/postgresql/data
or
    pg_ctl -D /var/lib/postgresql/data -l logfile start


WARNING: enabling "trust" authentication for local connections
You can change this by editing pg_hba.conf or using the option -A, or
--auth-local and --auth-host, the next time you run initdb.

WARNING: No password has been set for the database.
         This will allow anyone with access to the
         Postgres port to access your database. In
         Docker's default configuration, this is
         effectively any other container on the same
         system.

         Use "-e POSTGRES_PASSWORD=password" to set
         it in "docker run".

waiting for server to start....LOG:  database system was shut down at 2020-04-27 23:16:37 UTC
LOG:  MultiXact member wraparound protections are now enabled
LOG:  database system is ready to accept connections
LOG:  autovacuum launcher started
 done
server started

/usr/local/bin/docker-entrypoint.sh: sourcing /docker-entrypoint-initdb.d/initDBs.sh
CREATE ROLE
CREATE DATABASE
CREATE DATABASE
CREATE DATABASE
CREATE DATABASE
CREATE EXTENSION
CREATE EXTENSION

waiting for server to shut down....LOG:  received fast shutdown request
LOG:  aborting any active transactions
LOG:  autovacuum launcher shutting down
LOG:  shutting down
LOG:  database system is shut down
 done
server stopped

PostgreSQL init process complete; ready for start up.

LOG:  database system was shut down at 2020-04-27 23:16:40 UTC
LOG:  MultiXact member wraparound protections are now enabled
LOG:  database system is ready to accept connections
LOG:  autovacuum launcher started

ecos-model-app
--------------

Назначение:
~~~~~~~~~~~
Образ микросервиса, предназначенного для хранения и работы с такими сущностями как: тип(type), раздел(section), ассоциация(association), действие(action)

Базовые образы:
~~~~~~~~~~~~~~~
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
emodel-app:
    container_name: emodel-app
    restart: unless-stopped
    stop_grace_period: 1m
    image: nexus.citeck.ru/ecos-model:<ECOS_MODEL_IMAGE
    expose:
      - 8094/tcp
    environment:
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - _JAVA_OPTIONS=-Xmx256m -Xms256m
      - SPRING_PROFILES_ACTIVE=dev,swagger
      - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
      - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/config
      - SPRING_DATASOURCE_URL=jdbc:postgresql://emodel-postgresql:5432/emodel
      - ECOS_INIT_DELAY=120
    networks:
      - app_network
    depends_on:
      - emodel-postgresql
  emodel-postgresql:
    restart: unless-stopped
    stop_grace_period: 1m
    container_name: emodel-postgresql
    image: postgres:10.4
    environment:
      - POSTGRES_USER=emodel
      - POSTGRES_PASSWORD=
    volumes:
      - /opt/micro/postgresql/emodel:/var/lib/postgresql/data
    networks:
      - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~
*	**_JAVA_OPTIONS** - параметры для **jvm**
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**
*	**SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**
*	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	cloud config и eureka load balancer используют один и тот же пароль

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

emodel-app                  | ----------------------------------------------------------
emodel-app                  |   Application 'emodel' is running! Access URLs:
emodel-app                  |   Local:          http://localhost:8094/
emodel-app                  |   External:       http://172.25.0.26:8094/
emodel-app                  |   Profile(s):     [dev, swagger]
emodel-app                  | ----------------------------------------------------------
emodel-app                  | 2020-05-13 09:04:16.415  INFO 1 --- [           main] ru.citeck.ecos.model.EcosModelApp        : 
emodel-app                  | ----------------------------------------------------------
emodel-app                  |   Config Server:  Connected to the JHipster Registry running in Docker
emodel-app                  | ----------------------------------------------------------

ecos-app
--------
Назначение
~~~~~~~~~~
Образ, включающий контейнер сервлетов Tomcat с предварительно сформированным комплектом вебархивов, конфигурационных файлов для webapp и предустановленными инструментами.

Теги
~~~~

Тег:
<docker-registry>/ecos-<ecos project>:tag	

Веб архивы:
*	alfresco.war
*	share.war
*	flowable-admin.war
*	flowable-idm.war
*	flowable-modeler.war
*	flowable-rest.war
*	flowable-task.war
*	solr.war

Тег:
<docker-registry>/ecs-<ecos project>:tag

	Веб архивы:
*	alfresco.war
*	share.war
*	flowable-admin.war
*	flowable-idm.war
*	flowable-modeler.war
*	flowable-rest.war
*	flowable-task.war

Базовые образы
~~~~~~~~~~~~~~
**centos:centos7** - базовый образ последнего обновления CentOS 7.
**nexus.citeck.ru/ecs:base** - базовый образ на основе centos:centos7. В образ вынесены слои с типовыми инструкциями для переиспользования в итоговых образах.

Шаблон сервиса docker-compose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  ecos:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    container_name: ecos
    restart: unless-stopped
    ports:
      - 9090:9090/tcp
      - 50086:50086/tcp
    expose:
      - 8080/tcp
      - 8443/tcp
    environment:
      - USE_EXTERNAL_AUTH=<EXTERNAL_AUTH
      - DB_HOST=ecos-postgresql
      - ALFRESCO_HOSTNAME=<DOMAIN_NAME
      - ALFRESCO_PROTOCOL=https
      - SHARE_HOSTNAME=<DOMAIN_NAME
      - SHARE_PROTOCOL=https
      - SHARE_PORT=443
      - ALFRESCO_PORT=443
      - FLOWABLE_URL=https://<DOMAIN_NAME
      - MAIL_HOST=<M_HOST
      - MAIL_PORT=<M_PORT
      - DB_NAME=alfresco
      - FLOWABLE_DBNAME=alf_flowable
      - ECOS_EUREKA_INSTANCE_HOST=ecos
      - ECOS_EUREKA_INSTANCE_IP=ecos
      - ECOS_EUREKA_INSTANCE_PORT=8080
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
      - JAVA_OPTS=<BOOTSTRAP_LOCALE -Djava.security.egd=file:///dev/urandom <ECOS_XM <XDEBUG -Dcom.sun.management.jmxremote.authenticate=true -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.port=9090 -Dcom.sun.management.jmxremote.rmi.port=9090 -Djava.rmi.server.hostname=<HOST_IP -Dcom.sun.management.jmxremote.password.file=/tmp/alfresco/jmxremote.password -Dcom.sun.management.jmxremote.access.file=/tmp/alfresco/jmxremote.access
    volumes:
      - /opt/ecos/license:/opt/tomcat/shared/classes/alfresco/ecos
      - /opt/ecos/conf:/tmp/alfresco
      - /opt/ecos/content:/content
      - /opt/ecos/shared:/shared
      - /opt/ecos/extract_load:/extract_load
      - /opt/ecos/history_data/:/opt/history/data/
    networks:
      - app_network
    hostname: <HOSTNAME
    image: <ECOS_IMAGE
    stop_grace_period: 1m
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/alfresco"]
      interval: 1m
      timeout: 10s
      retries: 15
    depends_on:
      - ecos-postgresql
      - rabbitmq

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~
*	TWEAK_FLOWABLE - устаревший параметр, на данный момент по дефолту в true, требуется исключить из образа
*	FLOWABLE_REST_API_USERNAME - логин интеграции с flowable
*	FLOWABLE_REST_API_PASSWORD - пароль интеграции с flowable
*	ALFRESCO_HOSTNAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	ALFRESCO_PROTOCOL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco  -global.properties
*	SHARE_HOSTNAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	SHARE_PROTOCOL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	ALFRESCO_PORT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	SHARE_PORT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	DB_KIND - тип используемой бд (postgresql, mysql). Entrypoint формирует, в зависимости от выбранного параметра следующие переменные: DB_CONN_PARAMS, DB_DRIVER, DB_PORT.
*	DB_USERNAME - логин для подключеня к датасорсу
*	DB_PASSWORD - пароль для подключения к датасорсу
*	DB_NAME - имя базы данных
*	DB_HOST - fqdn or ip узла, где развернут инстанс бд
*	DB_DRIVER - используемый драйвер подключения к датасорсу, фомируется параметром DB_KIND
*	DB_PORT - порт усзла, где развернут инстанс бд, по умолчанию используются дефолтные порты postgresql, mysql
*	SYSTEM_SERVERMODE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_HOST - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_PORT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_USERNAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_PASSWORD - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_FROM_DEFAULT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_PROTOCOL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_SMTP_AUTH - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_SMTP_STARTTLS_ENABLE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_SMTPS_AUTH - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_SMTPS_STARTTLS_ENABLE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	FTP_PORT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	CIFS_ENABLED - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	CIFS_SERVER_NAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	CIFS_DOMAIN - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	NFS_ENABLED - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	CONTENT_STORE - расположение директорий contenstore/contentstore.deleted по абсолютному пути внутри контейнера
*	TOMCAT_CSRF_PATCH - расположение патча по отключению Tomcat CSRF token filter
*	TOMCAT_CSRF_ENABLED - использование Tomcat CSRF token filter (default true)
*	SOLR_WORKSPACE_PROPERTIES - (ecos image only) директория хранения настроек коллекции workspace solr4
*	SOLR_ARCHIVE_PROPERTIES -(ecos image only) директория хранения настроек коллекции archive solr4
*	SOLR_STORE - (ecos image only) расположение директории хранения индексов solr по абсолютному пути внутри контейнера
*	FLOWABLE_DB_KIND - тип используемой бд (postgresql, mysql). Entrypoint формирует, в зависимости от выбранного параметра следующие переменные: DB_CONN_PARAMS, DB_DRIVER, DB_PORT.
*	FLOWABLE_URL - fqdn or ip обращения к флобл ui
*	FLOWABLE_DB_NAME - имя базы данных
*	FLOWABLE_DB_USERNAME - логин для подключеня к датасорсу
*	FLOWABLE_DB_PASSWORD - пароль для подключения к датасорсу
*	FLOWABLE_DB_HOST - fqdn or ip узла, где развернут инстанс бд
*	FLOWABLE_DB_PORT - порт усзла, где развернут инстанс бд, по умолчанию используются дефолтные порты postgresql, mysql
*	FLOWABLE_DB_CONN_PARAMS - дополнительные параметры подключения к датасорсу
*	LDAP_ENABLED - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_KIND - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_AUTH_USERNAMEFORMAT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_URL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_DEFAULT_ADMINS - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_SECURITY_PRINCIPAL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_SECURITY_CREDENTIALS - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_GROUP_SEARCHBASE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_USER_SEARCHBASE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_USER_ATTRIBUTENAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_GROUP_MEMBER_ATTRIBUTENAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	USE_EXTERNAL_AUTH - конфгурирование share-config-custom.xml для использования внешней аутентификации по заголовку.

Известные проблемы
~~~~~~~~~~~~~~~~~~~
*	Часть событий лога приложений контейнера сервлетов остается внутри котейнера, что приводит к неконтролируему разрастанию overlay слоев контейнера и утилизации дискового ресурса хоста.
*	Часть параметров (отображены в документации типовой параметр конфигурации..) включены во входящиие параметры для entrypoint, часть параметров передается через alfresco-additional.properties, часть параметров находится на readonly слоях образа. Требуется выработка решения по использованию единого подхода к объявлению параметров.
*	Большое количество веб-приложений в составе одного образа, отсутствие возможности формализации используемых ресурсов в рамках веб приложения.
*	Невалидный ImageMagic (ecos image only)
*	Отсутствие контроля за процессами инструментов конвертации в образе (процесс конвертера не первичный, его состояние не влияет на ЖЦ контейнера, но влияет на доступность функционала в развернутом приложении)
*	Большой размер итогового образа (стандартная сборка без использования экспериментальных фич, типа сквоша слоев)
*	Отсутствие мониторинга в разрезе веб-приложения под Prometheus (есть jmx мониторинг через java-gateway zabbix)

Типовой вывод принятых настроек в лог контейнера
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Attention!!! All spaces in Environment variables will be deleted!!!
ecos                        | replacing option  flowable.rest-api.username=admin  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  flowable.rest-api.password=alfr3sc0  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  alfresco.host=ecos-demo.citeck.com  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  alfresco.protocol=https  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  alfresco.port=443  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  share.host=ecos-demo.citeck.com  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  share.protocol=https  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  share.port=443  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  system.serverMode=PRODUCTION  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  db.driver=org.postgresql.Driver  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  db.username=alfresco  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  db.password=alfr3sc0  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  db.name=alfresco  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  db.url=jdbc:postgresql://ecos-postgresql:5432/alfresco  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.host=mailhog  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.port=1025  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.username=  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.password=  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.from.default=alfresco@alfresco.org  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.protocol=smtp  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.smtp.auth=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.smtp.starttls.enable=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.smtps.auth=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  mail.smtps.starttls.enable=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  ftp.port=21  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  cifs.enabled=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  cifs.Server.Name=localhost  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  cifs.domain=WORKGROUP  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  cifs.hostannounce=true  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  cifs.broadcast=0.0.0.255  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  cifs.ipv6.enabled=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  nfs.enabled=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  dir.contentstore=/content/contentstore  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  dir.contentstore.deleted=/content/contentstore.deleted  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  flowable.modeler.url=https://ecos-demo.citeck.com/flowable-modeler/  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  flowable.rest-api.url=https://ecos-demo.citeck.com/flowable-rest/  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  flowable.webapps.deployment.api.url=https://ecos-demo.citeck.com/flowable-task/app-api  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | Flowable api url change skipped
ecos                        | adding option  idm.app.url=https://ecos-demo.citeck.com/flowable-idm/  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  flowable.db.url=jdbc:postgresql://ecos-postgresql:5432/alf_flowable  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  flowable.db.username=alfresco  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  flowable.db.password=alfr3sc0  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | adding option  flowable.db.driver.class.name=org.postgresql.Driver  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | replacing option  data.dir.root=/var/lib/solr4/index  in  /opt/alfresco/solr4/workspace-SpacesStore/conf/solrcore.properties
ecos                        | replacing option  solr.suggester.enabled=false  in  /opt/alfresco/solr4/workspace-SpacesStore/conf/solrcore.properties
ecos                        | replacing option  data.dir.root=/var/lib/solr4/index  in  /opt/alfresco/solr4/archive-SpacesStore/conf/solrcore.properties
ecos                        | adding option  authentication.chain=alfrescoNtlm1:alfrescoNtlm  in  /opt/tomcat/shared/classes/alfresco-global.properties
ecos                        | Flowable connection string: postgresql://ecos-postgresql:5432/alf_flowable
ecos                        | Solr configuration changed!


ecos-integrations-app
---------------------
Назначение
~~~~~~~~~~
Микросервис, предоставляющий эндпойнт ecos-records, через который можно посылать запросы в определенный список внешних систем.

Базовые образы
~~~~~~~~~~~~~~~
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

 integrations-app:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    image: nexus.citeck.ru/ecos-integrations:<INTEGRATIONS_APP_IMAGE
    container_name: integrations-app
    hostname: integrations-app
    restart: unless-stopped
    stop_grace_period: 1m
    depends_on:
      - integrations-postgresql
    environment:
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - _JAVA_OPTIONS=-Xmx256m -Xms256m
      - SPRING_PROFILES_ACTIVE=prod,swagger
      - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
      - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/config
      - SPRING_DATASOURCE_URL=jdbc:postgresql://integrations-postgresql:5432/integrations
      - JHIPSTER_SLEEP=140 # gives time for the JHipster Registry to boot before the application
    expose:
      - 8082/tcp
    networks:
      - app_network
 # INTEGRATIONS PSQL
  integrations-postgresql:
    image: postgres:10.4
    container_name: integrations-postgresql
    hostname: integrations-postgresql
    restart: unless-stopped
    stop_grace_period: 1m
    ports:
      - 127.0.0.1:15432:5432/tcp
    environment:
      - POSTGRES_USER=integrations
    volumes:
      - /opt/micro/postgresql/integrations:/var/lib/postgresql/data
    networks:
      - app_network

Используемые переменные
~~~~~~~~~~~~~~~~~~~~~~~~

*	_JAVA_OPTIONS - параметры для jvm
*	SPRING_PROFILES_ACTIVE - используемые при развертывании профили
*	EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE - url используемого по умолчанию eureka load balancer, содержит credentials
*	SPRING_CLOUD_CONFIG_URI - url используемого cloud config server, содержит credentials
*	JHIPSTER_REGISTRY_PASSWORD - пароль пользователя для аутентификации в eureka load balancer
*	SPRING_DATASOURCE_URL - url используемого postgresql datasource
*	JHIPSTER_SLEEP - таймаут перед развертыванием микросервиса

Известные проблемы
~~~~~~~~~~~~~~~~~~

•	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
•	Использование empty password в доступах к датасорсам
•	cloud config и eureka load balancer используют один и тот же пароль


Типовой вывод успешного развертывания в лог контейнера
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::
 
 integrations-app            | ----------------------------------------------------------
 integrations-app            |   Application 'integrations' is running! Access URLs:
 integrations-app            |   Local:          http://localhost:8082/
 integrations-app            |   External:       http://172.26.0.21:8082/
 integrations-app            |   Profile(s):     [prod, swagger]
 integrations-app            | ----------------------------------------------------------
 integrations-app            | 2020-05-14 06:12:11.339  INFO 1 --- [           main] r.c.ecos.integrations.IntegrationsApp    : 
 integrations-app            | ----------------------------------------------------------
 integrations-app            |   Config Server:  Connected to the JHipster Registry running in Docker
 integrations-app            | ----------------------------------------------------------

ecos-solr-app
-------------

Назначение
~~~~~~~~~~~
Образ с установленным контейнером сервлетов Tomcat с вебархивом проекта ecos-alfresco-solr4

Базовые образы
~~~~~~~~~~~~~~~
•	tomcat:7.0.59-jre8 - официальный образ tomcat 7.0.59, openjdk version "1.8.0_40-internal"

Шаблон сервиса docker-compose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::
 
 ess:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    image: nexus.citeck.ru/ess:<ECOS_SOLR4
    restart: unless-stopped
    stop_grace_period: 1m
    container_name: ess
    hostname: ess
    ports:
      - 8080:8080/tcp
      - 8443:8443/tcp
    env_file:
      - ./env_dir/ess.env
    volumes:
      - /opt/ess:/opt/solr4_data
    networks:
      - app_network

Используемые переменные
~~~~~~~~~~~~~~~~~~~~~~~~
•	ALFRESCO_HOST - fqdn/ip инстанса ecos
•	ALFRESCO_PORT - http порт инстанса ecos 
•	ALFRESCO_PORT_SSL - https порт инстанса ecos 
•	ALFRESCO_SECURE_COMMS - использовать шифрованное соединение
•	CITECK_MERGE_FACTOR - мерж фактор solr/lucene, используемый при определении необходимости мержить сегменты.
•	ALFRESCO_INDEX_TRANSFORM_CONTENT - если true - будет происходить конвертация контента в текст и его последующая пословесная индексация. Если false - будут индексироваться только метаданные (mimetype, size, etc).
•	ALFRESCO_RECORD_UNINDEXED_NODES - если true - ноды, типы которых отмечены как “неиндексируемые” - будут попадать в индекс в качестве документа без индексации атрибутов ноды. Если false - такие документы будут игнорироваться при индексации.
•	CITECK_RECORD_TRANSACTIONS - если true - каждая транзакция будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях будут храниться только в кеше, в памяти.
•	CITECK_TX_CONSISTENCY_CHECK_MODE - тип проверки консистентности индекса и базы для индексации транзакций. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.
•	CITECK_TX_IS_INDEXED_CACHE_SIZE - размер кеша, если CITECK_RECORD_TRANSACTIONS = false.
•	CITECK_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT - коэффициент чистки кеша при переполнении, если CITECK_RECORD_TRANSACTIONS = false.
•	CITECK_RECORD_ACL_TRANSACTIONS - если true - каждая транзакция прав будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях прав будут храниться только в кеше, в памяти.
•	CITECK_ACL_CONSISTENCY_CHECK_MODE - тип проверки консистентности индекса и базы для индексации транзакций прав. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.
•	CITECK_ACL_TX_IS_INDEXED_CACHE_SIZE - размер кеша, если CITECK_RECORD_ACL_TRANSACTIONS = false.
•	CITECK_ACL_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT - коэффициент чистки кеша при переполнении, если CITECK_RECORD_ACL_TRANSACTIONS = false.
•	JAVA_OPTS - параметры для jvm

Типовой вывод успешного развертывания в лог контейнера
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	ess                         | Attention!!! All spaces in Environment variables will be deleted!!!
	ess                         | Solr configuration changed!
	ess                         | replacing option  alfresco.index.transformContent=false  in  /opt/solr4/archive-SpacesStore/conf/solrcore.properties
	ess                         | replacing option  alfresco.index.transformContent=false  in  /opt/solr4/workspace-SpacesStore/conf/solrcore.properties
	ess                         | replacing option  alfresco.recordUnindexedNodes=false  in  /opt/solr4/archive-SpacesStore/conf/solrcore.properties
	ess                         | replacing option  alfresco.recordUnindexedNodes=false  in  /opt/solr4/workspace-SpacesStore/conf/solrcore.properties
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Server version:        Apache Tomcat/7.0.59
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Server built:          Jan 28 2015 15:51:10 UTC
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Server number:         7.0.59.0
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: OS Name:               Linux
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: OS Version:            3.10.0-957.21.2.el7.x86_64
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Architecture:          amd64
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Java Home:             /usr/lib/jvm/java-8-openjdk-amd64/jre
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: JVM Version:           1.8.0_40-internal-b27
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: JVM Vendor:            Oracle Corporation
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: CATALINA_BASE:         /usr/local/tomcat
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: CATALINA_HOME:         /usr/local/tomcat
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Djava.util.logging.config.file=/usr/local/tomcat/conf/logging.properties
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Xms1G
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Xmx2G
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Djava.endorsed.dirs=/usr/local/tomcat/endorsed
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Dcatalina.base=/usr/local/tomcat
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Dcatalina.home=/usr/local/tomcat
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Djava.io.tmpdir=/usr/local/tomcat/temp
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.core.AprLifecycleListener lifecycleEvent
	ess                         | INFO: The APR based Apache Tomcat Native library which allows optimal performance in production environments was not found on the java.library.path: /usr/java/packages/lib/amd64:/usr/lib/x86_64-linux-gnu/jni:/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:/usr/lib/jni:/lib:/usr/lib
	ess                         | May 14, 2020 9:28:30 AM org.apache.coyote.AbstractProtocol init
	ess                         | INFO: Initializing ProtocolHandler ["http-bio-8080"]
	ess                         | May 14, 2020 9:28:30 AM org.apache.coyote.AbstractProtocol init
	ess                         | INFO: Initializing ProtocolHandler ["ajp-bio-8009"]
	ess                         | May 14, 2020 9:28:31 AM org.apache.coyote.AbstractProtocol init
	ess                         | INFO: Initializing ProtocolHandler ["http-bio-8443"]
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.startup.Catalina load
	ess                         | INFO: Initialization processed in 1875 ms
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.core.StandardService startInternal
	ess                         | INFO: Starting service Catalina
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.core.StandardEngine startInternal
	ess                         | INFO: Starting Servlet Engine: Apache Tomcat/7.0.59
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.startup.HostConfig deployDescriptor
	ess                         | INFO: Deploying configuration descriptor /usr/local/tomcat/conf/Catalina/localhost/solr4.xml
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.startup.SetContextPropertiesRule begin
	ess                         | WARNING: [SetContextPropertiesRule]{Context} Setting property 'debug' to '0' did not find a matching property.
	ess                         | May 14, 2020 9:28:41 AM org.apache.catalina.core.ApplicationContext log
	ess                         | INFO: No Spring WebApplicationInitializer types detected on classpath
	ess                         | 2020-05-14 09:28:47,899  INFO  [solr.component.AsyncBuildSuggestComponent] [coreLoadExecutor-5-thread-2] Initializing SuggestComponent
	ess                         | 2020-05-14 09:28:49,601  INFO  [solr.component.AsyncBuildSuggestComponent] [coreLoadExecutor-5-thread-1] Initializing SuggestComponent
	ess                         | May 14, 2020 9:28:49 AM org.apache.catalina.startup.HostConfig deployDescriptor
	ess                         | INFO: Deployment of configuration descriptor /usr/local/tomcat/conf/Catalina/localhost/solr4.xml has finished in 18,143 ms
	ess                         | May 14, 2020 9:28:49 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/examples
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/examples has finished in 408 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/manager
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/manager has finished in 64 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/host-manager
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/host-manager has finished in 47 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/ROOT
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/ROOT has finished in 56 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/docs
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/docs has finished in 35 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.coyote.AbstractProtocol start
	ess                         | INFO: Starting ProtocolHandler ["http-bio-8080"]
	ess                         | May 14, 2020 9:28:50 AM org.apache.coyote.AbstractProtocol start
	ess                         | INFO: Starting ProtocolHandler ["ajp-bio-8009"]
	ess                         | May 14, 2020 9:28:50 AM org.apache.coyote.AbstractProtocol start
	ess                         | INFO: Starting ProtocolHandler ["http-bio-8443"]
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.Catalina start
	ess                         | INFO: Server startup in 18992 ms

ecos-proxy-app
--------------
Назначение
~~~~~~~~~~~
Образ проксирующего сервера со сборкой проекта ecos-ui. 

Базовые образы
~~~~~~~~~~~~~~
nexus.citeck.ru/ecos-nginx-spnego:stable -  Nginx (1.17.6) собирается из исходников + в сборку включен модуль spnego (1.1.0)  для интеграции с AD заказчика и реализации SSO. Базовый образ строится на alpine:3.7 
openresty/openresty:centos-rpm - openresty (1.15.8.3) устанавливается из репо пакетами. Базовый образ строится на CentOS 7.

Шаблон сервиса docker-compose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::
 ecos-proxy:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    container_name: ecos-proxy
    restart: unless-stopped
    stop_grace_period: 1m
    hostname: ecos-proxy
    ports:
      - 80:80/tcp
    env_file:
     - ./env_dir/ecos-proxy.env
    image: nexus.citeck.ru/ecos-proxy:<ECOS_PROXY_IMAGE
    networks:
      - app_network

Используемые переменные
~~~~~~~~~~~~~~~~~~~~~~~
•	DEFAULT_LOCATION_V2 - переключение дефолтного редиректа ( / ) с share/page на v2/. Формат переменной: DEFAULT_LOCATION_V2=true (параметр дублируется в клиенте в настройках системных журналов)
•	ECOS_INIT_DELAY - таймаут запуска entrypoint скрипта, формирующего default.conf сервера. По умолчанию 30с для нормализации инициализации апстримов в compose проектах.
•	CADVISOR_TARGET - если параметр не указан, то из файла конфигурации nginx будет удален апсрим cadvisor и зависимые от него локейшены. Формат переменной: CADVISOR_TARGET=ip_or_fqdn:port
•	NODE_EXPORTER_TARGET - если параметр не указан, то из файла конфигурации nginx будет удален апсрим node-exporter и зависимые от него локейшены. Формат переменной: NODE_EXPORTER_TARGET=ip_or_fqdn:port
•	USE_EXTERNAL_CONFIGURATION - при объявлении данной переменной будет удален конфигурационный файл default.conf в директории nginx. Используется для разработки и конфигурирования, при этом директории статики, конфигурационные файлы, сертификаты и прочее необходимо прокинуть в контейнер через pv. Директория монтирования файла конфигурации nginx  - /etc/nginx/conf.d/. Формат переменной: USE_EXTERNAL_CONFIGURATION=true
•	PROXY_TARGET - если параметр не указан в файле ecos-proxy.env, то выставляется дефолтное проксирование на контейнер ecos- ecos:8080. Соответственно, при объявлении параметра в файле переменных будет заменено значение ecos:8080 в апстриме ecos конфигурации nginx образа на указанное в файле переменных. Формат переменной: PROXY_TARGET=ip_or_fqdn:port
•	GATEWAY_TARGET - если параметр не указан, то из файла конфигурации nginx будет удален апсрим gateway и зависимые от него локейшены. Формат переменной: GATEWAY_TARGET=ip_or_fqdn:port
•	ENABLE_LOGGING - по умолчанию логирование контейнера отключено, объявление данной переменной включит стандартное логирование nginx, выставление переменной в debug включит расширенный режим отладки обработки пакетов nginx. Формат переменной: ENABLE_LOGGING=true (debug для расширенного режима)
•	ENABLE_SERVER_STATUS - включение локейшена с выдачей статистики сервера nginx, используется для централизированного мониторинга. Локейш доступен только из docker сети. Формат переменной: ENABLE_SERVER_STATUS=true
•	ENABLE_MOBILE_APP_ACCESS - включение локейшена /gateeway с проверкой bearer токена в хидере Authorization. Используется для доступа мобильным приложением. Формат переменной: ENABLE_MOBILE_APP_ACCESS=true. При включении данного функционала требуется сконфигрурировать переменные EIS_ID, REALM_ID, CLIENT_SECRET для интеграции с keycloak.
•	ENABLE_OIDC_FULL_ACCESS - включение проверки bearer токена в хидере Authorization для любого из обрабатываемых локейшенов. Формат переменной: ENABLE_OIDC_FULL_ACCESS=true. При включении данного функционала требуется сконфигрурировать переменные EIS_ID, REALM_ID, CLIENT_SECRET для интеграции с keycloak.
•	ONLYOFFICE_TARGET - включение локейшена /onlyoffice/ для интеграции ecos c развернутым инстансом OnlyOffice. Формат переменной: ONLYOFFICE_TARGET=ip_or_fqdn:port
•	MAILHOG_TARGET - включение локейшена проксирования в ui контейнера mailhog. MAILHOG_TARGET=ip_or_fqdn:port
•	ECOS_REGISTRY_TARGET - включение локейшена проксирования в ui контейнера ecos(jhipster)-registry. Формат переменной: ECOS_REGISTRY_TARGET=ip_or_fqdn:port
•	RABBITMQ_TARGET - включение локейшена проксирования в managment ui контейнера rabbitmq. Формат переменной: RABBITMQ_TARGET=ip_or_fqdn:port
•	EIS_TARGET - включение локейшена проксирования в ui контейнера eis. Используется при размещении eis за проксирующим сервером в сетевом сегменте заказчика. Формат переменной: EIS_TARGET=ip_or_fqdn:port
•	ECOS_PAGE_TITLE - настройка заголовка index.html страницы браузера для нового интерфейса (v2). По умолчанию Citeck ECOS
•	EIS_PROTO – протокол, по которому идёт взаимодействие с keycloak. Значение по-умолчанию  https, опционально можно поставить http
Не реализованы:
•	SOLR_TARGET
•	ECOS_REGISTRY_TARGET (проблема с api)

Типовой вывод принятых настроек в лог контейнера
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	ecos-proxy                  | Wait 30 seconds and run nginx
	ecos-proxy                  | - Logging disabled
	ecos-proxy                  | + Server status monitoring enabled!
	ecos-proxy                  | + Changed upstream gateway: gateway-app:8085
	ecos-proxy                  | - Disabled api-auth upstream and locations
	ecos-proxy                  | + Changed mailhog upstream: mailhog:8025
	ecos-proxy                  | - Disabled gss
	ecos-proxy                  | + Changed ecos-registry upstream: jhipster-registry:8761
	ecos-proxy                  | + Changed rabbitmq upstream: rabbitmq:15672
	ecos-proxy                  | - Disabled eis upstream and locations
	ecos-proxy                  | - Disabled solr location


ecos-uiserv-app
---------------
Назначение
~~~~~~~~~~~~~
Образ микросервиса, предоставляющего элементы ui и хранящий их настройки (меню, журналы, UI конфиги, формы, настройки журналов, дашборды)

Базовые образы
~~~~~~~~~~~~~~~
•	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::
 uiserv-app:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    image: nexus.citeck.ru/ecos-uiserv:<UISERV_APP_IMAGE
    container_name: uiserv-app
    hostname: uiserv-app
    restart: unless-stopped
    stop_grace_period: 1m
    depends_on:
      - uiserv-postgresql
    environment:
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - _JAVA_OPTIONS=-Xmx256m -Xms256m <UISERV_MENU_OVERRIDE
      - SPRING_PROFILES_ACTIVE=prod,swagger
      - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
      - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/config
      - SPRING_DATASOURCE_URL=jdbc:postgresql://uiserv-postgresql:5432/uiserv
      - JHIPSTER_SLEEP=120 # gives time for the JHipster Registry to boot before the application
    expose:
      - 8081/tcp
    networks:
      - app_network
    volumes:
      <MENU_OVERRIDE_DIR
      - /opt/alfresco/logs/uiserv:/tmp
  uiserv-postgresql:
    image: postgres:10.4
    container_name: uiserv-postgresql
    hostname: uiserv-postgresql
    restart: unless-stopped
    stop_grace_period: 1m
    environment:
      - POSTGRES_USER=uiserv
      - POSTGRES_PASSWORD=
    volumes:
      - /opt/micro/postgresql/uiserv:/var/lib/postgresql/data
    networks:
      - app_network

Используемые переменные
~~~~~~~~~~~~~~~~~~~~~~~~
•	**_JAVA_OPTIONS** - параметры для jvm
•	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
•	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию eureka load balancer, содержит credentials
•	**SPRING_CLOUD_CONFIG_URI** - url используемого cloud config server, содержит credentials
•	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
•	**SPRING_DATASOURCE_URL** - url используемого postgresql datasource
•	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы
~~~~~~~~~~~~~~~~~~~~~~~~
•	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
•	Использование empty password в доступах к датасорсам
•	cloud config и eureka load balancer используют один и тот же пароль

Типовой вывод успешного развертывания в лог контейнера
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	uiserv-app                  | ----------------------------------------------------------
	uiserv-app                  |   Application 'uiserv' is running! Access URLs:
	uiserv-app                  |   Local:          http://localhost:8081/
	uiserv-app                  |   External:       http://172.25.0.20:8081/
	uiserv-app                  |   Profile(s):     [prod, swagger]
	uiserv-app                  | ----------------------------------------------------------
	uiserv-app                  | 2020-05-13 10:46:57.034  INFO 1 --- [           main] ru.citeck.ecos.uiserv.Application        : 
	uiserv-app                  | ----------------------------------------------------------
	uiserv-app                  |   Config Server:  Connected to the JHipster Registry running in Docker
	uiserv-app                  | ----------------------------------------------------------

ecos-process-app
----------------
Назначение
~~~~~~~~~~
Образ микросервиса для управления CMMN процессами 

Базовые образы
~~~~~~~~~~~~~~~
•	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

 ecos-process-app:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    image: nexus.citeck.ru/ecos-process:<ECOS_PROCESS_IMAGE
    container_name: ecos-process-app
    stop_grace_period: 1m
    hostname: ecos-process-app
    restart: unless-stopped
    depends_on:
      - mongo-app
    environment:
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - _JAVA_OPTIONS=-Xmx256m -Xms256m
      - SPRING_PROFILES_ACTIVE=dev,swagger
      - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
      - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/config
      - SPRING_DATA_MONGODB_URI=mongodb://ecos-process:ecos-process-password@mongo-app:27017/ecos-process
      - ECOS_INIT_DELAY=120
    expose:
      - 8098/tcp
    networks:
      - app_network

Используемые переменные
~~~~~~~~~~~~~~~~~~~~~~~~
•	**_JAVA_OPTIONS** - параметры для jvm
•	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
•	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию eureka load balancer, содержит credentials
•	**SPRING_CLOUD_CONFIG_URI** - url используемого cloud config server, содержит credentials
•	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
•	**SPRING_DATA_MONGODB_URI** - url используемого mongodb datasource
•	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы
~~~~~~~~~~~~~~~~~~
•	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
•	Использование empty password в доступах к датасорсам
•	cloud config и eureka load balancer используют один и тот же пароль

Типовой вывод успешного развертывания в лог контейнера
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	ecos-process-app            | ----------------------------------------------------------
	ecos-process-app            |   Application 'eproc' is running! Access URLs:
	ecos-process-app            |   Local:          http://localhost:8098/
	ecos-process-app            |   External:       http://172.26.0.26:8098/
	ecos-process-app            |   Profile(s):     [dev, swagger]
	ecos-process-app            | ----------------------------------------------------------
	ecos-process-app            | 2020-05-14 06:30:07.511  INFO 1 --- [           main] ru.citeck.ecos.process.EprocApp          : 
	ecos-process-app            | ----------------------------------------------------------
	ecos-process-app            |   Config Server:  Connected to the JHipster Registry running in Docker
	ecos-process-app            | ----------------------------------------------------------
