Чтение из RabbitMQ -> роутинг по jsonPath -> переотправка в ECOS Event + Dead Letter Queue
=============================================================================================

.. code-block:: yaml

   - beans:
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
           deadLetterExchange: income-test-data
           deadLetterQueue: test-data-queue-dlq
           deadLetterRoutingKey: deadLetterTestData
           retryDelay: 5000
           arg.queue.durable: true
           arg.queue.autoDelete: false
         steps:
           - to:
               uri: "log:income?level=INFO&showAll=true"
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
                   - throwException:
                       exceptionType: "java.lang.IllegalArgumentException"
                       message: "Unsupported operation. Only CREATE and UPDATE are supported."
