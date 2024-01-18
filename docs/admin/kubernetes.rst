Kubernetes
==========

.. contents::

Менеджмент ресурсов подов и контейнеров
----------------------------------------

Ниже описаны минимальные требования к ресурсам mem/cpu для стабильной работы микросервисов в сочетании с xmx/xms параметрами java. (TODO: привязка к количеству пользователей)


Ecos Registry
~~~~~~~~~~~~~

.. code-block:: yaml

    EcosRegistryApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 300m
                memory: 1Gi

Ecos Model
~~~~~~~~~~

.. code-block:: yaml

    EcosModelApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Gateway
~~~~~~~~~~~~

.. code-block:: yaml

    EcosGatewayApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Apps
~~~~~~~~~

.. code-block:: yaml

    EcosAppsApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Process
~~~~~~~~~~~~

.. code-block:: yaml

    EcosProcessApp:
        environments:
            javaOpts: "-Xmx2G -Xms512m"
        resources: |
            limits:
                cpu: 1
                memory: 3Gi
            requests:
                cpu: 100m
                memory: 3Gi

Ecos Uiserv
~~~~~~~~~~~

.. code-block:: yaml

    EcosUiservApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos History
~~~~~~~~~~~~

.. code-block:: yaml

    EcosHistoryApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Integrations
~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosIntegrationsApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Notifications
~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosNotificationsApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Transformations
~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosTransformationsApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Ecom
~~~~~~~~~

.. code-block:: yaml

    EcosEcomApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Service Desk
~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosServiceDeskApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Edi
~~~~~~~~

.. code-block:: yaml

    EcosEdiApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Content
~~~~~~~~~~~~

.. code-block:: yaml

    EcosContentApp:
        environments:
            javaOpts: "-Xmx300m -Xms300m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Proxy
~~~~~~~~~~

.. code-block:: yaml

    EcosProxyApp:
        resources: |
            limits:
                cpu: 1
                memory: 512Mi
            requests:
                cpu: 100m
                memory: 256Mi

Microservices Posgtresql
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosMicroservicesPostgresqlApp:
        resources: |
            limits:
                cpu: 1
                memory: 800Mi
            requests:
                cpu: 300m
                memory: 800Mi

Mongo DB
~~~~~~~~

.. code-block:: yaml

    MongoDBApp:
        resources: |
            limits:
                cpu: 1
                memory: 512Mi
            requests:
                cpu: 300m
                memory: 512Mi

Zookeeper
~~~~~~~~~

.. code-block:: yaml

    ZookeeperApp:
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 1
                memory: 1Gi

RabbitMQ
~~~~~~~~

.. code-block:: yaml

    RabbitmqApp:
        resources: |
            limits:
                cpu: 500m
                memory: 1Gi
            requests:
                cpu: 100m
                memory: 1Gi

Ecos Indentity
~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosIdentityApp:
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 300m
                memory: 1Gi

Onlyoffice
~~~~~~~~~~

.. code-block:: yaml

    OnlyofficeApp:
        resources: |
            limits:
                cpu: 2
                memory: 2Gi
            requests:
                cpu: 100m
                memory: 2Gi

