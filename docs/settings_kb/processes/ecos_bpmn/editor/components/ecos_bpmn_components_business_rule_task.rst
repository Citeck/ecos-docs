Задача бизнес-правило
=======================

.. _business_rule_task:


Задача бизнес-правило служит для вызова :ref:`решения DMN<dmn_decision>` из процесса BPMN, используется для синхронного выполнения одного или нескольких правил.

Элемент выбирается следующим образом:

 .. image:: _static/business_rule_task/b_rule_1.png
       :width: 400
       :align: center

|

 .. image:: _static/business_rule_task/b_rule_2.png
       :width: 400
       :align: center

.. note::

      Выходной элемент решения, также называемый результатом решения, не сохраняется автоматически как переменная процесса. Он должен передаваться в переменную процесса с использованием предопределенного или пользовательского отображения результата решения. [прошу проверить]

.. list-table::
      :widths: 5 5
      :class: tight-table 

      * - Указать **Имя**
        - 
               .. image:: _static/business_rule_task/b_rule_3.png
                :width: 300
                :align: center

      * - Выбрать **Решение** из списка созданных:
        - 
               .. image:: _static/business_rule_task/b_rule_4.png
                :width: 300
                :align: center

      * - | Выбрать **Связь** с версией решения:
          | 
          |  **Опубликованное с процессом** - рассчитывается версия решения, которая была опубликована вместе с версией процесса.
          |  **Актуальное** - всегда последняя версия решения.
          |  **Версия** - позволяет указать конкретную версию решения.
          |  **Тег версии** - позволяет указать конкретную версию решения по тегу.
        - 
               .. image:: _static/business_rule_task/b_rule_5.png
                :width: 300
                :align: center

      * - Укажите **Переменную результата** из списка созданных:
        - 
               .. image:: _static/business_rule_task/b_rule_6.png
                :width: 300
                :align: center

      * - | Выберите **Сопоставление результата решения** из списка созданных:
          | 
          |  **Собрать все объекты (List<Object>)** - [пояснить]
          |  **Список результатов (List<Map<String, Object>>)** - [пояснить]
          |  **Один объект (TypedValue)** - [пояснить]
          |  **Один результат (Map<String, Object>)** - [пояснить]
        - 
               .. image:: _static/business_rule_task/b_rule_7.png
                :width: 300
                :align: center

      * - Настройки асинхронности, см. подробнее о `асинхронных задачах <https://camunda.com/blog/2014/07/advanced-asynchronous-continuations/>`_ 
        - 
               .. image:: _static/business_rule_task/b_rule_8.png
                :width: 300
                :align: center