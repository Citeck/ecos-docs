ecos-app
=========

Назначение
----------------
Образ, включающий контейнер сервлетов Tomcat с предварительно сформированным комплектом вебархивов, конфигурационных файлов для webapp и предустановленными инструментами.

Теги
--------

<docker-registry>/ecos-<ecos project>:tag*

**Веб архивы**

*	alfresco.war
*	share.war
*	flowable-admin.war
*	flowable-idm.war
*	flowable-modeler.war
*	flowable-rest.war
*	flowable-task.war
*	solr.war

Тег:
*<docker-registry>/ecs-<ecos project>:tag*

**Веб архивы:**

*	alfresco.war
*	share.war
*	flowable-admin.war
*	flowable-idm.war
*	flowable-modeler.war
*	flowable-rest.war
*	flowable-task.war

Базовые образы
----------------
* **centos:centos7** - базовый образ последнего обновления CentOS 7.
* **nexus.citeck.ru/ecs:base** - базовый образ на основе centos:centos7. В образ вынесены слои с типовыми инструкциями для переиспользования в итоговых образах.

Шаблон сервиса docker-compose
--------------------------------

::

  ecos:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    container_name: ecos
    restart: unless-stopped
    ports:
      - 9090:9090/tcp
      - 50086:50086/tcp
    expose:
      - 8080/tcp
      - 8443/tcp
    environment:
      - USE_EXTERNAL_AUTH=<EXTERNAL_AUTH
      - DB_HOST=ecos-postgresql
      - ALFRESCO_HOSTNAME=<DOMAIN_NAME
      - ALFRESCO_PROTOCOL=https
      - SHARE_HOSTNAME=<DOMAIN_NAME
      - SHARE_PROTOCOL=https
      - SHARE_PORT=443
      - ALFRESCO_PORT=443
      - FLOWABLE_URL=https://<DOMAIN_NAME
      - MAIL_HOST=<M_HOST
      - MAIL_PORT=<M_PORT
      - DB_NAME=alfresco
      - FLOWABLE_DBNAME=alf_flowable
      - ECOS_EUREKA_INSTANCE_HOST=ecos
      - ECOS_EUREKA_INSTANCE_IP=ecos
      - ECOS_EUREKA_INSTANCE_PORT=8080
      - JHIPSTER_REGISTRY_PASSWORD=alfr3sc0
      - EUREKA_CLIENT_SERVICE_URL_DEFAULTZONE=http://admin:$${jhipster.registry.password}@jhipster-registry:8761/eureka
      - JAVA_OPTS=<BOOTSTRAP_LOCALE -Djava.security.egd=file:///dev/urandom <ECOS_XM <XDEBUG -Dcom.sun.management.jmxremote.authenticate=true -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.port=9090 -Dcom.sun.management.jmxremote.rmi.port=9090 -Djava.rmi.server.hostname=<HOST_IP -Dcom.sun.management.jmxremote.password.file=/tmp/alfresco/jmxremote.password -Dcom.sun.management.jmxremote.access.file=/tmp/alfresco/jmxremote.access
    volumes:
      - /opt/ecos/license:/opt/tomcat/shared/classes/alfresco/ecos
      - /opt/ecos/conf:/tmp/alfresco
      - /opt/ecos/content:/content
      - /opt/ecos/shared:/shared
      - /opt/ecos/extract_load:/extract_load
      - /opt/ecos/history_data/:/opt/history/data/
    networks:
      - app_network
    hostname: <HOSTNAME
    image: <ECOS_IMAGE
    stop_grace_period: 1m
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/alfresco"]
      interval: 1m
      timeout: 10s
      retries: 15
    depends_on:
      - ecos-postgresql
      - rabbitmq

Используемые переменные:
------------------------
*	TWEAK_FLOWABLE - устаревший параметр, на данный момент по дефолту в true, требуется исключить из образа
*	FLOWABLE_REST_API_USERNAME - логин интеграции с flowable
*	FLOWABLE_REST_API_PASSWORD - пароль интеграции с flowable
*	ALFRESCO_HOSTNAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	ALFRESCO_PROTOCOL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco  -global.properties
*	SHARE_HOSTNAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	SHARE_PROTOCOL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	ALFRESCO_PORT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	SHARE_PORT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	DB_KIND - тип используемой бд (postgresql, mysql). Entrypoint формирует, в зависимости от выбранного параметра следующие переменные: DB_CONN_PARAMS, DB_DRIVER, DB_PORT.
*	DB_USERNAME - логин для подключеня к датасорсу
*	DB_PASSWORD - пароль для подключения к датасорсу
*	DB_NAME - имя базы данных
*	DB_HOST - fqdn or ip узла, где развернут инстанс бд
*	DB_DRIVER - используемый драйвер подключения к датасорсу, фомируется параметром DB_KIND
*	DB_PORT - порт усзла, где развернут инстанс бд, по умолчанию используются дефолтные порты postgresql, mysql
*	SYSTEM_SERVERMODE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_HOST - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_PORT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_USERNAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_PASSWORD - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_FROM_DEFAULT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_PROTOCOL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_SMTP_AUTH - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_SMTP_STARTTLS_ENABLE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_SMTPS_AUTH - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	MAIL_SMTPS_STARTTLS_ENABLE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	FTP_PORT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	CIFS_ENABLED - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	CIFS_SERVER_NAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	CIFS_DOMAIN - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	NFS_ENABLED - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	CONTENT_STORE - расположение директорий contenstore/contentstore.deleted по абсолютному пути внутри контейнера
*	TOMCAT_CSRF_PATCH - расположение патча по отключению Tomcat CSRF token filter
*	TOMCAT_CSRF_ENABLED - использование Tomcat CSRF token filter (default true)
*	SOLR_WORKSPACE_PROPERTIES - (ecos image only) директория хранения настроек коллекции workspace solr4
*	SOLR_ARCHIVE_PROPERTIES -(ecos image only) директория хранения настроек коллекции archive solr4
*	SOLR_STORE - (ecos image only) расположение директории хранения индексов solr по абсолютному пути внутри контейнера
*	FLOWABLE_DB_KIND - тип используемой бд (postgresql, mysql). Entrypoint формирует, в зависимости от выбранного параметра следующие переменные: DB_CONN_PARAMS, DB_DRIVER, DB_PORT.
*	FLOWABLE_URL - fqdn or ip обращения к флобл ui
*	FLOWABLE_DB_NAME - имя базы данных
*	FLOWABLE_DB_USERNAME - логин для подключеня к датасорсу
*	FLOWABLE_DB_PASSWORD - пароль для подключения к датасорсу
*	FLOWABLE_DB_HOST - fqdn or ip узла, где развернут инстанс бд
*	FLOWABLE_DB_PORT - порт усзла, где развернут инстанс бд, по умолчанию используются дефолтные порты postgresql, mysql
*	FLOWABLE_DB_CONN_PARAMS - дополнительные параметры подключения к датасорсу
*	LDAP_ENABLED - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_KIND - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_AUTH_USERNAMEFORMAT - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_URL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_DEFAULT_ADMINS - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_SECURITY_PRINCIPAL - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_SECURITY_CREDENTIALS - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_GROUP_SEARCHBASE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_USER_SEARCHBASE - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_USER_ATTRIBUTENAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	LDAP_GROUP_MEMBER_ATTRIBUTENAME - типовой параметр конфигурации alfresco, при объявлении переопределяет соответствующий параметр в alfresco-global.properties
*	USE_EXTERNAL_AUTH - конфгурирование share-config-custom.xml для использования внешней аутентификации по заголовку.

Известные проблемы
------------------------
*	Часть событий лога приложений контейнера сервлетов остается внутри котейнера, что приводит к неконтролируему разрастанию overlay слоев контейнера и утилизации дискового ресурса хоста.
*	Часть параметров (отображены в документации типовой параметр конфигурации..) включены во входящиие параметры для entrypoint, часть параметров передается через alfresco-additional.properties, часть параметров находится на readonly слоях образа. Требуется выработка решения по использованию единого подхода к объявлению параметров.
*	Большое количество веб-приложений в составе одного образа, отсутствие возможности формализации используемых ресурсов в рамках веб приложения.
*	Невалидный ImageMagic (ecos image only)
*	Отсутствие контроля за процессами инструментов конвертации в образе (процесс конвертера не первичный, его состояние не влияет на ЖЦ контейнера, но влияет на доступность функционала в развернутом приложении)
*	Большой размер итогового образа (стандартная сборка без использования экспериментальных фич, типа сквоша слоев)
*	Отсутствие мониторинга в разрезе веб-приложения под Prometheus (есть jmx мониторинг через java-gateway zabbix)

Типовой вывод принятых настроек в лог контейнера
------------------------------------------------
::

	Attention!!! All spaces in Environment variables will be deleted!!!
	ecos                        | replacing option  flowable.rest-api.username=admin  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  flowable.rest-api.password=alfr3sc0  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  alfresco.host=ecos-demo.citeck.com  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  alfresco.protocol=https  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  alfresco.port=443  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  share.host=ecos-demo.citeck.com  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  share.protocol=https  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  share.port=443  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  system.serverMode=PRODUCTION  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  db.driver=org.postgresql.Driver  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  db.username=alfresco  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  db.password=alfr3sc0  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  db.name=alfresco  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  db.url=jdbc:postgresql://ecos-postgresql:5432/alfresco  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.host=mailhog  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.port=1025  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.username=  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.password=  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.from.default=alfresco@alfresco.org  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.protocol=smtp  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.smtp.auth=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.smtp.starttls.enable=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.smtps.auth=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  mail.smtps.starttls.enable=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  ftp.port=21  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  cifs.enabled=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  cifs.Server.Name=localhost  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  cifs.domain=WORKGROUP  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  cifs.hostannounce=true  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  cifs.broadcast=0.0.0.255  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  cifs.ipv6.enabled=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  nfs.enabled=false  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  dir.contentstore=/content/contentstore  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  dir.contentstore.deleted=/content/contentstore.deleted  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  flowable.modeler.url=https://ecos-demo.citeck.com/flowable-modeler/  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  flowable.rest-api.url=https://ecos-demo.citeck.com/flowable-rest/  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  flowable.webapps.deployment.api.url=https://ecos-demo.citeck.com/flowable-task/app-api  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | Flowable api url change skipped
	ecos                        | adding option  idm.app.url=https://ecos-demo.citeck.com/flowable-idm/  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  flowable.db.url=jdbc:postgresql://ecos-postgresql:5432/alf_flowable  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  flowable.db.username=alfresco  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  flowable.db.password=alfr3sc0  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | adding option  flowable.db.driver.class.name=org.postgresql.Driver  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | replacing option  data.dir.root=/var/lib/solr4/index  in  /opt/alfresco/solr4/workspace-SpacesStore/conf/solrcore.properties
	ecos                        | replacing option  solr.suggester.enabled=false  in  /opt/alfresco/solr4/workspace-SpacesStore/conf/solrcore.properties
	ecos                        | replacing option  data.dir.root=/var/lib/solr4/index  in  /opt/alfresco/solr4/archive-SpacesStore/conf/solrcore.properties
	ecos                        | adding option  authentication.chain=alfrescoNtlm1:alfrescoNtlm  in  /opt/tomcat/shared/classes/alfresco-global.properties
	ecos                        | Flowable connection string: postgresql://ecos-postgresql:5432/alf_flowable
	ecos                        | Solr configuration changed!

