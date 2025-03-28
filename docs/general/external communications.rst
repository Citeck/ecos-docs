Настройка внешних коммуникаций для Citeck
==========================================

.. contents::
   :depth: 3

Базовые принципы
------------------

Все коммуникации настраиваются через spring конфигурацию, которая может быть настроена либо через ENV переменные, либо через конфигурационные файлы.

Конфигурационные файлы могут быть в формате либо yaml, либо properties.
Правила для маппинга между ENV переменными и свойствами в конфигурационных файлах:

 1. Разбиваем ключ по ``"."`` (т.е. ``aa.customProp.cc`` => [``'aa'``, ``'customProp'``, ``'cc'``])
 2. Разбиваем каждую часть ключа по словам если находим camelCase ([``'aa'``, ``'customProp'``, ``'cc'``] => [``'aa'``, ``'custom'``, ``'Prop'``, ``'cc'``]) – прим. этот этап опционален и применим только к платформе Citeck. В стандартном spring его нет. 
 3. Переводим все части в UPPER CASE и объединяем через символ ``"_"`` ([``'aa'``, ``'custom'``, ``'Prop'``, ``'cc'``] => ``AA_CUSTOM_PROP_CC``)

ENV переменные имеют наивысший приоритет.

Подробнее про spring конфигурацию можно прочитать в `официальной документации spring boot <https://docs.spring.io/spring-boot/reference/features/external-config.html>`_ 

JWT токен
----------

Все микросервисы при общении между собой используют **jwt токен** для подписывания запросов и валидации входящих запросов. Токен задается свойством

.. code-block::

    ecos.webapp.web.authenticators.jwt.secret

и должен содержать произвольный base64 ключ, который должен совпадать у всех микросервисов.

Подключение к RabbitMQ
------------------------

Каждый микросервис в платформе Citeck требует наличия основного подключения к RabbitMQ и все микросервисы должны быть подключены к одному виртуальному хосту в одном RabbitMQ.

Стандартные настройки ``spring.rabbitmq.*`` в Citeck отключены и вместо них следует использовать настройки ``ecos.webapp.dataSources.main-rabbitmq.*``

.. attention::

    Подключение к RabbitMQ может быть не одно и в этом случае настройки остаются те же самые, но вместо main-rabbitmq будет другой ключ. Подробнее о наличии дополнительных подключений можно прочитать в разделах ниже.

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      :align: center
      :class: tight-table 

      * - Настройка
        - Значение по умолчанию
        - Описание
      * - ecos.webapp.dataSources.main-rabbitmq.host
        - rabbitmq
        - Хост для подключения к rabbitmq
      * - ecos.webapp.dataSources.main-rabbitmq.username
        - admin
        - Имя пользователя для подключения к rabbitmq
      * - ecos.webapp.dataSources.main-rabbitmq.password
        - admin
        - Пароль для подключения к rabbitmq
      * - ecos.webapp.dataSources.main-rabbitmq.virtualHost
        - /
        - Виртуальный хост для подключения к rabbitmq
      * - ecos.webapp.dataSources.main-rabbitmq.executor
        - rabbitmq
        - | Исполнитель задач, который обслуживает подключение к rabbitmq.
          | Эта настройка определяет пул потоков, который будет использован для обработки сообщений.
      * - ecos.webapp.dataSources.main-rabbitmq.port
        - | 5671 если включен tls
          | 5672 если tls выключен
        - Порт для подключения к rabbitmq
      * - ecos.webapp.dataSources.main-rabbitmq.tls.enabled
        - false
        - Включено или нет шифрование
      * - ecos.webapp.dataSources.main-rabbitmq.tls.clientKey
        - null
        - Секретный ключ, который будет использован микросервисом для аутентификации.
      * - ecos.webapp.dataSources.main-rabbitmq.tls.trustedCerts
        - null
        - Список доверенных CA сертификатов
      * - ecos.webapp.dataSources.main-rabbitmq.tls.protocol
        - TLSv1.2
        - TLS протокол
      * - ecos.webapp.dataSources.main-rabbitmq.tls.verifyHostname
        - true
        - Следует или нет проверять имя хоста сервера с значением в сертификате, который он предоставляет.

Особенности микросервиса ecos-process
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

В ecos-process добавлено дополнительное подключение к rabbitmq с ключом bpmn-rabbitmq. Настройки все те же что и для main-rabbitmq, но с поправкой на дефолтные значения:

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :align: center
      :class: tight-table 

      * - Настройка
        - Значение по умолчанию
      * - ecos.webapp.dataSources.bpmn-rabbitmq.host
        - ${ecos.webapp.dataSources.main-rabbitmq.host}
      * - ecos.webapp.dataSources.bpmn-rabbitmq.username
        - ${ecos.webapp.dataSources.main-rabbitmq.username}
      * - ecos.webapp.dataSources.bpmn-rabbitmq.password
        - ${ecos.webapp.dataSources.main-rabbitmq.password}
      * - ecos.webapp.dataSources.bpmn-rabbitmq.executor
        - bpmn-rabbitmq

Подключение к Zookeeper
-------------------------

Каждый микросервис в платформе Citeck требует наличия подключения к общему Zookeeper.

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      :align: center
      :class: tight-table 

      * - Настройка
        - Значение по умолчанию
        - Описание
      * - ecos.webapp.zookeeper.host
        - zookeeper-app
        - Хост для подключения к Zookeeper
      * - ecos.webapp.zookeeper.port	
        - 2181
        - Хост для подключения к Zookeeper

Подключение к БД (JDBC)
------------------------
.. note::

    Стандартные spring настройки spring.datasource.* в Citeck не используются.

Ряд микросервисов требуют наличия двух основных подключений к БД PostgreSQL: 

 * ecos-model
 * ecos-apps
 * ecos-uiserv
 * ecos-history
 * ecos-notifications
 * ecos-integrations

Основные подключения настраиваются через настройки:

.. code-block::

    ecos.webapp.dataSources.main.*
    ecos.webapp.dataSources.main-xa-aware.*

В таблице описание настроек для main датасорса. Для main-xa-aware url, username, password должны быть такими же, а остальные настройки могут быть произвольными, но по умолчанию лучше их сделать такими же как и у main.

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      :align: center
      :class: tight-table 

      * - Настройка
        - Значение по умолчанию
        - Описание
      * - ecos.webapp.dataSources.main.url
        - 
        - JDBC URL для подключения к БД
      * - ecos.webapp.dataSources.main.username
        - 
        - Имя пользователя для подключения
      * - ecos.webapp.dataSources.main.password
        - 
        - Пароль для подключения
      * - ecos.webapp.dataSources.main.maxPoolSize
        - 30
        - Максимальный размер пула подключений
      * - ecos.webapp.dataSources.main.minIdle
        - 0
        - | Устанавливает минимальное количество неактивных соединений в пуле.
          | Пул пытается обеспечить наличие minIdle соединений, когда запускается механизм удаления неактивных объектов.
          | Значение этого свойства не имеет эффекта, если timeBetweenEvictionRunsMillis не имеет положительного значения.
      * - ecos.webapp.dataSources.main.initialSize
        - 0
        - Начальное количество соединений, которые создаются при запуске пула.
      * - ecos.webapp.dataSources.main.timeBetweenEvictionRunsMillis
        - -1
        - | Количество миллисекунд, которое поток, отвечающий за удаление неактивных объектов, будет ждать между запусками.
          | Если значение меньше или равно нулю, этот поток не будет запускаться.

Особенности ecos-process
~~~~~~~~~~~~~~~~~~~~~~~~~~

В ecos-process основной датасорс отсутствует, но есть два других - eproc и camunda. Они настраиваются так же как и main, но с префиксами ``ecos.webapp.dataSources.eproc.*`` и ``ecos.webapp.dataSources.camunda.*`` соответственно.

В таблице представлены значения по умолчанию, которые отличны от основных:

.. list-table::
      :widths: 10 10
      :align: center
      :class: tight-table 

      * - ecos.webapp.dataSources.camunda.url
        - jdbc:postgresql://localhost:14523/ecos_camunda
      * - ecos.webapp.dataSources.camunda.username
        - camunda
      * - ecos.webapp.dataSources.camunda.password
        - camundapassword
      * - ecos.webapp.dataSources.eproc.url
        - jdbc:postgresql://localhost:14523/ecos_process
      * - ecos.webapp.dataSources.eproc.username
        - process
      * - ecos.webapp.dataSources.eproc.password
        - processpassword

Подключение к БД (Mongo)
-------------------------

Микросервис ecos-process требует настройку для подключения к БД mongo:

.. list-table::
      :widths: 10 5 10
      :header-rows: 1
      :align: center
      :class: tight-table 

      * - 
        - Значение по умолчанию
        - Описание
      * - spring.data.mongodb.uri
        - mongodb://localhost:27017/eproc
        - | Строка подключения к mongo. Может содержать логин и пароль. Общий вид:
          | ``mongodb://{user}:{password}@{host}:{port}/{dbname}``

Cloud config
-------------

Начиная с версии 2024.8 наличие ecos-registry стало опциональным т.к. service registry был переделан на использование Zookeeper.

Единственный функционал, который остался в ecos-registry - это cloud config, который можно выключить через переменную ``SPRING_CONFIG_IMPORT``: и доставлять конфигурацию инфраструктурными средствами.

:ref:`Подробнее про ключевые изменения в релизе 2024.8<breaking_changes_2024.8>`