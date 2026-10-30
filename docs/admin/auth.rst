Аутентификация и безопасность
==============================

Раздел описывает механизмы аутентификации в Citeck и интеграцию с Keycloak как стандартным провайдером идентификации (IdP).

.. grid:: 1
   :gutter: 2

   .. grid-item-card:: Аутентификация
      :link: authentication
      :link-type: ref

      Общая архитектура аутентификации в платформе: протокол OpenID Connect, роли Access Token / Refresh Token, схемы взаимодействия между компонентами.

   .. grid-item-card:: Интеграция Citeck с Keycloak
      :link: keycloak_ecos_integration
      :link-type: ref

      Настройка двусторонней синхронизации пользователей между Citeck и Keycloak через RESTful API (ecos-model начиная с версии 2.20.0).

   .. grid-item-card:: Настройки аутентификации для Records API
      :link: keycloak_postman
      :link-type: ref

      Получение Client ID и Client Secret в Keycloak, настройка OAuth 2.0 и отправка запросов к Records API из внешних систем (на примере Postman).

   .. grid-item-card:: Citeck Keycloak Extension (Enterprise)
      :link: keycloak_extension
      :link-type: ref

      Расширение Keycloak со стороны Citeck: генерация событий платформы при пользовательских событиях Keycloak, синхронизация статуса пользователей.

.. toctree::
    :maxdepth: 2
    :hidden:

    auth/authentication
    auth/keycloak_ecos_integration
    auth/keycloak_postman
    auth/keycloak_extension