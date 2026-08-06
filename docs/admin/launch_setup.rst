Установка и развёртывание
============================

Раздел описывает способы развёртывания платформы Citeck — от локального запуска для разработки до производственных конфигураций в Kubernetes.

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

      Развёртывание платформы через Docker Compose для тестовых и небольших производственных сред.

   .. grid-item-card:: Kubernetes
      :link: kubernetes
      :link-type: ref

      Развёртывание платформы в Kubernetes-кластере: менеджмент ресурсов подов и контейнеров, параметры конфигурации Helm chart (Enterprise), генерация ключа шифрования при развёртывании нового сервера.

   .. grid-item-card:: Сайзинг: тестовая и продуктивная среда
      :link: sizing
      :link-type: ref

      Рекомендации по планированию инфраструктуры (ноды, диски, внешние сервисы) для развёртывания Citeck с числом именных пользователей до 1 000.

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