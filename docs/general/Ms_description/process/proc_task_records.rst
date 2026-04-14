.. _proc_task_records:

Querying Process Tasks via Records API (eproc/proc-task)
=========================================================

The ``eproc/proc-task`` Records source exposes active BPMN process tasks managed by
``ecos-process``. It allows any Records API consumer — browser, backend service, or journal —
to search and filter tasks using the standard :ref:`predicate language <ecos-predicate_main>`.

Source ID
---------

.. code-block::

    eproc/proc-task

Supported Filter Attributes
----------------------------

The following attributes can be used in predicates when querying ``eproc/proc-task``:

.. list-table::
   :widths: 30 70
   :header-rows: 1
   :class: tight-table

   * - Attribute
     - Description
   * - ``documentRef``
     - EntityRef of the document the task is linked to (e.g. ``emodel/contract@<id>``)
   * - ``documentTypeRef``
     - EntityRef of the **type** of the associated document (e.g. ``emodel/type@contract``).
       Use this to retrieve all tasks across documents of the same type.
   * - ``assignee``
     - Username of the task assignee
   * - ``actors``
     - All task actors: both candidates and the assigned user
   * - ``processInstanceId``
     - Internal Camunda process instance ID
   * - ``processDefRef``
     - EntityRef of the process definition

Filtering by documentTypeRef
-----------------------------

The ``documentTypeRef`` attribute lets you retrieve tasks for all documents that belong to a
specific type. This is useful for building type-scoped task lists or dashboards.

.. important::

    Prior to the fix released on 2026-04-14, a ``documentTypeRef`` predicate in an
    ``eproc/proc-task`` query was silently ignored — tasks were returned regardless of document
    type. The predicate is now applied correctly.

**Example — query all active tasks for a document type (JSON predicate):**

.. code-block:: json

    {
      "sourceId": "eproc/proc-task",
      "query": {
        "t": "eq",
        "att": "documentTypeRef",
        "val": "emodel/type@contract"
      }
    }

**Example — browser console (JavaScript Records API):**

.. code-block:: javascript

    await Records.query(
        {
            sourceId: 'eproc/proc-task',
            query: {
                t: 'eq',
                att: 'documentTypeRef',
                val: 'emodel/type@contract'
            }
        },
        ['id', 'name', 'assignee', 'documentRef']
    )

**Example — combine documentTypeRef with assignee filter:**

.. code-block:: json

    {
      "sourceId": "eproc/proc-task",
      "query": {
        "t": "and",
        "val": [
          {
            "t": "eq",
            "att": "documentTypeRef",
            "val": "emodel/type@contract"
          },
          {
            "t": "eq",
            "att": "assignee",
            "val": "john.doe"
          }
        ]
      }
    }

**Example — backend (Kotlin):**

.. code-block:: kotlin

    val tasks = recordsService.query(
        RecordsQuery.create {
            withSourceId("eproc/proc-task")
            withQuery(
                Predicates.and(
                    Predicates.eq("documentTypeRef", "emodel/type@contract"),
                    Predicates.eq("assignee", "john.doe")
                )
            )
        }
    )

See Also
--------

* :ref:`Predicate language <ecos-predicate_main>`
* :ref:`Records API <Records_API>`
* :ref:`Process Engine microservice <process>`
