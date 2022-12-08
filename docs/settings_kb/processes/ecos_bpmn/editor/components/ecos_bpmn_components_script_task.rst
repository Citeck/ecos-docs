Задача-сценарий
===============
.. _script_task:

Используеттся язык JavaScript.

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
      * - Указать **скрипт** 
        - Асинхронность можно настроить ко многим элементам. См. подробнее https://camunda.com/blog/2014/07/advanced-asynchronous-continuations/ 
               .. image:: _static/62.png
                :width: 300
                :align: center

Доступные переменные
--------------------

В контексте скрипта доступно:

1.	**Переменные процесса**. 

Обращение к переменным процесса осуществляется по прямому наименованию переменной. Например:

.. code-block:: javascript

    print("someVar: " + someVar);

2.	**Переменная «execution» процесса** 

`См. подробно <https://docs.camunda.org/javadoc/camunda-bpm-platform/7.17/org/camunda/bpm/engine/delegate/DelegateExecution.html>`_ 

Через нее можно так же получать переменные процесса (аналог пункта 1) или записывать:

.. code-block:: javascript

    // get process variable
    sum = execution.getVariable('x')

    // set process variable
    execution.setVariable('y', x + 15)

3.	**Переменная «document»** - скриптовое представление документа 

.. code-block:: javascript

    AttValueScriptCtxfun getId(): String

    fun getRef(): RecordRef

    fun getLocalId(): String

    fun load(attributes: Any?): Any?

    fun save(): AttValueScriptCtx fun att(attribute: String, value: Any?)

    fun reset()
    }

**load()** - получение атрибута документа: 

.. code-block:: javascript

    var created = document.load("cm:created")

**att()** - установление атрибуту документа указанного значения:

.. code-block:: javascript

    document.att("ufrm:firArchiveBoxNumber", 123)

**save()** - сохранение внесенных изменений атриумов документа через **att()**

**reset()** - сброс состояния документа, если ранее были внесены изменения через **att()**

Пример задания атрибута и сохранение:

.. code-block:: javascript

    document.att("ufrm:firArchiveBoxNumber", 123)
    document.save()


4. **RecordsScriptService** 

Доступен под переменной «Records». 

Методы:

Получение скриптового представления рекорда по **recordReffun** 

.. code-block:: kotlin

    fun get(record: Any): AttValueScriptCtx 

Поиск рекордов по заданному **query**

.. code-block:: kotlin

    query(query: Any?, attributes: Any?): Any 
