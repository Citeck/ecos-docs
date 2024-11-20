Соединение элементов
=====================

.. _dmn_connectors:

.. list-table::
      :widths: 20 30 20 
      :align: center
      :class: tight-table 
      
      * - **Требование к информации**
        - Требование к информации обозначает входные данные или результат решения, которые используются в качестве одного из входов решения.
        -
            
            .. image:: _static/connectors/connector_1.png
                  :width: 100
                  :align: center

      * - **Требование к знаниям**
        - Требование к знаниям обозначает вызов модели бизнес-знаний с помощью логики решения.
        -
            
            .. image:: _static/connectors/connector_2.png
                  :width: 100
                  :align: center

      * - **Требование к полномочиям**
        - Требование к полномочиям обозначает зависимость элемента модели принятия решений от другого элемента , который выступает в качестве источника руководства или знаний.
        -
            
            .. image:: _static/connectors/connector_3.png
                  :width: 100
                  :align: center

Правила соединения элементов:

.. list-table::
      :widths: 20 20 20 20 
      :header-rows: 1
      :align: center
      :class: tight-table 
      
      * - Выходит от
        - Идет к
        - Требование
        - Отображение на схеме

      * - Решение
        - Решение
        - Информация
        -
            
            .. image:: _static/connectors/01.png
                  :width: 200
                  :align: center

      * - Решение
        - Источник знания
        - Полномочия
        -
            
            .. image:: _static/connectors/02.png
                  :width: 200
                  :align: center

      * - Модель бизнес-знаний
        - Решение
        - Знание
        -
            
            .. image:: _static/connectors/03.png
                  :width: 200
                  :align: center

      * - Модель бизнес-знаний
        - Модель бизнес-знаний
        - Знание
        -
            
            .. image:: _static/connectors/04.png
                  :width: 200
                  :align: center

      * - Входные данные
        - Решение
        - Информация
        -
            
            .. image:: _static/connectors/05.png
                  :width: 200
                  :align: center

      * - Входные данные
        - Источник знания
        - Полномочия
        -
            
            .. image:: _static/connectors/06.png
                  :width: 200
                  :align: center

      * - Источник знания
        - Решение
        - Полномочия
        -
            
            .. image:: _static/connectors/07.png
                  :width: 200
                  :align: center

      * - Источник знания
        - Модель бизнес-знаний
        - Полномочия
        -
            
            .. image:: _static/connectors/08.png
                  :width: 200
                  :align: center

      * - Источник знания
        - Источник знания
        - Полномочия
        -
            
            .. image:: _static/connectors/09.png
                  :width: 200
                  :align: center