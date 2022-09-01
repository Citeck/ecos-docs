ecos-registry-app
===================

Назначение:
------------
Образ одного из центральных компонентов микросервисной архитектуры. Приложение объединяет eureka REST сервис (load balancing, registering, service discovery) и Spring Cloud Config server для централизации конфигурации.

Теги:
------
jhipster/jhipster-registry:v4.1.1 - официальный образ

`nexus_ecos_registry <http://nexus.citeck.ru/ecos-registry:>`_  - собственная сборка

Базовые образы:
----------------
**openjdk:8-jre-alpine** - официальный образ openjdk 8 jre на базе alpine linux

Шаблон сервиса docker-compose:
------------------------------
::

	jhipster-registry:
	    logging:
	      options:
	        max-size: "10m"
	        max-file: "5"
	    image: jhipster/jhipster-registry:<JHIPSTER_APP_IMAGE
	    container_name: jhipster-registry
	    hostname: jhipster-registry
	    restart: unless-stopped
	    stop_grace_period: 1m
	    volumes:
	      - /opt/micro/central-server-config:/central-config
	    environment:
	      - _JAVA_OPTIONS=-Xmx512m -Xms256m -Dcom.sun.management.jmxremote=true -Dcom.sun.management.jmxremote.port=10004 -Dcom.sun.management.jmxremote.authenticate=true -Dcom.sun.management.jmxremote.access.file=/central-config/jmxremote.access -Dcom.sun.management.jmxremote.password.file=/central-config/jmxremote.password -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.rmi.port=10004  -Djava.rmi.server.hostname=<HOST_IP
	      - SPRING_PROFILES_ACTIVE=dev,swagger
	      - SPRING_SECURITY_USER_PASSWORD=alfr3sc0
	      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
	      - SPRING_CLOUD_CONFIG_SERVER_COMPOSITE_0_TYPE=native
	      - SPRING_CLOUD_CONFIG_SERVER_COMPOSITE_0_SEARCH_LOCATIONS=file:/central-config/docker-config/
	    expose:
	      - 8761/tcp
	      - 10004/tcp
	    networks:
	      - app_network

Используемые переменные:
-------------------------
*	**_JAVA_OPTIONS** - параметры для jvm
*	**SPRING_PROFILES_ACTIVE** - используемые при развертывании профили
*	**SPRING_SECURITY_USER_PASSWORD** - пароль пользователя для аутентификации в cloud config
*	**JHIPSTER_REGISTRY_PASSWORD** - пароль пользователя для аутентификации в eureka load balancer
*	Документация по `spring cloud config <https://cloud.spring.io/spring-cloud-config/reference/html/#_spring_cloud_config_server>`_

Известные проблемы:
--------------------
*	Требуется закончить переход на ecos-registry проект
*	Утилизации цпу
*	Требуется конфигурация registry как экспортера метрик микросервисов в Prometheus
*	Использование localPath расположения конфигурационного файла
*	Не реализован доступ к ui registry через location
*	Не используется JWT token

Типовой вывод успешного развертывания в лог контейнера:
----------------------------------------------------------
::

	jhipster-registry                    | ----------------------------------------------------------
	jhipster-registry                    |  Application 'jhipster-registry' is running! Access URLs:
	jhipster-registry                    |  Local:          http://localhost:8761
	jhipster-registry                    |  External:       http://172.18.0.11:8761
	jhipster-registry                    |  Profile(s):     [composite, dev, swagger]
	jhipster-registry                    | ----------------------------------------------------------
	jhipster-registry                    | 2020-04-28 20:35:36.017  INFO 1 --- [           main] i.g.j.registry.JHipsterRegistryApp       : 
	jhipster-registry                    | ----------------------------------------------------------
	jhipster-registry                    |  Config Server:  Connected to the JHipster Registry running in Docker
	jhipster-registry                    | ----------------------------------------------------------

