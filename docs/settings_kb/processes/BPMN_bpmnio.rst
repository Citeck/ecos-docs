Редактор бизнес-процессов (BPMN) с использованием bpmn-js 
============================================================

.. contents::
    :depth: 3

Общий обзор (Overview)
------------------------

В Ecos реализован удобный и понятный редактор бизнес-процессов на основе библиотеки bpmn-js ( https://bpmn.io/).

Библиотека bpmn-js предназначена для моделирования и автоматизации бизнес-процессов (БП) со встроенным механизмом выполнения бизнес-процессов BPMN 2.0 (BPMN-движок).

 .. image:: _static/BPMN_bpmnio/01.png
       :width: 600
       :align: center

Для создания нового бизнес-процесса необходимо перейти в левом меню в пункт **«Редактор бизнес-процессов»** или через верхнее меню **«Раздел администратора – Управление процессами – Модели бизнес-процессов»**.

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_bpmnio/02.png
                :width: 50
                :align: center

        - представление в виде плитки|списка

Представление в виде списка:

 .. image:: _static/BPMN_bpmnio/03.png
       :width: 600
       :align: center

Для созданного процесса доступны следующие опции:

 .. image:: _static/BPMN_bpmnio/04.png
       :width: 200
       :align: center

* **Просмотреть:**
  
        .. image:: _static/BPMN_bpmnio/05.png
            :width: 600
            :align: center

*	**Удалить**
*	**Редактировать карточку процесса:**

        .. image:: _static/BPMN_bpmnio/06.png
            :width: 600
            :align: center


*	**Редактировать бизнес-процесс:**

        .. image:: _static/BPMN_bpmnio/07.png
            :width: 600
            :align: center


.. _modeller_bp:

Конструктор бизнес-процесса
-----------------------------

 .. image:: _static/BPMN_bpmnio/11.png
       :width: 600
       :align: center

1.	Панель элементов 
2.	Панель свойств элемента - задаются свойства либо самой диаграммы, либо выделенного элемента.
3.	Свернуть панель свойств элемента
4.	Ползунок для перемещения рабочего пространства
5.	Сохранение процесса
6.	Посмотреть XML
7.	Сохранение и публикация процесса в движок
8.	Сохранить в svg
9.	Кнопки работы с масштабом

Состав панели элементов
~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_bpmnio/12.png
                :width: 30
                :align: center

        - **Activate the hand tool** – используется для перемещения диаграммы вверх-вниз, вправо-влево, удерживая ее левой кнопкой мыши.
      * - 
               .. image:: _static/BPMN_bpmnio/13.png
                :width: 30
                :align: center

        - | **Activate the lasso tool** – используется для выделения области диаграммы - позволяет выделить несколько элементов диаграммы, удерживая левую кнопку мыши. 
          | Выделяются все элементы, попавшие в выделяемую область.
      * - 
               .. image:: _static/BPMN_bpmnio/14.png
                :width: 30
                :align: center

        - | **Activate the create/remove space tool** – позволяет «раздвинуть» или «сжать» диаграмму: указатель мыши ставиться на то место на диаграмме, где нужно «раздвинуть» или «сжать» диаграмму.
          | И удерживая левую кнопку мыши, указателем переместить часть диаграммы в нужное место.
      * - 
               .. image:: _static/BPMN_bpmnio/15.png
                :width: 30
                :align: center

        - | **Activate the global connect tool** - соединяющие элементы: поток управления (сплошная линия) и поток сообщений (прерывистая линия).

Элементы потока управления:

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_bpmnio/16.png
                :width: 30
                :align: center

        - **Create StartEvent** - начальное событие
      * - 
               .. image:: _static/BPMN_bpmnio/17.png
                :width: 30
                :align: center

        - **Create Intermediate/Boundary Event** - промежуточное событие
      * -
               .. image:: _static/BPMN_bpmnio/18.png
                :width: 30
                :align: center

        - **Create EndEvent** - завершающее событие
      * - 
               .. image:: _static/BPMN_bpmnio/19.png
                :width: 30
                :align: center

        - **Create Gateway** - развилка или шлюз, логический оператор
      * - 
               .. image:: _static/BPMN_bpmnio/20.png
                :width: 30
                :align: center

        - **Create Task** – задача
      * -
               .. image:: _static/BPMN_bpmnio/21.png
                :width: 30
                :align: center

        - **Create expanded SubProcess** – несколько task, выделенные в отдельную подзадачу
      * -
               .. image:: _static/BPMN_bpmnio/89.png
                :width: 30
                :align: center

        - **Create Set document status** – изменение значения статуса элемента бизнес-процесса
      * -
               .. image:: _static/BPMN_bpmnio/22.png
                :width: 30
                :align: center

        - **Create DataObjectReference** - объект данных представляет информацию, проходящую через процесс
      * -
               .. image:: _static/BPMN_bpmnio/23.png
                :width: 30
                :align: center

        - | **Хранилище данных** — хранилище, куда процесс может считывать или записывать данные, например, база данных или картотека.
          | Он сохраняется за пределами жизненного цикла экземпляра процесса
      * -
               .. image:: _static/BPMN_bpmnio/24.png
                :width: 30
                :align: center

        - | **Create Pool/Participant** – пул, используются для разграничении ответственности между задачами, организациями, пользователями. 
          | Пулы взаимодействуют между собой только потоками сообщений.
      * -
               .. image:: _static/BPMN_bpmnio/25.png
                :width: 30
                :align: center

        - **Create Group** – объединение элементов в группу

Любой бизнес-процесс начинается с начального события  и заканчивается конечным событием. 

Вы создаете диаграмму БП, выбирая на Панели элементов нужные вам элементы диаграммы и соединяете их потоками управления. Выделив любой элемент диаграммы, справа от него появляется панель кнопок 

 .. image:: _static/BPMN_bpmnio/26.png
       :width: 300
       :align: center

На панели рядом с элементом расположены следующие кнопки:

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_bpmnio/27.png
                :width: 70
                :align: center

        - создать следующий элемент диаграммы, связанный с выделенным потоком управления
      * - 
               .. image:: _static/BPMN_bpmnio/28.png
                :width: 30
                :align: center

        - добавить текст аннотации к элементу
      * - 
               .. image:: _static/BPMN_bpmnio/89.png
                :width: 30
                :align: center

        - изменить значение статуса элемента бизнес-процесса
      * - 
               .. image:: _static/BPMN_bpmnio/29.png
                :width: 30
                :align: center

        - | изменить тип элемента
          | Нажать для изменения типа элемента и далее выбрать соответствующий тип.
      * - 
               .. image:: _static/BPMN_bpmnio/30.png
                :width: 30
                :align: center

        - удалить элемент
      * - 
               .. image:: _static/BPMN_bpmnio/31.png
                :width: 30
                :align: center

        - связать элемент с любым другим на диаграмме  

Основные типы элемента **Задача**:

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_bpmnio/32.png
                :width: 80
                :align: center

        - пользовательская задача 
      * - 
               .. image:: _static/BPMN_bpmnio/90.png
                :width: 80
                :align: center

        - задача-сценарий
      * - 
               .. image:: _static/BPMN_bpmnio/34.png
                :width: 80
                :align: center

        - отправка сообщений
      * - 
               .. image:: _static/BPMN_bpmnio/35.png
                :width: 80
                :align: center

        - [не реализован] получение сообщений
      * - 
               .. image:: _static/BPMN_bpmnio/36.png
                :width: 80
                :align: center

        - [не реализован] ручное выполнение
      * - 
               .. image:: _static/BPMN_bpmnio/37.png
                :width: 80
                :align: center

        - задача, имеющая вложенный процесс

Основные типы элемента **Шлюз**:

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_bpmnio/38.png
                :width: 100
                :align: center

        -  параллельный шлюз, используется для обозначения слияния/ ветвления потоков управления в рамках процесса
      * - 
               .. image:: _static/BPMN_bpmnio/38a.png
                :width: 100
                :align: center

        -  исключающий шлюз, используется для ветвления потока управления на несколько альтернативных потоков, когда выполнение процесса зависит от выполнения некоторого исключающего условия
      * - 
               .. image:: _static/BPMN_bpmnio/39.png
                :width: 100
                :align: center

        - [не реализован] неэксклюзивный шлюз, используется для ветвления потока управления на несколько потоков, когда выполнение процесса зависит от выполнения условий
      * - 
               .. image:: _static/BPMN_bpmnio/40.png
                :width: 100
                :align: center

        - [не реализован] комплексный шлюз, используется для ветвления потока управления на несколько потоков, когда выполнение процесса зависит от выполнения условий
      * - 
               .. image:: _static/BPMN_bpmnio/41.png
                :width: 100
                :align: center

        - [не реализован] эксклюзивный шлюз по событиям, используется для ветвления потока на несколько альтернативных потоков, когда дальнейшее выполнение процесса зависит от возникновения некоторого события-обработчика, следующего после шлюза. Событие, идущее после шлюза и возникшее первым, определяет дальнейший ход  выполнения процесса 

Основные типы элемента **Поток управления**:

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_bpmnio/42.png
                :width: 100
                :align: center

        -  поток управления по умолчанию, используется, когда необходимо показать, что выполнение процесса будет происходить по этому потоку только если не выполняется ни одно из заданных условий
      * - 
               .. image:: _static/BPMN_bpmnio/43.png
                :width: 100
                :align: center

        - | условный поток управления, используется чтобы показать, что выполнение процесса будет происходить по этому потоку только в том случае, когда выполнятся заданное условие. 
          | Такой тип элемента выбирается, если условный поток управления является исходящим от процесса

**Multi Instance** - многоэкземплярная активность выполняется либо последовательно, либо параллельно (по умолчанию).

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_bpmnio/44.png
                :width: 30
                :align: center

        -  | **Parallel Multi Instance** - параллельная активность с несколькими экземплярами. 
           | Все экземпляры создаются при активации тела активности с несколькими экземплярами. 
           | Экземпляры выполняются одновременно и независимо друг от друга.

      * - 
               .. image:: _static/BPMN_bpmnio/45.png
                :width: 30
                :align: center

        - | **Sequential Multi Instance** – последовательная активность с несколькими экземплярами. 
          | Экземпляры выполняются друг за другом. 
          | Когда один экземпляр завершен, создается новый экземпляр для следующего элемента в ``inputCollection``. 

      * - 
               .. image:: _static/BPMN_bpmnio/46.png
                :width: 30
                :align: center

        -  | **Loop** – циклическая задача повторяется до тех пор, пока определенное условие либо не будет применено, либо перестанет применяться.
           | В Ecos не поддерживается.
      * - 
               .. image:: _static/BPMN_bpmnio/47.png
                :width: 30
                :align: center

        - | **Ad hoc**. Доступно только для подпроцесса. Ad hoc подпроцесс можно использовать, чтобы отметить сегмент, в котором содержащиеся действия (задачи или подпроцессы) могут:

            *	выполняться в любом порядке,
            *	выполняться несколько раз
            *	пропустить.

.. _new_bp:

Создание бизнес-процесса
-------------------------

Для создания процесса необходимо нажать:

 .. image:: _static/BPMN_bpmnio/08.png
       :width: 300
       :align: center

Откроется форма создания карточки процесса:

 .. image:: _static/BPMN_bpmnio/09.png
       :width: 600
       :align: center

.. list-table:: 
      :widths: 10 20 30
      :header-rows: 1
      :align: center
      :class: tight-table 

      * - п/п
        - Наименование
        - Описание
      * - 1
        - **Идентификатор**
        - уникальный идентификатор
      * - 2
        - **Имя**
        - наименование создаваемого бизнес-процесса
      * - 3
        - **Ecos Type**
        - тип данных. При привязке к типу данных можно автоматически начинать процесс, если проставлен  чекбокс **(7)**. На форме редактора на основе типа данных будут подтягиваться роли, статусы и т.д.
      * - 4
        - **Раздел**
        - наименование раздела, в котором будет сохранен процесс. Если не заполнять, то сохранение происходит в раздел "По умолчанию".
      * - 5
        - **Форма**
        - указать для запуска (старта) процесса через форму.
      * - 6
        - **Включен**
        - включение процесса
      * - 7
        - **Автоматический старт процесса**
        - при создании объекта указанного типа процесс будет запущен автоматически.

Нажать **«Save»**.

Для работы с процессом в редакторе нажмите:

 .. image:: _static/BPMN_bpmnio/10.png
       :width: 600
       :align: center

Откроется :ref:`конструктор бизнес-процесса<modeller>`

.. _modeller:

Компоненты конструктора
-----------------------

.. _notification:

Уведомление
~~~~~~~~~~~

 .. image:: _static/BPMN_bpmnio/48.png
       :width: 400
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя**, выбрать **Тип уведомления**

        - 
               .. image:: _static/BPMN_bpmnio/49.png
                :width: 300
                :align: center

      * - Выбрать шаблон, или указать **Заголовок** и тело сообщения

        - 
               .. image:: _static/BPMN_bpmnio/50.png
                :width: 300
                :align: center

         |

               .. image:: _static/BPMN_bpmnio/51.png
                :width: 300
                :align: center
         
         | При прямом использовании Заголовка и Тела возможно указывать только текст, без использования динамических переменных из процесса или документа. 

      * - Получатели выбираются из списка ролей, заполненных в :ref:`типе данных<data_types_main>`
        - 
               .. image:: _static/BPMN_bpmnio/52.png
                :width: 300
                :align: center

         |

               .. image:: _static/BPMN_bpmnio/53.png
                :width: 300
                :align: center   

.. _user_task:

Пользовательская задача
~~~~~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/BPMN_bpmnio/54.png
       :width: 400
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя**, **Реципиентов** – исполнителей задачи, выбираются из списка ролей, заполненных в :ref:`типе данных<roles_statuses>` 

        - 
               .. image:: _static/BPMN_bpmnio/55.png
                :width: 300
                :align: center
      * - | Выбрать **форму задачи** из списка или создать ее (см. ниже), выставить **приоритет задачи**, указать результат задачи – **идентификатор** и **название**.
          | **Форма задачи** определяет то, что будет отображено при назначении задачи пользователю.
          | Если какие-то задачи могут совпадать, то можно использовать одинаковую форму, но если различаются, то, соответственно, формы разные.
        - 
               .. image:: _static/BPMN_bpmnio/56.png
                :width: 300
                :align: center

Создание формы:

 .. image:: _static/BPMN_bpmnio/57.png
       :width: 600
       :align: center

Элементы формы задачи связаны с переменными инстанса (экземпляра) процесса.

Если в области видимости задачи/процесса есть переменная с таким же **id** (Имя свойства), как и у элемента формы, то ее содержимое отобразится на форме. 

При сабмите (публикации) формы задачи переменные будут записаны в переменные процесса.

Элементы формы задачи так же могут быть связаны с переменными документа, по которому идет бизнес-процесс.

Для отображения и обновления переменных документа на форме задачи необходимо добавить элемент с **id** (Имя свойства) с префиксом **_ECM_**, например **_ECM_paymentSum**, где **paymentSum** - свойства документа.

Для добавления кнопки вердикта задачи на форму задачи необходимо добавить кнопку с **«Имя свойства»**, заданным по шаблону **outcome_идентификаторВердикта**. Например, **outcome_approve**.

 .. image:: _static/BPMN_bpmnio/58.png
       :width: 600
       :align: center

.. _script_task:

Задача-сценарий
~~~~~~~~~~~~~~~~

 .. image:: _static/BPMN_bpmnio/59.png
       :width: 300
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/BPMN_bpmnio/60.png
                :width: 300
                :align: center
      * - Указать **скрипт** 
        - 
               .. image:: _static/BPMN_bpmnio/61.png
                :width: 300
                :align: center
      * - Указать **скрипт** 
        - Асинхронность можно настроить ко многим элементам. См. подробнее https://camunda.com/blog/2014/07/advanced-asynchronous-continuations/ 
               .. image:: _static/BPMN_bpmnio/62.png
                :width: 300
                :align: center

Описание и примеры
"""""""""""""""""""

Язык JavaScript. В контексте скрипта доступно:

1.	**Переменные процесса**. Обращение к переменным процесса осуществляется по прямому наименованию переменной. Например:

.. code-block::

    print("someVar: " + someVar);

2.	**Переменная «execution» процесса** 

см. подробно https://docs.camunda.org/javadoc/camunda-bpm-platform/7.17/org/camunda/bpm/engine/delegate/DelegateExecution.html 

Через нее можно так же получать переменные процесса (аналог пункта 1) или записывать:

.. code-block::

    // get process variable
    sum = execution.getVariable('x')

    // set process variable
    execution.setVariable('y', x + 15)

3.	**Переменная «document»** - скриптовое представление документа 

.. code-block::

    AttValueScriptCtxfun getId(): String

    fun getRef(): RecordRef

    fun getLocalId(): String

    fun load(attributes: Any?): Any?

    fun save(): AttValueScriptCtx fun att(attribute: String, value: Any?)

    fun reset()
    }

**load()** - получение атрибута документа: 

.. code-block::

    var created = document.load("cm:created")

**att()** - установление атрибуту документа указанного значения:

.. code-block::

    document.att("ufrm:firArchiveBoxNumber", 123)

**save()** - сохранение внесенных изменений атриумов документа через **att()**

**reset()** - сброс состояния документа, если ранее были внесены изменения через **att()**

Пример задания атрибута и сохранение:

.. code-block::

    document.att("ufrm:firArchiveBoxNumber", 123)
    document.save()


1. **RecordsScriptService** 

Доступен под переменной «Records». 

Методы:

Получение скриптового представления рекорда по **recordReffun** 

.. code-block::

    **fun get(record: Any): AttValueScriptCtx 

Поиск рекордов по заданному **query**

.. code-block::

    **query(query: Any?, attributes: Any?): Any 


.. _gateway:

Шлюз
~~~~~~

 .. image:: _static/BPMN_bpmnio/63.png
       :width: 300
       :align: center

Для шлюза указываются выходы из предыдущих элементов задач. 

Условия могут иметь разные типы условия:

 .. image:: _static/BPMN_bpmnio/64.png
       :width: 300
       :align: center

*	Исходящий (выход из задачи)
*	Скрипт - скрипт, который должен вернуть булевое значение. Например: pasymentSum >= 30000
*	Выражение – expression см. подробно https://docs.camunda.io/docs/components/concepts/expressions/

Например:

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Для согласования:
        - Для отказа в согласовании:
      * - 
               .. image:: _static/BPMN_bpmnio/65.png
                :width: 300
                :align: center

        - 
               .. image:: _static/BPMN_bpmnio/66.png
                :width: 300
                :align: center

Таймер
~~~~~~

 .. image:: _static/BPMN_bpmnio/67.png
       :width: 300
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/BPMN_bpmnio/68.png
                :width: 300
                :align: center
      * - Указать **Тип** и **Значение**

        - 
               .. image:: _static/BPMN_bpmnio/69.png
                :width: 300
                :align: center
      * - | Асинхронность можно настроить ко многим элементам. 
          | См. подробнее https://camunda.com/blog/2014/07/advanced-asynchronous-continuations/
        - 
               .. image:: _static/BPMN_bpmnio/70.png
                :width: 300
                :align: center

Возможные типы:

 .. image:: _static/BPMN_bpmnio/70_a.png
       :width: 300
       :align: center

* **Дата** - указанный момент времени, определяемый как комбинированное представление даты и времени в соответствии с `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.
    
    2019-10-01T12:00:00Z — время UTC
    2019-10-02T08:09:40+02:00 — UTC плюс смещение зоны на 2 часа

* **Продолжительность** - длительность времени, определенная как формат длительности `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.
  
    PT15S - 15 секунд
    PT1H30M - 1 час 30 минут
    P14D - 14 дней

* **Цикл** - цикл, определенный как формат повторяющихся интервалов `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_.

    R5/PT10S - каждые 10 секунд, до 5 раз
    R/P1D - каждый день, бесконечно

Вы можете использовать выражения для значения таймера. Таким образом, вы можете влиять на определение таймера на основе переменных процесса. Переменные процесса должны содержать строку ISO 8601 (или cron для типа цикла) для соответствующего типа таймера. 
Например - **${duration}**.

Подпроцесс
~~~~~~~~~~~~

 .. image:: _static/BPMN_bpmnio/71.png
       :width: 300
       :align: center

**Sub Process (collapsed)** – свернутый подпроцесс. Процесс создается в новом окне редактора по стрелке:

 .. image:: _static/BPMN_bpmnio/72.png
       :width: 200
       :align: center

 .. image:: _static/BPMN_bpmnio/73.png
       :width: 600
       :align: center

**Sub Process (expanded)** – подпроцесс, который отражается на основном окне редактора:

 .. image:: _static/BPMN_bpmnio/74.png
       :width: 300
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/BPMN_bpmnio/75.png
                :width: 300
                :align: center
      * - | **Multi Instance** - действие с несколькими экземплярами выполняется несколько раз — один раз для каждого элемента данной коллекции. 
          | См. подробнее https://docs.camunda.org/manual/7.8/reference/bpmn20/tasks/task-markers/#multiple-instance 
          | Указать **Количество повторений цикла**, **Условие завершения**
          | **Коллекция** - атрибут указывает коллекцию, где для каждого элемента будет создан экземпляр
          | **Переменная элемента** - Атрибут указывает переменную процесса, которая будет установлена для каждого созданного экземпляра, содержащего элемент указанной коллекции.
        - 
               .. image:: _static/BPMN_bpmnio/76.png
                :width: 300
                :align: center
      * - | Асинхронность можно настроить ко многим элементам. 
          | См. подробнее https://camunda.com/blog/2014/07/advanced-asynchronous-continuations/
        - 
               .. image:: _static/BPMN_bpmnio/77.png
                :width: 300
                :align: center

Создание элементов подпроцесса аналогично описанным выше.

.. _set_status:

Установка статуса
~~~~~~~~~~~~~~~~~~~~

Уникальный для ECOS элемент, отмеченный как:

 .. image:: _static/BPMN_bpmnio/86.png
       :width: 200
       :align: center

Элемент позволяет производить смену статуса в создаваемом бизнес-процессе.

 .. image:: _static/BPMN_bpmnio/87.png
       :width: 200
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя** и выбрать **Статус** из списка статусов, заполненных в :ref:`ECOS типе данных<roles_statuses>`

        - 
               .. image:: _static/BPMN_bpmnio/88.png
                :width: 300
                :align: center

Сохранение и публикация
------------------------

Созданный процесс сохраняем и публикуем:

 .. image:: _static/BPMN_bpmnio/78.png
       :width: 600
       :align: center

Настройка меню
-----------------

Для добавления процесса в меню **«Создать»**:
1.	Перейти в настройку меню, нажав на шестеренку, потом кнопку **«Настроить меню» справа сверху**.

 .. image:: _static/BPMN_bpmnio/79.png
       :width: 600
       :align: center

2.	Выбрать элемент меню, в котором будет находиться процесс. Навести на элемент и нажать кнопку **«Добавить»**, выбрать **«Запустить бизнес-процесс»**, из списка выбрать необходимый процесс, нажать **«Ok»**.

 .. image:: _static/BPMN_bpmnio/80.png
       :width: 600
       :align: center

|

 .. image:: _static/BPMN_bpmnio/81.png
       :width: 600
       :align: center

|

 .. image:: _static/BPMN_bpmnio/82.png
       :width: 600
       :align: center

Добавленный пункт меню:

 .. image:: _static/BPMN_bpmnio/83.png
       :width: 400
       :align: center

Запуск задачи
-------------

 .. image:: _static/BPMN_bpmnio/84.png
       :width: 600
       :align: center

|

 .. image:: _static/BPMN_bpmnio/85.png
       :width: 600
       :align: center