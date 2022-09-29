Создание бизнес-процесса согласования оффера
============================================

:ref:`Для добавленного типа данных «Оффер»<job_offer>` создадим модель бизнес-процесса в редакторе.

Удобный и понятный редактор бизнес-процессов реализован на основе библиотеки bpmn-js ( https://bpmn.io).

Для создания нового бизнес-процесса необходимо перейти в левом меню в пункт **«Редактор бизнес-процессов»**:

 .. image:: _static/BPMN_process/bmpn01.png
       :width: 600
       :align: center

В редакторе бизнес-процессов представлены уже созданные процессы.

Создание бизнес-процесса
-------------------------

Для создания процесса необходимо нажать **«Создать camunda процесс»**:

 .. image:: _static/BPMN_process/bmpn02.png
       :width: 300
       :align: center

Откроется форма создания карточки процесса: 

 .. image:: _static/BPMN_process/bmpn03.png
       :width: 600
       :align: center

1.	**Идентификатор** – указать уникальный идентификатор.
2.	**Ecos Type** – тип данных. Выбрать созданный ранее тип **hr-offer-type** На форме редактора на основе типа данных будут подтягиваться роли, статусы и т.д.
3.	**Имя** – указать наименование создаваемого бизнес-процесса.
4.	**Включен** – чекбокс включения процесса. Можно выставить после моделирования всего процесса в редакторе.
5.	**Автоматический старт процесса** - при создании объекта указанного типа процесс будет запущен автоматически.

После ввода данных нажмите **«Save»**.

Для моделирования элементов созданного процесса в редакторе нажмите:

 .. image:: _static/BPMN_process/bmpn04.png
       :width: 600
       :align: center

Редактор процесса
------------------

 .. image:: _static/BPMN_process/bmpn05.png
       :width: 600
       :align: center

Интерфейс редактора состоит из следующих элементов:
1.	**Панель элементов** 
2.	**Панель свойств элемента** - задаются свойства либо самой диаграммы, либо выделенного элемента.
3.	**Свернуть панель свойств элемента**
4.	**Ползунок** для перемещения рабочего пространства
5.	**Сохранение процесса**
6.	**Посмотреть XML**
7.	**Сохранение и публикация процесса в движок**
8.	**Сохранить в svg**
9.	Кнопки работы с **масштабом**

Панель инструментов состоит из следующих элементов управления:

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_process/12.png
                :width: 30
                :align: center

        - **Activate the hand tool** – используется для перемещения диаграммы вверх-вниз, вправо-влево, удерживая ее левой кнопкой мыши.
      * - 
               .. image:: _static/BPMN_process/13.png
                :width: 30
                :align: center

        - | **Activate the lasso tool** – используется для выделения области диаграммы - позволяет выделить несколько элементов диаграммы, удерживая левую кнопку мыши. 
          | Выделяются все элементы, попавшие в выделяемую область.
      * - 
               .. image:: _static/BPMN_process/14.png
                :width: 30
                :align: center

        - | **Activate the create/remove space tool** – позволяет «раздвинуть» или «сжать» диаграмму: указатель мыши ставиться на то место на диаграмме, где нужно «раздвинуть» или «сжать» диаграмму.
          | И удерживая левую кнопку мыши, указателем переместить часть диаграммы в нужное место.
      * - 
               .. image:: _static/BPMN_process/15.png
                :width: 30
                :align: center

        - | **Activate the global connect tool** - соединяющие элементы: поток управления (сплошная линия) и поток сообщений (прерывистая линия).

В данном примере рассмотрим следующие элементы потока управления:

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_process/16.png
                :width: 30
                :align: center

        - **Create StartEvent** - начальное событие
      * -
               .. image:: _static/BPMN_process/18.png
                :width: 30
                :align: center

        - **Create EndEvent** - завершающее событие
      * - 
               .. image:: _static/BPMN_process/19.png
                :width: 30
                :align: center

        - **Create Gateway** - развилка или шлюз, логический оператор
      * - 
               .. image:: _static/BPMN_process/20.png
                :width: 30
                :align: center

        - **Create Task** – задача

Любой бизнес-процесс начинается с **начального события** и заканчивается **конечным событием**. 

Диаграмма процесса создается из элементов, выбираемых на Панели элементов. Элементы соединяются потоками управления. 

Выделив любой элемент диаграммы, справа от него появляется панель кнопок: 

 .. image:: _static/BPMN_process/26.png
       :width: 300
       :align: center


.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_process/27.png
                :width: 70
                :align: center

        - создать следующий элемент диаграммы, связанный с выделенным потоком управления
      * - 
               .. image:: _static/BPMN_process/28.png
                :width: 30
                :align: center

        - добавить текст аннотации к элементу
      * - 
               .. image:: _static/BPMN_process/29.png
                :width: 30
                :align: center

        - | изменить тип элемента
          | Нажать для изменения типа элемента и далее выбрать соответствующий тип.
      * - 
               .. image:: _static/BPMN_process/30.png
                :width: 30
                :align: center

        - удалить элемент
      * - 
               .. image:: _static/BPMN_process/31.png
                :width: 30
                :align: center

        - связать элемент с любым другим на диаграмме  

Для изменения типа элемента необходимо нажать:

 .. image:: _static/BPMN_process/bmpn06.png
       :width: 300
       :align: center

далее выбрать соответствующий тип.

В данном примере рассмотрим создание следующих типов элемента **Задача** и **Шлюз**:


Основные типы элемента **Задача**:

.. list-table::
      :widths: 1 5
      :class: tight-table 

      * - 
               .. image:: _static/BPMN_process/32.png
                :width: 80
                :align: center

        - пользовательская задача 
      * - 
               .. image:: _static/BPMN_process/34.png
                :width: 80
                :align: center

        - отправка сообщений
      * - 
               .. image:: _static/BPMN_process/bmpn08.png
                :width: 80
                :align: center

        - задача с задаваемым сценарием
      * - 
               .. image:: _static/BPMN_process/bmpn07.png
                :width: 80
                :align: center

        - исключающий шлюз, используется для ветвления потока управления на несколько альтернативных потоков, когда выполнение процесса зависит от выполнения некоторого исключающего условия

Создание элементов
-------------------

Начальное событие
~~~~~~~~~~~~~~~~~~

Начальное событие задается по умолчанию элементом:

 .. image:: _static/BPMN_process/bmpn09.png
       :width: 600
       :align: center

**ID элемента** Система указывает автоматически для всех создаваемых элементов.

Шлюз
~~~~~

 .. image:: _static/BPMN_process/bmpn10.png
       :width: 600
       :align: center

Для шлюза укажите **Имя**.

Создание уведомления
~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/BPMN_process/bmpn11.png
       :width: 600
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - | Указать **Имя**, 
          | выбрать **Тип уведомления**

        - 
               .. image:: _static/BPMN_process/bmpn12.png
                :width: 300
                :align: center

      * - | Выбрать шаблон, 
          | или указать **Заголовок** и **тело сообщения**

        - 
               .. image:: _static/BPMN_process/bmpn13.png
                :width: 300
                :align: center

         |

               .. image:: _static/BPMN_process/bmpn14.png
                :width: 300
                :align: center
         
      * - Получатели выбираются из списка ролей, заполненных в :ref:`типе данных<roles_offer>`
        - 
               .. image:: _static/BPMN_process/bmpn15.png
                :width: 300
                :align: center

         |

               .. image:: _static/BPMN_process/bmpn16.png
                :width: 300
                :align: center   

Создание script task
~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/BPMN_process/bmpn17.png
       :width: 600
       :align: center

.. list-table::
      :widths: 5 5
      :align: center
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/BPMN_process/bmpn18.png
                :width: 300
                :align: center

      * - Указать **скрипт**

        - 
               .. image:: _static/BPMN_process/bmpn19.png
                :width: 300
                :align: center

:ref:`Подробно о скриптах<script_task>`

Создание user task
~~~~~~~~~~~~~~~~~~~~

 .. image:: _static/BPMN_process/bmpn20.png
       :width: 600
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/BPMN_process/bmpn21.png
                :width: 300
                :align: center

      * - Указать **Реципиентов** – исполнителей задачи, выбираются из списка ролей, заполненных :ref:`типе данных<roles_offer>`

        - 
               .. image:: _static/BPMN_process/bmpn22.png
                :width: 300
                :align: center
      * - | **Форма задачи** определяет то, что будет отображено при назначении задачи пользователю.
          | Если какие-то задачи могут совпадать, то можно использовать одинаковую форму, но если различаются, то, соответственно, формы разные.
          | Можно создать форму заранее и выбрать ее из списка или создать непосредственно из списка выбора (см. ниже)

        - 
               .. image:: _static/BPMN_process/bmpn23.png
                :width: 300
                :align: center

      * - Выставить **приоритет задачи**, указать **результат задачи** – идентификатор и название.

        - 
               .. image:: _static/BPMN_process/bmpn24.png
                :width: 300
                :align: center

Создание формы:

 .. image:: _static/BPMN_process/bmpn25.png
       :width: 600
       :align: center

Создание формы аналогично описанным в разделе :ref:`«Кандидаты»<candidates>` , :ref:`«Оффер»<job_offer>` :

 .. image:: _static/BPMN_process/bmpn26.png
       :width: 600
       :align: center

:ref:`Подробно о формах для бизнес-процессов<user_task>`

Сохранение и публикация
------------------------

Созданный процесс сохраняем и публикуем:

 .. image:: _static/BPMN_process/bmpn27.png
       :width: 600
       :align: center

Настройка меню
-----------------

Для добавления процесса в меню **«Создать»**:
1.	Перейти в настройку меню, нажав на шестеренку, потом кнопку **«Настроить меню» справа сверху**.

 .. image:: _static/BPMN_process/bmpn28.png
       :width: 600
       :align: center

2.	Выбрать элемент меню, в котором будет находиться процесс. Навести на элемент и нажать кнопку **«Добавить»**, выбрать **«Запустить бизнес-процесс»**, из списка выбрать необходимый процесс, нажать **«Ok»**.

 .. image:: _static/BPMN_process/bmpn29.png
       :width: 400
       :align: center

|

 .. image:: _static/BPMN_process/bmpn30.png
       :width: 400
       :align: center

Выберите процесс:

 .. image:: _static/BPMN_process/bmpn31.png
       :width: 600
       :align: center

**Название** будет указано по умолчанию из бизнес-процесса, и может быть изменено:

 .. image:: _static/BPMN_process/bmpn32.png
       :width: 400
       :align: center

Добавленный пункт меню:

 .. image:: _static/BPMN_process/bmpn33.png
       :width: 250
       :align: center

Запуск задачи
--------------

 .. image:: _static/BPMN_process/bmpn34.png
       :width: 500
       :align: center

В системе можно ознакомиться с уже предустановленными бизнес-процессами:

 .. image:: _static/BPMN_process/bmpn35.png
       :width: 600
       :align: center

|

 .. image:: _static/BPMN_process/bmpn36.png
       :width: 600
       :align: center