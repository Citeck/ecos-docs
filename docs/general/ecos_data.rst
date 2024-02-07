.. _ecos_data_main:

ECOS Data
=========

.. contents::
   :depth: 3

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
  import ru.citeck.ecos.model.lib.utils.ModelUtils;
  import ru.citeck.ecos.webapp.api.entity.EntityRef;
  import ru.citeck.ecos.records3.record.dao.RecordsDao;
  
  @Configuration
  public class CustomRecordsDaoConfig {
  
      private DbDomainFactory dbDomainFactory;
  
      @Bean
      public RecordsDao customRecordsDao() {
  
          EntityRef typeRef = ModelUtils.getTypeRef("ecos-type-id");
  
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
                          b.withTable("table_name");
                          b.withStoreTableMeta(true);
                          return Unit.INSTANCE;
                      })
                  )
                  .build()
          ).withSchema("schema_name").build();
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
  import ru.citeck.ecos.model.lib.utils.ModelUtils
  import ru.citeck.ecos.records3.record.dao.RecordsDao
  
  @Configuration
  class CustomRecordsDaoConfig(
      private val dbDomainFactory: DbDomainFactory
  ) {
  
      @Bean
      fun customRecordsDao(): RecordsDao {
  
          val typeRef = ModelUtils.getTypeRef("ecos-type-id")
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
                          withTable("table_name")
                          withStoreTableMeta(true)
                      }
                  )
                  .build()
          ).withSchema("schema_name").build()
  
          return recordsDao
      }
  }

Поиск по полям ассоциаций
-------------------------

Если источники данных на базе ecos-data находятся в одном микросервисе, в одной БД и одной схеме, то можно выполнять поиск
с использованием полей из связанных сущностей. Для этого у атрибута-ассоциации должен быть указан тип, в котором sourceId ссылается
на ecos-data источник в той же схеме.

Для поиска по полям из связанных сущностей в предикате нужно указать атрибут в формате ``{имя ассоциации}.{имя поля из связанной сущности}``
Например, если мы хотим найти договоры, у которых имя контрагента содержит строку "ООО", то это можно сделать используя следующий скрипт::

  await Records.query({
    ecosType: 'ecos-contract',
    language: 'predicate',
    query: {
      t: 'contains',
      a: 'counterparty.fullOrganizationName',
      v: 'ООО'
    }
  });

здесь **counterparty** - это ассоциация на контрагента, а **fullOrganizationName** - его имя.

.. _ecos_data_functions:

Запросы с использованием функций
--------------------------------

Если атрибут заканчивается на круглые скобки с любым содержимым (например ``max(attribute)`` или ``count(*)``, то этот атрибут воспринимается
как функция и транслируется в SQL запрос (если речь о SQL бэкенде). 
Функции можно указывать в условиях поиска, для группировки, для сортировки и для получения значения.

Пример запроса::
  
  await Records.query(
    {
      ecosType: 'ecos-contract',
      language: 'predicate',
      query: {
        t: 'contains',
        a: 'counterparty',
        v: 'emodel/counterparty@some-counterparty-id'
      }
    }, 
    {
      amount: 'amount?num',
      poweredAmount: 'power(amount,2)?num' // функция power
    }
  );

Список поддерживаемых функций:

.. raw:: html

   <details>
   <summary><a>Числовые функции</a></summary>

.. list-table::
      :widths: 20 40
      :header-rows: 1
      :class: tight-table 
      
      * - Функция
        - Описание
      * - | ``abs ( number ) → number``
        - | Абсолютное значение
          | ``abs(-17.4) → 17.4``
      * - | ``ceil ( number ) → number``
        - | Ближайшее целое, большее или равное аргументу  
          | ``ceil(42.2) → 43``
          | ``ceil(-42.8) → -42``
      * - | ``ceiling ( number ) → number``
        - | Ближайшее целое, большее или равное аргументу (равнозначно ceil)
          | ``ceiling(95.3) → 96``
      * - | ``div ( y number, x number ) → number``
        - | Целочисленный результат y/x (округлённый в направлении нуля)
          | ``div(9, 4) → 2``
      * - | ``exp ( number ) → number``
        - | Экспонента (e возводится в заданную степень)
          | ``exp(1.0) → 2.7182818284590452``
      * - | ``floor ( number ) → number``
        - | Ближайшее целое, меньшее или равное аргументу
          | ``floor(42.8) → 42``
          | ``floor(-42.8) → -43``
      * - | ``mod ( y number, x number ) → number``
        - | Остаток от деления y/x
          | ``mod(9, 4) → 1``
      * - | ``power ( a number, b number ) → number``
        - | a возводится в степень b
          | ``power(9, 3) → 729``
      * - | ``round ( number ) → numeric``
        - | Округляет до ближайшего целого числа. Для numeric половина (.5) округляется до одного по модулю. 
          | ``round(42.4) → 42``
      * - | ``round ( v number, s number ) → numeric``
        - | Округление v до s десятичных знаков. Половина (.5) округляется до 1 по модулю.
          | ``round(42.4382, 2) → 42.44``
          | ``round(1234.56, -1) → 1230``
      * - | ``sign ( number ) → number``
        - | Знак аргумента (-1, 0 или +1)
          | ``sign(-8.4) → -1``
      * - | ``sqrt ( number ) → number``
        - | Квадратный корень
          | ``sqrt(2) → 1.4142135623730951``
      * - | ``trunc ( number ) → number``
        - | Округление до целого (в направлении нуля)
          | ``trunc(42.8) → 42``
          | ``trunc(-42.8) → -42``

.. raw:: html

   </details>
   <details>
   <summary><a>Строковые функции</a></summary>

.. list-table::
      :widths: 25 40
      :header-rows: 1
      :class: tight-table 

      * - Функция
        - Описание
      * - | ``btrim ( string text [, characters text] ) → text``
        - | Удаляет наибольшую подстроку, содержащую только символы characters (по умолчанию пробел), 
          | с начала и с конца строки string.
          | ``btrim('xyxtrimyyx', 'xyz') → trim``
      * - | ``length ( text ) → integer``
        - | Возвращает число символов в строке.
          | ``char_length('josé') → 4``
      * - | ``initcap ( text ) → text``
        - | Переводит первую букву каждого слова в строке в верхний регистр, а остальные — в нижний. 
          | Словами считаются последовательности алфавитно-цифровых символов, разделённые любыми другими символами.
          | ``initcap('hi THOMAS') → Hi Thomas``
      * - | ``lpad ( string text, length integer [, fill text] ) → text``
        - | Дополняет строку string слева до длины length символами fill (по умолчанию пробелами). 
          | Если длина строки уже больше заданной, она обрезается справа.
          | ``lpad('hi', 5, 'xy') → xyxhi``
      * - | ``ltrim ( string text [, characters text] ) → text``
        - | Удаляет наибольшую подстроку, содержащую только символы characters (по умолчанию пробелы), 
          | с начала строки string.
          | ``ltrim('zzzytest', 'xyz') → test``
      * - | ``repeat ( string text, number integer ) → text``
        - | Повторяет содержимое string указанное число (number) раз.
          | ``repeat('Pg', 4) → PgPgPgPg``
      * - | ``replace ( string text, from text, to text ) → text``
        - | Заменяет все вхождения в string подстроки from подстрокой to.
          | ``replace('abcdefabcdef', 'cd', 'XX') → abXXefabXXef``   
      * - | ``rpad ( string text, length integer [, fill text] ) → text``
        - | Дополняет строку string справа до длины length символами fill (по умолчанию пробелами). Если длина строки уже больше заданной, она обрезается.
          | ``rpad('hi', 5, 'xy') → hixyx``
      * - | ``rtrim ( string text [, characters text] ) → text``
        - | Удаляет наибольшую подстроку, содержащую только символы characters (по умолчанию пробелы), с конца строки string.
          | ``rtrim('testxxzx', 'xyz') → test``
      * - | ``strpos ( string text, substring text ) → integer``
        - | Возвращает начальную позицию первого вхождения substring в строке string либо 0, если такого вхождения нет. 
      * - | ``upper ( text ) → text``
        - | Переводит символы строки в верхний регистр, в соответствии с правилами локали базы данных.
          | ``upper('tom') → TOM``
      * - | ``lower ( text ) → text``
        - | Переводит символы строки в нижний регистр в соответствии с правилами локали базы данных.
          | ``lower('TOM') → tom``

.. raw:: html

   </details>
   <details>
   <summary><a>Функции форматирования данных</a></summary>

.. list-table::
      :widths: 25 40
      :header-rows: 1
      :class: tight-table 
      
      * - Функция
        - Описание
      * - | ``to_char ( timestamp, text ) → text``
          | ``to_char ( timestamp with time zone, text ) → text``
        - | Преобразует время в строку согласно заданному формату.
          | ``to_char(timestamp '2002-04-20 17:31:12.66', 'HH12:MI:SS') → 05:31:12``
      * - | ``to_char ( interval, text ) → text``
        - | Преобразует интервал в строку согласно заданному формату.
          | ``to_char(interval '15h 2m 12s', 'HH24:MI:SS') → 15:02:12``
      * - | ``to_char ( numeric_type, text ) → text``
        - | Преобразует число в строку согласно заданному формату; поддерживаются типы integer, bigint, numeric, real, double precision.
          | ``to_char(125, '999') → 125``
          | ``to_char(125.8::real, '999D9') → 125.8``
          | ``to_char(-125.8, '999D99S') → 125.80-``
      * - | ``to_date ( text, text ) → date``
        - | Преобразует строку в дату согласно заданному формату.
          | ``to_date('05 Dec 2000', 'DD Mon YYYY') → 2000-12-05``
      * - | ``to_number ( text, text ) → numeric``
        - | Преобразует строку в число согласно заданному формату.
          | ``to_number('12,454.8-', '99G999D9S') → -12454.8``
      * - | ``to_timestamp ( text, text ) → timestamp with time zone``
        - | Преобразует строку в значение времени согласно заданному формату.
          | ``to_timestamp('05 Dec 2000', 'DD Mon YYYY') → 2000-12-05 00:00:00-05``

.. raw:: html

   </details>
   <details>
   <summary><a>Функции даты/времени</a></summary>

.. list-table::
      :widths: 25 40
      :header-rows: 1
      :class: tight-table 
      
      * - Функция
        - Описание
      * - | ``age ( timestamp, timestamp ) → interval``
        - | Вычитает аргументы и выдаёт «символический» результат с годами и месяцами, а не просто днями
          | ``age(timestamp '2001-04-10', timestamp '1957-06-13') → 43 years 9 mons 27 days (43 года 9 месяцев 27 дней)``
      * - | ``age ( timestamp ) → interval``
        - | Вычитает аргумент из current_date (полночь текущего дня)
          | ``age(timestamp '1957-06-13') → 62 years 6 mons 10 days (62 года 6 месяцев 10 дней)``
      * - | ``current_date → date``
        - | Текущая дата
          | ``current_date → 2023-12-23``
      * - | ``current_time → time with time zone``
        - | Текущее время суток
          | ``current_time → 14:39:53.662522-05``
      * - | ``current_time ( integer ) → time with time zone``
        - | Текущее время суток (с ограниченной точностью)
          | ``current_time(2) → 14:39:53.66-05``
      * - | ``current_timestamp → timestamp with time zone``
        - | Текущая дата и время (на момент начала транзакции)
          | ``current_timestamp → 2019-12-23 14:39:53.662522-05``
      * - | ``current_timestamp ( integer ) → timestamp with time zone``
        - | Текущие дата и время (на момент начала транзакции; с ограниченной точностью)
          | ``current_timestamp(0) → 2019-12-23 14:39:53-05``
      * - | ``clock_timestamp ( ) → timestamp with time zone``
        - | Текущая дата и время (меняется в процессе выполнения операторов)
          | ``clock_timestamp() → 2019-12-23 14:39:53.662522-05``
      * - | ``date_bin ( interval, timestamp, timestamp ) → timestamp``
        - | Подгоняет заданное значение под интервал, отсчитывая от указанного начального момента
          | ``date_bin('15 minutes', timestamp '2001-02-16 20:38:40', timestamp '2001-02-16 20:05:00') → 2001-02-16 20:35:00``
      * - | ``date_part ( text, timestamp ) → double precision``
        - | Возвращает поле даты/времени (равнозначно extract)
          | ``date_part('hour', timestamp '2001-02-16 20:38:40') → 20``
      * - | ``date_trunc ( text, timestamp ) → timestamp``
        - | Отсекает компоненты даты до заданной точности
          | ``date_trunc('hour', timestamp '2001-02-16 20:38:40') → 2001-02-16 20:00:00``
      * - | ``date_trunc ( text, timestamp with time zone, text ) → timestamp with time zone``
        - | Отсекает компоненты даты до заданной точности в указанном часовом поясе
          | ``date_trunc('day', timestamptz '2001-02-16 20:38:40+00', 'Australia/Sydney') → 2001-02-16 13:00:00+00``
      * - | ``date_trunc ( text, interval ) → interval``
        - | Отсекает компоненты даты до заданной точности
          | ``date_trunc('hour', interval '2 days 3 hours 40 minutes') → 2 days 03:00:00``
      * - | ``isfinite ( date ) → boolean``
        - | Проверяет конечность даты (её отличие от +/-бесконечности)
          | ``isfinite(date '2001-02-16') → true``
      * - | ``isfinite ( timestamp ) → boolean``
        - | Проверяет конечность времени (его отличие от +/-бесконечности)
          | ``isfinite(timestamp 'infinity') → false``
      * - | ``isfinite ( interval ) → boolean``
        - | Проверяет конечность интервала (в настоящее время все интервалы конечны)
          | ``isfinite(interval '4 hours') → true``
      * - | ``justify_days ( interval ) → interval``
        - | Преобразует интервал так, что каждый 30-дневный период считается одним месяцем
          | ``justify_days(interval '35 days') → 1 mon 5 days (1 месяц 5 дней)``
      * - | ``justify_hours ( interval ) → interval``
        - | Преобразует интервал так, что каждый 24-часовой период считается одним днём 
          | ``justify_hours(interval '27 hours') → 1 day 03:00:00 (1 день 03:00:00)``
      * - | ``justify_interval ( interval ) → interval``
        - | Преобразует интервал с применением justify_days и justify_hours и дополнительно корректирует знаки
          | ``justify_interval(interval '1 mon -1 hour') → 29 days 23:00:00 (29 дней 23:00:00)``
      * - | ``make_date ( year int, month int, day int ) → date``
        - | Образует дату из полей: year (год), month (месяц) и day (день) 
          | (отрицательное значение поля year означает год до н. э.)
          | ``make_date(2013, 7, 15) → 2013-07-15``
      * - | ``make_interval ( [years int [, months int [, weeks int [, days int [, hours int [, mins int [, secs double precision]]]]]]] ) → interval``
        - | Образует интервал из полей: years (годы), months (месяцы), weeks (недели), days (дни), hours (часы), 
          | minutes (минуты) и secs (секунды), каждое из которых по умолчанию считается равным нулю.
          | ``make_interval(days => 10) → 10 days``
      * - | ``make_time ( hour int, min int, sec double precision ) → time``
        - | Образует время из полей: hour (час), minute (минута) и sec (секунда)
          | ``make_time(8, 15, 23.5) → 08:15:23.5``
      * - | ``make_timestamp ( year int, month int, day int, hour int, min int, sec double precision ) → timestamp``
        - | Образует момент времени из полей: year (год), month (месяц), day (день), hour (час), 
          | minute (минута) и sec (секунда) (отрицательное значение поля year означает год до н. э.)
          | ``make_timestamp(2013, 7, 15, 8, 15, 23.5) → 2013-07-15 08:15:23.5``
      * - | ``make_timestamptz ( year int, month int, day int, hour int, min int, sec double precision [, timezone text] ) → timestamp with time zone``
        - | Образует дату и время с часовым поясом из полей: year (год), month (месяц), day (день), hour (час), minute (минута) и sec (секунда) (отрицательное значение поля year означает год до н. э.). Если параметр timezone (часовой пояс) не указан, используется текущий часовой пояс; в примерах предполагается часовой пояс Europe/London (Европа/Лондон).
          | ``make_timestamptz(2013, 7, 15, 8, 15, 23.5) → 2013-07-15 08:15:23.5+01``
          | ``make_timestamptz(2013, 7, 15, 8, 15, 23.5, 'America/New_York') → 2013-07-15 13:15:23.5+01``
      * - | ``statement_timestamp ( ) → timestamp with time zone``
        - | Текущая дата и время (на момент начала текущего оператора)
          | ``statement_timestamp() → 2019-12-23 14:39:53.662522-05``
      * - | ``timeofday ( ) → text``
        - | Текущая дата и время (как clock_timestamp, но в виде строки типа text)
          | ``timeofday() → Mon Dec 23 14:39:53.662522 2019 EST``
      * - | ``transaction_timestamp ( ) → timestamp with time zone``
        - | Текущая дата и время (на момент начала транзакции)
          | ``transaction_timestamp() → 2019-12-23 14:39:53.662522-05``
      * - | ``extract ( field from timestamp ) → numeric``
        - | Возвращает поле даты/времени
          | ``extract(hour from timestamp '2001-02-16 20:38:40') → 20``
      * - | ``extract ( field from interval ) → numeric``
        - | Возвращает поле интервала
          | ``extract(month from interval '2 years 3 months') → 3``
      * - | ``localtime → time``
        - | Текущее время суток
          | ``localtime → 14:39:53.662522``
      * - | ``localtime ( integer ) → time``
        - | Текущее время суток (с ограниченной точностью)
          | ``localtime(0) → 14:39:53``
      * - | ``localtimestamp → timestamp``
        - | Текущая дата и время (на момент начала транзакции)
          | ``localtimestamp → 2019-12-23 14:39:53.662522``
      * - | ``localtimestamp ( integer ) → timestamp``
        - | Текущие дата и время (на момент начала транзакции; с ограниченной точностью)
          | ``localtimestamp(2) → 2019-12-23 14:39:53.66``
      * - | ``now ( ) → timestamp with time zone``
        - | Текущая дата и время (на момент начала транзакции)
          | ``now() → 2019-12-23 14:39:53.662522-05``
      * - | ``startOfMonth ( integer ) → date``
        - | Первое число месяца. Аргумент определяет относительный сдвиг в месяцах:
          | 0 - текущий месяц
          | 1 - следующий месяц
          | -1 - предыдущий месяц
      * - | ``endOfMonth ( integer ) → date``
        - | Последнее число месяца. Аргумент определяет относительный сдвиг в месяцах:
          | 0 - текущий месяц
          | 1 - следующий месяц
          | -1 - предыдущий месяц
          
.. raw:: html

   </details>
   <details>
   <summary><a>Случайные функции</a></summary>

.. list-table::
      :widths: 20 40
      :header-rows: 1
      :class: tight-table 

      * - Функция
        - Описание
      * - | ``random ( ) → number``
        - | Возвращает случайное число в диапазоне 0.0 <= x < 1.0
          | ``random() → 0.897124072839091``

.. raw:: html

   </details>
   <details>
   <summary><a>Условные функции</a></summary>

.. list-table::
      :widths: 20 40
      :header-rows: 1
      :class: tight-table 

      * - Функция
        - Описание
      * - | ``COALESCE(значение [, ...])``
        - | Функция COALESCE возвращает первый попавшийся аргумент, отличный от NULL. 
          | Если же все аргументы равны NULL, результатом тоже будет NULL. 
          | Это часто используется при отображении данных для подстановки некоторого 
          | значения по умолчанию вместо значений NULL.
      * - | ``NULLIF(значение1, значение2)``
        - | Функция NULLIF выдаёт значение NULL, если значение1 равно значение2; 
          | в противном случае она возвращает значение1. Это может быть полезно 
          | для реализации обратной операции к COALESCE.
      * - | ``GREATEST(значение [, ...])``
        - | Выбирает наибольшее значение из списка выражений.
      * - | ``LEAST(значение [, ...])``
        - | Выбирает наименьшее значение из списка выражений.

.. raw:: html

   </details>
   <details>
   <summary><a>Агрегатные функции</a></summary>

.. list-table::
      :widths: 20 40
      :header-rows: 1
      :class: tight-table 

      * - Функция
        - Описание
      * - | ``avg ( number ) → numeric``
        - | Вычисляет арифметическое среднее для всех входных значений, отличных от NULL.
      * - | ``count ( * ) → bigint``
        - | Выдаёт количество входных строк.
      * - | ``count ( "any" ) → bigint``
        - | Выдаёт количество входных строк, в которых входное значение отлично от NULL.
      * - | ``max ( см. описание ) → тот же тип, что на входе``
        - | Вычисляет максимальное из всех значений, отличных от NULL. 
          | Имеется для всех числовых и строковых типов, типов-перечислений и даты/времени.
      * - | ``min ( см. описание ) → тот же тип, что на входе``
        - | Вычисляет минимальное из всех значений, отличных от NULL. 
          | Имеется для всех числовых и строковых типов, типов-перечислений и даты/времени.
      * - | ``sum ( number ) → bigint``
        - | Вычисляет сумму всех входных значений, отличных от NULL.

.. raw:: html

   </details>
   <br/>



Использование выражений при поиске
----------------------------------

Если атрибут начинается на ``(`` и заканчивается на ``)``, то между скобками может быть выражение любого уровня сложности
с использованием функций и операторов ``+``, ``-``, ``*``, ``/``

Пример запроса::
  
  await Records.query(
    {
      ecosType: 'ecos-contract',
      language: 'predicate',
      query: {
        t: 'contains',
        a: 'counterparty',
        v: 'emodel/counterparty@some-counterparty-id'
      }
    }, 
    {
      amount: 'amount?num',
      poweredAmount: '(2 * power(amount,2))?num' // возводим в степень и умножаем на два
    }
  );

