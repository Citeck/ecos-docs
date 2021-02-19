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
