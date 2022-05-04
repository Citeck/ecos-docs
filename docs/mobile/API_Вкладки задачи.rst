Вкладки задачи
================

получение списка вкладок ``/gateway/api/records/query?k=q_uiserv/dashboard``

.. code-block::

  {
    query: {
      sourceId: 'uiserv/dashboard',
      query: {
        typeRef,
        user: state.user.username,
        authority: state.user.username,
      },
      page: {
        maxItems: 1,
      },
    },
    attributes: {
      config: 'config?json',
    },
  }

из полученных id формируется url ${server}/v2/dashboard?activeLayoutId= ``${activeTabId}`` &recordRef= ``${taskUuid}`` , котрый передается в WebView