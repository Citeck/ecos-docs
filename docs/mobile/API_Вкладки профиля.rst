Вкладки профиля
==============================

Получение списка вкладок ``/gateway/api/records/query?k=q_uiserv/dashboard``

.. code-block:: javascript

  {
    query: {
      sourceId: 'uiserv/dashboard',
      query: {
        "typeRef": "emodel/type@person",
        recordRef: username ? `people@${username}` : `people@${state.user.username}`,
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

Из полученных id формируется URL вида ``${server}/v2/dashboard?activeLayoutId=${activeTabId}&recordRef=people@${this.props.user.username}``, который передаётся в WebView.
