ecos-mongo-app
===============

Назначение:
--------------
Образ для развертывания контейнера с mongodb с преконфигурированными настройками датасорсов для микросервисов

Базовые образы:
----------------
*	`mongo_4 <https://hub.docker.com/layers/mongo/library/mongo/4.0/images/sha256-ccd97bd444338973ac143a22753e6b73a3e707a6a3edd512311a418a3e432cdb?context=explore>`_ - Официальный образ mongodb v 4.0.x

Шаблон сервиса docker-compose:
------------------------------------------
::
 
	mongo-app:
	    logging:
	      options:
	        max-size: "10m"
	        max-file: "5"
	    container_name: mongo-app
	    hostname: mongo-app
	    restart: unless-stopped
	    stop_grace_period: 1m
	    image: nexus.citeck.ru/mongo:4.0
	    env_file:
	     - ./env_dir/mongo-app.env
	    expose:
	      - 27017/tcp
	    volumes:
	      - /opt/mongo-app:/data/db/
	    networks:
	      - app_network

Используемые переменные:
----------------------------

*	**MONGO_INITDB_ROOT_USERNAME** - логин пользователя, который будет создан в **admin db с root** привилегиями
*	**MONGO_INITDB_ROOT_PASSWORD** - пароль привилегированного пользователя
*	**MONGO_INITDB_DATABASE** - определение базы данных, используемой в скриптах развертывания в ``/docker-entrypoint-initdb.d/*.js/sh. (1)``
*	**ECOS_HISTORY_APP_DATASOURCE_DATABASE** - db микросервиса истории **(ecos-history)**
*	**ECOS_HISTORY_APP_DATASOURCE_USERNAME** - логин для мкр истории, роль dbOwner **(ecos-history)**
*	**ECOS_HISTORY_APP_DATASOURCE_PASSWORD** - пароль для мкр истории **(ecos-history-password)**
*	**ECOS_PROCESS_APP_DATASOURCE_DATABASE** - db микросервиса ecos-process **(ecos-process)**
*	**ECOS_PROCESS_APP_DATASOURCE_USERNAME **- логин для мкр ecos-process, роль dbOwner **(ecos-process)**
*	**ECOS_PROCESS_APP_DATASOURCE_PASSWORD** - пароль для мкр ecos-process **(ecos-process-password)**
 	
(1) - This variable allows you to specify the name of a database to be used for creation scripts in /docker-entrypoint-initdb.d/.js (see Initializing a fresh instance below). MongoDB is fundamentally designed for «create on first use», so if you do not insert data with your JavaScript files, then no database is created.

Известные проблемы:
--------------------
::
 
	2020-05-06T07:44:14.752+0000 I STORAGE [initandlisten] ** WARNING: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine
	2020-05-06T07:44:14.752+0000 I STORAGE [initandlisten] ** See `mongo_prodnotes_filesystem <http://dochub.mongodb.org/core/prodnotes-filesystem>`_ 

Типовой вывод успешного развертывания в лог контейнера:
--------------------------------------------------------
::

	MongoDB shell version v4.0.18
	connecting to: mongodb://127.0.0.1:27017/test?gssapiServiceName=mongodb
	2020-05-06T07:44:13.565+0000 I NETWORK  [listener] connection accepted from 127.0.0.1:42378 #3 (1 connection now open)
	2020-05-06T07:44:13.565+0000 I NETWORK  [conn3] received client metadata from 127.0.0.1:42378 conn3: { application: { name: "MongoDB Shell" }, driver: { name: "MongoDB Internal Client", version: "4.0.18" }, os: { type: "Linux", name: "Ubuntu", architecture: "x86_64", version: "16.04" } }
	Implicit session: session { "id" : UUID("3cb7f158-dfaa-4ffd-896f-b36052828f19") }
	MongoDB server version: 4.0.18
	2020-05-06T07:44:13.593+0000 I ACCESS   [conn3] Successfully authenticated as principal root_user on admin from client 127.0.0.1:42378
	1
	ecos-process
	Successfully added user: {
	        "user" : "ecos-process",
	        "roles" : [
	                {
	                        "role" : "dbOwner",
	                        "db" : "ecos-process"
	                }
	        ]
	}
	ecos-history
	Successfully added user: {
	        "user" : "ecos-history",
	        "roles" : [
	                {
	                        "role" : "dbOwner",
	                        "db" : "ecos-history"
	                }
	        ]
	}
	bye

