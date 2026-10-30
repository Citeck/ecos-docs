.. _ui_actions_format:

Формат действия и получение действий по записи
================================================

Описание полей действия и способы запросить доступные действия для записей через API.

.. contents::
    :depth: 2

Описание формата
------------------

.. list-table::
      :widths: 3 3 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Имя
        - Тип
        - Описание
      * - **id**
        - String
        - | Идентификатор действия.
          | Уникальный среди всех действий в системе
      * - **key**
        - String
        - | Ключ, по которому возможна фильтрация.
          | Должен быть в формате **word0.word1.word2**, чтобы можно было фильтровать по маске.
      * - **name**
        - String
        - Имя действия, которое увидит пользователь
      * - **type**
        - String
        - | Тип действия.
          | Тип определяет логику, которая будет выполнена при выполнении действия.
      * - **icon**
        - String
        - | Иконка действия. Пример "icon-delete", "icon-on".
          | Все иконки можно посмотреть в ``citeck/ecos-ui/src/fonts/citeck/demo.html``
      * - **config**
        - JsonObject
        - | Конфигурация действия.
          | Полезно в случаях, когда один тип действия может на основе конфигурации менять свое поведение.
          | Например - для действия с типом **Download** можно задать шаблон URI для скачивания контента.
      * - **predicate**
        - Predicate
        - | Используется для динамического определения доступности действия для пользователя. Подробно о :ref:`предикатах <ecos-predicate_main>`
          | Например, действия **Редактировать** и **Удалить** не могут выполнять пользователи без прав на запись и для них эти действия скрываются.


Получение действий по записи
------------------------------
Для запроса действий отправляется следующий запрос:

.. code-block:: json

 {
    "query": {
        "records": [
            "emodel/someType@bb617ee9-e085-4a3a-8fbf-df2d9534eadb",
            "emodel/someType@74c11ef8-8c63-40c1-b119-94feefd7f885"
        ],
        "actions": [
            "ui/action$delete",
            "ui/action$edit"
        ]
    }
 }

Ответ:

.. code-block:: json

 [
    {
        "record": "emodel/someType@bb617ee9-e085-4a3a-8fbf-df2d9534eadb",
        "actions": [
            {
                "icon": "edit",
                "key": "...",
                "type": "mutate",
                "config": {}
            },
            {
                "icon": "delete",
                "key": "...",
                "type": "delete",
                "config": {}
            }
        ]
    },
    {
        "record": "emodel/someType@74c11ef8-8c63-40c1-b119-94feefd7f885",
        "actions": [
            {
                "icon": "edit",
                "id": "...",
                "type": "mutate",
                "config": {}
            },
            {
                "icon": "delete",
                "id": "...",
                "type": "delete",
                "config": {}
            }
        ]
    }
 ]

Также доступен вариант раздельного указания действий по записям:

.. code-block:: json

 {
    "query": {
        "records": [
            {
                "record": "emodel/someType@3352b46d-ec44-465c-8673-086282d62b04",
                "actions": [
                    "ui/action$delete",
                    "ui/action$edit"
                ]
            },
            {
                "record": "emodel/someType@3dfff282-3ddf-45e1-886d-f5f2c94fe4e7",
                "actions": [
                    "ui/action$edit"
                ]
            }
        ]
    }
 }
