CounterpartyEdiInfoRecordsDao
=============================

**appId** - integrations

**sourceId** - counterparty-edi-info

Цель этого **RecordsDAO** - получение информации о контрагенте непосредственно из ЭДО-провайдера.

На момент написания статьи - было возможно получить следующие данные о контрагенте из ЭДО-провайдера:

* **counterpartyName** - название, по которому контрагент зарегистрирован в ЭДО-провайдере.
* **boxId** - Идентификатор ящика контрагента, который участвует как идентификатор данного контрагента в интеграции (при получении документов - определяется контрагент по этому идентификатору, при отправке - определяется куда отправить документ). 
* **nsId** - Идентификатор контрагента в ФНС. Участвует в формализованном документообороте, но хранить его не обязательно, как правило, интеграция подставляет его автоматически.

Данные для запроса могут быть разными, в зависимости от ситуаций и от того, какие параметры известны.

На момент написания статьи, полная структура, которую можно передать в запросе, выглядит следующим образом (обратите пожалуйста внимание на комментарии):

.. code-block::

    private boolean allowMultiple = false; // Разрешать ли получение более 1 записи с информацией о контрагенте. Если true - при нахождении 2 и более, будет ошибка выполнения запроса.
    
    private OurId ourId; // От имени какого ящика системы выполнять поиск информации о контрагенте. Параметр не обязателен, если useAnyBox=true.
    private boolean useAnyBox = false; // Если true - поиск информации о контрагенте будет выполнен от имени любого ящика, который зарегистрирован в системе (регистрация ящиков в системе производится в системном журнале "Конфигурация ящиков ЭДО")
    
    private String operatorId; // Идентификатор оператора ЭДО, в котором будет искаться информация о контрагенте (где 2BM=EdiProviderType.KONTUR, 2BE=EdiProviderType.SBIS и тд, полный список можно посмотреть в ru.citeck.ecos.edi.service.common.operator.OperatorIdConversationServiceImpl)
    private EdiProviderType ediProviderType; // Тип оператора ЭДО, в котором будет искаться информация о контрагенте.
    
    private String inn; // ИНН для поиска в ЭДО-провайдере.
    private String kpp; // КПП для поиска в ЭДО-провейдере (может быть опциональным).

Примеры запросов:

1. Пример запроса в Контур с использованием случайного ящика (указание оператора через operatorId):

**Запрос**

.. code-block::

    {
    "query": {
        "sourceId": "alfresco/counterparty-edi-info",
        "language": "predicate",
        "query": {
        "allowMultiple": false,
        "useAnyBox": true,
        "operatorId": "2BM",
        "inn": "9999999999",
        "kpp": "999999999"
        }
    },
    "attributes": [
        ".json"
    ]
    }

**Ответ**

.. code-block::

    {
    "records": [
        {
        "id": "alfresco/counterparty-edi-info@082e8d0f-93b6-4326-8580-753717af8ab2",
        "attributes": {
            ".json": {
            "counterpartyName": "Тест АО «АО» тестовая",
            "boxId": "0806d6e3-6508-41c7-9038-8c8031df112c",
            "fnsId": "2BM-9649397010-964901000-201512170845396498364"
            }
        }
        }
    ],
    "errors": [],
    "hasMore": false,
    "totalCount": 1
    }

2. Пример запроса в Контур с использованием случайного ящика (указание оператора через EdiProviderType):

**Запрос**

.. code-block::

        {
        "query": {
            "sourceId": "alfresco/counterparty-edi-info",
            "language": "predicate",
            "query": {
            "allowMultiple": false,
            "useAnyBox": true,
            "operatorId": "KONTUR",
            "inn": "9999999999",
            "kpp": "999999999"
            }
        },
        "attributes": [
            ".json"
        ]
        }


**Ответ**

.. code-block::

    {
    "query": {
        "sourceId": "alfresco/counterparty-edi-info",
        "language": "predicate",
        "query": {
        "allowMultiple": false,
        "useAnyBox": true,
        "operatorId": "KONTUR",
        "inn": "9999999999",
        "kpp": "999999999"
        }
    },
    "attributes": [
        ".json"
    ]
    }