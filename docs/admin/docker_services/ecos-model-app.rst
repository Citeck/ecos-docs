ecos-model-app
===============

Назначение:
------------
Образ микросервиса, предназначенного для хранения и работы с такими сущностями как: тип(type), раздел(section), ассоциация(association), действие(action)

Базовые образы:
------------------
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
-------------------------------
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
--------------------------
*	**_JAVA_OPTIONS** - параметры для **jvm**
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**
*	**SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**
*	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы:
----------------------
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	cloud config и eureka load balancer используют один и тот же пароль

Типовой вывод успешного развертывания в лог контейнера:
--------------------------------------------------------
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

