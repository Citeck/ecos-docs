.. _core-mechanisms:

Механизмы платформы
=====================

Раздел описывает взаимодействие компонентов Citeck через команды, события и WebAPI, управление транзакциями, версии контента и настройку инфраструктурных подключений.

Раздел включает следующие темы:

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Команды
      :link: ecos_commands
      :link-type: ref

      Декларативный вызов локальных и удалённых действий, синхронная и асинхронная обработка команд.

   .. grid-item-card:: События
      :link: ecos_events
      :link-type: ref

      Локальные и удалённые подписки, параметры слушателей, стандартные события записей и транзакционная обработка.

   .. grid-item-card:: Citeck WebAPI
      :link: ecos-webapi
      :link-type: ref

      Низкоуровневое взаимодействие микросервисов по схеме «запрос — ответ», потоковые данные и обработка ошибок.

   .. grid-item-card:: Транзакции
      :link: ecos-transactions
      :link-type: ref

      Двухфазный коммит, транзакционные ресурсы и действия на этапах жизненного цикла транзакции.

   .. grid-item-card:: Версионирование контента
      :link: content_versioning
      :link-type: ref

      Аспекты версионирования, загрузка и получение версий, права доступа и текстовое сравнение файлов.

   .. grid-item-card:: Внешние коммуникации
      :link: external-communications
      :link-type: ref

      Настройка RabbitMQ, ZooKeeper, БД и cloud config через параметры Spring, ENV и конфигурационные файлы.

.. toctree::
    :maxdepth: 4
    :hidden:

    Core_mechanisms/Commands
    Core_mechanisms/Events
    Core_mechanisms/ECOS_WebAPI
    Core_mechanisms/Transactions
    Core_mechanisms/Content_versioning
    Core_mechanisms/external communications
