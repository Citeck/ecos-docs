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
      :align: center
      :class: tight-table 

      * - Указать **Имя**

        - 
               .. image:: _static/sub_process/75.png
                :width: 300
                :align: center

      * - | Настройки асинхронности: 
          |  - **Асинхронно "перед"**- исполнение доходит до точки перед блоком, транзакция комитится и дальнейшее выполнение ставится в очередь, которую разбирает уже джоба
          |  - **Асинхронно "после"** - исполнение доходит до точки после блока, транзакция комитится и дальнейшее выполнение ставится в очередь, которую разбирает уже джоба
          | См. подробнее о `асинхронных задачах <https://camunda.com/blog/2014/07/advanced-asynchronous-continuations/>`_  
        - 
               .. image:: _static/sub_process/77.png
                :width: 300
                :align: center

Создание элементов подпроцесса аналогично описанным в разделе :ref:`Компоненты Citeck BPMN<ecos_bpmn_components>`.