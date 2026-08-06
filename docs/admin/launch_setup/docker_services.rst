.. _docker_services:

Сервисы Docker
===============

Раздел описывает Docker-образы, входящие в состав платформы Citeck: назначение каждого сервиса, шаблон его описания в docker-compose, используемые переменные окружения и типовой вид лога успешного запуска.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: onlyoffice-ds-app
      :link: onlyoffice_ds_app
      :link-type: ref

      Образ, включающий набор инструментов для развертывания OnlyOffice Document Server.

   .. grid-item-card:: ecos-gateway-app
      :link: ecos_gateway_app
      :link-type: ref

      Образ одного из центральных компонентов микросервисной архитектуры — API-шлюз взаимодействия с остальными микросервисами.

   .. grid-item-card:: ecos-notifications-app
      :link: ecos_notifications_app
      :link-type: ref

      Образ микросервиса рассылки нотификаций.

   .. grid-item-card:: ecos-mongo-app
      :link: ecos_mongo_app
      :link-type: ref

      Образ для развертывания контейнера с MongoDB с преконфигурированными настройками датасорсов для микросервисов.

   .. grid-item-card:: mailhog-app
      :link: mailhog_app
      :link-type: ref

      Образ инструмента для e-mail тестирования.

   .. grid-item-card:: ecos-postgresql-app
      :link: ecos_postgresql_app
      :link-type: ref

      Образ на базе PostgreSQL 9.4.x со скриптом инициализации баз данных и пользователей.

   .. grid-item-card:: ecos-model-app
      :link: ecos_model_app
      :link-type: ref

      Образ микросервиса для хранения и работы с сущностями модели данных: тип, раздел, ассоциация, действие.

   .. grid-item-card:: ecos-integrations-app
      :link: ecos_integrations_app
      :link-type: ref

      Микросервис, предоставляющий эндпойнт ecos-records для запросов к внешним системам.

   .. grid-item-card:: ecos-proxy-app
      :link: ecos_proxy_app
      :link-type: ref

      Образ проксирующего сервера со сборкой проекта ecos-ui.

   .. grid-item-card:: ecos-uiserv-app
      :link: ecos_uiserv_app
      :link-type: ref

      Образ микросервиса, предоставляющего элементы UI и хранящего их настройки: меню, журналы, конфиги, формы, дашборды.

   .. grid-item-card:: ecos-process-app
      :link: ecos_process_app
      :link-type: ref

      Образ микросервиса для управления бизнес-процессами.

   .. grid-item-card:: ecos-microservices-postgresql-app
      :link: ecos_microservices_postgresql_app
      :link-type: ref

      Образ на базе PostgreSQL 12.x со скриптом инициализации баз данных и пользователей для микросервисов.

   .. grid-item-card:: ecos-history-app
      :link: ecos_history_app
      :link-type: ref

      Образ микросервиса для хранения истории, статистики по задачам и фасада атрибутов.

   .. grid-item-card:: rabbitmq-app
      :link: rabbitmq_app
      :link-type: ref

      Образ брокера сообщений RabbitMQ.

   .. grid-item-card:: ecos-apps-app
      :link: ecos_apps_app
      :link-type: ref

      Образ микросервиса, управляющего деплоем приложений и модулей ECOS.

   .. grid-item-card:: eis (Keycloak)
      :link: eis_keycloak
      :link-type: ref

      Сервис аутентификации и авторизации (IAM) на основе Keycloak: SSO, управление пользователями, ролями и группами.

.. toctree::
    :maxdepth: 3
    :hidden:

    docker_services/onlyoffice-ds-app
    docker_services/ecos-gateway-app
    docker_services/ecos-notifications-app
    docker_services/ecos-mongo-app
    docker_services/mailhog-app
    docker_services/ecos-postgresql-app
    docker_services/ecos-model-app
    docker_services/ecos-integrations-app
    docker_services/ecos-proxy-app
    docker_services/ecos-uiserv-app
    docker_services/ecos-process-app
    docker_services/ecos-microservices-postgresql-app
    docker_services/ecos-history-app
    docker_services/rabbitmq-app
    docker_services/ecos-apps-app
    docker_services/eis_Keycloak
