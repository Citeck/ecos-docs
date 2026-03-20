.. _camel-dsl-bd-deletion:

Удаление данных из БД
=======================================

Для удаления данных из БД необходимо создать **Credentials**, **Источник данных** и **Camel DSL** так же, как описано в разделе **«Выборка из БД»**. Содержимое маршрута должно включать SQL-запрос на удаление данных.

Простое удаление записей
--------------------------

Маршрут **clearValues** удаляет все записи из таблицы **simple** источника данных **datasource**, кроме записей с **id** равным **'1'** или **'2'**:

.. code-block:: yaml

  - route:
      id: "clearValues"
      from:
        uri: "timer:start?delay=-1&repeatCount=1"
        steps:
          - setBody:
              constant: "delete from simple where id not in ('1','2')"
          - to: "jdbc:datasource"

Выборка с последующим удалением
---------------------------------

Следующий контекст выбирает данные из источника **todb**, обрабатывает их через ``RecordsDaoEndpoint`` **daoEndpoint**, после чего очищает таблицу **simple**:

.. code-block:: yaml

  - beans:
      - name: "daoEndpoint"
        type: ru.citeck.ecos.integrations.domain.cameldsl.service.RecordsDaoEndpoint
        properties:
          sourceId: testDao
          pkProp: id
          columnMap:
            name: content
            state: currentState
            type: type
  - route:
      id: "getValues"
      from:
        uri: "timer:start?delay=-1&repeatCount=1"
        steps:
          - setBody:
              constant: "select * from simple"
          - to: "jdbc:todb"
          - split:
              simple: "${body}"
              steps:
                - to: "bean:daoEndpoint"
                - to: "direct:clearValues"
  - route:
      id: "clearValues"
      from:
        uri: "direct:clearValues"
        steps:
          - setBody:
              constant: "delete from simple"
          - to: "jdbc:todb"

.. note::

   Значение ``constant`` автоматически приводится к нижнему регистру. Например, запрос ``"select * from simple order by COMPANY_ID"`` вызовет ошибку ``ERROR: column "company_id" does not exist``, так как имя колонки будет преобразовано в нижний регистр.
