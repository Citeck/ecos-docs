.. _edi_deployment:

Подключение микросервиса ecos-edi локально
===========================================

Ниже приведён пример подключения ecos-edi к локальному Docker Compose окружению. Выберите образ микросервиса, совместимый с используемой поставкой ECOS, и задайте его полный адрес с тегом в переменной ``ECOS_EDI_IMAGE`` (например, в файле ``.env`` рядом с Compose-файлом).

Параметры БД в примере соответствуют конфигурации ecos-edi 1.14.0. Имена сервисов, профили и параметры registry/config-сервера необходимо согласовать с вашим окружением.

Для поднятия микросервиса ecos-edi локально необходимо выполнить следующие шаги:

1) Добавить описание в yaml:

.. code-block:: yaml

    #=== ECOS EDI ===#
    
    edi-app-dev:
      container_name: edi-app-dev
      image: ${ECOS_EDI_IMAGE:?Set ECOS_EDI_IMAGE}
      ports:
        - 8083:8083
      environment:
        - _JAVA_OPTIONS=-Xmx512m -Xms512m
        - SPRING_PROFILES_ACTIVE=dev,swagger
        - SPRING_RABBITMQ_HOST=rabbitmq-dev
        - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@ecos-registry:8761/eureka
        - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@ecos-registry:8761/config
        - ECOS_WEBAPP_DATASOURCES_MAIN_URL=jdbc:postgresql://ecos-microservices-psql-dev:5432/ecos_edi
        - ECOS_WEBAPP_DATASOURCES_MAIN_USERNAME=edi
        - ECOS_WEBAPP_DATASOURCES_MAIN_PASSWORD=edipassword
        - ECOS_INIT_DELAY=20
      depends_on:
        - ecos-registry
        - rabbitmq-dev


Также перед запуском в БД микросервиса **ecos-microservices-psql-dev** необходимо создать базу данных **ecos_edi**.

В запущенном контейнере **ecos-microservices-psql-dev** необходимо выполнить следующие команды:

.. code-block:: sql

    CREATE USER edi WITH ENCRYPTED PASSWORD 'edipassword';
    CREATE DATABASE ecos_edi;
    GRANT ALL PRIVILEGES ON DATABASE ecos_edi TO edi;

Параметры подключения должны соответствовать созданной БД. В конфигурации приложения используются свойства ``ecos.webapp.dataSources.main.url``, ``ecos.webapp.dataSources.main.username`` и ``ecos.webapp.dataSources.main.password``. В примере они переопределены через переменные окружения. Источник ``main-xa-aware`` в поставляемом ``application.yml`` ссылается на эти же свойства.

Если ваше окружение создаёт БД и пользователя автоматически, повторно выполнять SQL-команды не требуется.

Для сборки ecos-edi 1.14.0 из исходников требуется JDK 25. При запуске готового Docker-образа Java используется внутри контейнера.
