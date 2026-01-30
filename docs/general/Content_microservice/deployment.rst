Развертывание микросервиса и первичная настройка
===================================================

Для того чтобы развернуть микросервис **ecos-content** в docker необходимо в свой файл **docker-compose.yml** добавить следующую конфигурацию:

.. code-block:: yaml

    #=== ECOS CONTENT ===#
    
    content-app-dev:
      container_name: content-app-dev
      image: enterprise-registry.citeck.ru/ecos-content:1.0.0
      ports:
        - 8088:8088
      environment:
        - _JAVA_OPTIONS=-Xmx256m -Xms256m
        - SPRING_PROFILES_ACTIVE=dev,swagger
        - SPRING_RABBITMQ_HOST=rabbitmq-dev
        - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@ecos-registry:8761/eureka
        - SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@ecos-registry:8761/config
        - ECOS_INIT_DELAY=30
      depends_on:
        - ecos-registry
        - rabbitmq-dev

После поднятия микросервиса в рабочем пространстве **Раздел администратора** должен создаться пункт **Контент** с журналом **Хранилища контента**:

 .. image:: _static/content_1.png
       :width: 700
       :align: center

Настройка конфигурации Citeck после поднятия системы с микросервисом
----------------------------------------------------------------------

Параметр **default-content-storage**

В системе необходимо установить параметр, устанавливающий хранилище данных по умолчанию. Это хранилище будет подхватываться по умолчанию, если у типа данных в Citeck будет указано, что его content должен быть сохранен в хранилище данных, но не выбрано конкретное хранилище (например: на каждом стенде может быть использовано свое хранилище, поэтому в конфигурации типа не будет установлено конкретное значение).

 .. image:: _static/content_2.png
       :width: 600
       :align: center
