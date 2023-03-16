Скриптовая задача
=================
.. _script_task:

.. contents::

Атрибуты и форма
----------------

Используется язык JavaScript.

 .. image:: _static/59.png
       :width: 300
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/60.png
                :width: 300
                :align: center
      * - Указать **скрипт** 
        - 
               .. image:: _static/61.png
                :width: 300
                :align: center
      * - Настройки асинхронности, см. подробнее о `асинхронных задачах <https://camunda.com/blog/2014/07/advanced-asynchronous-continuations/>`_ 
        - 
               .. image:: _static/62.png
                :width: 300
                :align: center

Доступные переменные
--------------------

Переменные процесса
~~~~~~~~~~~~~~~~~~~

Во время выполнения скриптов доступны все переменные процесса, видимые в текущей области.

.. code-block:: javascript

    //someVar - переменная процесса
    print("someVar: " + someVar);


Execution
~~~~~~~~~

.. _execution:

``execution`` - переменная, которая всегда доступна, если скрипт выполняется в области выполнения (например, в Script Task). `(DelegateExecution) <https://docs.camunda.org/javadoc/camunda-bpm-platform/7.17/org/camunda/bpm/engine/delegate/DelegateExecution.html>`_

.. code-block:: javascript

    // получение переменной процесса
    var sum = execution.getVariable('x');

    // установление переменной процесса
    execution.setVariable('y', x + 15);

Document
~~~~~~~~

``document`` - является скриптовым представлением документа `AttValueScriptCtx <https://gitlab.citeck.ru/ecos-community/ecos-records/-/blob/master/ecos-records/src/main/java/ru/citeck/ecos/records3/record/atts/computed/script/AttValueScriptCtx.kt>`_ , по которому идет БП.

.. code-block:: javascript

    //получение атрибута документа
    var created = document.load("_created");

    //установление атрибуту документа указанного значения
    document.att("firArchiveBoxNumber", 123);
    //сохранение
    document.save();

    //сброс состояния документа, если ранее были внесены изменения через att()
    document.att("firArchiveBoxNumber", 123);
    document.reset();

Records
~~~~~~~

``Records`` - это сервис, который предоставляет доступ к функциям работы с рекордами `RecordsScriptService <https://gitlab.citeck.ru/ecos-community/ecos-records/-/blob/master/ecos-records/src/main/java/ru/citeck/ecos/records3/record/atts/computed/script/RecordsScriptService.kt>`_.

.. code-block:: javascript

    //Получение скриптового представление указанного рекорда
    var doc = Records.get("emodel/doc@111");

    //Query рекордов
    var queryCommentsResult = Records.query({
        sourceId: "emodel/comment",
        language: "predicate",
        query: {
            a: "record",
            t: "eq",
            v: "emodel/doc@123"
        }
    }, {
        text: "text",
        created: "_created"
    });

    var firstComment = queryCommentsResult.records[0];
    var text = firstComment.text;
    var created = firstComment.created;

    print("comment: " + text + " created on " + created);

Ecos Config
~~~~~~~~~~~

``Config`` - предоставляет доступ к Конфигурации Ecos по ключу в формате ``<область>$<идентификатор>``.

    - ``get(key: String): DataValue`` - получение значения по ключу
    - ``getOrDefault(key: String, defaultValue: Any): DataValue`` - получение значения по ключу, если значение не найдено, то возвращается значение по умолчанию
    - ``getNotNull(key: String): DataValue`` - получение значения по ключу, если значение null, то выбрасывается исключение

.. code-block:: javascript

    //получение значения конфигурации по ключу и приведение к типу String
    var serviceDeskEmailFrom = Config.get("app/service-desk$send-sd-email-from").asText()

DataValue
~~~~~~~~~

``DataValue`` - объект, позволяющий сконвертировать данные в стркутуру `BpmnDataValue <https://gitlab.citeck.ru/ecos-community/ecos-process/-/blob/develop/src/main/java/ru/citeck/ecos/process/domain/bpmn/engine/camunda/impl/variables/convert/BpmnDataValue.kt>`_ для удобной работы с json представлением, это позволяет безопасно обращаться к полям, получать значения по умолчанию, приводить к нужному типу, сохранять данные в execution и многое другое, подробнее см. методы класса.

    - ``DataValue.of(content: Any?)`` - создает объект DataValue из любого объекта, если объект не может быть сконвертирован в DataValue, то возвращается пустой объект DataValue.
    - ``DataValue.createObj()`` - создает пустой объект DataValue.
    - ``DataValue.createArr()`` - создает пустой массив DataValue.
    - ``DataValue.createStr(value: Any?)`` - создает строковое представление переданного значения.
    
Пример использования:
    
.. code-block:: javascript

    var event = DataValue.of(someExampleEventStructure);

    print("---HELLO FROM SCRIPT---");


    print("event id from base: " + event.get("_meta").get("id"));
    print("event id from $: " + event.get("$._meta.id"));
    print("event id from JsonPointer: " + event.get("/_meta/id"));

    print("event time as instant: " + event.get("/_meta/time").takeAsInstant());
    print("event field names list: " + event.fieldNamesList());

    print("call undefined prop is safe: " + event.get("/_meta/a/b/c/"));

    print("event id is boolean " + event.get("_meta").get("id").isBoolean());


    print("-------END--------------");
    
    
DataValue может быть сохранен в execution процесса с последующим извлечением и использованием.

Сохраняем в execution:

.. code-block:: javascript

    var arr = ["a", "b"];
    var obj = {
      a: "b"
    }
    
    var dArr = DataValue.of(arr);
    var dObj = DataValue.of(obj);
    
    execution.setVariable("dArr", dArr);
    execution.setVariable("dObj", dObj);
    
    
Обращаемся к сохраненным в execution переменным в другом скрипте
    
.. code-block:: javascript

    print("----------");
    
    print("dArr: " + dArr);
    print("dArr 0: " + dArr.get("0"));
    
    print("dObj: " + dObj);
    print("dObj a: " + dObj.get("a"));
    
    print("----------");
    
    
Результат:

.. code-block::

    ----------
    dArr: {"0":"a","1":"b"}
    dArr 0: "a"
    dObj: {"a":"b"}
    dObj a: "b"
    ----------

WebUrl
~~~~~~

``webUrl`` - переменная возвращает настроенный веб url сервера

Tasks
~~~~~

``tasks`` - сервис для манипуляций над задачами.
    
    - ``tasks.completeActiveTasks(execution: DelegateExecution)`` - завершает все активные задачи по инстансу процесса из [DelegateExecution.getProcessInstanceId]. Задачи завершаются с результатом *defaultDone: Выполнено*.

Logger
~~~~~~

``log`` -  логгер, пишет в микросервис ecos-process, дополнительно выводится информация о execution. Для настройки уровня логирования используется класс ``ru.citeck.ecos.process.domain.bpmn.engine.camunda.services.beans.ScriptLogger``. |br| Поддерживаемые методы:
    
    - ``log.info(message: String)``
    - ``log.warn(message: String)``
    - ``log.error(message: String)``
    - ``log.debug(message: String)``
    - ``log.trace(message: String)``

.. note:: 

    Читай подробнее о `scripting в Camunda <https://docs.camunda.org/manual/7.14/user-guide/process-engine/scripting/>`_



.. |br| raw:: html

     <br>   
