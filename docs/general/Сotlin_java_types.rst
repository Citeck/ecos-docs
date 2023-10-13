Типы данных в Kotlin/Java
=========================

Метод ObjectData set/add
-------------------------

``set`` - установить значение по ключу. Аналог метода put в Map

``add`` - добавить элемент к массиву. Сам по себе **ObjectData** является аналогом **Map** и для него **add** имеет мало смысла напрямую, но **add** первым аргументом может принимать путь до вложенного массива. 

Например:

.. code-block::

    ObjectData data = ObjectData.create();
    data.set("arr", new LinkedList<Object>());
    data.add("$.arr", "new-element");

Формат c **$** - стандарт JsonPath.

