RecordsService (Java)
=======================

.. _ecos_RecordsService:

.. contents::
   :depth: 3

**RecordsService** - сервис для работы с абстрактными записями, источником которых может быть любой DAO.

Существует четыре операции, которые можно проделывать над записями:

1. Поиск записей
-------------------

.. _RecordsQuery:

Методы: **query, queryOne**

Для поиска записей всегда передается **RecordsQuery**, который содержит параметры поиска. Помимо самого простого метода для поиска с одним параметром **RecordsQuery** так же есть варианты с объединенным поиском и запросом атрибутов.

.. code-block:: java

  recordsService.queryOne(
    RecordsQuery.create()
          .withLanguage(PredicateService.LANGUAGE_PREDICATE)
          .withQuery(Predicates.and(
                  Predicates.eq(ValuePredicateToFtsAlfrescoConstants.TYPE, "cm:person"),
                  Predicates.eq("testc:personalNumber", personalNumber)))
          .withConsistency(Consistency.EVENTUAL)
          .addSort(new SortBy("cm:created", true))
          .build());

.. code-block:: java

  recordsService.query(RecordsQuery.create()
          .withLanguage(PredicateService.LANGUAGE_PREDICATE)
          .withQuery(Predicates.and(
                  Predicates.eq("_type", "emodel/type@testip-inboundPackage"),
                  Predicates.eq("testip:isNeedSendToVim", true),
                  Predicates.not(
                          Predicates.eq("testip:isAlreadySentToVim", true)
                  )
          ))
          .withConsistency(Consistency.EVENTUAL)
          .build());

* **.withLanguage** – указываем язык запроса;

* **.withQuery** – сам запрос;

* **.withConsistency** – Consistency (Согласованность). Возможные варианты: EVENTUAL, TRANSACTIONAL, DEFAULT, TRANSACTIONAL_IF_POSSIBLE

* **.addSort** – указываем по какому полю нужна сортировка

* **.build()** – сборка запроса

На выходе:

* при **query** получаем **RecsQueryRes<RecordRef>**
* при **queryOne** получаем **RecordRef**

2. Получение атрибутов записи
-------------------------------

Методы: **getAtt**, **getAtts**

.. code-block:: java

  recordsService.getAtt(documentRef, "eint:ediProviderType?str").asText();

* **documentRef** – record, к которому обращаемся

* **"eint:ediProviderType?str"** – параметр, который хотим получить

.. code-block:: java

 List<ObjPropertyClass> list = recordsService.getAtt(documentRef, "objProperty[]?json").asList(ObjPropertyClass.class);

.. code-block:: java

  RecordAtts recordAtts = recordsService.getAtts(RecordRef.valueOf(nodeRef.toString()),
        Collections.singletonMap("assocId", name + "[]?id"));

Существует два уровня абстрации для получения атрибутов:

**DTO Class > Attributes**

* **DTO Class** - класс, который используется для генерации списка аттрибутов для формирования схемы и запроса атрибутов из DAO.

После получения всех данных из DAO идет создание инстансов переданного DTO класса и наполнение его данными с помощью библиотеки jackson;
Список аттрибутов формируется либо из названий полей, либо можно добавить аннотацию AttName для указания атрибута вручную.

* **Attributes** - аттрибуты записи в чистом виде. Есть варианты с одним атрибутом, списком атрибутов или набором ключ->значение (Map)

3. Мутация (изменение или создание) записи
---------------------------------------------

Каждый DAO решает сам создавать или редактировать полученную запись.
Если в DAO приходит запись с пустым идентификатором, то это команда к созданию новой записи.

Изменение записи
~~~~~~~~~~~~~~~~~~

.. code-block:: java

  RecordAtts recordAtts = new RecordAtts();
  recordAtts.setId(recordRef);
  recordAtts.setAtt("testdl:isOutboundPackageSyncNeeded", false);
  recordsService.mutate(recordAtts);

Для обновления записи необходимо указывать **.setId()** записи которой необходимо изменить.

Создание записи
~~~~~~~~~~~~~~~~

.. code-block:: java

  RecordAtts recordAtts = new RecordAtts();
  recordAtts.setAtt(AlfNodeRecord.ATTR_TYPE, "testdl:routeTemplate");
  recordAtts.setAtt(RecordConstants.ATT_TYPE, "emodel/type@testdl-routeTemplateItem");
  recordAtts.setAtt("etype:type","testdl-routeTemplateItem");
  recordAtts.setAtt(RecordConstants.ATT_PARENT,
          "/app:company_home/st:sites/cm:ssg-edi/cm:dataLists/cm:testdl-routeTemplate");
  recordAtts.setAtt(RecordConstants.ATT_PARENT_ATT, "cm:contains");
  recordsService.mutate(recordAtts);

При создании новой записи параметр **setId()** не указывается. 

Если при мутации указать атрибут: 

.. code-block::

  __disableAudit=true

(константа DbRecordsControlAtts.DISABLE_AUDIT), то поля: 

.. code-block::

  _creator
  _created
  _modifier
  _modified

заполняться автоматически не будут. Если эти поля установить вручную, то в БД попадут именно они. 

Для ``creator`` и ``modifier`` допустимо указывать как username так и полный ref пользователя.

Атрибут

.. code-block::

  __disableAudit

допустимо проставлять только в контексте системы (runAsSystem)

4. Удаление записи
--------------------

.. code-block:: java

  recordsService.delete(routeTemplate);

* **RecordRef routeTemplate** – record который необходимо удалить