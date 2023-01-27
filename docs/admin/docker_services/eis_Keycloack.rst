eis (Keycloak)
===============

Назначение:
----------------

Теги:
----------------

Базовые образы:
----------------

Шаблон сервиса docker-compose:
--------------------------------

.. code-block::

	eis:
		logging:
		options:
			max-size: "10m"
			max-file: "5"
		image: docker.io/jboss/keycloak:10.0.1
		container_name: eis
		hostname: eis
		restart:  unless-stopped
		environment:
			PROXY_ADDRESS_FORWARDING: "true"
			DB_VENDOR: POSTGRES
			DB_ADDR: eis_postgres
			DB_DATABASE: keycloak
			DB_USER: keycloak
			DB_SCHEMA: public
			DB_PASSWORD: LklsdkkuOIUjkh
			KEYCLOAK_USER: admin
			KEYCLOAK_PASSWORD: ERRESkhlu7iu4hkhjfd
				# Uncomment the line below if you want to specify JDBC parameters. The parameter below is just an example, and it shouldn't be used in production without knowledge. It is highly recommended that you read the PostgreSQL JDBC driver documentation in order to use it.
				#JDBC_PARAMS: "ssl=true"
		ports:
    		- 443:8443
		depends_on:
    		- eis_postgres
		networks:
    		- app_network
    eis_postgres:
		image: postgres:11
		container_name: eis_postgres
		hostname: eis_postgres
		volumes:
            - /opt/postgresql/keycloak:/var/lib/postgresql/data
        environment:
			POSTGRES_DB: keycloak
			POSTGRES_USER: keycloak
			POSTGRES_PASSWORD: LklsdkkuOIUjkh
        networks:
            - app_network

Используемые переменные:
-------------------------

Известные проблемы:
--------------------
 

Дополнительно:
----------------
 

Типовой вывод успешного развертывания в лог контейнера:
--------------------------------------------------------

