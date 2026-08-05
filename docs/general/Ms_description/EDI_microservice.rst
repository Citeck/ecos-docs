.. _ecos-edi:

EDI микросервис
=================

.. note::

    Доступно только в Enterprise версии.

Микросервис, отвечающий за функционал ЮЗДО.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Подключение микросервиса ecos-edi локально
      :link: edi_deployment
      :link-type: ref

      Развёртывание ecos-edi в docker для локальной разработки.

   .. grid-item-card:: Настройка синхронизации и конфигурация
      :link: edi_configuration
      :link-type: ref

      Настройка ящиков и синхронизаций с провайдерами diadoc и sbis.

   .. grid-item-card:: API запросы ecos-edi
      :link: edi_api_request
      :link-type: ref

      Справочник запросов к record dao ``edi-action``.

.. toctree::
    :maxdepth: 2
    :hidden:

    EDI_microservice/deployment
    EDI_microservice/configuration
    EDI_microservice/API_request

