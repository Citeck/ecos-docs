.. _kubernetes:

Kubernetes
==========

.. note::

    Доступно только в Enterprise версии.

Раздел описывает развёртывание платформы Citeck в среде Kubernetes: управление ресурсами подов и контейнеров, настройку Helm chart, остановку и запуск системы, а также ключ шифрования секретов.

.. contents::

.. _k8s-resource-management:

Менеджмент ресурсов подов и контейнеров
----------------------------------------

Ниже описаны минимальные требования к ресурсам MEM/CPU для стабильной работы микросервисов в сочетании с XMX/XMS параметрами java. 
На данной конфигурации было произведено нагрузочное тестирование в **1000** одновременно работающих пользователей, длительностью в **1** час.

.. seealso::

    Расчёт worker-нод кластера на основе этих значений — :ref:`Сайзинг в Kubernetes <sizing_k8s>`.

Состав сценария и распределение нагрузки:

    - логин в систему и просмотр главной страницы с загрузкой меню, дашборда, информации о пользователе (20%);
    - просмотр журнала контрактов (30%);
    - переход на страницу просмотра контракта с загрузкой всех виджетов: информация о контракте, действия, задачи, комментарии, связи, история версий и т.д. (30%);
    - просмотр журнала активных задач  (30%);
    - создание документов (20%);
    - старт процессов по документам (10%);
    - выполнение задач по процессу (50%).

В ходе нагрузки было сгенерировано **2 043 398 запросов**, из них 1 запроса (0.00 %) завершилось с ошибками или превысило лимит времени выполнения.

.. list-table::
   :header-rows: 1
   :widths: 50 50
   :class: tight-table

   * - Метрика
     - Значение
   * - Среднее время отклика
     - 6.88 мс
   * - Медиана
     - 6 мс
   * - 90% запросов
     - < 16 мс
   * - 95% запросов
     - < 25 мс
   * - 99% запросов
     - < 47 мс


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
            javaOpts: "-Xmx2G -Xms2G"
        resources: |
            limits:
                cpu: 1
                memory: 3548Mi
            requests:
                cpu: 1
                memory: 3548Mi

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
                memory: 4Gi
            requests:
                cpu: 2
                memory: 4Gi

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
            requests:
                cpu: 500m
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

.. _helm-chart-config:

Параметры конфигурации Helm chart
-------------------------------------

Раздел описывает параметры Helm chart, используемые для тонкой настройки развёртывания платформы Citeck в Kubernetes-кластере.
Параметры позволяют управлять ресурсами, репликами, переменными окружения и другими характеристиками микросервисов.

Описание параметров представлено в `примере Helm chart <https://github.com/Citeck/helm-value-samples/blob/master/values.yaml>`_.


Общее описание
~~~~~~~~~~~~~~~~~~

.. note::

    ``<mSRV>`` заменяется на имя микросервиса, например ``EcosApp``, ``RabbitmqApp`` и т.д.

Общие параметры
""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``.Values.FQDN``
     - Доменное имя платформы
   * - ``.Values.TenantID``
     - Уникальный идентификатор тенанта
   * - ``.Values.clusterDomain``
     - Домен кластера Kubernetes

Управление микросервисами
"""""""""""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``.Values.<mSRV>.enabled``
     - Включение/отключение микросервисов
   * - ``.Values.<mSRV>.clearData``
     - Очистка данных при старте контейнера
   * - ``.Values.<mSRV>.type``
     - Тип ingress
   * - ``.Values.<mSRV>.apiVersion``
     - Версия API ingress
   * - ``.Values.<mSRV>.secretName``
     - Используемый TLS сертификат
   * - ``.Values.<mSRV>.albIngress.enabled``
     - Использовать ALB ingress контроллер

Контейнеры и образы
"""""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``.Values.<mSRV>.image.registry``
     - Реестр образов
   * - ``.Values.<mSRV>.image.repository``
     - Репозиторий образов
   * - ``.Values.<mSRV>.image.tag``
     - Тег образа
   * - ``.Values.<mSRV>.image.pullSecrets``
     - Секреты для доступа к реестру
   * - ``.Values.<mSRV>.initContainers.image.*``
     - Настройки init-контейнеров

Vault и секреты
""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``.Values.<mSRV>.vault.enabled``
     - Включение Vault
   * - ``.Values.<mSRV>.vault.*``
     - Переменные окружения и пароли для сервисов (MongoDB, PostgreSQL, Keycloak и др.)

Переменные окружения
""""""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``.Values.<mSRV>.environments.username/password``
     - Логин/пароль администратора
   * - ``.Values.<mSRV>.environments.javaOpts``
     - Java-опции старта микросервисов
   * - ``.Values.<mSRV>.environments.*``
     - Специфичные переменные (Solr, Alfresco, Flowable и др.)

Хранилища и PVC
""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``.Values.<mSRV>.persistence.enabled``
     - Включение persistent-хранилища
   * - ``.Values.<mSRV>.persistence.size``
     - Размер PVC
   * - ``.Values.<mSRV>.persistence.storageClass``
     - StorageClass PVC
   * - ``.Values.<mSRV>.persistence.accessModes``
     - Режим доступа PVC
   * - ``.Values.<mSRV>.persistence.existingClaim``
     - Использовать существующий PVC
   * - ``.Values.<mSRV>.persistence.backup*``
     - Параметры PVC для бэкапов

Метрики и мониторинг
""""""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``.Values.<mSRV>.metrics.enabled``
     - Включение экспорта метрик
   * - ``.Values.<mSRV>.metrics.config``
     - Конфигурация jmx-exporter
   * - ``.Values.<mSRV>.metrics.serviceMonitor.*``
     - Настройки ServiceMonitor
   * - ``.Values.<mSRV>.metrics.service.ports.*``
     - Порты метрик
   * - ``.Values.<mSRV>.metrics.containerSecurityContext.*``
     - Контекст безопасности контейнера
   * - ``.Values.<mSRV>.metrics.startupProbe.*``
     - Startup Probe
   * - ``.Values.<mSRV>.metrics.readinessProbe.*``
     - Readiness Probe
   * - ``.Values.<mSRV>.metrics.livenessProbe.*``
     - Liveness Probe

Ресурсы и ограничения
""""""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``.Values.<mSRV>.resources``
     - CPU и память для микросервисов
   * - ``.Values.<mSRV>.tolerations``
     - Tolerations для Pods

Прочее
""""""""""""""""""

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``.Values.<mSRV>.webapp.properties.webUrl``
     - URL для Spring-приложений
   * - ``.Values.<mSRV>.x509.certs``
     - Сертификаты (неясное назначение)

.. _zookeeper-ecos-chart:

ZooKeeper в чарте ecos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Начиная с версии **1.3.108** чарт поддерживает два образа Zookeeper: Bitnami и официальный Apache. Дефолтный не менялся — без новых флагов, остаётся на Bitnami.

Режимы
""""""""""""""""""

``ZookeeperApp.legacyStartCmd.enabled`` выбирает layout и команду старта.

.. list-table::
   :header-rows: 1
   :widths: 20 40 40
   :class: tight-table

   * - Свойство
     - Bitnami (``true``, дефолт)
     - Official (``false``)
   * - Команда
     - ``/entrypoint.sh /run.sh``
     - ``/docker-entrypoint.sh zkServer.sh start-foreground``
   * - Том
     - ``/bitnami/zookeeper`` (данные в ``data/myid``)
     - ``/data`` (``/data/myid``)
   * - UID / fsGroup
     - ``1001``
     - ``1000``
   * - Env
     - ``ZOO_SERVER_ID``, ``ZOO_PORT_NUMBER``, …
     - ``ZOO_MY_ID``, ``ZOO_DATA_DIR=/data``, ``ZOO_SERVERS`` вида ``server.1=host:2888:3888;2181``
   * - Проба
     - ``echo ruok | nc localhost 2181 | grep imok``
     - ``ruok`` через bash ``/dev/tcp`` (в образе нет ``nc``)
   * - Тег чарта по умолчанию
     - ``3.6.2-debian-10-r124``
     - —

``legacyStartCmd`` без нужного образа не переключать: Bitnami не поймёт ``/data`` и ``/docker-entrypoint.sh``, переход с Bitnami на official — возможен.

Флаги
""""""

.. code-block:: yaml

   ZookeeperApp:
     legacyStartCmd:
       enabled: true    # true = Bitnami, false = official
     migrateFromBitnami:
       enabled: true    # только official: flatten data/ → /data и chown

Апгрейд Bitnami → Bitnami
""""""""""""""""""""""""""""""""""""

Остаётесь на Bitnami, нужен только более новый тег (3.6 / 3.8 → 3.9.3). Флаг не выключать, migrate не нужен.

.. code-block:: yaml

   ZookeeperApp:
     legacyStartCmd:
       enabled: true
     image:
       tag: 3.9.3-debian-12-r22

Тот же PVC, ``/bitnami/zookeeper``, UID ``1001``. Snapshot читается как есть.

Дальше 3.9.3 на Bitnami не поднимать: у 3.9.4+ другой entrypoint, чарт под него не заточен. Если нужна 3.9.4+ — official.

Переход Bitnami → official (тот же PVC)
""""""""""""""""""""""""""""""""""""""""""""""""""""""

Данные на диске не копируются и не удаляются. Меняется только путь, по которому контейнер видит том, и init один раз поправляет вложенную папку.

На Bitnami PVC смонтирован как ``/bitnami/zookeeper``. Файлы лежат так:

.. code-block:: text

   /bitnami/zookeeper/data/myid
   /bitnami/zookeeper/data/version-2/

На official тот же PVC монтируется как ``/data``. Содержимое диска то же, точка монтирования другая, поэтому те же файлы видны глубже:

.. code-block:: text

   /data/data/myid
   /data/data/version-2/

Official ищет ``/data/myid``, не ``/data/data/myid``. Init ``init-migrate-from-bitnami`` (busybox) поднимает содержимое на уровень выше:

.. code-block:: text

   /data/myid
   /data/version-2/
   /data/.migrated-from-bitnami

Порядок работы init:

1. Есть ``/data/myid`` — том уже в формате official, файлы не трогает.
2. Есть ``/data/data/myid`` — переносит всё из ``data/`` в ``/data``, пишет маркер ``.migrated-from-bitnami``.
3. Нет ни того ни другого — пустой том, ZK сам создаст ``myid``.
4. В любом случае ``chown`` на ``runAsUser:fsGroup`` (для official это ``1000:1000``). Если оставить UID Bitnami ``1001``, official не сможет писать в том.

.. code-block:: yaml

   ZookeeperApp:
     legacyStartCmd:
       enabled: false
     migrateFromBitnami:
       enabled: true
     securityContext:
       runAsUser: 1000
       fsGroup: 1000
     image:
       registry: harbor.citeck.ru
       repository: docker-hub/library/zookeeper
       tag: "3.9.5"
       pullSecrets: harbor-docker-rpoxy
     persistence:
       enabled: true
       volumePermissions:
         enabled: true

После этого шага ``legacyStartCmd: true`` обратно не включать: пути уже не Bitnami, под не будет стартовать.

Пробы
"""""""

Тайминги из values (дефолт): 

- liveness delay 30 с, 
- readiness 5 с, 
- timeout 5 с, 
- 6 фейлов. 

На апгрейде чарта Bitnami — пробу не меняют.

Память
"""""""""""

В поде два разных лимита: Kubernetes (``resources.limits.memory``) и JVM-куча (heap). Если Java просит больше, чем даёт kube, под убивают с ``OOMKilled``.

Bitnami режет сам. Чарт ставит ``ZOO_HEAP_SIZE`` из ``environments.heapSize`` (дефолт ``512``, в мегабайтах):

.. code-block:: yaml

   ZookeeperApp:
     environments:
       heapSize: 512
     resources: |
       limits:
         memory: 768Mi
       requests:
         memory: 768Mi

JVM-куча ~512 Mi, запас в limit на метаспейс и нативные буферы. Так устроен дефолт чарта (768 Mi).

Official переменную ``ZOO_HEAP_SIZE`` игнорирует. Без ``JVMFLAGS`` JVM сама выбирает JVM-кучу (часто от размера контейнера). Чарт пишет ``JVMFLAGS``, только если задать ``environments.jvmFlags``. Если official начнёт упираться в память (OOM или тяжёлые пробы), поднять limit и явно ограничить кучу:

.. code-block:: yaml

   ZookeeperApp:
     environments:
       jvmFlags: "-Xmx256m -Xms256m"
     resources: |
       limits:
         cpu: 500m
         memory: 768Mi
       requests:
         cpu: 300m
         memory: 768Mi

``-Xmx`` держать заметно ниже ``limits.memory``: кроме кучи есть метаспейс, треды, прямые буферы. ``heapSize`` на official на это не влияет.

Итого: выставлять ``heapSize`` на official можно, но без смысла. Это не ошибка чарта и не поломка — просто мёртвая env.

Проверка после деплоя
"""""""""""""""""""""""""

.. code-block:: bash

   kubectl -n <ns> get pod zookeeper-app-0
   kubectl -n <ns> logs zookeeper-app-0 --tail=50
   kubectl -n <ns> logs zookeeper-app-0 -c init-migrate-from-bitnami
   kubectl -n <ns> exec zookeeper-app-0 -- zkCli.sh -server 127.0.0.1:2181 ls /ecos

Под должен быть ``1/1 Running``, в логах ZK — bind на 2181 и чтение snapshot, ``/ecos`` — прежний набор каталогов. Лог init-контейнера покажет один из трёх исходов: ``flatten bitnami data/ -> /data`` (первый переход), ``already official layout`` (повторный старт после миграции) или ``empty volume, nothing to migrate`` (пустой PVC). На томе после миграции (``ls -la /data``) должны быть ``myid`` и ``version-2``, без вложенного ``/data/data/myid``.

Чего не делать:

- Не ставить official-тег при ``legacyStartCmd: true``.
- Не возвращать Bitnami после migrate.


.. _k8s-stop-start:

Остановка и запуск
------------------

Раздел описывает плановую остановку и запуск системы, развёрнутой Helm chart ``ecos`` версии 1.4.x. Состав компонентов приведён для релиза 2026.3.

- **Остановка** уменьшает число реплик каждого Deployment и StatefulSet релиза до 0. Helm-релиз, PVC, ConfigMap и Secret остаются, данные сохраняются.
- **Запуск** возвращает каждому компоненту прежнее число реплик.

Систему можно остановить и запустить через ``kubectl``, Argo CD или Kubernetes Dashboard. Порядок компонентов во всех способах одинаковый.

.. warning::

    - Не останавливайте систему через ``helm uninstall`` и не удаляйте Deployment, StatefulSet и PVC: вместе с PVC PostgreSQL и RabbitMQ удалятся данные.
    - Пока система остановлена, не выполняйте ``helm upgrade``, ``helm rollback`` и синхронизацию в Argo CD. Остановка через Scale не меняет манифесты релиза, поэтому деплой вернёт число реплик из чарта и запустит систему раньше времени, например посреди работ с данными.
    - Не останавливайте систему через values. ``replicas: 0`` не сработает: шаблоны чарта подставляют вместо нуля 1. Отключение компонентов через ``enabled: false`` удалит их ресурсы вместе с PVC.
    - Если релизом управляет Argo CD с автосинхронизацией, отключите её до остановки и включите после запуска. Иначе Argo CD вернёт реплики сам.

Порядок
~~~~~~~

Компоненты останавливаются группами в порядке, обратном зависимостям: сервис останавливается только после всех, кто им пользуется.

1. Точка входа — группы 1–2 в таблице ниже: система перестаёт принимать запросы пользователей и внешних систем.
2. Микросервисы — группы 3–7: от прикладных модулей к ядру платформы.
3. Сторонние сервисы, инфраструктура и СУБД — группы 8–10.

Запуск идёт в обратном порядке. Внутри группы компоненты останавливаются и запускаются одновременно. К следующей группе переходите, когда поды предыдущей удалены (при остановке) или готовы (при запуске).

.. note::

    Одновременный запуск всех компонентов, например после ``helm upgrade``, систему не ломает. Init-контейнеры не дают микросервисам стартовать раньше PostgreSQL и RabbitMQ. Остальные зависимости микросервисы отрабатывают сами: повторяют обращения к нужным сервисам, пока те не станут доступны.

    Порядок из таблицы нужен, чтобы:

    - пользователи и внешние системы не попадали в недоподнятую систему;
    - снизить пиковую нагрузку на ноды кластера: при одновременном старте Java-сервисы делят процессор и дольше проходят проверки готовности;
    - при сбое было видно, какой компонент не поднялся.

.. list-table::
   :header-rows: 1
   :widths: 8 8 30 54
   :class: tight-table

   * - Остановка
     - Запуск
     - Компоненты
     - Комментарии
   * - 1
     - 10
     - ``ecos-proxy-app``
     - ``ecos-proxy-app`` — точка входа пользователей.
   * - 2
     - 9
     - ``ecos-gateway-app``
     - ``ecos-gateway-app`` — принимает только внешние запросы: UI, REST API, вебхуки. Микросервисы вызывают друг друга напрямую, минуя gateway.
   * - 3
     - 8
     - | ``ecos-edi-app``
       | ``ecos-ecom-app``
       | ``ecos-service-desk-app``
       | ``ecos-project-tracker-app``
       | ``ecos-power-of-attorneys``
       | ``ecos-ai-app`` (модуль AI)
       | ``ecos-rag-app`` (модуль AI)
       | сервисы, разработанные под заказчика
     - | Прикладные модули и сервисы заказчика: пользуются сервисами платформы, но платформе сами не нужны. Все необязательны, в релизе есть только установленные. Сюда относится всё, чего нет в других группах.
       | ``ecos-edi-app`` — обмен электронными документами с контрагентами через операторов ЭДО.
       | ``ecos-ecom-app`` — email-рассылки, чат-боты, импорт входящих писем в лиды CRM.
       | ``ecos-service-desk-app`` — обработка обращений (Service Desk).
       | ``ecos-project-tracker-app`` — управление проектами и задачами.
       | ``ecos-power-of-attorneys`` — доверенности, в том числе машиночитаемые (МЧД).
       | ``ecos-ai-app`` — AI-ассистент.
       | ``ecos-rag-app`` — поиск по базе знаний для AI-ассистента (RAG).
       | Сервисы, разработанные под заказчика, — прикладная логика конкретного проекта.
   * - 4
     - 7
     - | ``ecos-process-app``
       | ``ecos-integrations-app``
     - | Модули из группы 3 работают поверх процессов и интеграций.
       | ``ecos-process-app`` — бизнес-процессы.
       | ``ecos-integrations-app`` — интеграции с внешними системами: маршруты, синхронизация, импорт файлов.
   * - 5
     - 6
     - | ``ecos-uiserv-app``
       | ``ecos-transformations-app``
       | ``ecos-notifications-app``
       | ``ecos-apps-app``
     - | Общие сервисы, которыми пользуются модули и процессы.
       | ``ecos-uiserv-app`` — формы, журналы, меню и дашборды.
       | ``ecos-transformations-app`` — генерация документов по шаблонам и конвертация форматов.
       | ``ecos-notifications-app`` — отправка уведомлений.
       | ``ecos-apps-app`` — раздача артефактов приложений (типов, форм, журналов) по микросервисам.
   * - 6
     - 5
     - | ``ecos-history-app``
       | ``ecos-content-app``
     - | ``ecos-history-app`` — принимает события от всех микросервисов и хранит историю. Останавливается после всех, кто пишет события, чтобы успеть обработать очередь.
       | ``ecos-content-app`` — хранит файлы остальных микросервисов. Останавливается после всех, кто читает и пишет файлы.
   * - 7
     - 4
     - ``ecos-model-app``
     - ``ecos-model-app`` — ядро: типы, пользователи, группы, права. Без него не работают gateway и остальные микросервисы; при старте они ждут его доступности.
   * - 8
     - 3
     - | ``onlyoffice-app``
       | ``mailhog-app`` (Mailpit) — если развёрнут
       | ``qdrant-app`` — если установлен модуль AI
       | ``stt-sidecar-app`` — если установлен модуль AI
     - | Сторонние сервисы, которыми пользуются микросервисы.
       | ``onlyoffice-app`` — конвертация и редактирование документов.
       | ``mailhog-app`` — SMTP-сервер для уведомлений.
       | ``qdrant-app`` — векторное хранилище для ``ecos-rag-app``.
       | ``stt-sidecar-app`` — распознавание речи для ``ecos-ai-app`` и телефонии в ``ecos-integrations-app``.
   * - 9
     - 2
     - | ``ecos-identity-app`` (Keycloak) — если развёрнут в этом релизе
       | ``rabbitmq-app``
       | ``zookeeper-app``
     - | ``ecos-identity-app`` — аутентификация (Keycloak).
       | ``rabbitmq-app`` — шина сообщений.
       | ``zookeeper-app`` — обнаружение сервисов.
   * - 10
     - 1
     - | ``ecos-microservices-postgresql-app``
       | ``ecos-mongodb-app`` — если установлена MongoDB
     - | ``ecos-microservices-postgresql-app`` — СУБД микросервисов.
       | ``ecos-mongodb-app`` — данные старых инсталляций, ещё не перенесённые в PostgreSQL.

Все компоненты — Deployment, кроме ``zookeeper-app`` (StatefulSet).

Порядок действий
~~~~~~~~~~~~~~~~

.. tab-set::

   .. tab-item:: kubectl

      .. rubric:: Подготовка

      Нужен ``kubectl`` с правами в неймспейсе релиза:

      - ``get``, ``scale``, ``annotate`` для deployments и statefulsets;
      - ``get``, ``list``, ``watch`` для pods.

      Задайте неймспейс и определите функции в той же bash-сессии, где будете останавливать и запускать систему:

      .. code-block:: bash

         NS=<неймспейс>

         # Группы в порядке остановки (запуск — в обратном порядке)
         G_PROXY="ecos-proxy-app"
         G_GATEWAY="ecos-gateway-app"
         G_BUSINESS="ecos-process-app ecos-integrations-app"
         G_PLATFORM="ecos-uiserv-app ecos-transformations-app ecos-notifications-app ecos-apps-app"
         G_DATA="ecos-history-app ecos-content-app"
         G_CORE="ecos-model-app"
         G_EXT="onlyoffice-app mailhog-app qdrant-app stt-sidecar-app"
         G_INFRA="ecos-identity-app rabbitmq-app zookeeper-app"
         G_DB="ecos-microservices-postgresql-app ecos-mongodb-app"
         KNOWN="$G_PROXY $G_GATEWAY $G_BUSINESS $G_PLATFORM $G_DATA $G_CORE $G_EXT $G_INFRA $G_DB"

         ANN=citeck.ru/replicas-before-stop

         res()   { kubectl get deploy,sts -n "$NS" --field-selector "metadata.name=$1" -o name 2>/dev/null | head -n1; }
         saved() { kubectl get "$1" -n "$NS" -o jsonpath='{.metadata.annotations.citeck\.ru/replicas-before-stop}'; }

         # Группа 3 (прикладные сервисы и модули): всё, что есть в релизе и не входит в остальные группы
         modules() {
           kubectl get deploy,sts -n "$NS" -o jsonpath='{range .items[*]}{.metadata.name}{"\n"}{end}' \
             | grep -vxF -f <(printf '%s\n' $KNOWN)
         }

         # Сохраняет число реплик в аннотацию (если ещё не сохранено), масштабирует в 0 и ждёт удаления подов
         stop() {
           for n in "$@"; do
             k=$(res "$n"); [ -z "$k" ] && { echo "— $n: нет в релизе, пропуск"; continue; }
             [ -z "$(saved "$k")" ] && kubectl annotate "$k" -n "$NS" "$ANN=$(kubectl get "$k" -n "$NS" -o jsonpath='{.spec.replicas}')"
             kubectl scale "$k" -n "$NS" --replicas=0
           done
           for n in "$@"; do
             kubectl get pod -n "$NS" -l "app=$n" -o name | grep -q . && \
               kubectl wait pod -n "$NS" -l "app=$n" --for=delete --timeout=10m
           done
         }

         # Возвращает сохранённое число реплик (по умолчанию 1), ждёт готовности и снимает аннотацию
         start() {
           for n in "$@"; do
             k=$(res "$n"); [ -z "$k" ] && { echo "— $n: нет в релизе, пропуск"; continue; }
             r=$(saved "$k"); kubectl scale "$k" -n "$NS" --replicas="${r:-1}"
           done
           for n in "$@"; do
             k=$(res "$n"); [ -z "$k" ] && continue
             kubectl rollout status "$k" -n "$NS" --timeout=20m && \
               { kubectl annotate "$k" -n "$NS" "$ANN-" >/dev/null 2>&1 || true; }
           done
         }

         # Состояние: реплики, готовность, сохранённое значение
         status() {
           kubectl get deploy,sts -n "$NS" \
             -o custom-columns='NAME:.metadata.name,REPLICAS:.spec.replicas,READY:.status.readyReplicas,SAVED:.metadata.annotations.citeck\.ru/replicas-before-stop'
         }

      Повторный вызов ``stop`` безопасен: уже сохранённое число реплик не перезаписывается нулём.

      Функция ``modules`` выводит компоненты группы 3. Проверьте список перед остановкой:

      .. code-block:: bash

         modules

      Если в списке оказался инфраструктурный компонент (например, своя БД или брокер сообщений), он будет остановлен слишком рано. Добавьте его имя в ``G_DB``, ``G_INFRA`` или ``G_EXT`` и выполните определения заново.

      .. rubric:: Остановка

      Каждый шаг ждёт, пока поды группы удалятся. Штатное завершение пода занимает до 2 минут.

      .. code-block:: bash

         stop $G_PROXY       # 1. закрыть вход
         stop $G_GATEWAY     # 2. внешний API
         stop $(modules)     # 3. прикладные сервисы и модули
         stop $G_BUSINESS    # 4. процессы и интеграции
         stop $G_PLATFORM    # 5. общие сервисы
         stop $G_DATA        # 6. история и контент
         stop $G_CORE        # 7. ecos-model-app
         stop $G_EXT         # 8. OnlyOffice, Mailpit, сервисы модуля AI
         stop $G_INFRA       # 9. Keycloak, RabbitMQ, ZooKeeper
         stop $G_DB          # 10. СУБД — последней

      Проверка:

      .. code-block:: bash

         status                       # у всех REPLICAS = 0, в SAVED — исходное число
         kubectl get pods -n "$NS"    # подов нет
         kubectl get pvc -n "$NS"     # все PVC на месте, Bound

      .. rubric:: Запуск

      Каждый шаг ждёт готовности (readiness) группы. Java-сервис стартует 1–3 минуты.

      .. code-block:: bash

         start $G_DB         # 1. СУБД
         start $G_INFRA      # 2. Keycloak, RabbitMQ, ZooKeeper
         start $G_EXT        # 3. OnlyOffice, Mailpit, сервисы модуля AI
         start $G_CORE       # 4. ecos-model-app
         start $G_DATA       # 5. история и контент
         start $G_PLATFORM   # 6. общие сервисы
         start $G_BUSINESS   # 7. процессы и интеграции
         start $(modules)    # 8. прикладные сервисы и модули
         start $G_GATEWAY    # 9. внешний API
         start $G_PROXY      # 10. открыть вход

      После шага 1 убедитесь, что PostgreSQL был остановлен штатно. В логе должна быть строка ``database system was shut down at ...``, а не ``was interrupted``:

      .. code-block:: bash

         kubectl logs deploy/ecos-microservices-postgresql-app -n "$NS" | head -n 20

      .. rubric:: Проверка после запуска

      .. code-block:: bash

         status                                   # REPLICAS = READY, колонка SAVED пустая
         kubectl get pods -n "$NS" \
           -o custom-columns='NAME:.metadata.name,STATUS:.status.phase,RESTARTS:.status.containerStatuses[*].restartCount'
         kubectl exec deploy/ecos-microservices-postgresql-app -n "$NS" -- pg_isready
         kubectl exec deploy/rabbitmq-app -n "$NS" -- rabbitmq-diagnostics -q check_running

   .. tab-item:: Argo CD

      .. rubric:: Подготовка

      1. Проверьте права учётной записи Argo CD на приложение:

         - просмотр приложения и логов подов: ``applications, get`` и ``logs, get``;
         - изменение политики синхронизации: ``applications, update``;
         - действие Scale: ``applications, action/apps/Deployment/scale`` и ``applications, action/apps/StatefulSet/scale``;
         - для проверок через терминал пода — ``exec, create``.

      2. Откройте приложение. Оно должно быть в статусе **Synced** и **Healthy**. Если приложение в статусе **OutOfSync**, выясните причину до остановки: иначе отложенные изменения из Git применятся, когда вы включите автосинхронизацию после запуска.
      3. Определите состав группы 3. В панели фильтров отметьте **Kinds** ``Deployment`` и ``StatefulSet``: к группе 3 относятся все компоненты, которых нет в остальных группах таблицы.
      4. Запишите число реплик компонентов, у которых оно больше одной: при запуске нужно вернуть именно его. Значение видно в окне Scale и в манифесте из Git (вкладка **Desired Manifest**, поле ``spec.replicas``).
      5. Нажмите **App Details**, запишите текущую политику синхронизации (**Auto-Sync**, **Prune Resources**, **Self Heal**) и нажмите **Disable Auto-Sync**. Если приложением управляет ApplicationSet или родительское приложение (App of Apps), отключите автосинхронизацию на их уровне: иначе родитель вернёт прежнюю политику.

      .. rubric:: Остановка

      Для каждой группы по порядку из столбца «Остановка»:

      1. В дереве ресурсов приложения нажмите на Deployment компонента (для ``zookeeper-app`` — на StatefulSet).
      2. Нажмите **Actions** → **Scale**, введите ``0`` и нажмите **OK**.
      3. Дождитесь, пока поды всех компонентов группы исчезнут из дерева. Штатное завершение пода занимает до 2 минут.

      Если в меню **Actions** нет пункта **Scale** (старые версии Argo CD), откройте вкладку **Live Manifest**, нажмите **Edit**, замените значение ``spec.replicas`` на ``0`` и нажмите **Save**.

      После первой остановки приложение перейдёт в статус **OutOfSync** — это ожидаемо. Не запускайте Sync.

      Когда все группы остановлены, в дереве не должно остаться подов. В фильтре **Kinds** отметьте ``PersistentVolumeClaim`` и убедитесь, что все PVC на месте.

      .. rubric:: Запуск

      Для каждой группы по порядку из столбца «Запуск»:

      1. Нажмите на Deployment компонента (для ``zookeeper-app`` — на StatefulSet) → **Actions** → **Scale**.
      2. Введите прежнее число реплик (обычно ``1``) и нажмите **OK**.
      3. Дождитесь, пока поды группы станут **Healthy**. Java-сервис стартует 1–3 минуты.

      После запуска СУБД убедитесь, что PostgreSQL был остановлен штатно. Откройте под ``ecos-microservices-postgresql-app`` → вкладка **Logs**: в начале лога должна быть строка ``database system was shut down at ...``, а не ``was interrupted``.

      Когда все группы запущены, нажмите **App Details** → **Enable Auto-Sync** и верните прежние значения **Prune Resources** и **Self Heal**. Приложение должно перейти в статус **Synced** и **Healthy**. Если оно осталось в **OutOfSync**, откройте **App Diff**: у какого-то компонента число реплик не совпадает с Git.

      .. rubric:: Проверка после запуска

      - Все поды в дереве — **Running** и **Healthy**.
      - Если доступен терминал пода (вкладка **Terminal**): ``pg_isready`` в поде ``ecos-microservices-postgresql-app`` и ``rabbitmq-diagnostics -q check_running`` в поде ``rabbitmq-app``.

   .. tab-item:: Kubernetes Dashboard

      .. rubric:: Подготовка

      1. Проверьте права учётной записи Dashboard в неймспейсе релиза:

         - ``get``, ``list``, ``watch`` для deployments, statefulsets, pods, events и persistentvolumeclaims;
         - ``get``, ``update``, ``patch`` для deployments/scale и statefulsets/scale;
         - ``get`` для pods/log;
         - для проверок через терминал пода — ``create`` для pods/exec.

      2. Войдите в Dashboard и выберите неймспейс релиза в списке вверху страницы.
      3. Определите состав группы 3. Откройте **Workloads** → **Deployments** и **Stateful Sets**: к группе 3 относятся все компоненты, которых нет в остальных группах таблицы.
      4. Запишите число реплик компонентов, у которых оно больше одной (колонка **Pods**, например ``2 / 2``): при запуске нужно вернуть именно его.
      5. Если релизом управляет Argo CD с автосинхронизацией, попросите администратора Argo CD отключить её (см. вкладку **Argo CD**).

      .. rubric:: Остановка

      Для каждой группы по порядку из столбца «Остановка»:

      1. Откройте **Workloads** → **Deployments** (для ``zookeeper-app`` — **Stateful Sets**), в строке компонента — меню **⋮** → **Scale**.
      2. В поле **Desired replicas** введите ``0`` и нажмите **Scale**.
      3. Дождитесь, пока поды всех компонентов группы исчезнут в **Workloads** → **Pods**. Штатное завершение пода занимает до 2 минут.

      Когда все группы остановлены, проверьте:

      - **Workloads** → **Pods**: подов нет;
      - **Workloads** → **Deployments** и **Stateful Sets**: у всех компонентов ``0 / 0``;
      - **Config and Storage** → **Persistent Volume Claims**: все PVC на месте, в статусе ``Bound``.

      .. rubric:: Запуск

      Для каждой группы по порядку из столбца «Запуск»:

      1. Откройте **Workloads** → **Deployments** (для ``zookeeper-app`` — **Stateful Sets**), в строке компонента — меню **⋮** → **Scale**.
      2. В поле **Desired replicas** введите прежнее число реплик (обычно ``1``) и нажмите **Scale**.
      3. Дождитесь, пока поды группы перейдут в статус ``Running``, а у компонентов в списке Deployments станет ``1 / 1``. Java-сервис стартует 1–3 минуты.

      После запуска СУБД убедитесь, что PostgreSQL был остановлен штатно. В **Workloads** → **Pods** откройте под ``ecos-microservices-postgresql-app-…`` → **Logs**: в начале лога должна быть строка ``database system was shut down at ...``, а не ``was interrupted``.

      .. rubric:: Проверка после запуска

      - **Workloads** → **Deployments** и **Stateful Sets**: у всех компонентов число готовых подов равно желаемому.
      - **Workloads** → **Pods**: все поды в статусе ``Running``, в колонке **Restarts** нули.
      - Если доступен терминал пода (меню **⋮** → **Exec**): ``pg_isready`` в поде ``ecos-microservices-postgresql-app-…`` и ``rabbitmq-diagnostics -q check_running`` в поде ``rabbitmq-app-…``.

Проверка работы и типовые проблемы
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

После запуска откройте систему в браузере и проверьте:

- вход в систему;
- открытие журнала;
- открытие карточки документа;
- открытие документа в редакторе (если используется OnlyOffice).

Типовые проблемы:

- **Под висит в** ``Init``. Init-контейнеры ждут PostgreSQL или RabbitMQ. Проверьте, что они запущены, и посмотрите события пода.
- **В логах сервиса** ``Patch ... depends on app 'emodel', but it is not available yet``. Сервис ждёт ``ecos-model-app``. Проверьте, что ``ecos-model-app`` запущен и готов.
- **PostgreSQL не стартует, в событиях пода** ``Multi-Attach error``. Старый под ещё держит том. Дождитесь его удаления.
- **Микросервис перезапускается по кругу** (``CrashLoopBackOff``). Посмотрите логи пода. Если зависимости уже поднялись, перезапустите сервис: ``kubectl rollout restart deploy/<имя> -n <неймспейс>`` или действие **Restart** в Argo CD и Dashboard.
- **Реплики вернулись сами, пока система была остановлена.** Прошёл деплой релиза или синхронизация Argo CD.


.. _k8s-secrets-encryption-key:

Ключ шифрования секретов
------------------------

``ecos-model-app`` хранит :ref:`секреты <ecos_secret>` в своей БД в зашифрованном виде (AES/GCM). Секреты — это логины и пароли, токены, ключи и сертификаты, на которые ссылаются эндпоинты внешних систем, маршруты Camel DSL и другие интеграции. Ключ шифрования задаётся параметрами Helm chart.

.. warning::

    Если ключ не задан, используется ключ по умолчанию. Он одинаковый во всех инсталляциях и опубликован в открытом коде, поэтому любой, у кого есть копия БД, сможет расшифровать секреты. При профиле ``prod`` ``ecos-model-app`` пишет в лог ``SECURITY ALERT``, но продолжает работать. Для каждой инсталляции генерируйте собственный ключ.

Генерация ключа
~~~~~~~~~~~~~~~

Ключ — 128-битный ключ AES в кодировке Base64:

.. code-block:: bash

   openssl rand -base64 16

Параметры Helm chart
~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 40 60
   :class: tight-table

   * - Параметр
     - Описание
   * - ``EcosModelApp.secret.encryption.current.key``
     - Текущий ключ: им шифруются секреты.
   * - ``EcosModelApp.secret.encryption.previous.key``
     - Предыдущий ключ. Нужен только при смене ключа, чтобы расшифровать секреты, зашифрованные прежним ключом.
   * - ``EcosModelApp.secret.encryption.existingSecret``
     - Имя существующего Kubernetes Secret с ключами ``current-key`` (обязательный) и ``previous-key`` (необязательный). Если параметр задан, ``current.key`` и ``previous.key`` не используются. Secret должен существовать до деплоя.

Ключ в values:

.. code-block:: yaml

   EcosModelApp:
     secret:
       encryption:
         current:
           key: "<ключ>"

Ключ в существующем Secret:

.. code-block:: bash

   kubectl create secret generic ecos-model-encryption -n <неймспейс> \
     --from-literal=current-key="$(openssl rand -base64 16)"

.. code-block:: yaml

   EcosModelApp:
     secret:
       encryption:
         existingSecret: ecos-model-encryption

Подробнее о Secret и режимах их подключения — в разделе :ref:`Управление секретами через Kubernetes Secrets <kubernetes-secrets>`.

.. important::

    Ключ должен быть задан при каждом деплое. Если убрать его из values или Secret, чарт подставит ключ по умолчанию, и ``ecos-model-app`` перестанет расшифровывать секреты, зашифрованные вашим ключом.

Смена ключа
~~~~~~~~~~~

1. Сгенерируйте новый ключ.
2. Задайте новый ключ в ``current.key`` (``current-key``), а прежний — в ``previous.key`` (``previous-key``). Если инсталляция работала на ключе по умолчанию, прежний ключ — ``Cz6ruLL9XkNjn4vaU0/MDQ==``.
3. Выполните деплой. При старте ``ecos-model-app`` расшифрует секреты прежним ключом и зашифрует их новым.
4. Когда ``ecos-model-app`` запустился и секреты работают, прежний ключ можно убрать из ``previous.key``. Сохраните его вместе с резервными копиями БД, сделанными до смены ключа.

Резервные копии и перенос БД
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Секреты в копии БД расшифровываются только тем ключом, которым они были зашифрованы. Поэтому:

- храните ключ вместе с резервными копиями БД ``ecos-model-app``;
- при восстановлении или переносе БД на другой стенд задайте на нём тот же ключ. Если на новом стенде нужен свой ключ, укажите перенесённый как предыдущий (``previous.key``): при старте ``ecos-model-app`` перешифрует секреты новым ключом.

Если ключ не совпадает, ``ecos-model-app`` не расшифрует секреты: в логе будет ``Cannot decrypt secret ... Re-save the secret to fix it``, и секреты придётся заводить заново.

Подробнее о секретах — в разделе :ref:`Шифрование секретов <secrets_encryption>`.
