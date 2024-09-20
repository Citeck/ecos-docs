Получение сообщений из RabbitMQ и отправка события ECOS
=========================================================

Пример чтения из rabbitmq и отправка события ECOS:

1. Создаем новый **секрет (Интеграция - Credentials)** для подключения к RMQ
2. Создаем новый **endpoint (Интеграция - Источники данных)** с id 'rabbitmq-endpoint'  (можно любой id, но в camel конфиге мы на него ссылаемся) для подключения к RMQ и устанавливаем секрет из п.1 в него
3. Заходим в **журнал Camel DSL (Интеграция - Camel DSL)** и создаем новый контекст со следующим конфигом: 

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
