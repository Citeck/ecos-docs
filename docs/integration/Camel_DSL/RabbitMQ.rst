.. _rabbitmq_camel:

Получение сообщений из RabbitMQ и отправка события Citeck
=========================================================

Пример демонстрирует базовый сценарий интеграции через RabbitMQ:

1. Подключение к очереди RabbitMQ с использованием credentials из ECOS Endpoint.
2. Удаление служебных заголовков RabbitMQ перед дальнейшей обработкой.
3. Логирование входящего сообщения.
4. Публикация события Citeck с телом, сформированным из тела сообщения.

.. note::

   Для работы примера необходимо:

   - Создать **секрет** (Модель → Секреты) с данными для подключения к RabbitMQ.
   - Создать **endpoint** (Модель → Конечные точки) с id ``rabbitmq-endpoint`` и указать созданный секрет.
   - Зайти в **журнал Camel DSL** (Интеграция → Camel DSL) и создать новый контекст с конфигурацией ниже.

.. code-block:: yaml

   - beans:
       # Бин подключения к RabbitMQ на основе данных из ECOS Endpoint
       - name: rabbitConnectionFactory
         type: org.springframework.amqp.rabbit.connection.CachingConnectionFactory
         properties:
           uri: '{{ecos-endpoint:rabbitmq-endpoint/url}}'
           username: '{{ecos-endpoint:rabbitmq-endpoint/credentials/username}}'
           password: '{{ecos-endpoint:rabbitmq-endpoint/credentials/password}}'

   - route:
       from:
         # "default" — дефолтный exchange в RabbitMQ (обычно обозначается пустой строкой,
         # но Camel требует явного значения "default")
         uri: "spring-rabbitmq:default"
         parameters:
           connectionFactory: '#bean:rabbitConnectionFactory'
           queues: test-queue
         steps:
           # Удаление заголовков RabbitMQ — актуально, если сообщение будет переотправлено в RMQ
           - removeHeaders:
               pattern: "CamelRabbitmq*"
           # Логирование входящего сообщения
           - to: "log:rmq-test"
           # Отправка события типа "test-event-type".
           # В теле передаётся DataValue.of(exchange.message.body)
           - to: "ecos-event:test-event-type"
