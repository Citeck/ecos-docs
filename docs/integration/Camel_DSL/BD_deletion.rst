Удаление данных из БД
=======================

Для удаления данных из БД необходимо создать **Credentials**, **Источник данных** и **Camel DSL** как указано в пункте **«Выборка из БД»**. При этом, содержимое маршрута должно включать в себя SQL-запрос на удаление данных. 

Например, следующий маршрут **clearValues** удаляет все записи из таблицы **simple** источника данных **datasource**, кроме тех у которых атрибут **id** равен **'1'** или **'2'**.

.. code-block:: yaml

  - route:
      id: "clearValues"
      from:
        uri: "timer:start?delay=-1&repeatCount=1"
        steps:
          - setBody:
              constant: "delete from simple where id not in ('1','2')"
          - to: "jdbc:datasource"


Пример контекста, который берет данные из источника данных **todb**, обрабатывает их через R`RecordsDaoEndpoint`` **daoEndpoint**  и очищает таблицу **simple**, из которой взял данные:

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
    Особенности контекста: 
    Содержимое constant переводится в нижний регистр. Например, выборка **"select * from simple order by COMPANY_ID"** приводит к ошибке **ERROR: column "company_id" does not exist**
