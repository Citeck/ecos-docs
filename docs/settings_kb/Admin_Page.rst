Страница администратора
=======================

Общее описание
~~~~~~~~~~~~~~

Страница администратора служит для управления системой через интерфейс.

Настройка разделов меню администратора
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для настройки разделов меню администратора предусмотрены артефакты с типом **ui/admin-sections-group**, каждый из которых представляет собой группу разделов в меню.

Каждый микросервис может добавлять свою группу разделов (или несколько групп) при запуске.
Для модификации существующих групп можно воспользоваться патчами для артефактов.

Типы разделов:

.. csv-table::

    Тип,Параметры,Описание
    JOURNAL,journalId - идентификатор журнала, Раздел с журналом
    BPM,\-,Раздел с бизнес-процессами в виде плитки или списка
    DEV_TOOLS,\-,Страница dev-tools

Стандартные группы разделов:

.. csv-table:: 

    Микросервис,Идентификатор группы,Порядок
    ecos-apps,application,0
    ecos-process,process,10
    ecos-model,model,20
    ecos-uiserv,user-interface,30
    ecos-notifications,notification,40
    ecos-integrations,integration,50

Модель группы разделов::

    AdminSectionsGroupDef {
        id: String // идентификатор группы может быть произвольным, но должен оставаться одним и тем же
        name: MLText // имя группы разделов
        order: Float // порядок группы в меню. Больше - ниже
        sections: List<AdminSectionDef> // разделы
    }

Модель раздела::

    AdminSectionDef {
        name: MLText // имя раздела. Можно не задавать для раздела с типом JOURNAL
        type: String // тип раздела
        config: ObjectData // конфигурация раздела
    }

Пример конфигурации::

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
        },
        ...
      ]
    }

Пример патча для добавления нового раздела в группу::

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
