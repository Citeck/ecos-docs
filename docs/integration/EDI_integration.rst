Интеграция с ЭДО провайдерами
==============================

.. _edi_integration:

Citeck поддерживает интеграцию с провайдерами электронного документооборота (ЭДО)
для обмена юридически значимыми документами. Платформа предоставляет набор библиотек
и модулей для подключения к таким провайдерам, как Контур.Диадок, СБИС и другим.
Интеграция позволяет отправлять, получать и обрабатывать электронные документы,
управлять контрагентами и настраивать серверное подписание. В данном разделе описана
архитектура интеграции, библиотеки для работы с конкретными провайдерами
и порядок добавления нового провайдера.

.. toctree::
    :maxdepth: 3

    EDI_integration/EDI
    EDI_integration/events_kontur
    EDI_integration/counterparty_kontur
    EDI_integration/new_provider
    EDI_integration/ecos-edi-kontur-lib
    EDI_integration/ecos-edi-ftps-lib
    EDI_integration/ecos-edi-sbis-lib
    EDI_integration/common_lib
    EDI_integration/server_signing
    EDI_integration/4_RC2+_configuration
