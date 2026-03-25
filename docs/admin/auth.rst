Аутентификация и безопасность
==============================

Раздел описывает механизмы аутентификации в Citeck и интеграцию с Keycloak как стандартным провайдером идентификации (IdP).

**Аутентификация** — общая архитектура аутентификации в платформе: протокол OpenID Connect, роли Access Token / Refresh Token, схемы взаимодействия между компонентами.

**Интеграция Citeck с Keycloak** — настройка двусторонней синхронизации пользователей между Citeck и Keycloak через RESTful API (ecos-model начиная с версии 2.20.0).

**Настройки аутентификации для Records API** — получение Client ID и Client Secret в Keycloak, настройка OAuth 2.0 и отправка запросов к Records API из внешних систем (на примере Postman).

**Citeck Keycloak Extension** *(Enterprise)* — расширение Keycloak со стороны Citeck: генерация событий платформы при пользовательских событиях Keycloak, синхронизация статуса пользователей.

.. toctree::
    :maxdepth: 2

    auth/authentication
    auth/keycloak_ecos_integration
    auth/keycloak_postman
    auth/keycloak_extension