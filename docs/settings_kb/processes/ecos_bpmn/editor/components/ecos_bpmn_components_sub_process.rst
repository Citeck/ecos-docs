Подпроцесс
==========

.. _sub_process:

**Подпроцесс BPMN** – действие, которое может включать в себя: другие действия, шлюзы, события и потоки операций.

 .. image:: _static/sub_process/71.png
       :width: 300
       :align: center

**Sub Process (collapsed)** – свернутый подпроцесс. Процесс создается в новом окне редактора по стрелке:

 .. image:: _static/sub_process/72.png
       :width: 200
       :align: center

 .. image:: _static/sub_process/73.png
       :width: 600
       :align: center

**Sub Process (expanded)** – подпроцесс, который отражается на основном окне редактора:

 .. image:: _static/sub_process/74.png
       :width: 300
       :align: center

Атрибуты
--------

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/sub_process/75.png
                :width: 300
                :align: center

      * - | Асинхронность можно настроить ко многим элементам. 
          | `См. подробнее  <https://camunda.com/blog/2014/07/advanced-asynchronous-continuations/>`_ 
        - 
               .. image:: _static/sub_process/77.png
                :width: 300
                :align: center

Создание элементов подпроцесса аналогично описанным в разделе :ref:`Компоненты Ecos BPMN<ecos_bpmn_components>`.