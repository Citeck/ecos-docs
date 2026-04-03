.. _ecos-notifications-settings:

Настройка подключения микросервиса ecos-notifications
=======================================================

Для отправки писем пользователям необходимо настроить подключение микросервиса ecos-notifications к SMTP-серверу.

Эти параметры задаются в конфигурации сервиса (**spring properties**) и обычно настраиваются не через интерфейс, а при развертывании приложения: например, через application.yml, переменные окружения, Docker Compose, Helm chart или другой способ конфигурации.

Ниже пример настройки для mail.ru.

Через **application.yml**:

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

Или то же самое через **переменные окружения**:

.. code-block:: text

 SPRING_MAIL_HOST=smtp.mail.ru
 SPRING_MAIL_PORT=587
 SPRING_MAIL_USERNAME=user@mail.ru
 SPRING_MAIL_PASSWORD=12345
 SPRING_MAIL_PROPERTIES_MAIL_SMTP_AUTH=true
 SPRING_MAIL_PROPERTIES_MAIL_SMTP_STARTTLS_ENABLE=true
 ECOS_NOTIFICATIONS_EMAIL_FROM_FIXED=user@mail.ru