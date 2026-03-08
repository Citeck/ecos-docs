.. _camel-rabbitmq-routing:

Чтение из RabbitMQ, роутинг по jsonPath и переотправка в Citeck Event
======================================================================

Пример демонстрирует типичный сценарий интеграции через RabbitMQ:

1. Подключение к очереди RabbitMQ с использованием credentials из ECOS Endpoint.
2. Логирование входящего сообщения.
3. Роутинг сообщения по значению поля ``operation`` в JSON-теле:

   - ``CREATE`` → публикация события ``test-data-create``,
   - ``UPDATE`` → публикация события ``test-data-update``,
   - прочие значения → выброс исключения (сообщение уходит в Dead Letter Queue).

.. note::

   Для работы примера необходимо создать ECOS Endpoint с именем ``my-rabbitmq-endpoint``, содержащий ``url``, ``credentials/username`` и ``credentials/password``.

.. code-block:: yaml

   - beans:
       # Бин подключения к RabbitMQ на основе данных из ECOS Endpoint
       - name: myRabbitConnectionFactory
         type: org.springframework.amqp.rabbit.connection.CachingConnectionFactory
         properties:
           uri: '{{ecos-endpoint:my-rabbitmq-endpoint/url}}'
           username: '{{ecos-endpoint:my-rabbitmq-endpoint/credentials/username}}'
           password: '{{ecos-endpoint:my-rabbitmq-endpoint/credentials/password}}'

   - route:
       from:
         uri: "spring-rabbitmq:income-test-data"
         parameters:
           connectionFactory: '#bean:myRabbitConnectionFactory'
           queues: test-data-queue
           autoDeclare: true
           # Dead Letter Queue — принимает сообщения, которые не удалось обработать
           deadLetterExchange: income-test-data
           deadLetterQueue: test-data-queue-dlq
           deadLetterRoutingKey: deadLetterTestData
           # Задержка перед повторной попыткой обработки (мс)
           retryDelay: 5000
           arg.queue.durable: true
           arg.queue.autoDelete: false
         steps:
           # Логирование входящего сообщения
           - to:
               uri: "log:income?level=INFO&showAll=true"
           # Роутинг по полю operation в JSON
           - choice:
               when:
                 - jsonpath:
                     expression: "$.[?(@.operation == 'CREATE')]"
                   steps:
                     - to: "ecos-event:test-data-create"
                 - jsonpath:
                     expression: "$.[?(@.operation == 'UPDATE')]"
                   steps:
                     - to: "ecos-event:test-data-update"
               otherwise:
                 steps:
                   # Неизвестное значение operation — исключение отправит сообщение в DLQ
                   - throwException:
                       exceptionType: "java.lang.IllegalArgumentException"
                       message: "Unsupported operation. Only CREATE and UPDATE are supported."
