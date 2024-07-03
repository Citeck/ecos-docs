Enterprise
===========

2024.7
-------

1. BPMN редактор. Для :ref:`пользовательской задачи<user_task>` добавлен функционал :ref:`Lazy approval<user_task_lazy_approval>`, позволяющий принимать решения из электронной почты, не заходя в Citeck.
   
2. Добавлен функционал :ref:`портала технической поддержки<portal_sd>`, на котором доступно:

       * создание заявок,
       * отслеживание статуса текущих заявок,
       * просмотр истории, комментариев и вложений закрытых заявок,
       * общение через комментарии и обмен файлами со специалистами технической поддержки.

2024.4
-------

1. Отображение KPI на схеме бизнес-процесса в виджете :ref:`«Статистика процесса»<widget_process_statistics_KPI>`.

2. Отображение % экземпляров процессов :ref:`на разветвлениях <widget_process_statistics_extended>` в модели процессов . Расчет % ведется от общего числа экземпляров, прошедших шлюз.

3. В библиотеку ecos-camel добавлен компонент ecos-records-delete для возможности удаления сущностей через роутинг camel.
   
4. Добавлена возможность :ref:`импорта данных<Excel-import>` из Excel в Citeck.

4.9.0
-----

1. `Рабочее расписание и производственный календарь <https://citeck-ecos.readthedocs.io/ru/latest/introduction/functions/work_calendar.html>`_ - функциональность для учета нерабочих, праздничных дней сотрудников, которая позволяют более гибко настраивать рабочий процесс сотрудников в различных модулях системы. 

2. `KPI <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/processes/ecos_bpmn/ecos_bpmn_kpi.html>`_ - функционал для настройки норм времени:
  
  - KPI по продолжительности позволяет отслеживать время между указанными BPMN элементами (Исходный и Целевой) в процессе. 
  - KPI по количеству позволяет считать количество прохождения через указанный элемент.    

4.8.0
-------

1. Добавлена поддержка `серверных групповых действий <https://citeck-ecos.readthedocs.io/ru/latest/general/Group_actions.html>`_.

2. В модулях **ОРД, Исходящие документы** добавлена возможность :ref:`подписания с использованием ЭЦП <esign>`.

4.7.0
-------

1. Реализован `микросервис <https://citeck-ecos.readthedocs.io/ru/latest/general/Content_microservice.html>`_ , предназначенный для обеспечения хранения файлов в системе в определенное файловое хранилище. 

2. Логика ЭДО вынесена в `отдельный микросервис <https://citeck-ecos.readthedocs.io/ru/latest/general/EDI_microservice.html>`_


4.5.0
-------

1.	Открыты публичные доступы к enterprise модулям. Доступны по `ссылке <https://github.com/orgs/Citeck/repositories>`_ 

2.	Добавлена возможность пользователю делегировать свои полномочия на время отсутствия. Подробнее описано в статье `Делегирование <https://citeck-ecos.readthedocs.io/ru/latest/introduction/delegation.html>`_ 

3.	Настройка выбора положения штрихкода. См. `Пример: Настройка действия Скачать c штрихкод <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/ui_actions.html#c>`_  

4.  Виджет «Графическая статистика». Виджет позволяет пользователям наглядно представлять и анализировать данные, повышая эффективность принятия решений и улучшая понимание текущего состояния бизнес-процессов. `О виджете «Графическая статистика» подробно <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id29>`_

4.4.0
------

1.	Виджет «Канбан». Виджет добавляет в карточку канбан доску с настраиваемым журналом, связанным атрибутам и шаблонами для удобства пользователя и быстрым взаимодействием со статусами через карточку. Подробнее описано в статье `Виджет «Канбан» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id28>`_ 

4.3.0
------

1.	Добавлен новый тип синхронизации пользователей в ecos-model - `LDAP синхронизация <https://citeck-ecos.readthedocs.io/ru/latest/admin/sync_authorities.html>`_ 

2.	Возможность `формировать PDF-файла со штрихкодом <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/barcode.html>`_

3.	Сервис трансформации. Добавлена `возможность конвертации всех офисных форматов в PDF <https://citeck-ecos.readthedocs.io/ru/latest/general/Preview/Content_transformation.html>`_ 

4.	Сервис трансформации. Генерация `контента из шаблона <https://citeck-ecos.readthedocs.io/ru/latest/general/Transformations_microservice.html#id12>`_ 

4.1.0
------

1.	Виджет «Стадии». Разработан новый виджет, который визуализирует прохождение ECOS стадий документа. Подробнее описано в статье `Виджет «Стадии» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html?highlight=heatmap#widget-stages>`_

4.0.0
-------

1.	Виджет «Статистика процесса». Виджет визуализирует статистику по бизнес-процессу с отображением тепловой карты (heatmap). Подробнее описано в статье `Виджет «Статистика процесса» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#widget-process-statistics>`_

2.	Микросервис ecos-transformations. Микросервис для генерации документов по шаблонам, которые можно подгрузить с проектом или добавить через инструменты администратора. Подробнее описано в статье `Микросервис Трансформации <https://citeck-ecos.readthedocs.io/ru/latest/general/Transformations_microservice.html>`_

3.	Механизм лицензирования. Подробнее о `добавлении лицензии <https://citeck-ecos.readthedocs.io/ru/latest/admin/license.html>`_

