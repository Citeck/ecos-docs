.. _journals:

Журналы
========

**Журнал** — табличная форма представления объектов с возможностью настройки отображения столбцов, фильтрации и манипуляции данными. Столбцы соответствуют атрибутам объекта или могут вычисляться на их основе.

В качестве источников данных могут использоваться любые **RecordsDAO** (:ref:`ECOS Records <Records_API>`), поддерживающие :ref:`язык предикатов <ecos-predicate_main>`.

Citeck поддерживает несколько режимов представления данных: таблицу, :ref:`канбан-доску <kanban_board>`, :ref:`список и плитки <tiles>`, :ref:`библиотеку документов <document_library>`.

Раздел охватывает:

Основы
------

.. grid:: 1
    :gutter: 2

    .. grid-item-card:: Общее описание
        :link: journals_overview
        :link-type: ref

        Определение, возможности системы, журнал «Журналы».

    .. grid-item-card:: Создание журнала
        :link: new_journal
        :link-type: ref

        Форма создания, основные вкладки и параметры.

    .. grid-item-card:: Пользовательское описание
        :link: user_description_journal
        :link-type: ref

        Режимы представления, управление настройками.

    .. grid-item-card:: Конфигурация
        :link: journals_config
        :link-type: ref

        Хранение и структура конфигурации в yml/json-формате.

Настройка и вычисления
-----------------------

.. grid:: 1
    :gutter: 2

    .. grid-item-card:: Групповые действия
        :link: group_actions
        :link-type: ref

        Настройка действий над несколькими записями одновременно.

    .. grid-item-card:: Вычисляемые атрибуты
        :link: computed_attributes
        :link-type: ref

        Вычисление значений столбцов на основе данных из БД.

    .. grid-item-card:: Выражения
        :link: journal_expressions
        :link-type: ref

        Операторы и функции для формирования значений в столбцах.

    .. grid-item-card:: Настройки журнала
        :link: advanced_journal_settings
        :link-type: ref

        Примеры конфигурирования столбцов, фильтров и сортировки.

    .. grid-item-card:: Синхронизация атрибутов
        :link: attribute_synchro
        :link-type: ref

        Фильтрация задач по атрибутам документа и задачи.

    .. grid-item-card:: Форматтеры
        :link: formatters
        :link-type: ref

        Управление отображением значений в ячейках.

    .. grid-item-card:: Редакторы
        :link: editors
        :link-type: ref

        Встроенное редактирование значений непосредственно в таблице.

Режимы представления
----------------------

.. grid:: 1
    :gutter: 2

    .. grid-item-card:: Канбан-доска
        :link: kanban_board
        :link-type: ref

        Представление записей в виде карточек по статусам.

    .. grid-item-card:: Библиотека документов
        :link: document_library
        :link-type: ref

        Иерархический интерфейс для работы с папками и файлами.

    .. grid-item-card:: Список и плитки
        :link: tiles
        :link-type: ref

        Альтернативные режимы отображения записей.

Рабочие пространства
----------------------

.. grid:: 1
    :gutter: 2

    .. grid-item-card:: Публикация
        :link: publication
        :link-type: ref

        Тип данных для управления контентом.

    .. grid-item-card:: Новости
        :link: news
        :link-type: ref

        Виджет и журнал для публикации анонсов в рабочих пространствах.

    .. grid-item-card:: База знаний
        :link: wiki_base
        :link-type: ref

        Ведение внутренней базы знаний в рабочих пространствах.

.. toctree::
    :maxdepth: 3
    :hidden:

    journals/journals
    journals/new_journal
    journals/user_description
    journals/content_types
    journals/views
    journals/configuration
    journals/journal_settings
    journals/features
