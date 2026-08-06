.. _camel_dsl:

Использование Camel DSL
=======================

**Camel DSL** — надстройка над Apache Camel, адаптированная для работы с платформой Citeck. Инструмент позволяет описывать интеграционные маршруты в форматах **YAML DSL** и **XML DSL** и использует ключевые концепции Apache Camel: контексты, маршруты, компоненты и endpoint-ы.

Основные сценарии применения:

- интеграция Citeck с внешними системами через REST, JDBC, RabbitMQ и другие протоколы;
- миграция и синхронизация данных между базами данных;
- обработка событий и сообщений через подписки;
- автоматизация импорта данных из файлов.

В данном разделе описаны ключевые возможности Camel DSL в Citeck: настройка контекстов и маршрутов, доступные компоненты, endpoint-ы и процессоры, а также интеграция с ECOS Records через ``RecordsDaoEndpoint``.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Общая информация
      :link: camel_dsl_overview
      :link-type: ref

      Camel-контексты, маршруты, компоненты Apache Camel и типы запуска в Citeck.

   .. grid-item-card:: Визуальный просмотрщик маршрутов (Kaoto)
      :link: camel_dsl_visual_editor
      :link-type: ref

      Просмотр Camel-маршрута в виде схемы рядом с YAML на базе Kaoto.

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

      Журнал запущенных инстансов контекста и их возможные состояния.

   .. grid-item-card:: Подключение RecordsDaoEndpoint
      :link: camel_dsl_records_dao_endpoint
      :link-type: ref

      Запись данных в RecordsDao через бин ``RecordsDaoEndpoint``, в том числе из XML/CSV/текстовых файлов.

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

      Camel-компоненты для подключения маршрутов к внешним системам, включая EcosRecordsSync.

   .. grid-item-card:: Конечные точки
      :link: endpoints_dsl
      :link-type: ref

      FileFromCamelDslEndpoint, EcosRecordsSyncConsumer, EcosRecordsMutateEndpoint и другие endpoint-ы.

   .. grid-item-card:: Процессоры
      :link: camel_dsl_processors
      :link-type: ref

      Обработка CSV/Excel-данных, сопоставление ассоциаций и другие процессоры Camel DSL.

   .. grid-item-card:: Библиотека ecos-camel-core
      :link: ecos-camel-core
      :link-type: ref

      Встраивание Camel-контекстов напрямую в код микросервиса (требует enterprise-лицензию).

   .. grid-item-card:: Примеры реализации
      :link: camel_dsl_examples
      :link-type: ref

      Импорт из Excel, синхронизация с Bitrix24 CRM, глобальный импорт данных.

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
    Camel_DSL/ecos-camel-core
    Camel_DSL/examples



