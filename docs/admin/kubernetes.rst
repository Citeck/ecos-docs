Kubernetes
==========

.. contents::

Менеджмент ресурсов подов и контейнеров
----------------------------------------

Ниже описаны минимальные требования к ресурсам MEM/CPU для стабильной работы микросервисов в сочетании с XMX/XMS параметрами java. 
На данной конфигурации было произведено нагрузочное тестирование в **1000** одновременно работающих пользователей, длительностью в **1** час.

Состав сценария и распределение нагрузки:

    - логин в систему и просмотр главной страницы с загрузкой меню, дашборда, информации о пользователе (20%);
    - просмотр журнала контрактов (30%);
    - переход на страницу просмотра контракта с загрузкой всех виджетов: информация о контракте, действия, задачи, комментарии, связи, история версий и т.д. (30%);
    - просмотр журнала активных задач  (30%);
    - создание документов (20%);
    - старт процессов по документам (10%);
    - выполнение задач по процессу (50%).

В ходе нагрузки было сгенерировано **2 043 398 запросов**, из них 1 запроса (0.00 %) завершилось с ошибками или превысило лимит времени выполнения. |br|

    Среднее время отклика - **6.88 миллисекунд**. |br|
    Медиана - 6 миллисекунд. |br|
    **90%** всех запросов обрабатывались менее чем за **16 миллисекунд**. |br|
    **95%** всех запросов обрабатывались менее чем за **25 миллисекунд**. |br|
    **99%** всех запросов обрабатывались менее чем за **47 миллисекунд**. |br|


Ecos Registry
~~~~~~~~~~~~~

.. code-block:: yaml

    EcosRegistryApp:
        environments:
            javaOpts: "-Xmx256m -Xms256m"
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
            javaOpts: "-Xmx256m -Xms256m"
        resources: |
            limits:
                cpu: 2
                memory: 1Gi
            requests:
                cpu: 2
                memory: 1Gi

Ecos Gateway
~~~~~~~~~~~~

.. code-block:: yaml

    EcosGatewayApp:
        environments:
            javaOpts: "-Xmx256m -Xms256m"
        resources: |
            limits:
                cpu: 2
                memory: 1Gi
            requests:
                cpu: 2
                memory: 1Gi

Ecos Apps
~~~~~~~~~

.. code-block:: yaml

    EcosAppsApp:
        environments:
            javaOpts: "-Xmx256m -Xms256m"
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
                memory: 4Gi
            requests:
                cpu: 1
                memory: 4Gi

Ecos Uiserv
~~~~~~~~~~~

.. code-block:: yaml

    EcosUiservApp:
        environments:
            javaOpts: "-Xmx256m -Xms256m"
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:
                cpu: 1
                memory: 1Gi

Ecos History
~~~~~~~~~~~~

.. code-block:: yaml

    EcosHistoryApp:
        environments:
            javaOpts: "-Xmx256m -Xms256m"
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
            javaOpts: "-Xmx256m -Xms256m"
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
            javaOpts: "-Xmx256m -Xms256m"
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
            javaOpts: "-Xmx256m -Xms256m"
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
            javaOpts: "-Xmx256m -Xms256m"
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
            javaOpts: "-Xmx256m -Xms256m"
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
            javaOpts: "-Xmx256m -Xms256m"
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
            javaOpts: "-Xmx256m -Xms256m"
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
                cpu: 300m
                memory: 256Mi

Microservices Posgtresql
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: yaml

    EcosMicroservicesPostgresqlApp:
        resources: |
            limits:
                cpu: 2
                memory: 2Gi
            requests:
                cpu: 2
                memory: 2Gi

Mongo DB
~~~~~~~~

.. code-block:: yaml

    MongoDBApp:
        resources: |
            limits:
                cpu: 500m
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
                cpu: 500m
                memory: 1Gi

RabbitMQ
~~~~~~~~

.. code-block:: yaml

    RabbitmqApp:
        resources: |
            limits:
                cpu: 1
                memory: 1Gi
            requests:m
                cpu: 500
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

.. |br| raw:: html

     <br>