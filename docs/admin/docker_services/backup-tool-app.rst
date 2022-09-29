backup-tool-app
================

Назначение:
----------------

Образ для создания бекапов.

Создан на базе решения `Backup 4.4.1.  <https://github.com/backup/backup>`_
Документация находится `тут  <http://backup.github.io/backup/v4/>`_

Выключен по умолчанию.

Исходники находятся в репозитории `https://gitlab.citeck.ru/citeck-projects/citeck-devops <https://gitlab.citeck.ru/citeck-projects/citeck-devops/>`_

Теги:
-----

Актуальная версия `nexus.citeck.ru/backup-tool <nexus.citeck.ru/backup-tool>`_ 0.0.3
UPD:  По сравнению с предыдущей версией ( 0.0.2 ) поправлены СА серты R3 и актуализированы версии вспомогательных утилит.

Шаблон сервиса docker-compose:
--------------------------------

.. code-block::

	services:
		app:
			logging:
			 options:
				max-size: "10m"
				max-file: "5"
			 hostname: backup-tool-app
			 restart: always
			 stop_grace_period: 1m
			image: nexus.citeck.ru/backup-tool:0.0.2
			env_file:
			 - ./environments/backup-tool-app.env
			volumes:
		{% if (BackupToolApp.environments.backup.contentstore)and(EcosApp.enabled) %}
			- {{ EcosProjectDataDir }}ecos-app/:/content/
		{% endif %}
		{% if (BackupToolApp.environments.backup.index) and (EcosSearchApp.enabled) %}
			- {{ EcosProjectDataDir }}ecos-search-app/:/index/
		{% endif %}
		{% if BackupToolApp.environments.export.local.enabled %}
			- {{ EcosProjectDataDir }}backups/:/backups/
		{% endif %}
			networks:
			- app_network

Используемые переменные:
--------------------------------

Пример ожидаемых переменных в ``backup-tool-app.env`` с значениями по умолчанию:

  * **BACKUP_SHEDULE=”0 0 * * *”**
    
  * **BACKUP_DEBUG_CONFIG=false**
    
  * **BACKUP_INSTANCE_ID=local.dev**
    
  * **BACKUP_CONTENTSTORE=false**
    
  * **BACKUP_INDEX=false**
    
  * **BACKUP_POSTGRESQL_APP_1=false**

  * **BACKUP_POSTGRESQL_APP_1_HOST=ecos-postgresql-app**
    
  * **BACKUP_POSTGRESQL_APP_1_PORT=5432**
    
  * **BACKUP_POSTGRESQL_APP_1_USERNAME=user**
    
  * **BACKUP_POSTGRESQL_APP_1_PASSWORD=password**
    
  * **BACKUP_POSTGRESQL_APP_2=false**
    
  * **BACKUP_POSTGRESQL_APP_2_HOST=ecos-microservices-postgresql-app**
    
  * **BACKUP_POSTGRESQL_APP_2_PORT=5432**
    
  * **BACKUP_POSTGRESQL_APP_2_USERNAME=user**
    
  * **BACKUP_POSTGRESQL_APP_2_PASSWORD=password**
    
  * **BACKUP_MONGODB_APP_1=false**

  * **BACKUP_MONGODB_APP_1_HOST=mongodb-app**
    
  * **BACKUP_MONGODB_APP_1_PORT=27017**
    
  * **BACKUP_MONGODB_APP_1_USERNAME=user**
    
  * **BACKUP_MONGODB_APP_1_PASSWORD=password**
    
  * **BACKUP_MYSQL_APP_1=false**
    
  * **BACKUP_MYSQL_APP_1_HOST=mysql-app**
    
  * **BACKUP_MYSQL_APP_1_PORT=3306**
    
  * **BACKUP_MYSQL_APP_1_USERNAME=user**
    
  * **BACKUP_MYSQL_APP_1_PASSWORD=password**

  * **BACKUP_LOCAL_EXPORT=false**
    
  * **BACKUP_LOCAL_EXPORT_KEEP=7**
    
  * **BACKUP_S3_EXPORT=false**
    
  * **BACKUP_S3_EXPORT_USE_FOG_OPTIONS=true**
    
  * **BACKUP_S3_EXPORT_ENDPOINT=s3.citeck.ru**
    
  * **BACKUP_S3_EXPORT_REGION=**
    
  * **BACKUP_S3_EXPORT_KEY=changemeplease**
    
  * **BACKUP_S3_EXPORT_SECRET=changemeplease**
    
  * **BACKUP_S3_EXPORT_BUCKET=bucket**
    
  * **BACKUP_S3_EXPORT_KEEP=7**
    
  * **BACKUP_MATTERMOST_NOTIFICATIONS=false**
    
  * **BACKUP_MATTERMOST_NOTIFICATIONS_WEBHOOK=changemeplease**
    
  * **BACKUP_MATTERMOST_NOTIFICATIONS_CHANNEL=channel**

``BACKUP_POSTGRESQL_APP_*``

``BACKUP_MONGODB_APP_*``

``BACKUP_MYSQL_APP_*``

Отвечают за авторизацию в субд. При использовании шаблонизатора docker-compose значения полей подставляются автоматически. Эти параметры в большинстве случаев нет необходимости предопределять.

* **BACKUP_SHEDULE** - Как часто необходимо делать бекапы. Задается в формате cron. По умолчанию ежедневно в 00:00. p.s. `вот удобный калькулятор <https://crontab.guru/>`_

* **BACKUP_DEBUG_CONFIG** - Возвращает список переменных и сконфигурированый backup_plan.rb.

* **BACKUP_INSTANCE_ID** - Имя инстанса. Используется для оповещений в mattermost и для экспорта в S3.

* **BACKUP_CONTENTSTORE** - Включает бекапы для ``ecos-app`` ``contentstore``.

* **BACKUP_INDEX** - Включает бекапы для ``ecos-search-app`` ``index``.

* **BACKUP_LOCAL_EXPORT** - Включает хранение бекапов на сервере, в директории ``backups/``.

* **BACKUP_LOCAL_EXPORT_KEEP** - Сколько дней хранить бекапы в директории ``backups/``. Зависит о частоты выполнения бекап плана.

* **BACKUP_S3_EXPORT** - Включает экспорт бекапов в S3 хранилище.

* **BACKUP_S3_EXPORT_USE_FOG_OPTIONS** - Переключатель необходимый для использования в S3-like хранилищах, например в `DigitalOcean’s Spaces <https://developers.digitalocean.com/documentation/v2/>`_ или `Minio <https://www.minio.io/>`_. Использует в качестве хоста переменную BACKUP_S3_EXPORT_ENDPOINT. Более подробно в `документации <https://backup.github.io/backup/v4/storage-s3/>`_ 

* **BACKUP_S3_EXPORT_ENDPOINT** - Адрес S3-like сервера. Зависит от значения ``true`` переменной BACKUP_S3_EXPORT_USE_FOG_OPTIONS.

* **BACKUP_S3_EXPORT_REGION** - Регион для amazon S3. 

* **BACKUP_S3_EXPORT_KEY** - S3 ключ авторизации.

* **BACKUP_S3_EXPORT_SECRET** - S3 сикрет авторизации.

* **BACKUP_S3_EXPORT_BUCKET** - Ведерко, куда складывать бекапы в S3.

* **BACKUP_S3_EXPORT_KEEP** - Сколько дней хранить бекапы в S3 хранилище. Зависит о частоты выполнения бекап плана.

* **BACKUP_MATTERMOST_NOTIFICATIONS** - Включает отправку уведомлений в mattermost / slack.

* **BACKUP_MATTERMOST_NOTIFICATIONS_WEBHOOK** - Полный адрес webhook, куда нужно отправлять уведомления. `Например <https://mm.citeck.ru/hooks/apbhdnp72djpexxmofkywptyy>`_.

* **BACKUP_MATTERMOST_NOTIFICATIONS_CHANNEL** - Канал в mattermost / slack для уведомлений.

Типовой вывод принятых настроек в лог контейнера:
--------------------------------------------------

.. code-block::

	17:27:10.INFO  ==> ** Starting Backup plan setup **
	17:27:10.INFO  ==> ** Export to s3 storage disabled **
	17:27:10.INFO  ==> ** Export to local storage disabled **
	17:27:10.INFO  ==> ** Disabled mattermost notification **
	17:27:11.INFO  ==> ** Generation of the configuration file /opt/backup/backup_plan.rb completed successfully **
	17:27:11.INFO  ==> ** Configuration check completed successfully **
	17:27:11.INFO  ==> ** Backup plan setup finished! **

	17:27:11.INFO  ==> ** Сonfiguring the scheduler **
	17:27:11.INFO  ==> ** Schedule applied: 0 0 * * * **

