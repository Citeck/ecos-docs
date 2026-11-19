Установка и развёртывание
============================

Раздел описывает способы развёртывания платформы Citeck — от локального запуска для разработки до производственных конфигураций в Kubernetes.

Платформа поставляется в виде Docker-образов и разворачивается с использованием средств контейнеризации (Docker) и оркестрации (Kubernetes):

- **Kubernetes** — основной вариант для продуктивных окружений. Все компоненты платформы устанавливаются и обновляются автоматически с помощью Helm chart, в том числе из CI/CD-конвейера или GitOps-инструмента (Argo CD). Платформа использует только стандартные объекты Kubernetes и не привязана к конкретному дистрибутиву. Поддерживается развёртывание on-premise в кластере заказчика. Требования к кластеру — в разделе :ref:`Требования к кластеру и автоматизированное развёртывание <k8s-requirements>`.
- **Docker** — для тестовых и небольших продуктивных окружений: Citeck Launcher.

При необходимости доступно развёртывание в закрытом контуре без доступа в интернет: образы размещаются во внутреннем реестре заказчика.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Citeck Launcher: локальный режим
      :link: citeck_launcher
      :link-type: ref

      Графический инструмент (Windows / Linux / macOS) для быстрого локального запуска Citeck Community без ручной настройки Docker.

   .. grid-item-card:: Citeck Launcher: серверный режим
      :link: launcher_server
      :link-type: ref

      Установка и управление платформой Citeck на Linux-серверах через CLI и systemd.

   .. grid-item-card:: Docker Compose
      :link: docker_compose
      :link-type: ref

      Развёртывание платформы через Docker Compose для тестовых и небольших продуктивных окружений.

   .. grid-item-card:: Kubernetes
      :link: kubernetes
      :link-type: ref

      Развёртывание платформы в Kubernetes-кластере: требования к кластеру, автоматизированная установка и обновление через Helm chart, менеджмент ресурсов подов и контейнеров, параметры конфигурации Helm chart (Enterprise), генерация ключа шифрования при развёртывании нового сервера.

   .. grid-item-card:: Типовой сайзинг
      :link: sizing
      :link-type: ref

      Планирование инфраструктуры под развёртывание Citeck с числом именных пользователей до 2 000: конфигурации worker-нод Kubernetes и виртуальных машин, диски, требования к внешним сервисам (PostgreSQL, S3, OpenSearch).

   .. grid-item-card:: Kubernetes Secrets
      :link: kubernetes-secrets
      :link-type: ref

      Хранение чувствительных данных (пароли, токены, credentials) в Kubernetes Secrets вместо ``values.yaml``.

   .. grid-item-card:: Сервисы Docker
      :link: docker_services
      :link-type: ref

      Справочник по Docker-образам платформы: назначение сервисов, шаблоны описания в docker-compose, переменные окружения, лог успешного запуска.

.. toctree::
    :maxdepth: 2
    :hidden:

    launch_setup/launcher
    launch_setup/launcher_server
    launch_setup/docker-compose
    launch_setup/kubernetes
    launch_setup/sizing
    launch_setup/kubernetes_secrets
    launch_setup/docker_services
