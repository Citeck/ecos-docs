.. _process_bpmn:

BPMN Process Engine
===================

В качестве движка BPMN в ecos-process используется **Camunda 7**. В проверенной версии исходников ecos-process **2.38.0-SNAPSHOT** задана Camunda **7.24.0**. Движок работает с реляционной БД через JDBC; подробнее см. :ref:`архитектуру микросервиса <process_description>`.

.. toctree::
    :maxdepth: 3

    process_bpmn/process_bpmn_ecos_events_integrations
    process_bpmn/process_bpmn_unit_tests
