ecos-alfresco-search-service
=============================

Назначение:
------------

Образ с установленным контейнером сервлетов Tomcat с вебархивом проекта ecos-alfresco-search-service (solr6)

Теги:
------

`nexus.citeck.ru/ecos-alfresco-search-service <nexus.citeck.ru/ecos-alfresco-search-service>`_ :<tag>

Базовые образы
----------------------

* **alfresco/alfresco-base-java:11.0.1-openjdk-centos-7-3e4e9f4e5d6a** базовый образ tomcat/java от alfresco,  openjdk version "11.0.1-openjdk"

Шаблон сервиса docker-compose
------------------------------

.. code-block::

	ecos-alfresco-search-services:
		logging:
		 options:
			max-size: "10m"
			max-file: "5"
		image: nexus.citeck.ru/ecos-alfresco-search-services:<ECOS_SOLR6
		restart: unless-stopped
		stop_grace_period: 1m
		container_name: ecos-alfresco-search-services
		hostname: ecos-alfresco-search-services
		ports:
    		- 8983:8983
		env_file:
  		- ./env_dir/ecos-search-service-app.env
		volumes:
    		- /opt/ecos-alfresco-search-services/contentstore:/opt/ecos-alfresco-search-services/contentstore
    		- /opt/ecos-alfresco-search-services/data:/opt/ecos-alfresco-search-services/data
		networks:
    		- app_network

Используемые переменные:
-------------------------

* **ALFRESCO_HOST** - fqdn/ip инстанса ecos

* **ALFRESCO_PORT** - http порт инстанса ecos 

* **ALFRESCO_PORT_SSL** - https порт инстанса ecos 

* **SOLR_SOLR_HOST** - fqdn/ip инстанса solr

* **SOLR_SOLR_PORT** - http порт инстанса solr

* **SOLR_CITECK_MERGE_FACTOR** - мерж фактор solr/lucene, используемый при определении необходимости мержить сегменты.

* **SOLR_ALFRESCO_INDEX_TRANSFORM_CONTENT** - если true - будет происходить конвертация контента в текст и его последующая пословесная индексация. Если false - будут индексироваться только метаданные  (mimetype, size, etc).

* **SOLR_ALFRESCO_RECORD_UNINDEXED_NODES** - если true - ноды, типы которых отмечены как “неиндексируемые” - будут попадать в индекс в качестве документа без индексации атрибутов ноды. Если false - такие документы будут игнорироваться при индексации.

* **SOLR_CITECK_RECORD_TRANSACTIONS** - если true - каждая транзакция будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях будут храниться только в кеше, в памяти.

* **SOLR_CITECK_TX_CONSISTENCY_CHECK_MODE** - тип проверки консистентности индекса и базы для индексации транзакций. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.

* **SOLR_CITECK_TX_IS_INDEXED_CACHE_SIZE** - размер кеша, если CITECK_RECORD_TRANSACTIONS = false.

* **SOLR_CITECK_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT** - коэффициент чистки кеша при переполнении, если CITECK_RECORD_TRANSACTIONS = false.

* **SOLR_CITECK_RECORD_ACL_TRANSACTIONS** - если true - каждая транзакция прав будет попадать в индекс, как отметка о том, что она проиндексирована. Если false - данные о проиндексированных транзакциях прав будут храниться только в кеше, в памяти.

* **SOLR_CITECK_ACL_CONSISTENCY_CHECK_MODE** - тип проверки консистентности индекса и базы для индексации транзакций прав. Может принимать значения FULL_DB_AND_INDEX_CHECK, ONLY_LAST_TRANSACTION или NONE.

* **SOLR_CITECK_ACL_TX_IS_INDEXED_CACHE_SIZE** - размер кеша, если CITECK_RECORD_ACL_TRANSACTIONS = false.

* **SOLR_CITECK_ACL_TX_IS_INDEXED_CACHE_CLEAR_COEFFICIENT** - коэффициент чистки кеша при переполнении, если CITECK_RECORD_ACL_TRANSACTIONS = false.

* **SOLR_OPTS** - параметры для **jvm**

**Настройки SSL:**

По умолчанию SSL включён в микросервисе, при старте необходимо указать следующие environments

.. code-block::

	SOLR_SSL_KEY_STORE: /opt/ecos-alfresco-search-services/keystores/ssl.repo.client.keystore
	SOLR_SSL_KEY_STORE_PASSWORD: kT9X6oe68t
	SOLR_SSL_KEY_STORE_TYPE: JCEKS
	SOLR_SSL_TRUST_STORE: /opt/ecos-alfresco-search-services/keystores/ssl.repo.client.truststore
	SOLR_SSL_TRUST_STORE_PASSWORD: kT9X6oe68t
	SOLR_SSL_TRUST_STORE_TYPE: JCEKS
	SOLR_SSL_NEED_CLIENT_AUTH: true
	SOLR_SSL_WANT_CLIENT_AUTH: false

Для отключения SSL проверяем что у нас не устанавливаться environments выше, иначе обнуляем значения этих environments. Затем устанавливаем **ALFRESCO_SECURE_COMMS** =none

Для установки своих ключей достаточно примонтировать в директорию микросервиса ``/opt/ecos-alfresco-search-services/`` свои ключи.
Содержимое папки должно быть следующим:

.. code-block::

	ssl.repo.client.keystore
	ssl.repo.client.truststore
	ssl-keystore-passwords.properties
	ssl-truststore-passwords.properties 

Доп информация по некоторым параметрам может быть найдена тут:

`https://citeck.atlassian.net/wiki/x/Q4AgRg  <https://citeck.atlassian.net/wiki/x/Q4AgRg>`_

`https://docs.alfresco.com/search-services/1.3/config/properties <https://docs.alfresco.com/search-services/1.3/config/properties/>`_

Типовой вывод успешного развертывания в лог контейнера:

.. code-block::

	OpenJDK 64-Bit Server VM warning: Option UseConcMarkSweepGC was deprecated in version 9.0 and will likely be removed in a future release.
	2021-10-18 07:22:35.735 INFO  (main) [   ] o.e.j.s.Server jetty-9.3.27.v20190418, build timestamp: 2019-04-18T18:11:38Z, git hash: d3e249f86955d04bc646bb620905b7c1bc596a8d
	2021-10-18 07:22:36.283 INFO  (main) [   ] o.a.s.s.SolrDispatchFilter  ___      _       Welcome to Apache Solr™ version 6.6.5-patched.2 660ad3d2332b99205fbc436047f8d547511cd767 - tpage - 2019-11-27 08:18:56
	2021-10-18 07:22:36.284 INFO  (main) [   ] o.a.s.s.SolrDispatchFilter / __| ___| |_ _   Starting in standalone mode on port 8983
	2021-10-18 07:22:36.284 INFO  (main) [   ] o.a.s.s.SolrDispatchFilter \__ \/ _ \ | '_|  Install dir: /opt/ecos-alfresco-search-services/solr
	2021-10-18 07:22:36.298 INFO  (main) [   ] o.a.s.s.SolrDispatchFilter |___/\___/_|_|    Start time: 2021-10-18T07:22:36.286136Z
	2021-10-18 07:22:37.349 INFO  (main) [   ] o.e.j.s.Server Started @2533ms
	2021-10-18 07:22:47.283 WARN  (Thread-12) [   x:alfresco] o.a.s.c.Config XML parse warning in "solrres:/solrconfig.xml", line 1919, column 88: Include operation failed, reverting to fallback. Resource error reading file as XML (href='solrconfig_insight.xml'). Reason: Can't find resource 'solrconfig_insight.xml' in classpath or '/opt/ecos-alfresco-search-services/solrhome/alfresco'
	2021-10-18 07:22:47.916 WARN  (Thread-12) [   x:alfresco] o.a.s.c.SolrResourceLoader Solr loaded a deprecated plugin/analysis class [org.apache.solr.analysis.WordDelimiterFilterFactory]. Please consult documentation how to replace it accordingly.
	2021-10-18 07:22:47.923 WARN  (Thread-12) [   x:alfresco] o.a.s.c.SolrResourceLoader Solr loaded a deprecated plugin/analysis class [solr.SynonymFilterFactory]. Please consult documentation how to replace it accordingly.
	2021-10-18 07:22:49.231 WARN  (Thread-12) [   x:alfresco] o.a.s.h.c.AlfrescoSolrClusteringComponent No default engine for document clustering.
	2021-10-18 07:22:49.381 WARN  (Thread-12) [   x:alfresco] o.a.s.c.Config XML parse warning in "solrres:/solrconfig.xml", line 1919, column 88: Include operation failed, reverting to fallback. Resource error reading file as XML (href='solrconfig_insight.xml'). Reason: Can't find resource 'solrconfig_insight.xml' in classpath or '/opt/ecos-alfresco-search-services/solrhome/archive'
	2021-10-18 07:22:49.934 WARN  (searcherExecutor-7-thread-1-processing-x:alfresco) [   x:alfresco] o.a.s.SolrInformationServer Citeck unindex are initialized for alfresco
	2021-10-18 07:22:49.948 WARN  (Thread-12) [   x:alfresco] o.a.s.h.c.AlfrescoSolrClusteringComponent No default engine for document clustering.
	2021-10-18 07:22:49.979 WARN  (searcherExecutor-21-thread-1-processing-x:alfresco) [   x:alfresco] o.a.s.SolrInformationServer Citeck unindex are initialized for archive