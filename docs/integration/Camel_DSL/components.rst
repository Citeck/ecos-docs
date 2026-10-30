.. _camel_dsl_components:

Компоненты
====================

**Компоненты** используются для подключения маршрутов к внешним системам и сервисам.

Подробнее: `Apache Camel Components <https://camel.apache.org/manual/component.html>`_

Помимо стандартных компонентов Apache Camel, в Citeck доступны компоненты, перечисленные ниже. Ключ компонента — это префикс схемы в URI маршрута, например ``ecos-records-mutate:`` в шаге ``to``.

.. list-table::
   :widths: 10 10 30
   :header-rows: 1
   :class: tight-table

   * - Ключ компонента
     - Роль
     - Назначение
   * - :ref:`ecos-event <EcosEventEndpoint>`
     - Потребитель и производитель
     - Подписка на события ECOS и публикация событий
   * - :ref:`ecos-records-sync-consumer <camel_ecos_records_sync_consumer>`
     - Потребитель
     - Последовательная выгрузка записей из источника данных с сохранением состояния
   * - :ref:`ecos-records-query <EcosRecordsQueryEndpoint>`
     - Производитель
     - Выполнение запроса к RecordsAPI и получение записей с атрибутами
   * - :ref:`ecos-records-mutate <EcosRecordsMutateEndpoint>`
     - Производитель
     - Создание и изменение записей через RecordsAPI
   * - :ref:`ecos-records-delete <EcosRecordsDeleteEndpoint>`
     - Производитель
     - Удаление записей через RecordsAPI
   * - :ref:`ecos-attributes-mapper <EcosAttributesMapperEndpoint>`
     - Производитель
     - Приведение строковых значений атрибутов к модели атрибутов ECOS-типа
   * - :ref:`ecos-ftp <EcosFtpEndpoint>`
     - Потребитель и производитель
     - Работа с FTP/SFTP/FTPS, где адрес и учетные данные берутся из конечной точки ECOS
   * - :ref:`file-from-camel-dsl <camel_file_from_camel_dsl>`
     - Потребитель
     - Чтение содержимого файла, вложенного в саму запись Camel DSL
   * - :ref:`ecos-excel-stream-read <EcosExcelStreamReadEndpoint>`
     - Потребитель
     - Потоковое чтение XLSX-файла по строкам пачками
   * - :ref:`gitlab-commits-sync <camel_dsl_external_import>`
     - Потребитель
     - Периодическая выгрузка коммитов из GitLab
   * - :ref:`gitlab-merge-requests-sync <camel_dsl_external_import>`
     - Потребитель
     - Периодическая выгрузка запросов на слияние из GitLab
   * - :ref:`jira-issues <camel_dsl_external_import>`
     - Потребитель
     - Периодическая выгрузка задач из проектов Jira
   * - :ref:`import-jira-releases <camel_dsl_external_import>`
     - Производитель
     - Создание релизов ECOS из версий задачи Jira
   * - :ref:`import-jira-attachment <camel_dsl_external_import>`
     - Производитель
     - Перенос вложений задачи Jira в ECOS
   * - :ref:`import-jira-dev-info <camel_dsl_external_import>`
     - Производитель
     - Перенос связанных коммитов и запросов на слияние
   * - :ref:`import-jira-component <camel_dsl_external_import>`
     - Производитель
     - Создание компонентов ECOS из компонентов задачи Jira
   * - :ref:`import-jira-sprint <camel_dsl_external_import>`
     - Производитель
     - Создание спринтов ECOS из спринта задачи Jira
   * - :ref:`import-jira-tags <camel_dsl_external_import>`
     - Производитель
     - Создание меток ECOS из меток задачи Jira
   * - :ref:`transform-jira-issue <camel_dsl_external_import>`
     - Производитель
     - Преобразование задачи Jira в набор атрибутов задачи EPT
   * - :ref:`transform-jira-comment <camel_dsl_external_import>`
     - Производитель
     - Преобразование комментариев задачи Jira
   * - :ref:`transform-jira-worklog <camel_dsl_external_import>`
     - Производитель
     - Преобразование записей о затраченном времени

.. note::

  Ранее существовал компонент с ключом **ecos-records-sync**, совмещавший потребителя и производителя. Он удален. Для чтения записей используйте :ref:`ecos-records-sync-consumer <camel_ecos_records_sync_consumer>`, для записи — :ref:`ecos-records-mutate <EcosRecordsMutateEndpoint>` и :ref:`ecos-records-delete <EcosRecordsDeleteEndpoint>`.
