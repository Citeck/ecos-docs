Поток управления 
================

.. _sequential flow:

Поток управления используется для связи элементов потока BPMN (событий, процессов, шлюзов).

Поток управления отображает ход выполнения процесса. 

 .. image:: _static/92.png
       :width: 200
       :align: center

Далее ведите стрелку к необходимому элементу. Для потока можно указать тип условия.

Условия могут иметь разные типы:

 .. image:: _static/64.png
       :width: 300
       :align: center

*	Исходящий (выход из задачи)
*	Скрипт - скрипт, который должен вернуть булевое значение. Например: pasymentSum >= 30000
*	Выражение – expression (`подробнее о expressions <https://docs.camunda.io/docs/components/concepts/expressions/>`_)

Например, для шлюза - **(2)** и **(3)**:

 .. image:: _static/63.png
       :width: 300
       :align: center

.. list-table::
      :widths: 5 5
      :align: center
      :class: tight-table 

      * - Для согласования:
        - Для отказа в согласовании:
      * - 
               .. image:: _static/65.png
                :width: 300
                :align: center

        - 
               .. image:: _static/66.png
                :width: 300
                :align: center
