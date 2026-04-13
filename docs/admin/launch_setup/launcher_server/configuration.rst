.. _server_configuration:

Конфигурация
=============

Конфигурация серверного режима Citeck Launcher хранится в двух YAML-файлах в директории ``/opt/citeck/conf/``.

.. contents::
    :local:
    :depth: 2

namespace.yml
--------------

Основной файл конфигурации платформы. Определяет, какие компоненты запускать и как их настраивать.

**Расположение:** ``/opt/citeck/conf/namespace.yml``

Структура
~~~~~~~~~~

.. code-block:: yaml

    apiVersion: v1

    # Идентификатор namespace (генерируется автоматически)
    id: citeck-abc123

    # Отображаемое имя
    name: Citeck

    # Ссылка на бандл (набор Docker-образов определённой версии)
    bundleRef: "community:2024.11"

    # Снапшот для инициализации (демо-данные)
    snapshot: with-demo-data

    # Настройки прокси
    proxy:
      host: 203.0.113.45
      port: 443
      tls:
        enabled: true
        letsEncrypt: true
        certFile: ""
        keyFile: ""

    # Аутентификация
    authentication:
      type: keycloak
      users:
        - admin

    # PgAdmin (веб-интерфейс PostgreSQL)
    pgAdmin:
      enabled: false

    # Настройки веб-приложений (переопределение параметров из бандла)
    webapps:
      eapps:
        heapSize: 1024m
      emodel:
        heapSize: 768m
        env:
          CUSTOM_PROPERTY: value

    # Настройки Email (SMTP)
    email:
      host: smtp.example.com
      port: 587
      tls: true
      from: noreply@example.com
      username: mailuser

    # Настройки S3-совместимого хранилища
    s3:
      endpoint: https://s3.example.com
      bucket: citeck-data
      accessKey: AKIAIOSFODNN
      region: us-east-1

Секретные поля (формат ссылок)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Поля, содержащие чувствительные данные (``s3.secretKey``, ``email.password``
и т.д.), в файле ``namespace.yml`` хранятся **не как plain-значения**, а как
ссылки формата ``secret:<имя_ключа>``:

.. code-block:: yaml

   s3:
     endpoint: https://s3.example.com
     bucket: ecos-content
     accessKey: minio-user
     secretKey: secret:s3.secretKey     # ссылка, не plain-значение
   email:
     host: smtp.example.com
     port: 587
     from: noreply@example.com
     password: secret:email.password    # ссылка

Фактические значения зашифрованы и лежат в ``/opt/citeck/conf/secrets/*.json``.
Launcher автоматически резолвит ссылки при генерации env-переменных контейнеров.

При использовании ``citeck setup`` команды (например, ``setup s3``) ссылки
создаются/обновляются автоматически — прямое редактирование ``namespace.yml``
обычно не требуется.

Основные секции
~~~~~~~~~~~~~~~~

**bundleRef**

Определяет версию платформы. Формат: ``repo:key``, например ``community:2024.11``.

- ``repo`` -- идентификатор репозитория бандлов (``community`` или ``enterprise``)
- ``key`` -- версия бандла

Для смены версии используйте ``citeck upgrade``.

**template**

Ссылка на шаблон namespace из workspace-конфигурации (``workspace-v1.yml``). Устанавливается автоматически при ``citeck install``. Шаблоны могут определять приложения, отключённые по умолчанию:

.. code-block:: yaml

    # В workspace-v1.yml
    namespaceTemplates:
      - id: default
        name: Default
        config:
          bundleRef: 'community:LATEST'
        detachedApps:
          - onlyoffice

Приложения из ``detachedApps`` не запускаются при первом старте. Для включения: ``citeck start <app>``.

**proxy**

Настройки прокси-сервера (точка входа для всех HTTP-запросов):

.. list-table::
    :widths: 20 15 65
    :header-rows: 1

    * - Параметр
      - Тип
      - Описание
    * - ``host``
      - string
      - IP-адрес или доменное имя сервера
    * - ``port``
      - int
      - Порт (443 для HTTPS, 80 для HTTP)
    * - ``tls.enabled``
      - bool
      - Включить HTTPS
    * - ``tls.letsEncrypt``
      - bool
      - Использовать Let's Encrypt для получения сертификата
    * - ``tls.certFile``
      - string
      - Путь к пользовательскому файлу сертификата
    * - ``tls.keyFile``
      - string
      - Путь к пользовательскому файлу ключа

**authentication**

Тип аутентификации платформы:

- ``keycloak`` -- аутентификация через Keycloak (рекомендуется для production)
- ``basic`` -- базовая HTTP-аутентификация (для разработки)

**webapps**

Переопределение параметров отдельных приложений. Каждое приложение может иметь:

.. list-table::
    :widths: 20 15 65
    :header-rows: 1

    * - Параметр
      - Тип
      - Описание
    * - ``heapSize``
      - string
      - Размер Java heap (например, ``1024m``, ``2g``)
    * - ``memoryLimit``
      - string
      - Лимит памяти Docker-контейнера
    * - ``env``
      - map
      - Дополнительные переменные окружения
    * - ``image``
      - string
      - Переопределение Docker-образа

**email** (опционально)

Настройки SMTP для отправки уведомлений:

.. code-block:: yaml

    email:
      host: smtp.example.com
      port: 587
      tls: true
      from: noreply@example.com
      username: mailuser
      # Пароль хранится в зашифрованном хранилище секретов

.. note::

    Пароль SMTP задаётся через ``citeck setup email`` и хранится в зашифрованном виде, а не в конфигурационном файле.

**Поле** ``tls`` **и соответствие портам:**

Транспорт SMTP управляется булевым полем ``tls``. Генератор транслирует его в протокол Spring Mail (``smtp`` или ``smtps``), используемый веб-приложениями.

.. list-table::
    :widths: 15 20 65
    :header-rows: 1

    * - Значение
      - Типичный порт
      - Описание
    * - ``true``
      - 587
      - SMTP с STARTTLS (Spring Mail protocol ``smtp`` + ``starttls.enable=true``). Рекомендуемый режим для большинства внешних SMTP-серверов.
    * - ``false``
      - 25
      - Незашифрованный SMTP (Spring Mail protocol ``smtp``). Используется преимущественно для внутренних релеев.

Если имя пользователя (``username``) оставить пустым, SMTP-аутентификация отключается -- это допустимо для релеев, принимающих неавторизованные отправки.

**s3** (опционально, только Enterprise)

Настройки S3-совместимого объектного хранилища. Доступно только в Enterprise-бандлах, где присутствует приложение ``ecos-content``.

.. code-block:: yaml

    s3:
      endpoint: https://s3.example.com
      bucket: citeck-data
      accessKey: AKIAIOSFODNN
      region: us-east-1
      # Secret key хранится в зашифрованном хранилище секретов

Совместимо с Amazon S3, MinIO, и другими S3-совместимыми хранилищами.

.. note::

    В меню ``citeck setup`` пункт S3 отображается только при наличии приложения ``ecos-content`` в бандле. На Community-бандлах он скрыт.

daemon.yml
-----------

Конфигурация самого демона (процесса Citeck Launcher).

**Расположение:** ``/opt/citeck/conf/daemon.yml``

Структура
~~~~~~~~~~

.. code-block:: yaml

    # Язык интерфейса CLI (en, ru, zh, es, de, fr, pt, ja)
    locale: ru

    # Настройки встроенного сервера (внутреннее; не изменяйте -- формат может меняться)
    server:
      webui:
        enabled: true
        listen: "127.0.0.1:7088"

    # Настройки реконсилера (мониторинг и автовосстановление)
    reconciler:
      interval: 60              # интервал проверки в секундах
      livenessPeriod: 30000     # период liveness-проверок в мс
      livenessEnabled: true     # включить liveness-проверки

    # Настройки Docker
    docker:
      pullConcurrency: 4        # параллельных загрузок образов
      stopTimeout: 10           # таймаут остановки контейнера в секундах

Параметры
~~~~~~~~~~

**locale**

Язык для сообщений CLI. Поддерживаемые значения: ``en``, ``ru``, ``zh``, ``es``, ``de``, ``fr``, ``pt``, ``ja``.

Изменение: ``citeck setup language``

**reconciler**

Реконсилер автоматически мониторит состояние приложений и перезапускает упавшие:

- ``interval`` -- как часто проверять состояние (по умолчанию 60 секунд)
- ``livenessPeriod`` -- период liveness-проверок (по умолчанию 30 секунд)
- ``livenessEnabled`` -- включение/выключение liveness-проверок (по умолчанию ``true``)

При сбое приложения реконсилер использует экспоненциальный backoff для повторных попыток запуска (от 1 минуты до 30 минут максимум).

**docker**

- ``pullConcurrency`` -- количество параллельных загрузок Docker-образов (по умолчанию 4)
- ``stopTimeout`` -- время ожидания graceful shutdown контейнера перед SIGKILL (по умолчанию 10 секунд)

Настройка через citeck setup
------------------------------

Команда ``citeck setup`` предоставляет удобный интерактивный интерфейс для изменения конфигурации, не редактируя YAML-файлы вручную.

.. note::

    Интерактивный CLI-доступ к этим настройкам и подробное описание флагов
    отдельных подкоманд (``setup hostname``, ``setup email``, ``setup s3``,
    ``setup admin-password`` и т. д.) описаны в :ref:`server_commands`,
    раздел «setup».

**Hostname** (``citeck setup hostname``)

Изменение IP-адреса или доменного имени. Влияет на:

- URL платформы
- Сертификаты TLS
- Конфигурацию Keycloak

**TLS** (``citeck setup tls``)

Переключение режима TLS. Влияет на сертификаты и порты.

**Auth** (``citeck setup auth``)

Переключение типа аутентификации между Keycloak и Basic.

.. warning::

    Переключение с Basic на Keycloak требует перезапуска всех компонентов. Переключение с Keycloak на Basic удаляет все пользовательские аккаунты Keycloak.

**Resources** (``citeck setup resources``)

Настройка ресурсов приложений (heap size, memory limit). Полезно для оптимизации потребления памяти на серверах с ограниченными ресурсами.

**Admin password** (``citeck setup admin-password``)

Смена пароля администратора. Применяется к компонентам:

- Keycloak (realm ``ecos-app`` — пользовательский вход)
- RabbitMQ
- PgAdmin

Смена происходит через API сервисов в реальном времени, без перезапуска контейнеров.

.. note::

    Внутренние операции платформы (настройка Keycloak, обновление OIDC-клиента,
    смена паролей) выполняются от имени стабильного сервисного аккаунта ``citeck``
    (в master realm Keycloak и в RabbitMQ). Благодаря этому ``citeck setup admin-password``
    может менять пароли человека-администратора в UI-админках Keycloak / RabbitMQ /
    PgAdmin без влияния на работу платформы — лончер продолжает использовать ``citeck``
    SA для своих внутренних операций.

Режимы TLS
-----------

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Режим
      - Описание
    * - **Auto HTTPS**
      - Автоматический выбор: пробует Let's Encrypt, при неудаче переходит на самоподписанный сертификат. Рекомендуемый режим.
    * - **Let's Encrypt**
      - Получение доверенного сертификата от Let's Encrypt. Поддерживает как доменные имена, так и IP-адреса (через shortlived-профиль, сертификаты обновляются каждые ~6 дней).
    * - **Self-signed**
      - Автоматическая генерация самоподписанного сертификата. Браузеры будут показывать предупреждение.
    * - **Custom**
      - Использование собственных файлов сертификата и ключа. Укажите пути к ``cert.pem`` и ``key.pem``.
    * - **HTTP only**
      - Без шифрования. Только для тестовых окружений.

Пароль администратора
----------------------

**Генерация при установке**

При первом запуске в серверном режиме автоматически генерируется случайный пароль администратора. Он применяется к:

- Keycloak (пользователь ``admin`` в realm ``ecos-app``; master-realm управляется отдельно сервисной учётной записью ``citeck``)
- RabbitMQ (пользователь ``admin``)
- PgAdmin (``admin@admin.com``)

Пароль отображается один раз в выводе мастера установки.

.. note::

    В отличие от десктопного режима, где используется стандартный пароль ``admin``, серверный режим генерирует уникальный пароль для каждой установки.

**Смена пароля**

.. code-block:: bash

    citeck setup admin-password

Команда:

1. Запрашивает новый пароль (с подтверждением)
2. Применяет его к Keycloak через ``kcadm.sh``
3. Применяет к RabbitMQ через ``rabbitmqctl``
4. Применяет к PgAdmin через ``setup.py``
5. Перезагружает веб-приложения для применения обновлённого пароля RabbitMQ

Пароль сохраняется между перезапусками и обновлениями.

Структура директорий
---------------------

.. code-block:: text

    /opt/citeck/                 # Корневая директория (CITECK_HOME)
    +-- conf/                    # Конфигурация
    |   +-- namespace.yml        # Конфигурация платформы
    |   +-- daemon.yml           # Конфигурация демона
    |   \-- secrets/             # Зашифрованные секреты (AES-256-GCM)
    +-- data/                    # Данные
    |   +-- repo/                # Git-клоны workspace и бандлов
    |   \-- runtime/             # Данные контейнеров (volumes)
    \-- log/                     # Логи
        \-- daemon.log           # Лог демона (ротация)

    /run/citeck/
    \-- daemon.sock              # Unix-сокет для CLI-демон коммуникации

    /usr/local/bin/
    +-- citeck                   # Основной бинарный файл
    \-- citeck.bak               # Резервная копия (для rollback)

    /etc/systemd/system/
    \-- citeck.service           # Systemd unit-файл

Переменные окружения
---------------------

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Переменная
      - Описание
    * - ``CITECK_HOME``
      - Корневая директория (по умолчанию ``/opt/citeck``)
    * - ``CITECK_RUN``
      - Директория для сокетов (по умолчанию ``/run/citeck``)
