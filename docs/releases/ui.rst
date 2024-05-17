UI
===

2.19
----

1. Обновлен функционал на :ref:`странице оргструктуры<org_structure>`.

2. Отображение KPI на схеме бизнес-процесса в виджете :ref:`«Статистика процесса»<widget_process_statistics_KPI>`.
   
3. Оптимизирована загрузка :ref:`открытых вкладок<ecos_tabs>`.
   
4. В настройке колонок агрегации реализована возможность :ref:`добавлять несколько колонок <additional_column>` с разными настройками фильтров и возможностью указать имя колонки.

2.18
----

1. В журналах :ref:`ширину колонки<column_width>` таблицы можно изменять и сохранять.

2. Добавлен новый форматтер :ref:`Duration<DurationFormatter>` , при включении которого, продолжительность будет трансформироваться в часы, то есть 2d 3h 30m = 51h 30m

3. К возможности выдавать ответ в виде ссылки на скачивания файла (использование config: implSourceId) только при выборе действия из журнала объектов, добавлена возможность аналогичного действия из :ref:`карточки объекта<mutate_action>`.

2.17
----

1. Добавлена возможность редактировать только `определенные поля в onlyoffice <https://citeck-ecos.readthedocs.io/ru/latest/general/transformation/transformation_service.html#onlyoffice>`_.

2. Добавлена возможность скачать zip-архив со всеми :ref:`загруженными файлами<widget_documents>`.

3. Для передачи в массив определенных данных выбранного журнала (ID журнала) можно использовать режим `Пользовательские значения <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/select%20journal.html#id4>`_.


2.16
----

1. Добавлены BPMN линтеры. `Отображение ошибок <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/editor/ecos_bpmn_editor.html#bpmn-linter>`_ на схеме бизнес-процесса 

2. Добавлена возможность `добавлять заголовок колонки в двух локализациях <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/table%20form.html#id3>`_ при ручном добавлении атрибутов в Table Form. 

3. Добавлена возможность `отображать только связанные записи <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id28>`_ в виджете «Канбан-доска» на дашборде. Доступно только для Enterprise версии.


2.15
----

1. Предоставление прав `разграничено <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/ecos_bpmn_overview.html#id2>`_ в рамках категорий бизнес-процессов/конкретных бизнес-процессов.

2. Для пользователей можно `разграничить права <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/dashboards.html#dashboard-config>`_ на настройку дашборда и настройку виджетов. 

3. Добавлен виджет «Графическая статистика». Виджет позволяет пользователям наглядно представлять и анализировать данные, повышая эффективность принятия решений и улучшая понимание текущего состояния бизнес-процессов. Доступно только для Enterprise версии. `О виджете «Графическая статистика» подробно <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id29>`_

4. Добавлена возможность `отображать только связанные записи <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id28>`_ в виджете «Канбан-доска» на дашборде. Доступно только для Enterprise версии.

5. Добавлена возможность `добавлять заголовок колонки <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/table%20form.html#id3>`_ в двух локализациях при ручном добавлении атрибутов в Table Form. 

