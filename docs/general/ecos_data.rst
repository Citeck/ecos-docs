.. _ecos_data_main:

ECOS Data
=========

**ecos-data** - это библиотека, которая позволяет добавлять новые Records DAO, записи которых будут храниться в БД.
Библиотека на основе атрибутов в :ref:`ECOS типе<data_types_main>` автоматически создает таблицы и предоставляет базовые операции над записями:

1. Создание новых записей;
2. Получение атрибутов у записей по их ID;
3. Поиск записей с использованием :ref:`языка предикатов<ecos-predicate_main>`;

Поддерживаемые БД:

.. csv-table::

    Тип,Версия
    PostgreSQL,9.4+

Хранение данных в ecos-model
------------------------------

В ECOS по умолчанию для типов предусмотрено хранение в микросервисе **ecos-model**. Для этого достаточно на форме типа
выбрать тип источника данных "ECOS Model". Микросервис ecos-model для всех подобных типов автоматически создаст RecordsDAO
с идентификатором (sourceId), который формируется по следующим правилам:

1. Берем id типа и меняем camelCase на kebab-case;
2. Переводим id в нижний регистр;
3. Заменяем все специальные символы на ``-``;
4. Убираем все задублировавшиеся символы ``-`` заменяя их на одинарные (т.е. ``--`` заменяем на ``-``);
5. Если длина полученного id получилась больше 42х символов, то берем первые 34 символа из id, добавляем ``-`` плюс контрольная сумма оставшихся символов в идентификаторе;
6. Убираем символ ``-`` в начале идентификатора и в конце если он там есть

Примеры::

  camelCaseTest -> camel-case-test
  kebab-case-id -> kebab-case-id
  a----b- -> a-b
  $$$-abc-$$$ -> abc

При создании типа с sourceId, который конфликтует с существующими будет показана ошибка. 
Чтобы проверить список зарегистрированных sourceId можно выполнить следующий скрипт в консоли браузера::
  
  await Citeck.Records.query({sourceId: 'emodel/src', query: {}, language:'predicate'}, '?localId')

Создание нового RecordsDAO в своем микросервисе
------------------------------------------------

Для создания нового RecordsDAO в своем микросервисе нужно добавить следующую Spring конфигурацию

Java::

  import kotlin.Unit;
  import org.springframework.beans.factory.annotation.Autowired;
  import org.springframework.context.annotation.Bean;
  import org.springframework.context.annotation.Configuration;
  import ru.citeck.ecos.data.sql.domain.DbDomainConfig;
  import ru.citeck.ecos.data.sql.domain.DbDomainFactory;
  import ru.citeck.ecos.data.sql.dto.DbTableRef;
  import ru.citeck.ecos.data.sql.records.DbRecordsDaoConfig;
  import ru.citeck.ecos.data.sql.service.DbDataServiceConfig;
  import ru.citeck.ecos.model.lib.type.service.utils.TypeUtils;
  import ru.citeck.ecos.records2.RecordRef;
  import ru.citeck.ecos.records3.record.dao.RecordsDao;
  
  @Configuration
  public class CustomRecordsDaoConfig {
  
      private DbDomainFactory dbDomainFactory;
  
      @Bean
      public RecordsDao customRecordsDao() {
  
          RecordRef typeRef = TypeUtils.getTypeRef("ecos-type-id");
  
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
                          b.withAuthEnabled(false);
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

Kotlin::

  import org.springframework.context.annotation.Bean
  import org.springframework.context.annotation.Configuration
  import ru.citeck.ecos.data.sql.domain.DbDomainConfig
  import ru.citeck.ecos.data.sql.domain.DbDomainFactory
  import ru.citeck.ecos.data.sql.dto.DbTableRef
  import ru.citeck.ecos.data.sql.records.DbRecordsDaoConfig
  import ru.citeck.ecos.data.sql.service.DbDataServiceConfig
  import ru.citeck.ecos.model.lib.type.service.utils.TypeUtils
  import ru.citeck.ecos.records3.record.dao.RecordsDao
  
  @Configuration
  class CustomRecordsDaoConfig(
      private val dbDomainFactory: DbDomainFactory
  ) {
  
      @Bean
      fun customRecordsDao(): RecordsDao {
  
          val typeRef = TypeUtils.getTypeRef("ecos-type-id")
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
                          withAuthEnabled(false)
                          withTableRef(DbTableRef("schema_name", "table_name"))
                          withStoreTableMeta(true)
                      }
                  )
                  .build()
          ).build()
  
          return recordsDao
      }
  }
