.. _widgets:

Виджеты
==========================

**Виджеты** — настраиваемые блоки информации, которые размещаются на :ref:`дашбордах <dashboard>` и отображают данные о документе, задачах, процессах, пользователях и другом контенте системы.

Виджеты добавляются и переносятся перетаскиванием при настройке дашборда. Набор доступных виджетов зависит от типа дашборда. Для части виджетов доступна индивидуальная настройка отображаемых данных.

.. _widget_settings:

Для некоторых виджетов доступна настройка. Настройка отмечена следующей иконкой:

.. image:: _static/widgets/widget_1.png
       :width: 600
       :align: center

.. note::

  При включенном конфиге **restrict-access-to-edit-dashboard-widgets** (true) настройка виджетов запрещена пользователю.

**Настройка прав на редактирование**

В системе для пользователей можно разграничить права на настройку дашборда (**restrict-access-to-edit-dashboard**) и настройку виджетов (**restrict-access-to-edit-dashboard-widgets**).

То есть у пользователя могут быть права на настройку дашборда, но запрещена настройка виджетов.

Конфиги хранятся в разделе **Управление системой – Конфигурация ECOS** (``v2/journals?journalId=ecos-configs&viewMode=table&ws=admin$workspace``):

.. image:: _static/widgets/dashboards_widgets_settings.png
       :width: 700
       :align: center

Включение настройки:

.. image:: _static/widgets/dashboards_widgets_settings_1.png
       :width: 400
       :align: center

.. toctree::
   :maxdepth: 3

   widgets/activities
   widgets/tasks
   widgets/graphic_statistics
   widgets/birthdays
   widgets/record_actions
   widgets/gantt
   widgets/documents
   widgets/available_ws
   widgets/journal
   widgets/versions_journal
   widgets/events_history
   widgets/kanban
   widgets/comments
   widgets/knowledge_base
   widgets/current_tasks
   widgets/news
   widgets/preview
   widgets/user_profile
   widgets/publication
   widgets/doc_associations
   widgets/stages
   widgets/report
   widgets/process_statistics
   widgets/doc_status
   widgets/properties
   widgets/html
   widgets/web_page
   widgets/barcode
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
