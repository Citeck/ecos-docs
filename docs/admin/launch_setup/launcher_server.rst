.. _launcher_server:

Citeck Launcher: серверный режим
================================

**Citeck Launcher** в серверном режиме -- это единый исполняемый файл (Go binary, ~27 МБ), предназначенный для развёртывания и управления платформой Citeck на серверах Linux. В отличие от :ref:`десктопной версии <citeck_launcher>`, серверный режим работает без графического и веб-интерфейса: управление осуществляется через **CLI** и **systemd-сервис**.

**Возможности:**

- Полностью автоматизированная установка через интерактивный мастер или one-liner скрипт.
- Управление жизненным циклом платформы: запуск, остановка, перезапуск, обновление.
- TLS из коробки: автоматический HTTPS (Let's Encrypt, включая IP-адреса), самоподписанные сертификаты, пользовательские сертификаты.
- Управление паролем администратора (Keycloak, RabbitMQ, PgAdmin).
- Интеграция с systemd: автоматический перезапуск при сбоях.
- Горячая перезагрузка конфигурации (``citeck reload``) и точечное редактирование приложений (``citeck edit``).
- Защита данных при обновлении бандла: версии PostgreSQL, RabbitMQ, ZooKeeper и других компонентов привязаны к данным, их обновление и откат выполняются явно (``citeck deps``).
- Резервное копирование и восстановление данных (snapshots).
- Очистка неиспользуемых ресурсов Docker.
- Диагностика и проверка здоровья системы, дампы потоков и памяти JVM (``citeck jstack``, ``citeck jmap``, ``citeck jcmd``).

**Требования:**

- Поддерживаемые платформы:

  - **Linux amd64** (x86_64) -- рекомендуется для production
  - **Linux arm64** (aarch64) -- AWS Graviton, Oracle Cloud Ampere, Raspberry Pi и т.п.

- Установлен `Docker <https://docs.docker.com/engine/install/>`_ (Docker Engine, не Docker Desktop)
- Не менее **16 ГБ** ОЗУ для Community, **24–32 ГБ** для Enterprise
- Не менее **50 ГБ** свободного дискового пространства
- Root-доступ (для systemd и привязки к портам 80/443)

.. warning::

    Для Enterprise-бандла **16 ГБ ОЗУ -- это абсолютный минимум без запаса**. Сразу после установки необходимо отключить 7 необязательных приложений (``citeck stop onlyoffice attorneys ecom service-desk ecos-project-tracker ai edi``), иначе OOM Killer начнёт завершать процессы. Для стабильной работы с полным набором приложений требуется **24--32 ГБ** ОЗУ.

.. seealso::

    Серверный режим доступен начиная с версии **2.0**. Для десктопных систем (Windows / Linux / macOS с GUI) используйте :ref:`локальный режим <citeck_launcher>`.

Для быстрого старта перейдите к разделу :ref:`server_quick_start`.

.. toctree::
    :maxdepth: 2

    launcher_server/quick_start
    launcher_server/commands
    launcher_server/configuration
    launcher_server/dependencies
    launcher_server/jvm_diagnostics
    launcher_server/architecture
    launcher_server/migration_from_compose
    launcher_server/troubleshooting
