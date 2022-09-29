ecos-microservices-postgresql-app
=====================================

Назначение
------------

Образ, собранный на официальном образе postgresql 12.x с добавлением скрипта инициализации баз данных и пользователей

Теги:
------------
`nexus.citeck.ru/postrgesql:msvc-latest <nexus.citeck.ru/postrgesql:msvc-latest>`_- собран на базовом образе  postgres:12, используется в композ проектах, файлы конфигурации размещаются в образе

`nexus.citeck.ru/postrgesql:12 <nexus.citeck.ru/postrgesql:12>`_ - базовый образ  postgres:12, размещен в нашем docker registry, используется в k8s объектах, файлы конфигурации и скрипт развертывания конфигурируются через configmap

Базовые образы
---------------

* **postgres:12** 

Шаблон сервиса docker-compose:
------------------------------------

.. code-block::
	
	ecos-microservices-postgresql-app:
		container_name: ecos-microservices-postgresql-app
		hostname: ecos-microservices-postgresql-app
		restart: unless-stopped
		image: nexus.citeck.ru/postgresql:msvc-latest
		stop_grace_period: 1m
		command: ["postgres", "-c", "config_file=/var/lib/postgresql/conf/postgresql.conf"]
		expose:
    		- 5432/tcp
		env_file:
    		- ./env_dir/ecos-microservices-postgresql-app.env
		volumes:
    		- /opt/ecos-microservices-postgresql:/var/lib/postgresql/data
		networks:
		- app_network

Используемые переменные:
------------------------

* **ECOS_APPS_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-apps-app

* **ECOS_APPS_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-apps-app

* **ECOS_APPS_APP_DATASOURCE_PASSWORD**  - пароль для мрк ecos-apps-app


* **ECOS_GATEWAY_APP_DATASOURCE_DATABASE**  - база данных для мрк ecos-gateway-app

* **ECOS_GATEWAY_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-gateway-app

* **ECOS_GATEWAY_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-gateway-app

 

* **ECOS_UISERV_APP_DATASOURCE_DATABASE**  - база данных для мрк ecos-uiserv-app

* **ECOS_UISERV_APP_DATASOURCE_USERNAME**  - пользователь для мрк ecos-uiserv-app

* **ECOS_UISERV_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-uiserv-app

 

* **ECOS_INTEGRATIONS_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-integrations-app

* **ECOS_INTEGRATIONS_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-integrations-app

* **ECOS_INTEGRATIONS_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-integrations-app
 

* **ECOS_MODEL_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-model-app

* **ECOS_MODEL_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-model-app

* **ECOS_MODEL_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-model-app
 

* **ECOS_NOTIFICATIONS_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-notifications-app

* **ECOS_NOTIFICATIONS_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-notifications-app

* **ECOS_NOTIFICATIONS_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-notifications-app
 

* **ECOS_HISTORY_APP_DATASOURCE_DATABASE** - база данных для мрк ecos-history-app

* **ECOS_HISTORY_APP_DATASOURCE_USERNAME** - пользователь для мрк ecos-history-app

* **ECOS_HISTORY_APP_DATASOURCE_PASSWORD** - пароль для мрк ecos-history-app

 

* **POSTGRES_PASSWORD** - обязательный параметр за исключением **POSTGRES_HOST_AUTH_METHOD=trust**, пароль привилегированного пользователя  **postgres**

* **POSTGRES_USER** - переопределение дефолтного пользователя **postgres**

* **POSTGRES_DB** - переопределение дефолтной базы данных

* **POSTGRES_INITDB_ARGS** - дополнительные параметры для инициализации кластера

* **POSTGRES_INITDB_WALDIR** - переопределение дефолтной директории хранения логов транзакций

* **POSTGRES_HOST_AUTH_METHOD** - метод аутентификации host подключений для **всех бд**, пользователей и адресов в pg_hba.conf. Дефолтное значение **md5**

* **PGDATA** - переопределение дефолтной директории хранения фалов инициируемого кластера

Известные проблемы:
------------------------

* Не реализована возможность конфигурирования датасорсов (добавление/удаление баз данных, пользователей) после первичного развертывания
* Отсутствие конфигурации используемых схем
* Конфигурирование postgresql только через пересборку образа с внесением изменений в конфигурационные файлы

Типовой вывод принятых настроек в лог контейнера:
------------------------------------------------------------

.. code-block::

	The files belonging to this database system will be owned by user "postgres".
	This user must also own the server process.

	The database cluster will be initialized with locale "en_US.utf8".
	The default database encoding has accordingly been set to "UTF8".
	The default text search configuration will be set to "english".

	Data page checksums are disabled.

	fixing permissions on existing directory /var/lib/postgresql/data ... ok
	creating subdirectories ... ok
	selecting dynamic shared memory implementation ... posix
	selecting default max_connections ... 100
	selecting default shared_buffers ... 128MB
	selecting default time zone ... UTC
	creating configuration files ... ok
	running bootstrap script ... ok
	performing post-bootstrap initialization ... sh: locale: not found
	2020-04-28 08:59:20.042 UTC [30] WARNING:  no usable system locales were found
	ok
	syncing data to disk ... initdb: warning: enabling "trust" authentication for local connections
	You can change this by editing pg_hba.conf or using the option -A, or
	--auth-local and --auth-host, the next time you run initdb.
	ok


	Success. You can now start the database server using:

		pg_ctl -D /var/lib/postgresql/data -l logfile start

	waiting for server to start....2020-04-28 08:59:20.503 UTC [35] LOG:  starting PostgreSQL 12.2 on x86_64-pc-linux-musl, compiled by gcc (Alpine 9.2.0) 9.2.0, 64-bit
	2020-04-28 08:59:20.506 UTC [35] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
	2020-04-28 08:59:20.555 UTC [36] LOG:  database system was shut down at 2020-04-28 08:59:20 UTC
	2020-04-28 08:59:20.563 UTC [35] LOG:  database system is ready to accept connections
	done
	server started

	/usr/local/bin/docker-entrypoint.sh: sourcing /docker-entrypoint-initdb.d/init-db.sh
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT
	CREATE ROLE
	CREATE DATABASE
	GRANT

	waiting for server to shut down....2020-04-28 08:59:21.371 UTC [35] LOG:  received fast shutdown request
	2020-04-28 08:59:21.374 UTC [35] LOG:  aborting any active transactions
	2020-04-28 08:59:21.376 UTC [35] LOG:  background worker "logical replication launcher" (PID 42) exited with exit code 1
	2020-04-28 08:59:21.376 UTC [37] LOG:  shutting down
	2020-04-28 08:59:21.409 UTC [35] LOG:  database system is shut down
	done
	server stopped

	PostgreSQL init process complete; ready for start up.

	2020-04-28 08:59:21.494 UTC [1] LOG:  starting PostgreSQL 12.2 on x86_64-pc-linux-musl, compiled by gcc (Alpine 9.2.0) 9.2.0, 64-bit
	2020-04-28 08:59:21.494 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
	2020-04-28 08:59:21.494 UTC [1] LOG:  listening on IPv6 address "::", port 5432
	2020-04-28 08:59:21.502 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
	2020-04-28 08:59:21.538 UTC [46] LOG:  database system was shut down at 2020-04-28 08:59:21 UTC
	2020-04-28 08:59:21.542 UTC [1] LOG:  database system is ready to accept connections
