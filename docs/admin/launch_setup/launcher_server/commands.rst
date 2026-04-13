.. _server_commands:

Справочник команд
==================

Все команды выполняются от имени root или с использованием ``sudo``. Общий формат:

.. code-block:: bash

    citeck <command> [options] [arguments]

**Глобальные флаги:**

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``--format json``
      - Вывод в формате JSON (для автоматизации)
    * - ``--yes``
      - Пропустить запросы подтверждения

.. contents::
    :local:
    :depth: 1

install
--------

Интерактивная установка и настройка платформы.

.. code-block:: bash

    citeck install [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``--workspace <path>``
      - Путь к ZIP-архиву workspace (оффлайн-импорт бандлов)
    * - ``--offline``
      - Оффлайн-режим: пропустить сетевые проверки
    * - ``--rollback``
      - Откатить бинарный файл к предыдущей версии

**Примеры:**

.. code-block:: bash

    # Стандартная установка
    citeck install

    # Оффлайн-установка с архивом workspace
    citeck install --workspace /tmp/workspace.zip --offline

    # Откат к предыдущей версии после неудачного обновления
    citeck install --rollback

При вызове на уже установленной системе команда проверит версию и предложит обновление, если новая версия бинарного файла отличается от установленной.

.. note::

    Режим «Auto» (вариант по умолчанию в мастере установки) — это не отдельный
    режим в ``namespace.yml``, а логика выбора: launcher проверяет доступность
    Let's Encrypt; при успехе конфигурация сохраняется как ``letsEncrypt: true``,
    при недоступности — как self-signed. После установки ``citeck setup`` покажет
    конкретный выбранный вариант.

start
------

Запуск платформы (демон + все приложения).

.. code-block:: bash

    citeck start [app] [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``-d``, ``--detach``
      - Запуск в фоне без ожидания (аналог ``docker-compose up -d``)
    * - ``-f``, ``--foreground``
      - Запуск в режиме переднего плана (не форкать демон)
    * - ``--follow``
      - Не выходить после выхода всех приложений в ``RUNNING`` --
        продолжать перерисовывать таблицу статусов каждые 2 секунды
        до Ctrl+C. Полезно при ручном мониторинге запуска платформы.
        По умолчанию ``citeck start`` завершает работу, как только
        все приложения достигли ``RUNNING`` или терминального статуса.
    * - ``--offline``
      - Пропустить git-операции, использовать только локальные данные

**Примеры:**

.. code-block:: bash

    # Запуск с интерактивной таблицей статусов
    citeck start

    # Запуск в фоне
    citeck start -d

    # Запуск конкретного приложения (если было отключено — включает обратно)
    citeck start eapps

    # Запуск с непрерывным мониторингом
    citeck start --follow

При запуске без указания приложения демон стартует в фоновом режиме и отображает интерактивную таблицу с прогрессом запуска всех приложений.

Если приложение было ранее отключено через ``citeck stop <app>`` (detach), команда ``citeck start <app>`` повторно подключает его к namespace — приложение снова будет запускаться при старте/перезагрузке платформы и мониториться реконсилером.

.. note::

   Если systemd-сервис установлен, ``citeck start`` (без аргументов, демон не
   запущен) делегирует запуск ``systemctl start citeck`` — демон запускается
   как systemd-unit с journald-логированием и автоперезапуском. Если systemd
   недоступен, демон форкается напрямую. Флаг ``-d``/``--detach`` принудительно
   обходит systemd и форкает демон напрямую (для контейнеров или ручной отладки).

.. note::

    ``citeck start <app>`` ждёт перехода приложения в ``RUNNING`` по умолчанию.
    Чтобы вернуть управление сразу после отправки запроса (без ожидания), используйте
    флаг ``-d``/``--detach``: ``citeck start <app> -d``. Для опроса состояния отдельно
    подойдёт ``citeck status`` (например, ``watch -n 5 'citeck status | grep <app>'``).

stop
-----

Остановка платформы или отдельных приложений. Допускается передача
**нескольких** имён приложений в одной команде:
``citeck stop onlyoffice attorneys ecom service-desk``.

.. code-block:: bash

    citeck stop [app...] [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``-s``, ``--shutdown``
      - Также остановить демон
    * - ``-d``, ``--detach``
      - Отправить команду и не ждать завершения

**Примеры:**

.. code-block:: bash

    # Остановка всех приложений (демон продолжает работать)
    citeck stop

    # Остановка с выключением демона
    citeck stop --shutdown

    # Остановка конкретного приложения (detach)
    citeck stop eapps

    # Остановка нескольких приложений сразу (все будут detach)
    citeck stop onlyoffice attorneys ecom service-desk

.. note::

    При остановке **конкретных приложений** (``citeck stop <app> [<app>...]``) каждое переходит в состояние **detached** — не будет автоматически запускаться при ``citeck start``, ``citeck reload`` или перезапуске демона. Реконсилер также не будет пытаться восстановить отключённые приложения.

    Для повторного включения используйте ``citeck start <app>``.

    Это удобно для временного отключения необязательных сервисов (OnlyOffice, AI и др.) с целью экономии памяти.

restart
--------

Перезапуск всех приложений или конкретного приложения. Команда ждёт
возвращения приложения в статус ``RUNNING`` по умолчанию.

.. code-block:: bash

    citeck restart [app] [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``-d``, ``--detach``
      - Не ждать запуска после перезапуска (вернуть управление сразу
        после отправки запроса).
    * - ``--timeout <sec>``
      - Таймаут ожидания в секундах (по умолчанию 300)

**Примеры:**

.. code-block:: bash

    # Перезапуск всех приложений (stop + start, ждёт RUNNING)
    citeck restart

    # Перезапуск одного приложения (ждёт RUNNING)
    citeck restart eapps

    # Перезапуск без ожидания (вернуть управление сразу)
    citeck restart eapps --detach

status
-------

Отображение состояния платформы и приложений.

.. code-block:: bash

    citeck status [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``-w``, ``--watch``
      - Непрерывный мониторинг (обновление по событиям SSE)

**Примеры:**

.. code-block:: bash

    # Статус платформы с таблицей приложений
    citeck status

    # Непрерывный мониторинг (Ctrl+C для выхода)
    citeck status --watch

    # JSON-вывод для скриптов
    citeck status --format json

**Пример вывода** (сокращённый фрагмент на Community-бандле):

.. code-block:: text

    Name:    Citeck
    Status:  RUNNING
    Bundle:  community:2026.1
    URL:     https://203.0.113.45

    APP                STATUS   IMAGE                                       CPU   MEMORY
    Citeck Core
      eapps            RUNNING  nexus.citeck.ru/ecos-apps:2.25.1            0.0%  803M / 1.0G
      emodel           RUNNING  nexus.citeck.ru/ecos-model:2.37.3           0.0%  1005M / 1.3G
      gateway          RUNNING  nexus.citeck.ru/ecos-gateway:3.6.0          0.0%  638M / 1.0G
      proxy            RUNNING  nexus.citeck.ru/ecos-proxy-oidc:2.26.9      0.0%  45M / 128M
      uiserv           RUNNING  nexus.citeck.ru/ecos-uiserv:2.34.3          0.0%  751M / 1.0G
    Citeck Core Extensions
      integrations     RUNNING  nexus.citeck.ru/ecos-integrations:2.32.4    0.0%  874M / 1.0G
    Citeck Additional
      ecom             RUNNING  nexus.citeck.ru/ecos-ecom:1.14.0            0.0%  644M / 1.0G
    Third Party
      keycloak         RUNNING  keycloak/keycloak:26.4.5                    0.0%  581M / 1.0G
      postgres         RUNNING  postgres:17.5                               0.0%  253M / 1.0G
      rabbitmq         RUNNING  rabbitmq:4.1.2-management                   0.0%  130M / 256M

Приложения сгруппированы по категориям из workspace-определения бандла
(``Citeck Core``, ``Citeck Core Extensions``, ``Citeck Additional``,
``Third Party``). Enterprise-бандл включает дополнительные приложения
(``attorneys``, ``service-desk``, ``ecos-project-tracker``, ``ai``,
``edi``, ``ecos-content`` и др.) -- группировка такая же.

logs
-----

Просмотр логов приложений или демона.

.. code-block:: bash

    citeck logs [app] [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``--tail <N>``
      - Количество последних строк (по умолчанию 1000)
    * - ``-f``, ``--follow``
      - Потоковый вывод (следить за новыми записями)
    * - ``--since <time>``
      - Показать логи с указанного момента (RFC3339 или ``1h``, ``30m``)
    * - ``--until <time>``
      - Показать логи до указанного момента
    * - ``-t``, ``--timestamps``
      - Показать временные метки

**Примеры:**

.. code-block:: bash

    # Логи демона (последние 1000 строк)
    citeck logs

    # Логи конкретного приложения
    citeck logs eapps

    # Последние 100 строк
    citeck logs eapps --tail 100

    # Потоковый вывод
    citeck logs -f eapps

    # Логи за последний час
    citeck logs eapps --since 1h

describe
---------

Подробная информация о приложении: образ, порты, тома, переменные окружения.

.. code-block:: bash

    citeck describe <app>

**Пример:**

.. code-block:: bash

    citeck describe eapps

    # Пример вывода:
    # Name           eapps
    # Container ID   a1b2c3d4e5f6
    # Image          registry.citeck.ru/community/ecos-apps:2024.11
    # Status         RUNNING
    # State          running
    # Network        citeck-net
    # Started at     2026-04-10T08:30:00Z
    # Uptime         2d 5h 30m
    # Restarts       0
    #
    # Ports:
    #   8080/tcp -> 0.0.0.0:8080
    #
    # Volumes:
    #   eapps-data:/data
    #
    # Environment:
    #   JAVA_OPTS=-Xmx1024m
    #   SPRING_PROFILES_ACTIVE=server
    #   RABBITMQ_PASSWORD=***

reload
-------

Горячая перезагрузка конфигурации: пересчитывает deployment hash и пересоздаёт только изменённые контейнеры.

.. code-block:: bash

    citeck reload [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``--dry-run``
      - Показать изменения без применения
    * - ``-d``, ``--detach``
      - Применить и не ждать стабилизации сервисов

**Примеры:**

.. code-block:: bash

    # Предварительный просмотр изменений
    citeck reload --dry-run

    # Пример вывода dry-run:
    # Config valid: /opt/citeck/conf/namespace.yml
    # Changes:
    #   ~ webapps.eapps.heapSize = 2048m (was 1024m)
    #   + webapps.uiserv.env.CUSTOM_VAR = value

    # Применить изменения
    citeck reload

.. note::

    Отключённые приложения (ранее остановленные через ``citeck stop <app>``) исключаются из ``reload`` -- они остаются остановленными. Чтобы повторно включить их, используйте ``citeck start <app>``.

update
-------

Обновление определений workspace и бандлов из git-репозиториев.

.. code-block:: bash

    citeck update [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``-f``, ``--file <path>``
      - Путь к ZIP-архиву workspace (оффлайн-импорт)

**Примеры:**

.. code-block:: bash

    # Обновление из git (pull latest)
    citeck update

    # Импорт из файла (оффлайн)
    citeck update -f /tmp/workspace.zip

upgrade
--------

Переключение на другую версию платформы.

.. code-block:: bash

    citeck upgrade [bundle:version] [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``-y``, ``--yes``
      - Пропустить подтверждение. Применить выбранную версию немедленно.

**Аргумент:** при указании ``bundle:version`` (например, ``enterprise:2026.1``) команда пропускает интерактивный выбор и сразу предлагает подтверждение (или применяет без подтверждения при ``--yes``).

Команда выполняет три шага:

1. Обновляет определения бандлов из git (если доступны).
2. Открывает **табличный выбор** со списком доступных версий -- одна вкладка на репозиторий (Community / Enterprise). Текущая версия помечена ``(current)``, последняя -- ``(latest)``.
3. После выбора запрашивает подтверждение и, в случае согласия, применяет новую версию (``namespace.yml`` обновляется и выполняется ``reload``).

**Пример:**

.. code-block:: bash

    citeck upgrade --help

    # Пример вывода:
    # Update workspace repos and upgrade to a different bundle version.
    #
    # Usage:
    #   citeck upgrade                        # interactive picker (TTY required)
    #   citeck upgrade <bundle>:<version>     # non-interactive (e.g., citeck upgrade community:2026.1)
    #
    # Steps:
    #   1. Pull latest workspace/bundle definitions from git (skipped for offline installs)
    #   2. Show available releases with the current version marked (interactive only)
    #   3. Confirm the upgrade (interactive only; skip with --yes/-y)
    #   4. Apply selected version and reload

Интерактивный запуск:

.. code-block:: text

    $ citeck upgrade

    # 1. Обновление workspace из git
    # 2. Табличный выбор версии:
    #    Community Bundles │ Enterprise Bundles
    #    ──────────────────────────────────────
    #    > 2026.1   (latest)  (current)
    #      2025.12
    #      2025.5
    #
    #    ←/→ переключить вкладку   ↑/↓ выбор   Enter подтвердить   Esc отмена
    #
    # 3. Если выбран другой бандл (Enterprise), может быть запрошен
    #    логин/пароль для реестра Docker-образов.
    # 4. Подтверждение: Upgrade community:2026.1 → enterprise:2026.1? [y/N]
    # 5. Применение: namespace.yml обновляется, выполняется reload,
    #    отображается интерактивная таблица статусов.

Неинтерактивный вариант (для скриптов и CI):

.. code-block:: bash

    citeck upgrade enterprise:2026.1 --yes

.. warning::

    **Требования к памяти различаются между бандлами:** Community -- ~14--16 ГБ ОЗУ, Enterprise -- ~24--32 ГБ ОЗУ. Переключение с Community на Enterprise на сервере с 16 ГБ ОЗУ почти наверняка приведёт к OOM. Перед таким обновлением отключите необязательные приложения через ``citeck stop <app>`` (см. :ref:`server_troubleshooting`, раздел "Нехватка памяти") либо увеличьте ОЗУ до рекомендованного объёма.

setup
------

Интерактивный редактор настроек.

.. code-block:: bash

    citeck setup [setting]

Без аргументов открывает меню всех доступных настроек. С аргументом -- сразу переходит к конкретной настройке.

.. note::

    Полный справочник полей YAML, значения по умолчанию и формат данных
    для каждой настройки: :ref:`server_configuration`, раздел «Настройка
    через citeck setup».

**Доступные настройки:**

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Настройка
      - Описание
    * - ``hostname``
      - Имя хоста или IP-адрес платформы
    * - ``tls``
      - Режим TLS. В меню отображается одно из значений:
        «Let's Encrypt», «Self-signed», «Custom certificate» или «HTTP only».
    * - ``port``
      - Порт прокси-сервера
    * - ``email``
      - Настройки SMTP для отправки писем
    * - ``s3``
      - Настройки S3-совместимого хранилища
    * - ``auth``
      - Тип аутентификации (Keycloak / Basic)
    * - ``resources``
      - Ресурсы приложений (heapSize, memoryLimit)
    * - ``language``
      - Язык интерфейса CLI
    * - ``admin-password``
      - Смена пароля администратора

**Подкоманды:**

.. code-block:: bash

    # История изменений конфигурации
    citeck setup history

**Примеры:**

.. code-block:: bash

    # Открыть меню настроек
    citeck setup

    # Сменить пароль администратора
    citeck setup admin-password

    # Изменить hostname
    citeck setup hostname

    # Посмотреть историю изменений
    citeck setup history

    # Пример вывода history:
    # DATE                 SETTING    FILE            DESCRIPTION
    # 2026-04-10 08:30:00  hostname   namespace.yml   replace proxy.host = 203.0.113.45
    # 2026-04-10 08:35:00  tls        namespace.yml   replace proxy.tls.enabled = true

При изменении настройки команда:

1. Показывает diff до и после изменения
2. Предлагает выбор: применить с перезагрузкой, применить без перезагрузки, или отменить
3. Записывает изменения и создаёт запись в истории

setup hostname
~~~~~~~~~~~~~~~

Изменение имени хоста или IP-адреса платформы.

.. code-block:: bash

    citeck setup hostname

.. note::

    Если введённое значение совпадает с уже сконфигурированным hostname,
    команда определяет, что изменений нет: выводит сообщение ``Nothing
    changed``, **не добавляет запись в историю** и **не перевыпускает
    TLS-сертификат**.

setup auth
~~~~~~~~~~~

Переключение режима аутентификации между Keycloak и Basic.

.. code-block:: bash

    citeck setup auth

.. warning::

    Переключение режима аутентификации приводит к **перезапуску всех
    веб-приложений и Keycloak**. На сервере с 16 ГБ RAM ожидайте
    **5--10 минут недоступности платформы**.

    Не переключайте режим аутентификации во время активной работы
    пользователей -- планируйте операцию в технологическое окно.

setup history
~~~~~~~~~~~~~~

Просмотр журнала изменений конфигурации namespace.

.. code-block:: bash

    citeck setup history

**Типы записей (столбец** ``SETTING`` **):**

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Значение
      - Что означает
    * - ``hostname``, ``tls``, ``port``, ``email``, ``s3``, ``auth``,
        ``resources``, ``language``, ``admin-password``
      - Изменения, применённые через соответствующую подкоманду
        ``citeck setup <имя>``.
    * - ``external_change``
      - Настройка была изменена **вне** потока ``setup`` (например,
        прямым редактированием ``namespace.yml`` или автоматической
        нормализацией на стороне демона). Запись добавляется при
        ближайшем сохранении конфигурации.

setup admin-password
~~~~~~~~~~~~~~~~~~~~~

Смена единого пароля администратора для всех сервисов платформы.

.. code-block:: bash

    citeck setup admin-password

Команда запрашивает новый пароль (ввод скрыт) и применяет его к:

- **Keycloak** (realm ``ecos-app``) -- пароль администратора платформы,
  через ``kcadm.sh`` под сервисным аккаунтом ``citeck``
- **Keycloak** (realm ``master``) -- пароль администратора
  административной консоли Keycloak, через ``kcadm.sh`` под тем же
  сервисным аккаунтом
- **RabbitMQ** -- через ``rabbitmqctl change_password``
- **PgAdmin** -- через ``setup.py``

Сервисный аккаунт ``citeck`` (используемый launcher-ом для внутренней
авторизации в Keycloak и RabbitMQ) **НЕ** ротируется этой командой --
его пароль остаётся стабильным, чтобы launcher не потерял доступ к
платформе.

.. warning::

    **Ожидайте 2--5 минут простоя платформы.** Несмотря на то что пароли
    обновляются во время выполнения (без пересоздания контейнеров
    инфраструктуры), веб-приложения перезапускаются для подхвата нового
    ``RABBITMQ_PASSWORD``, что приводит к недоступности HTTP-эндпоинтов
    (платформа возвращает ошибки соединения) на время их повторного запуска.
    На серверах с большим количеством Java-приложений (Enterprise, 24+ apps)
    фактическое время простоя может достигать 5--7 минут.

    Планируйте выполнение команды в технологическое окно.

.. important::

    Команда ``citeck setup admin-password`` меняет пароль администратора
    сразу во всех административных UI платформы: **Keycloak** (realms
    ``ecos-app`` и ``master``), **RabbitMQ** и **PgAdmin**.

    Сервисный аккаунт ``citeck`` (отдельный пользователь Keycloak /
    RabbitMQ, используемый launcher-ом для внутренних вызовов API)
    **не** затрагивается -- его пароль генерируется один раз и остаётся
    стабильным. Поэтому изменение пользовательского пароля администратора
    никогда не приводит к потере launcher-ом доступа к Keycloak или
    RabbitMQ.

    Ротация ``master``-realm выполняется best-effort: если этот шаг
    завершится ошибкой, остальные компоненты уже получат новый пароль,
    и сообщение об ошибке будет записано в журнал демона. Launcher в
    любом случае продолжит работать через сервисный аккаунт.

setup email
~~~~~~~~~~~~

Настройка SMTP-сервера для отправки уведомлений платформой.

.. code-block:: bash

    citeck setup email

Интерактивный поток:

1. **Выбор провайдера.** Сначала команда предлагает выбрать провайдера SMTP -- например, ``Generic SMTP``, ``Gmail``, ``Outlook`` и другие. Для каждого провайдера подставляются подходящие значения по умолчанию (хост, порт, TLS); их можно переопределить на следующем шаге.
2. **Ввод параметров.** Хост, порт, адрес отправителя, имя пользователя и пароль. Пароль сохраняется в зашифрованном хранилище секретов.
3. **Выбор режима применения.** Применить немедленно (с reload), запланировать на следующий reload или сохранить без применения.

.. note::

    **Без аутентификации.** Если SMTP-релей принимает письма без логина/пароля, оставьте поле "username" пустым -- в этом случае SMTP-аутентификация отключается.

.. note::

    **Автоматическое удаление mailhog.** При настройке реального SMTP-сервера встроенный контейнер ``mailhog`` (использовался как dev-заглушка) будет автоматически удалён при следующем ``reload``. Обратное тоже верно: если очистить email-настройки, mailhog снова появится при перегенерации namespace.

.. note::

    Подробнее про поле ``tls`` (``true`` / ``false``) и соответствие портам см. в :ref:`server_configuration`, раздел "email".

setup s3
~~~~~~~~~

Настройка S3-совместимого объектного хранилища (только Enterprise, при наличии приложения ``ecos-content``).

.. code-block:: bash

    citeck setup s3

Интерактивный поток запрашивает ``endpoint``, ``region``, ``bucket``, ``accessKey`` и ``secretKey``. Secret key сохраняется в зашифрованном хранилище секретов.

После ввода параметров CLI предлагает **три варианта применения**:

- **Применить сейчас** -- выполняется ``reload`` сразу, приложение ``ecos-content`` перезапускается с новыми настройками.
- **Применить при следующем reload** -- изменения записываются в ``namespace.yml``, но не применяются немедленно; вступят в силу при ближайшем ``citeck reload``.
- **Только сохранить** -- записать конфигурацию без запланированного применения.

.. note::

   После настройки подключения к S3 войдите в систему и измените настройку
   ``default-content-storage`` на **"Хранилище контента для S3"**. Откройте
   раздел системных настроек:

   .. code-block:: text

      /v2/journals?journalId=ecos-configs&search=default-content-storage&viewMode=table&ws=admin$workspace

   Найдите запись ``default-content-storage`` и установите её значение
   ``content/storage@content-storage-s3``.

health
-------

Проверка здоровья системы.

.. code-block:: bash

    citeck health

**Коды возврата:**

.. list-table::
    :widths: 15 85
    :header-rows: 1

    * - Код
      - Значение
    * - ``0``
      - Система здорова
    * - ``1``
      - Ошибка подключения к демону
    * - ``8``
      - Система нездорова (есть проблемные компоненты)

**Пример:**

.. code-block:: bash

    citeck health

    # Пример вывода:
    # Status: HEALTHY
    #
    #   [OK]     docker        — Docker Engine reachable
    #   [OK]     disk_space    — 45 GB available
    #   [OK]     postgres      — accepting connections
    #   [OK]     keycloak      — realm accessible
    #   [OK]     rabbitmq      — management API responding

    # Использование в скриптах:
    citeck health && echo "OK" || echo "FAILED"

diagnose
---------

Диагностика проблем с возможностью автоматического исправления.

.. code-block:: bash

    citeck diagnose [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``--fix``
      - Автоматически исправить обнаруженные проблемы
    * - ``--dry-run``
      - Показать, что будет исправлено, без внесения изменений

**Проверки:**

- Наличие файла сокета и отклик демона (удаление stale-сокета)
- Доступность Docker Engine
- Достаточность дискового пространства
- Корректность конфигурации namespace.yml
- Состояние контейнеров

.. note::

    Если хотя бы одно приложение находится в состоянии ``FAILED`` или ``START_FAILED``, ``diagnose`` повышает уровень соответствующей проверки до **ERROR** и печатает ссылку на :ref:`server_troubleshooting`. Для каждой проверки, которая завершилась с предупреждением или ошибкой, в выводе отображается строка с рекомендацией (``→ see docs: …``).

**Пример:**

.. code-block:: bash

    citeck diagnose --fix

.. _cmd_dump_system_info:

dump-system-info
-----------------

Собирает полную диагностику (статус, логи, системную информацию,
``docker inspect``) в ZIP-архив ``./citeck-dump-<timestamp>.zip`` в
текущей директории. Предназначено для отправки в поддержку.

.. code-block:: bash

    citeck dump-system-info [flags]

**Флаги:**

.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``--full``
      - Включить полные логи контейнеров без обрезки (по умолчанию: head 1000 + tail 2000 строк).

Подробное описание содержимого архива и инструкции по отправке —
в :ref:`server_support_dump` (раздел «Обращение в поддержку» в
:ref:`server_troubleshooting`).

clean
------

Очистка осиротевших ресурсов Docker.

.. code-block:: bash

    citeck clean [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``--force``
      - Выполнить удаление (по умолчанию -- только показать)
    * - ``--volumes``
      - Также сканировать и удалять осиротевшие директории томов
    * - ``--images``
      - Удалить неиспользуемые (dangling) Docker-образы

**Примеры:**

.. code-block:: bash

    # Сухой запуск: показать, что будет удалено
    citeck clean

    # Выполнить очистку
    citeck clean --force

    # Полная очистка с удалением образов и томов
    citeck clean --force --volumes --images

snapshot
---------

Управление снимками (backup/restore) данных namespace.

.. code-block:: bash

    citeck snapshot <subcommand>

**Подкоманды:**

.. list-table::
    :widths: 20 80
    :header-rows: 1

    * - Подкоманда
      - Описание
    * - ``list``
      - Показать доступные снимки
    * - ``export``
      - Экспортировать данные в ZIP-архив
    * - ``import``
      - Импортировать данные из архива
    * - ``delete``
      - Удалить снимок по имени

**Флаги** ``snapshot import`` **:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``-d``, ``--detach``
      - Не ждать перехода namespace в состояние ``RUNNING`` после импорта. По умолчанию команда ждёт готовности платформы.

**Примеры:**

.. code-block:: bash

    # Список снимков
    citeck snapshot list

    # Экспорт текущих данных
    citeck snapshot export

    # Экспорт в указанную директорию
    citeck snapshot export --dir /backup/

    # Импорт из снимка (имя из списка, с или без .zip)
    citeck snapshot import citeck_2026-04-10_08-30-00

    # Импорт без ожидания готовности платформы
    citeck snapshot import citeck_2026-04-10_08-30-00 --detach

.. note::

    При импорте снимка команда сначала проверяет существование файла, и только затем останавливает namespace. Если снимок не найден, namespace не будет остановлен.

    После импорта namespace автоматически перезапускается.

**Расположение снимков**

По умолчанию снимки сохраняются в каталоге данных namespace: ``/opt/citeck/data/runtime/<namespace-id>/snapshots/``. В команде ``citeck snapshot import`` можно указать как имя файла из этого каталога (с суффиксом ``.zip`` или без), так и абсолютный путь к ZIP-архиву в другом месте. Каталог можно изменить на время экспорта через флаг ``--dir``.

.. warning::

    Импорт снимка запускает последовательность: остановка namespace → восстановление томов → повторный запуск. На сервере с 16 ГБ ОЗУ полный цикл занимает около **10 минут простоя** (до 15 минут на Enterprise). Планируйте импорт в технологическое окно.

.. note::

    Импорт можно запускать **на работающей платформе** -- лончер сам остановит namespace перед восстановлением данных и запустит его снова после завершения импорта. Дополнительно вручную останавливать namespace не нужно.

uninstall
----------

Полное удаление Citeck Launcher.

.. code-block:: bash

    citeck uninstall [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``--delete-data``
      - Удалить все данные без запроса (для автоматизации). Предполагает согласие с удалением данных и пропускает типовое подтверждение фразой.
    * - ``--yes``
      - Пропустить запрос подтверждения (подходит для автоматизации).

Команда выполняет:

1. Остановку всех приложений и демона
2. Удаление systemd-сервиса
3. (Опционально) удаление всех данных из ``/opt/citeck``
4. Удаление бинарного файла ``/usr/local/bin/citeck``

**Примеры:**

.. code-block:: bash

    # Интерактивное удаление
    citeck uninstall

    # Полное удаление для автоматизации (без запросов)
    citeck uninstall --delete-data --yes

.. warning::

    При вводе фразы ``drop all data`` на этапе подтверждения все данные платформы будут безвозвратно удалены, включая базы данных и файлы конфигурации.

.. note::

    **Взаимодействие** ``--delete-data`` **и подтверждения.** Флаг ``--delete-data`` неявно включает согласие на удаление данных и пропускает типовое подтверждение фразой ``drop all data`` -- то есть работает как ``--yes`` для этого шага. Чтобы сохранить безопасный интерактивный сценарий с ручным подтверждением, запускайте ``citeck uninstall`` без ``--delete-data`` и принимайте решение об удалении данных в диалоге.

version
--------

Информация о версии.

.. code-block:: bash

    citeck version [flags]

**Флаги:**

.. list-table::
    :widths: 30 70
    :header-rows: 1

    * - Флаг
      - Описание
    * - ``--short``
      - Вывести только номер версии

**Пример:**

.. code-block:: bash

    citeck version

    # Пример вывода:
    # Citeck CLI 2.1.0
    # Commit: 38ee6d0
    # Built:  2026-04-10T12:00:00Z
    # OS:     linux/amd64
    # Go:     go1.24.2

exec
-----

Выполнение команды внутри контейнера приложения.

.. code-block:: bash

    citeck exec <app> -- <command>

**Пример:**

.. code-block:: bash

    citeck exec postgres -- psql -U postgres -c "SELECT version();"

config
-------

Управление конфигурацией namespace.

.. code-block:: bash

    citeck config [command]

**Доступные подкоманды:**

.. list-table::
    :widths: 25 75
    :header-rows: 1

    * - Подкоманда
      - Описание
    * - ``view``
      - Выводит содержимое ``namespace.yml`` из запущенного демона
    * - ``validate``
      - Проверяет корректность конфигурации namespace

.. note::

    Вызов ``citeck config`` без подкоманды выводит справку по команде,
    а не содержимое ``namespace.yml``. Для просмотра YAML используйте
    ``citeck config view``.

**Примеры:**

.. code-block:: bash

    # Показать текущий namespace.yml
    citeck config view

    # Проверить корректность конфигурации
    citeck config validate

completion
-----------

Генерация скрипта автодополнения для shell.

.. code-block:: bash

    citeck completion <shell>

**Поддерживаемые оболочки:** ``bash``, ``zsh``, ``fish``, ``powershell``

**Пример:**

.. code-block:: bash

    # Активация автодополнения для bash
    source <(citeck completion bash)

    # Постоянная установка
    citeck completion bash > /etc/bash_completion.d/citeck
