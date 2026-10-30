.. _ecos-notifications-settings:

Настройка подключения микросервиса ecos-notifications
=======================================================

.. contents::

Для отправки писем пользователям необходимо настроить подключение микросервиса ecos-notifications к SMTP-серверу.

Эти параметры задаются в конфигурации сервиса (**spring properties**) и обычно настраиваются не через интерфейс, а при развертывании приложения: например, через application.yml, переменные окружения, Docker Compose, Helm chart или другой способ конфигурации.

Ниже пример настройки для mail.ru.

.. tab-set::

   .. tab-item:: application.yml

      .. code-block:: yaml

       spring:
         mail:
           host: smtp.mail.ru
           port: 587
           username: user@mail.ru
           password: 12345
           properties:
             mail:
               smtp:
                 auth: true
                 starttls:
                   enable: true

       ecos-notifications:
         email:
           from:
             fixed: user@mail.ru

   .. tab-item:: Переменные окружения

      .. code-block:: text

       SPRING_MAIL_HOST=smtp.mail.ru
       SPRING_MAIL_PORT=587
       SPRING_MAIL_USERNAME=user@mail.ru
       SPRING_MAIL_PASSWORD=12345
       SPRING_MAIL_PROPERTIES_MAIL_SMTP_AUTH=true
       SPRING_MAIL_PROPERTIES_MAIL_SMTP_STARTTLS_ENABLE=true
       ECOS_NOTIFICATIONS_EMAIL_FROM_FIXED=user@mail.ru

Параметры, влияющие на повторные отправки
-------------------------------------------

Помимо параметров подключения, поведение микросервиса при сбоях отправки задаётся блоком
``ecos-notifications.retry`` — см. :ref:`повторные попытки отправки <notifications-label>`.

Значения по умолчанию рассчитаны на типовой сценарий, менять их обычно не требуется.

.. warning::

   Следующие SMTP-параметры важны для корректной работы повторов — переопределять их
   значения по умолчанию не рекомендуется:

.. code-block:: yaml

 spring:
   mail:
     properties:
       mail:
         smtp:
           connectiontimeout: 10000
           timeout: 10000
           writetimeout: 10000
           sendpartial: true

.. list-table::
   :header-rows: 1
   :widths: 25 75
   :class: tight-table

   * - Параметр
     - Описание
   * - ``connectiontimeout``, ``timeout``, ``writetimeout``
     - Таймауты обязательно должны быть конечными: иначе зависшее соединение заблокирует
       уведомление на всё время ожидания ответа сервера.
   * - ``sendpartial``
     - Доставлять письмо принявшим его получателям вместо отмены отправки целиком, если
       часть адресов отклонена сервером.