.. _ecos_data_main:

Citeck Data
=============

.. contents::
   :depth: 3

**ecos-data** — библиотека для создания Records DAO, записи которых хранятся в БД. Ниже описаны API и ограничения версии ``1.19.0-SNAPSHOT``.

На основе атрибутов :ref:`типа данных <data_types_main>` библиотека создаёт и обновляет таблицы и предоставляет операции над записями:

1. Создание новых записей.
2. Получение атрибутов у записей по их ID.
3. Поиск записей с использованием :ref:`языка предикатов <ecos-predicate_main>`.
4. Изменение существующих записей.
5. Удаление записей.

Создание, изменение и удаление можно отключить в ``DbRecordsDaoConfig`` параметрами ``insertable``, ``updatable`` и ``deletable``. По умолчанию все три операции разрешены конфигурацией; права пользователя проверяются отдельно.

PostgreSQL-бэкенд предоставляется модулем ``ecos-data-sql-pg``. Совместимость с конкретной версией сервера необходимо учитывать для используемой сборки; версия JDBC-драйвера сама по себе не определяет минимальную версию PostgreSQL.

Изменение схемы существующих колонок имеет ограничения. Параметр ``DbDataServiceConfig.maxItemsToAllowSchemaMigration`` по умолчанию равен ``1000``: при необходимости такой миграции и превышении порога по числу записей автоматическая миграция прерывается с ошибкой. Этот порог не является общим запретом на создание таблиц или добавление колонок.

Хранение данных в ecos-model
----------------------------------------------

Интеграция с **ecos-model** позволяет использовать DB-хранение для типов данных. Автоматическая регистрация источников и правила формирования ``sourceId`` определяются версией ecos-model; сама библиотека ecos-data использует ID, заданный в конфигурации DAO.

Для обращения к источнику используйте его фактический ``sourceId``. В приложении ``emodel`` список зарегистрированных источников можно запросить через источник метаданных Records API:

.. code-block:: javascript

  await Records.query({sourceId: 'emodel/src', query: {}, language:'predicate'}, '?localId')

.. _new_RecordsDAO:

Создание нового RecordsDAO в своем микросервисе
--------------------------------------------------------------------------------

Примеры ниже предполагают, что интеграция приложения уже предоставляет Spring-bean ``DbDomainFactory`` с настроенными подключением к БД и компонентами. Тип ``ecos-type-id`` должен быть доступен в репозитории типов. Имена схемы, таблицы и источника замените своими значениями.

Java:

.. code-block:: java

  import kotlin.Unit;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;
  import ru.citeck.ecos.data.sql.domain.DbDomainConfig;
  import ru.citeck.ecos.data.sql.domain.DbDomainFactory;
  import ru.citeck.ecos.data.sql.dto.DbTableRef;
  import ru.citeck.ecos.data.sql.records.DbRecordsDaoConfig;
  import ru.citeck.ecos.data.sql.service.DbDataServiceConfig;
  import ru.citeck.ecos.records2.RecordRef;
  import ru.citeck.ecos.records3.record.dao.RecordsDao;

  @Configuration
  public class CustomRecordsDaoConfig {

      private DbDomainFactory dbDomainFactory;

      @Bean
      public RecordsDao customRecordsDao() {

          RecordRef typeRef = RecordRef.create("emodel", "type", "ecos-type-id");

          return dbDomainFactory.create(
              DbDomainConfig.create()
                  .withRecordsDao(
                      DbRecordsDaoConfig.create(b -> {
                          b.withId("records-dao-id");
                          b.withTypeRef(typeRef);
                          return Unit.INSTANCE;
                      })
                  )
                  .withDataService(
                      DbDataServiceConfig.create(b -> {
                          b.withTableRef(new DbTableRef("schema_name", "table_name"));
                          b.withStoreTableMeta(true);
                          return Unit.INSTANCE;
                      })
                  )
                  .build()
          ).build();
      }

      @Autowired
      public void setDbDomainFactory(DbDomainFactory dbDomainFactory) {
          this.dbDomainFactory = dbDomainFactory;
      }
  }

Kotlin:

.. code-block:: kotlin

  import org.springframework.context.annotation.Bean
  import org.springframework.context.annotation.Configuration
  import ru.citeck.ecos.data.sql.domain.DbDomainConfig
  import ru.citeck.ecos.data.sql.domain.DbDomainFactory
  import ru.citeck.ecos.data.sql.dto.DbTableRef
  import ru.citeck.ecos.data.sql.records.DbRecordsDaoConfig
  import ru.citeck.ecos.data.sql.service.DbDataServiceConfig
  import ru.citeck.ecos.records2.RecordRef
  import ru.citeck.ecos.records3.record.dao.RecordsDao

  @Configuration
  class CustomRecordsDaoConfig(
      private val dbDomainFactory: DbDomainFactory
  ) {

      @Bean
      fun customRecordsDao(): RecordsDao {

          val typeRef = RecordRef.create("emodel", "type", "ecos-type-id")
          val recordsDao = dbDomainFactory.create(
              DbDomainConfig.create()
                  .withRecordsDao(
                      DbRecordsDaoConfig.create {
                          withId("records-dao-id")
                          withTypeRef(typeRef)
                      }
                  )
                  .withDataService(
                      DbDataServiceConfig.create {
                          withTableRef(DbTableRef("schema_name", "table_name"))
                          withStoreTableMeta(true)
                      }
                  )
                  .build()
          ).build()

          return recordsDao
      }
  }

Поиск записей и ассоциации
------------------------------------------------

Для поиска используется язык ``predicate``. Имена атрибутов в условиях должны соответствовать доступным колонкам записи; значения системных атрибутов и ассоциаций преобразуются DB-слоем.

Например, поиск по значению самой ассоциации:

.. code-block:: javascript

  await Records.query({
    sourceId: 'emodel/ecos-contract',
    language: 'predicate',
    query: {
      t: 'eq',
      att: 'counterparty',
      val: 'emodel/counterparty@some-counterparty-id'
    },
    page: { maxItems: 100, skipCount: 0 }
  });

В примере должны существовать указанные источник, ассоциация и контрагент. Ссылка ассоциации преобразуется во внутренний идентификатор для поиска.

.. note::

   В версии ``1.19.0-SNAPSHOT`` путь вида ``counterparty.fullOrganizationName`` не преобразуется в JOIN к связанной записи. Нахождение источников в одной БД и схеме само по себе не добавляет такой возможности. Чтение вложенных атрибутов через Records API и поиск по ним в SQL — разные операции.

Размер страницы ограничен ``DbRecordsDaoConfig.queryMaxItems`` (по умолчанию ``5000``). Если ``page.maxItems`` больше этого предела, применяется предел DAO; значение ``-1`` также использует предел DAO. Для полного обхода результатов учитывайте ``hasMore`` и передавайте следующую страницу через ``skipCount``.

.. _ecos_data_functions:

Запросы с использованием функций
----------------------------------------------------------------

В запросе атрибутов поддерживается простая форма вызова:

.. code-block:: text

  function(column)
  function(*)

Имя функции и имя колонки должны состоять из символов, соответствующих ``\w+``; пробелы внутри вызова, несколько аргументов и вложенные выражения этой формой не поддерживаются. Кроме ``*``, аргумент должен быть именем существующей колонки. В SQL он передаётся как имя колонки, а не как произвольный SQL-фрагмент или константа.

Фактическая доступность функции и тип результата зависят от PostgreSQL и типа колонки. Наличие функции в PostgreSQL не означает, что все её перегрузки доступны через этот синтаксис Records API.

Группировка и агрегаты
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для агрегирования используйте ``groupBy`` с именами колонок и запрашивайте группировочные поля вместе с агрегатами. Поддерживаемый сценарий — группировка по ``taskId`` с вычислением агрегатов по числовой колонке ``amount``:

.. code-block:: javascript

  const result = await Records.query(
    {
      sourceId: 'emodel/your-type',
      language: 'predicate',
      query: {
        t: 'eq',
        att: '_type',
        val: 'emodel/type@your-type'
      },
      groupBy: ['taskId'],
      page: { maxItems: 100, skipCount: 0 }
    },
    {
      taskId: 'taskId?str',
      count: 'count(*)?num',
      amountSum: 'sum(amount)?num',
      amountMin: 'min(amount)?num',
      amountMax: 'max(amount)?num',
      amountAvg: 'avg(amount)?num'
    }
  );

Замените ``your-type`` фактическим источником и типом с полями ``taskId`` и ``amount``. Не добавляйте произвольные обычные поля к агрегатам: их использование должно соответствовать правилам SQL-группировки.

.. list-table:: Агрегаты
   :widths: 25 55
   :header-rows: 1
   :class: tight-table

   * - Вызов
     - Назначение
   * - ``count(*)``
     - Количество строк в группе
   * - ``count(column)``
     - Количество строк с непустым (не NULL) значением колонки
   * - ``sum(column)``
     - Сумма значений
   * - ``min(column)``
     - Минимальное значение
   * - ``max(column)``
     - Максимальное значение
   * - ``avg(column)``
     - Среднее арифметическое значений

Тип SQL-результата зависит от функции и входной колонки. В приведённом примере ``?num`` задаёт числовое представление результата для потребителя Records API.

Ограничения функций и выражений
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

В версии ``1.19.0-SNAPSHOT``:

* В условиях поиска атрибут разрешается как имя колонки; произвольные SQL-функции в предикате не разбираются.
* ``groupBy`` принимает имена существующих колонок; функциональные выражения в нём не разбираются.
* ``sortBy`` использует имя колонки сортировки; произвольное выражение не вычисляется.
* Вызовы с несколькими аргументами, например ``power(amount,2)``, и выражения вида ``(2 * power(amount,2))`` не поддерживаются описанным механизмом.
* SQL-литералы типов, конструкции ``::``, именованные аргументы ``=>`` и специальный синтаксис ``extract(field from ...)`` нельзя передавать как произвольные выражения атрибутов.
