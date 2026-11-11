.. _data_api_main:

Работа с данными
=================

Раздел описывает чтение и изменение записей через Records API, фильтрацию предикатами, расширение атрибутов миксинами и хранение данных в БД через Citeck Data.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Records API
      :link: records_api
      :link-type: ref

      Поиск, чтение атрибутов, создание, изменение и удаление записей. Синтаксис запросов и примеры для браузера и Java/Kotlin.

   .. grid-item-card:: Миксины
      :link: mixins
      :link-type: ref

      Вычисляемые атрибуты по типу записи, конфигураторы и условия межсервисной работы внешних миксинов.

   .. grid-item-card:: Язык предикатов
      :link: ecos-predicate_main
      :link-type: ref

      JSON-модель условий, операции сравнения, локальная проверка, поиск и отладка предикатов.

   .. grid-item-card:: Системные атрибуты
      :link: system_attributes
      :link-type: ref

      Служебные атрибуты записей: назначение, способы чтения и особенности использования.

   .. grid-item-card:: Citeck Data
      :link: ecos_data_main
      :link-type: ref

      Настройка DB-backed Records DAO, поиск по ассоциациям, группировка и ограничения SQL-функций.

.. toctree::
    :maxdepth: 2
    :hidden:

    Data_API/ECOS_Records
    Data_API/mixins
    Data_API/Язык_предикатов
    Data_API/System_attributes
    Data_API/ecos_data
