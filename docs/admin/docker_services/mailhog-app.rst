mailhog-app
============

Назначение:
--------------
Образ инструмента для e-mail тестирования

Шаблон сервиса docker-compose:
--------------------------------
::

	mailhog:
	    logging:
	      options:
	        max-size: "10m"
	        max-file: "5"
	    restart: unless-stopped
	    stop_grace_period: 1m
	    container_name: mailhog
	    hostname: mailhog
	    expose:
	      - 8025/tcp
	    environment:
	      - MH_UI_WEB_PATH=mailhog
	    image: mailhog/mailhog
	    networks:
	      - app_network

Используемые переменные:
---------------------------
*	**MH_UI_WEB_PATH** - web path для использования mailhog за проксирующим ecos-proxy (mailhog)

Типовой вывод успешного развертывания в лог контейнера:
-----------------------------------------------------------
::

	mailhog                     | [HTTP] Binding to address: 0.0.0.0:8025
	mailhog                     | 2020/05/14 06:43:07 Using in-memory storage
	mailhog                     | 2020/05/14 06:43:07 [SMTP] Binding to address: 0.0.0.0:1025
	mailhog                     | 2020/05/14 06:43:07 Serving under http://0.0.0.0:8025/mailhog/
	mailhog                     | Creating API v1 with WebPath: /mailhog
	mailhog                     | Creating API v2 with WebPath: /mailhog

