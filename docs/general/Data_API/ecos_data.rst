.. _ecos_data_main:

Citeck Data
=============

.. contents::
   :depth: 3

**ecos-data** — a library that allows adding new Records DAOs whose records are stored in a database.
Based on the attributes in the :ref:`data type <data_types_main>`, the library automatically creates tables and provides basic operations on records:

1. Creating new records.
2. Retrieving attributes of records by their ID.
3. Searching for records using the :ref:`predicate language <ecos-predicate_main>`.

Supported databases:

.. csv-table::

    Type,Version
    PostgreSQL,9.4+

Storing data in ecos-model
----------------------------------------------

In ECOS, data storage for types defaults to the **ecos-model** microservice. To enable this, simply select the "ECOS Model" data
source type on the type form. The ecos-model microservice will automatically create a RecordsDAO
with an identifier (sourceId) for all such types, formed according to the following rules:

1. Take the type id and convert camelCase to kebab-case.
2. Convert the id to lowercase.
3. Replace all special characters with ``-``.
4. Remove all duplicated ``-`` characters by replacing them with single ones (i.e. replace ``--`` with ``-``).
5. If the resulting id is longer than 42 characters, take the first 34 characters of the id, append ``-`` plus the checksum of the remaining characters in the identifier.
6. Remove the ``-`` character from the beginning and end of the identifier if present.

Examples::

  camelCaseTest -> camel-case-test
  kebab-case-id -> kebab-case-id
  a----b- -> a-b
  $$$-abc-$$$ -> abc

When creating a type with a sourceId that conflicts with an existing one, an error will be shown.
To check the list of registered sourceIds, run the following script in the browser console:

.. code-block:: javascript

  await Records.query({sourceId: 'emodel/src', query: {}, language:'predicate'}, '?localId')

.. _new_RecordsDAO:

Creating a new RecordsDAO in your own microservice
--------------------------------------------------------------------------------

To create a new RecordsDAO in your own microservice, add the following Spring configuration:

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

.. code-block:: kotlin

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

Searching by association fields
------------------------------------------------

If ecos-data-based data sources are located in the same microservice, the same database, and the same schema, you can search
using fields from related entities. To do this, the association attribute must have a type specified
whose sourceId references an ecos-data source in the same schema.

To search by fields from related entities, specify the attribute in the predicate using the format ``{association name}.{field name from the related entity}``
For example, to find contracts whose counterparty name contains the string "LLC", use the following script:

.. code-block:: javascript

  await Records.query({
    ecosType: 'ecos-contract',
    language: 'predicate',
    query: {
      t: 'contains',
      a: 'counterparty.fullOrganizationName',
      v: 'LLC'
    }
  });

here **counterparty** is the association to the counterparty, and **fullOrganizationName** is its name.

.. _ecos_data_functions:

Queries using functions
----------------------------------------------------------------

If an attribute ends with parentheses containing any content (for example ``max(attribute)`` or ``count(*)``, it is treated
as a function and translated into an SQL query (when using an SQL backend).
Functions can be used in search conditions, for grouping, sorting, and retrieving values.

Example query:

.. code-block:: javascript

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
      poweredAmount: 'power(amount,2)?num' // power function
    }
  );

List of supported functions:

.. raw:: html

   <details>
   <summary><a>Numeric functions</a></summary>

.. list-table::
      :widths: 20 40
      :header-rows: 1
      :class: tight-table

      * - Function
        - Description
      * - | ``abs ( number ) → number``
        - | Absolute value
          | ``abs(-17.4) → 17.4``
      * - | ``ceil ( number ) → number``
        - | Nearest integer greater than or equal to the argument
          | ``ceil(42.2) → 43``
          | ``ceil(-42.8) → -42``
      * - | ``ceiling ( number ) → number``
        - | Nearest integer greater than or equal to the argument (equivalent to ceil)
          | ``ceiling(95.3) → 96``
      * - | ``div ( y number, x number ) → number``
        - | Integer result of y/x (truncated toward zero)
          | ``div(9, 4) → 2``
      * - | ``exp ( number ) → number``
        - | Exponential (e raised to the given power)
          | ``exp(1.0) → 2.7182818284590452``
      * - | ``floor ( number ) → number``
        - | Nearest integer less than or equal to the argument
          | ``floor(42.8) → 42``
          | ``floor(-42.8) → -43``
      * - | ``mod ( y number, x number ) → number``
        - | Remainder of y/x
          | ``mod(9, 4) → 1``
      * - | ``power ( a number, b number ) → number``
        - | a raised to the power of b
          | ``power(9, 3) → 729``
      * - | ``round ( number ) → numeric``
        - | Rounds to the nearest integer. For numeric, half (.5) rounds away from zero.
          | ``round(42.4) → 42``
      * - | ``round ( v number, s number ) → numeric``
        - | Rounds v to s decimal places. Half (.5) rounds away from zero.
          | ``round(42.4382, 2) → 42.44``
          | ``round(1234.56, -1) → 1230``
      * - | ``sign ( number ) → number``
        - | Sign of the argument (-1, 0, or +1)
          | ``sign(-8.4) → -1``
      * - | ``sqrt ( number ) → number``
        - | Square root
          | ``sqrt(2) → 1.4142135623730951``
      * - | ``trunc ( number ) → number``
        - | Truncates to an integer (toward zero)
          | ``trunc(42.8) → 42``
          | ``trunc(-42.8) → -42``

.. raw:: html

   </details>
   <details>
   <summary><a>String functions</a></summary>

.. list-table::
      :widths: 25 40
      :header-rows: 1
      :class: tight-table

      * - Function
        - Description
      * - | ``btrim ( string text [, characters text] ) → text``
        - | Removes the longest substring containing only the characters in characters (a space by default),
          | from the beginning and end of the string string.
          | ``btrim('xyxtrimyyx', 'xyz') → trim``
      * - | ``length ( text ) → integer``
        - | Returns the number of characters in the string.
          | ``char_length('josé') → 4``
      * - | ``initcap ( text ) → text``
        - | Converts the first letter of each word in the string to uppercase and the rest to lowercase.
          | Words are sequences of alphanumeric characters separated by any other characters.
          | ``initcap('hi THOMAS') → Hi Thomas``
      * - | ``lpad ( string text, length integer [, fill text] ) → text``
        - | Pads string string on the left to length length with fill characters (spaces by default).
          | If the string is already longer than the specified length, it is truncated on the right.
          | ``lpad('hi', 5, 'xy') → xyxhi``
      * - | ``ltrim ( string text [, characters text] ) → text``
        - | Removes the longest substring containing only the characters in characters (spaces by default),
          | from the beginning of the string string.
          | ``ltrim('zzzytest', 'xyz') → test``
      * - | ``repeat ( string text, number integer ) → text``
        - | Repeats the content of string the specified number of times.
          | ``repeat('Pg', 4) → PgPgPgPg``
      * - | ``replace ( string text, from text, to text ) → text``
        - | Replaces all occurrences of substring from with substring to in string.
          | ``replace('abcdefabcdef', 'cd', 'XX') → abXXefabXXef``
      * - | ``rpad ( string text, length integer [, fill text] ) → text``
        - | Pads string string on the right to length length with fill characters (spaces by default). If the string is already longer than the specified length, it is truncated.
          | ``rpad('hi', 5, 'xy') → hixyx``
      * - | ``rtrim ( string text [, characters text] ) → text``
        - | Removes the longest substring containing only the characters in characters (spaces by default) from the end of the string string.
          | ``rtrim('testxxzx', 'xyz') → test``
      * - | ``strpos ( string text, substring text ) → integer``
        - | Returns the starting position of the first occurrence of substring in string, or 0 if no such occurrence exists.
      * - | ``upper ( text ) → text``
        - | Converts the characters of the string to uppercase, according to the database locale rules.
          | ``upper('tom') → TOM``
      * - | ``lower ( text ) → text``
        - | Converts the characters of the string to lowercase according to the database locale rules.
          | ``lower('TOM') → tom``

.. raw:: html

   </details>
   <details>
   <summary><a>Data formatting functions</a></summary>

.. list-table::
      :widths: 25 40
      :header-rows: 1
      :class: tight-table

      * - Function
        - Description
      * - | ``to_char ( timestamp, text ) → text``
          | ``to_char ( timestamp with time zone, text ) → text``
        - | Converts a timestamp to a string according to the given format.
          | ``to_char(timestamp '2002-04-20 17:31:12.66', 'HH12:MI:SS') → 05:31:12``
      * - | ``to_char ( interval, text ) → text``
        - | Converts an interval to a string according to the given format.
          | ``to_char(interval '15h 2m 12s', 'HH24:MI:SS') → 15:02:12``
      * - | ``to_char ( numeric_type, text ) → text``
        - | Converts a number to a string according to the given format; supported types are integer, bigint, numeric, real, double precision.
          | ``to_char(125, '999') → 125``
          | ``to_char(125.8::real, '999D9') → 125.8``
          | ``to_char(-125.8, '999D99S') → 125.80-``
      * - | ``to_date ( text, text ) → date``
        - | Converts a string to a date according to the given format.
          | ``to_date('05 Dec 2000', 'DD Mon YYYY') → 2000-12-05``
      * - | ``to_number ( text, text ) → numeric``
        - | Converts a string to a number according to the given format.
          | ``to_number('12,454.8-', '99G999D9S') → -12454.8``
      * - | ``to_timestamp ( text, text ) → timestamp with time zone``
        - | Converts a string to a timestamp according to the given format.
          | ``to_timestamp('05 Dec 2000', 'DD Mon YYYY') → 2000-12-05 00:00:00-05``

.. raw:: html

   </details>
   <details>
   <summary><a>Date/time functions</a></summary>

.. list-table::
      :widths: 25 40
      :header-rows: 1
      :class: tight-table

      * - Function
        - Description
      * - | ``age ( timestamp, timestamp ) → interval``
        - | Subtracts the arguments and returns a "symbolic" result with years and months rather than just days
          | ``age(timestamp '2001-04-10', timestamp '1957-06-13') → 43 years 9 mons 27 days``
      * - | ``age ( timestamp ) → interval``
        - | Subtracts the argument from current_date (midnight of the current day)
          | ``age(timestamp '1957-06-13') → 62 years 6 mons 10 days``
      * - | ``current_date → date``
        - | Current date
          | ``current_date → 2023-12-23``
      * - | ``current_time → time with time zone``
        - | Current time of day
          | ``current_time → 14:39:53.662522-05``
      * - | ``current_time ( integer ) → time with time zone``
        - | Current time of day (with limited precision)
          | ``current_time(2) → 14:39:53.66-05``
      * - | ``current_timestamp → timestamp with time zone``
        - | Current date and time (at the start of the transaction)
          | ``current_timestamp → 2019-12-23 14:39:53.662522-05``
      * - | ``current_timestamp ( integer ) → timestamp with time zone``
        - | Current date and time (at the start of the transaction; with limited precision)
          | ``current_timestamp(0) → 2019-12-23 14:39:53-05``
      * - | ``clock_timestamp ( ) → timestamp with time zone``
        - | Current date and time (changes during statement execution)
          | ``clock_timestamp() → 2019-12-23 14:39:53.662522-05``
      * - | ``date_bin ( interval, timestamp, timestamp ) → timestamp``
        - | Bins the given value into the specified interval, counting from the indicated origin
          | ``date_bin('15 minutes', timestamp '2001-02-16 20:38:40', timestamp '2001-02-16 20:05:00') → 2001-02-16 20:35:00``
      * - | ``date_part ( text, timestamp ) → double precision``
        - | Returns a date/time field (equivalent to extract)
          | ``date_part('hour', timestamp '2001-02-16 20:38:40') → 20``
      * - | ``date_trunc ( text, timestamp ) → timestamp``
        - | Truncates date components to the specified precision
          | ``date_trunc('hour', timestamp '2001-02-16 20:38:40') → 2001-02-16 20:00:00``
      * - | ``date_trunc ( text, timestamp with time zone, text ) → timestamp with time zone``
        - | Truncates date components to the specified precision in the given time zone
          | ``date_trunc('day', timestamptz '2001-02-16 20:38:40+00', 'Australia/Sydney') → 2001-02-16 13:00:00+00``
      * - | ``date_trunc ( text, interval ) → interval``
        - | Truncates date components to the specified precision
          | ``date_trunc('hour', interval '2 days 3 hours 40 minutes') → 2 days 03:00:00``
      * - | ``isfinite ( date ) → boolean``
        - | Tests for finite date (not +/-infinity)
          | ``isfinite(date '2001-02-16') → true``
      * - | ``isfinite ( timestamp ) → boolean``
        - | Tests for finite timestamp (not +/-infinity)
          | ``isfinite(timestamp 'infinity') → false``
      * - | ``isfinite ( interval ) → boolean``
        - | Tests for finite interval (currently all intervals are finite)
          | ``isfinite(interval '4 hours') → true``
      * - | ``justify_days ( interval ) → interval``
        - | Adjusts the interval so that each 30-day period is counted as one month
          | ``justify_days(interval '35 days') → 1 mon 5 days``
      * - | ``justify_hours ( interval ) → interval``
        - | Adjusts the interval so that each 24-hour period is counted as one day
          | ``justify_hours(interval '27 hours') → 1 day 03:00:00``
      * - | ``justify_interval ( interval ) → interval``
        - | Adjusts the interval using justify_days and justify_hours, and additionally corrects signs
          | ``justify_interval(interval '1 mon -1 hour') → 29 days 23:00:00``
      * - | ``make_date ( year int, month int, day int ) → date``
        - | Creates a date from fields: year, month, and day
          | (a negative year value denotes a BC year)
          | ``make_date(2013, 7, 15) → 2013-07-15``
      * - | ``make_interval ( [years int [, months int [, weeks int [, days int [, hours int [, mins int [, secs double precision]]]]]]] ) → interval``
        - | Creates an interval from fields: years, months, weeks, days, hours,
          | minutes, and secs (seconds), each of which defaults to zero.
          | ``make_interval(days => 10) → 10 days``
      * - | ``make_time ( hour int, min int, sec double precision ) → time``
        - | Creates a time from fields: hour, minute, and sec (second)
          | ``make_time(8, 15, 23.5) → 08:15:23.5``
      * - | ``make_timestamp ( year int, month int, day int, hour int, min int, sec double precision ) → timestamp``
        - | Creates a timestamp from fields: year, month, day, hour,
          | minute, and sec (second) (a negative year value denotes a BC year)
          | ``make_timestamp(2013, 7, 15, 8, 15, 23.5) → 2013-07-15 08:15:23.5``
      * - | ``make_timestamptz ( year int, month int, day int, hour int, min int, sec double precision [, timezone text] ) → timestamp with time zone``
        - | Creates a timestamp with time zone from fields: year, month, day, hour, minute, and sec (second) (a negative year value denotes a BC year). If the timezone parameter is not specified, the current time zone is used; the examples assume the Europe/London time zone.
          | ``make_timestamptz(2013, 7, 15, 8, 15, 23.5) → 2013-07-15 08:15:23.5+01``
          | ``make_timestamptz(2013, 7, 15, 8, 15, 23.5, 'America/New_York') → 2013-07-15 13:15:23.5+01``
      * - | ``statement_timestamp ( ) → timestamp with time zone``
        - | Current date and time (at the start of the current statement)
          | ``statement_timestamp() → 2019-12-23 14:39:53.662522-05``
      * - | ``timeofday ( ) → text``
        - | Current date and time (like clock_timestamp, but returned as a text string)
          | ``timeofday() → Mon Dec 23 14:39:53.662522 2019 EST``
      * - | ``transaction_timestamp ( ) → timestamp with time zone``
        - | Current date and time (at the start of the transaction)
          | ``transaction_timestamp() → 2019-12-23 14:39:53.662522-05``
      * - | ``extract ( field from timestamp ) → numeric``
        - | Returns a date/time field
          | ``extract(hour from timestamp '2001-02-16 20:38:40') → 20``
      * - | ``extract ( field from interval ) → numeric``
        - | Returns an interval field
          | ``extract(month from interval '2 years 3 months') → 3``
      * - | ``localtime → time``
        - | Current time of day
          | ``localtime → 14:39:53.662522``
      * - | ``localtime ( integer ) → time``
        - | Current time of day (with limited precision)
          | ``localtime(0) → 14:39:53``
      * - | ``localtimestamp → timestamp``
        - | Current date and time (at the start of the transaction)
          | ``localtimestamp → 2019-12-23 14:39:53.662522``
      * - | ``localtimestamp ( integer ) → timestamp``
        - | Current date and time (at the start of the transaction; with limited precision)
          | ``localtimestamp(2) → 2019-12-23 14:39:53.66``
      * - | ``now ( ) → timestamp with time zone``
        - | Current date and time (at the start of the transaction)
          | ``now() → 2019-12-23 14:39:53.662522-05``
      * - | ``startOfMonth ( integer ) → date``
        - | First day of the month. The argument defines the relative offset in months:
          | 0 — current month
          | 1 — next month
          | -1 — previous month
      * - | ``endOfMonth ( integer ) → date``
        - | Last day of the month. The argument defines the relative offset in months:
          | 0 — current month
          | 1 — next month
          | -1 — previous month

.. raw:: html

   </details>
   <details>
   <summary><a>Random functions</a></summary>

.. list-table::
      :widths: 20 40
      :header-rows: 1
      :class: tight-table

      * - Function
        - Description
      * - | ``random ( ) → number``
        - | Returns a random number in the range 0.0 <= x < 1.0
          | ``random() → 0.897124072839091``

.. raw:: html

   </details>
   <details>
   <summary><a>Conditional functions</a></summary>

.. list-table::
      :widths: 20 40
      :header-rows: 1
      :class: tight-table

      * - Function
        - Description
      * - | ``COALESCE(value [, ...])``
        - | The COALESCE function returns the first non-NULL argument.
          | If all arguments are NULL, the result is also NULL.
          | This is often used when displaying data to substitute a default
          | value in place of NULL values.
      * - | ``NULLIF(value1, value2)``
        - | The NULLIF function returns NULL if value1 equals value2;
          | otherwise it returns value1. This can be useful
          | for implementing the inverse operation of COALESCE.
      * - | ``GREATEST(value [, ...])``
        - | Selects the largest value from a list of expressions.
      * - | ``LEAST(value [, ...])``
        - | Selects the smallest value from a list of expressions.

.. raw:: html

   </details>
   <details>
   <summary><a>Aggregate functions</a></summary>

.. list-table::
      :widths: 20 40
      :header-rows: 1
      :class: tight-table

      * - Function
        - Description
      * - | ``avg ( number ) → numeric``
        - | Computes the arithmetic mean of all non-NULL input values.
      * - | ``count ( * ) → bigint``
        - | Returns the number of input rows.
      * - | ``count ( "any" ) → bigint``
        - | Returns the number of input rows in which the input value is not NULL.
      * - | ``max ( see description ) → same type as input``
        - | Computes the maximum of all non-NULL input values.
          | Available for all numeric and string types, enumeration types, and date/time types.
      * - | ``min ( see description ) → same type as input``
        - | Computes the minimum of all non-NULL input values.
          | Available for all numeric and string types, enumeration types, and date/time types.
      * - | ``sum ( number ) → bigint``
        - | Computes the sum of all non-NULL input values.

.. raw:: html

   </details>
   <br/>



Using expressions in search
------------------------------------------------------------------

If an attribute starts with ``(`` and ends with ``)``, the expression between the parentheses can be of any complexity,
using functions and the operators ``+``, ``-``, ``*``, ``/``

Example query:

.. code-block:: javascript

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
      poweredAmount: '(2 * power(amount,2))?num' // raise to power and multiply by two
    }
  );
