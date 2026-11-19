.. _script_task:

Скриптовая задача
=================

.. contents::

Задача, запускающая скрипт (т.е. последовательность действий) или программный код, который выполняется автоматически.

Атрибуты и форма
----------------

Используется язык JavaScript.

.. image:: _static/script_task/59.png
   :width: 300
   :align: center

Имя
~~~

Укажите **Имя**.

.. image:: _static/script_task/60.png
   :width: 300
   :align: center

Скрипт
~~~~~~

Укажите **скрипт**.

.. image:: _static/script_task/61.png
   :width: 300
   :align: center

Настройки асинхронности
~~~~~~~~~~~~~~~~~~~~~~~~

- **Асинхронно "перед"** — исполнение доходит до точки перед блоком, транзакция комитится и дальнейшее выполнение ставится в очередь, которую разбирает уже джоба.
- **Асинхронно "после"** — исполнение доходит до точки после блока, транзакция комитится и дальнейшее выполнение ставится в очередь, которую разбирает уже джоба.

При включении асинхронности также доступны **«Эксклюзивность»**, **«Цикл повтора»** и **«Приоритет»** фоновой задачи.

См. подробнее о `асинхронных задачах <https://camunda.com/blog/2014/07/advanced-asynchronous-continuations/>`_.

.. image:: _static/script_task/62.png
   :width: 300
   :align: center

.. important::

   Поле **«Скрипт»** обязательно в форме настройки элемента. При серверной валидации скрипт не должен быть пустым или состоять из пробелов.

Multi Instance
~~~~~~~~~~~~~~

В форме также доступны настройки **Multi Instance** для многократного выполнения скриптовой задачи.
  
Доступные переменные
--------------------

Переменные процесса
~~~~~~~~~~~~~~~~~~~

Во время выполнения скриптов доступны все переменные процесса, видимые в текущей области.

Наличие и значения переменных зависят от способа запуска процесса и уже выполненных действий. Для обращения к переменной, которая может отсутствовать, используйте ``execution.getVariable('имя')``.

.. code-block:: javascript

    // someVar - переменная процесса
    print("someVar: " + someVar);

Типичные переменные процесса:

``documentRef`` - строковое представление entityRef документа |br|
``documentType`` - id типа документа |br|
``lastTaskCompletor`` - username пользователя, который завершил последнюю задачу |br|
``comment`` - комментарий из последней завершенной задачи |br|
``workflowInitiator`` - username инициатора БП |br|

Переменные ``lastTaskCompletor`` и ``comment`` формируются при завершении пользовательских задач. До выполнения соответствующих действий их наличие предполагать нельзя.

.. _execution:

Execution
~~~~~~~~~

``execution`` - переменная, которая всегда доступна, если скрипт выполняется в области выполнения (например, в Script Task). `(DelegateExecution) <https://docs.camunda.org/javadoc/camunda-bpm-platform/7.17/org/camunda/bpm/engine/delegate/DelegateExecution.html>`_

.. code-block:: javascript

    // Получение переменной процесса
    var x = execution.getVariable('x');

    // Установление переменной процесса
    execution.setVariable('y', x + 15);

Document
~~~~~~~~

``document`` - является скриптовым представлением документа `AttValueScriptCtx <https://github.com/Citeck/ecos-records/blob/master/ecos-records/src/main/java/ru/citeck/ecos/records3/record/atts/computed/script/AttValueScriptCtx.kt>`_ , по которому идет БП.

Объект создаётся через ``Records.get(documentRef)``. Если процесс запущен без документа, получите нужную запись явно через ``Records.get(...)``, передав корректную ссылку.

.. code-block:: javascript

    // Получение атрибута документа
    var created = document.load("_created");

    // Установление атрибуту документа указанного значения
    document.att("firArchiveBoxNumber", 123);
    // Сохранение
    document.save();

    // Сброс состояния документа, если ранее были внесены изменения через att()
    document.att("firArchiveBoxNumber", 123);
    document.reset();
    

Records
~~~~~~~

``Records`` - сервис, который предоставляет доступ к функциям работы с рекордами `RecordsScriptService <https://github.com/Citeck/ecos-records/blob/master/ecos-records/src/main/java/ru/citeck/ecos/records3/record/atts/computed/script/RecordsScriptService.kt>`_.

.. code-block:: javascript

    // Получение скриптового представление указанного рекорда
    var doc = Records.get("emodel/doc@111");

    // Query рекордов
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

ECOS Config
~~~~~~~~~~~

``Config`` - предоставляет доступ к Конфигурации Citeck по ключу в формате ``<область>$<идентификатор>``.

Методы возвращают ``ru.citeck.ecos.bpmn.commons.values.BpmnDataValue`` (далее в сигнатурах — ``BpmnDataValue``).

    - ``get(key: String): BpmnDataValue`` - получение значения по ключу
    - ``getOrDefault(key: String, defaultValue: Any): BpmnDataValue`` - получение значения по ключу, если значение не найдено, то возвращается значение по умолчанию
    - ``getNotNull(key: String): BpmnDataValue`` - получение значения по ключу, если значение null, то выбрасывается исключение

.. code-block:: javascript

    // Получение значения конфигурации по ключу и приведение к типу String
    const serviceDeskEmailFrom = Config.get("app/service-desk$send-sd-email-from").asText()
    
    // Получение значение конфигурации из ecos-app и приведение к типу Boolean
    const enabled = Config.get("app/eapps$enable-crm-lead-ai-spam-check").asBoolean();

.. _bpmn_script_data_value:

DataValue
~~~~~~~~~

``DataValue`` — сервис для создания объектов ``ru.citeck.ecos.bpmn.commons.values.BpmnDataValue``. Объект позволяет работать с JSON-данными: безопасно обращаться к полям, получать значения по умолчанию, приводить значения к нужному типу и сохранять данные в execution. Класс находится в библиотеке BPMN commons; одноимённый класс в пакете ``ecos.process.domain.bpmn.engine.camunda.impl.variables.convert`` устарел.

    - ``DataValue.of(content: Any?)`` — преобразует переданные данные в объект DataValue.
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

Для прямого сохранения JavaScript-объектов используйте ``DataValue.of(...)``. Нативные JavaScript-объекты через ``execution.setVariable(...)`` сохранять нельзя. JavaScript-массивы поддерживаются и могут сохраняться напрямую.

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
    
    
.. _time_and_duration:

Time и Duration. Работа с датами и временными интервалами
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

При работе с датами и временными интервалами рекомендуется использовать объекты ``Time`` и ``Duration``.

``Time`` - объект, упрощающий работу с датами, позволяющий сохранять дату в execution процесса, добавлять к дате календарное/рабочее время на основе рабочего расписания, получать разницу между двумя датами и многое другое. Подробнее см. примеры.

``Duration`` - объект, упрощающий работу с временными интервалами. Поддерживается сохранение в execution процесса.

Примеры использования:

.. code-block:: javascript

    // Получение текущего времени
    let now = Time.now();

    // Получение времени из строки в формате ISO
    let timeFromIsoString = Time.of("2023-02-07T15:00:00.0Z");

    // Получение времени из миллисекунд с начала 1970-01-01T00:00:00Z.
    let timeFromEpochMilli = Time.ofEpochMilli(1644236400000);

    // Получение миллисекунд с начала 1970-01-01T00:00:00Z.
    let timeToEpochMilli = timeFromIsoString.toEpochMilli();



    // Создание объектов Time
    let aprilFirst = Time.of("2023-04-01T00:00:00.0Z");
    let mayFirst = Time.of("2023-05-01T00:00:00.0Z");
    let mayFirst2 = Time.of("2023-05-01T00:00:00.0Z");

    // Сравнение времени
    let isBefore = aprilFirst.isBefore(mayFirst); // true
    let isAfter = aprilFirst.isAfter(mayFirst); // false

    let isBeforeOrEqual = aprilFirst.isBeforeOrEqual(mayFirst); // true
    let isAfterOrEqual = mayFirst.isAfterOrEqual(mayFirst2); // true



    // Создание объектов Time
    let timeFirst = Time.of("2023-04-01T00:00:00.0Z");
    let timeSecond = Time.of("2023-04-01T00:30:00.0Z");

    // Получение разницы между двух точек времени в Duration
    let durationBetween = Time.durationBetween(timeFirst, timeSecond); // PT30M
    let durationAsString = durationBetween.toString(); // "30m"
    let durationAsIsoString = durationBetween.toIsoString(); // "PT30M"

    // Получение разницы между двумя точками времени в минутах
    let durationBetweenMinutes = Time.durationBetween(timeFirst, timeSecond).inWholeMinutes(); // 30
    // etc.



    // Объект Time можно сохранять в execution процесса
    execution.setVariable("time", now);
    // Можно получить объект Time из execution процесса
    let timeFromExecution = execution.getVariable("time");

    // Объект Duration можно сохранять в execution процесса
    execution.setVariable("duration", durationBetween);
    // Можно получить объект Duration из execution процесса
    let durationFromExecution = execution.getVariable("duration");



    let someTime = Time.now();

    // Добавление 1 часа к указанному времени
    let plus1h = Time.plus(someTime, "PT1H");

    // Вычитание 1 часа из указанного времени
    let minus1h = Time.minus(someTime, "PT1H");

    // Добавление 10 минут к текущему времени
    let nowPlus10m = Time.nowPlus("PT10M");

    // Вычитание 10 минут из текущего времени
    let nowMinus10m = Time.nowMinus("PT10M");



    // Добавление 1 часа 30 минут рабочего времени к указанному. Используется рабочее расписание по умолчанию
    let plusWorkingTime1h30m = Time.plusWorkingTime(someTime, "PT1H30M");

    // Добавление 1 часа 30 минут рабочего времени к указанному. Можно указать id рабочего расписания
    let plusWorkingTime1h30mScheduleId = Time.plusWorkingTime(someTime, "PT1H30M", "DEFAULT");

    // Добавление 8 часов рабочего времени к текущему времени. Используется рабочее расписание по умолчанию
    let nowPlusWorkingTime = Time.nowPlusWorkingTime("PT8H");

    // Добавление 8 часов рабочего времени к текущему времени. Можно указать id рабочего расписания
    let nowPlusWorkingTimeWithScheduleId = Time.nowPlusWorkingTime("PT8H", "DEFAULT");


.. warning::

    Прямое сохранение нативного JavaScript ``Date`` через ``execution.setVariable(...)`` не поддерживается. Для сохранения даты используйте ``Time`` или ISO-строку, для временного интервала — ``Duration``.


WebUrl
~~~~~~

``webUrl`` — переменная возвращает настроенный веб url сервера

Tasks
~~~~~

``tasks`` — сервис для манипуляций над задачами.
    
    - ``completeActiveTasks(execution: DelegateExecution)`` - завершает все активные задачи экземпляра процесса, определённого через ``execution.getProcessInstanceId()``. Задачи завершаются с идентификатором результата ``defaultDone``. Если у задачи настроен вердикт с таким идентификатором, используется его название; иначе — название по умолчанию **«Выполнено»**.


Templated content
~~~~~~~~~~~~~~~~~~

``templatedContent`` — сервис для работы с шаблонизированным контентом.

    - ``write(record, template)`` — генерирует контент по шаблону ``template`` на основе данных записи ``record`` и записывает его в атрибут ``content`` этой записи.
    - ``write(record, template, parentAtt: String, childType: String, attribute: String)`` — позволяет явно задать атрибут контента ``attribute``. Если параметры ``parentAtt`` и ``childType`` не нужны, передайте пустые строки.

Параметры ``record`` и ``template`` принимают строку или ``EntityRef``. Для шаблона можно указать его id; отсутствующие части ссылки дополняются до ``transformations/template@id``.

.. warning::

    В ``ecos-process 2.38.0-SNAPSHOT`` трёхаргументный вызов ``write(record, template, attribute)`` передаёт третий аргумент как ``parentAtt``, а атрибут контента остаётся ``content``. Для явного задания атрибута используйте пятиаргументный вызов:

    .. code-block:: javascript

        templatedContent.write(documentRef, "template-id", "", "", "customContent");

Events
~~~~~~

``events`` — сервис для работы с :ref:`событиями Citeck <ecos_bpmn_events>`.

    - ``send(type: String, data: BpmnDataValue)`` - отправляет событие с указанным типом (именем) и данными.
    
Например, можно отправить Citeck событие через скрипт:

.. code-block:: javascript

    var data = DataValue.of({
      foo: "bar",
      number: 123
    });
     
    events.send("test-topic", data);
     
И подписаться на него в bpmn event через ручную настройку с "test-topic" или программно через слушателя:

.. code-block:: kotlin

    eventsService.addListener<ObjectData> {
      withEventType("test-topic")
      withDataClass(ObjectData::class.java)
      withTransactional(true)
      withAttributes(
        mapOf("foo" to "foo", "itsNum" to "number")
      )
      withAction { event ->
        log.info("event received: $event")
      }
    }

Logger
~~~~~~

``log`` — логгер, пишет в микросервис ecos-process, дополнительно выводится информация о execution. Для настройки уровня логирования используется класс ``ru.citeck.ecos.process.domain.bpmn.engine.camunda.services.beans.ScriptLogger``. |br| Поддерживаемые методы:
    
    - ``log.info(message: Any)``
    - ``log.warn(message: Any)``
    - ``log.error(message: Any)``
    - ``log.debug(message: Any)``
    - ``log.trace(message: Any)``

.. note::

    Читай подробнее о `scripting в Camunda <https://docs.camunda.org/manual/7.14/user-guide/process-engine/scripting/>`_



.. |br| raw:: html

     <br>   

Примеры
---------


Скрипт, как в атрибут записать человека, который выполнил предыдущую задачу
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    document.att("manager", "emodel/person@" + lastTaskCompletor);
    document.save();


.. image:: _static/script_task/sample_01.png
       :width: 800
       :align: center


Получить локальную часть глобальной ссылки на сущность
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    document.load("requestCategory?localId") == "community"

- **requestCategory** - ассоциация

- **?localId** - :ref:`скаляр<Records_API_scalar>` из :ref:`Records API<Records_API>`, который возвращает локальную часть глобальной ссылки на сущность. Например для **emodel/person@someuser** локальная часть - **"someuser"**

Загрузка идентификаторов из ассоциаций
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

При работе с ассоциациями в скриптах важно учитывать разницу между ``.id`` и ``?id``:

- ``.id`` — возвращает часть ссылки после ``@`` (localId). Например: ``emodel/authority-group@accountant`` → ``accountant``
- ``?id`` — возвращает полную ссылку. Например: ``emodel/authority-group@accountant``

Для передачи значений в другие ассоциации используйте ``?id``:

.. code-block:: javascript

    // Получить полную ссылку для передачи в другую ассоциацию
    var refs = document.load("approvers[]?id");

    // Наполнение другой ассоциации полными ссылками
    document.att("doc_watchers", document.load("approvers[]?id"));
    document.save();

Скрипт для проверки наличия комментариев после завершения задачи
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    if (!execution.getVariable('comment')) {
        throw new Error("Комментарий не заполнен");
    }

При завершении задачи пустой или состоящий из пробелов комментарий нормализуется в ``null`` и записывается в переменную ``comment``. Предыдущий комментарий при этом не сохраняется.


.. dropdown:: Пример вычисления id рабочего расписания с использованием DMN
   :color: secondary

   Пример процесса:

   .. image:: _static/script_task/process_01.png
      :width: 700
      :align: center

   Установка переменной для DMN:

   .. image:: _static/script_task/process_02.png
      :width: 700
      :align: center

   Скрипт:

   .. code-block:: javascript

       execution.setVariable("sum", document.load("sum?num"));

   Выбор рабочего календаря:

   .. image:: _static/script_task/process_03.png
      :width: 700
      :align: center

   **Переменная результата:** ``workingCalendarId``

   :ref:`DMN решение<dmn_decision>` содержит id :ref:`созданных календарей<business-schedule>`:

   .. image:: _static/script_task/process_04.png
      :width: 600
      :align: center

   Пользовательская задача:

   .. image:: _static/script_task/process_05.png
      :width: 700
      :align: center

   Срок выполнения:

   .. code-block:: javascript

       ${Time.nowPlusWorkingDays(5, workingCalendarId).toIsoString()}

   :download:`скачать процесс <../examples/test-bpmn-process.bpmn.xml>`
