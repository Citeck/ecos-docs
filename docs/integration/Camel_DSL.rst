Использование Camel DSL
=======================

**Camel DSL** - это надстройка над Apache Camel, которая адаптирована для работы с платформой Citeck.

Общие сведения
---------------

**Apache Camel** — открытый кроссплатформенный java-фреймворк, который позволяет проводить интеграцию приложений в простой и понятной форме.

Camel использует доменные языки (Domain Specific Language - DSL) для описания проектных шаблонов интеграции или маршрутов. 

В Citeck используется Yaml DSL для описания маршрутов в формате **YAML** и **XML DSL**.

**Camel-контекст** – главная сущность Camel. Контекст является контейнером среды выполнения Camel. Контекст предоставляет много полезных сервисов, наиболее значимыми являются маршруты, компоненты, языки, конверторы типов, реестр, endpointы и форматы данных.

**Маршрут** – определение `интеграционного потока <https://camel.apache.org/manual/routes.html>`_ 
Например, для объединения двух систем маршрут определяет как именно эти системы взаимодействуют.

**Компоненты**  - подробно описано по `ссылке <https://camel.apache.org/components/4.0.x/>`_

  * **Bean** – для вызова методов Java-бинов, хранящихся в реестре;
  * **Direct** – вызывает другой endpoint из того же контекста синхронно;
  * **Direct VM** - вызывает другой endpoint из любого контекста на той же JVM синхронно;
  * **File** – читает и записывает файлы;
  * **Timer** – генерирует сообщения с определенным интервалом, используя java.util.Timer;
  * **JDBC** – предоставляет доступ к базам данных через JDBC;
  * **Jetty** – предоставляет endpoint на основе HTTP для получения и отправки HTTP запросов.

Пример контекста с маршрутом:

.. image:: _static/camel/Camel_1.png
       :width: 600
       :align: center    

|

.. note::
    Атрибут = свойство = поле

    Целевая БД = БД назначения = целевой источник данных – куда данные помещаются

    Исходная БД = исходный источник данных – откуда данные берутся


.. toctree::
    :maxdepth: 3

    Camel_DSL/BD_selection
    Camel_DSL/actions
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

