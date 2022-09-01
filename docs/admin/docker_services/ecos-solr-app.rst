ecos-solr-app
===============

Назначение
-------------
Образ с установленным контейнером сервлетов Tomcat с вебархивом проекта ecos-alfresco-solr4

Базовые образы
----------------
*	tomcat:7.0.59-jre8 - официальный образ tomcat 7.0.59, openjdk version "1.8.0_40-internal"

Шаблон сервиса docker-compose
---------------------------------------
::
 
 ess:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    image: nexus.citeck.ru/ess:<ECOS_SOLR4
    restart: unless-stopped
    stop_grace_period: 1m
    container_name: ess
    hostname: ess
    ports:
      - 8080:8080/tcp
      - 8443:8443/tcp
    env_file:
      - ./env_dir/ess.env
    volumes:
      - /opt/ess:/opt/solr4_data
    networks:
      - app_network

Используемые переменные
--------------------------
*	ALFRESCO_HOST - fqdn/ip инстанса ecos
*	ALFRESCO_PORT - http порт инстанса ecos 
*	ALFRESCO_PORT_SSL - https порт инстанса ecos 
*	ALFRESCO_SECURE_COMMS - использовать шифрованное соединение
*	CITECK_MERGE_FACTOR - мерж фактор solr/lucene, используемый при определении необходимости мержить сегменты.
*	ALFRESCO_INDEX_TRANSFORM_CONTENT - если true - будет происходить конвертация контента в текст и его последующая пословесная индексация. Если false - будут индексироваться только метаданные (mimetype, size, etc).
*	ALFRESCO_RECORD_UNINDEXED_NODES - если true - ноды, типы которых отмечены как “неиндексируемые” - будут попадать в индекс в качестве документа без индексации атрибутов ноды. Если false - такие документы будут игнорироваться при индексации.
*	CITECK_RECORD_TRANSACTIONS - если true - каждая транзакция будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях будут храниться только в кеше, в памяти.
*	CITECK_TX_CONSISTENCY_CHECK_MODE - тип проверки консистентности индекса и базы для индексации транзакций. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.
*	CITECK_TX_IS_INDEXED_CACHE_SIZE - размер кеша, если CITECK_RECORD_TRANSACTIONS = false.
*	CITECK_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT - коэффициент чистки кеша при переполнении, если CITECK_RECORD_TRANSACTIONS = false.
*	CITECK_RECORD_ACL_TRANSACTIONS - если true - каждая транзакция прав будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях прав будут храниться только в кеше, в памяти.
*	CITECK_ACL_CONSISTENCY_CHECK_MODE - тип проверки консистентности индекса и базы для индексации транзакций прав. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.
*	CITECK_ACL_TX_IS_INDEXED_CACHE_SIZE - размер кеша, если CITECK_RECORD_ACL_TRANSACTIONS = false.
*	CITECK_ACL_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT - коэффициент чистки кеша при переполнении, если CITECK_RECORD_ACL_TRANSACTIONS = false.
*	JAVA_OPTS - параметры для jvm

Типовой вывод успешного развертывания в лог контейнера
-----------------------------------------------------------------
::

	ess                         | Attention!!! All spaces in Environment variables will be deleted!!!
	ess                         | Solr configuration changed!
	ess                         | replacing option  alfresco.index.transformContent=false  in  /opt/solr4/archive-SpacesStore/conf/solrcore.properties
	ess                         | replacing option  alfresco.index.transformContent=false  in  /opt/solr4/workspace-SpacesStore/conf/solrcore.properties
	ess                         | replacing option  alfresco.recordUnindexedNodes=false  in  /opt/solr4/archive-SpacesStore/conf/solrcore.properties
	ess                         | replacing option  alfresco.recordUnindexedNodes=false  in  /opt/solr4/workspace-SpacesStore/conf/solrcore.properties
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Server version:        Apache Tomcat/7.0.59
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Server built:          Jan 28 2015 15:51:10 UTC
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Server number:         7.0.59.0
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: OS Name:               Linux
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: OS Version:            3.10.0-957.21.2.el7.x86_64
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Architecture:          amd64
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Java Home:             /usr/lib/jvm/java-8-openjdk-amd64/jre
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: JVM Version:           1.8.0_40-internal-b27
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: JVM Vendor:            Oracle Corporation
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: CATALINA_BASE:         /usr/local/tomcat
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: CATALINA_HOME:         /usr/local/tomcat
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Djava.util.logging.config.file=/usr/local/tomcat/conf/logging.properties
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Djava.util.logging.manager=org.apache.juli.ClassLoaderLogManager
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Xms1G
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Xmx2G
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Djava.endorsed.dirs=/usr/local/tomcat/endorsed
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Dcatalina.base=/usr/local/tomcat
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Dcatalina.home=/usr/local/tomcat
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.startup.VersionLoggerListener log
	ess                         | INFO: Command line argument: -Djava.io.tmpdir=/usr/local/tomcat/temp
	ess                         | May 14, 2020 9:28:30 AM org.apache.catalina.core.AprLifecycleListener lifecycleEvent
	ess                         | INFO: The APR based Apache Tomcat Native library which allows optimal performance in production environments was not found on the java.library.path: /usr/java/packages/lib/amd64:/usr/lib/x86_64-linux-gnu/jni:/lib/x86_64-linux-gnu:/usr/lib/x86_64-linux-gnu:/usr/lib/jni:/lib:/usr/lib
	ess                         | May 14, 2020 9:28:30 AM org.apache.coyote.AbstractProtocol init
	ess                         | INFO: Initializing ProtocolHandler ["http-bio-8080"]
	ess                         | May 14, 2020 9:28:30 AM org.apache.coyote.AbstractProtocol init
	ess                         | INFO: Initializing ProtocolHandler ["ajp-bio-8009"]
	ess                         | May 14, 2020 9:28:31 AM org.apache.coyote.AbstractProtocol init
	ess                         | INFO: Initializing ProtocolHandler ["http-bio-8443"]
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.startup.Catalina load
	ess                         | INFO: Initialization processed in 1875 ms
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.core.StandardService startInternal
	ess                         | INFO: Starting service Catalina
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.core.StandardEngine startInternal
	ess                         | INFO: Starting Servlet Engine: Apache Tomcat/7.0.59
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.startup.HostConfig deployDescriptor
	ess                         | INFO: Deploying configuration descriptor /usr/local/tomcat/conf/Catalina/localhost/solr4.xml
	ess                         | May 14, 2020 9:28:31 AM org.apache.catalina.startup.SetContextPropertiesRule begin
	ess                         | WARNING: [SetContextPropertiesRule]{Context} Setting property 'debug' to '0' did not find a matching property.
	ess                         | May 14, 2020 9:28:41 AM org.apache.catalina.core.ApplicationContext log
	ess                         | INFO: No Spring WebApplicationInitializer types detected on classpath
	ess                         | 2020-05-14 09:28:47,899  INFO  [solr.component.AsyncBuildSuggestComponent] [coreLoadExecutor-5-thread-2] Initializing SuggestComponent
	ess                         | 2020-05-14 09:28:49,601  INFO  [solr.component.AsyncBuildSuggestComponent] [coreLoadExecutor-5-thread-1] Initializing SuggestComponent
	ess                         | May 14, 2020 9:28:49 AM org.apache.catalina.startup.HostConfig deployDescriptor
	ess                         | INFO: Deployment of configuration descriptor /usr/local/tomcat/conf/Catalina/localhost/solr4.xml has finished in 18,143 ms
	ess                         | May 14, 2020 9:28:49 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/examples
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/examples has finished in 408 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/manager
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/manager has finished in 64 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/host-manager
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/host-manager has finished in 47 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/ROOT
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/ROOT has finished in 56 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deploying web application directory /usr/local/tomcat/webapps/docs
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.HostConfig deployDirectory
	ess                         | INFO: Deployment of web application directory /usr/local/tomcat/webapps/docs has finished in 35 ms
	ess                         | May 14, 2020 9:28:50 AM org.apache.coyote.AbstractProtocol start
	ess                         | INFO: Starting ProtocolHandler ["http-bio-8080"]
	ess                         | May 14, 2020 9:28:50 AM org.apache.coyote.AbstractProtocol start
	ess                         | INFO: Starting ProtocolHandler ["ajp-bio-8009"]
	ess                         | May 14, 2020 9:28:50 AM org.apache.coyote.AbstractProtocol start
	ess                         | INFO: Starting ProtocolHandler ["http-bio-8443"]
	ess                         | May 14, 2020 9:28:50 AM org.apache.catalina.startup.Catalina start
	ess                         | INFO: Server startup in 18992 ms

