Сервисы Docker
================

.. contents::
		:depth: 2

onlyoffice-ds-app
-----------------

Назначение:
~~~~~~~~~~~
Образ, включающий набор инструментов для развертывания onlyoffice-ds

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

	onlyoffice-ds:
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
::

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
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Образ одного из центральных компонентов микросервисной архитектуры. Приложение реализует API шлюз взаимодействия с остальными микросервисами

Теги:
~~~~~

`Nexus_gateway <http://nexus.citeck.ru/ecos-gateway:>`_ <tag> - сборка проекта ecos-gateway 

Базовые образы:
~~~~~~~~~~~~~~~

**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

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
::

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
::

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
*	Cloud config и eureka load balancer используют один и тот же пароль
*	Монтирование firebase credentials как волюма
*	Часть app properties (ECOS-NOTIFICATIONS*) нужно вынести в spring cloud config

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

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
::
 
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
*	**MONGO_INITDB_DATABASE** - определение базы данных, используемой в скриптах развертывания в ``/docker-entrypoint-initdb.d/*.js/sh. (1)``
*	**ECOS_HISTORY_APP_DATASOURCE_DATABASE** - db микросервиса истории **(ecos-history)**
*	**ECOS_HISTORY_APP_DATASOURCE_USERNAME** - логин для мкр истории, роль dbOwner **(ecos-history)**
*	**ECOS_HISTORY_APP_DATASOURCE_PASSWORD** - пароль для мкр истории **(ecos-history-password)**
*	**ECOS_PROCESS_APP_DATASOURCE_DATABASE** - db микросервиса ecos-process **(ecos-process)**
*	**ECOS_PROCESS_APP_DATASOURCE_USERNAME **- логин для мкр ecos-process, роль dbOwner **(ecos-process)**
*	**ECOS_PROCESS_APP_DATASOURCE_PASSWORD** - пароль для мкр ecos-process **(ecos-process-password)**
 	
(1) - This variable allows you to specify the name of a database to be used for creation scripts in /docker-entrypoint-initdb.d/.js (see Initializing a fresh instance below). MongoDB is fundamentally designed for «create on first use», so if you do not insert data with your JavaScript files, then no database is created.

Известные проблемы:
~~~~~~~~~~~~~~~~~~~
::
 
	2020-05-06T07:44:14.752+0000 I STORAGE [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
	2020-05-06T07:44:14.752+0000 I STORAGE [initandlisten] ** See `mongo_prodnotes_filesystem <http://dochub.mongodb.org/core/prodnotes-filesystem>`_ 

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

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
::

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
::

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
**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

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
::

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
**postgres:9.4-alpine** - официальный образ postgresql 9.4.x на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::

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

*	**POSTGRES_PASSWORD** - обязательный параметр за исключением 
*   **POSTGRES_HOST_AUTH_METHOD=trust**, пароль рутового пользователя
*	**POSTGRES_USER** - переопределение дефолтного пользователя **postgres**
*	**POSTGRES_DB** - переопределение дефолтной базы данных
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
::

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
::

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
::

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

<docker-registry>/ecos-<ecos project>:tag*

**Веб архивы**

*	alfresco.war
*	share.war
*	flowable-admin.war
*	flowable-idm.war
*	flowable-modeler.war
*	flowable-rest.war
*	flowable-task.war
*	solr.war

Тег:
*<docker-registry>/ecs-<ecos project>:tag*

**Веб архивы:**

*	alfresco.war
*	share.war
*	flowable-admin.war
*	flowable-idm.war
*	flowable-modeler.war
*	flowable-rest.war
*	flowable-task.war

Базовые образы
~~~~~~~~~~~~~~
* **centos:centos7** - базовый образ последнего обновления CentOS 7.
* **nexus.citeck.ru/ecs:base** - базовый образ на основе centos:centos7. В образ вынесены слои с типовыми инструкциями для переиспользования в итоговых образах.

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
::

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

*	**_JAVA_OPTIONS** - параметры для jvm
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию eureka load balancer, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого cloud config server, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
*	**SPRING_DATASOURCE_URL** - url используемого postgresql datasource
*	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы
~~~~~~~~~~~~~~~~~~

*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	Cloud config и eureka load balancer используют один и тот же пароль


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
*	tomcat:7.0.59-jre8 - официальный образ tomcat 7.0.59, openjdk version "1.8.0_40-internal"

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
*	ALFRESCO_HOST - fqdn/ip инстанса ecos
*	ALFRESCO_PORT - http порт инстанса ecos 
*	ALFRESCO_PORT_SSL - https порт инстанса ecos 
*	ALFRESCO_SECURE_COMMS - использовать шифрованное соединение
*	CITECK_MERGE_FACTOR - мерж фактор solr/lucene, используемый при определении необходимости мержить сегменты.
*	ALFRESCO_INDEX_TRANSFORM_CONTENT - если true - будет происходить конвертация контента в текст и его последующая пословесная индексация. Если false - будут индексироваться только метаданные (mimetype, size, etc).
*	ALFRESCO_RECORD_UNINDEXED_NODES - если true - ноды, типы которых отмечены как “неиндексируемые” - будут попадать в индекс в качестве документа без индексации атрибутов ноды. Если false - такие документы будут игнорироваться при индексации.
*	CITECK_RECORD_TRANSACTIONS - если true - каждая транзакция будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях будут храниться только в кеше, в памяти.
*	CITECK_TX_CONSISTENCY_CHECK_MODE - тип проверки консистентности индекса и базы для индексации транзакций. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.
*	CITECK_TX_IS_INDEXED_CACHE_SIZE - размер кеша, если CITECK_RECORD_TRANSACTIONS = false.
*	CITECK_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT - коэффициент чистки кеша при переполнении, если CITECK_RECORD_TRANSACTIONS = false.
*	CITECK_RECORD_ACL_TRANSACTIONS - если true - каждая транзакция прав будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях прав будут храниться только в кеше, в памяти.
*	CITECK_ACL_CONSISTENCY_CHECK_MODE - тип проверки консистентности индекса и базы для индексации транзакций прав. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.
*	CITECK_ACL_TX_IS_INDEXED_CACHE_SIZE - размер кеша, если CITECK_RECORD_ACL_TRANSACTIONS = false.
*	CITECK_ACL_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT - коэффициент чистки кеша при переполнении, если CITECK_RECORD_ACL_TRANSACTIONS = false.
*	JAVA_OPTS - параметры для jvm

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
*	DEFAULT_LOCATION_V2 - переключение дефолтного редиректа ( / ) с share/page на v2/. Формат переменной: DEFAULT_LOCATION_V2=true (параметр дублируется в клиенте в настройках системных журналов)
*	ECOS_INIT_DELAY - таймаут запуска entrypoint скрипта, формирующего default.conf сервера. По умолчанию 30с для нормализации инициализации апстримов в compose проектах.
*	CADVISOR_TARGET - если параметр не указан, то из файла конфигурации nginx будет удален апсрим cadvisor и зависимые от него локейшены. Формат переменной: CADVISOR_TARGET=ip_or_fqdn:port
*	NODE_EXPORTER_TARGET - если параметр не указан, то из файла конфигурации nginx будет удален апсрим node-exporter и зависимые от него локейшены. Формат переменной: NODE_EXPORTER_TARGET=ip_or_fqdn:port
*	USE_EXTERNAL_CONFIGURATION - при объявлении данной переменной будет удален конфигурационный файл default.conf в директории nginx. Используется для разработки и конфигурирования, при этом директории статики, конфигурационные файлы, сертификаты и прочее необходимо прокинуть в контейнер через pv. Директория монтирования файла конфигурации nginx  - /etc/nginx/conf.d/. Формат переменной: USE_EXTERNAL_CONFIGURATION=true
*	PROXY_TARGET - если параметр не указан в файле ecos-proxy.env, то выставляется дефолтное проксирование на контейнер ecos- ecos:8080. Соответственно, при объявлении параметра в файле переменных будет заменено значение ecos:8080 в апстриме ecos конфигурации nginx образа на указанное в файле переменных. Формат переменной: PROXY_TARGET=ip_or_fqdn:port
*	GATEWAY_TARGET - если параметр не указан, то из файла конфигурации nginx будет удален апсрим gateway и зависимые от него локейшены. Формат переменной: GATEWAY_TARGET=ip_or_fqdn:port
*	ENABLE_LOGGING - по умолчанию логирование контейнера отключено, объявление данной переменной включит стандартное логирование nginx, выставление переменной в debug включит расширенный режим отладки обработки пакетов nginx. Формат переменной: ENABLE_LOGGING=true (debug для расширенного режима)
*	ENABLE_SERVER_STATUS - включение локейшена с выдачей статистики сервера nginx, используется для централизированного мониторинга. Локейш доступен только из docker сети. Формат переменной: ENABLE_SERVER_STATUS=true
*	ENABLE_MOBILE_APP_ACCESS - включение локейшена /gateeway с проверкой bearer токена в хидере Authorization. Используется для доступа мобильным приложением. Формат переменной: ENABLE_MOBILE_APP_ACCESS=true. При включении данного функционала требуется сконфигрурировать переменные EIS_ID, REALM_ID, CLIENT_SECRET для интеграции с keycloak.
*	ENABLE_OIDC_FULL_ACCESS - включение проверки bearer токена в хидере Authorization для любого из обрабатываемых локейшенов. Формат переменной: ENABLE_OIDC_FULL_ACCESS=true. При включении данного функционала требуется сконфигрурировать переменные EIS_ID, REALM_ID, CLIENT_SECRET для интеграции с keycloak.
*	ONLYOFFICE_TARGET - включение локейшена /onlyoffice/ для интеграции ecos c развернутым инстансом OnlyOffice. Формат переменной: ONLYOFFICE_TARGET=ip_or_fqdn:port
*	MAILHOG_TARGET - включение локейшена проксирования в ui контейнера mailhog. MAILHOG_TARGET=ip_or_fqdn:port
*	ECOS_REGISTRY_TARGET - включение локейшена проксирования в ui контейнера ecos(jhipster)-registry. Формат переменной: ECOS_REGISTRY_TARGET=ip_or_fqdn:port
*	RABBITMQ_TARGET - включение локейшена проксирования в managment ui контейнера rabbitmq. Формат переменной: RABBITMQ_TARGET=ip_or_fqdn:port
*	EIS_TARGET - включение локейшена проксирования в ui контейнера eis. Используется при размещении eis за проксирующим сервером в сетевом сегменте заказчика. Формат переменной: EIS_TARGET=ip_or_fqdn:port
*	ECOS_PAGE_TITLE - настройка заголовка index.html страницы браузера для нового интерфейса (v2). По умолчанию Citeck ECOS
*	EIS_PROTO – протокол, по которому идёт взаимодействие с keycloak. Значение по-умолчанию  https, опционально можно поставить http
* GATEWAY_TLS_ENABLED - включить HTTPS до ecos-gateway (v4)
* GATEWAY_TLS_CERT - корневой сертификат для проверки сертификата ecos-gateway. Можно указать непосредственно тот же сертификат, который использует gateway. По умолчанию цепочка сертификатов проверяется на 2 уровня. По умолчанию false. (v4)
* GATEWAY_TLS_NAME - имя gateway сервера. nginx всегда проверяет хост gateway на соответствие сертификату, но если хост динамический, то можно использовать эту настройку чтобы задать его константой. (v4)
* ENABLE_HTTPS - включает сервер по SERVER_HTTPS_PORT порту и ждет сертификаты SERVER_TLS_CERT и SERVER_TLS_KEY (v3, v4)
* ENABLE_HSTS - добавлять заголовок Strict-Transport-Security к ответам сервера. (v3, v4)
* SERVER_TLS_CERT - сертификат сервера. По умолчанию /app/ssl/ecos-proxy.cert (v4)
* SERVER_TLS_KEY - приватный ключ сервера. По умолчанию /app/ssl/ecos-proxy.key (v4)
* SERVER_HTTP_PORT - http порт, который будет слушать nginx. По умолчанию зависит от пользователя, под которым запускается контейнер. Если это root, то 80, иначе - 8080 (v4)
* SERVER_HTTPS_PORT - https порт, который будет слушать nginx. По умолчанию зависит от пользователя, под которым запускается контейнер. Если это root, то 443, иначе - 8443 (v4)
* MIN_TLS_VER - минимально допустимая версия TLS. Допустимные значения: [1.3, 1.2, 1.0] (v3, v4)

Не реализованы:

*	SOLR_TARGET
*	ECOS_REGISTRY_TARGET (проблема с api)

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
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

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
*	**_JAVA_OPTIONS** - параметры для jvm
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию eureka load balancer, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого cloud config server, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
*	**SPRING_DATASOURCE_URL** - url используемого postgresql datasource
*	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы
~~~~~~~~~~~~~~~~~~~~~~~~
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	cloud config и eureka load balancer используют один и тот же пароль

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
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

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
*	**_JAVA_OPTIONS** - параметры для jvm
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию eureka load balancer, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого cloud config server, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
*	**SPRING_DATA_MONGODB_URI** - url используемого mongodb datasource
*	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы
~~~~~~~~~~~~~~~~~~
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	Cloud config и eureka load balancer используют один и тот же пароль

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

ecos-microservices-postgresql-app
------------------------------------

Назначение
~~~~~~~~~~

Образ, собранный на официальном образе postgresql 12.x с добавлением скрипта инициализации баз данных и пользователей

Теги:
~~~~~~~~~
`nexus.citeck.ru/postrgesql:msvc-latest <nexus.citeck.ru/postrgesql:msvc-latest>`_- собран на базовом образе  postgres:12, используется в композ проектах, файлы конфигурации размещаются в образе

`nexus.citeck.ru/postrgesql:12 <nexus.citeck.ru/postrgesql:12>`_ - базовый образ  postgres:12, размещен в нашем docker registry, используется в k8s объектах, файлы конфигурации и скрипт развертывания конфигурируются через configmap

Базовые образы
~~~~~~~~~~~~~~~

* **postgres:12** 

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::
	
	ecos-microservices-postgresql-app:
		container_name: ecos-microservices-postgresql-app
		hostname: ecos-microservices-postgresql-app
		restart: unless-stopped
		image: nexus.citeck.ru/postgresql:msvc-latest
		stop_grace_period: 1m
		command: ["postgres", "-c", "config_file=/var/lib/postgresql/conf/postgresql.conf"]
		expose:
    		- 5432/tcp
		env_file:
    		- ./env_dir/ecos-microservices-postgresql-app.env
		volumes:
    		- /opt/ecos-microservices-postgresql:/var/lib/postgresql/data
		networks:
		- app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~~

* **ECOS_APPS_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-apps-app

* **ECOS_APPS_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-apps-app

* **ECOS_APPS_APP_DATASOURCE_PASSWORD**  - пароль для мрк ecos-apps-app


* **ECOS_GATEWAY_APP_DATASOURCE_DATABASE**  - база данных для мрк ecos-gateway-app

* **ECOS_GATEWAY_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-gateway-app

* **ECOS_GATEWAY_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-gateway-app

 

* **ECOS_UISERV_APP_DATASOURCE_DATABASE**  - база данных для мрк ecos-uiserv-app

* **ECOS_UISERV_APP_DATASOURCE_USERNAME**  - пользователь для мрк ecos-uiserv-app

* **ECOS_UISERV_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-uiserv-app

 

* **ECOS_INTEGRATIONS_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-integrations-app

* **ECOS_INTEGRATIONS_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-integrations-app

* **ECOS_INTEGRATIONS_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-integrations-app
 

* **ECOS_MODEL_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-model-app

* **ECOS_MODEL_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-model-app

* **ECOS_MODEL_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-model-app
 

* **ECOS_NOTIFICATIONS_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-notifications-app

* **ECOS_NOTIFICATIONS_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-notifications-app

* **ECOS_NOTIFICATIONS_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-notifications-app
 

* **ECOS_HISTORY_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-history-app

* **ECOS_HISTORY_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-history-app

* **ECOS_HISTORY_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-history-app

 

* **POSTGRES_PASSWORD** - обязательный параметр за исключением **POSTGRES_HOST_AUTH_METHOD=trust**, пароль привилегированного пользователя  **postgres**

* **POSTGRES_USER** - переопределение дефолтного пользователя **postgres**

* **POSTGRES_DB** - переопределение дефолтной базы данных

* **POSTGRES_INITDB_ARGS** - дополнительные параметры для инициализации кластера

* **POSTGRES_INITDB_WALDIR** - переопределение дефолтной директории хранения логов транзакций

* **POSTGRES_HOST_AUTH_METHOD** - метод аутентификации host подключений для **всех бд**, пользователей и адресов в pg_hba.conf. Дефолтное значение **md5**

* **PGDATA** - переопределение дефолтной директории хранения фалов инициируемого кластера

Известные проблемы:
~~~~~~~~~~~~~~~~~~~~

* Не реализована возможность конфигурирования датасорсов (добавление/удаление баз данных, пользователей) после первичного развертывания
* Отсутствие конфигурации используемых схем
* Конфигурирование postgresql только через пересборку образа с внесением изменений в конфигурационные файлы

Типовой вывод принятых настроек в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

	The files belonging to this database system will be owned by user "postgres".
	This user must also own the server process.

	The database cluster will be initialized with locale "en_US.utf8".
	The default database encoding has accordingly been set to "UTF8".
	The default text search configuration will be set to "english".

	Data page checksums are disabled.

	fixing permissions on existing directory /var/lib/postgresql/data ... ok
	creating subdirectories ... ok
	selecting dynamic shared memory implementation ... posix
	selecting default max_connections ... 100
	selecting default shared_buffers ... 128MB
	selecting default time zone ... UTC
	creating configuration files ... ok
	running bootstrap script ... ok
	performing post-bootstrap initialization ... sh: locale: not found
	2020-04-28 08:59:20.042 UTC [30] WARNING:  no usable system locales were found
	ok
	syncing data to disk ... initdb: warning: enabling "trust" authentication for local connections
	You can change this by editing pg_hba.conf or using the option -A, or
	--auth-local and --auth-host, the next time you run initdb.
	ok


	Success. You can now start the database server using:

		pg_ctl -D /var/lib/postgresql/data -l logfile start

	waiting for server to start....2020-04-28 08:59:20.503 UTC [35] LOG:  starting PostgreSQL 12.2 on x86_64-pc-linux-musl, compiled by gcc (Alpine 9.2.0) 9.2.0, 64-bit
	2020-04-28 08:59:20.506 UTC [35] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
	2020-04-28 08:59:20.555 UTC [36] LOG:  database system was shut down at 2020-04-28 08:59:20 UTC
	2020-04-28 08:59:20.563 UTC [35] LOG:  database system is ready to accept connections
	done
	server started

	/usr/local/bin/docker-entrypoint.sh: sourcing /docker-entrypoint-initdb.d/init-db.sh
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT

	waiting for server to shut down....2020-04-28 08:59:21.371 UTC [35] LOG:  received fast shutdown request
	2020-04-28 08:59:21.374 UTC [35] LOG:  aborting any active transactions
	2020-04-28 08:59:21.376 UTC [35] LOG:  background worker "logical replication launcher" (PID 42) exited with exit code 1
	2020-04-28 08:59:21.376 UTC [37] LOG:  shutting down
	2020-04-28 08:59:21.409 UTC [35] LOG:  database system is shut down
	done
	server stopped

	PostgreSQL init process complete; ready for start up.

	2020-04-28 08:59:21.494 UTC [1] LOG:  starting PostgreSQL 12.2 on x86_64-pc-linux-musl, compiled by gcc (Alpine 9.2.0) 9.2.0, 64-bit
	2020-04-28 08:59:21.494 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
	2020-04-28 08:59:21.494 UTC [1] LOG:  listening on IPv6 address "::", port 5432
	2020-04-28 08:59:21.502 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
	2020-04-28 08:59:21.538 UTC [46] LOG:  database system was shut down at 2020-04-28 08:59:21 UTC
	2020-04-28 08:59:21.542 UTC [1] LOG:  database system is ready to accept connections

ecos-history-app
----------------

Назначение:
~~~~~~~~~~~~

Образ микросервиса для хранения истории, статистики по задачам и фасаду аттрибутов.

Теги:
~~~~~~~~

`nexus.citeck.ru/ecos-history <nexus.citeck.ru/ecos-history>`_ :<tag>

Базовые образы:
~~~~~~~~~~~~~~~~
* **openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

	ecos-history:
		logging:
		options:
			max-size: "10m"
			max-file: "5"
		image: nexus.citeck.ru/ecos-history:<ECOS_HISTORY_APP_IMAGE
		container_name: ecos-history
		hostname: ecos-history
		restart: unless-stopped
		stop_grace_period: 1m
		environment:
    		- JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
    		- _JAVA_OPTIONS=-Xmx256m -Xms256m
    		- SPRING_PROFILES_ACTIVE=<ECOS-HISTORY_PROFILES
    		- EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
    		- SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/config
    		- SPRING_DATASOURCE_URL=<ECOS_HISTORY_DATASOURCE
    		- SPRING_DATASOURCE_USERNAME=alfresco
    		- SPRING_DATASOURCE_PASSWORD=alfr3sc0
    		- SPRING_DATA_MONGODB_URI=<SPRING_DATA_MONGODB_URI
    		- SPRING_DATA_MONGODB_DATABASE=ecos-history
    		- ECOS-HISTORY_RECOVER_SOURCEFOLDER=/source
    		- ECOS-HISTORY_RECOVER_ERRORSFOLDER=/errors
    		- ECOS-HISTORY_ALFRESCO_TENANTID=<ALFRESCO_TENANT_ID
    		- ECOS-HISTORY_EVENT_HOST=<ECOS-HISTORY_EVENT_HOST
    		- ECOS-HISTORY_EVENT_PORT=<ECOS-HISTORY_EVENT_PORT
    		- ECOS-HISTORY_EVENT_USERNAME=<ECOS-HISTORY_EVENT_USERNAME
    		- ECOS-HISTORY_EVENT_PASSWORD=<ECOS-HISTORY_EVENT_PASSWORD
    		- JHIPSTER_SLEEP=1200 # gives time for the JHipster Registry to boot before the application
		expose:
    		- 8086/tcp
		volumes:
    		- /opt/micro/ecos-history/source:/source
    		- /opt/micro/ecos-history/errors:/errors
		networks:
    		- app_network
		depends_on:
    		- ecos
    		- ecos-postgresql
    		- rabbitmq

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **JHIPSTER_REGISTRY_PASSWORD** - пароль аутентификации jhipster

* **_JAVA_OPTIONS** - параметры для **jvm**

* **SPRING_PROFILES_ACTIVE** - профили развертывания приложения

* **EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - **url** регистрации микросервиса в сервисе балансировки

* **SPRING_CLOUD_CONFIG_URI** - **url** параметров конфигурации

* **SPRING_DATASOURCE_URL** - **url postgresql** инстанса с бд хренения истории

* **SPRING_DATASOURCE_USERNAME** - логин пользователя для бд хренения истории

* **SPRING_DATASOURCE_PASSWORD** - пароль пользователя для бд хранения истории

* **SPRING_DATA_MONGODB_URI** - **url mongodb** инстанса для хранения history/task records атрибутов нод

* **SPRING_DATA_MONGODB_DATABASE** - бд хранения history/task records атрибутов нод

* **ECOS-HISTORY_RECOVER_SOURCEFOLDER** - **резервный** датасорс очереди событий истории 

* **ECOS-HISTORY_RECOVER_ERRORSFOLDER** - **резервный** датасорс хранения ошибок обработки очереди событий истории

* **ECOS-HISTORY_ALFRESCO_TENANTID** - **tenantid** развернутого деплоя ecos

* **ECOS-HISTORY_EVENT_HOST** - адрес диспетчера очередей

* **ECOS-HISTORY_EVENT_PORT** -  **amqp**  порт диспетчера очередей

* **ECOS-HISTORY_EVENT_USERNAME** - логин пользователя для диспетчера очередей

* **ECOS-HISTORY_EVENT_PASSWORD** - пароль пользователя для диспетчера очередей

* **JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы:
~~~~~~~~~~~~~~~~~~~~~~

* Расхождения в формирования url в микросервисах, использующих в качестве датасорса mongodb

* Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса

Дополнительно:
~~~~~~~~~~~~~~~~~~

* Документация по `spring cloud config  <https://cloud.spring.io/spring-cloud-config/reference/html/#_spring_cloud_config_server>`_

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

	ecos-history                | ----------------------------------------------------------
	ecos-history                |   Application 'history' is running! Access URLs:
	ecos-history                |   Local:          http://localhost:8086/
	ecos-history                |   External:       http://172.18.0.27:8086/
	ecos-history                |   Profile(s):     [prod, swagger, facade]
	ecos-history                | ----------------------------------------------------------
	ecos-history                | 2020-05-06 10:51:52.991  INFO 1 --- [           main] ru.citeck.ecos.history.HistoryApp        : 
	ecos-history                | ----------------------------------------------------------
	ecos-history                |   Config Server:  Connected to the JHipster Registry running in Docker
	ecos-history                | ----------------------------------------------------------




rabbitmq-app
--------------

Назначение:
~~~~~~~~~~~~

Образ брокера сообщений Rabbitmq

Теги:
~~~~~

**rabbitmq:3.7.18-management-alpine** - используется официальный образ

Базовые образы:
~~~~~~~~~~~~~~~~~~

* **rabbitmq:3.7.18-management-alpine** - образ версии 3.7.18 c интегрированным плагином managment на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

	rabbitmq:
		logging:
		options:
			max-size: "10m"
			max-file: "5"
		image: "rabbitmq:3.7.18-management-alpine"
		restart: unless-stopped
		stop_grace_period: 1m
		container_name: rabbitmq
		hostname: rabbitmq
		environment:
            - RABBITMQ_DEFAULT_USER=rabbitmqadmin
            - RABBITMQ_DEFAULT_PASS=LKSjdlkj847Klhfc
            - RABBITMQ_DEFAULT_VHOST=/
        expose:
            - 15672/tcp
        ports: 
            - 35672:5672
        volumes:
            - /opt/rabbitmqdata:/var/lib/rabbitmq
        networks:
            - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~

* **RABBITMQ_DEFAULT_USER** - логин создаваемого пользователя по умолчанию

* **RABBITMQ_DEFAULT_PASS** - пароль пользователя

* **RABBITMQ_DEFAULT_VHOST** - создаваемый виртуальный хост

Известные проблемы:
~~~~~~~~~~~~~~~~~~~~~~~

* k8s после пересоздания пода при условии что приложение развернуто как statesful контейнер уходит в crash loopback

* Не реализовано конфигурирование дополнительных виртуальных хостов, пользователей, наделение правами пользователей

Типовой вывод успешного развертывания в лог контейнера:

.. code-block::

	rabbitmq                    | 2020-05-12 20:35:36.412 [info] <0.8.0> Feature flags: list of feature flags found:
	rabbitmq                    | 2020-05-12 20:35:36.413 [info] <0.8.0> Feature flags: feature flag states written to disk: yes
	rabbitmq                    | 2020-05-12 20:35:36.754 [info] <0.264.0> 
	rabbitmq                    |  Starting RabbitMQ 3.7.18 on Erlang 22.1.1
	rabbitmq                    |  Copyright (C) 2007-2019 Pivotal Software, Inc.
	rabbitmq                    |  Licensed under the MPL.  See https://www.rabbitmq.com/
	rabbitmq                    | 
	rabbitmq                    |   ##  ##
	rabbitmq                    |   ##  ##      RabbitMQ 3.7.18. Copyright (C) 2007-2019 Pivotal Software, Inc.
	rabbitmq                    |   ##########  Licensed under the MPL.  See https://www.rabbitmq.com/
	rabbitmq                    |   ######  ##
	rabbitmq                    |   ##########  Logs: <stdout>
	rabbitmq                    | 
	rabbitmq                    |               Starting broker...
	rabbitmq                    | 2020-05-12 20:35:36.756 [info] <0.264.0> 
	rabbitmq                    |  node           : rabbit@rabbitmq
	rabbitmq                    |  home dir       : /var/lib/rabbitmq
	rabbitmq                    |  config file(s) : /etc/rabbitmq/rabbitmq.conf
	rabbitmq                    |  cookie hash    : 69+WXGG5CrjDEU7Bmh7IbA==
	rabbitmq                    |  log(s)         : <stdout>
	rabbitmq                    |  database dir   : /var/lib/rabbitmq/mnesia/rabbit@rabbitmq
	rabbitmq                    | 2020-05-12 20:35:36.807 [info] <0.264.0> Running boot step pre_boot defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.807 [info] <0.264.0> Running boot step rabbit_core_metrics defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.808 [info] <0.264.0> Running boot step rabbit_alarm defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.843 [info] <0.284.0> Memory high watermark set to 6202 MiB (6504172748 bytes) of 15507 MiB (16260431872 bytes) total
	rabbitmq                    | 2020-05-12 20:35:36.900 [info] <0.301.0> Enabling free disk space monitoring
	rabbitmq                    | 2020-05-12 20:35:36.900 [info] <0.301.0> Disk free limit set to 50MB
	rabbitmq                    | 2020-05-12 20:35:36.924 [info] <0.264.0> Running boot step code_server_cache defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.924 [info] <0.264.0> Running boot step file_handle_cache defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.925 [info] <0.316.0> FHC read buffering:  OFF
	rabbitmq                    | 2020-05-12 20:35:36.925 [info] <0.316.0> FHC write buffering: ON
	rabbitmq                    | 2020-05-12 20:35:36.924 [info] <0.315.0> Limiting to approx 1048476 file handles (943626 sockets)
	rabbitmq                    | 2020-05-12 20:35:36.929 [info] <0.264.0> Running boot step worker_pool defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.929 [info] <0.265.0> Will use 4 processes for default worker pool
	rabbitmq                    | 2020-05-12 20:35:36.929 [info] <0.265.0> Starting worker pool 'worker_pool' with 4 processes in it
	rabbitmq                    | 2020-05-12 20:35:36.930 [info] <0.264.0> Running boot step database defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:36.955 [info] <0.264.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
	rabbitmq                    | 2020-05-12 20:35:37.025 [info] <0.264.0> Waiting for Mnesia tables for 30000 ms, 9 retries left
	rabbitmq                    | 2020-05-12 20:35:37.025 [info] <0.264.0> Peer discovery backend rabbit_peer_discovery_classic_config does not support registration, skipping registration.
	rabbitmq                    | 2020-05-12 20:35:37.025 [info] <0.264.0> Running boot step database_sync defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.025 [info] <0.264.0> Running boot step feature_flags defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step codec_correctness_check defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step external_infrastructure defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step rabbit_registry defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step rabbit_auth_mechanism_cr_demo defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step rabbit_queue_location_random defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.030 [info] <0.264.0> Running boot step rabbit_event defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_auth_mechanism_amqplain defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_auth_mechanism_plain defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_exchange_type_direct defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_exchange_type_fanout defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.031 [info] <0.264.0> Running boot step rabbit_exchange_type_headers defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_exchange_type_topic defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_mirror_queue_mode_all defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_mirror_queue_mode_exactly defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_mirror_queue_mode_nodes defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_priority_queue defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Priority queues enabled, real BQ is rabbit_variable_queue
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_queue_location_client_local defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_queue_location_min_masters defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step kernel_ready defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.032 [info] <0.264.0> Running boot step rabbit_sysmon_minder defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.033 [info] <0.264.0> Running boot step rabbit_epmd_monitor defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.067 [info] <0.264.0> Running boot step guid_generator defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.069 [info] <0.264.0> Running boot step rabbit_node_monitor defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.070 [info] <0.343.0> Starting rabbit_node_monitor
	rabbitmq                    | 2020-05-12 20:35:37.070 [info] <0.264.0> Running boot step delegate_sup defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.070 [info] <0.264.0> Running boot step rabbit_memory_monitor defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.071 [info] <0.264.0> Running boot step core_initialized defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.071 [info] <0.264.0> Running boot step upgrade_queues defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_connection_tracking defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_connection_tracking_handler defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_exchange_parameters defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_mirror_queue_misc defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.100 [info] <0.264.0> Running boot step rabbit_policies defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.101 [info] <0.264.0> Running boot step rabbit_policy defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.101 [info] <0.264.0> Running boot step rabbit_queue_location_validator defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.101 [info] <0.264.0> Running boot step rabbit_vhost_limit defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.101 [info] <0.264.0> Running boot step rabbit_mgmt_reset_handler defined by app rabbitmq_management
	rabbitmq                    | 2020-05-12 20:35:37.102 [info] <0.264.0> Running boot step rabbit_mgmt_db_handler defined by app rabbitmq_management_agent
	rabbitmq                    | 2020-05-12 20:35:37.102 [info] <0.264.0> Management plugin: using rates mode 'basic'
	rabbitmq                    | 2020-05-12 20:35:37.102 [info] <0.264.0> Running boot step recovery defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.113 [info] <0.446.0> Making sure data directory '/var/lib/rabbitmq/mnesia/rabbit@rabbitmq/msg_stores/vhosts/628WB79CIFDYO9LJI6DKMI09L' for vhost '/' exists
	rabbitmq                    | 2020-05-12 20:35:37.117 [info] <0.446.0> Starting message stores for vhost '/'
	rabbitmq                    | 2020-05-12 20:35:37.117 [info] <0.450.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_transient": using rabbit_msg_store_ets_index to provide index
	rabbitmq                    | 2020-05-12 20:35:37.119 [info] <0.446.0> Started message store of type transient for vhost '/'
	rabbitmq                    | 2020-05-12 20:35:37.119 [info] <0.453.0> Message store "628WB79CIFDYO9LJI6DKMI09L/msg_store_persistent": using rabbit_msg_store_ets_index to provide index
	rabbitmq                    | 2020-05-12 20:35:37.124 [info] <0.446.0> Started message store of type persistent for vhost '/'
	rabbitmq                    | 2020-05-12 20:35:37.352 [info] <0.264.0> Running boot step load_definitions defined by app rabbitmq_management
	rabbitmq                    | 2020-05-12 20:35:37.352 [info] <0.264.0> Running boot step empty_db_check defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.352 [info] <0.264.0> Running boot step rabbit_looking_glass defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.352 [info] <0.264.0> Running boot step rabbit_core_metrics_gc defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.353 [info] <0.264.0> Running boot step background_gc defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.353 [info] <0.264.0> Running boot step connection_tracking defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.353 [info] <0.264.0> Setting up a table for connection tracking on this node: tracked_connection_on_node_rabbit@rabbitmq
	rabbitmq                    | 2020-05-12 20:35:37.353 [info] <0.264.0> Setting up a table for per-vhost connection counting on this node: tracked_connection_per_vhost_on_node_rabbit@rabbitmq
	rabbitmq                    | 2020-05-12 20:35:37.354 [info] <0.264.0> Running boot step routing_ready defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.354 [info] <0.264.0> Running boot step pre_flight defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.354 [info] <0.264.0> Running boot step notify_cluster defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.354 [info] <0.264.0> Running boot step networking defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.362 [info] <0.704.0> started TCP listener on [::]:5672
	rabbitmq                    | 2020-05-12 20:35:37.362 [info] <0.264.0> Running boot step direct_client defined by app rabbit
	rabbitmq                    | 2020-05-12 20:35:37.430 [info] <0.754.0> Management plugin: HTTP (non-TLS) listener started on port 15672
	rabbitmq                    | 2020-05-12 20:35:37.430 [info] <0.860.0> Statistics database started.
	rabbitmq                    | 2020-05-12 20:35:37.431 [info] <0.859.0> Starting worker pool 'management_worker_pool' with 3 processes in it
	rabbitmq                    |  completed with 3 plugins.
	rabbitmq                    | 2020-05-12 20:35:37.739 [info] <0.8.0> Server startup complete; 3 plugins started.
	rabbitmq                    |  * rabbitmq_management
	rabbitmq                    |  * rabbitmq_management_agent
	rabbitmq                    |  * rabbitmq_web_dispatch

ecos-apps-app
--------------

Назначение:
~~~~~~~~~~~~

Образ микросервиса, управляющего деплоем приложений и модулей ECOS

Теги:
~~~~~~~

`nexus.citeck.ru/ecos-apps <nexus.citeck.ru/ecos-apps>`_ :<tag> - сборка проекта ecos-apps

Базовые образы:
~~~~~~~~~~~~~~~~

* **openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

 ecos-apps:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    image: nexus.citeck.ru/ecos-apps:<ECOS_APPS_IMAGE
    container_name: ecos-apps
    stop_grace_period: 1m
    hostname: ecos-apps
    restart: on-failure:5
    depends_on:
      - ecosapps-postgresql
    environment:
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - _JAVA_OPTIONS=-Xmx256m -Xms256m
      - SPRING_PROFILES_ACTIVE=prod,swagger
      - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
      - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/config
      - SPRING_DATASOURCE_URL=jdbc:postgresql://ecosapps-postgresql:5432/eapps
      - JHIPSTER_SLEEP=60 # gives time for the JHipster Registry to boot before the application
 #    ports:
 #    - 8089:8089
    networks:
      - app_network
  ecosapps-postgresql:
    container_name: ecosapps-postgresql
    hostname: ecosapps-postgresql
    restart: unless-stopped
    image: postgres:10.4
    stop_grace_period: 1m
    environment:
      - POSTGRES_USER=eapps
      - POSTGRES_PASSWORD=
    volumes:
      - /opt/micro/postgresql/ecosapps:/var/lib/postgresql/data
    networks:
      - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~

* **_JAVA_OPTIONS** - параметры для **jvm**

* **SPRING_PROFILES_ACTIVE** - используемые при развертывании профили

* **EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials

* **SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials

* **JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**

* **SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**

* **JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы:
~~~~~~~~~~~~~~~~~~~~~~~~

* Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса

* Использование empty password в доступах к датасорсам

* cloud config и eureka load balancer используют один и тот же пароль

Дополнительно:
~~~~~~~~~~~~~~~

Документация по использованию микросервиса Apps microservice 

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

	ecos-apps                   | ----------------------------------------------------------
	ecos-apps                   |   Application 'eapps' is running! Access URLs:
	ecos-apps                   |   Local:          http://localhost:8089/
	ecos-apps                   |   External:       http://172.25.0.19:8089/
	ecos-apps                   |   Profile(s):     [prod, swagger]
	ecos-apps                   | ----------------------------------------------------------
	ecos-apps                   | 2020-05-13 08:40:19.215  INFO 1 --- [           main] ru.citeck.ecos.apps.EcosAppsApp          : 
	ecos-apps                   | ----------------------------------------------------------
	ecos-apps                   |   Config Server:  Connected to the JHipster Registry running in Docker
	ecos-apps                   | ----------------------------------------------------------


eis (Keycloack)
----------------

Назначение:
~~~~~~~~~~~~

Теги:
~~~~~~

Базовые образы:
~~~~~~~~~~~~~~~

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

	eis:
		logging:
		options:
			max-size: "10m"
			max-file: "5"
		image: docker.io/jboss/keycloak:10.0.1
		container_name: eis
		hostname: eis
		restart:  unless-stopped
		environment:
			PROXY_ADDRESS_FORWARDING: "true"
			DB_VENDOR: POSTGRES
			DB_ADDR: eis_postgres
			DB_DATABASE: keycloak
			DB_USER: keycloak
			DB_SCHEMA: public
			DB_PASSWORD: LklsdkkuOIUjkh
			KEYCLOAK_USER: admin
			KEYCLOAK_PASSWORD: ERRESkhlu7iu4hkhjfd
				# Uncomment the line below if you want to specify JDBC parameters. The parameter below is just an example, and it shouldn't be used in production without knowledge. It is highly recommended that you read the PostgreSQL JDBC driver documentation in order to use it.
				#JDBC_PARAMS: "ssl=true"
		ports:
    		- 443:8443
		depends_on:
    		- eis_postgres
		networks:
    		- app_network
    eis_postgres:
		image: postgres:11
		container_name: eis_postgres
		hostname: eis_postgres
		volumes:
            - /opt/postgresql/keycloak:/var/lib/postgresql/data
        environment:
			POSTGRES_DB: keycloak
			POSTGRES_USER: keycloak
			POSTGRES_PASSWORD: LklsdkkuOIUjkh
        networks:
            - app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~

Известные проблемы:
~~~~~~~~~~~~~~~~~~~~
 

Дополнительно:
~~~~~~~~~~~~~~~
 

Типовой вывод успешного развертывания в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

backup-tool-app
----------------

Назначение:
~~~~~~~~~~~~

Образ для создания бекапов.

Создан на базе решения `Backup 4.4.1.  <https://github.com/backup/backup>`_
Документация находится `тут  <http://backup.github.io/backup/v4/>`_

Выключен по умолчанию.

Исходники находятся в репозитории `https://gitlab.citeck.ru/citeck-projects/citeck-devops <https://gitlab.citeck.ru/citeck-projects/citeck-devops/>`_

Теги:
~~~~~~

Актуальная версия `nexus.citeck.ru/backup-tool <nexus.citeck.ru/backup-tool>`_ 0.0.3
UPD:  По сравнению с предыдущей версией ( 0.0.2 ) поправлены СА серты R3 и актуализированы версии вспомогательных утилит.

Шаблон сервиса docker-compose:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

	services:
		app:
			logging:
			 options:
				max-size: "10m"
				max-file: "5"
			 hostname: backup-tool-app
			 restart: always
			 stop_grace_period: 1m
			image: nexus.citeck.ru/backup-tool:0.0.2
			env_file:
			 - ./environments/backup-tool-app.env
			volumes:
		{% if (BackupToolApp.environments.backup.contentstore)and(EcosApp.enabled) %}
			- {{ EcosProjectDataDir }}ecos-app/:/content/
		{% endif %}
		{% if (BackupToolApp.environments.backup.index) and (EcosSearchApp.enabled) %}
			- {{ EcosProjectDataDir }}ecos-search-app/:/index/
		{% endif %}
		{% if BackupToolApp.environments.export.local.enabled %}
			- {{ EcosProjectDataDir }}backups/:/backups/
		{% endif %}
			networks:
			- app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~~

Пример ожидаемых переменных в ``backup-tool-app.env`` с значениями по умолчанию:

  * **BACKUP_SHEDULE=”0 0 * * *”**
    
  * **BACKUP_DEBUG_CONFIG=false**
    
  * **BACKUP_INSTANCE_ID=local.dev**
    
  * **BACKUP_CONTENTSTORE=false**
    
  * **BACKUP_INDEX=false**
    
  * **BACKUP_POSTGRESQL_APP_1=false**

  * **BACKUP_POSTGRESQL_APP_1_HOST=ecos-postgresql-app**
    
  * **BACKUP_POSTGRESQL_APP_1_PORT=5432**
    
  * **BACKUP_POSTGRESQL_APP_1_USERNAME=user**
    
  * **BACKUP_POSTGRESQL_APP_1_PASSWORD=password**
    
  * **BACKUP_POSTGRESQL_APP_2=false**
    
  * **BACKUP_POSTGRESQL_APP_2_HOST=ecos-microservices-postgresql-app**
    
  * **BACKUP_POSTGRESQL_APP_2_PORT=5432**
    
  * **BACKUP_POSTGRESQL_APP_2_USERNAME=user**
    
  * **BACKUP_POSTGRESQL_APP_2_PASSWORD=password**
    
  * **BACKUP_MONGODB_APP_1=false**

  * **BACKUP_MONGODB_APP_1_HOST=mongodb-app**
    
  * **BACKUP_MONGODB_APP_1_PORT=27017**
    
  * **BACKUP_MONGODB_APP_1_USERNAME=user**
    
  * **BACKUP_MONGODB_APP_1_PASSWORD=password**
    
  * **BACKUP_MYSQL_APP_1=false**
    
  * **BACKUP_MYSQL_APP_1_HOST=mysql-app**
    
  * **BACKUP_MYSQL_APP_1_PORT=3306**
    
  * **BACKUP_MYSQL_APP_1_USERNAME=user**
    
  * **BACKUP_MYSQL_APP_1_PASSWORD=password**

  * **BACKUP_LOCAL_EXPORT=false**
    
  * **BACKUP_LOCAL_EXPORT_KEEP=7**
    
  * **BACKUP_S3_EXPORT=false**
    
  * **BACKUP_S3_EXPORT_USE_FOG_OPTIONS=true**
    
  * **BACKUP_S3_EXPORT_ENDPOINT=s3.citeck.ru**
    
  * **BACKUP_S3_EXPORT_REGION=**
    
  * **BACKUP_S3_EXPORT_KEY=changemeplease**
    
  * **BACKUP_S3_EXPORT_SECRET=changemeplease**
    
  * **BACKUP_S3_EXPORT_BUCKET=bucket**
    
  * **BACKUP_S3_EXPORT_KEEP=7**
    
  * **BACKUP_MATTERMOST_NOTIFICATIONS=false**
    
  * **BACKUP_MATTERMOST_NOTIFICATIONS_WEBHOOK=changemeplease**
    
  * **BACKUP_MATTERMOST_NOTIFICATIONS_CHANNEL=channel**

``BACKUP_POSTGRESQL_APP_*``

``BACKUP_MONGODB_APP_*``

``BACKUP_MYSQL_APP_*``

Отвечают за авторизацию в субд. При использовании шаблонизатора docker-compose значения полей подставляются автоматически. Эти параметры в большинстве случаев нет необходимости предопределять.

* **BACKUP_SHEDULE** - Как часто необходимо делать бекапы. Задается в формате cron. По умолчанию ежедневно в 00:00. p.s. `вот удобный калькулятор <https://crontab.guru/>`_

* **BACKUP_DEBUG_CONFIG** - Возвращает список переменных и сконфигурированый backup_plan.rb.

* **BACKUP_INSTANCE_ID** - Имя инстанса. Используется для оповещений в mattermost и для экспорта в S3.

* **BACKUP_CONTENTSTORE** - Включает бекапы для ``ecos-app`` ``contentstore``.

* **BACKUP_INDEX** - Включает бекапы для ``ecos-search-app`` ``index``.

* **BACKUP_LOCAL_EXPORT** - Включает хранение бекапов на сервере, в директории ``backups/``.

* **BACKUP_LOCAL_EXPORT_KEEP** - Сколько дней хранить бекапы в директории ``backups/``. Зависит о частоты выполнения бекап плана.

* **BACKUP_S3_EXPORT** - Включает экспорт бекапов в S3 хранилище.

* **BACKUP_S3_EXPORT_USE_FOG_OPTIONS** - Переключатель необходимый для использования в S3-like хранилищах, например в `DigitalOcean’s Spaces <https://developers.digitalocean.com/documentation/v2/>`_ или `Minio <https://www.minio.io/>`_. Использует в качестве хоста переменную BACKUP_S3_EXPORT_ENDPOINT. Более подробно в `документации <https://backup.github.io/backup/v4/storage-s3/>`_ 

* **BACKUP_S3_EXPORT_ENDPOINT** - Адрес S3-like сервера. Зависит от значения ``true`` переменной BACKUP_S3_EXPORT_USE_FOG_OPTIONS.

* **BACKUP_S3_EXPORT_REGION** - Регион для amazon S3. 

* **BACKUP_S3_EXPORT_KEY** - S3 ключ авторизации.

* **BACKUP_S3_EXPORT_SECRET** - S3 сикрет авторизации.

* **BACKUP_S3_EXPORT_BUCKET** - Ведерко, куда складывать бекапы в S3.

* **BACKUP_S3_EXPORT_KEEP** - Сколько дней хранить бекапы в S3 хранилище. Зависит о частоты выполнения бекап плана.

* **BACKUP_MATTERMOST_NOTIFICATIONS** - Включает отправку уведомлений в mattermost / slack.

* **BACKUP_MATTERMOST_NOTIFICATIONS_WEBHOOK** - Полный адрес webhook, куда нужно отправлять уведомления. `Например <https://mm.citeck.ru/hooks/apbhdnp72djpexxmofkywptyy>`_.

* **BACKUP_MATTERMOST_NOTIFICATIONS_CHANNEL** - Канал в mattermost / slack для уведомлений.

Типовой вывод принятых настроек в лог контейнера:
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

	17:27:10.INFO  ==> ** Starting Backup plan setup **
	17:27:10.INFO  ==> ** Export to s3 storage disabled **
	17:27:10.INFO  ==> ** Export to local storage disabled **
	17:27:10.INFO  ==> ** Disabled mattermost notification **
	17:27:11.INFO  ==> ** Generation of the configuration file /opt/backup/backup_plan.rb completed successfully **
	17:27:11.INFO  ==> ** Configuration check completed successfully **
	17:27:11.INFO  ==> ** Backup plan setup finished! **

	17:27:11.INFO  ==> ** Сonfiguring the scheduler **
	17:27:11.INFO  ==> ** Schedule applied: 0 0 * * * **

ecos-alfresco-search-service
-----------------------------

Назначение:
~~~~~~~~~~~~

Образ с установленным контейнером сервлетов Tomcat с вебархивом проекта ecos-alfresco-search-service (solr6)

Теги:
~~~~~~

`nexus.citeck.ru/ecos-alfresco-search-service <nexus.citeck.ru/ecos-alfresco-search-service>`_ :<tag>

Базовые образы
~~~~~~~~~~~~~~

* **alfresco/alfresco-base-java:11.0.1-openjdk-centos-7-3e4e9f4e5d6a** базовый образ tomcat/java от alfresco,  openjdk version "11.0.1-openjdk"

Шаблон сервиса docker-compose
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

	ecos-alfresco-search-services:
		logging:
		 options:
			max-size: "10m"
			max-file: "5"
		image: nexus.citeck.ru/ecos-alfresco-search-services:<ECOS_SOLR6
		restart: unless-stopped
		stop_grace_period: 1m
		container_name: ecos-alfresco-search-services
		hostname: ecos-alfresco-search-services
		ports:
    		- 8983:8983
		env_file:
  		- ./env_dir/ecos-search-service-app.env
		volumes:
    		- /opt/ecos-alfresco-search-services/contentstore:/opt/ecos-alfresco-search-services/contentstore
    		- /opt/ecos-alfresco-search-services/data:/opt/ecos-alfresco-search-services/data
		networks:
    		- app_network

Используемые переменные:
~~~~~~~~~~~~~~~~~~~~~~~~~

* **ALFRESCO_HOST** - fqdn/ip инстанса ecos

* **ALFRESCO_PORT** - http порт инстанса ecos 

* **ALFRESCO_PORT_SSL** - https порт инстанса ecos 

* **SOLR_SOLR_HOST** - fqdn/ip инстанса solr

* **SOLR_SOLR_PORT** - http порт инстанса solr

* **SOLR_CITECK_MERGE_FACTOR** - мерж фактор solr/lucene, используемый при определении необходимости мержить сегменты.

* **SOLR_ALFRESCO_INDEX_TRANSFORM_CONTENT** - если true - будет происходить конвертация контента в текст и его последующая пословесная индексация. Если false - будут индексироваться только метаданные  (mimetype, size, etc).

* **SOLR_ALFRESCO_RECORD_UNINDEXED_NODES** - если true - ноды, типы которых отмечены как “неиндексируемые” - будут попадать в индекс в качестве документа без индексации атрибутов ноды. Если false - такие документы будут игнорироваться при индексации.

* **SOLR_CITECK_RECORD_TRANSACTIONS** - если true - каждая транзакция будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях будут храниться только в кеше, в памяти.

* **SOLR_CITECK_TX_CONSISTENCY_CHECK_MODE** - тип проверки консистентности индекса и базы для индексации транзакций. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.

* **SOLR_CITECK_TX_IS_INDEXED_CACHE_SIZE** - размер кеша, если CITECK_RECORD_TRANSACTIONS = false.

* **SOLR_CITECK_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT** - коэффициент чистки кеша при переполнении, если CITECK_RECORD_TRANSACTIONS = false.

* **SOLR_CITECK_RECORD_ACL_TRANSACTIONS** - если true - каждая транзакция прав будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях прав будут храниться только в кеше, в памяти.

* **SOLR_CITECK_ACL_CONSISTENCY_CHECK_MODE** - тип проверки консистентности индекса и базы для индексации транзакций прав. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.

* **SOLR_CITECK_ACL_TX_IS_INDEXED_CACHE_SIZE** - размер кеша, если CITECK_RECORD_ACL_TRANSACTIONS = false.

* **SOLR_CITECK_ACL_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT** - коэффициент чистки кеша при переполнении, если CITECK_RECORD_ACL_TRANSACTIONS = false.

* **SOLR_OPTS** - параметры для **jvm**

**Настройки SSL:**

По умолчанию SSL включён в микросервисе, при старте необходимо указать следующие environments

.. code-block::

	SOLR_SSL_KEY_STORE: /opt/ecos-alfresco-search-services/keystores/ssl.repo.client.keystore
	SOLR_SSL_KEY_STORE_PASSWORD: kT9X6oe68t
	SOLR_SSL_KEY_STORE_TYPE: JCEKS
	SOLR_SSL_TRUST_STORE: /opt/ecos-alfresco-search-services/keystores/ssl.repo.client.truststore
	SOLR_SSL_TRUST_STORE_PASSWORD: kT9X6oe68t
	SOLR_SSL_TRUST_STORE_TYPE: JCEKS
	SOLR_SSL_NEED_CLIENT_AUTH: true
	SOLR_SSL_WANT_CLIENT_AUTH: false

Для отключения SSL проверяем что у нас не устанавливаться environments выше, иначе обнуляем значения этих environments. Затем устанавливаем **ALFRESCO_SECURE_COMMS** =none

Для установки своих ключей достаточно примонтировать в директорию микросервиса ``/opt/ecos-alfresco-search-services/`` свои ключи.
Содержимое папки должно быть следующим:

.. code-block::

	ssl.repo.client.keystore
	ssl.repo.client.truststore
	ssl-keystore-passwords.properties
	ssl-truststore-passwords.properties 

Доп информация по некоторым параметрам может быть найдена тут:

`https://citeck.atlassian.net/wiki/x/Q4AgRg  <https://citeck.atlassian.net/wiki/x/Q4AgRg>`_

`https://docs.alfresco.com/search-services/1.3/config/properties <https://docs.alfresco.com/search-services/1.3/config/properties/>`_

Типовой вывод успешного развертывания в лог контейнера:

.. code-block::

	OpenJDK 64-Bit Server VM warning: Option UseConcMarkSweepGC was deprecated in version 9.0 and will likely be removed in a future release.
	2021-10-18 07:22:35.735 INFO  (main) [   ] o.e.j.s.Server jetty-9.3.27.v20190418, build timestamp: 2019-04-18T18:11:38Z, git hash: d3e249f86955d04bc646bb620905b7c1bc596a8d
	2021-10-18 07:22:36.283 INFO  (main) [   ] o.a.s.s.SolrDispatchFilter  ___      _       Welcome to Apache Solr™ version 6.6.5-patched.2 660ad3d2332b99205fbc436047f8d547511cd767 - tpage - 2019-11-27 08:18:56
	2021-10-18 07:22:36.284 INFO  (main) [   ] o.a.s.s.SolrDispatchFilter / __| ___| |_ _   Starting in standalone mode on port 8983
	2021-10-18 07:22:36.284 INFO  (main) [   ] o.a.s.s.SolrDispatchFilter \__ \/ _ \ | '_|  Install dir: /opt/ecos-alfresco-search-services/solr
	2021-10-18 07:22:36.298 INFO  (main) [   ] o.a.s.s.SolrDispatchFilter |___/\___/_|_|    Start time: 2021-10-18T07:22:36.286136Z
	2021-10-18 07:22:37.349 INFO  (main) [   ] o.e.j.s.Server Started @2533ms
	2021-10-18 07:22:47.283 WARN  (Thread-12) [   x:alfresco] o.a.s.c.Config XML parse warning in "solrres:/solrconfig.xml", line 1919, column 88: Include operation failed, reverting to fallback. Resource error reading file as XML (href='solrconfig_insight.xml'). Reason: Can't find resource 'solrconfig_insight.xml' in classpath or '/opt/ecos-alfresco-search-services/solrhome/alfresco'
	2021-10-18 07:22:47.916 WARN  (Thread-12) [   x:alfresco] o.a.s.c.SolrResourceLoader Solr loaded a deprecated plugin/analysis class [org.apache.solr.analysis.WordDelimiterFilterFactory]. Please consult documentation how to replace it accordingly.
	2021-10-18 07:22:47.923 WARN  (Thread-12) [   x:alfresco] o.a.s.c.SolrResourceLoader Solr loaded a deprecated plugin/analysis class [solr.SynonymFilterFactory]. Please consult documentation how to replace it accordingly.
	2021-10-18 07:22:49.231 WARN  (Thread-12) [   x:alfresco] o.a.s.h.c.AlfrescoSolrClusteringComponent No default engine for document clustering.
	2021-10-18 07:22:49.381 WARN  (Thread-12) [   x:alfresco] o.a.s.c.Config XML parse warning in "solrres:/solrconfig.xml", line 1919, column 88: Include operation failed, reverting to fallback. Resource error reading file as XML (href='solrconfig_insight.xml'). Reason: Can't find resource 'solrconfig_insight.xml' in classpath or '/opt/ecos-alfresco-search-services/solrhome/archive'
	2021-10-18 07:22:49.934 WARN  (searcherExecutor-7-thread-1-processing-x:alfresco) [   x:alfresco] o.a.s.SolrInformationServer Citeck unindex are initialized for alfresco
	2021-10-18 07:22:49.948 WARN  (Thread-12) [   x:alfresco] o.a.s.h.c.AlfrescoSolrClusteringComponent No default engine for document clustering.
	2021-10-18 07:22:49.979 WARN  (searcherExecutor-21-thread-1-processing-x:alfresco) [   x:alfresco] o.a.s.SolrInformationServer Citeck unindex are initialized for archive