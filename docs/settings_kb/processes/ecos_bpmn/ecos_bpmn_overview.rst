Общее описание ECOS BPMN
========================

.. _ecos_bpmn:

Платформа основана на библиотеке редактора `bpmn-js <https://bpmn.io/>`_ и движка `camunda <https://camunda.com/>`_.

 .. image:: _static/01.png
       :width: 600
       :align: center

Права на описание процессов
----------------------------

Предоставление прав разграничено в рамках категорий бизнес-проессов/конкретных бизнес-проессов.

.. list-table::
      :widths: 10 20 10 10 10 10
      :header-rows: 1
      :class: tight-table 
      
      * - Право / Роль
        - Описание
        - Администратор БП
        - Менеджер БП
        - Разработчик БП
        - Читатель БП
      * - Создание / Редактирование
        - Создание и редактирование моделей БП
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center
      * - Просмотр
        - Просмотр моделей БП
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center
      * - Публикация
        - Публикация моделей БП
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center
      * - Запуск
        - Ручной запуск инстансов БП
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center
      * - Просмотр отчетности
        - Статистика БП + планируемый функционал отчетности 
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center
      * - Редактирование инстанса процесса
        - Админка camunda + excamad
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center
        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center
      * - Миграция БП
        - Планируемый функционал ECOS миграции БП
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center
        -
            .. image:: _static/plus.png
                  :width: 10
                  :align: center

        -
            .. image:: _static/minus.png
                  :width: 10
                  :align: center

Роли назначаются на соответствующие группы.

1. Раздел «Моделирование» с редакторами DMN/BPMN, раздел доступен для пользователей с правом **Просмотр**

 .. image:: _static/rights_1.png
       :width: 200
       :align: center

2. В редакторах DMN/BPMN публикация моделей доступна только для пользователей с правом **Публикация**

 .. image:: _static/rights_2.png
       :width: 600
       :align: center

|

 .. image:: _static/rights_3.png
       :width: 600
       :align: center

Право на деплой можно проверить запросом ``permissions._has.deploy?bool``

Например:

.. code-block::

      Citeck.Records.get('eproc/bpmn-def@you-process').load("permissions._has.deploy?bool", true).then(res => console.log(res))

3.	Добавлена возможность просмотра схемы БП для пользователей с правом с правом **Просмотр**

 .. image:: _static/rights_4.png
       :width: 600
       :align: center

|

 .. image:: _static/rights_5.png
       :width: 600
       :align: center

4.	Добавлен просмотр отчетности для ролей с правом **Просмотр отчетности**. Под отчетностью понимаем виджет «Статистика по процессу».

Право на деплой можно проверить запросом ``permissions._has.viewReports?bool``

Например:

.. code-block::

      Citeck.Records.get('eproc/bpmn-def@you-process').load("permissions._has.viewReports?bool", true).then(res => console.log(res))

.. image:: _static/rights_6.png
       :width: 600
       :align: center

Настройка просмотра доступна только пользователям из группы администраторы ECOS.

 .. image:: _static/rights_7.png
       :width: 600
       :align: center

О виджете см. :ref:`подробно<widget_process_statistics>`