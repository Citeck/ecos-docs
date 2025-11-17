Отправка тестового сообщения при запуске микросервиса
========================================================

В **application property** добавлена конфигурация для отправки тестового сообщения при запуске микросервиса **ecos-notification**:

.. code-block:: yaml

 ecos-notifications:
     startup-notification:
         enabled: true
         body: Microservice ecos-notifications successfully started and ready for operation. This is a test message – no reply is needed.
         title: Microservice ecos-notifications successfully started and ready for operation
         recipient: test@test.ru

- **enabled** - true/false включена или выключена отправка сообщения;
- **body** - тело тестового сообщения
- **title** - тема тестового сообщения
- **recipient** - получатель тестового сообщения