Установка статуса
=================

.. _set_status:

Уникальный для Citeck элемент, отмеченный как:

 .. image:: _static/set_status/86.png
       :width: 200
       :align: center

Элемент позволяет производить смену статуса в создаваемом бизнес-процессе.

Атрибуты и форма
----------------

 .. image:: _static/set_status/87.png
       :width: 200
       :align: center

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Укажите **Имя** и выберите **Статус** из списка статусов, заполненных в :ref:`Citeck типе данных<roles_statuses>`

        - 
               .. image:: _static/set_status/88.png
                :width: 300
                :align: center

.. important::

  При сохранении, сохранении/публикации процесса проверяется обязательность заполнения следующих полей:

   - **«Статус»**

  Иначе в :ref:`линтере<bpmn_linter>` будет выдана ошибка.  