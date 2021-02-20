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

•	**_JAVA_OPTIONS** - параметры для **jvm**
•	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
•	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials
•	**SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials
•	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**
•	**SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**
•	**JHIPSTER_SLEEP **- **таймаут** перед развертыванием микросервиса

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
•	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
•	Использование empty password в доступах к датасорсам
•	cloud config и eureka load balancer используют один и тот же пароль

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
•	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

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
•	**_JAVA_OPTIONS** - параметры для **jvm**
•	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
•	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials
•	**SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials
•	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**
•	**SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**
•	**JHIPSTER_SLEEP **- **таймаут** перед развертыванием микросервиса
•	**ECOS-NOTIFICATIONS_EVENT_HOST** - fqdn/ip диспетчера очередей rabbitmq
•	**ECOS-NOTIFICATIONS_EVENT_PORT** - amqp порт диспетчера очередей rabbitmq
•	**ECOS-NOTIFICATIONS_EVENT_USERNAME** - пользователь диспетчера очередей rabbitmq
•	**ECOS-NOTIFICATIONS_EVENT_PASSWORD** - пароль диспетчера очередей rabbitmq
•	**ECOS-NOTIFICATIONS_ALFRESCO_URL** - fqdn развернутого приложения ecos
•	**ECOS-NOTIFICATIONS_ALFRESCO_AUTHENTICATION_USERNAME** - пользователь в ecos для интеграции с микросервисом нотификации
•	**ECOS-NOTIFICATIONS_ALFRESCO_AUTHENTICATION_PASSWORD** - пароль пользователя в ecos для интеграции с микросервисом нотификации

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
•	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
•	Использование empty password в доступах к датасорсам
•	cloud config и eureka load balancer используют один и тот же пароль
•	Монтирование firebase credentials как волюма
•	Часть app properties (ECOS-NOTIFICATIONS*) нужно вынести в spring cloud config

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
•	`mongo_4 <https://hub.docker.com/layers/mongo/library/mongo/4.0/images/sha256-ccd97bd444338973ac143a22753e6b73a3e707a6a3edd512311a418a3e432cdb?context=explore>`_ - Официальный образ mongodb v 4.0.x

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

•	**MONGO_INITDB_ROOT_USERNAME** - логин пользователя, который будет создан в **admin db с root** привилегиями
•	**MONGO_INITDB_ROOT_PASSWORD** - пароль привилегированного пользователя
•	**MONGO_INITDB_DATABASE** - определение базы данных, используемой в скриптах развертывания в /docker-entrypoint-initdb.d/*.js/sh. Для понимания:
This variable allows you to specify the name of a database to be used for creation scripts in /docker-entrypoint-initdb.d/*.js (see Initializing a fresh instance below). MongoDB is fundamentally designed for "create on first use", so if you do not insert data with your JavaScript files, then no database is created.
•	**ECOS_HISTORY_APP_DATASOURCE_DATABASE** - db микросервиса истории **(ecos-history)**
•	**ECOS_HISTORY_APP_DATASOURCE_USERNAME** - логин для мкр истории, роль dbOwner **(ecos-history)**
•	**ECOS_HISTORY_APP_DATASOURCE_PASSWORD** - пароль для мкр истории **(ecos-history-password)**
•	**ECOS_PROCESS_APP_DATASOURCE_DATABASE** - db микросервиса ecos-process **(ecos-process)**
•	**ECOS_PROCESS_APP_DATASOURCE_USERNAME **- логин для мкр ecos-process, роль dbOwner **(ecos-process)**
•	**ECOS_PROCESS_APP_DATASOURCE_PASSWORD** - пароль для мкр ecos-process **(ecos-process-password)**

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
•	**MH_UI_WEB_PATH** - web path для использования mailhog за проксирующим ecos-proxy (mailhog)

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
•	**_JAVA_OPTIONS** - параметры для jvm
•	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
•	**SPRING_SECURITY_USER_PASSWORD** - пароль пользователя для аутентификации в cloud config
•	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
•	Документация по `spring cloud config <https://cloud.spring.io/spring-cloud-config/reference/html/#_spring_cloud_config_server>`_

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
•	Требуется закончить переход на ecos-registry проект
•	Утилизации цпу
•	Требуется конфигурация registry как экспортера метрик микросервисов в Prometheus
•	Использование localPath расположения конфигурационного файла
•	Не реализован доступ к ui registry через location
•	Не используется JWT token

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

•	**POSTGRES_PASSWORD **- обязательный параметр за исключением 
*   **POSTGRES_HOST_AUTH_METHOD=trust**, пароль рутового пользователя
•	**POSTGRES_USER** - переопределение дефолтного пользователя **postgres**
•	**POSTGRES_DB **- переопределение дефолтной базы данных
•	**POSTGRES_INITDB_ARGS** - дополнительные параметры для инициализации кластера
•	**POSTGRES_INITDB_WALDIR** - переопределение дефолтной директории хранения логов транзакций
•	**POSTGRES_HOST_AUTH_METHOD** - метод аутентификации host подключений для всех бд, пользователей и адресов в **pg_hba.conf**. Дефолтное значение **md5**
•	**PGDATA** - переопределение дефолтной директории хранения фалов инициируемого кластера
•	**DB_NAME** - определение базы данных **ecos**
•	**DB_USERNAME** - определение пользователя для базы данных **ecos/flowable/ecos-history**
•	**DB_PASSWORD** - пароль создаваемого пользователя
•	**FLOWABLE_DBNAME** - определение базы данных **flowable**
•	**HISTORY_DBNAME** - определение базы данных для ecos-history-app (устаревший параметр, базы данных мкр вынесены в отдельный инстанс)
•	**CASE_MODEL_DBNAME** - определение базы данных **ecos-case-model-app**

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
•	EOL версии postgresl
•	Используется один пользователь для баз данных
•	Отсутствие конфигурации postgresql.conf, pg_hba.conf
•	Отсутствие конфигурации используемых схем

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
•	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

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
•	**_JAVA_OPTIONS** - параметры для **jvm**
•	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
•	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials
•	**SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials
•	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**
•	**SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**
•	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
•	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
•	Использование empty password в доступах к датасорсам
•	cloud config и eureka load balancer используют один и тот же пароль

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