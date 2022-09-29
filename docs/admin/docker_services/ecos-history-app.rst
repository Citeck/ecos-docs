ecos-history-app
=================

Назначение:
-----------

Образ микросервиса для хранения истории, статистики по задачам и фасаду аттрибутов.

Теги:
------

`nexus.citeck.ru/ecos-history <nexus.citeck.ru/ecos-history>`_ :<tag>

Базовые образы:
-----------------
* **openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
------------------------------

.. code-block::

	ecos-history:
		logging:
		options:
			max-size: "10m"
			max-file: "5"
		image: nexus.citeck.ru/ecos-history:<ECOS_HISTORY_APP_IMAGE
		container_name: ecos-history
		hostname: ecos-history
		restart: unless-stopped
		stop_grace_period: 1m
		environment:
    		- JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
    		- _JAVA_OPTIONS=-Xmx256m -Xms256m
    		- SPRING_PROFILES_ACTIVE=<ECOS-HISTORY_PROFILES
    		- EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
    		- SPRING_CLOUD_CONFIG_URI=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/config
    		- SPRING_DATASOURCE_URL=<ECOS_HISTORY_DATASOURCE
    		- SPRING_DATASOURCE_USERNAME=alfresco
    		- SPRING_DATASOURCE_PASSWORD=alfr3sc0
    		- SPRING_DATA_MONGODB_URI=<SPRING_DATA_MONGODB_URI
    		- SPRING_DATA_MONGODB_DATABASE=ecos-history
    		- ECOS-HISTORY_RECOVER_SOURCEFOLDER=/source
    		- ECOS-HISTORY_RECOVER_ERRORSFOLDER=/errors
    		- ECOS-HISTORY_ALFRESCO_TENANTID=<ALFRESCO_TENANT_ID
    		- ECOS-HISTORY_EVENT_HOST=<ECOS-HISTORY_EVENT_HOST
    		- ECOS-HISTORY_EVENT_PORT=<ECOS-HISTORY_EVENT_PORT
    		- ECOS-HISTORY_EVENT_USERNAME=<ECOS-HISTORY_EVENT_USERNAME
    		- ECOS-HISTORY_EVENT_PASSWORD=<ECOS-HISTORY_EVENT_PASSWORD
    		- JHIPSTER_SLEEP=1200 # gives time for the JHipster Registry to boot before the application
		expose:
    		- 8086/tcp
		volumes:
    		- /opt/micro/ecos-history/source:/source
    		- /opt/micro/ecos-history/errors:/errors
		networks:
    		- app_network
		depends_on:
    		- ecos
    		- ecos-postgresql
    		- rabbitmq

Используемые переменные:
-------------------------

* **JHIPSTER_REGISTRY_PASSWORD** - пароль аутентификации jhipster

* **_JAVA_OPTIONS** - параметры для **jvm**

* **SPRING_PROFILES_ACTIVE** - профили развертывания приложения

* **EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE** - **url** регистрации микросервиса в сервисе балансировки

* **SPRING_CLOUD_CONFIG_URI** - **url** параметров конфигурации

* **SPRING_DATASOURCE_URL** - **url postgresql** инстанса с бд хренения истории

* **SPRING_DATASOURCE_USERNAME** - логин пользователя для бд хренения истории

* **SPRING_DATASOURCE_PASSWORD** - пароль пользователя для бд хранения истории

* **SPRING_DATA_MONGODB_URI** - **url mongodb** инстанса для хранения history/task records атрибутов нод

* **SPRING_DATA_MONGODB_DATABASE** - бд хранения history/task records атрибутов нод

* **ECOS-HISTORY_RECOVER_SOURCEFOLDER** - **резервный** датасорс очереди событий истории 

* **ECOS-HISTORY_RECOVER_ERRORSFOLDER** - **резервный** датасорс хранения ошибок обработки очереди событий истории

* **ECOS-HISTORY_ALFRESCO_TENANTID** - **tenantid** развернутого деплоя ecos

* **ECOS-HISTORY_EVENT_HOST** - адрес диспетчера очередей

* **ECOS-HISTORY_EVENT_PORT** -  **amqp**  порт диспетчера очередей

* **ECOS-HISTORY_EVENT_USERNAME** - логин пользователя для диспетчера очередей

* **ECOS-HISTORY_EVENT_PASSWORD** - пароль пользователя для диспетчера очередей

* **JHIPSTER_SLEEP** - таймаут перед развертыванием микросервиса

Известные проблемы:
---------------------

* Расхождения в формирования url в микросервисах, использующих в качестве датасорса mongodb

* Отсутствие readness/liveness проверок датасорсов при развертывании и активном состоянии микросервиса

Дополнительно:
---------------

* Документация по `spring cloud config  <https://cloud.spring.io/spring-cloud-config/reference/html/#_spring_cloud_config_server>`_

Типовой вывод успешного развертывания в лог контейнера:
---------------------------------------------------------

.. code-block::

	ecos-history                | ----------------------------------------------------------
	ecos-history                |   Application 'history' is running! Access URLs:
	ecos-history                |   Local:          http://localhost:8086/
	ecos-history                |   External:       http://172.18.0.27:8086/
	ecos-history                |   Profile(s):     [prod, swagger, facade]
	ecos-history                | ----------------------------------------------------------
	ecos-history                | 2020-05-06 10:51:52.991  INFO 1 --- [           main] ru.citeck.ecos.history.HistoryApp        : 
	ecos-history                | ----------------------------------------------------------
	ecos-history                |   Config Server:  Connected to the JHipster Registry running in Docker
	ecos-history                | ----------------------------------------------------------




