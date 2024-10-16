Процесс запроса на закупку оборудования. Добавление событий BPMN
=================================================================

.. contents::
	:depth: 3

.. note::

    Данная статья является продолжением работы с созданным ранее бизнес-процессом :ref:`Запрос на закупку оборудования<sample_request_dmn_demo>` 

     Для редактирования бизнес-процесса используйте следующие учетные данные:

        * Заместитель генерального директора по цифровизации — Валентина Вассерман (**valentina.wasserman**)

        * Начальник отдела цифровизации бизнес-процессов —  Георгий Цезарев (**georgy.tsezarev**)

        * Специалист отдела цифровизации бизнес-процессов —  Ирина Васнецова (**irina.vasnetsova**)


Добавим в созданный бизнес-процесс :ref:`события<bpmn_events>`:

    1. :ref:`Сигнал<ecos_bpmn_events>`, который запустит отдельный процесс отправки уведомления согласующему после получения заявкой статуса «На согласовании». 
    2. :ref:`Таймер»<ecos_bpmn_timer>`. Если согласующий не согласовал заявку в течение 30 минут, то она автоматически перейдет в статус «Отказано».


.. image:: _static/equipment_request_events_demo/01.png
       :width: 600
       :align: center

Сигнал
--------

Между компонентами **Статус «На согласовании»** и **Пользовательская задача «На согласовании согласующим»** необходимо добавить промежуточное событие :ref:`«Сигнал»<ecos_bpmn_events>`

.. image:: _static/equipment_request_events_demo/event_01.png
       :width: 600
       :align: center

Далее выбрать его тип **Signal Intermediate Throw event**:

.. image:: _static/equipment_request_events_demo/event_02.png
       :width: 600
       :align: center

Укажите свойства события:

    •	Имя - **Отправить уведомление**
    •	Имя сигнала - **sendEmail**,
    •	Фильтр события по документу – **Текущий документ**

.. image:: _static/equipment_request_events_demo/event_03.png
       :width: 600
       :align: center

И далее добавьте :ref:`событийный подпроцесс «Сигнал»<event_subprocess>` - подпроцесс, запускаемый событием. Для создания событийного подпроцесса создайте сначала стандартный подпроцесс. И далее выберите **Event Sub Process**:

.. image:: _static/equipment_request_events_demo/event_04.png
       :width: 600
       :align: center

В подпроцессе измените **Start event** на **Signal Start event (non-interrupting)**:

.. image:: _static/equipment_request_events_demo/event_05.png
       :width: 600
       :align: center

Со следующими свойствами:

    •	Чекбокс **Ручная настройка**
    •	Имя сигнала – **sendEmail** 
    •	Фильтр события по документу – **Текущий документ**

.. image:: _static/equipment_request_events_demo/event_06.png
       :width: 600
       :align: center

К начальному событию добавьте компонент :ref:`Уведомление<notification>`:

.. image:: _static/equipment_request_events_demo/event_07.png
       :width: 600
       :align: center

со следующими свойствами:

    •	Имя – **Уведомление согласующему**
    •	Заголовок – **Согласуйте заявку**
    •	Тело сообщения – **Согласуйте заявку на покупку оборудования**
    •	Кому – **Согласующий**

.. image:: _static/equipment_request_events_demo/event_08.png
       :width: 600
       :align: center

Добавьте **End Event** компонент **(1)**:

.. image:: _static/equipment_request_events_demo/event_09.png
       :width: 600
       :align: center

**Опубликуйте** бизнес-процесс **(2)**.


Таймер
--------

К компоненту **Пользовательская задача «На согласовании согласующим»** необходимо добавить промежуточное событие :ref:`«Таймер»<ecos_bpmn_timer>`:

.. image:: _static/equipment_request_events_demo/timer_01.png
       :width: 600
       :align: center

Далее перенесите событие на компонент **Пользовательская задача «На согласовании согласующим»**:

.. image:: _static/equipment_request_events_demo/timer_02.png
       :width: 600
       :align: center

Выберите **Timer Boundary Event**:

.. image:: _static/equipment_request_events_demo/timer_03.png
       :width: 600
       :align: center

Укажите свойства события:

       • Тип – **Дата**
       • Значение – **PT30M** В формате ISO 8601 **PT30M - 30 минут**. Подробно о :ref:`формате<time_format>`

.. image:: _static/equipment_request_events_demo/timer_04.png
       :width: 600
       :align: center

Поток от таймера отведите к **gateway (1)**:

.. image:: _static/equipment_request_events_demo/timer_05.png
       :width: 600
       :align: center

**Опубликуйте** бизнес-процесс **(2)**.

Для проверки создайте заявку, чтобы процесс пошел по ветке с согласованием сотрудником. Для этого укажите любое другое название оборудования, не указанное в таблице, или укажите:

    •	Название оборудование – **Ноутбук**
    •	Стоимость - **65000**
    •	Инициатор – **текущий пользователь**
    •	Согласующий – **любой пользователь, у которого в профиле указан электронный адрес.**

Когда процесс дойдет до согласования согласующим, не выносите решение по задаче – через 30 минут заявка будет автоматически переведена в статус **«Отказано»**.

Весь процесс финально:

.. image:: _static/equipment_request_events_demo/02.png
       :width: 600
       :align: center