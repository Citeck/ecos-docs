Создание новых источников записей через Web интерфейс
======================================================

В микросервисе интеграций есть возможность создавать новые источники записей через Web интерфейс. Для этого предусмотрен системный журнал Records Sources.

Поле Json response transform specification описывается в формате `jolt transform <https://jolt-demo.appspot.com>`_  

Инструкция для мапинга REST запроса у одного из заказчиков:

.. code-block::

    1. Зайти в системные журналы в старом интерфейсе
    2. Открыть журнал Data Sources
    3. Нажать "Создать", выбрать REST Data Source
    4. Заполнить поля:
    Id: cities_source
    Name: Cities source
    URL: http://alfresco/share/page/proxy/alfresco/sem/api/v1/city/search?key={key}
    Json response transform specification:
    [
    {
        "operation": "shift",
        "spec": {
        "*": {
            "dataBusId": "[&1].id",
            "name": "[&1].name",
            "district": "[&1].state",
            "country": "[&1].country"
        }
        }
    }
    ]
    Internal: Да
    5. Нажать Submit
    6. Перейти в журнал статусов кейса (нужно чтобы сбросился текущий журнал)
    7. Перейти в журнал Records Sources
    8. Нажать "Создать" и выбрать RecordsSource
    9. Ввести данные:
    Id: cities
    Name: Cities Records
    Query Data Source: выбрать Data Source, который мы создали ранее
    Query params:
    key - {name:}

    10.  Нажать Submit

.. list-table:: 
      :widths: 20 20

      * - | 
  
             .. image:: _static/records_sources/records_sources_1.png
                  :width: 600   

        - | 

             .. image:: _static/records_sources/records_sources_2.png
                  :width: 600   

Автозаполнение контрагента
---------------------------

В ent-core 3.32.0 был добавлен **Record Source**? использующийся для автозаполнение контрагентов по ИНН при нажатии на кнопку.

 .. image:: _static/records_sources/records_sources_3.png
     :width: 600  

Для данного Record Source доступны два Data source'а:

* **suggestions-dadata-find-by-id-party** `https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party <https://suggestions.dadata.ru/suggestions/api/4_1/rs/findById/party>`_ 

    Для получение информации Dadata. Подробнее  `https://dadata.ru/api/find-party <https://dadata.ru/api/find-party/>`_

    Этот вариант получения данных включен по умолчанию.

* **focus-api-kontur-ru-api3-req** `https://focus-api.kontur.ru/api3/req <https://focus-api.kontur.ru/api3/req>`_ 

    Для получения информации из Контура. Подробнее `https://focus-api.kontur.ru/api3/req/userform <https://focus-api.kontur.ru/api3/req/userform>`_

    Для смены источника данных достаточно поменять поля **Query Data Source** и **Query params → token**

    Для смены параметров на стендах необходимо использовать патч `См. Патчи для артефактов <https://citeck.atlassian.net/wiki/spaces/knowledgebase/pages/1482883161>`_

 .. image:: _static/records_sources/records_sources_4.png
     :width: 600  

.. code-block::

    await Citeck.Records.query({
        sourceId: 'integrations/rs_findContractorByInn',
        query: {
            inn: '7707083893'
        }
    }, '.json')