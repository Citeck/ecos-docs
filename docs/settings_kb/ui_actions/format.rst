.. _ui_actions_format:

Формат действия и получение действий по записи
==============================================

Общие поля действия и получение доступных действий через клиентский Records API.

.. contents::
    :depth: 2

Описание формата
----------------

.. list-table::
    :widths: 20 15 65
    :header-rows: 1
    :class: tight-table

    * - Поле
      - Тип
      - Описание
    * - ``id``
      - String
      - Идентификатор действия. Для обращения через Records используется полная ссылка ``uiserv/action@<id>``, учитывающая пространство имён действия.
    * - ``name``
      - String / MLText
      - Название действия: строка или объект локализаций, например ``{"ru": "Открыть", "en": "Open"}``.
    * - ``pluralName``
      - String / MLText
      - Название для нескольких записей. Если не задано, используется ``name``.
    * - ``type``
      - String
      - Идентификатор зарегистрированного обработчика, например ``download`` или ``mutate``.
    * - ``icon``
      - String
      - Код иконки, например ``icon-delete``. Каталог иконок в ecos-ui: ``src/fonts/citeck/demo.html``.
    * - ``theme``
      - String
      - Тема оформления действия.
    * - ``config``
      - Object
      - Параметры выбранного типа. Например, ``config.url`` для ``download`` задаёт URL скачивания.
    * - ``features``
      - Object
      - Применимость: ``execForRecord``, ``execForRecords``, ``execForQuery``. Возможности ограничены методами исполнителя.
    * - ``confirm``
      - Object
      - Заголовок, сообщение или форма подтверждения; исходные данные формы и перенос введённых значений в конфигурацию.
    * - ``preActionModule``
      - String
      - URL модуля предобработки.
    * - ``execForRecordsBatchSize``
      - Number
      - Размер пакета при групповом выполнении; значение ``0`` не включает разбиение на пакеты.
    * - ``execForRecordsParallelBatchesCount``
      - Number
      - Настройка обработки пакетов. Значение ``1`` используется для последовательной обработки.
    * - ``execForQueryConfig``
      - Object
      - Настройки выполнения запроса. ``execAsForRecords`` включает обработку найденных записей через групповой режим, если режим запроса доступен у исполнителя.
    * - ``predicate`` / ``evaluator``
      - Object
      - Серверные условия доступности действия. Фронтенд получает результат их проверки; правила зависят от серверной конфигурации. См. :ref:`Предикаты <ecos-predicate_main>`.
    * - ``key``
      - String
      - Ключ для серверной фильтрации действий. Общий механизм выполнения фронтенда не использует его для выбора исполнителя — для этого служит ``type``.

Подробности подтверждения, подстановок и предобработки см. в разделе :ref:`Общие настройки <ui_actions_frontend_settings>`.

Получение действий по записи
----------------------------

Текущий клиент ecos-ui запрашивает источник ``uiserv/record-actions``. Ниже приведён вызов JavaScript Records API с сокращённой схемой атрибутов:

.. code-block:: javascript

    const result = await Records.queryOne(
      {
        sourceId: 'uiserv/record-actions',
        query: {
          records: [
            'emodel/someType@bb617ee9-e085-4a3a-8fbf-df2d9534eadb',
            'emodel/someType@74c11ef8-8c63-40c1-b119-94feefd7f885'
          ],
          actions: ['uiserv/action@edit', 'uiserv/action@delete']
        }
      },
      {
        records: 'records[]?num',
        actions: 'actions[]{id,name,icon,type,config:config?json,features:features?json}'
      }
    );

Пример результата этого вызова:

.. code-block:: json

    {
      "records": [3, 2],
      "actions": [
        {
          "id": "uiserv/action@edit",
          "name": "Редактировать",
          "icon": "icon-edit",
          "type": "edit",
          "config": {},
          "features": {"execForRecord": true}
        },
        {
          "id": "uiserv/action@delete",
          "name": "Удалить",
          "icon": "icon-delete",
          "type": "delete",
          "config": {},
          "features": {"execForRecord": true, "execForRecords": true}
        }
      ]
    }

Массив ``records`` содержит числовые маски доступности в порядке запрошенных записей. Бит ``1 << actionIndex`` соответствует позиции действия в массиве ``actions``. В примере маска ``3`` разрешает оба действия для первой записи, а ``2`` — только второе для второй.

Рабочий клиент дополнительно запрашивает ``pluralName``, ``preActionModule``, ``confirm`` и настройки пакетного выполнения и запроса. Полный список находится в ``ACTION_INNER_ATTRIBUTES`` файла ``src/components/core/Records/actions/recordActionsApi.js``.

Сервис ``recordActions.getActionsForRecords(records, actions, context)`` преобразует этот ответ в группы ``forRecord``, ``forRecords`` и ``forQuery``, проверяет возможности исполнителей и контекст. Это уже клиентская модель, отличающаяся от результата ``Records.queryOne``.

При вызове ``recordActions.getActionsForRecord(record)`` без явного списка действий клиент сначала загружает ``_type?id`` записи, затем ``_actions[]?id`` её типа и запрашивает доступность найденных действий.
