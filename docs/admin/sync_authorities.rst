Синхронизация Authorities
=========================

Синхронизация Пользователей или Групп с ECOS

.. contents::

Синхронизация выполняется на стороне микросрвиса ecos-model. |br|
Настройка осуществляется через журнал *Модель -> Синхронизация* или деплой соответствующего артифакта ``authorities-sync``.

Общие атрибуты
--------------

.. code-block:: json

    {
        "id": "emodel-ldap-person-sync",
        "name": {
            "ru": "Пользователи из LDAP",
            "en": "Persons from LDAP"
        },
        "type": "emodel-ldap",
        "repeatDelayDuration": "PT10S",
        "enabled": true,
        "config": {},
        "version": 1,
        "authorityType": "PERSON",
        "manageNewAuthorities": true
    }


.. list-table:: Описание общих атрибутов
      :widths: 5 10
      :header-rows: 1
      :class: tight-table

      * - Атрибут
        - Описание
      * - id
        - Идентификатор синхронизации
      * - name
        - Название синхронизации
      * - type
        - Тип синхронизации. См. :ref:`Типы синхронизации <sync-auth-types>`
      * - repeatDelayDuration
        - Периодичность синхронизации (PT10S - каждые 10 секунд)
      * - enabled
        - Включена ли синхронизация
      * - config
        - Конфигурация синхронизации специфичная для каждого типа синхронизации
      * - version
        - Версия синхронизации. При изменении конфигурации синхронизации, необходимо увеличить версию
      * - authorityType
        - Тип синхронизируемых объектов, возможные значения - PERSON, GROUP
      * - manageNewAuthorities
        - TODO: fill @pavel.simonov

.. _sync-auth-types:

Типы синхронизаций
------------------

Синхронизация пользователей из Alfresco
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Тип: ``alfresco``

Пример конфигурации:

.. code-block:: json

    {
        "id": "alfresco-persons-sync",
        "name": {
            "ru": "Пользователи из Alfresco",
            "en": "Persons from Alfresco"
        },
        "type": "alfresco",
        "repeatDelayDuration": "PT10S",
        "enabled": true,
        "config": {
            "batchSize": 30,
            "attributes": {
                "firstName": "cm:firstName",
                "middleName": "cm:middleName",
                "personDisabled": "ecos:isPersonDisabled",
                "photoCacheKey": "ecos:photo.contentUrl|presuf(\"v2-\")",
                "workingCalendar": "org:workingCalendar?id"
            }
        },
        "version": 1,
        "authorityType": "PERSON",
        "manageNewAuthorities": true
    }

.. list-table:: Описание атрибутов конфигурации синхронизации пользователей из Alfresco
      :widths: 5 10
      :header-rows: 1
      :class: tight-table

      * - Атрибут
        - Описание
      * - batchSize
        - Размер пакета для синхронизации
      * - attributes
        - Список атрибутов для синхронизации. Ключ - имя атрибута в Ecos, значение - атрибут в Alfresco

Синхронизация групп из Alfresco
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Тип: ``alfresco``

Пример конфигурации:

.. code-block:: json

    {
        "id": "alfresco-groups-sync",
        "name": {
            "ru": "Группы из Alfresco",
            "en": "Groups from Alfresco"
        },
        "type": "alfresco",
        "repeatDelayDuration": "PT10S",
        "enabled": true,
        "config": {
            "batchSize": 30,
            "attributes": {
                "name": "cm:authorityDisplayName",
                "roleType": "org:roleType",
                "branchType": "org:branchType",
                "roleSubType": "org:roleTypeAssoc.cm:name",
                "branchSubType": "org:branchTypeAssoc.cm:name",
                "roleIsManager": "org:roleTypeAssoc.org:roleIsManager?bool",
                "authorityGroups": "assoc_src_cm:member[].cm:authorityName|rxg(\"GROUP_(.+)\")|presuf(\"emodel/authority-group@\")"
            }
        },
        "version": 3,
        "authorityType": "GROUP",
        "manageNewAuthorities": true
    }

.. list-table:: Описание атрибутов конфигурации синхронизации групп из Alfresco
      :widths: 5 10
      :header-rows: 1
      :class: tight-table

      * - Атрибут
        - Описание
      * - batchSize
        - Размер пакета для синхронизации
      * - attributes
        - Список атрибутов для синхронизации. Ключ - имя атрибута в Ecos, значение - атрибут в Alfresco

Синхронизация пользователей из LDAP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Тип: ``emodel-ldap``

.. note::

    Доступно только в Ecos Enterprise

Подключение к LDAP осуществляется через Spring LDAP. |br|
Вы можете создать несколько конфигураций синхронизации, указав различные настройки - например, сервера, домены, фильтры и т.д.

Пример конфигурации:

.. code-block:: json

    {
        "id": "emodel-ldap-person-sync",
        "name": {
            "ru": "Пользователи из LDAP",
            "en": "Persons from LDAP"
        },
        "type": "emodel-ldap",
        "repeatDelayDuration": "PT5M",
        "enabled": true,
        "config": {
                "batchSize": 100,
                "usernameAttributeName": "uid",
                "modifyTimestampAttName": "modifyTimestamp",
                "modifyTimestampFormat": "yyyyMMddHHmmss'Z'",
                "attributes": {
                    "email": "mail",
                    "lastName": "sn",
                    "firstName": "givenname"
                },
                "ldapSearch": {
                    "filter": "(objectClass=person)"
                },
                "differential": true,
                "ldapConnection": {
                    "base": "dc=example,dc=org",
                    "urls": [
                        "ldap://localhost:389"
                    ],
                    "credentials": "ldap-cred"
                }
        },
        "version": 1,
        "authorityType": "PERSON",
        "manageNewAuthorities": true
    }


.. list-table:: Описание атрибутов конфигурации синхронизации пользователей из LDAP
      :widths: 5 10
      :header-rows: 1
      :class: tight-table

      * - Атрибут
        - Описание
      * - batchSize
        - Размер пакета для синхронизации
      * - usernameAttributeName
        - Атрибут LDAP, содержащий имя пользователя (username), должно быть уникальным в системе. По умолчанию - ``uid``
      * - modifyTimestampAttName
        - Атрибут LDAP, содержащий время последнего изменения пользователя, необходим для дифференциальной синхронизации.  По умолчанию - ``modifyTimestamp``
      * - modifyTimestampFormat
        - Формат времени последнего изменения пользователя в LDAP (значения атрибута ``modifyTimestampAttName``). По умолчанию - ``yyyyMMddHHmmss'Z'``
      * - attributes
        - Список атрибутов для синхронизации. Ключ - имя атрибута в Ecos, значение - атрибут в LDAP
      * - differential
        - Флаг, указывающий на необходимость синхронизации только измененных пользователей
      * - ldapSearch
        - | Параметры поиска
  
            * base - базовый DN для поиска
            * filer - фильтр для поиска
            * scope - область поиска. Допустимые значения: ``BASE``, ``ONE_LEVEL``, ``SUBTREE``
  
      * - ldapConnection
        - | Параметры подключения к LDAP серверу
          
            * base - базовый DN подключения
            * urls - список URL серверов
            * credentials - идентификатор credentials для подключения к LDAP серверу (сейчас это credentials из мкр. ecos-integrations)

.. note:: 

    Если включена дифференциальная синхронизация и была изменена конфигурация с повышением версии, то первая синхронизация после изменения будет полной.

.. |br| raw:: html

     <br>   
