.. _citeck_launcher:

Citeck Launcher
===============

**Citeck Launcher** — кроссплатформенный инструмент для локального развёртывания и управления платформой Citeck. Позволяет запустить Citeck Community в несколько кликов, не требуя ручной настройки Docker-окружения.

**Возможности:**

- Быстрый локальный запуск Citeck Community — с :ref:`демонстрационными данными <ecos_modules>` или без них.
- Управление несколькими изолированными окружениями (namespace) в одном рабочем пространстве.
- Мониторинг микросервисов: статус, потребление CPU/RAM, логи, запуск и остановка.
- Создание снапшотов данных и восстановление из них.
- Безопасное хранение секретов с шифрованием мастер-паролем.
- Обновление Citeck Community без потери данных.
- Поддержка нескольких рабочих пространств с независимыми конфигурациями.

**Требования:**

- Установлен `Docker <https://docs.docker.com/get-docker/>`_
- Не менее **16 ГБ** ОЗУ

**Поддерживаемые платформы:**

- Windows — **.msi**
- Linux — **.deb**
- macOS — **.dmg**

Актуальный дистрибутив доступен на `странице релизов <https://github.com/Citeck/citeck-launcher/releases>`_.

.. list-table::
      :widths: 20 20
      :align: center

      * - |

            .. image:: _static/launcher/01.png
                  :width: 500
                  :align: center

        - |

            .. image:: _static/launcher/02.png
                  :width: 500
                  :align: center

.. toctree::
    :maxdepth: 3

    launcher/quick_start
    launcher/update
    launcher/overview
    launcher/namespace
    launcher/secrets
    launcher/dump
    launcher/workspace
