onlyoffice-ds-app
===================

Назначение:
-------------
Образ, включающий набор инструментов для развертывания onlyoffice-ds

Шаблон сервиса docker-compose:
---------------------------------------
::

	onlyoffice-ds:
	    logging:
	      options:
	        max-size: "10m"
	        max-file: "5"
	    container_name: onlyoffice-ds
	    hostname: onlyoffice-ds
	    image: onlyoffice/documentserver:latest
	    restart: unless-stopped
	    stop_grace_period: 1m
	    networks:
	      - app_network
	    expose:
	      - '80'
	      - '443'
	    volumes:
	      - /opt/onlyoffice/document_data:/var/www/onlyoffice/Data
	      - /opt/onlyoffice/document_log:/var/log/onlyoffice
	      - /opt/onlyoffice/document_fonts:/usr/share/fonts/truetype/custom
	      - /opt/onlyoffice/document_forgotten:/var/lib/onlyoffice/documentserver/App_Data/cache/files/forgotten

Типовой вывод успешного развертывания в лог контейнера:
-----------------------------------------------------------------
::

	onlyoffice-ds               |  * Starting PostgreSQL 10 database server
	onlyoffice-ds               |    ...done.
	onlyoffice-ds               |  * Starting RabbitMQ Messaging Server rabbitmq-server
	onlyoffice-ds               |    ...done.
	onlyoffice-ds               | Starting redis-server: redis-server.
	onlyoffice-ds               | Starting supervisor: supervisord.
	onlyoffice-ds               |  * Starting periodic command scheduler cron
	onlyoffice-ds               |    ...done.
	onlyoffice-ds               |  * Starting nginx nginx
	onlyoffice-ds               |    ...done.
	onlyoffice-ds               | Generating AllFonts.js, please wait...Done
	onlyoffice-ds               | Generating presentation themes, please wait...Done
	onlyoffice-ds               | ds:docservice: stopped
	onlyoffice-ds               | ds:docservice: started
	onlyoffice-ds               | ds:converter: stopped
	onlyoffice-ds               | ds:converter: started
	onlyoffice-ds               |  * Reloading nginx configuration nginx
	onlyoffice-ds               |    ...done.
	onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/converter/err.log <==
	onlyoffice-ds               | 
	onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/converter/out.log <==
	onlyoffice-ds               | [2020-05-14T20:35:52.505] [WARN] nodeJS - update cluster with 1 workers
	onlyoffice-ds               | [2020-05-14T20:36:27.586] [WARN] nodeJS - update cluster with 1 workers
	onlyoffice-ds               | [2020-05-14T20:36:27.604] [WARN] nodeJS - worker 903 started.
	onlyoffice-ds               | [2020-05-14T20:36:27.605] [WARN] nodeJS - update cluster with 1 workers
	onlyoffice-ds               | [2020-05-15T09:48:03.094] [WARN] nodeJS - update cluster with 1 workers
	onlyoffice-ds               | [2020-05-15T09:48:03.125] [WARN] nodeJS - worker 861 started.
	onlyoffice-ds               | [2020-05-15T09:48:03.126] [WARN] nodeJS - update cluster with 1 workers
	onlyoffice-ds               | [2020-05-15T09:48:35.735] [WARN] nodeJS - update cluster with 1 workers
	onlyoffice-ds               | [2020-05-15T09:48:35.746] [WARN] nodeJS - worker 926 started.
	onlyoffice-ds               | [2020-05-15T09:48:35.748] [WARN] nodeJS - update cluster with 1 workers
	onlyoffice-ds               | 
	onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/docservice/err.log <==
	onlyoffice-ds               | 
	onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/docservice/out.log <==
	onlyoffice-ds               | [2020-05-14T20:36:05.671] [WARN] nodeJS - error description: docId = 0a2955d7-9505-421b-8e14-4bfaa68d994a_1.0 errorId = Other error
	onlyoffice-ds               | [2020-05-14T20:36:26.944] [WARN] nodeJS - Express server starting...
	onlyoffice-ds               | [2020-05-14T20:36:26.947] [WARN] nodeJS - Plugins watch exception (https://nodejs.org/docs/latest/api/fs.html#fs_availability).
	onlyoffice-ds               | [2020-05-14T20:36:27.185] [WARN] nodeJS - Express server listening on port 8000 in production-linux mode
	onlyoffice-ds               | [2020-05-15T09:48:04.094] [WARN] nodeJS - Express server starting...
	onlyoffice-ds               | [2020-05-15T09:48:04.100] [WARN] nodeJS - Plugins watch exception (https://nodejs.org/docs/latest/api/fs.html#fs_availability).
	onlyoffice-ds               | [2020-05-15T09:48:04.354] [WARN] nodeJS - Express server listening on port 8000 in production-linux mode
	onlyoffice-ds               | [2020-05-15T09:48:34.897] [WARN] nodeJS - Express server starting...
	onlyoffice-ds               | [2020-05-15T09:48:34.901] [WARN] nodeJS - Plugins watch exception (https://nodejs.org/docs/latest/api/fs.html#fs_availability).
	onlyoffice-ds               | [2020-05-15T09:48:35.083] [WARN] nodeJS - Express server listening on port 8000 in production-linux mode
	onlyoffice-ds               | 
	onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/gc/err.log <==
	onlyoffice-ds               | 
	onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/gc/out.log <==
	onlyoffice-ds               | 
	onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/metrics/err.log <==
	onlyoffice-ds               | 
	onlyoffice-ds               | ==> /var/log/onlyoffice/documentserver/metrics/out.log <==
	onlyoffice-ds               |   gauges: { 'statsd.timestamp_lag': 0 },
	onlyoffice-ds               |   timer_data: {},
	onlyoffice-ds               |   counter_rates:
	onlyoffice-ds               |    { 'statsd.bad_lines_seen': 0,
	onlyoffice-ds               |      'statsd.packets_received': 0,
	onlyoffice-ds               |      'statsd.metrics_received': 0 },
	onlyoffice-ds               |   sets: {},
	onlyoffice-ds               |   pctThreshold: [ 90 ] }
	onlyoffice-ds               | 15 May 09:48:02 - [796] reading config file: ./config/config.js
	onlyoffice-ds               | 15 May 09:48:02 - server is up INFO

