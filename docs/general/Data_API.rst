.. _data_api_main:

Работа с данными
=================

Раздел описывает инструменты и API платформы Citeck для работы с данными: получение, запись, фильтрация и расширение атрибутов сущностей.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Records API
      :link: records_api
      :link-type: ref

      Единый интерфейс для доступа к данным системы из браузера, мобильного приложения, микросервисов и других потребителей.

   .. grid-item-card:: Миксины
      :link: mixins
      :link-type: ref

      Механизм расширения атрибутивного состава записей из любой части системы.

   .. grid-item-card:: Язык предикатов
      :link: ecos-predicate_main
      :link-type: ref

      Язык запросов для фильтрации и поиска записей на стороне frontend и backend.

   .. grid-item-card:: Системные атрибуты
      :link: system_attributes
      :link-type: ref

      Зарезервированные атрибуты платформы, доступные для любой сущности.

   .. grid-item-card:: Citeck Data
      :link: ecos_data_main
      :link-type: ref

      Библиотека для создания Records DAO с хранением данных в БД.

.. toctree::
    :maxdepth: 2
    :hidden:

    Data_API/ECOS_Records
    Data_API/mixins
    Data_API/Язык_предикатов
    Data_API/System_attributes
    Data_API/ecos_data