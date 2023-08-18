Поток управления 
================

.. _sequential flow:

Поток управления используется для связи элементов потока BPMN (событий, процессов, шлюзов).

Поток управления отображает ход выполнения процесса. 

 .. image:: _static/seq_flow/92.png
       :width: 200
       :align: center

Далее ведите стрелку к необходимому элементу. 

Виды потоков управления:

.. list-table::
      :widths: 10 20 
      :align: center
      :class: tight-table 
 
      
      * - 
           
           .. image:: _static/seq_flow/normal_flow.png
              :width: 200
              :align: center 

        - | **Стандартный поток управления** относится к потокам, берущим начало от Стартового события и следующим по ходу выполнения процесса.   
      * - 
           
           .. image:: _static/seq_flow/default_flow.png
              :width: 200
              :align: center 


        - | **Поток управления по умолчанию** определяет ту ветвь бизнес-процесса, которая выполняется, когда все условия ветвления не выполнены. 
          | Этот поток может использоваться как совместно с эксклюзивным шлюзом, так и без него. 

Стандартный поток управления задается по умолчанию. Для изменения вида потока:

 .. image:: _static/seq_flow/flow_types.png
       :width: 400
       :align: center


Для потока можно указать тип условия. 
Условия могут иметь разные типы:

 .. image:: _static/seq_flow/64.png
       :width: 300
       :align: center

*	**Исходящий** (выход из задачи)
*	**Скрипт** - скрипт, который должен вернуть булевое значение. Например: pasymentSum >= 30000
*	**Выражение** – expression (`подробнее о expressions <https://docs.camunda.io/docs/components/concepts/expressions/>`_)

Например, для шлюза - **(2)** и **(3)**:

 .. image:: _static/seq_flow/63.png
       :width: 300
       :align: center

.. list-table::
      :widths: 5 5
      :align: center
      :class: tight-table 

      * - Для согласования:
        - Для отказа в согласовании:
      * - 
               .. image:: _static/seq_flow/65.png
                :width: 300
                :align: center

        - 
               .. image:: _static/seq_flow/66.png
                :width: 300
                :align: center
