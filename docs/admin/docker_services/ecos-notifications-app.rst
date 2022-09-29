ecos-notifications-app
=======================

Назначение:
-----------
Образ микросервиса рассылки нотификаций

Базовые образы:
----------------
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
-------------------------------
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
--------------------------
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
--------------------
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	Cloud config и eureka load balancer используют один и тот же пароль
*	Монтирование firebase credentials как волюма
*	Часть app properties (ECOS-NOTIFICATIONS*) нужно вынести в spring cloud config

Типовой вывод успешного развертывания в лог контейнера:
--------------------------------------------------------
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

