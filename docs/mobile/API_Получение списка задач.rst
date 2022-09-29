Получение списка задач
=======================

* выполнить запрос ``/gateway/api/records/query``

.. code-block::

  {
    query: {
    sourceId: 'wftask',
    query: {
        actor: '$CURRENT',
        active: true,
    },
    page: {
        skipCount,
        maxItems,
    },
    sortBy: [
        {
        attribute: 'cm:created',
        ascending: false,
        },
    ],
    },
    attributes: {
    documentStatusTitle: 'docStatusTitle',
    documentStatus: 'docStatus',
    docType: 'docType',
    person: 'cwf_senderName',
    actors: 'actors?json',
    formKey: '_formKey_mobile[]',
    documentDisplayName: 'docDisplayName',
    documentSum: 'docSum',
    docUuid: '_ECM_sys:node-uuid',
    priority: 'bpm_priority',
    description: 'workflow',
    dueDate: 'bpm_dueDate',
    comment: 'lastcomment',
    counterparty: 'counterparty',
    docEcosType: 'docEcosType',
    etype: 'document._etype?id',
    documentId: 'document?id',
    workflowId: 'workflow?id',
    },
  }

.. note::
 Для получения списка Завершенных задач изменить аттрибут ``active: false``

* отфильтровать записи по ранее полученным
* перебрать все элементы ``resp.records``, получить ключи форм ``attributes.formKey``
* выполнить запрос ``/gateway/api/records/query``, получить настройки форм

.. code-block::

  {
    query: {
        query: {
        formKeys,
        },
        sourceId: 'uiserv/rform',
    },
    attributes: {
        definition: 'definition?json',
        i18n: 'i18n?json',
        formKey: 'formKey',
    },
  }

* полученные формы передать в функцию ``parseForm``
* получить данные для всех форм ``/gateway/api/records/query``

.. code-block::

  {
    records: formIds,
    attributes: attribute,
  }

* сопоставить задачи, полученные на первом шаге, и данные для форм
