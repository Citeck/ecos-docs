Страница администратора
=======================

Общее описание
--------------

Страница администратора предоставляет централизованный интерфейс управления системой ECOS.
Она разделена на группы разделов, каждая из которых соответствует отдельному микросервису и содержит ссылки на журналы, бизнес-процессы и инструменты разработчика.

Доступ к странице администратора требует наличия роли ``ROLE_ADMIN``.

Настройка разделов меню администратора
---------------------------------------

Для настройки разделов меню администратора предусмотрены артефакты с типом **ui/admin-sections-group**, каждый из которых представляет собой группу разделов в меню.

Каждый микросервис может добавлять свою группу разделов (или несколько групп) при запуске.
Для модификации существующих групп используются патчи для артефактов.

Типы разделов
~~~~~~~~~~~~~

.. csv-table::
   :header-rows: 1

   Тип,Параметры,Описание
   JOURNAL,"journalId — идентификатор журнала",Раздел с журналом
   BPM,—,Раздел с бизнес-процессами в виде плитки или списка
   DEV_TOOLS,—,Страница инструментов разработчика (dev-tools)

Стандартные группы разделов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. csv-table::
   :header-rows: 1

   Микросервис,Идентификатор группы,Порядок
   ecos-apps,application,0
   ecos-process,process,10
   ecos-model,model,20
   ecos-uiserv,user-interface,30
   ecos-notifications,notification,40
   ecos-integrations,integration,50
   ecos-integrations,integration-legacy,1000

.. note::

   Группа ``integration-legacy`` содержит устаревшие журналы микросервиса ``ecos-integrations`` (``ecos-sync``, ``ecos-credentials``, ``edi-box``, ``ecos-osgi-bundles``, ``file-import-config``, ``file-import-task``, ``file-import-task-item``).
   Значение ``order: 1000`` намеренно выбрано большим, чтобы группа отображалась в конце боковой панели после всех остальных разделов. Это рекомендуемое соглашение для групп с устаревшим/legacy-содержимым.

Модель группы разделов
~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: typescript

   AdminSectionsGroupDef {
       id: String       // идентификатор группы (должен быть неизменным)
       name: MLText     // локализованное имя группы
       order: Float     // порядок в меню (чем больше, тем ниже)
       sections: List<AdminSectionDef>  // список разделов
   }

Модель раздела
~~~~~~~~~~~~~~

.. code-block:: typescript

   AdminSectionDef {
       name: MLText     // имя раздела (необязательно для типа JOURNAL)
       type: String     // тип раздела: JOURNAL | BPM | DEV_TOOLS
       config: ObjectData  // конфигурация, зависящая от типа раздела
   }

Пример конфигурации группы
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: json

   {
     "id": "user-interface",
     "name": {
       "en": "UI configuration",
       "ru": "Конфигурация UI"
     },
     "order": 30,
     "sections": [
       {
         "type": "JOURNAL",
         "config": {
           "journalId": "ecos-journals"
         }
       },
       {
         "type": "JOURNAL",
         "config": {
           "journalId": "ecos-forms"
         }
       }
     ]
   }

Пример патча: добавление нового раздела в группу
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для добавления раздела в существующую группу без изменения её базовой конфигурации используется патч типа ``json``:

.. code-block:: yaml

   id: add-some-journal-to-admin-page

   name:
     ru: Добавить журнал "Some Journal" на страницу администратора
     en: Add journal "Some Journal" to admin page

   target: ui/admin-sections-group$application

   type: json
   config:
     operations:
       - op: add
         path: '$.sections'
         value:
           type: JOURNAL
           config:
             journalId: some-journal-id

Паттерн: выделение устаревших разделов в Legacy-группу
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Если в группе разделов накопились журналы, которые больше не используются активно, рекомендуется переместить их в отдельную группу с суффиксом ``-legacy``.
Это позволяет сохранить доступ к устаревшим данным, не перегружая основной раздел.

Соглашения:

* Идентификатор группы: ``<исходная-группа>-legacy`` (например, ``integration-legacy``).
* Название: ``{ "en": "Legacy", "ru": "Устаревшее" }`` — использование единообразного имени упрощает навигацию.
* Значение ``order``: выбирайте большое число (например, ``1000``), чтобы группа всегда отображалась в конце боковой панели.
* Оба файла (основная группа и legacy-группа) деплоятся атомарно в рамках одного приложения — риска частичного состояния нет.
* Прямые ссылки на журналы продолжают работать после переноса, так как маршрутизация ведётся по ``journalId``, а не по группе разделов.

Пример файла ``integration-legacy.json``:

.. code-block:: json

   {
     "id": "integration-legacy",
     "name": {
       "en": "Legacy",
       "ru": "Устаревшее"
     },
     "order": 1000,
     "sections": [
       { "type": "JOURNAL", "config": { "journalId": "ecos-sync" } },
       { "type": "JOURNAL", "config": { "journalId": "ecos-credentials" } },
       { "type": "JOURNAL", "config": { "journalId": "edi-box" } },
       { "type": "JOURNAL", "config": { "journalId": "ecos-osgi-bundles" } },
       { "type": "JOURNAL", "config": { "journalId": "file-import-config" } },
       { "type": "JOURNAL", "config": { "journalId": "file-import-task" } },
       { "type": "JOURNAL", "config": { "journalId": "file-import-task-item" } }
     ]
   }

.. note::

   При разбиении группы убедитесь, что суммарное количество журналов во всех результирующих файлах совпадает с исходным.
   Это позволяет избежать потери или дублирования журналов.
