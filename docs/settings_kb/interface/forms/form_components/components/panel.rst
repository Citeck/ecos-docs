.. _panel_component:

Panel
======

Во вкладке **Вид (View)** в поле **Название свойства (Property Name)**, можно вывести значение из любого компонента, находящегося внутри этой панели.
Используются вставки вида ``${…}``. 

Например: ``${someField}``

 .. image:: _static/panel/panel_header_1.png
       :width: 600
       :align: center

В данном примере в название панели будет выведено ФИО контактного лица.

 .. image:: _static/panel/panel_header_2.png
       :width: 600
       :align: center

Также мы можем изменить цвет самой панели. Для этого необходимо добавить нужный класс Bootstrap ``instance.element.classList.add("panel-info");``.

Например по какой-то логике добавить действие:

 .. image:: _static/panel/panel_header_3.png
       :width: 400
       :align: center

В данном примере цвет панели будет меняться на ``panel-info``, если чекбокс **Завершена** активен:

 .. image:: _static/panel/panel_header_4.png
       :width: 500
       :align: center