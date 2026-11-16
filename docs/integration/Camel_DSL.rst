.. _camel_dsl:

Использование Camel DSL
=======================

**Camel DSL в Citeck** позволяет описывать и выполнять интеграционные маршруты Apache Camel в микросервисе **ecos-integrations**. Поддерживаются форматы **YAML DSL** и **XML DSL**. Компоненты Citeck дополняют стандартные средства Camel работой с Records API, событиями платформы, файлами и внешними системами.

Основная единица настройки — **Camel-контекст**: он содержит маршруты, бины и параметры их выполнения. Маршрут задаёт источник сообщений или данных, последовательность обработки и целевые конечные точки (endpoint-ы).

Основные сценарии применения:

- интеграция Citeck с внешними системами через REST, JDBC, RabbitMQ и другие протоколы;
- миграция и синхронизация данных между базами данных;
- обработка событий и сообщений через подписки;
- автоматизация импорта данных из файлов.

Начало работы
--------------

#. Откройте журнал **Camel DSL** в рабочем пространстве администратора: ``v2/journals?journalId=ecos-camel-dsl&viewMode=table&ws=admin$workspace``.
#. Создайте или выберите контекст и задайте формат его содержимого — YAML или XML. Укажите тип запуска:

   - **MANUALLY** — запуск и остановка контекста действиями в журнале;
   - **IMPORT_DATA** — обработка файла через механизм импорта данных с созданием отдельного инстанса контекста.

#. Настройте подключения к внешним системам, учётные данные и маршрут. Пример работы с JDBC приведён в разделе :ref:`Выборка из БД <camel_dsl_bd_selection>`, чтения и записи данных Citeck — в справочнике :ref:`конечных точек <endpoints_dsl>`.
#. Для YAML-маршрута можно открыть :ref:`просмотрщик Kaoto <camel_dsl_visual_editor>`. По умолчанию схема служит для просмотра и навигации, а изменения вносятся в YAML. Визуальное редактирование схемы включается отдельно настройкой ``app/integrations$camel-visual-editing-enabled``.
#. Сохраните контекст и запустите его выбранным способом. Для диагностики используйте :ref:`действия и лог контекста <camel_dsl_actions>`, а для импорта данных — :ref:`журнал инстансов <camel_instance>`.

.. note::

   Для новых маршрутов записи данных через Records API используйте :ref:`ecos-records-mutate <EcosRecordsMutateEndpoint>`. Описанный отдельно бин :ref:`RecordsDaoEndpoint <camel_dsl_records_dao_endpoint>` подавляет ошибки сохранения: успешное завершение его шага не гарантирует, что запись сохранена. Это нужно учитывать перед удалением исходных данных или отметкой об успешном импорте.

Справочники и примеры
----------------------

Раздел включает настройку контекстов, справочники компонентов, конечных точек и процессоров, а также готовые сценарии интеграции. Набор доступных компонентов и параметры зависят от версии и состава поставки. Для встраивания Camel-контекстов в код микросервиса см. :ref:`ecos-camel-core <ecos-camel-core>`.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Общая информация
      :link: camel_dsl_overview
      :link-type: ref

      Camel-контексты, маршруты, компоненты Apache Camel и типы запуска в Citeck.

   .. grid-item-card:: Визуальный просмотрщик маршрутов (Kaoto)
      :link: camel_dsl_visual_editor
      :link-type: ref

      Просмотр Camel-маршрута в виде схемы рядом с YAML на базе Kaoto, навигация по схеме и включение полноценного визуального редактирования.

   .. grid-item-card:: Выборка из БД
      :link: camel_dsl_bd_selection
      :link-type: ref

      Настройка Credentials, источника данных и маршрута для выборки из БД через JDBC.

   .. grid-item-card:: Действия, доступные с Camel DSL
      :link: camel_dsl_actions
      :link-type: ref

      Старт, стоп контекста и просмотр лога последней синхронизации.

   .. grid-item-card:: Инстансы контекста Camel DSL
      :link: camel_instance
      :link-type: ref

      Отдельные запуски импорта данных с типом IMPORT_DATA, журнал инстансов и их состояния.

   .. grid-item-card:: Подключение RecordsDaoEndpoint
      :link: camel_dsl_records_dao_endpoint
      :link-type: ref

      Настройка бина ``RecordsDaoEndpoint`` для обработки XML/CSV/текстовых файлов и ограничения обработки ошибок сохранения.

   .. grid-item-card:: Удаление данных из БД
      :link: camel-dsl-bd-deletion
      :link-type: ref

      Простое удаление записей и удаление после выборки и обработки.

   .. grid-item-card:: Получение сообщений из RabbitMQ
      :link: rabbitmq_camel
      :link-type: ref

      Подключение к очереди RabbitMQ и публикация события Citeck.

   .. grid-item-card:: Подписка на событие Citeck
      :link: camel_subscription
      :link-type: ref

      Подписка на события Citeck с фильтрацией по атрибутам, в том числе по смене статуса.

   .. grid-item-card:: Роутинг из RabbitMQ
      :link: camel-rabbitmq-routing
      :link-type: ref

      Чтение из RabbitMQ, роутинг по jsonPath и переотправка в Citeck Event.

   .. grid-item-card:: Компоненты
      :link: camel_dsl_components
      :link-type: ref

      Схемы URI компонентов Citeck, их роли потребителей и производителей и назначение.

   .. grid-item-card:: Конечные точки
      :link: endpoints_dsl
      :link-type: ref

      Подробное описание endpoint-ов: URI, параметры, входные и выходные данные.

   .. grid-item-card:: Процессоры
      :link: camel_dsl_processors
      :link-type: ref

      Чтение и запись CSV/Excel, преобразование данных, работа с контентом, сопоставление ассоциаций и другие процессоры.

   .. grid-item-card:: Импорт из Jira и GitLab
      :link: camel_dsl_external_import
      :link-type: ref

      Компоненты для переноса задач, комментариев, вложений, спринтов и связанных коммитов.

   .. grid-item-card:: Настройка импорта проектов из Jira
      :link: camel_dsl_jira_import
      :link-type: ref

      Пошаговая настройка синхронизации коммитов и MR из GitLab и импорта проекта из Jira в Project tracker: пример маршрута, маппинг значений и атрибутов, устранение неполадок.

   .. grid-item-card:: Библиотека ecos-camel-core
      :link: ecos-camel-core
      :link-type: ref

      Подключение библиотеки и создание Camel-контекстов в коде микросервиса; координаты зависимости и требования к поставке.

   .. grid-item-card:: Примеры реализации
      :link: camel_dsl_examples
      :link-type: ref

      Импорт из Excel, синхронизация с Bitrix24 CRM, глобальный импорт данных и примеры маршрутов из репозитория ecos-camel.

.. toctree::
    :maxdepth: 2
    :hidden:

    Camel_DSL/overview
    Camel_DSL/visual_editor
    Camel_DSL/BD_selection
    Camel_DSL/actions
    Camel_DSL/context_instance
    Camel_DSL/RecordsDaoEndpoint_connection
    Camel_DSL/BD_deletion
    Camel_DSL/RabbitMQ
    Camel_DSL/subscription
    Camel_DSL/RabbitMQ_routing
    Camel_DSL/components
    Camel_DSL/endpoints
    Camel_DSL/processors
    Camel_DSL/external_import
    Camel_DSL/jira_citeck
    Camel_DSL/ecos-camel-core
    Camel_DSL/examples
