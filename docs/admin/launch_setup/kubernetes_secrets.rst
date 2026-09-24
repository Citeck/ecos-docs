.. _kubernetes-secrets:

Управление секретами через Kubernetes Secrets
==============================================

Параметр ``existingSecret`` позволяет хранить чувствительные данные (пароли, токены, credentials) в Kubernetes Secrets вместо ``values.yaml``.

При использовании ``existingSecret`` Helm выполняет ``lookup`` секрета во время деплоя и подставляет значения напрямую.

.. contents::

Принцип работы
---------------------------

* Если ``existingSecret`` **задан** — пароли берутся из указанного Kubernetes Secret по соответствующему ключу.
* Если ``existingSecret`` **не задан** — используется значение из ``values.yaml`` (обратная совместимость сохранена).
* Если ``existingSecret`` задан, но секрет **не найден** в кластере — деплой завершится ошибкой.

.. note::

    Секрет должен существовать до деплоя — Helm выполняет ``lookup`` во время рендеринга шаблонов.

Компоненты и ключи секретов
----------------------------

RabbitmqApp
~~~~~~~~~~~

.. code-block:: yaml

    RabbitmqApp:
      existingSecret: <secret-name>
      environments:
        username: "rabbitmqadmin"  # берётся из values.yaml, не из секрета
        password: ""               # используется только если existingSecret не задан

.. list-table::
   :header-rows: 1
   :widths: 30 40 30
   :class: tight-table

   * - Ключ в секрете
     - Поле в values.yaml
     - Дефолт (если оба пусты)
   * - ``password``
     - ``RabbitmqApp.environments.password``
     - ``RabbitmqStrongPassword``

.. note::

    ``username`` всегда берётся из ``RabbitmqApp.environments.username``, секрет его не переопределяет.

Пример секрета:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-rabbitmq-secret
    type: Opaque
    stringData:
      password: "StrongRabbitPassword"

EcosRegistryApp
~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosRegistryApp:
      existingSecret: <secret-name>
      environments:
        adminPassword: ""  # используется только если existingSecret не задан

.. list-table::
   :header-rows: 1
   :widths: 30 40 30
   :class: tight-table

   * - Ключ в секрете
     - Поле в values.yaml
     - Дефолт (если оба пусты)
   * - ``admin-password``
     - ``EcosRegistryApp.environments.adminPassword``
     - ``EcosRegistryStrongPassword``

Пример секрета:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-registry-secret
    type: Opaque
    stringData:
      admin-password: "StrongRegistryPassword"

EcosIdentityApp (Keycloak)
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosIdentityApp:
      existingSecret: <secret-name>
      environments:
        password: ""  # используется только если existingSecret не задан

.. list-table::
   :header-rows: 1
   :widths: 30 40 30
   :class: tight-table

   * - Ключ в секрете
     - Поле в values.yaml
     - Дефолт (если оба пусты)
   * - ``password``
     - ``EcosIdentityApp.environments.password``
     - ``VeryStrongPassword``

Пример секрета:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-identity-secret
    type: Opaque
    stringData:
      password: "StrongKeycloakPassword"

EcosProxyApp
~~~~~~~~~~~~

.. code-block:: yaml

    EcosProxyApp:
      existingSecret: <secret-name>
      eisIntegration:
        clientSecret: ""  # используется только если existingSecret не задан

.. list-table::
   :header-rows: 1
   :widths: 30 40 30
   :class: tight-table

   * - Ключ в секрете
     - Поле в values.yaml
     - Дефолт (если оба пусты)
   * - ``client-secret``
     - ``EcosProxyApp.eisIntegration.clientSecret``
     - ``change-me-please``

Пример секрета:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-proxy-secret
    type: Opaque
    stringData:
      client-secret: "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"

EcosGatewayApp
~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosGatewayApp:
      existingSecret: <secret-name>

.. list-table::
   :header-rows: 1
   :widths: 30 40 30
   :class: tight-table

   * - Ключ в секрете
     - Поле в values.yaml
     - Дефолт (если оба пусты)
   * - ``truststore-password``
     - — (нет прямого поля в values)
     - — (ключ optional)

.. note::

    Ключ ``truststore-password`` помечен как ``optional: true``. Если ключ отсутствует в секрете — env var ``GATEWAY_TRUSTSTORE_PASSWORD`` просто не будет установлен.

Пример секрета:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-gateway-secret
    type: Opaque
    stringData:
      truststore-password: "strongpassword"

MongoDBApp
~~~~~~~~~~

.. code-block:: yaml

    MongoDBApp:
      existingSecret: <secret-name>
      environments:
        username: ""   # берётся из values.yaml, не из секрета
        password: ""   # используется только если existingSecret не задан

.. list-table::
   :header-rows: 1
   :widths: 30 40 30
   :class: tight-table

   * - Ключ в секрете
     - Поле в values.yaml
     - Дефолт (если оба пусты)
   * - ``password``
     - ``MongoDBApp.environments.password``
     - ``root_user_password``

.. note::

    ``username`` всегда берётся из ``MongoDBApp.environments.username``, секрет его не переопределяет.

Пример секрета:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-mongodb-secret
    type: Opaque
    stringData:
      password: "StrongMongoPassword"

EcosPostgresqlApp
~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosPostgresqlApp:
      existingSecret: <secret-name>
      environments:
        password: ""    # пароль superuser — только если existingSecret не задан
        databases:
          ecosApp:
            username: alfresco
            password: ""  # только если existingSecret не задан
          ecosFlowable:
            username: alfresco
            password: ""  # только если existingSecret не задан

.. list-table::
   :header-rows: 1
   :widths: 30 40 30
   :class: tight-table

   * - Ключ в секрете
     - Поле в values.yaml
     - Дефолт (если оба пусты)
   * - ``password``
     - ``EcosPostgresqlApp.environments.password``
     - ``postgresstorngpassword``
   * - ``alfresco-db-password``
     - ``EcosPostgresqlApp.environments.databases.ecosApp.password``
     - ``alfr3sc0``
   * - ``flowable-db-password``
     - ``EcosPostgresqlApp.environments.databases.ecosFlowable.password``
     - ``alfr3sc0``

Пример секрета:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-postgresql-secret
    type: Opaque
    stringData:
      password: "StrongPostgresPassword"
      alfresco-db-password: "AlfrescoDbPassword"
      flowable-db-password: "FlowableDbPassword"

EcosMicroservicesPostgresqlApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosMicroservicesPostgresqlApp:
      existingSecret: <secret-name>
      environments:
        username: ""     # postgres superuser username — не берётся из секрета
        password: ""     # postgres superuser password — только если existingSecret не задан
        databases:
          ecosAppsApp:
            database: ecos_apps
            username: apps          # определяет ключ секрета: apps-password
            password: appspassword  # только если existingSecret не задан
          ecosGatewayApp:
            username: gateway       # ключ секрета: gateway-password
            password: gatewaypassword
          # ... и т.д. для каждой БД

Ключи паролей для каждой базы данных формируются по шаблону **``{username}-password``**:

.. list-table::
   :header-rows: 1
   :widths: 30 35 35
   :class: tight-table

   * - Ключ в секрете
     - ``username`` в values.yaml
     - Поле в values.yaml
   * - ``postgres-password``
     - — (superuser)
     - ``environments.password``
   * - ``apps-password``
     - ``databases.ecosAppsApp.username: apps``
     - ``databases.ecosAppsApp.password``
   * - ``gateway-password``
     - ``databases.ecosGatewayApp.username: gateway``
     - ``databases.ecosGatewayApp.password``
   * - ``uiserv-password``
     - ``databases.ecosUiservApp.username: uiserv``
     - ``databases.ecosUiservApp.password``
   * - ``notifications-password``
     - ``databases.ecosNotificationsApp.username: notifications``
     - ``databases.ecosNotificationsApp.password``
   * - ``history-password``
     - ``databases.ecosHistoryApp.username: history``
     - ``databases.ecosHistoryApp.password``
   * - ``integrations-password``
     - ``databases.ecosIntegrationsApp.username: integrations``
     - ``databases.ecosIntegrationsApp.password``
   * - ``model-password``
     - ``databases.ecosModelApp.username: model``
     - ``databases.ecosModelApp.password``
   * - ``reports-password``
     - ``databases.ecosJiraReportsApp.username: reports``
     - ``databases.ecosJiraReportsApp.password``
   * - ``casemodel-password``
     - ``databases.ecosCasemodelApp.username: casemodel``
     - ``databases.ecosCasemodelApp.password``
   * - ``eis-password``
     - ``databases.ecosIdentityApp.username: eis``
     - ``databases.ecosIdentityApp.password``
   * - ``process-password``
     - ``databases.ecosProcessApp.username: process``
     - ``databases.ecosProcessApp.password``
   * - ``camunda-password``
     - ``databases.ecosCamundaApp.username: camunda``
     - ``databases.ecosCamundaApp.password``
   * - ``edi-password``
     - ``databases.ecosEdiApp.username: edi``
     - ``databases.ecosEdiApp.password``

.. important::

    Если ``username`` изменён в ``values.yaml``, ключ в секрете должен быть обновлён соответственно. Например, если ``username: myapps`` — ключ должен быть ``myapps-password``.

Пример секрета:

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-microservices-postgresql-secret
    type: Opaque
    stringData:
      postgres-password: "StrongPostgresPassword"
      apps-password: "AppsDbPassword"
      gateway-password: "GatewayDbPassword"
      uiserv-password: "UiservDbPassword"
      notifications-password: "NotificationsDbPassword"
      history-password: "HistoryDbPassword"
      integrations-password: "IntegrationsDbPassword"
      model-password: "ModelDbPassword"
      reports-password: "ReportsDbPassword"
      casemodel-password: "CasemodelDbPassword"
      eis-password: "EisDbPassword"
      process-password: "ProcessDbPassword"
      camunda-password: "CamundaDbPassword"
      edi-password: "EdiDbPassword"

EcosApp
~~~~~~~

.. code-block:: yaml

    EcosApp:
      existingSecret: <secret-name>
      environments:
        alfresco:
          ldap:
            enabled: true
            injectSyncCredentials: false        # false — пароль не берётся из секрета
            injectTruststorePassphrase: false   # false — пароль не берётся из секрета
        mail:
          password: ""                          # используется только если existingSecret не задан
          injectPasswordFromSecret: false       # false — пароль не берётся из секрета
          injectFlowablePasswordFromSecret: false
      dataSource:
        alfresco:
          password: ""   # используется если EcosPostgresqlApp.enabled: false
        flowable:
          password: ""   # используется если EcosPostgresqlApp.enabled: false

.. list-table::
   :header-rows: 1
   :widths: 30 35 20 15
   :class: tight-table

   * - Ключ в секрете
     - Поле в values.yaml
     - Управляющий флаг
     - Дефолт
   * - ``alfresco-db-password``
     - ``EcosPostgresqlApp.environments.databases.ecosApp.password`` или ``dataSource.alfresco.password``
     - — (всегда при existingSecret)
     - ``alfr3sc0``
   * - ``flowable-db-password``
     - ``EcosPostgresqlApp.environments.databases.ecosFlowable.password`` или ``dataSource.flowable.password``
     - — (всегда при existingSecret)
     - ``alfr3sc0``
   * - ``ldap-sync-credentials``
     - — (нет прямого поля)
     - ``ldap.injectSyncCredentials: true``
     - —
   * - ``ldap-truststore-passphrase``
     - — (нет прямого поля)
     - ``ldap.injectTruststorePassphrase: true``
     - —
   * - ``mail-password``
     - ``environments.mail.password``
     - ``mail.injectPasswordFromSecret: true``
     - —
   * - ``flowable-mail-password``
     - — (нет прямого поля)
     - ``mail.injectFlowablePasswordFromSecret: true``
     - —

.. note::

    При ``injectPasswordFromSecret: true`` пароль подставляется в свойство ``mail.password`` (Alfresco mail). При ``injectFlowablePasswordFromSecret: true`` — в ``flowable.mail.server.password`` (Flowable mail). Оба можно использовать одновременно с разными паролями.

Пример секрета (полный):

.. code-block:: yaml

    apiVersion: v1
    kind: Secret
    metadata:
      name: my-ecos-app-secret
    type: Opaque
    stringData:
      alfresco-db-password: "AlfrescoDbPassword"
      flowable-db-password: "FlowableDbPassword"
      ldap-sync-credentials: "LdapBindPassword"
      ldap-truststore-passphrase: "strongpassword"
      mail-password: "AlfrescoMailPassword"
      flowable-mail-password: "FlowableMailPassword"

Полный пример конфигурации
--------------------------------------------------

.. code-block:: yaml

    RabbitmqApp:
      existingSecret: my-rabbitmq-secret

    EcosRegistryApp:
      existingSecret: my-registry-secret

    EcosIdentityApp:
      existingSecret: my-identity-secret

    EcosProxyApp:
      existingSecret: my-proxy-secret

    EcosGatewayApp:
      existingSecret: my-gateway-secret

    MongoDBApp:
      existingSecret: my-mongodb-secret

    EcosPostgresqlApp:
      existingSecret: my-postgresql-secret

    EcosMicroservicesPostgresqlApp:
      existingSecret: my-microservices-postgresql-secret

    EcosApp:
      existingSecret: my-ecos-app-secret
      environments:
        alfresco:
          ldap:
            enabled: true
            injectSyncCredentials: true
            injectTruststorePassphrase: false
        mail:
          injectPasswordFromSecret: true
          injectFlowablePasswordFromSecret: true
