Фильтры
==============

По контрагенту
----------------------------

* получение списка контрагентов ``/gateway/api/records/query``

.. code-block:: javascript

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
    },
  }

По типу документа
----------------------------------

* получение списка типов ``/gateway/api/records/query``

.. code-block:: javascript

  {
    records: [
      "emodel/type@case"
    ],
    attributes: {
      types: "children[]{id:?id,name}"
    },
  }

По приоритету
--------------------------

Список приоритетов ``src/model/enums/task-priority.ts TaskPriority``

Применение фильтра
------------------------------------

Выбранные фильтры добавляются в запрос списка. См. :doc:`API_Получение списка задач`

.. code-block:: javascript

  {
    query: {
      "docEcosTypes": ["emodel/type@idocs-doc"],
      "counterparties": ["alfresco/counterparty@workspace://SpacesStore/5901e71d-bb0a-49d1-9d1a-a93a5ade198f"],
    },
  }
