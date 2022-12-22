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

Во время выполнения скриптов доступны все переменные процесса, видимые в текущей области.

.. code-block:: javascript

    //someVar - переменная процесса
    print("someVar: " + someVar);


Также в контексте скрипта доступно несколько специальных переменных:

``execution`` - переменная, которая всегда доступна, если скрипт выполняется в области выполнения (например, в Script Task). `(DelegateExecution) <https://docs.camunda.org/javadoc/camunda-bpm-platform/7.17/org/camunda/bpm/engine/delegate/DelegateExecution.html>`_

.. code-block:: javascript

    // получение переменной процесса
    var sum = execution.getVariable('x');

    // установление переменной процесса
    execution.setVariable('y', x + 15);


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


``webUrl`` - переменная возвращает настроенный веб url сервера

``tasks`` - сервис для манипуляций над задачами.
    - ``tasks.completeActiveTasks(execution: DelegateExecution)`` - завершает все активные задачи по инстансу процесса из [DelegateExecution.getProcessInstanceId]. Задачи завершаются с результатом *defaultDone: Выполнено*.

.. note:: 

    Читай подробнее о `scripting в Camunda <https://docs.camunda.org/manual/7.14/user-guide/process-engine/scripting/>`_
