.. _camel_dsl:

Использование Camel DSL
=======================

**Camel DSL** — надстройка над Apache Camel, адаптированная для работы с платформой Citeck ECOS. Инструмент позволяет описывать интеграционные маршруты в форматах **YAML DSL** и **XML DSL** и использует ключевые концепции Apache Camel: контексты, маршруты, компоненты и endpoint-ы.

Основные сценарии применения:

- интеграция Citeck с внешними системами через REST, JDBC, RabbitMQ и другие протоколы;
- миграция и синхронизация данных между базами данных;
- обработка событий и сообщений через подписки;
- автоматизация импорта данных из файлов.

В данном разделе описаны ключевые возможности Camel DSL в Citeck: настройка контекстов и маршрутов, доступные компоненты, endpoint-ы и процессоры, а также интеграция с ECOS Records через ``RecordsDaoEndpoint``.

.. toctree::
    :maxdepth: 2

    Camel_DSL/overview
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



