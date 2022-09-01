ecos-integrations-app
======================
Назначение
-----------
Микросервис, предоставляющий эндпойнт ecos-records, через который можно посылать запросы в определенный список внешних систем.

Базовые образы
---------------
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose
---------------------------------
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
-------------------------

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
*	Cloud config и eureka load balancer используют один и тот же пароль


Типовой вывод успешного развертывания в лог контейнера
-------------------------------------------------------
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

