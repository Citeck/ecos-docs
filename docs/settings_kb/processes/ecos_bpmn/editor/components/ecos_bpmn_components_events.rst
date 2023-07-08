События
=======

.. _bpmn_events:

**Событие** является одним из главных элементов BPMN и служит для описания того, что должно случиться (в отличие от задачи, когда что-то должно быть сделано). Событием может быть, например, подписание договора, или разговор с клиентом.

Графические элементы событий в BPMN классифицируют двумя способами:

1. В зависимости от положения события на схеме процесса:

.. list-table::
      :widths: 5 20
      :class: tight-table 
      
      * - 
  
          .. image:: _static/events/common_1.png
                :width: 50
                :align: center
 
        - Начальное событие (инициирующее бизнес-процесс)/ Start event
      * - 
  
          .. image:: _static/events/common_2.png
                :width: 50
                :align: center
 
        - Промежуточное событие / Intermediate Event
      * - 
  
          .. image:: _static/events/common_3.png
                :width: 50
                :align: center
 
        - Конечное событие (заканчивающее бизнес-процесс) / End event


1. По типу события:

.. list-table::
      :widths: 5 5 20
      :class: tight-table 
      
      * - 
  
          .. image:: _static/events/common_4.png
                :width: 50
                :align: center
 
        - Событие-таймер
        - | Используется для моделирования регулярных событий. 
          | Также таймер может использоваться для моделирования моментов времени, временных промежутков и превышения лимита времени.
      * - 
  
          .. image:: _static/events/common_5.png
                :width: 50
                :align: center
 
          .. image:: _static/events/common_6.png
                :width: 50
                :align: center

        - Событие-сигнал
        - | Обозначает ожидание или отправку сигнала между процессами, используется интеграция с :ref:`событиями ECOS <bpmn_events_integrations>`.
      * - 
  
          .. image:: _static/events/common_7.png
                :width: 50
                :align: center
 
        - Событие-условие
        - Используется для моделирования реакции бизнес-процесса на изменения условий. 
      * - 
  
          .. image:: _static/events/common_8.png
                :width: 50
                :align: center
 
        - Событие-останов
        - Вызывает немедленное завершение выполнения процесса, при этом все его активные потоки управления прерываются.  
      * - 
  
          .. image:: _static/events/common_9.png
                :width: 50
                :align: center

        - Событие-ошибка
        - Используется для моделирования возможных ошибок при выполнении процесса, а также для отображения последовательности действий по устранению этих ошибок.  


.. toctree::
    :maxdepth: 3

    events/ecos_bpmn_components_timer
    events/ecos_bpmn_components_signal
    events/ecos_bpmn_components_event_subprocess
    events/ecos_bpmn_components_conditional
    events/ecos_bpmn_components_termination
    events/ecos_bpmn_components_error
