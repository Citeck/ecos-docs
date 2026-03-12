Выборка из БД
==========================

Для выборки данных из БД необходимо:

1. Создать **«Credentials»** для подключения.

   Перейти в журнал **«Credentials»** (Рабочее пространство «Раздел администратора» → Интеграция):

   .. image:: _static/BD_selection/Camel_3.png
      :width: 800
      :align: center

   .. image:: _static/BD_selection/Camel_3_1.png
      :width: 600
      :align: center

2. Создать **«Источник данных»** DB Data Source — источник будет создан с типом ``db``.

   Перейти в журнал **«Источники данных»** (Рабочее пространство «Раздел администратора» → Интеграция):

   .. image:: _static/BD_selection/Camel_4.png
      :width: 800
      :align: center

   .. image:: _static/BD_selection/Camel_5.png
      :width: 600
      :align: center

3. Создать **«Camel DSL»**.

   Перейти в журнал **«Camel DSL»** (Рабочее пространство «Раздел администратора» → Интеграция):

   .. image:: _static/BD_selection/Camel_6.png
      :width: 800
      :align: center

   .. image:: _static/BD_selection/Camel_6_1.png
      :width: 600
      :align: center

   Контекст Camel DSL должен содержать маршрут выборки из БД. Например:

   .. code-block:: yaml

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
                     - to: "stream:out"

   где:

   * **datasource** — имя источника данных, созданного в п. 2; при использовании в маршруте необходимо добавлять префикс **«jdbc:»**;
   * **actions** — имя таблицы БД, из которой делается выборка;
   * **timer** — таймер, запускающий маршрут: ``delay=-1`` — немедленно при старте контекста, ``repeatCount=1`` — только один раз;
   * **блок split** — разделяет результат выборки на строки, которые выводятся в трассу ``stream:out``.

4. Для выполнения содержимого контекста изменить состояние Camel DSL на **Started**.
