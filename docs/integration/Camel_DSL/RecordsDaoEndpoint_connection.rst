Подключение RecordsDaoEndpoint
================================

Для записи данных в RecordsDao в содержании контекста Camel DSL нужно описать ``RecordsDaoEndpoint``. Для этого до маршрутов описывается секция **beans**. Например: 

.. code-block:: yaml

    - beans:
        - name: "recordsDaoEndpoint"
          type: ru.citeck.ecos.integrations.domain.cameldsl.service.RecordsDaoEndpoint
          properties:
            sourceId: testDao
            pkProp: id
            columnMap:
            name: content
            state: currentState
            type: type
            valueConvertMap: |
              {"type": {"*": "YAML"}, "state": {"1":"STARTED", "*": "STOPPED"}}
    - route:
        from:
          uri: "timer:start?delay=-1&repeatCount=1"
          steps:
            - setBody:
                constant: "select * from actions"
            - to: "jdbc:datasource"
            - split:
                simple: "${body}"
                steps:
                  - to: "bean:recordsDaoEndpoint"       

Где 

    * **recordsDaoEndpoint** – имя ``RecordsDaoEndpoint``, при его использовании в маршруте нужно добавлять префикс **«bean:»**;
    * **type** – класс бина, всегда указывается **ru.citeck.ecos.integrations.domain.cameldsl.service.RecordsDaoEndpoint**
    * в секции **properties** описываются настройки ``RecordsDaoEndpoint``:

      * **appName** - целевой идентификатор приложения
      * **sourceId** - целевой идентификатор источника данных, куда будут помещаться данные. Обязательное свойство;
      * **pkProp** – атрибут исходного источника, который является первичным ключом;
      * **columnMap** – соответствие атрибутов исходного источника и атрибутов назначения. В приведенном примере значение атрибута **name** из источника будет перекладываться в атрибут **content** назначения, **state** в **currentState**, **type** в **type**. Общий вид карты:

        .. code-block:: text

            sourcePropName1: targetPropName1
            sourcePropName2: targetPropName2
            …
            sourcePropNameN: targetPropNameN
            чтоБерем: кудаКладем

    * **valueConvertMap** – карта преобразований исходных значений перед записью их в БД назначения. Карта пишется в формате JSON, символ **'*'** означает любое значение атрибута. В приведенном примере перед записью в атрибут **currentState** значение поля **state** будет заменено на **STARTED**, если оно равно **1**, и на **STOPPED** во всех других случаях. Таким образом, атрибут **currentState** в результирующей таблице будет содержать только два значения: **STARTED** или **STOPPED**. Общий вид карты:
    
  .. code-block:: text

      {“sourcePropName1”: 
      {“value1”:”resultValue1”,
          “value2”:”resultValue2”,
          … 
          “valueN”:”resultValueN”},
      “sourcePropName2”: 
      {“value21”:”resultValue21”,
          “value22”:”resultValue22”,
          … 
          “value2N”:”resultValue2N”},
      …
      “sourcePropNameM”: 
      {“valueM1”:”resultValueM1”,
          “valueM2”:”resultValueM2”,
          … 
          “valueMN”:”resultValueMN”}}

Так как **valueConvertMap** многострочное свойство, то перед значением необходимо указать символ **«|»**.

В одном контексте может быть описано несколько ``RecordsDaoEndpoint``.

.. code-block:: yaml

   - beans:
     - name: "recordsTestDaoEndpoint"
       type: ru.citeck.ecos.integrations.domain.cameldsl.service.RecordsDaoEndpoint
       properties:
         sourceId: recordsTestDao
         pkProp: id
     - name: "testDaoEndpoint"
       type: ru.citeck.ecos.integrations.domain.cameldsl.service.RecordsDaoEndpoint
       properties:
         sourceId: testDao
         pkProp: id
         columnMap:
         name: content
         state: currentState
         type: type
         valueConvertMap: |
           {"type": {"*": "YAML"}}
     - name: "…"
       …

``RecordsDaoEndpoint`` также может обрабатывать данные полученные из XML-файла, CSV-файла или текстового файла, содержащего строковые представления **Map**.

Пример контекста, содержащего маршруты для обработки ``RecordsDaoEndpoint`` данных из файлов:

.. code-block:: yaml

  - beans:
      - name: "recordsDaoEndpoint"
        type: ru.citeck.ecos.integrations.domain.cameldsl.service.RecordsDaoEndpoint
        properties:
          sourceId: testDao
          pkProp: id
          columnMap:
            name: content
            state: currentState
          delimiter: ","
  - route:
      id: "fromXmlFileToDb"
      from:
        uri: "direct:fromXmlFileToDb"
        steps:
          - split:
              xpath: "//someObject"
              steps:
                - to: "bean:recordsDaoEndpoint"
  - route:
      id: "fromTxtFileToDb"
      from:
        uri: "direct:fromTxtFileToDb"
        steps:
          - split:
              tokenize: "\n"
              steps:
                - to: "bean:recordsDaoEndpoint"

Маршрут **fromXmlFileToDb** делит входной XML-поток из файла на элементы **someObject** и передает их в ``RecordsDaoEndpoint``.

Пример входного XML-файла:

.. code-block:: xml

 <?xml version="1.0" encoding="UTF-8"?>
  <massages>
    <someObject id="50" usage ="Additional">
      <name>Test route name James</name>
      <purpose>Test endpoint</purpose>        
    </someObject>
    <someObject id="210" usage ="Standard">
      <name>Route 61</name>
      <purpose>Test</purpose>
      <city>Moscow</city>
    </someObject>
  </massages>

В приведенном примере для установки значений доступны атрибуты записи **id**, **usage**, **name** и **purpose**.

Маршрут **fromTxtFileToDb** делит входной текстовый поток из файла на строки. Пример CSV-файла:

.. code-block::

  id,name,value
  10,SomeName,
  908,- route:,additional
  77,,

Пример файла со строковыми представлениями Map:

.. code-block::

  id=15, name=Test
  id=64, name=Route, value=null
  id=48, name=Open route, value=null

Для работы со строковыми данными используются настройки ``RecordsDaoEndpoint`` **delimiter** и **keyValueSeparator**. 

  * **delimiter** – определяет строку-разделитель значений в строке для CSV-файла и пар ключ-значение для строкового представления Map, по умолчанию значение **«,»**
  * **keyValueSeparator** – определяет строку-разделитель ключа и значения в строковом представлении Map, по умолчанию значение **«=»**