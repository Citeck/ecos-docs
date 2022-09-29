ecos-process-app
=================

Назначение
-----------
Образ микросервиса для управления CMMN процессами 

Базовые образы
----------------------
*	**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose
---------------------------------
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
---------------------------------
*	**_JAVA_OPTIONS** - параметры для jvm
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию eureka load balancer, содержит credentials
*	**SPRING_CLOUD_CONFIG_URI** - url используемого cloud config server, содержит credentials
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
*	**SPRING_DATA_MONGODB_URI** - url используемого mongodb datasource
*	**JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы
----------------------
*	Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса
*	Использование empty password в доступах к датасорсам
*	Cloud config и eureka load balancer используют один и тот же пароль

Типовой вывод успешного развертывания в лог контейнера
-------------------------------------------------------
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

