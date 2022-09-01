ecos-apps-app
=============

Назначение:
------------

Образ микросервиса, управляющего деплоем приложений и модулей ECOS

Теги:
------

`nexus.citeck.ru/ecos-apps <nexus.citeck.ru/ecos-apps>`_ :<tag> - сборка проекта ecos-apps

Базовые образы:
-----------------

* **openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
---------------------------------

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
-------------------------

* **_JAVA_OPTIONS** - параметры для **jvm**

* **SPRING_PROFILES_ACTIVE** - используемые при развертывании профили

* **EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - url используемого по умолчанию **eureka load balancer**, содержит credentials

* **SPRING_CLOUD_CONFIG_URI** - url используемого **cloud config server**, содержит credentials

* **JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в **eureka load balancer**

* **SPRING_DATASOURCE_URL** - url используемого **postgresql datasource**

* **JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы:
--------------------

* Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса

* Использование empty password в доступах к датасорсам

* cloud config и eureka load balancer используют один и тот же пароль

Дополнительно:
---------------

Документация по использованию микросервиса Apps microservice 

Типовой вывод успешного развертывания в лог контейнера:
--------------------------------------------------------

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


