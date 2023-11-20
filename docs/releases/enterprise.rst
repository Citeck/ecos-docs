Enterprise
===========

4.8.0
-------

1. Добавлена поддержка `серверных групповых действий <https://citeck-ecos.readthedocs.io/ru/latest/general/Group_actions.html>`_


4.7.0
-------

1. Реализован `микросервис <https://citeck-ecos.readthedocs.io/ru/latest/general/Content_microservice.html>`_ , предназначенный для обеспечения хранения файлов в системе в определенное файловое хранилище. 

2. Логика ЭДО вынесена в `отдельный микросервис <https://citeck-ecos.readthedocs.io/ru/latest/general/EDI_microservice.html>`_


4.5.0
-------

1.	Открыты публичные доступы к enterprise модулям. Доступны по `ссылке <https://github.com/orgs/Citeck/repositories>`_ 

2.	Добавлена возможность пользователю делегировать свои полномочия на время отсутствия. Подробнее описано в статье `Делегирование <delegation>`_ 

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

4.	Сервис трансформации. Генерация `контента из шаблона <https://citeck-ecos.readthedocs.io/ru/latest/general/transformation/transformation_service.html#id11>`_ 

4.1.0
------

1.	Виджет «Стадии». Разработан новый виджет, который визуализирует прохождение ECOS стадий документа. Подробнее описано в статье `Виджет «Стадии» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html?highlight=heatmap#widget-stages>`_

4.0.0
-------

1.	Виджет «Статистика процесса». Виджет визуализирует статистику по бизнес-процессу с отображением тепловой карты (heatmap). Подробнее описано в статье `Виджет «Статистика процесса» <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#widget-process-statistics>`_

2.	Микросервис ecos-transformations. Микросервис для генерации документов по шаблонам, которые можно подгрузить с проектом или добавить через инструменты администратора. Подробнее описано в статье `Микросервис Трансформации <https://citeck-ecos.readthedocs.io/ru/latest/general/%D0%93%D0%B5%D0%BD%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D1%8F%20%D0%B4%D0%BE%D0%BA%D1%83%D0%BC%D0%B5%D0%BD%D1%82%D0%BE%D0%B2.html>`_

3.	Механизм лицензирования. Подробнее о `добавлении лицензии <https://citeck-ecos.readthedocs.io/ru/latest/admin/license.html>`_

