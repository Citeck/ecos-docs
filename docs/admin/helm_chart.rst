Параметры конфигурации Helm chart
==================================

.. note::

    Доступно только в Enterprise версии.

Пример Helm chart с описанием параметров
-------------------------------------------

Описание параметров представлено в `примере Helm chart <https://github.com/Citeck/helm-value-samples/blob/master/values.yaml>`_.


Общее описание
---------------

.. note::

    ``<mSRV>`` заменяется на имя микросервиса, например ``EcosApp``, ``RabbitmqApp`` и т.д.

Общие параметры
~~~~~~~~~~~~~~~~~~

- ``.Values.FQDN``: Доменное имя платформы
- ``.Values.TenantID``: Уникальный идентификатор тенанта
- ``.Values.clusterDomain``: Домен кластера Kubernetes

Управление микросервисами
~~~~~~~~~~~~~~~~~~~~~~~~~~

- ``.Values.<mSRV>.enabled``: Включение/отключение микросервисов
- ``.Values.<mSRV>.clearData``: Очистка данных при старте контейнера
- ``.Values.<mSRV>.type``: Тип ingress
- ``.Values.<mSRV>.apiVersion``: Версия API ingress
- ``.Values.<mSRV>.secretName``: Используемый TLS сертификат
- ``.Values.<mSRV>.albIngress.enabled``: Использовать ALB ingress контроллер

Контейнеры и образы
~~~~~~~~~~~~~~~~~~~~~

- ``.Values.<mSRV>.image.registry``: Реестр образов
- ``.Values.<mSRV>.image.repository``: Репозиторий образов
- ``.Values.<mSRV>.image.tag``: Тег образа
- ``.Values.<mSRV>.image.pullSecrets``: Секреты для доступа к реестру
- ``.Values.<mSRV>.initContainers.image.*``: Настройки init-контейнеров

Vault и секреты
~~~~~~~~~~~~~~~~~~

- ``.Values.<mSRV>.vault.enabled``: Включение Vault
- ``.Values.<mSRV>.vault.*``: Переменные окружения и пароли для сервисов (MongoDB, PostgreSQL, Keycloak и др.)

Переменные окружения
~~~~~~~~~~~~~~~~~~~~~~

- ``.Values.<mSRV>.environments.username/password``: Логин/пароль администратора
- ``.Values.<mSRV>.environments.javaOpts``: Java-опции старта микросервисов
- ``.Values.<mSRV>.environments.*``: Специфичные переменные (Solr, Alfresco, Flowable и др.)

Хранилища и PVC
~~~~~~~~~~~~~~~~~~

- ``.Values.<mSRV>.persistence.enabled``: Включение persistent-хранилища
- ``.Values.<mSRV>.persistence.size``: Размер PVC
- ``.Values.<mSRV>.persistence.storageClass``: StorageClass PVC
- ``.Values.<mSRV>.persistence.accessModes``: Режим доступа PVC
- ``.Values.<mSRV>.persistence.existingClaim``: Использовать существующий PVC
- ``.Values.<mSRV>.persistence.backup*``: Параметры PVC для бэкапов

Метрики и мониторинг
~~~~~~~~~~~~~~~~~~~~~~

- ``.Values.<mSRV>.metrics.enabled``: Включение экспорта метрик
- ``.Values.<mSRV>.metrics.config``: Конфигурация jmx-exporter
- ``.Values.<mSRV>.metrics.serviceMonitor.*``: Настройки ServiceMonitor
- ``.Values.<mSRV>.metrics.service.ports.*``: Порты метрик
- ``.Values.<mSRV>.metrics.containerSecurityContext.*``: Контекст безопасности контейнера
- ``.Values.<mSRV>.metrics.startupProbe.*``: Startup Probe
- ``.Values.<mSRV>.metrics.readinessProbe.*``: Readiness Probe
- ``.Values.<mSRV>.metrics.livenessProbe.*``: Liveness Probe

Ресурсы и ограничения
~~~~~~~~~~~~~~~~~~~~~~~

- ``.Values.<mSRV>.resources``: CPU и память для микросервисов
- ``.Values.<mSRV>.tolerations``: Tolerations для Pods

Прочее
~~~~~~~

- ``.Values.<mSRV>.webapp.properties.webUrl``: URL для Spring-приложений
- ``.Values.<mSRV>.x509.certs``: Сертификаты (неясное назначение)





