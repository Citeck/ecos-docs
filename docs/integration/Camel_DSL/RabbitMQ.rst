Получение сообщений из RabbitMQ и отправка события Citeck
=========================================================

.. _rabbitmq_camel:

Пример чтения из rabbitmq и отправка события Citeck:

1. Создать новый **секрет (Модель -  Секреты)** для подключения к RMQ.
2. Создать новый **endpoint (Модель - Конечные точки)** с id 'rabbitmq-endpoint'  (можно любой id, но в camel конфиге мы на него ссылаемся) для подключения к RMQ и устанавить секрет из п.1 в него.
3. Зайти в **журнал Camel DSL (Интеграция - Camel DSL)** и создать новый контекст со следующим конфигом: 

.. code-block:: yaml
  
  - beans:
      - name: rabbitConnectionFactory
        type: org.springframework.amqp.rabbit.connection.CachingConnectionFactory
        properties:
          uri: '{{ecos-endpoint:rabbitmq-endpoint/url}}'
          username: '{{ecos-endpoint:rabbitmq-endpoint/credentials/username}}'
          password: '{{ecos-endpoint:rabbitmq-endpoint/credentials/password}}'
  - route:
      from:
        uri: spring-rabbitmq:default # default здесь -это дефолтный exchange в RMQ. Обычно он обозначается пустой строкой, но в camel endpoint'е вместо этого пишется "default"
        parameters:
          connectionFactory: '#bean:rabbitConnectionFactory'
          queues: test-queue
        steps:
          - removeHeaders: # если в дальнейшем предполагается переотправка сообщения в RMQ, то лучше удалить заголовки, которые относятся к RMQ. Здесь этот этап просто для примера.
              pattern: "CamelRabbitmq*" #"CamelRabbitmqRoutingKey"
          - to: log:rmq-test # вывод в лог. Можно убрать
          - to: ecos-event:test-event-type # отправка события с типом "test-event-type". В теле отправляется DataValue.of(exchange.message.body)
