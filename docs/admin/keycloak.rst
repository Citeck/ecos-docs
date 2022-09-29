ECOS KeyCloak Extensions
=========================

Расширения KeyCloak со стороны ECOS: `<https://gitlab.citeck.ru/citeck-projects/ecos-keycloak-ext>`_ 

Возможности расширения
-----------------------

1. Кидание событий ECOS при возникновении пользовательских и админских событий Keycloak (например, при логине или логауте пользователя).

2. Если включен флаг  ``ECOS_KK_LISTEN_PERSON_DISABLED_STATUS``, то при отключении пользователя в ecos-model он так же отключается и в Keycloak. Работает только если в KeyCloak нет синхронизации пользователей из LDAP.

При создании новых пользователей в KeyCloak они так же создаются и в ECOS.

Подключение плагина
--------------------

Подключается плагин добавлением volume к контейнеру с Keycloak: 
::

  volumes:   
    - ./volumes/dir_with_jar_file:/opt/jboss/keycloak/standalone/deployments/ecos

Плагин можно скачать `отсюда <https://jenkins.citeck.ru/job/ecos-keycloak-ext/job/master/>`_

Активация плагина
------------------

Активировать плагин можно в админке клока для нужного реалма:

 .. image:: _static/keycloack_config.png
       :width: 600
       :align: center
       :alt: Колонки

**ENV Конфигурация**

``ECOS_KK_RMQ_HOST=rabbitmq-dev`` - хост для подключения к rabbitmq

``ECOS_KK_RMQ_USERNAME=admin`` - пользователь для подключения к rabbitmq

``ECOS_KK_RMQ_PASSWORD=admin`` - пароль для подключения к rabbitmq

``ECOS_KK_ZK_HOST=zookeeper-app`` - хост для подключения к zookeeper

``ECOS_KK_LISTEN_PERSON_DISABLED_STATUS={{EcosIdentityApp.ecosExtensions.listenPersonDisabledStatus}}``

Для доставки на стенды сформирован docker образ:

.. code-block::

  ecos-keycloak-ext:
	image: nexus.citeck.ru/ecos-keycloak-ext:12.0.1.2
	container_name: ecos-keycloak-ext
	hostname: ecos-keycloak-ext
	environment:
		- KK_EXT_TARGET_ROOT=/run/extensions-target
	volumes:
		- ./kk-ecos-extensions:/run/extensions-target

``KK_EXT_TARGET_ROOT`` - это папка, в которую будет скопирована Jar'ка расширения