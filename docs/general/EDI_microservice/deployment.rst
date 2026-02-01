Подключение микросервса ecos-edi локально
==========================================

Рассматривается yaml версия для ECOS 4.2 и выше.

Для поднятия микросервиса ecos-edi локально необходимо выполнить следующие шаги:

1) Добавить описание в yaml:

.. code-block:: yaml

    #=== ECOS EDI ===#
    
    edi-app-dev:
      container_name: edi-app-dev
      image: enterprise-registry.citeck.ru/ecos-edi:1.0.0-snapshot
      ports:
        - 8083:8083
      environment:
        - _JAVA_OPTIONS=-Xmx512m -Xms512m
        - SPRING_PROFILES_ACTIVE=dev,swagger
        - SPRING_RABBITMQ_HOST=rabbitmq-dev
        - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@ecos-registry:8761/eureka
        - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@ecos-registry:8761/config
        - SPRING_DATASOURCE_URL=jdbc:postgresql://ecos-microservices-psql-dev:5432/ecos_edi
        - SPRING_DATASOURCE_USERNAME=edi
        - SPRING_DATASOURCE_PASSWORD=edipassword
        - ECOS_INIT_DELAY=20
      depends_on:
        - ecos-registry
        - rabbitmq-dev


Также перед запуском в БД микросервиса **ecos-microservices-psql-dev** необходимо создать базу данных **ecos_edi**.

Пока же в запущенном контейнере **ecos-microservices-psql-dev** необходимо выполнить следующие команды:

.. code-block:: 

    CREATE USER edi WITH ENCRYPTED PASSWORD 'edipassword';
    CREATE DATABASE ecos_edi;
    GRANT ALL PRIVILEGES ON DATABASE ecos_edi TO edi;

При локальном поднятии также убедиться что в **apllication.yml** прописаны параметры подключения к БД edi соответствущие созданной БД.

Создание базы добавлено в скрипт инициализции БД для nexus.citeck.ru/postgresql:12.7-1