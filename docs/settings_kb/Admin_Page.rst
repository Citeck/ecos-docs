Страница администратора
=======================

Общее описание
--------------

Страница администратора предоставляет централизованный интерфейс управления системой.
Она разделена на группы разделов, каждая из которых соответствует отдельному микросервису и содержит ссылки на журналы, бизнес-процессы и инструменты разработчика.

Доступ к странице администратора требует наличия роли ``ROLE_ADMIN``.

Настройка разделов меню администратора
---------------------------------------

Для настройки разделов меню администратора существуют два типа артефактов. Важно использовать правильный механизм:

.. list-table::
   :header-rows: 1
   :widths: 25 30 15

   * - Тип артефакта
     - Путь
     - Статус
   * - ``ui/admin-sections-group``
     - ``artifacts/ui/admin-sections-group/*.json``
     - **Устарел** — не влияет на меню администратора в актуальных версиях платформы
   * - ``app/artifact-patch``
     - ``artifacts/app/artifact-patch/*.yml``
     - **Актуален** — правильный механизм для изменения меню администратора

.. warning::

   Артефакты типа ``ui/admin-sections-group`` **не оказывают эффекта** на меню администратора в текущих версиях платформы.
   Для изменения структуры меню администратора необходимо использовать ``app/artifact-patch`` с целевым артефактом ``ui/menu$admin-workspace-menu``.
   Подробнее см. раздел `Настройка через artifact-patch (актуальный механизм)`_ ниже.

Настройка через artifact-patch (актуальный механизм)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Разделы меню администратора добавляются с помощью :ref:`патчей для артефактов<artifact_patch>` типа ``app/artifact-patch``, которые модифицируют артефакт ``ui/menu$admin-workspace-menu``.

Структура патча:

.. code-block:: yaml

   ---
   id: add-my-service-admin-menu-section
   name:
     en: Add my service admin section
     ru: Добавить раздел администратора

   target: 'ui/menu$admin-workspace-menu'
   system: true
   order: 500

   type: json
   config:
     operations:
       - op: add
         path: '$.subMenu.left.items'
         value:
           id: my-service-section
           label:
             en: My Service
             ru: Мой сервис
           hidden: false
           type: SECTION
           config: { }
           items:
             - id: my-service-journal
               label:
                 en: My Journal
                 ru: Мой журнал
               hidden: false
               type: JOURNAL
               config:
                 recordRef: uiserv/journal@my-journal-id

Ключевые поля:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Поле
     - Описание
   * - ``target``
     - Всегда ``ui/menu$admin-workspace-menu`` для разделов боковой панели администратора
   * - ``system``
     - Всегда ``true`` для системных патчей меню администратора
   * - ``order``
     - Порядок применения патча: ``500`` — для активных разделов, ``1000`` — для legacy/устаревших разделов (отображаются в конце панели)
   * - ``path``
     - ``$.subMenu.left.items`` — путь для добавления секции в левую боковую панель

Структура элемента меню типа SECTION:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Поле
     - Описание
   * - ``id``
     - Уникальный идентификатор секции
   * - ``label``
     - Локализованное название секции (объект с ключами ``en``, ``ru``)
   * - ``hidden``
     - Признак скрытия; ``false`` — секция отображается
   * - ``type``
     - ``SECTION`` для группы журналов
   * - ``config``
     - Конфигурация секции (обычно пустой объект ``{ }``)
   * - ``items``
     - Список элементов-журналов (тип ``JOURNAL``) внутри секции

Структура элемента меню типа JOURNAL:

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Поле
     - Описание
   * - ``id``
     - Уникальный идентификатор элемента
   * - ``label``
     - Локализованное название (объект с ключами ``en``, ``ru``)
   * - ``hidden``
     - Признак скрытия; ``false`` — элемент отображается
   * - ``type``
     - ``JOURNAL``
   * - ``config.recordRef``
     - Ссылка на журнал в формате ``uiserv/journal@<journal-id>``

Паттерн: выделение устаревших разделов в Legacy-секцию
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Если накопились журналы, которые больше не используются активно, рекомендуется вынести их в отдельную секцию с меткой «Legacy» (Устаревшее). Это сохраняет доступ к данным, не перегружая основной раздел.

Соглашения:

* Идентификатор патча: ``add-<сервис>-legacy-admin-menu-section``.
* Название секции: ``{ "en": "Legacy", "ru": "Устаревшее" }`` — единообразное имя упрощает навигацию.
* Значение ``order``: ``1000`` — секция отображается в конце боковой панели после всех остальных разделов.
* Идентификатор секции: ``<сервис>-legacy-section``.

Пример патча для Legacy-секции (``add-integrations-legacy-admin-menu-section.yml``):

.. code-block:: yaml

   ---
   id: add-integrations-legacy-admin-menu-section
   name:
     en: Add legacy integrations admin section
     ru: Добавить раздел администратора устаревших интеграций

   target: 'ui/menu$admin-workspace-menu'
   system: true
   order: 1000

   type: json
   config:
     operations:
       - op: add
         path: '$.subMenu.left.items'
         value:
           id: integrations-legacy-section
           label:
             en: Legacy
             ru: Устаревшее
           hidden: false
           type: SECTION
           config: { }
           items:
             - id: integrations-ecos-sync
               label:
                 en: Synchronizations
                 ru: Синхронизации
               hidden: false
               type: JOURNAL
               config:
                 recordRef: uiserv/journal@ecos-sync
             - id: integrations-ecos-credentials
               label:
                 en: Credentials
                 ru: Учётные данные
               hidden: false
               type: JOURNAL
               config:
                 recordRef: uiserv/journal@ecos-credentials

Текущая структура меню ecos-integrations
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

После разделения на активные и устаревшие журналы раздел интеграций в меню администратора выглядит следующим образом:

.. list-table::
   :header-rows: 1
   :widths: 35 20 45

   * - Файл патча
     - ``order``
     - Содержимое
   * - ``add-notifications-admin-menu-section.yml``
     - 500
     - Активные журналы: Data Sources, Records sources, Camel DSL, Camel DSL Instance, Synchronization state, Synchronization log, External portals, Incoming webhooks
   * - ``add-integrations-legacy-admin-menu-section.yml``
     - 1000
     - Устаревшие журналы: Synchronizations, Credentials, EDI boxes configuration, OSGI Bundles, File import configuration, Files for Import, File import items

.. note::

   Файл ``add-notifications-admin-menu-section.yml`` имеет историческое имя (был скопирован из сервиса уведомлений), однако его внутренний идентификатор — ``add-integrations-admin-menu-section``. Не переименовывайте файл без согласования, но учитывайте это несоответствие при работе с артефактами меню администратора в проекте.

Добавление нового журнала в меню администратора
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

При добавлении нового журнала в меню администратора:

1. Добавьте новый элемент в ``config.operations[0].value.items`` соответствующего файла патча.
2. Используйте шаблон идентификатора: ``<сервис>-<journal-id>``.
3. Используйте шаблон ``recordRef``: ``uiserv/journal@<journal-id>``.
4. Активные журналы → ``add-notifications-admin-menu-section.yml``.
5. Устаревшие журналы → ``add-integrations-legacy-admin-menu-section.yml``.

.. warning::

   Не модифицируйте файлы ``ui/admin-sections-group/*.json`` для изменений меню администратора — эти артефакты не оказывают эффекта на меню в текущих версиях платформы.

Устаревший механизм: ui/admin-sections-group
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. deprecated::

   Ниже приведено описание артефактов ``ui/admin-sections-group``, которые **не влияют** на меню администратора в текущих версиях платформы. Документация сохранена для справки.

Артефакты типа ``ui/admin-sections-group`` описывали группы разделов в меню администратора.

Стандартные группы разделов (исторический справочник):

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

Типы разделов (устаревший справочник)
""""""""""""""""""""""""""""""""""""""

.. csv-table::
   :header-rows: 1

   Тип,Параметры,Описание
   JOURNAL,"journalId — идентификатор журнала",Раздел с журналом
   BPM,—,Раздел с бизнес-процессами в виде плитки или списка
   DEV_TOOLS,—,Страница инструментов разработчика (dev-tools)

Модель группы разделов
""""""""""""""""""""""

.. code-block:: typescript

   AdminSectionsGroupDef {
       id: String       // идентификатор группы (должен быть неизменным)
       name: MLText     // локализованное имя группы
       order: Float     // порядок в меню (чем больше, тем ниже)
       sections: List<AdminSectionDef>  // список разделов
   }

Модель раздела
""""""""""""""

.. code-block:: typescript

   AdminSectionDef {
       name: MLText     // имя раздела (необязательно для типа JOURNAL)
       type: String     // тип раздела: JOURNAL | BPM | DEV_TOOLS
       config: ObjectData  // конфигурация, зависящая от типа раздела
   }

Пример конфигурации группы (устаревший)
""""""""""""""""""""""""""""""""""""""""

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

Пример патча для ``ui/admin-sections-group`` (устаревший, не работает)
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

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

Пример файла ``integration-legacy.json`` (устаревший)
"""""""""""""""""""""""""""""""""""""""""""""""""""""

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
