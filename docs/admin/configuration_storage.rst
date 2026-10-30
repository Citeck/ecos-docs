Конфигурация и хранилище
=========================

Раздел охватывает два аспекта инфраструктуры Citeck: управление конфигурацией приложений и настройку хранилищ контента.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Конфигурация
      :link: configuration
      :link-type: ref

      Системный и административный уровни настройки платформы — от параметров подключения к базам данных до конфигурации, управляемой через интерфейс Citeck с использованием Spring Cloud Config.

   .. grid-item-card:: Хранилище
      :link: s3_storage
      :link-type: ref

      Настройка S3-совместимого хранилища контента для Enterprise-версии платформы.

.. toctree::
    :maxdepth: 2
    :hidden:

    configuration_storage/configuration
    configuration_storage/s3_storage
