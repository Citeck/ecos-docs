ecos-uiserv-app
================

Назначение
-----------
Образ микросервиса, предоставляющего элементы ui и хранящий их настройки (меню, журналы, UI конфиги, формы, настройки журналов, дашборды)

Базовые образы
-----------------
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose
------------------------------
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
------------------------
*	**_JAVA_OPTIONS** - параметры для jvm
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию eureka load balancer, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого cloud config server, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
*	**SPRING_DATASOURCE_URL** - url используемого postgresql datasource
*	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы
----------------------
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	cloud config и eureka load balancer используют один и тот же пароль

Типовой вывод успешного развертывания в лог контейнера
--------------------------------------------------------
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

