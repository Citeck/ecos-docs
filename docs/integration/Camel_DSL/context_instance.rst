.. _camel_instance:

Инстансы контекста Camel DSL
=============================================

Журнал содержит информацию о запущенных отдельных инстансах Camel контекста импорта данных.

Журнал доступен по адресу: ``v2/journals?journalId=ecos-camel-dsl&viewMode=table&ws=admin$workspace``

.. image:: _static/instances/instance_01.png
   :width: 700
   :align: center

Подробная информация об инстансе:

.. image:: _static/instances/instance_02.png
   :width: 600
   :align: center

Возможные состояния Camel DSL Instance:

.. list-table::
   :widths: 20 80
   :header-rows: 1
   :class: tight-table

   * - Состояние
     - Описание
   * - RUNNING
     - Контекст запущен и выполняется работа
   * - STOPPED
     - Контекст успешно выполнил работу и завершён
   * - ERROR
     - Во время выполнения произошла ошибка, контекст остановлен
