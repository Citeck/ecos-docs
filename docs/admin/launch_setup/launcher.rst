.. _citeck_launcher:

Citeck Launcher: локальный режим
================================

**Citeck Launcher** в локальном режиме — кроссплатформенное десктопное приложение (Windows / Linux / macOS) для развёртывания и управления платформой Citeck без необходимости ручной настройки Docker. Подходит для локальной разработки и демонстраций.

Для установки на Linux-серверах (без GUI, через CLI + systemd) используйте :ref:`серверный режим <launcher_server>`.

**Возможности:**

- Быстрый локальный запуск Citeck Community и Enterprise версий — с :ref:`демонстрационными данными <ecos_modules>` или без них.
- Управление несколькими изолированными окружениями (namespace) в одном рабочем пространстве.
- Мониторинг микросервисов: статус, потребление CPU/RAM, логи, запуск и остановка.
- Создание снапшотов данных и восстановление из них.
- Безопасное хранение секретов с шифрованием мастер-паролем.
- Обновление Citeck без потери данных.
- Поддержка нескольких рабочих пространств с независимыми конфигурациями.

.. seealso::

   Начиная с версии **2.0** доступен также :ref:`серверный режим <launcher_server>` — для развёртывания Citeck на Linux-серверах через CLI и systemd.

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
