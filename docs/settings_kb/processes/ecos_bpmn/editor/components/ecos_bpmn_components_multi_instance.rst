.. _multi_instance:

Multi instance
==============

.. contents::

**Multi Instance (многоэкземплярная активность)** — способ определения повторения определенного шага в бизнес-процессе.

В концепциях программирования мультиэкземпляр соответствует for each конструкции: он позволяет выполнять определенный шаг или даже полный подпроцесс для каждого элемента в данной коллекции, последовательно или параллельно.

Многоэкземплярная активность — обычное действие, для которого определены дополнительные свойства (так называемые multi-instance characteristics), которые заставляют действие выполняться несколько раз во время выполнения.

Следующие действия могут стать действиями с несколькими экземплярами:

* Пользовательская задача;
* Задача-сценарий;
* Подпроцесс.

В редакторе Multi Instance можно установить следующим образом:

.. image:: _static/multi_instance/93.png
   :width: 400
   :align: center

Sequential и Parallel Multi Instance
-------------------------------------

.. tab-set::

   .. tab-item:: Sequential Multi Instance

      .. image:: _static/multi_instance/45.png
         :width: 30
         :align: center

      **Sequential Multi Instance** — последовательная активность с несколькими экземплярами.

      Экземпляры выполняются друг за другом. Когда один экземпляр завершен, создается новый экземпляр для следующего элемента в ``inputCollection``.

      .. image:: _static/multi_instance/94.png
         :width: 300
         :align: center

   .. tab-item:: Parallel Multi Instance

      .. image:: _static/multi_instance/44.png
         :width: 30
         :align: center

      **Parallel Multi Instance** — параллельная активность с несколькими экземплярами.

      Все экземпляры создаются при активации тела активности с несколькими экземплярами. Экземпляры выполняются одновременно и независимо друг от друга.

      .. image:: _static/multi_instance/95.png
         :width: 300
         :align: center

Подробно о `Multi instance <https://docs.camunda.org/manual/7.8/reference/bpmn20/tasks/task-markers/#multiple-instance>`_.

Настройки
---------

Пользовательская задача
~~~~~~~~~~~~~~~~~~~~~~~~

Если выбрано parallel или sequential multi-instance, то задачи будут назначаться на **authority** из ролей — пользователи записываются в **assignee**, группы в **candidateGroup**.

При выставлении флага **«Ручное назначение»** появляется возможность указать реципиентов:

.. image:: _static/multi_instance/96.png
   :width: 300
   :align: center

Подробно :ref:`о реципиентах <user_task>`.

Общие настройки множественного экземпляра
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Настройки, аналогичные для **Пользовательской задачи**, :ref:`Скриптовой задачи <script_task>` и :ref:`Подпроцесса <sub_process>`:

.. image:: _static/multi_instance/97.png
   :width: 300
   :align: center

.. list-table::
   :widths: 5 20
   :class: tight-table
   :align: center

   * - **Количество повторений цикла / Loop cardinality**
     - Прямое указание числа экземпляров.
   * - **Условие завершения / Completion condition**
     - Выражение, которое вычисляется каждый раз, когда заканчивается один экземпляр.
   * - **Коллекция / Collection**
     - Коллекция, в которой экземпляр будет создан для каждого элемента.
   * - **Переменная элемента / Element variable**
     - Переменная процесса, которая будет установлена для каждого созданного экземпляра, содержащего элемент указанной коллекции.

Примеры использования
----------------------

Пользовательская задача
~~~~~~~~~~~~~~~~~~~~~~~~

Как в пользовательской задаче указать, что задачи должны идти параллельно на пользователей, указанных в переменной.

Используйте ``java.util.ArrayList()``:

.. image:: _static/multi_instance/user_task_01.png
   :width: 700
   :align: center

|

.. image:: _static/multi_instance/user_task_02.png
   :width: 700
   :align: center

|

.. image:: _static/multi_instance/user_task_03.png
   :width: 600
   :align: center
