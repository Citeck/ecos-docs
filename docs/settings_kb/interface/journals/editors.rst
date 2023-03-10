.. _editors:

Редакторы
==========

.. contents:: Содержание
   :depth: 3

перейти в раздел администрирования > :guilabel:`Журналы` > найти необходимый журнал > действие :guilabel:`Редактировать`. Перейти в :guilabel:`Дополнительно`

.. list-table:: 
      :widths: 40
      :align: center

      * - |

             .. image:: _static/editor/editor_1.png
                 :width: 500   
                 :align: center

          | 

             .. image:: _static/editor/editor_2.png
                  :width: 500 
                  :align: center  


Типы
---------

BooleanEditor
~~~~~~~~~~~~~~~~~~

Тип: ``boolean``

.. list-table:: 
      :widths: 5 40 40
      :header-rows: 1

      * - Ключ
        - Значение
        - По умолчанию
      * - **mode**
        - |
          | режим редактора ``select`` 

             .. image:: _static/editor/editor_3.png
                 :width: 200   

          | ``checkbox``

             .. image:: _static/editor/editor_4.png
                  :width: 200   

        - ``select``         

DateEditor
~~~~~~~~~~~~~~~~~~

Тип: ``date``

DateTimeEditor
~~~~~~~~~~~~~~~~~~

Тип: ``datetime``

JournalEditor
~~~~~~~~~~~~~~~~~~

Тип: ``journal``

.. list-table:: 
      :widths: 5 40 40
      :header-rows: 1

      * - Ключ
        - Значение
        - По умолчанию
      * - **journalId**
        - идентификатор журнала
        - 

NumberEditor
~~~~~~~~~~~~~~~~~~

Тип: ``number``

OrgstructEditor
~~~~~~~~~~~~~~~~~~

Тип: ``orgstruct``

Конфигурация:

.. list-table:: 
      :widths: 5 40 40
      :header-rows: 1

      * - Ключ
        - Значение
        - По умолчанию
      * - **allowedAuthorityTypes**
        - строка вариантов: ``GROUP`` , ``USER``
        - 
      * - **multiple**
        - множественный выбор boolean
        - false
  
SelectEditor
~~~~~~~~~~~~~~~~~~

Тип: ``select``

Конфигурация:

можно задавать статические варианты или получаемые используя ``recordRef + attribute`` записи и параметр ``optionsAtt``

.. list-table:: 
      :widths: 5 40 40
      :header-rows: 1

      * - Ключ
        - Значение
        - По умолчанию
      * - **options**
        - | json-строка вариантов
          | пр. ``[{"label":"priority.high","value":1},``
          | ``{"label":"priority.low","value":3},``
          | ``{"label":"priority.medium","value":2}]``
        -  
      * - **optionsAtt**
        - 	пр. `_edge.${attribute}.options{value:?str,label:?disp}`
        - `_edge.${attribute}.options{value:?str,label:?disp}`

TextEditor
~~~~~~~~~~~~~~~~~~

Тип: ``text``