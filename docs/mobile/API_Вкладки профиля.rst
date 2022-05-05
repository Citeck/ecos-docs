Вкладки профиля
================

получение списка вкладок ``/gateway/api/records/query?k=q_uiserv/dashboard``

.. code-block::

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

из полученных id формируется url ${server}/v2/dashboard?activeLayoutId= ``${activeTabId}`` &recordRef= ``${`people@${this.props.user.username}`}`` , котрый передается в WebView