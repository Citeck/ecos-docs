.. _core-mechanisms:

Механизмы платформы
=====================

В данном разделе описаны ключевые механизмы платформы Citeck, обеспечивающие взаимодействие компонентов, интеграцию с внешними системами и надёжную работу бизнес-логики.

Раздел включает следующие темы:

- :ref:`Команды <ecos_commands>` — механизм декларативного вызова действий над записями платформы.
- :ref:`События <ecos_events>` — система публикации и подписки на события внутри платформы.
- :ref:`Citeck WebAPI <ecos-webapi>` — REST-интерфейс для работы с данными и сервисами платформы.
- :ref:`Транзакции <ecos-transactions>` — управление транзакционностью операций на основе двухфазного коммита.
- :ref:`Внешние коммуникации <external-communications>` — настройка каналов уведомлений (email, Telegram и др.).

.. toctree::
    :maxdepth: 4
    :hidden:

    Core_mechanisms/Commands.rst
    Core_mechanisms/Events.rst
    Core_mechanisms/ECOS_WebAPI.rst
    Core_mechanisms/Transactions.rst
    Core_mechanisms/external communications.rst