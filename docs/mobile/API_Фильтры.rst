Фильтры
========

По контрагенту
-----------------

* получение списка контрагенттов ``/gateway/api/records/query``

.. code-block::

  {
    query: {
      sourceId: 'counterparty',
      query: {
        allAvailableCounterparties: true,
      },
      page: {
        skipCount: 0,
        maxItems: 10,
      },
    },
    attributes: {
      disp: '.disp',
    }
  }

По типу документа
-----------------

* получение списка типов ``/gateway/api/records/query``

.. code-block::

  {
    records: [
      "emodel/type@case"
    ],
    attributes: {
      types: "children[]{id:?id,name}"
    },
  }

По приоритету
-----------------

список приоритетов src/model/enums/task-priority.ts TaskPriority

Применение фильтра
-------------------

Выбранные фильтры добавляются в запрос списка 
:doc: `API_Получение списка задач`

.. code-block::

  {
    query: {
      "docEcosTypes":["emodel/type@idocs-doc"],
      "counterparties":["alfresco/counterparty@workspace://SpacesStore/5901e71d-bb0a-49d1-9d1a-a93a5ade198f"]},
  }
