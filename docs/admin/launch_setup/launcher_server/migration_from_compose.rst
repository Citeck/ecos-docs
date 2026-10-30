.. _migration_from_compose:

Миграция данных с docker-compose
================================

Инструкция по переносу данных со старого сервера, развёрнутого из репозитория `citeck-community <https://github.com/Citeck/citeck-community>`_ (``docker-compose``), на новый сервер, развёрнутый через :ref:`Citeck Launcher <launcher_server>` v2 в серверном режиме.

Рассчитана на администратора с ``root``-доступом к обоим серверам. Все шаги выполняются вручную, отдельными командами в терминале.

.. warning::

    Если установка кастомизирована, команды и логины/пароли нужно будет подкорректировать под Ваше окружение.

Соглашения
----------

- На **source** команды используют синтаксис ``docker compose`` (Compose v2, plugin). Если у вас установлен legacy ``docker-compose`` (v1) -- заменяйте ``docker compose`` на ``docker-compose`` в каждой команде.
- Команды этапа 2 (выгрузка) и предусловий **выполняются из каталога** ``citeck-community`` (там, где лежит ``docker-compose.yaml``), иначе compose не найдёт сервисы.
- На **target** launcher2 управляет контейнерами напрямую через Docker SDK (без compose) -- там используется ``docker exec`` с реальными именами контейнеров (``citeck_postgres_default``, ``citeck_mongo_default``, ``citeck_zookeeper_default``).

Что мигрируется и что нет
-------------------------

**Мигрируется:**

- PostgreSQL -- пользовательские БД (схема + данные), точечно по mapping-таблице.
- MongoDB -- одна БД ``ecos-process`` → ``citeck_eproc``.
- Zookeeper -- содержимое каталога ``version-2/`` (snapshots + transaction log).

**НЕ мигрируется** (то есть **выходит за рамки этой инструкции** -- технически данные ниже тоже можно перенести, если у кого-то такая задача возникнет, но пошаговую процедуру для них мы здесь не описываем):

- БД ``keycloak`` -- на target создаётся самим launcher2. На source соответствующая БД называется ``ecos_identity`` (сервис ``ecos-identity-app`` в community -- это Keycloak старой версии).
- Пользователи, роли, клиенты Keycloak источника (включая demo-аккаунт ``admin/admin``). Если они заводились вручную -- пересоздать после миграции. Admin на target использует пароль, сгенерированный launcher'ом при первом старте (показывается в визарде один раз; перевыпустить через ``citeck setup admin-password``).
- RabbitMQ -- очереди и in-flight сообщения.
- Volumes proxy/nginx -- логи, кеш сертификатов Let's Encrypt.
- Секреты (JWT, OIDC client secret, admin password) -- launcher2 генерирует свои при первой установке.

Матрица совместимости
---------------------

.. list-table::
    :widths: 20 25 25 30
    :header-rows: 1

    * - Компонент
      - Source
      - Target
      - Тип миграции
    * - PostgreSQL
      - 12.7
      - 17.5
      - логический dump (``pg_dump -F c``)
    * - MongoDB
      - 4.0
      - 4.0.2
      - ``mongodump --archive``
    * - Zookeeper
      - 3.8.2 (Bitnami)
      - 3.9.4 (official)
      - копия ``version-2/`` из dataDir
    * - RabbitMQ
      - --
      - --
      - пропускаем
    * - Keycloak БД
      - --
      - --
      - пропускаем

PostgreSQL переезжает с мажорным скачком версии (12 → 17). Физическое копирование data-каталога (volume) не сработает -- нужен только логический dump.

Mapping БД и пользователей
--------------------------

В launcher2 действует соглашение: ``имя_БД == имя_пользователя == пароль``. На target пароли пользовательских БД совпадают с именами этих БД.

PostgreSQL
~~~~~~~~~~

.. list-table::
    :widths: 25 20 25 30
    :header-rows: 1

    * - Source DB
      - Source owner
      - Target DB
      - Target owner
    * - ``ecos_apps``
      - ``apps``
      - ``citeck_eapps``
      - ``citeck_eapps``
    * - ``ecos_uiserv``
      - ``uiserv``
      - ``citeck_uiserv``
      - ``citeck_uiserv``
    * - ``ecos_integrations``
      - ``integrations``
      - ``citeck_integrations``
      - ``citeck_integrations``
    * - ``ecos_model``
      - ``model``
      - ``citeck_emodel``
      - ``citeck_emodel``
    * - ``ecos_notifications``
      - ``notifications``
      - ``citeck_notifications``
      - ``citeck_notifications``
    * - ``ecos_history``
      - ``history``
      - ``citeck_history``
      - ``citeck_history``
    * - ``ecos_process``
      - ``process``
      - ``citeck_eproc``
      - ``citeck_eproc``
    * - ``ecos_camunda``
      - ``camunda``
      - ``citeck_camunda``
      - ``citeck_camunda``
    * - ``ecos_edi``
      - ``edi``
      - ``citeck_edi``
      - ``citeck_edi``

**Не мигрируются (на source игнорируем):**

- ``ecos_gateway`` -- в launcher2 у gateway нет своей БД.
- ``ecos_identity`` -- это БД сервиса ``ecos-identity-app``, который в community-сетапе является Keycloak (просто более старой версии). Соответствует решению «БД ``keycloak`` не мигрируем» -- пользователи и роли источника при миграции теряются (см. «НЕ мигрируется» во вступлении).
- ``keycloak`` -- на target создаёт сам launcher2.

MongoDB
~~~~~~~

.. list-table::
    :widths: 50 50
    :header-rows: 1

    * - Source DB
      - Target DB
    * - ``ecos-process``
      - ``citeck_eproc``

Zookeeper
~~~~~~~~~

.. list-table::
    :widths: 40 60
    :header-rows: 1

    * - Source путь (хост)
      - Target путь (хост)
    * - ``services/ecos-community-demo-data/zookeeper-app/data/version-2/``
      - ``/opt/citeck/data/runtime/default/volumes/zookeeper2/data/version-2/`` (snapshots) + ``/opt/citeck/data/runtime/default/volumes/zookeeper2/datalog/version-2/`` (logs)

Особенности:

- **Source (Bitnami)** хранит и снэпшоты, и transaction log в одном каталоге ``version-2/``.
- **Target (official zookeeper)** разделяет: ``data/version-2/`` для снэпшотов и служебных файлов (``acceptedEpoch``, ``currentEpoch``), ``datalog/version-2/`` для transaction log. Если их не разделить, target падает с ``SnapDirContentCheckException``.
- Хранилище в launcher2 -- это bind-mount каталог на хосте (не named docker volume). Точный путь можно подтвердить через ``docker inspect citeck_zookeeper_default --format '{{(index .Mounts 0).Source}}'``.

Предусловия
-----------

0. Резервный backup source ДО любых действий
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Это страховка на случай, если апгрейд до 2026.1 (предусловие 1) сломает старый сервер. **Backup НЕ используется для миграции** -- только для отката source.

Простейший вариант (с остановкой сервера):

.. code-block:: bash

    docker compose stop
    tar -czf citeck-community-backup-$(date +%F).tar.gz \
      services/ecos-community-demo-data/ \
      services/backups/
    docker compose start

Если останавливать сервер нельзя -- ``pg_dumpall`` + ``mongodump`` + копия каталога zookeeper в горячем режиме на работающих контейнерах.

1. Source обновлён до релиза 2026.1
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Это снимает риск рассинхронизации schema/changelog при заливке в launcher2 (тоже 2026.1). В каталоге ``citeck-community``:

.. code-block:: bash

    git pull
    docker compose up -d

Дождаться, пока все микросервисы дойдут до ``RUNNING`` / ``healthy`` -- Liquibase должен догнать changelog. Проверить можно так:

.. code-block:: bash

    docker compose ps

2. Target подготовлен
~~~~~~~~~~~~~~~~~~~~~

Установлен ``citeck-launcher`` версии ≥ 2.x, bundle ``community:2026.1`` или ``enterprise:2026.1`` (в зависимости от лицензии). Подробности первого запуска -- в этапе 1.

3. Свободное место
~~~~~~~~~~~~~~~~~~

- На source: ≥ объём данных × 1.5 (для дампов).
- На target: то же.

4. Доступ к docker
~~~~~~~~~~~~~~~~~~

``docker ps`` без sudo либо через sudo на обоих серверах.

Этап 1. Подготовка target (launcher2)
-------------------------------------

Цель этапа: получить запущенный один раз namespace, чтобы launcher создал инфраструктуру (контейнеры + docker volumes), завёл пустые БД с пользователями и сгенерировал секреты.

1.1. Установить launcher
~~~~~~~~~~~~~~~~~~~~~~~~

Если ещё не установлен:

.. code-block:: bash

    curl -fsSL https://github.com/Citeck/citeck-launcher/releases/latest/download/install.sh | bash

В TUI-визарде выбрать bundle ``community:2026.1`` или ``enterprise:2026.1`` (под лицензию). **Записать сгенерированный admin-пароль** -- он показывается один раз. Если пароль потерян -- после миграции его можно перевыпустить через ``citeck setup admin-password``.

1.2. Дождаться полного запуска
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    citeck status -w

Все приложения должны быть в статусе ``RUNNING``. На сервере с 16 GB RAM это занимает 5--15 минут (для enterprise -- дольше). Этот шаг критичен: если webapp'ы не успеют отработать Liquibase на пустых БД, на этапе 4 импорт пойдёт в БД с неполной схемой.

1.3. Остановить все webapp'ы, оставив инфраструктуру
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Состав webapp в ``community`` и ``enterprise`` отличается, единого списка не приводим.

1. Посмотреть текущий список:

   .. code-block:: bash

       citeck status

2. Остановить всё, что **не** относится к инфраструктуре. Инфраструктурные контейнеры, которые остаются запущенными для импорта: ``postgres`` и ``mongo`` (zookeeper тоже инфраструктура, но его остановим непосредственно перед заливкой данных в шаге 4.3).

   Перечислить остальные приложения списком (``gateway``, ``eapps``, ``emodel``, ``uiserv``, ``history``, ``notifications``, ``integrations``, ``eproc``, ``transformations``, ``proxy``, и так далее -- что вернёт ``citeck status``):

   .. code-block:: bash

       citeck stop <app1> <app2> <app3> ...

   Команда ``citeck stop <app>`` помечает приложение как detached: после очередного ``citeck start`` без аргументов оно автоматически не поднимется. Это нужно, чтобы пока идёт restore, никакой webapp не писал в БД.

1.4. Учётные данные для импорта
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Искать вручную не нужно:

- PostgreSQL: ``postgres / postgres`` (захардкожено в launcher2).
- MongoDB: пароль root сгенерирован launcher'ом, читается через ``docker exec citeck_mongo_default printenv MONGO_INITDB_ROOT_PASSWORD``. Команды импорта в этапе 4 берут его именно так.

Этап 2. Выгрузка с source
-------------------------

Все команды этого этапа выполняются на старом сервере, **из каталога** ``citeck-community``. Используются service-имена из ``docker-compose.yaml``:

- PostgreSQL -- ``ecos-microservices-postgresql-app``
- MongoDB -- ``mongodb-app``
- Zookeeper -- ``zookeeper-app``

Подход: запускаем ``pg_dump`` / ``mongodump`` через ``docker compose exec -T``, перенаправляем stdout прямо в файл на хосте. Никаких промежуточных ``docker cp`` и временных файлов внутри контейнера.

Рабочий каталог для дампов в инструкции -- ``~/citeck-migration/``. Создаём подкаталоги заранее:

.. code-block:: bash

    mkdir -p \
      ~/citeck-migration/postgres \
      ~/citeck-migration/mongo \
      ~/citeck-migration/zookeeper

2.1. PostgreSQL
~~~~~~~~~~~~~~~

Параметры ``pg_dump``:

- ``-F c`` -- формат custom (компактный, поддерживает параллельный restore).
- ``--no-owner --no-acl`` -- выкидываем ``OWNER TO`` / ``GRANT`` (на target пользователи называются иначе, ownership проставит ``pg_restore --role``).
- ``--clean --if-exists`` НЕ используем -- целевую БД чистим отдельно командой ``DROP SCHEMA``.
- Без ``-f /tmp/...`` -- ``pg_dump`` пишет в stdout, мы перенаправляем ``>`` в файл на хосте.

.. note::

    **Если какая-то из БД отсутствует на вашем source** (например, в community-only deployment нет ``ecos_edi``) -- ``pg_dump`` упадёт с ``database "<name>" does not exist``. Просто пропустите соответствующий блок: соответствующая target-БД на launcher2 либо отсутствует, либо останется пустой и Liquibase webapp'а наполнит её при первом старте.

Команды для каждой БД из mapping-таблицы (выполнять блоками, по одному):

**ecos_apps:**

.. code-block:: bash

    docker compose exec -T \
      -e PGPASSWORD=postgresstorngpassword \
      ecos-microservices-postgresql-app \
      pg_dump -U postgres -F c --no-owner --no-acl ecos_apps \
      > ~/citeck-migration/postgres/ecos_apps.dump

**ecos_uiserv:**

.. code-block:: bash

    docker compose exec -T \
      -e PGPASSWORD=postgresstorngpassword \
      ecos-microservices-postgresql-app \
      pg_dump -U postgres -F c --no-owner --no-acl ecos_uiserv \
      > ~/citeck-migration/postgres/ecos_uiserv.dump

**ecos_integrations:**

.. code-block:: bash

    docker compose exec -T \
      -e PGPASSWORD=postgresstorngpassword \
      ecos-microservices-postgresql-app \
      pg_dump -U postgres -F c --no-owner --no-acl ecos_integrations \
      > ~/citeck-migration/postgres/ecos_integrations.dump

**ecos_model:**

.. code-block:: bash

    docker compose exec -T \
      -e PGPASSWORD=postgresstorngpassword \
      ecos-microservices-postgresql-app \
      pg_dump -U postgres -F c --no-owner --no-acl ecos_model \
      > ~/citeck-migration/postgres/ecos_model.dump

**ecos_notifications:**

.. code-block:: bash

    docker compose exec -T \
      -e PGPASSWORD=postgresstorngpassword \
      ecos-microservices-postgresql-app \
      pg_dump -U postgres -F c --no-owner --no-acl ecos_notifications \
      > ~/citeck-migration/postgres/ecos_notifications.dump

**ecos_history:**

.. code-block:: bash

    docker compose exec -T \
      -e PGPASSWORD=postgresstorngpassword \
      ecos-microservices-postgresql-app \
      pg_dump -U postgres -F c --no-owner --no-acl ecos_history \
      > ~/citeck-migration/postgres/ecos_history.dump

**ecos_process:**

.. code-block:: bash

    docker compose exec -T \
      -e PGPASSWORD=postgresstorngpassword \
      ecos-microservices-postgresql-app \
      pg_dump -U postgres -F c --no-owner --no-acl ecos_process \
      > ~/citeck-migration/postgres/ecos_process.dump

**ecos_camunda:**

.. code-block:: bash

    docker compose exec -T \
      -e PGPASSWORD=postgresstorngpassword \
      ecos-microservices-postgresql-app \
      pg_dump -U postgres -F c --no-owner --no-acl ecos_camunda \
      > ~/citeck-migration/postgres/ecos_camunda.dump

**ecos_edi:**

.. code-block:: bash

    docker compose exec -T \
      -e PGPASSWORD=postgresstorngpassword \
      ecos-microservices-postgresql-app \
      pg_dump -U postgres -F c --no-owner --no-acl ecos_edi \
      > ~/citeck-migration/postgres/ecos_edi.dump

После выполнения в ``~/citeck-migration/postgres/`` должно быть **9 файлов**:

.. code-block:: bash

    ls ~/citeck-migration/postgres/
    # ecos_apps.dump  ecos_camunda.dump  ecos_edi.dump  ecos_history.dump
    # ecos_integrations.dump  ecos_model.dump  ecos_notifications.dump
    # ecos_process.dump  ecos_uiserv.dump

.. note::

    **Если пароль** ``postgres`` **был изменён** (вместо ``postgresstorngpassword`` из ``services/environments/ecos-microservices-postgresql-app.env``) -- заменить значение ``PGPASSWORD=...`` во всех командах.

2.2. MongoDB
~~~~~~~~~~~~

Дамп одной БД ``ecos-process``. Логин/пароль root -- из ``services/environments/mongodb-app.env``. Если они менялись -- заменить в команде. ``--archive`` без значения = вывод в stdout.

.. code-block:: bash

    docker compose exec -T mongodb-app mongodump \
      --username root_user --password root_user_password --authenticationDatabase admin \
      --db ecos-process --archive --gzip \
      > ~/citeck-migration/mongo/ecos-process.archive

После выполнения в ``~/citeck-migration/mongo/`` должен быть один файл ``ecos-process.archive``.

2.3. Zookeeper
~~~~~~~~~~~~~~

Делаем на остановленном контейнере, чтобы не получить частично записанный snapshot. Bind-mount каталог принадлежит uid Bitnami zookeeper (1001), а не вашему пользователю -- поэтому ``tar`` запускаем во временном контейнере, чтобы не зависеть от ``sudo``:

.. code-block:: bash

    docker compose stop zookeeper-app
    docker run --rm \
      -v "$(pwd)/services/ecos-community-demo-data/zookeeper-app/data:/src:ro" \
      -v "$HOME/citeck-migration/zookeeper:/dst" \
      alpine sh -c "
        tar -czf /dst/version-2.tar.gz -C /src version-2 && \
        chown $(id -u):$(id -g) /dst/version-2.tar.gz
      "
    docker compose start zookeeper-app

Путь ``services/ecos-community-demo-data/zookeeper-app/data`` -- это host-путь bind-mount из ``services/zookeeper-app.yaml``. Compose разрешает относительные пути относительно файла сервиса (т. е. ``services/...``), а не корня репо. Если в вашем развёртывании layout другой -- указать свой путь.

2.4. Итоговая структура каталога
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: text

    ~/citeck-migration/
    ├── postgres/   # 9 .dump файлов
    ├── mongo/      # 1 .archive
    └── zookeeper/  # version-2.tar.gz

Этап 3. Передача файлов
-----------------------

Передайте каталог ``~/citeck-migration/`` (PostgreSQL-дампы + Mongo-архив + Zookeeper-tarball) на целевой сервер любым удобным способом: ``rsync``, ``scp``, S3, переносной носитель -- на ваше усмотрение.

На целевом сервере положите его по тому же пути -- ``~/citeck-migration/``. **Важно сохранить структуру с тремя подкаталогами** (``postgres/``, ``mongo/``, ``zookeeper/``) -- команды этапа 4 ссылаются на пути вида ``~/citeck-migration/postgres/<имя>.dump``. Если файлы скопированы плоско в одну папку, импорт сломается.

Этап 4. Загрузка на target
--------------------------

Все команды -- на новом сервере. Имена контейнеров launcher2 в серверном режиме (namespace всегда ``default``):

- PostgreSQL -- ``citeck_postgres_default``
- MongoDB -- ``citeck_mongo_default``
- Zookeeper -- ``citeck_zookeeper_default``

4.1. PostgreSQL
~~~~~~~~~~~~~~~

На каждую пару БД из mapping-таблицы -- три действия:

1. Скопировать дамп в контейнер.
2. Очистить **все** пользовательские схемы целевой БД (Liquibase на первом старте создал в ней служебные объекты; их надо снести, иначе restore конфликтует по именам).
3. Выполнить ``pg_restore`` с указанием ``--role=<target_user>``, чтобы ownership объектов навешивался корректно.

Расширения (``pg_trgm``, ``uuid-ossp`` и др.) восстанавливаются от имени ``postgres`` -- ``--role`` на ``CREATE EXTENSION`` не влияет.

Блок команд для каждой пары (повторить 9 раз):

**ecos_apps → citeck_eapps:**

.. code-block:: bash

    docker cp ~/citeck-migration/postgres/ecos_apps.dump citeck_postgres_default:/tmp/

    docker exec -i \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      psql -U postgres -d citeck_eapps <<'SQL'
    DO $$ DECLARE r RECORD; BEGIN
      FOR r IN SELECT schema_name FROM information_schema.schemata
               WHERE schema_name NOT IN ('pg_catalog','pg_toast','information_schema')
      LOOP EXECUTE 'DROP SCHEMA IF EXISTS '||quote_ident(r.schema_name)||' CASCADE'; END LOOP;
    END $$;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO citeck_eapps;
    SQL

    docker exec \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      pg_restore -U postgres \
        -d citeck_eapps \
        --no-owner --no-acl --role=citeck_eapps \
        -j 4 /tmp/ecos_apps.dump

    docker exec citeck_postgres_default rm /tmp/ecos_apps.dump

**ecos_uiserv → citeck_uiserv:**

.. code-block:: bash

    docker cp ~/citeck-migration/postgres/ecos_uiserv.dump citeck_postgres_default:/tmp/

    docker exec -i \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      psql -U postgres -d citeck_uiserv <<'SQL'
    DO $$ DECLARE r RECORD; BEGIN
      FOR r IN SELECT schema_name FROM information_schema.schemata
               WHERE schema_name NOT IN ('pg_catalog','pg_toast','information_schema')
      LOOP EXECUTE 'DROP SCHEMA IF EXISTS '||quote_ident(r.schema_name)||' CASCADE'; END LOOP;
    END $$;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO citeck_uiserv;
    SQL

    docker exec \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      pg_restore -U postgres \
        -d citeck_uiserv \
        --no-owner --no-acl --role=citeck_uiserv \
        -j 4 /tmp/ecos_uiserv.dump

    docker exec citeck_postgres_default rm /tmp/ecos_uiserv.dump

**ecos_integrations → citeck_integrations:**

.. code-block:: bash

    docker cp ~/citeck-migration/postgres/ecos_integrations.dump citeck_postgres_default:/tmp/

    docker exec -i \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      psql -U postgres -d citeck_integrations <<'SQL'
    DO $$ DECLARE r RECORD; BEGIN
      FOR r IN SELECT schema_name FROM information_schema.schemata
               WHERE schema_name NOT IN ('pg_catalog','pg_toast','information_schema')
      LOOP EXECUTE 'DROP SCHEMA IF EXISTS '||quote_ident(r.schema_name)||' CASCADE'; END LOOP;
    END $$;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO citeck_integrations;
    SQL

    docker exec \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      pg_restore -U postgres \
        -d citeck_integrations \
        --no-owner --no-acl --role=citeck_integrations \
        -j 4 /tmp/ecos_integrations.dump

    docker exec citeck_postgres_default rm /tmp/ecos_integrations.dump

**ecos_model → citeck_emodel:**

.. code-block:: bash

    docker cp ~/citeck-migration/postgres/ecos_model.dump citeck_postgres_default:/tmp/

    docker exec -i \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      psql -U postgres -d citeck_emodel <<'SQL'
    DO $$ DECLARE r RECORD; BEGIN
      FOR r IN SELECT schema_name FROM information_schema.schemata
               WHERE schema_name NOT IN ('pg_catalog','pg_toast','information_schema')
      LOOP EXECUTE 'DROP SCHEMA IF EXISTS '||quote_ident(r.schema_name)||' CASCADE'; END LOOP;
    END $$;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO citeck_emodel;
    SQL

    docker exec \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      pg_restore -U postgres \
        -d citeck_emodel \
        --no-owner --no-acl --role=citeck_emodel \
        -j 4 /tmp/ecos_model.dump

    docker exec citeck_postgres_default rm /tmp/ecos_model.dump

**ecos_notifications → citeck_notifications:**

.. code-block:: bash

    docker cp ~/citeck-migration/postgres/ecos_notifications.dump citeck_postgres_default:/tmp/

    docker exec -i \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      psql -U postgres -d citeck_notifications <<'SQL'
    DO $$ DECLARE r RECORD; BEGIN
      FOR r IN SELECT schema_name FROM information_schema.schemata
               WHERE schema_name NOT IN ('pg_catalog','pg_toast','information_schema')
      LOOP EXECUTE 'DROP SCHEMA IF EXISTS '||quote_ident(r.schema_name)||' CASCADE'; END LOOP;
    END $$;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO citeck_notifications;
    SQL

    docker exec \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      pg_restore -U postgres \
        -d citeck_notifications \
        --no-owner --no-acl --role=citeck_notifications \
        -j 4 /tmp/ecos_notifications.dump

    docker exec citeck_postgres_default rm /tmp/ecos_notifications.dump

**ecos_history → citeck_history:**

.. code-block:: bash

    docker cp ~/citeck-migration/postgres/ecos_history.dump citeck_postgres_default:/tmp/

    docker exec -i \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      psql -U postgres -d citeck_history <<'SQL'
    DO $$ DECLARE r RECORD; BEGIN
      FOR r IN SELECT schema_name FROM information_schema.schemata
               WHERE schema_name NOT IN ('pg_catalog','pg_toast','information_schema')
      LOOP EXECUTE 'DROP SCHEMA IF EXISTS '||quote_ident(r.schema_name)||' CASCADE'; END LOOP;
    END $$;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO citeck_history;
    SQL

    docker exec \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      pg_restore -U postgres \
        -d citeck_history \
        --no-owner --no-acl --role=citeck_history \
        -j 4 /tmp/ecos_history.dump

    docker exec citeck_postgres_default rm /tmp/ecos_history.dump

**ecos_process → citeck_eproc:**

.. code-block:: bash

    docker cp ~/citeck-migration/postgres/ecos_process.dump citeck_postgres_default:/tmp/

    docker exec -i \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      psql -U postgres -d citeck_eproc <<'SQL'
    DO $$ DECLARE r RECORD; BEGIN
      FOR r IN SELECT schema_name FROM information_schema.schemata
               WHERE schema_name NOT IN ('pg_catalog','pg_toast','information_schema')
      LOOP EXECUTE 'DROP SCHEMA IF EXISTS '||quote_ident(r.schema_name)||' CASCADE'; END LOOP;
    END $$;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO citeck_eproc;
    SQL

    docker exec \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      pg_restore -U postgres \
        -d citeck_eproc \
        --no-owner --no-acl --role=citeck_eproc \
        -j 4 /tmp/ecos_process.dump

    docker exec citeck_postgres_default rm /tmp/ecos_process.dump

**ecos_camunda → citeck_camunda:**

.. code-block:: bash

    docker cp ~/citeck-migration/postgres/ecos_camunda.dump citeck_postgres_default:/tmp/

    docker exec -i \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      psql -U postgres -d citeck_camunda <<'SQL'
    DO $$ DECLARE r RECORD; BEGIN
      FOR r IN SELECT schema_name FROM information_schema.schemata
               WHERE schema_name NOT IN ('pg_catalog','pg_toast','information_schema')
      LOOP EXECUTE 'DROP SCHEMA IF EXISTS '||quote_ident(r.schema_name)||' CASCADE'; END LOOP;
    END $$;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO citeck_camunda;
    SQL

    docker exec \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      pg_restore -U postgres \
        -d citeck_camunda \
        --no-owner --no-acl --role=citeck_camunda \
        -j 4 /tmp/ecos_camunda.dump

    docker exec citeck_postgres_default rm /tmp/ecos_camunda.dump

**ecos_edi → citeck_edi:**

.. code-block:: bash

    docker cp ~/citeck-migration/postgres/ecos_edi.dump citeck_postgres_default:/tmp/

    docker exec -i \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      psql -U postgres -d citeck_edi <<'SQL'
    DO $$ DECLARE r RECORD; BEGIN
      FOR r IN SELECT schema_name FROM information_schema.schemata
               WHERE schema_name NOT IN ('pg_catalog','pg_toast','information_schema')
      LOOP EXECUTE 'DROP SCHEMA IF EXISTS '||quote_ident(r.schema_name)||' CASCADE'; END LOOP;
    END $$;
    CREATE SCHEMA public;
    GRANT ALL ON SCHEMA public TO citeck_edi;
    SQL

    docker exec \
      -e PGPASSWORD=postgres \
      citeck_postgres_default \
      pg_restore -U postgres \
        -d citeck_edi \
        --no-owner --no-acl --role=citeck_edi \
        -j 4 /tmp/ecos_edi.dump

    docker exec citeck_postgres_default rm /tmp/ecos_edi.dump

4.2. MongoDB
~~~~~~~~~~~~

.. code-block:: bash

    docker cp ~/citeck-migration/mongo/ecos-process.archive citeck_mongo_default:/tmp/

    docker exec citeck_mongo_default mongorestore \
      --username "$(docker exec citeck_mongo_default printenv MONGO_INITDB_ROOT_USERNAME)" \
      --password "$(docker exec citeck_mongo_default printenv MONGO_INITDB_ROOT_PASSWORD)" \
      --authenticationDatabase admin \
      --nsFrom 'ecos-process.*' --nsTo 'citeck_eproc.*' \
      --archive=/tmp/ecos-process.archive --gzip --drop

    docker exec citeck_mongo_default rm /tmp/ecos-process.archive

Опции:

- ``--nsFrom 'ecos-process.*' --nsTo 'citeck_eproc.*'`` -- переименование namespace при restore.
- ``--drop`` -- удаляет коллекции, оставшиеся от первого старта webapp ``eproc``.
- Username и пароль root читаются из ENV контейнера через ``printenv``, чтобы не зависеть от того, что launcher сгенерировал.

4.3. Zookeeper
~~~~~~~~~~~~~~

Останавливаем zookeeper **через** ``citeck stop``, а не ``docker stop``. Это критично: launcher2 имеет reconciler, который через ~1 минуту перезапустит контейнер, остановленный «снаружи», прямо во время того, как мы пишем в данные. ``citeck stop`` помечает приложение как detached и reconciler оставляет его в покое.

Хранилище zookeeper в launcher2 -- это **bind-mount каталог на хосте** (не named docker volume): ``/opt/citeck/data/runtime/default/volumes/zookeeper2/``. Внутри него -- подкаталог ``data/``, в котором zookeeper держит snapshots, и ``datalog/``, в котором держит transaction log. Bitnami же на source складывал и snapshots, и log в один каталог ``data/version-2/``. При импорте нужно **разделить файлы**: ``log.*`` идут в ``datalog/version-2/``, а **всё остальное** (``snapshot.*``, ``acceptedEpoch``, ``currentEpoch`` и любые другие служебные файлы) -- в ``data/version-2/``.

.. code-block:: bash

    ZK_DIR=/opt/citeck/data/runtime/default/volumes/zookeeper2

    citeck stop zookeeper

    # Очистить старые данные (они созданы launcher'ом при первом старте)
    rm -rf $ZK_DIR/data/version-2 $ZK_DIR/datalog/version-2
    mkdir -p $ZK_DIR/data/version-2 $ZK_DIR/datalog/version-2

    # Распаковать дамп во временный каталог
    TMP=$(mktemp -d)
    tar -xzf ~/citeck-migration/zookeeper/version-2.tar.gz -C $TMP

    # Сначала переносим log'и в datalog/, потом всё остальное в data/
    mv $TMP/version-2/log.* $ZK_DIR/datalog/version-2/ 2>/dev/null || true
    mv $TMP/version-2/*     $ZK_DIR/data/version-2/
    rm -rf $TMP

    # Выставить владельца -- uid/gid пользователя zookeeper в official образе
    chown -R 1001:1001 $ZK_DIR/data/version-2 $ZK_DIR/datalog/version-2

    citeck start zookeeper

Замечания:

- Точный путь bind-mount проверить через ``docker inspect citeck_zookeeper_default --format '{{(index .Mounts 0).Source}}'``.
- ``chown 1001:1001`` -- uid/gid пользователя ``zookeeper`` в официальном образе. Без него запуск падает с ``permission denied``.
- Если файлы не разделены -- official zookeeper падает с ``SnapDirContentCheckException: Snapshot directory has log files``.
- ``citeck start zookeeper`` re-attaches приложение, после чего reconciler снова им управляет.
- Проверить старт:

  .. code-block:: bash

      docker logs --tail 100 citeck_zookeeper_default

  В логах должно быть ``Snapshot loaded`` и ``Snapshotting:`` без ошибок.

4.4. Поднять webapp'ы обратно
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Тот же список приложений, что был остановлен в шаге 1.3. **Важно**: в отличие от ``citeck stop`` (принимает любое число аргументов), ``citeck start`` принимает только **один app за раз**, поэтому запускаем циклом -- **без** ``--detach``, чтобы каждый старт дожидался ``RUNNING`` перед стартом следующего:

.. code-block:: bash

    for app in <app1> <app2> <app3> ...; do
      citeck start "$app"
    done

Если запускать с ``--detach``, возникает race condition: proxy запускается раньше, чем onlyoffice (или другая зависимость) успевает стать DNS-резолвимым, и падает с ``host not found in upstream "onlyoffice"``. Sequential-старт (без ``--detach``) использует ``waitForDeps`` launcher2 и поднимает приложения в правильном порядке.

Цикл занимает 10--20 минут (каждый Java-webapp стартует 1--3 минуты). Прогресс параллельно можно смотреть через ``citeck status -w`` в другой сессии.

Liquibase каждого webapp при старте увидит актуальный changelog (source перед миграцией обновлён до 2026.1) -- изменений schema не будет.

Этап 5. Проверка
----------------

5.1. Что должно работать
~~~~~~~~~~~~~~~~~~~~~~~~

- Логин в Web UI под ``admin / <admin-пароль из шага 1.1>``. **Не** ``admin / admin`` источника -- пароль теперь сгенерирован launcher'ом.
- Списки записей в ``eapps``, ``eproc``, ``uiserv`` показывают данные источника.
- BPMN-процессы из ``eproc`` запускаются (mongo + postgres согласованы).
- В Keycloak присутствуют только пользователь ``admin`` и сервисный аккаунт ``citeck``.

5.2. Проверочные команды
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

    citeck status
    citeck health
    docker exec -e PGPASSWORD=postgres citeck_postgres_default \
      psql -U postgres -d citeck_eapps -c "\dn"
    docker exec -e PGPASSWORD=postgres citeck_postgres_default \
      psql -U postgres -d citeck_eapps -c "\dt+ *.*" | head
    docker exec citeck_mongo_default mongo \
      -u "$(docker exec citeck_mongo_default printenv MONGO_INITDB_ROOT_USERNAME)" \
      -p "$(docker exec citeck_mongo_default printenv MONGO_INITDB_ROOT_PASSWORD)" \
      --authenticationDatabase admin \
      citeck_eproc --eval "db.getCollectionNames()"
    docker exec citeck_zookeeper_default \
      bash -c 'echo "ls /" | zkCli.sh -server localhost:2181'

``citeck status`` должна показать все приложения в статусе ``RUNNING``. ``citeck health`` -- exit-код 0.

5.3. Что заведомо обнулилось
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Пользователи и роли Keycloak источника.
- In-flight сообщения RabbitMQ.
- Логи nginx/proxy.
- Кеш сертификатов Let's Encrypt -- будет перевыпущен при первом запросе.

Откат
-----

Сбой на target до доставки данных
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Переустановить с нуля:

.. code-block:: bash

    citeck uninstall --delete-data

Затем пройти установку и подготовку target заново (этап 1).

Сбой после импорта
~~~~~~~~~~~~~~~~~~

Повторить с нуля:

.. code-block:: bash

    citeck uninstall --delete-data

Затем установка → подготовка target → импорт. Source уже на 2026.1, его трогать не нужно -- дампы из ``~/citeck-migration/`` ещё валидны.

Сбой апгрейда source до 2026.1 (предусловие 1)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Восстановить из backup'а из шага 0:

- Если backup делался через ``tar`` -- ``docker compose down``, распаковать ``tar``, ``docker compose up -d``.
- Если делался через ``pg_dumpall`` + ``mongodump`` -- следовать стандартной процедуре restore PostgreSQL/MongoDB.

Дампы из ``~/citeck-migration/`` сохранять минимум 1--2 недели после миграции -- на случай поздно обнаруженных проблем.
