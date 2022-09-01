ecos-postgresql-app
====================

Назначение:
------------
Образ, собранный на официальном образе postgresql 9.4.x с добавлением скрипта инициализации баз данных и пользователей

Теги:
------
`nexus_alpine <http://nexus.citeck.ru/ecos-postgres:9.4-alpine>`_

Базовые образы:
----------------
**postgres:9.4-alpine** - официальный образ postgresql 9.4.x на базе alpine linux

Шаблон сервиса docker-compose:
----------------------------------
::

	ecos-postgresql:
	    container_name: ecos-postgresql
	    restart: unless-stopped
	    ports:
	      - 127.0.0.1:50432:5432/tcp
	    environment:
	      - POSTGRES_PASSWORD=alfr3sc0
	      - DB_NAME=alfresco
	      - FLOWABLE_DBNAME=alf_flowable
	      - HISTORY_DBNAME=history_service
	      - CASE_MODEL_DBNAME=alfresco_case_model
	    hostname: ecos-postgresql
	    image: nexus.citeck.ru/ecos-postgres:9.4-alpine
	    stop_grace_period: 1m
	    volumes:
	      - /opt/alfresco/postgresql/:/var/lib/postgresql/data
	    networks:
	      - app_network

Используемые переменные:
-------------------------

*	**POSTGRES_PASSWORD** - обязательный параметр за исключением 
*   **POSTGRES_HOST_AUTH_METHOD=trust**, пароль рутового пользователя
*	**POSTGRES_USER** - переопределение дефолтного пользователя **postgres**
*	**POSTGRES_DB** - переопределение дефолтной базы данных
*	**POSTGRES_INITDB_ARGS** - дополнительные параметры для инициализации кластера
*	**POSTGRES_INITDB_WALDIR** - переопределение дефолтной директории хранения логов транзакций
*	**POSTGRES_HOST_AUTH_METHOD** - метод аутентификации host подключений для всех бд, пользователей и адресов в **pg_hba.conf**. Дефолтное значение **md5**
*	**PGDATA** - переопределение дефолтной директории хранения фалов инициируемого кластера
*	**DB_NAME** - определение базы данных **ecos**
*	**DB_USERNAME** - определение пользователя для базы данных **ecos/flowable/ecos-history**
*	**DB_PASSWORD** - пароль создаваемого пользователя
*	**FLOWABLE_DBNAME** - определение базы данных **flowable**
*	**HISTORY_DBNAME** - определение базы данных для ecos-history-app (устаревший параметр, базы данных мкр вынесены в отдельный инстанс)
*	**CASE_MODEL_DBNAME** - определение базы данных **ecos-case-model-app**

Известные проблемы:
--------------------
*	EOL версии postgresl
*	Используется один пользователь для баз данных
*	Отсутствие конфигурации postgresql.conf, pg_hba.conf
*	Отсутствие конфигурации используемых схем

Типовой вывод принятых настроек в лог контейнера:
--------------------------------------------------
::

	The files belonging to this database system will be owned by user "postgres".
	This user must also own the server process.

	The database cluster will be initialized with locale "en_US.utf8".
	The default database encoding has accordingly been set to "UTF8".
	The default text search configuration will be set to "english".

	Data page checksums are disabled.

	fixing permissions on existing directory /var/lib/postgresql/data ... ok
	creating subdirectories ... ok
	selecting default max_connections ... 100
	selecting default shared_buffers ... 128MB
	selecting default timezone ... UTC
	selecting dynamic shared memory implementation ... posix
	creating configuration files ... ok
	creating template1 database in /var/lib/postgresql/data/base/1 ... ok
	initializing pg_authid ... ok
	setting password ... ok
	initializing dependencies ... ok
	creating system views ... ok
	loading system objects' descriptions ... ok
	creating collations ... sh: locale: not found
	ok
	No usable system locales were found.
	Use the option "--debug" to see details.
	creating conversions ... ok
	creating dictionaries ... ok
	setting privileges on built-in objects ... ok
	creating information schema ... ok
	loading PL/pgSQL server-side language ... ok
	vacuuming database template1 ... ok
	copying template1 to template0 ... ok
	copying template1 to postgres ... ok
	syncing data to disk ... ok

	Success. You can now start the database server using:

	    postgres -D /var/lib/postgresql/data
	or
	    pg_ctl -D /var/lib/postgresql/data -l logfile start


	WARNING: enabling "trust" authentication for local connections
	You can change this by editing pg_hba.conf or using the option -A, or
	--auth-local and --auth-host, the next time you run initdb.

	WARNING: No password has been set for the database.
	         This will allow anyone with access to the
	         Postgres port to access your database. In
	         Docker's default configuration, this is
	         effectively any other container on the same
	         system.

	         Use "-e POSTGRES_PASSWORD=password" to set
	         it in "docker run".

	waiting for server to start....LOG:  database system was shut down at 2020-04-27 23:16:37 UTC
	LOG:  MultiXact member wraparound protections are now enabled
	LOG:  database system is ready to accept connections
	LOG:  autovacuum launcher started
	 done
	server started

	/usr/local/bin/docker-entrypoint.sh: sourcing /docker-entrypoint-initdb.d/initDBs.sh
	CREATE ROLE
	CREATE DATABASE
	CREATE DATABASE
	CREATE DATABASE
	CREATE DATABASE
	CREATE EXTENSION
	CREATE EXTENSION

	waiting for server to shut down....LOG:  received fast shutdown request
	LOG:  aborting any active transactions
	LOG:  autovacuum launcher shutting down
	LOG:  shutting down
	LOG:  database system is shut down
	 done
	server stopped

	PostgreSQL init process complete; ready for start up.

	LOG:  database system was shut down at 2020-04-27 23:16:40 UTC
	LOG:  MultiXact member wraparound protections are now enabled
	LOG:  database system is ready to accept connections
	LOG:  autovacuum launcher started

