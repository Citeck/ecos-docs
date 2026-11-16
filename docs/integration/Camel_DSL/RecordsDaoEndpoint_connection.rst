.. _camel_dsl_records_dao_endpoint:

Подключение RecordsDaoEndpoint
==========================================

.. contents::
   :depth: 2

Для записи данных в RecordsDao в содержании контекста Camel DSL нужно описать ``RecordsDaoEndpoint``. Для этого до маршрутов описывается секция **beans**.

.. warning::

   При ошибке вызова Records API этот бин пишет сообщение ``Failed to mutate record`` в лог и не передает исключение дальше. Успешное завершение шага ``bean:`` не гарантирует, что запись сохранена. Не удаляйте исходные данные на основании одного лишь завершения этого шага.

   Для новых маршрутов, которым требуется получить ошибку сохранения и ссылки на сохраненные записи, используйте :ref:`ecos-records-mutate <EcosRecordsMutateEndpoint>`.

Бин рассчитан на вызов внутри ``split``: он использует индекс элемента ``CamelSplitIndex``. Для строковых данных элемент с индексом 0 используется как строка заголовков, если данные не представлены парами ключ-значение.

Настройка бина
------------------

Пример:

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
    * **type** – класс бина, всегда указывается **ru.citeck.ecos.integrations.domain.cameldsl.service.RecordsDaoEndpoint**;
    * в секции **properties** описываются настройки ``RecordsDaoEndpoint``:

.. list-table::
   :widths: 20 80
   :header-rows: 1
   :class: tight-table

   * - Свойство
     - Описание
   * - appName
     - Целевой идентификатор приложения
   * - sourceId
     - Целевой идентификатор источника данных, куда будут помещаться данные. Обязательное свойство
   * - pkProp
     - Атрибут исходных данных, значение которого передается целевой записи как атрибут id. Поведение создания или обновления определяется целевым Records DAO

columnMap
~~~~~~~~~~~~~~~~~~

**columnMap** – соответствие атрибутов исходного источника и атрибутов назначения. В приведенном примере значение атрибута **name** из источника будет перекладываться в атрибут **content** назначения, **state** в **currentState**, **type** в **type**. Общий вид карты:

.. code-block:: text

    sourcePropName1: targetPropName1
    sourcePropName2: targetPropName2
    …
    sourcePropNameN: targetPropNameN
    чтоБерем: кудаКладем

valueConvertMap
~~~~~~~~~~~~~~~~~~

**valueConvertMap** – карта преобразований исходных значений перед записью их в БД назначения. Карта пишется в формате JSON, символ **'*'** означает любое значение атрибута. В приведенном примере перед записью в атрибут **currentState** значение поля **state** будет заменено на **STARTED**, если оно равно **1**, и на **STOPPED** во всех других случаях. Таким образом, атрибут **currentState** в результирующей таблице будет содержать только два значения: **STARTED** или **STOPPED**. Общий вид карты:

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

В примере **valueConvertMap** задан строкой JSON через многострочный скаляр **«|»**. Однострочный JSON также можно передать строкой в кавычках.

Несколько RecordsDaoEndpoint в одном контексте
--------------------------------------------------

В одном контексте может быть описано несколько ``RecordsDaoEndpoint``.

.. code-block:: yaml

   - beans:
     - name: "recordsTestDaoEndpoint"
       type: ru.citeck.ecos.integrations.domain.cameldsl.service.RecordsDaoEndpoint
       properties:
         sourceId: recordsTestDao
         pkProp: id
         columnMap:
           name: name
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

Обработка данных из файлов
--------------------------------

``RecordsDaoEndpoint`` также может обрабатывать данные полученные из XML-файла, CSV-файла или текстового файла, содержащего строковые представления **Map**.

.. warning::

   Строковый разбор в этом бине использует простой разделитель и пропускает пустые поля. Он не учитывает CSV-кавычки и разделители внутри поля; пустое поле в середине строки может сдвинуть значения относительно заголовков. Применяйте этот способ только к простым строкам без таких конструкций.

   Для CSV с пустыми полями и кавычками используйте :ref:`CsvToListOfDataProcessor` и затем :ref:`ecos-records-mutate <EcosRecordsMutateEndpoint>`. CSV-процессор использует Apache Commons CSV и обрезает пробелы по краям значений и заголовков.

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
  <messages>
    <someObject id="50" usage ="Additional">
      <name>Test route name James</name>
      <purpose>Test endpoint</purpose>
    </someObject>
    <someObject id="210" usage ="Standard">
      <name>Route 61</name>
      <purpose>Test</purpose>
      <city>Moscow</city>
    </someObject>
  </messages>

В приведенном примере для установки значений доступны атрибуты записи **id**, **usage**, **name** и **purpose**.

Маршрут **fromTxtFileToDb** делит входной текстовый поток из файла на строки. Пример CSV-файла:

.. code-block:: text

  id,name,value
  10,SomeName,
  908,- route:,additional
  77,,

Пример файла со строковыми представлениями Map:

.. code-block:: text

  id=15, name=Test
  id=64, name=Route, value=null
  id=48, name=Open route, value=null

Для работы со строковыми данными используются настройки ``RecordsDaoEndpoint`` **delimiter** и **keyValueSeparator**.

.. list-table::
   :widths: 20 80
   :header-rows: 1
   :class: tight-table

   * - Свойство
     - Описание
   * - delimiter
     - Определяет строку-разделитель значений в строке для CSV-файла и пар ключ-значение для строкового представления Map, по умолчанию значение **«,»**
   * - keyValueSeparator
     - Определяет строку-разделитель ключа и значения в строковом представлении Map, по умолчанию значение **«=»**
