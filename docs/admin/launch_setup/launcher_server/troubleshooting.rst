.. _server_troubleshooting:

Решение проблем
================

.. contents::
    :local:
    :depth: 1

Диагностические команды
-------------------------

Перед началом диагностики выполните базовый набор проверок:

.. code-block:: bash

    # Общее состояние системы
    citeck health

    # Статус всех приложений
    citeck status -a

    # Логи конкретного приложения
    citeck logs <app>

    # Логи демона
    citeck logs

    # Логи демона через journald
    journalctl -u citeck -f

    # Состояние контейнеров Docker
    docker ps -a --filter label=citeck.launcher=true

    # Автоматическая диагностика с исправлением
    citeck diagnose --fix

.. note::

    **Метки Docker, используемые лончером.** Все контейнеры, создаваемые
    ``citeck``, помечаются набором меток для фильтрации и трассировки:

    - ``citeck.launcher=true`` -- признак того, что контейнер управляется
      лончером (используется для ``--filter``)
    - ``citeck.launcher.workspace`` -- идентификатор workspace
    - ``citeck.launcher.namespace`` -- идентификатор namespace
    - ``citeck.launcher.app.name`` -- логическое имя приложения
    - ``citeck.launcher.app.hash`` -- deployment hash (используется
      reload-ом для определения изменений)
    - ``citeck.launcher.original-name`` -- исходное имя до нормализации

Приложение зависло в статусе STARTING
---------------------------------------

**Симптомы:** приложение долго находится в состоянии ``STARTING`` и не переходит в ``RUNNING``.

**Причины и решения:**

1. **Недостаточно памяти.** Проверьте доступную память:

   .. code-block:: bash

       free -h
       citeck describe <app>  # посмотрите memoryLimit

   Увеличьте heapSize через ``citeck setup resources`` или добавьте оперативную память.

2. **Зависимость не готова.** Приложение может ждать другой сервис:

   .. code-block:: bash

       citeck status -a  # проверьте статус зависимостей
       citeck logs <dependency-app>

3. **Ошибка в конфигурации.** Проверьте логи приложения:

   .. code-block:: bash

       citeck logs <app> --tail 200

4. **Перезапуск приложения:**

   .. code-block:: bash

       citeck restart <app>

Keycloak не запускается
------------------------

**Симптомы:** Keycloak в статусе ``START_FAILED`` или ``STARTING``.

**Причины:**

1. **PostgreSQL недоступен.** Keycloak зависит от базы данных:

   .. code-block:: bash

       citeck status -a | grep postgres
       citeck logs postgres --tail 50

2. **Нехватка памяти.** Keycloak требует значительный объём памяти:

   .. code-block:: bash

       citeck describe keycloak  # проверьте heapSize
       citeck setup resources    # увеличьте heapSize для keycloak

3. **Повреждённая база данных.** Если Keycloak сообщает об ошибках миграции:

   .. code-block:: bash

       citeck logs keycloak --tail 500 | grep -i "migration\|liquibase"

Проблемы с TLS-сертификатами
------------------------------

**Самоподписанный сертификат -- предупреждение в браузере**

Это ожидаемое поведение. Добавьте исключение в браузере для продолжения работы.

**Let's Encrypt не может получить сертификат**

1. Проверьте, что порты 80 и 443 доступны из интернета:

   .. code-block:: bash

       curl -v http://<your-host>

2. Проверьте DNS-записи (если используется доменное имя):

   .. code-block:: bash

       dig <your-domain>

3. Переключитесь на другой режим TLS:

   .. code-block:: bash

       citeck setup tls
       # Выберите "Self-signed HTTPS" или "Auto HTTPS"

**Сертификат истёк**

Let's Encrypt-сертификаты обновляются автоматически. Если обновление не произошло:

.. code-block:: bash

    # Перезапуск демона обычно решает проблему
    systemctl restart citeck

Забытый пароль администратора
-------------------------------

Пароль администратора можно сменить в любой момент:

.. code-block:: bash

    citeck setup admin-password

Команда применяет новый пароль ко всем компонентам (Keycloak, RabbitMQ, PgAdmin) без перезапуска контейнеров.

Демон не отвечает
------------------

**Симптомы:** команды ``citeck status``, ``citeck start`` не работают.

1. **Проверьте systemd-сервис:**

   .. code-block:: bash

       systemctl status citeck

2. **Проверьте наличие сокета:**

   .. code-block:: bash

       ls -la /run/citeck/daemon.sock

3. **Stale-сокет (сокет есть, но демон не работает):**

   .. code-block:: bash

       # Автоматическое исправление
       citeck diagnose --fix

       # Или вручную
       rm /run/citeck/daemon.sock
       citeck start

   .. note::

       ``citeck diagnose --fix`` только удаляет stale-сокет, но **не
       перезапускает демон**. После автоисправления обязательно запустите
       демон заново -- ``systemctl start citeck`` (если установлен
       systemd-сервис) или ``citeck start -d`` (если запуск не через
       systemd).

4. **Логи демона:**

   .. code-block:: bash

       journalctl -u citeck --no-pager -n 100
       # или
       cat /opt/citeck/log/daemon.log

5. **Перезапуск через systemd:**

   .. code-block:: bash

       systemctl restart citeck

.. tip::

    **Когда установлен systemd-сервис, предпочитайте** ``systemctl start citeck`` **над** ``citeck start -d``. Первый вариант запускает демон как systemd-unit и пишет лог в journald, что упрощает отладку и обеспечивает корректный автозапуск. ``citeck start -d`` остаётся полезным, когда systemd недоступен (например, в контейнерах) или нужен ручной запуск вне service manager.

.. note::

    **Расположение логов демона:**

    - Файл: ``/opt/citeck/log/daemon.log`` (с автоматической ротацией)
    - systemd/journald: ``journalctl -u citeck -f``

Автовосстановление реконсилером
--------------------------------

Демон запускает реконсилер, который непрерывно следит за состоянием контейнеров и автоматически восстанавливает упавшие приложения:

- Отсутствующие контейнеры пересоздаются.
- Неуспешные liveness-проверки (3 промаха подряд) приводят к перезапуску контейнера.
- Для повторных попыток запуска используется экспоненциальный backoff: от 1 минуты до 30 минут максимум.

Перед тем как вручную перезапускать проблемное приложение, **подождите 1--2 минуты** и проверьте ``citeck status -a`` -- реконсилер может самостоятельно вернуть сервис в строй. Ручной ``citeck restart <app>`` имеет смысл, если приложение не восстанавливается автоматически (например, проблема в конфигурации, а не в транзиентном сбое).

Отключённые через ``citeck stop <app>`` приложения реконсилер **не трогает** -- они сохраняют статус ``STOPPED`` до ручного ``citeck start <app>``.

Нехватка дискового пространства
---------------------------------

**Симптомы:** ошибки ``no space left on device``, приложения не могут запуститься.

1. **Проверьте дисковое пространство:**

   .. code-block:: bash

       df -h /opt/citeck
       du -sh /opt/citeck/*

2. **Очистите неиспользуемые Docker-ресурсы:**

   .. code-block:: bash

       # Показать, что будет удалено
       citeck clean --volumes --images

       # Выполнить очистку
       citeck clean --force --volumes --images

3. **Обрежьте логи конкретного контейнера** (сохраняя файл, но обнуляя
   его содержимое):

   .. code-block:: bash

       # Найти путь к лог-файлу контейнера и обнулить его:
       docker inspect --format='{{.LogPath}}' <container-name> | xargs sudo truncate -s 0

   Либо настройте автоматическую ротацию логов глобально -- в
   ``/etc/docker/daemon.json`` задайте лимиты драйвера логирования:

   .. code-block:: json

       {
         "log-driver": "json-file",
         "log-opts": {
           "max-size": "50m",
           "max-file": "3"
         }
       }

   После изменения файла: ``systemctl restart docker``. Настройки применяются
   к **новым** контейнерам, существующие надо пересоздать (через
   ``citeck reload`` -- hash не изменится, но если вы хотите форсировать
   пересоздание, можно сделать ``citeck restart <app>``).

   .. warning::

       Не используйте ``docker system prune -f`` на сервере с работающим
       Citeck: команда удалит **все** неиспользуемые контейнеры, сети и
       dangling-образы, что может затронуть инфраструктуру за пределами
       лончера. Для безопасной очистки используйте
       ``citeck clean --force --volumes --images`` -- она удаляет только
       осиротевшие ресурсы лончера.

4. **Ротация логов демона** происходит автоматически. Проверьте размер:

   .. code-block:: bash

       ls -lh /opt/citeck/log/

Конфликт портов
-----------------

**Симптомы:** демон или прокси не могут запуститься, ошибка ``bind: address already in use``.

1. **Проверьте, что использует порты:**

   .. code-block:: bash

       ss -tlnp | grep -E ':80|:443'

2. **Остановите конфликтующий сервис:**

   .. code-block:: bash

       # Например, если nginx занимает порт
       systemctl stop nginx
       systemctl disable nginx

   **Если порт занят Docker-контейнером** (например, случайно оставшийся
   ``nginx``, ``apache``, ``traefik`` в контейнере), найдите и удалите его:

   .. code-block:: bash

       docker ps                   # найдите контейнер с нужным портом
       docker rm -f <container>    # остановит и удалит контейнер

3. **Или измените порт платформы:**

   .. code-block:: bash

       citeck setup port

Восстановление после сбоя демона
-----------------------------------

Systemd автоматически перезапускает демон при сбое (``Restart=on-failure``). Контейнеры Docker продолжают работать независимо от демона.

После перезапуска новый экземпляр демона подхватывает работающие контейнеры через сравнение deployment hash -- данные и состояние приложений не теряются.

Если автоматический перезапуск не помог:

.. code-block:: bash

    # Проверить логи
    journalctl -u citeck --no-pager -n 200

    # Ручной перезапуск
    systemctl restart citeck

    # Проверить, что контейнеры всё ещё работают
    docker ps --filter label=citeck.launcher=true

Откат неудачного обновления
-----------------------------

Если после обновления бинарного файла платформа работает некорректно:

.. code-block:: bash

    citeck install --rollback

Эта команда:

1. Восстанавливает предыдущую версию бинарного файла из ``/usr/local/bin/citeck.bak``
2. Перезапускает демон

Контейнеры Docker не затрагиваются -- они продолжают работать с прежними образами.

Проверка здоровья в скриптах мониторинга
-----------------------------------------

Для интеграции с системами мониторинга (Zabbix, Nagios, Prometheus) используйте:

.. code-block:: bash

    # Простая проверка (exit code: 0=OK, 8=unhealthy)
    citeck health
    echo $?

    # JSON-вывод для парсинга
    citeck health --format json

    # Проверка конкретного приложения
    citeck status --format json | jq '.apps[] | select(.name=="ecos-apps") | .status'

Приложение в статусе PULL_FAILED
----------------------------------

**Симптомы:** Docker-образ не может быть загружен.

1. **Проверьте подключение к интернету:**

   .. code-block:: bash

       curl -v https://registry.citeck.ru/v2/

2. **Проверьте учётные данные реестра (для Enterprise):**

   .. code-block:: bash

       docker login registry.citeck.ru

3. **Повторите загрузку:**

   .. code-block:: bash

       citeck restart <app>

4. **При оффлайн-установке** убедитесь, что все образы загружены:

   .. code-block:: bash

       docker images | grep citeck

.. _server_support_dump:

Обращение в поддержку
-----------------------

Для сбора полной диагностики одной командой запустите:

.. code-block:: bash

   citeck dump-system-info

Команда создаст архив ``citeck-dump-<timestamp>.zip`` в текущей директории. В архиве:

- Информация о системе (uname, OS, памяти, диске)
- Версия ``citeck`` и статус платформы (``status``, ``health``, ``diagnose``)
- Конфигурация: ``namespace.yml``, ``daemon.yml``, история ``setup``
- Логи демона (последние 5000 строк) + journalctl
- Docker: ``ps -a``, ``inspect`` каждого citeck-контейнера, логи контейнеров (head 1000 + tail 2000 строк)
- Любые ошибки выполнения отдельных шагов -- в ``errors.json``

Отправьте полученный ZIP-архив в `службу поддержки <https://citeck.ru/support>`_ или приложите к issue в `GitHub-репозитории <https://github.com/Citeck/citeck-launcher/issues>`_ (обычно < 5 MB).

.. note::

   Опция ``--full`` включает полные логи контейнеров без обрезки. Используйте
   только если команда поддержки попросила (архив может стать существенно больше).

Если ``dump-system-info`` недоступен (старая версия лончера или команда не работает), соберите диагностику вручную:

.. code-block:: bash

    # Версия лончера
    citeck version

    # Состояние системы
    citeck health --format json > health.json

    # Статус приложений
    citeck status --format json > status.json

    # Логи демона
    citeck logs --tail 5000 > daemon.log

    # Логи проблемного приложения
    citeck logs <app> --tail 5000 > app.log

    # Информация о системе
    uname -a > system.txt
    docker version >> system.txt
    free -h >> system.txt
    df -h >> system.txt

Отправьте собранные файлы в `службу поддержки <https://citeck.ru/support>`_ или создайте issue в `GitHub-репозитории <https://github.com/Citeck/citeck-launcher/issues>`_.

Нехватка памяти (Enterprise)
------------------------------

Enterprise-бандл включает более 20 Java-приложений и требует **24–32 ГБ** ОЗУ. На сервере с 16 ГБ платформа может работать нестабильно: OOM Killer завершает приложения, сервер становится недоступным.

**Решения:**

1. **Отключите необязательные приложения** для экономии памяти:

   .. code-block:: bash

       # Отключить приложения, которые не нужны (освобождает 4–5 ГБ)
       citeck stop onlyoffice
       citeck stop attorneys
       citeck stop ai
       citeck stop edi

   Отключённые приложения не будут запускаться при перезагрузке. Для повторного включения: ``citeck start <app>``.

2. **Увеличьте RAM** сервера до 24–32 ГБ (рекомендуется для Enterprise).

3. **Уменьшите heap** отдельных приложений:

   .. code-block:: bash

       citeck setup resources
