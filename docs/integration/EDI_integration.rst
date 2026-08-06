.. _edi_integration:

Интеграция с ЭДО провайдерами
==============================

Citeck поддерживает интеграцию с провайдерами электронного документооборота (ЭДО) для обмена юридически значимыми документами. Платформа предоставляет набор библиотек
и модулей для подключения к таким провайдерам, как Контур.Диадок, СБИС и другим.
Интеграция позволяет отправлять, получать и обрабатывать электронные документы, управлять контрагентами и настраивать серверное подписание. В данном разделе описана
архитектура интеграции, библиотеки для работы с конкретными провайдерами и порядок добавления нового провайдера.

.. grid:: 1
    :gutter: 2

    .. grid-item-card:: EDI
        :link: edi
        :link-type: ref

        Архитектура интеграции: механизм синхронизаций, ключевые сервисы и интерфейсы ecos-edi-commons, структура события Event.

    .. grid-item-card:: Настройка получения событий с ящиком Контур.Диадок
        :link: events_kontur
        :link-type: ref

        Пошаговая настройка DataSource, Credentials, ящика ЭДО и синхронизации на примере Контур.Диадок.

    .. grid-item-card:: Синхронизация данных контрагентов и их ящиков с Контур.Диадок
        :link: counterparty_kontur
        :link-type: ref

        Логика синхронизации контрагентов, устройство обрабатывающего бандла и настройка синхронизации.

    .. grid-item-card:: Реализация интеграции с новым ЭДО-провайдером
        :link: new_provider
        :link-type: ref

        Что нужно реализовать и зарегистрировать со стороны бандла провайдера, связующей либы и хранилки (альфреско).

    .. grid-item-card:: Описание ecos-edi-kontur-lib
        :link: ecos-edi-kontur-lib
        :link-type: ref

        Либа интеграции с сервисами Контур.Диадок и Контур.EDI.

    .. grid-item-card:: Описание ecos-edi-ftps-lib
        :link: ecos-edi-ftps-lib
        :link-type: ref

        Обмен EDI-сообщениями с контрагентами через FTP/FTPS-сервер: настройка, отправка и получение сообщений.

    .. grid-item-card:: Описание ecos-edi-sbis-lib
        :link: ecos-edi-sbis-lib
        :link-type: ref

        Либа интеграции с Тензор.СБИС.

    .. grid-item-card:: Общая библиотека для обработки EDI событий ecos-edi-integration
        :link: common_lib
        :link-type: ref

        Camel-контекст, принимающий события от всех провайдеров, для обработки их непосредственно в Citeck.

    .. grid-item-card:: Серверное подписание
        :link: server_signing
        :link-type: ref

        Серверное подписание документов ЭЦП без плагина КриптоПро: схема работы, REST API, настройка keycloak.

    .. grid-item-card:: Конфигурация ЭДО
        :link: edi_rc2_configuration
        :link-type: ref

        Актуальная конфигурация ЭДО в системном журнале "Конфигурация EDI".

.. toctree::
    :maxdepth: 3
    :hidden:

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
