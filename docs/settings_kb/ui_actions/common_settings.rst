.. _ui_actions_frontend_settings:

Фронтенд и общие настройки любого действия
==========================================

Общие поля действия задают его название, применимость, подтверждение и предобработку. Их поведение зависит от режима выполнения и возможностей выбранного типа.

.. contents::
    :depth: 2

Фронтенд
--------

Исполнители действий наследуют ``ActionsExecutor`` из ``src/components/core/Records/actions/handler/ActionsExecutor.js``. В зависимости от поддерживаемого режима они реализуют:

- ``execForRecord(record, action, context)`` — для одной записи;
- ``execForRecords(records, action, context)`` — для массива записей;
- ``execForQuery(query, action, context)`` — для поискового запроса.

Метод ``getDefaultActionModel()`` задаёт значения модели по умолчанию, а ``isAllowedInContext(context)`` проверяет доступность действия в контексте интерфейса.

Пример исполнителя: ``src/components/core/Records/actions/handler/executor/CreateAction.js``.
Реестр находится в ``src/components/core/Records/actions/actionsRegistry.js``; встроенные обработчики регистрируются функцией ``registerAllActions`` в ``actions.js``. Общий порядок выполнения описан в ``recordActions.js``.

Общие настройки
---------------

.. rubric:: Название и применимость

.. code-block:: yaml

    id: open-document
    name:
      ru: Открыть документ
      en: Open document
    type: open-url
    icon: icon-new-tab
    config:
      url: /v2/dashboard?recordRef=${recordRef}
    features:
      execForRecord: true
      execForRecords: false
      execForQuery: false

Описание общих полей см. в разделе :ref:`Формат действия <ui_actions_format>`.

Флажки ``features`` имеют три состояния:

- ``false`` — режим запрещён;
- ``true`` — режим разрешён, если исполнитель его реализует;
- значение не задано — используется доступность режима в исполнителе.

Флажок не добавляет отсутствующий метод. Например, ``open-url`` реализует только выполнение для одной записи; ``execForRecords: true`` не превращает его в групповое действие.

.. rubric:: Подтверждение

Пример поля ``confirm`` в конфигурации действия:

.. code-block:: yaml

    confirm:
      title:
        ru: Подтвердите действие
        en: Confirm the action
      formRef: uiserv/form@action-comment
      formAttributes:
        recordId: ${?id}
        recordName: ${name}
        constant: value
      attributesMapping:
        body.comment: comment

Если не заданы ``confirm.title``, ``confirm.message`` и ``confirm.formRef``, общего диалога подтверждения нет. Сам исполнитель может показывать собственный диалог, например ``delete``.

``title`` и ``message`` поддерживают локализацию. Если указан ``formRef``, открывается форма подтверждения, а ``message`` не отображается. ``formAttributes`` задаёт исходные данные формы.

``attributesMapping`` переносит данные отправленной формы в ``config`` действия: ключ — путь назначения внутри ``config``, значение — путь к полю в данных формы. В примере значение поля ``comment`` попадает в ``config.body.comment``.

При выполнении для одной записи в options формы передаётся ``actionRecord``, для выбранных записей — ``actionRecords``. Дополнительные options можно задать через ``confirm.formOptions``; они объединяются после автоматически сформированных options и могут их переопределить.

.. rubric:: Подстановка атрибутов записи

.. code-block:: json

    {
      "id": "artifact-deploy",
      "name": {
        "ru": "Развернуть артефакт",
        "en": "Deploy artifact"
      },
      "type": "fetch",
      "config": {
        "url": "/gateway/eapps/api/artifact/deploy",
        "args": {
          "ref": "${recordRef}"
        },
        "method": "POST"
      }
    }

Перед одиночным выполнением в любом месте ``config`` разворачиваются вставки ``${attribute_name}``. Значения загружаются как атрибуты Records; специальное выражение ``${recordRef}`` обозначает ссылку на текущую запись.

Для группового выполнения и запроса общей подстановки по одной записи нет. Она зависит от исполнителя: например, обычный групповой ``mutate`` разворачивает конфигурацию отдельно для каждой записи. В ``confirm.formAttributes`` подстановка выполняется только при одиночном подтверждении, когда известен ``actionRecord``.

.. rubric:: Окно результата

Для одиночного выполнения окно результата можно отключить через ``config.noResultModal``:

.. code-block:: json

    {
      "id": "show-record-id",
      "type": "script",
      "config": {
        "fn": "alert(record.id); return true;",
        "noResultModal": true
      }
    }

По умолчанию ``noResultModal`` равен ``false``. Общие ветки группового выполнения и выполнения по запросу этот флаг не проверяют. Он также не отключает собственные диалоги и уведомления исполнителя.

Заголовок общего окна результата формируется из ``config.title`` или названия действия. Содержимое определяется возвращённым результатом, см. :ref:`Формат результата <ui_actions_result>`.

.. rubric:: Предобработка внешним модулем

В поле верхнего уровня ``preActionModule`` задаётся URL загружаемого JS-модуля. Например:

.. code-block:: yaml

    preActionModule: /custom/action-preprocess.js

Модуль экспортирует объект с функциями для нужных режимов. Каждая функция вызывается с аргументами ``(records, action, context)``. В одиночном режиме ``records`` — массив из одной записи; в режиме запроса — ``undefined``.

Пример ES-модуля для группового выполнения:

.. code-block:: javascript

    export default {
      async execForRecords(records, action, context) {
        return {
          config: { customFlag: true },
          results: []
        };
      }
    };

Ответ может содержать:

- ``config`` — поля, которые неглубоко объединяются поверх ``action.config``. Вложенные объекты заменяются целиком;
- ``results`` — результаты для уже обработанных записей в групповом режиме. Каждый элемент содержит ``recordRef``, ``status`` и ``message``. Такие записи исключаются из основного выполнения, результаты объединяются для отображения.

.. warning::

   В текущей одиночной ветке возвращённый ``config`` не передаётся основному исполнителю: он получает ранее подготовленную конфигурацию. ``results`` также не отменяет выполнение одиночного действия. Не используйте эти поля предобработки для изменения или пропуска одиночного действия.

Для режима запроса модуль может определить ``execForQuery``. Исходный поисковый запрос отдельным аргументом предобработке не передаётся. Поведение предобработки запроса и выбранных записей различается.
