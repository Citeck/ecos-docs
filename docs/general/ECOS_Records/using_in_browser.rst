Использование в браузере
===========================

.. _using_in_browser:

.. contents::
   :depth: 3

.. note:: 

  Начиная с версии 4.5.0 вместо Citeck.Records.get и Citeck.Records.query можно использовать Records.get и Records.query 

Для работы с Records API разработан компонент **Citeck.Records**, который доступен в глобальном контексте на любой странице системы. 

Доступные операции:

* **get(recordRef)** - Получить запись по её идентификатору. Ниже представлен список операций с записью;
* **query(query, attributes)** - Поиск записей. Первый аргумент - запрос для поиска, а второй - какие атрибуты нам нужны у найденых записей;
* **remove(records)** - Удаление записей.

Операции с записью, которая получена через метод **"Citeck.Records.get"**:

* **load(attributes, forceLoad)** - Загрузить атрибут или несколько атрибутов. Первым аргументом мы указываем что нужно загрузить, а вторым следует использовать кэш или нет. Второй аргумент опционален и по умолчанию равен false (т.е. кэш активен);
* **att(attributeName, value)** - Проставить значение атрибута для записи. Используется перед сохранением записи;
* **save(attsToLoad)** - Сохранить изменения в записи, которые были сделаны методом att из предыдущего пункта и загрузить атрибуты, которые передали в attsToLoad (опционально);

Метод save с версии UI 2.8.1 может принимать атрибуты для загрузки. В этом случае на сервер вместе с атрибутами для изменения так же отправляются атрибуты для загрузки в поле attributes тела запроса.
Если при вызове save указаны атрибуты для загрузки, то в результате будет тот же формат, что и при вызове метода load.

Структура query::

  {
    "sourceId": String // идентификатор источника данных в формате "приложение/id_локального_источника_данных"
    "query": Any // любой формат, который поддерживается источником данных
    "language": String // язык для определения содержимого query. Источник данных может поддерживать несколько языков
    "sortBy": [
        {
            "attribute": String // атрибут для сортировки
            "ascending": Boolean // сортировка должна быть по возрастанию true или по убыванию false
        }
    ],
    "groupBy": [String] // список атрибутов для группировки
    "page": {
        maxItems: Number // максимальное кол-во элементов
        skipCount: Number // количество элементов, которое нужно пропустить при поиске
    }
    "consistency": EVENTUAL | TRANSACTIONAL | DEFAULT | TRANSACTIONAL_IF_POSSIBLE // ожидаемая консистенция данных. EVENTUAL позволяет использовать индексы для поиска элементов
  }

Примеры использования::


  // Запрос ФИО пользователя:

  var user = Citeck.Records.get('emodel/person@user');
  await user.load(['userName', 'firstName', 'lastName'])

   //Запрос имени пользователя:
  
  var user = Citeck.Records.get('emodel/person@user')
  await user.load('firstName')

  //Пример скрипта для смены статуса:

  var doc = Citeck.Records.get('someDocumentRef');
  doc.att('_status', 'some_status_id');
  doc.save();

  // Получение сразу нескольких атрибутов у вложенного значения:

  await Citeck.Records.get('uiserv/rjournal@test587').load(boardRefs[]{id,name}, true)

    // Статус объекта:

  await Citeck.Records.get('emodel/someType@id').load("_status?str")

  // Проверка enterprise лицензии:

  await Citeck.Records.get('emodel/meta@').load('$license.enterprise?bool', true)

CRUD операции
---------------

.. _CRUD_records_api:

.. tabs::

   .. tab:: CREATE    

    .. code-block::

      const record = Records.get("emodel/someType@");
      record.att("name", "New record"); 
      record.att("someAttribute", "Hello world!");
      record.save();

   .. tab:: READ    

    .. code-block::

      const record = Records.getRecordToEdit("emodel/someType@id");
      await record.load("?json");

   .. tab:: UPDATE    

    .. code-block::

      const record = Records.getRecordToEdit("emodel/someType@id");
      record.att("someAttribute", "New value");
      record.save();

   .. tab:: DELETE  

    .. code-block::
      
      Records.remove("emodel/someType@id1"); // 1 объект
      Records.remove(["emodel/someType@id1", "emodel/someType@id2"]); // массив объектов

Общение с сервером происходит через ``POST`` запросы:

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

            .. code-block:: js

              Records.query и Records.get("id_сущности").load(атрибуты_для_загрузки)

      * - ``READ_WRITE POST``

          .. code-block:: text

            /gateway/api/records/delete 

        - Удаление сущностей 
        - 

            .. code-block:: js

              Records.remove

      * - ``READ_WRITE POST``

          .. code-block:: text

            /gateway/api/records/mutate 

        - Создание или изменение сущностей
        - 

            .. code-block:: js

              var rec = Records.get("id_сущности"); rec.att("атрибут", "значение"); rec.save() 

Возвращаемые в ответе типы 
-------------------------------

В ответе может быть возвращен только тип json. 

Коды HTTP ответов
-------------------

Возможные коды ответов:

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

Доступный **level** только **"ERROR"**.