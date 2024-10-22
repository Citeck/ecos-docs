Компоненты
============

**Компоненты** используются для подключения маршрутов к внешним системам и сервисам.

Подробнее - https://camel.apache.org/manual/component.html 

EcosRecordsSync camel component
-------------------------------------

**EcosRecordsSyncComponent** - компонент camel, созданный для перебора/обновления записей через RecordsAPI. Ключ для использования компонента в camel-контексте: *ecos-records-sync*

Компонент включает в себя как потребителя *EcosRecordsSyncConsumer*, так и производителя EcosRecordsSyncProducer по терминологии camel

Ниже будут примеры регистрации компонента в yaml формате, например, при регистрации через Camel DSL.

1. **EcosRecordsSyncConsumer**. Расширяет стандартный ScheduledBatchPollingConsumer, реализует перебор записей по ECOS типу + sourceId. Возможные настройки для  *ecos-records-sync* консьюмера: 

.. list-table::
      :widths: 5 20
      :header-rows: 1
      :class: tight-table  

      * - Key
        - Value
      * - syncId
        - | уникальное значение в рамках инстанса приложения, на котором запускаются camel контексты. На основе этого значения создается стейт для периодического пуллинга из sourceId 
          | см: journalId=ecos-sync-state
      * - syncMode
        - | DEFAULT | CREATE | UPDATE
          | DEFAULT, UPDATE - перебор записей по дате обновления
          | CREATE - перебор записей по дате создания 
      * - sourceId
        - sourceId типа
      * - typeRef
        - ecos тип
      * - batchSize
        - размер батча при пуллинге 

Пример использования:  

.. code-block::

   - route:
       from:
         uri: ecos-records-sync:testEcosRecordsSync
         parameters:
           delay: 15000
           sourceId: emodel/test-type-mig-from
           typeRef: emodel/type@test-type-mig-from
           batchSize: 5
         steps:
         - to: log:ers-test

2. **EcosRecordsSyncProducer**. Расширяет DefaultProducer, реализует обновление записи через RecordsAPI. Данные для обновления берется из тела сообщения (id из тела из проперти сообщения - CamelEcosRecordsSyncEntityRef). Возможные настройки для  *ecos-records-sync* продюсера: 

.. list-table::
      :widths: 10 20
      :header-rows: 1
      :class: tight-table  

      * - Key
        - Value
      * - syncId
        - любое значение, скорее информационное
      * - sourceId
        - sourceId типа

Пример использования:  

.. code-block::

   - route:
       from:
         uri: .....
         steps:
         - to:
             uri: ecos-records-sync:test-type-mig-to
             parameters:
               sourceId: emodel/test-type-mig-to
