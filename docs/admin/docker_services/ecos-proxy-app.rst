.. _ecos_proxy_app:

ecos-proxy-app
================

Назначение
--------------
Образ проксирующего сервера со сборкой проекта ecos-ui. 

Базовые образы
--------------
nexus.citeck.ru/ecos-nginx-spnego:stable -  Nginx (1.17.6) собирается из исходников + в сборку включен модуль spnego (1.1.0)  для интеграции с AD заказчика и реализации SSO. Базовый образ строится на alpine:3.7 
openresty/openresty:centos-rpm - openresty (1.15.8.3) устанавливается из репо пакетами. Базовый образ строится на CentOS 7.

Шаблон сервиса docker-compose
------------------------------
::

 ecos-proxy:
    logging:
      options:
        max-size: "10m"
        max-file: "5"
    container_name: ecos-proxy
    restart: unless-stopped
    stop_grace_period: 1m
    hostname: ecos-proxy
    ports:
      - 80:80/tcp
    env_file:
     - ./env_dir/ecos-proxy.env
    image: nexus.citeck.ru/ecos-proxy:<ECOS_PROXY_IMAGE
    networks:
      - app_network

Используемые переменные
----------------------------
*	DEFAULT_LOCATION_V2 - переключение дефолтного редиректа ( / ) с share/page на v2/. Формат переменной: DEFAULT_LOCATION_V2=true (параметр дублируется в клиенте в настройках системных журналов)
*	ECOS_INIT_DELAY - таймаут запуска entrypoint скрипта, формирующего default.conf сервера. По умолчанию 30с для нормализации инициализации апстримов в compose проектах.
*	CADVISOR_TARGET - если параметр не указан, то из файла конфигурации nginx будет удален апсрим cadvisor и зависимые от него локейшены. Формат переменной: CADVISOR_TARGET=ip_or_fqdn:port
*	NODE_EXPORTER_TARGET - если параметр не указан, то из файла конфигурации nginx будет удален апсрим node-exporter и зависимые от него локейшены. Формат переменной: NODE_EXPORTER_TARGET=ip_or_fqdn:port
*	USE_EXTERNAL_CONFIGURATION - при объявлении данной переменной будет удален конфигурационный файл default.conf в директории nginx. Используется для разработки и конфигурирования, при этом директории статики, конфигурационные файлы, сертификаты и прочее необходимо прокинуть в контейнер через pv. Директория монтирования файла конфигурации nginx  - /etc/nginx/conf.d/. Формат переменной: USE_EXTERNAL_CONFIGURATION=true
*	PROXY_TARGET - если параметр не указан в файле ecos-proxy.env, то выставляется дефолтное проксирование на контейнер ecos- ecos:8080. Соответственно, при объявлении параметра в файле переменных будет заменено значение ecos:8080 в апстриме ecos конфигурации nginx образа на указанное в файле переменных. Формат переменной: PROXY_TARGET=ip_or_fqdn:port
*	GATEWAY_TARGET - если параметр не указан, то из файла конфигурации nginx будет удален апсрим gateway и зависимые от него локейшены. Формат переменной: GATEWAY_TARGET=ip_or_fqdn:port
*	ENABLE_LOGGING - по умолчанию логирование контейнера отключено, объявление данной переменной включит стандартное логирование nginx, выставление переменной в debug включит расширенный режим отладки обработки пакетов nginx. Формат переменной: ENABLE_LOGGING=true (debug для расширенного режима)
*	ENABLE_SERVER_STATUS - включение локейшена с выдачей статистики сервера nginx, используется для централизированного мониторинга. Локейш доступен только из docker сети. Формат переменной: ENABLE_SERVER_STATUS=true
*	ENABLE_MOBILE_APP_ACCESS - включение локейшена /gateeway с проверкой bearer токена в хидере Authorization. Используется для доступа мобильным приложением. Формат переменной: ENABLE_MOBILE_APP_ACCESS=true. При включении данного функционала требуется сконфигрурировать переменные EIS_ID, REALM_ID, CLIENT_SECRET для интеграции с keycloak.
*	ENABLE_OIDC_FULL_ACCESS - включение проверки bearer токена в хидере Authorization для любого из обрабатываемых локейшенов. Формат переменной: ENABLE_OIDC_FULL_ACCESS=true. При включении данного функционала требуется сконфигрурировать переменные EIS_ID, REALM_ID, CLIENT_SECRET для интеграции с keycloak.
*	ONLYOFFICE_TARGET - включение локейшена /onlyoffice/ для интеграции ecos c развернутым инстансом OnlyOffice. Формат переменной: ONLYOFFICE_TARGET=ip_or_fqdn:port
*	MAILHOG_TARGET - включение локейшена проксирования в ui контейнера mailhog. MAILHOG_TARGET=ip_or_fqdn:port
*	ECOS_REGISTRY_TARGET - включение локейшена проксирования в ui контейнера ecos(jhipster)-registry. Формат переменной: ECOS_REGISTRY_TARGET=ip_or_fqdn:port
*	RABBITMQ_TARGET - включение локейшена проксирования в managment ui контейнера rabbitmq. Формат переменной: RABBITMQ_TARGET=ip_or_fqdn:port
*	EIS_TARGET - включение локейшена проксирования в ui контейнера eis. Используется при размещении eis за проксирующим сервером в сетевом сегменте заказчика. Формат переменной: EIS_TARGET=ip_or_fqdn:port
*	ECOS_PAGE_TITLE - настройка заголовка index.html страницы браузера для нового интерфейса (v2). По умолчанию Citeck ECOS
*	EIS_PROTO – протокол, по которому идёт взаимодействие с keycloak. Значение по-умолчанию  https, опционально можно поставить http
* GATEWAY_TLS_ENABLED - включить HTTPS до ecos-gateway (v4)
* GATEWAY_TLS_CERT - корневой сертификат для проверки сертификата ecos-gateway. Можно указать непосредственно тот же сертификат, который использует gateway. По умолчанию цепочка сертификатов проверяется на 2 уровня. По умолчанию false. (v4)
* GATEWAY_TLS_NAME - имя gateway сервера. nginx всегда проверяет хост gateway на соответствие сертификату, но если хост динамический, то можно использовать эту настройку чтобы задать его константой. (v4)
* ENABLE_HTTPS - включает сервер по SERVER_HTTPS_PORT порту и ждет сертификаты SERVER_TLS_CERT и SERVER_TLS_KEY (v3, v4)
* ENABLE_HSTS - добавлять заголовок Strict-Transport-Security к ответам сервера. (v3, v4)
* SERVER_TLS_CERT - сертификат сервера. По умолчанию /app/ssl/ecos-proxy.cert (v4)
* SERVER_TLS_KEY - приватный ключ сервера. По умолчанию /app/ssl/ecos-proxy.key (v4)
* SERVER_HTTP_PORT - http порт, который будет слушать nginx. По умолчанию зависит от пользователя, под которым запускается контейнер. Если это root, то 80, иначе - 8080 (v4)
* SERVER_HTTPS_PORT - https порт, который будет слушать nginx. По умолчанию зависит от пользователя, под которым запускается контейнер. Если это root, то 443, иначе - 8443 (v4)
* MIN_TLS_VER - минимально допустимая версия TLS. Допустимные значения: [1.3, 1.2, 1.0] (v3, v4)

Не реализованы:

*	SOLR_TARGET
*	ECOS_REGISTRY_TARGET (проблема с api)

Типовой вывод принятых настроек в лог контейнера
--------------------------------------------------------
::

	ecos-proxy                  | Wait 30 seconds and run nginx
	ecos-proxy                  | - Logging disabled
	ecos-proxy                  | + Server status monitoring enabled!
	ecos-proxy                  | + Changed upstream gateway: gateway-app:8085
	ecos-proxy                  | - Disabled api-auth upstream and locations
	ecos-proxy                  | + Changed mailhog upstream: mailhog:8025
	ecos-proxy                  | - Disabled gss
	ecos-proxy                  | + Changed ecos-registry upstream: jhipster-registry:8761
	ecos-proxy                  | + Changed rabbitmq upstream: rabbitmq:15672
	ecos-proxy                  | - Disabled eis upstream and locations
	ecos-proxy                  | - Disabled solr location


