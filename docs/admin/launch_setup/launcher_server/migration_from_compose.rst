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
- На **target** лаунчер управляет контейнерами напрямую через Docker SDK (без compose) -- там используется ``docker exec`` с реальными именами контейнеров (``citeck_postgres_default``, ``citeck_mongo_default``, ``citeck_zookeeper_default``; в серверном режиме имя всегда ``citeck_<приложение>_default``).
- Файлы на **target** передаются в контейнеры через **каталог экспорта** ``/opt/citeck/data/runtime/default/export/<приложение>/`` (в контейнере -- ``/citeck/export``), а не через ``docker cp`` в ``/tmp`` контейнера (подробнее -- в шаге 4.1).

Что мигрируется и что нет
-------------------------

**Мигрируется:**

- PostgreSQL -- пользовательские БД (схема + данные), точечно по mapping-таблице.
- MongoDB -- одна БД ``ecos-process`` → ``citeck_eproc``.
- Zookeeper -- содержимое каталога ``version-2/`` (snapshots + transaction log).

**НЕ мигрируется** (то есть **выходит за рамки этой инструкции** -- технически данные ниже тоже можно перенести, если у кого-то такая задача возникнет, но пошаговую процедуру для них мы здесь не описываем):

- БД ``keycloak`` -- на target создаётся самим лаунчером. На source соответствующая БД называется ``ecos_identity`` (сервис ``ecos-identity-app`` в community -- это Keycloak старой версии).
- Пользователи, роли, клиенты Keycloak источника (включая demo-аккаунт ``admin/admin``). Если они заводились вручную -- пересоздать после миграции. Admin на target использует пароль, сгенерированный лаунчером при первом старте (показывается в визарде один раз; перевыпустить через ``citeck setup admin-password``).
- RabbitMQ -- очереди и in-flight сообщения.
- Volumes proxy/nginx -- логи, кеш сертификатов Let's Encrypt.
- Секреты (JWT, OIDC client secret, admin password) -- лаунчер генерирует свои при первой установке.

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
      - 3.9.5 (official)
      - копия ``version-2/`` из dataDir
    * - RabbitMQ
      - --
      - --
      - пропускаем
    * - Keycloak БД
      - --
      - --
      - пропускаем

Версии на target -- значения лаунчера по умолчанию для бандла ``2026.1``; фактические можно посмотреть командой ``docker ps``.

PostgreSQL переезжает с мажорным скачком версии (12 → 17). Физическое копирование data-каталога (volume) не сработает -- нужен только логический dump.

Mapping БД и пользователей
--------------------------

В лаунчере действует соглашение: ``имя_БД == имя_пользователя == пароль``. Для каждой БД (``citeck_emodel``, ``citeck_eapps`` и т. д.) создаётся роль с тем же именем и паролем, совпадающим с именем. Суперпользователь PostgreSQL -- ``postgres / postgres``.

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

- ``ecos_gateway`` -- в лаунчере у gateway нет своей БД.
- ``ecos_identity`` -- это БД сервиса ``ecos-identity-app``, который в community-сетапе является Keycloak (просто более старой версии). Соответствует решению «БД ``keycloak`` не мигрируем» -- пользователи и роли источника при миграции теряются (см. «НЕ мигрируется» во вступлении).
- ``keycloak`` -- на target создаёт сам лаунчер.

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
- Хранилище в лаунчере -- это bind-mount каталог на хосте (не named docker volume). Точный путь можно подтвердить через ``docker inspect citeck_zookeeper_default --format '{{range .Mounts}}{{.Source}} -> {{.Destination}}{{println}}{{end}}'`` -- нужна строка с ``/citeck/zookeeper``.

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

Это снимает риск рассинхронизации schema/changelog при заливке в лаунчер (тоже 2026.1). В каталоге ``citeck-community``:

.. code-block:: bash

    git pull
    docker compose up -d

Дождаться, пока все микросервисы дойдут до ``RUNNING`` / ``healthy`` -- Liquibase должен догнать changelog. Проверить можно так:

.. code-block:: bash

    docker compose ps

2. Target подготовлен
~~~~~~~~~~~~~~~~~~~~~

Установлен ``citeck-launcher`` версии **не ниже 2.15.2** (каталог экспорта, через который дампы передаются в контейнеры, появился в 2.10.0; публикация порта БД только на ``127.0.0.1`` -- в 2.15.2), bundle ``community:2026.1`` или ``enterprise:2026.1`` (в зависимости от лицензии). Подробности первого запуска -- в этапе 1.

Версию можно посмотреть командой ``citeck version``. Если лаунчер старее -- обновите его, повторно выполнив установочную команду из шага 1.1: скрипт определит установленную версию и предложит обновиться, запущенные контейнеры при этом продолжают работать. Команда ``citeck update`` лаунчер **не** обновляет -- она только подтягивает свежие описания workspace и бандлов.

3. Свободное место
~~~~~~~~~~~~~~~~~~

- На source: ≥ объём данных × 1.5 (для дампов).
- На target: то же, причём на разделе с ``/opt/citeck`` -- там лежат и данные PostgreSQL, и каталог экспорта, через который идёт restore (шаг 4.1).

4. Доступ к docker
~~~~~~~~~~~~~~~~~~

``docker ps`` без sudo либо через sudo на обоих серверах.

Этап 1. Подготовка target (лаунчер)
-----------------------------------

Цель этапа: получить запущенный один раз namespace, чтобы лаунчер создал инфраструктуру (контейнеры и каталоги данных в ``/opt/citeck/data/runtime/default/``), завёл пустые БД с пользователями и сгенерировал секреты.

1.1. Установить лаунчер
~~~~~~~~~~~~~~~~~~~~~~~

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

- PostgreSQL: ``postgres / postgres`` (задано в лаунчере жёстко).
- MongoDB: пароль root сгенерирован лаунчером, читается через ``docker exec citeck_mongo_default printenv MONGO_INITDB_ROOT_PASSWORD``. Команды импорта в этапе 4 берут его именно так.

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

    **Если какая-то из БД отсутствует на вашем source** (например, в community-only deployment нет ``ecos_edi``) -- ``pg_dump`` упадёт с ``database "<name>" does not exist``. Просто пропустите соответствующий блок: соответствующая target-БД в лаунчере либо отсутствует, либо останется пустой и Liquibase webapp'а наполнит её при первом старте.

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

Каталог ``~/citeck-migration/`` лучше разместить на том же разделе, что и ``/opt/citeck``: на этапе 4 дампы перемещаются в каталог экспорта лаунчера (``/opt/citeck/data/runtime/default/export/``), и в пределах одного раздела ``mv`` выполняется мгновенно, без копирования.

Этап 4. Загрузка на target
--------------------------

Все команды -- на новом сервере. Имена контейнеров лаунчера в серверном режиме (namespace всегда ``default``):

- PostgreSQL -- ``citeck_postgres_default``
- MongoDB -- ``citeck_mongo_default``
- Zookeeper -- ``citeck_zookeeper_default``

4.1. PostgreSQL
~~~~~~~~~~~~~~~

Дампы передаются в контейнер через **каталог экспорта**, а не через ``docker cp`` в ``/tmp``. Каталог ``/tmp`` лежит в записываемом слое контейнера (на разделе ``/var/lib/docker``), и большой дамп (десятки гигабайт) его просто переполняет. Каталог экспорта -- это обычный каталог на хосте, смонтированный в контейнер:

- на хосте: ``/opt/citeck/data/runtime/default/export/postgres/``;
- в контейнере ``citeck_postgres_default``: ``/citeck/export/`` (тот же путь записан в переменной окружения ``CITECK_EXPORT_DIR``).

Такой каталог есть у **каждого** контейнера лаунчера (``.../export/<приложение>/``), права ``1777`` -- писать в него может любой пользователь. Лаунчер создаёт его при запуске namespace (этап 1), поэтому к этому моменту он уже существует.

.. important::

    - Дамп нужно **переместить** (``mv``) или скопировать в каталог экспорта. Символьная ссылка не подойдёт: ссылка на файл вне каталога экспорта внутри контейнера не видна.
    - ``mv`` в пределах одного раздела выполняется мгновенно; если ``~/citeck-migration/`` и ``/opt/citeck`` на разных разделах, файл копируется, и на разделе с ``/opt/citeck`` должно хватить места под дамп. Можно сразу на этапе 3 передавать дампы прямо в ``/opt/citeck/data/runtime/default/export/postgres/``.
    - После restore уберите дамп из каталога экспорта -- ниже он перемещается обратно в ``~/citeck-migration/`` (дампы стоит хранить до окончания проверки, см. «Откат»). Проверить содержимое каталога можно командой ``citeck export ls postgres``.

На каждую пару БД из mapping-таблицы -- четыре действия:

1. Переместить дамп в каталог экспорта postgres.
2. Очистить **все** пользовательские схемы целевой БД: restore должен идти в пустую БД, а Liquibase на первом старте уже создал в ней свои объекты -- без очистки restore конфликтует по именам.
3. Выполнить ``pg_restore`` с указанием ``--role=<target_user>``, чтобы ownership объектов навешивался корректно.
4. Убрать дамп из каталога экспорта.

Расширения (``pg_trgm``, ``uuid-ossp`` и др.) восстанавливаются от имени ``postgres`` -- ``--role`` на ``CREATE EXTENSION`` не влияет.

Все webapp'ы уже остановлены на шаге 1.3, поэтому в БД во время restore никто не пишет.

Блок команд для каждой пары (повторить 9 раз):

**ecos_apps → citeck_eapps:**

.. code-block:: bash

    mv ~/citeck-migration/postgres/ecos_apps.dump /opt/citeck/data/runtime/default/export/postgres/

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
        -j 4 /citeck/export/ecos_apps.dump

    mv /opt/citeck/data/runtime/default/export/postgres/ecos_apps.dump ~/citeck-migration/postgres/

**ecos_uiserv → citeck_uiserv:**

.. code-block:: bash

    mv ~/citeck-migration/postgres/ecos_uiserv.dump /opt/citeck/data/runtime/default/export/postgres/

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
        -j 4 /citeck/export/ecos_uiserv.dump

    mv /opt/citeck/data/runtime/default/export/postgres/ecos_uiserv.dump ~/citeck-migration/postgres/

**ecos_integrations → citeck_integrations:**

.. code-block:: bash

    mv ~/citeck-migration/postgres/ecos_integrations.dump /opt/citeck/data/runtime/default/export/postgres/

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
        -j 4 /citeck/export/ecos_integrations.dump

    mv /opt/citeck/data/runtime/default/export/postgres/ecos_integrations.dump ~/citeck-migration/postgres/

**ecos_model → citeck_emodel:**

.. code-block:: bash

    mv ~/citeck-migration/postgres/ecos_model.dump /opt/citeck/data/runtime/default/export/postgres/

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
        -j 4 /citeck/export/ecos_model.dump

    mv /opt/citeck/data/runtime/default/export/postgres/ecos_model.dump ~/citeck-migration/postgres/

**ecos_notifications → citeck_notifications:**

.. code-block:: bash

    mv ~/citeck-migration/postgres/ecos_notifications.dump /opt/citeck/data/runtime/default/export/postgres/

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
        -j 4 /citeck/export/ecos_notifications.dump

    mv /opt/citeck/data/runtime/default/export/postgres/ecos_notifications.dump ~/citeck-migration/postgres/

**ecos_history → citeck_history:**

.. code-block:: bash

    mv ~/citeck-migration/postgres/ecos_history.dump /opt/citeck/data/runtime/default/export/postgres/

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
        -j 4 /citeck/export/ecos_history.dump

    mv /opt/citeck/data/runtime/default/export/postgres/ecos_history.dump ~/citeck-migration/postgres/

**ecos_process → citeck_eproc:**

.. code-block:: bash

    mv ~/citeck-migration/postgres/ecos_process.dump /opt/citeck/data/runtime/default/export/postgres/

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
        -j 4 /citeck/export/ecos_process.dump

    mv /opt/citeck/data/runtime/default/export/postgres/ecos_process.dump ~/citeck-migration/postgres/

**ecos_camunda → citeck_camunda:**

.. code-block:: bash

    mv ~/citeck-migration/postgres/ecos_camunda.dump /opt/citeck/data/runtime/default/export/postgres/

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
        -j 4 /citeck/export/ecos_camunda.dump

    mv /opt/citeck/data/runtime/default/export/postgres/ecos_camunda.dump ~/citeck-migration/postgres/

**ecos_edi → citeck_edi:**

.. code-block:: bash

    mv ~/citeck-migration/postgres/ecos_edi.dump /opt/citeck/data/runtime/default/export/postgres/

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
        -j 4 /citeck/export/ecos_edi.dump

    mv /opt/citeck/data/runtime/default/export/postgres/ecos_edi.dump ~/citeck-migration/postgres/

4.2. MongoDB
~~~~~~~~~~~~

.. note::

    Контейнер MongoDB (``citeck_mongo_default``) создаётся на target, только если в выбранном бандле ecos-process (``eproc``) старше 2.33.0 -- для ``2026.1`` это так. В новых версиях ecos-process данные процессов хранятся в PostgreSQL, и новый namespace создаётся без MongoDB. Проверить: ``docker ps | grep mongo``.

Архив передаётся тем же способом -- через каталог экспорта mongo (на хосте ``/opt/citeck/data/runtime/default/export/mongo/``, в контейнере ``/citeck/export/``):

.. code-block:: bash

    mv ~/citeck-migration/mongo/ecos-process.archive /opt/citeck/data/runtime/default/export/mongo/

    docker exec citeck_mongo_default mongorestore \
      --username "$(docker exec citeck_mongo_default printenv MONGO_INITDB_ROOT_USERNAME)" \
      --password "$(docker exec citeck_mongo_default printenv MONGO_INITDB_ROOT_PASSWORD)" \
      --authenticationDatabase admin \
      --nsFrom 'ecos-process.*' --nsTo 'citeck_eproc.*' \
      --archive=/citeck/export/ecos-process.archive --gzip --drop

    mv /opt/citeck/data/runtime/default/export/mongo/ecos-process.archive ~/citeck-migration/mongo/

Опции:

- ``--nsFrom 'ecos-process.*' --nsTo 'citeck_eproc.*'`` -- переименование namespace при restore.
- ``--drop`` -- удаляет коллекции, оставшиеся от первого старта webapp ``eproc``.
- Username и пароль root читаются из ENV контейнера через ``printenv``, чтобы не зависеть от того, что сгенерировал лаунчер.

4.3. Zookeeper
~~~~~~~~~~~~~~

Останавливаем zookeeper **через** ``citeck stop``, а не ``docker stop``. Это критично: у лаунчера есть reconciler, который через ~1 минуту перезапустит контейнер, остановленный «снаружи», прямо во время того, как мы пишем в данные. ``citeck stop`` помечает приложение как detached и reconciler оставляет его в покое.

Хранилище zookeeper в лаунчере -- это **bind-mount каталог на хосте** (не named docker volume): ``/opt/citeck/data/runtime/default/volumes/zookeeper2/``. Внутри него -- подкаталог ``data/``, в котором zookeeper держит snapshots, и ``datalog/``, в котором держит transaction log. Bitnami же на source складывал и snapshots, и log в один каталог ``data/version-2/``. При импорте нужно **разделить файлы**: ``log.*`` идут в ``datalog/version-2/``, а **всё остальное** (``snapshot.*``, ``acceptedEpoch``, ``currentEpoch`` и любые другие служебные файлы) -- в ``data/version-2/``.

.. code-block:: bash

    ZK_DIR=/opt/citeck/data/runtime/default/volumes/zookeeper2

    citeck stop zookeeper

    # Очистить старые данные (они созданы лаунчером при первом старте)
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
    chown -R 1000:1000 $ZK_DIR/data/version-2 $ZK_DIR/datalog/version-2

    citeck start zookeeper

Замечания:

- Точный путь bind-mount проверить через ``docker inspect citeck_zookeeper_default --format '{{range .Mounts}}{{.Source}} -> {{.Destination}}{{println}}{{end}}'`` -- нужна строка с ``/citeck/zookeeper`` (у контейнера есть и другие монтирования, например каталог экспорта).
- ``chown 1000:1000`` -- uid/gid пользователя ``zookeeper`` в официальном образе. Без него запуск может упасть с ``permission denied``.
- Пока zookeeper остановлен, ``citeck status`` может показывать namespace как ``STALLED`` -- это ожидаемо, после ``citeck start zookeeper`` статус вернётся.
- Если файлы не разделены -- official zookeeper падает с ``SnapDirContentCheckException: Snapshot directory has log files``.
- ``citeck start zookeeper`` re-attaches приложение, после чего reconciler снова им управляет.
- Проверить старт:

  .. code-block:: bash

      docker logs --tail 100 citeck_zookeeper_default

  В логах должно быть ``Snapshot loaded`` и ``Snapshotting:`` без ошибок.

4.4. Поднять webapp'ы обратно
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Тот же список приложений, что был остановлен в шаге 1.3. **Важно**: в отличие от ``citeck stop`` (принимает любое число аргументов), ``citeck start`` принимает только **один app за раз**, поэтому запускаем циклом -- **без** ``--detach``, чтобы каждый старт дожидался ``RUNNING`` перед стартом следующего. Цикл запускайте в интерактивном терминале: если вывод перенаправлен в файл или команда выполняется не в терминале (скрипт, ``nohup``), ``citeck start <app>`` не ждёт ``RUNNING`` и возвращается сразу:

.. code-block:: bash

    for app in <app1> <app2> <app3> ...; do
      citeck start "$app"
    done

Если запускать с ``--detach``, возникает race condition: proxy запускается раньше, чем onlyoffice (или другая зависимость) успевает стать DNS-резолвимым, и падает с ``host not found in upstream "onlyoffice"``. Последовательный старт (без ``--detach``) дожидается зависимостей каждого приложения и поднимает приложения в правильном порядке.

Цикл занимает 10--20 минут (каждый Java-webapp стартует 1--3 минуты). Прогресс параллельно можно смотреть через ``citeck status -w`` в другой сессии.

Liquibase каждого webapp при старте увидит актуальный changelog (source перед миграцией обновлён до 2026.1) -- изменений schema не будет.

Этап 5. Проверка
----------------

5.1. Что должно работать
~~~~~~~~~~~~~~~~~~~~~~~~

- Логин в Web UI под ``admin / <admin-пароль из шага 1.1>``. **Не** ``admin / admin`` источника -- пароль теперь сгенерирован лаунчером.
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

.. _migration_from_compose_db_access:

Работа с БД после миграции
--------------------------

В docker-compose версии PostgreSQL был доступен снаружи (порт ``15432``). В серверном режиме лаунчер публикует наружу **только прокси** -- порты PostgreSQL, MongoDB, RabbitMQ и остальных сервисов с хоста не доступны. Ниже -- как делать дампы и восстановление и как подключиться к БД из DBeaver/pgAdmin.

Резервная копия одной БД
~~~~~~~~~~~~~~~~~~~~~~~~

Дамп пишется сразу в каталог экспорта postgres и оказывается на хосте, минуя файловую систему контейнера:

.. code-block:: bash

    docker exec citeck_postgres_default \
      pg_dump -U postgres -F c -f /citeck/export/citeck_emodel.dump citeck_emodel

    ls -lh /opt/citeck/data/runtime/default/export/postgres/

Заберите файл из ``/opt/citeck/data/runtime/default/export/postgres/`` (или командой ``citeck export get postgres citeck_emodel.dump --rm`` -- скачает файл в текущий каталог и удалит его из каталога экспорта). Не оставляйте дампы в каталоге экспорта: они занимают место на разделе с данными.

Восстановление одной БД из дампа
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Пример для ``citeck_emodel``; для другой БД подставьте её имя и приложение, которое её использует (``citeck_eproc`` и ``citeck_camunda`` -- ``eproc``, ``citeck_eapps`` -- ``eapps`` и т. д., см. «Mapping БД и пользователей»).

1. Переместите дамп в каталог экспорта (не символьной ссылкой -- ссылка на файл вне каталога в контейнере не видна):

   .. code-block:: bash

       mv /path/to/emodel.dump /opt/citeck/data/runtime/default/export/postgres/

2. Остановите приложение, которое пишет в эту БД:

   .. code-block:: bash

       citeck stop emodel

3. Очистите целевую БД -- restore должен идти в пустую БД (блок ``DROP SCHEMA`` из шага 4.1 с подставленным именем БД и роли).

4. Восстановите дамп. Custom-формат (``pg_dump -F c``):

   .. code-block:: bash

       docker exec -it citeck_postgres_default \
         pg_restore -U postgres -d citeck_emodel \
           --no-owner --role=citeck_emodel \
           -j 4 /citeck/export/emodel.dump

   Обычный SQL-дамп (``.sql``, снятый с ``--no-owner --no-acl``) выполняется от имени роли БД, чтобы объекты принадлежали ей:

   .. code-block:: bash

       docker exec -it citeck_postgres_default \
         psql -U citeck_emodel -d citeck_emodel -v ON_ERROR_STOP=1 \
           -f /citeck/export/emodel.sql

5. Запустите приложение и удалите дамп из каталога экспорта:

   .. code-block:: bash

       citeck start emodel
       rm /opt/citeck/data/runtime/default/export/postgres/emodel.dump

Прямое подключение к PostgreSQL (DBeaver, pgAdmin)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Начиная с лаунчера 2.15.2 в описании порта можно указать адрес. Рекомендуемый вариант -- опубликовать PostgreSQL только на loopback-интерфейсе сервера и подключаться через SSH-туннель.

1. На сервере откройте описание приложения:

   .. code-block:: bash

       citeck edit postgres

   и добавьте в раздел ``ports:`` (если его нет -- создайте) запись:

   .. code-block:: yaml

       ports:
         - "127.0.0.1:15432:5432"

   После сохранения лаунчер пересоздаёт контейнер postgres (кратковременный перезапуск БД). Порт ``15432`` будет слушаться только на ``127.0.0.1`` сервера.

2. На рабочей станции поднимите туннель:

   .. code-block:: bash

       ssh -N -L 15432:127.0.0.1:15432 root@<server>

3. В DBeaver/pgAdmin подключайтесь к ``localhost:15432``, пользователь/пароль ``postgres / postgres`` (или роль конкретной БД, например ``citeck_emodel / citeck_emodel``).

Про адрес в описании порта:

- Порт без адреса (``"15432:5432"``) с версии 2.15.2 тоже публикуется только на ``127.0.0.1``.
- ``'*:15432:5432'`` (в YAML -- обязательно в кавычках) открывает порт на всех интерфейсах. **Не делайте так** без необходимости: Docker обходит правила ``ufw``/``iptables`` хоста, и БД с паролем ``postgres`` окажется доступна из сети. Используйте SSH-туннель.
- Убрать правку и вернуть описание по умолчанию -- ``citeck edit postgres --reset`` (сбрасывает **все** правки описания postgres).

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
