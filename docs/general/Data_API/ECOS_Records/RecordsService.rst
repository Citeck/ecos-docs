.. _ecos_RecordsService:

RecordsService (Java)
=======================

**RecordsService** - сервис для работы с абстрактными записями, источником которых может быть любой DAO.

Существует четыре операции, которые можно проделывать над записями:

.. tab-set::

   .. tab-item:: Поиск записей

      .. _RecordsQuery:

      Методы: **query, queryOne**

      Для поиска записей всегда передается **RecordsQuery**, который содержит параметры поиска.
      Помимо самого простого метода для поиска с одним параметром **RecordsQuery** так же есть варианты
      с объединенным поиском и запросом атрибутов.

      .. tab-set::

         .. tab-item:: queryOne

            .. code-block:: java

               recordsService.queryOne(
                 RecordsQuery.create()
                   .withSourceId("emodel/person")
                   .withLanguage(PredicateService.LANGUAGE_PREDICATE)
                   .withQuery(Predicates.and(
                           Predicates.eq("city", "Tomsk"),
                           Predicates.eq("organization", "Citeck")))
                   .withConsistency(Consistency.EVENTUAL)
                   .addSort(new SortBy("_created", true))
                   .build());

         .. tab-item:: query

            .. code-block:: java

               recordsService.query(RecordsQuery.create()
                   .withSourceId("edi/edi-inbound-main-document")
                   .withLanguage(PredicateService.LANGUAGE_PREDICATE)
                   .withQuery(Predicates.and(
                           Predicates.eq("type", "emodel/type@testip-inboundPackage"),
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

   .. tab-item:: Получение атрибутов

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
        После получения всех данных из DAO идет создание инстансов переданного DTO класса и наполнение его данными с помощью библиотеки jackson.
        Список аттрибутов формируется либо из названий полей, либо можно добавить аннотацию ``AttName`` для указания атрибута вручную.
      * **Attributes** - аттрибуты записи в чистом виде. Есть варианты с одним атрибутом, списком атрибутов или набором ключ→значение (Map).

   .. tab-item:: Мутация

      Каждый DAO решает сам создавать или редактировать полученную запись.
      Если в DAO приходит запись с пустым идентификатором, то это команда к созданию новой записи.

      .. tab-set::

         .. tab-item:: Изменение записи

            .. code-block:: java

               RecordAtts recordAtts = new RecordAtts();
               recordAtts.setId(recordRef);
               recordAtts.setAtt("testdl:isOutboundPackageSyncNeeded", false);
               recordsService.mutate(recordAtts);

            Для обновления записи необходимо указывать **.setId()** записи которой необходимо изменить.

         .. tab-item:: Создание записи

            .. code-block:: java

               RecordAtts recordAtts = new RecordAtts();
               recordAtts.setAtt(RecordConstants.ATT_TYPE, "emodel/type@testdl-routeTemplateItem");
               recordAtts.setAtt(RecordConstants.ATT_PARENT, "eproc/routeTemplate@c897a06d-e1b5-4564-9966-762124399dfd");
               recordAtts.setAtt(RecordConstants.ATT_PARENT_ATT, "routes");
               recordsService.mutate(recordAtts);

            При создании новой записи параметр **setId()** не указывается.

      Если при мутации указать атрибут ``__disableAudit=true``
      (константа ``DbRecordsControlAtts.DISABLE_AUDIT``), то поля
      ``_creator``, ``_created``, ``_modifier``, ``_modified``
      заполняться автоматически не будут. Если эти поля установить вручную, то в БД попадут именно они.

      Для ``creator`` и ``modifier`` допустимо указывать как username так и полный ref пользователя.

      Атрибут ``__disableAudit`` допустимо проставлять только в контексте системы (``runAsSystem``).

   .. tab-item:: Удаление записи

      .. code-block:: java

         recordsService.delete(routeTemplate);

      * **RecordRef routeTemplate** – record, который необходимо удалить
