Вкладки задачи
============================

Получение списка вкладок ``/gateway/api/records/query?k=q_uiserv/dashboard``

.. code-block:: javascript

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

Из полученных id формируется URL вида ``${server}/v2/dashboard?activeLayoutId=${activeTabId}&recordRef=${taskUuid}``, который передаётся в WebView.
