.. _mobile-api-filters:

Фильтры
==============

.. _mobile-api-filters-counterparty:

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

.. _mobile-api-filters-doc-type:

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

.. _mobile-api-filters-priority:

По приоритету
--------------------------

Список приоритетов ``src/model/enums/task-priority.ts TaskPriority``

.. _mobile-api-filters-apply:

Применение фильтра
------------------------------------

Выбранные фильтры добавляются в запрос списка. См. :ref:`mobile-api-task-list`

.. code-block:: javascript

  {
    query: {
      "docEcosTypes": ["emodel/type@idocs-doc"],
      "counterparties": ["alfresco/counterparty@workspace://SpacesStore/5901e71d-bb0a-49d1-9d1a-a93a5ade198f"],
    },
  }
