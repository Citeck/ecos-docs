.. _using_in_browser:

Использование в браузере
===========================

.. contents::
   :depth: 3

.. note::

  В инициализированном web-приложении ``Records`` и ``Citeck.Records`` ссылаются на один компонент.

Для работы с Records API разработан компонент **Records**, который доступен в глобальном контексте на любой странице системы. 

Атрибуты статуса, лицензии, рабочих областей и другие прикладные поля в примерах ниже предоставляются соответствующими сервисами. Их доступность и права определяются источником записи.

Доступные операции:

 * **get(recordRef)** - Получить запись по её идентификатору. Ниже представлен список операций с записью;
 * **query(query, attributes)** - Поиск записей. Первый аргумент - запрос для поиска, а второй - какие атрибуты нам нужны у найденых записей;
 * **remove(records)** - Удаление записей.

Операции с записью, которая получена через метод **"Records.get"**:

 * **load(attributes, forceLoad)** - Загрузить атрибут или несколько атрибутов. При ``forceLoad=true`` сохранённые значения загружаются повторно; при false или отсутствии параметра используется кэш;
 * **att(attributeName, value)** - Проставить значение атрибута для записи. Используется перед сохранением записи;
 * **save(attsToLoad)** - Сохранить изменения в записи, которые были сделаны методом att из предыдущего пункта и загрузить атрибуты, которые передали в attsToLoad (опционально);

``load`` возвращает Promise: для строки атрибута — одно значение, для массива строк — объект с этими строками в качестве ключей, для карты алиасов — объект с заданными ключами.

Метод ``save`` может принимать атрибуты для загрузки. В этом случае на сервер вместе с изменениями отправляется поле ``attributes``. ``save(attsToLoad)`` возвращает Promise с той же формой данных, что и ``load``; обычный ``save()`` для серверной записи возвращает Promise объекта Record. ``remove`` возвращает Promise без значения. Для последовательных операций используйте ``await``.

.. note::

  ``forceLoad=true`` не отменяет несохранённые изменения, сделанные через ``att``: для изменённого атрибута может вернуться локальное значение. Виртуальные записи обрабатываются локально; параметр не гарантирует HTTP-запрос в каждом случае.

Метод ``Records.getRecordToEdit(recordRef)`` возвращает отдельную обёртку редактирования базовой записи. Её временный идентификатор с ``-alias-`` связан с исходной записью и не является идентификатором новой сущности на сервере.

Структура query
-----------------

``Records.query`` возвращает Promise объекта с полями ``records``, ``messages``, ``hasMore``, ``totalCount``, ``attributes`` и ``errors``. Без запроса атрибутов элементы ``records`` — строки ссылок. С атрибутами это объекты с запрошенными значениями и полем ``id``, содержащим полную ссылку, если алиас ``id`` не задан потребителем.

Этот результат браузерного компонента отличается от сырых серверных записей вида ``{id, attributes}``.

.. list-table::
  :widths: 20 55
  :header-rows: 1
  :class: tight-table

  * - Поле
    - Описание
  * - ``sourceId``
    - Идентификатор источника данных в формате «приложение/id_локального_источника_данных»
  * - ``query``
    - Любой формат, который поддерживается источником данных
  * - ``language``
    - Язык для определения содержимого query. Источник данных может поддерживать несколько языков
  * - ``sortBy``
    - Список объектов ``{attribute: String, ascending: Boolean}`` — атрибут для сортировки и направление (по возрастанию ``true`` или по убыванию ``false``)
  * - ``groupBy``
    - Список атрибутов для группировки
  * - ``page``
    - Объект ``{maxItems: Number, skipCount: Number}`` — максимальное количество элементов и количество элементов, которое нужно пропустить при поиске
  * - ``consistency``
    - Ожидаемая консистенция данных: ``EVENTUAL`` \| ``TRANSACTIONAL`` \| ``DEFAULT`` \| ``TRANSACTIONAL_IF_POSSIBLE``. ``EVENTUAL`` позволяет использовать индексы для поиска элементов

.. code-block:: javascript

  {
    "sourceId": String,
    "query": Any,
    "language": String,
    "sortBy": [
        {
            "attribute": String,
            "ascending": Boolean
        }
    ],
    "groupBy": [String],
    "page": {
        "maxItems": Number,
        "skipCount": Number
    },
    "consistency": EVENTUAL | TRANSACTIONAL | DEFAULT | TRANSACTIONAL_IF_POSSIBLE
  }

Примеры использования
------------------------

Запрос ФИО пользователя:

.. code-block:: javascript

  var user = Records.get('emodel/person@user');
  await user.load(['userName', 'firstName', 'lastName'])

Запрос имени пользователя:

.. code-block:: javascript

  var user = Records.get('emodel/person@user')
  await user.load('firstName')

Пример скрипта для смены статуса:

.. code-block:: javascript

  var doc = Records.get('someDocumentRef');
  doc.att('_status', 'some_status_id');
  await doc.save();

Получение сразу нескольких атрибутов у вложенного значения:

.. code-block:: javascript

  await Records.get('uiserv/rjournal@test587').load('boardRefs[]{id,name}', true)

Статус объекта:

.. code-block:: javascript

  await Records.get('emodel/someType@id').load("_status?str")

Проверка enterprise лицензии:

.. code-block:: javascript

  await Records.get('emodel/meta@').load('$license.enterprise?bool', true)

Получение рабочих областей текущего пользователя:

.. code-block:: javascript

  await Records.query({
      sourceId: 'emodel/workspace',
      language: 'user-workspaces'
  }, {
      'wsId': '?localId',
      'wsName': '?disp!?localId'
  })

Узнать sourceId по typeId:

.. code-block:: javascript

  await Records.get('emodel/type@typeId').load('sourceId')



.. _CRUD_records_api:

CRUD операции
---------------

Ниже представлены примеры основных операций, выполняемых при управлении данными и манипулировании:

.. tab-set::

   .. tab-item:: CREATE

      .. code-block:: javascript

         const record = Records.get("emodel/someType@");
         record.att("name", "New record");
         record.att("someAttribute", "Hello world!");
         await record.save();

   .. tab-item:: READ

      .. code-block:: javascript

         const record = Records.getRecordToEdit("emodel/someType@id");
         await record.load("?json");

   .. tab-item:: UPDATE

      .. code-block:: javascript

         const record = Records.getRecordToEdit("emodel/someType@id");
         record.att("someAttribute", "New value");
         await record.save();

   .. tab-item:: DELETE

      .. code-block:: javascript

         await Records.remove("emodel/someType@id1"); // 1 объект
         await Records.remove(["emodel/someType@id1", "emodel/someType@id2"]); // массив объектов

Общение с сервером происходит через ``POST`` запросы:

Браузерный клиент передаёт ``version: 1`` в теле запроса для выбора версии REST-контракта.

.. list-table::
      :widths: 10 40 40
      :header-rows: 1
      :class: tight-table 

      * - Запрос
        - Описание
        - В коде ecos-ui используется
      * - ``READ_ONLY POST``

          .. code-block:: text
                      
            /gateway/api/records/query 

        - Поиск записей и/или получение атрибутов
        - 

            .. code-block:: javascript

              Records.query и Records.get("id_сущности").load(атрибуты_для_загрузки)

      * - ``READ_WRITE POST``

          .. code-block:: text

            /gateway/api/records/delete 

        - Удаление сущностей 
        - 

            .. code-block:: javascript

              Records.remove

      * - ``READ_WRITE POST``

          .. code-block:: text

            /gateway/api/records/mutate 

        - Создание или изменение сущностей
        - 

            .. code-block:: javascript

              var rec = Records.get("id_сущности"); rec.att("атрибут", "значение"); rec.save() 

Возвращаемые в ответе типы 
-------------------------------

Браузерный клиент читает ответы этих endpoint как JSON. Это описание транспорта браузерного клиента; Java/Kotlin API возвращает также DTO и другие объекты.

Коды HTTP ответов
-------------------

Примеры HTTP-кодов ответа (полный набор зависит также от gateway и авторизации):

*	200 **OK**
*	401 **Unauthorized**
*	500 **Internal Server Error**

Описание ошибок и их уровни
-----------------------------

Ошибки отражены в теле ответа по ключу **messages** и с полем **level** равным **"ERROR"**. 

Пример:

.. code-block:: json

  {
    "messages": [
      {
        "level": "ERROR",
        "time": 1653990549261,
        "type": "text",
        "msg": "Some error",
        "requestId": "7848a70e-a449-4b24-abb9-a2a7fbb8ebfa",
        "requestTrace": [
          "gateway:06d039e1766550be603cf98379bbdb22",
          "alfresco:019ca5db-160f-45df-84a6-02750a4f13b7"
        ]
      }
    ],
    "txnActions": [],
    "records": [],
    "hasMore": false,
    "totalCount": 0,
    "version": 1
  }

Поддерживаются уровни ``ERROR``, ``WARN``, ``INFO`` и ``DEBUG``; состав сообщений зависит от настроек запроса. Отладочные сообщения можно запросить через ``Records.query(query, attributes, {debug: true})``.

Ошибка может присутствовать в ``messages`` даже при HTTP 200. Транспорт браузерного компонента при сообщении ERROR отклоняет Promise; поле ``msg`` может содержать строку или объект ошибки. Для ``type=records-error`` текст может находиться в ``msg.msg``.

При обработке результата учитывайте особенности метода: некоторые ветки ``load`` перехватывают ошибку, выводят её в консоль и возвращают пустое значение. Успешный HTTP-статус сам по себе не подтверждает успешное выполнение операции.
