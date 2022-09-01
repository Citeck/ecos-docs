ecos-gateway-app
================

Назначение:
------------

Образ одного из центральных компонентов микросервисной архитектуры. Приложение реализует API шлюз взаимодействия с остальными микросервисами

Теги:
--------

`Nexus_gateway <http://nexus.citeck.ru/ecos-gateway:>`_ <tag> - сборка проекта ecos-gateway 

Базовые образы:
----------------

**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
-------------------------------
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
--------------------------

*	**_JAVA_OPTIONS** - параметры для **jvm**
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**
*	**SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**
*	**JHIPSTER_SLEEP **- **таймаут** перед развертыванием микросервиса

Известные проблемы:
--------------------
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	cloud config и eureka load balancer используют один и тот же пароль

Типовой вывод успешного развертывания в лог контейнера:
--------------------------------------------------------
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

