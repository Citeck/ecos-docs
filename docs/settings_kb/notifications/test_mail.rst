.. _test_mail:

Отправка тестового сообщения при запуске микросервиса
======================================================

Микросервис **ecos-notifications** может отправлять тестовое сообщение при старте — это задаётся конфигурацией в **application property**:

.. code-block:: yaml

    ecos-notifications:
        startup-notification:
            enabled: true
            body: Microservice ecos-notifications successfully started and ready for operation. This is a test message – no reply is needed.
            title: Microservice ecos-notifications successfully started and ready for operation
            recipient: test@test.ru

.. list-table::
   :header-rows: 1
   :class: tight-table

   * - Параметр
     - Описание
   * - ``enabled``
     - ``true``/``false`` — включена или выключена отправка сообщения
   * - ``body``
     - Тело тестового сообщения
   * - ``title``
     - Тема тестового сообщения
   * - ``recipient``
     - Получатель тестового сообщения

В поставляемом ``application.yml`` отправка включена. Обработчик вызывается после готовности приложения (``ApplicationReadyEvent``), кроме профиля ``test``.

Тестовое письмо отправляется напрямую встроенным email-отправителем: выбор command-отправителей, обычная регистрация уведомления и очередь повторов не используются. Поэтому письмо не обязано появляться в журнале уведомлений. Его успешная доставка проверяет почтовое соединение, но не всю цепочку шаблонов, маршрутизации и повторов.
