Описание отдельных микросервисов
==================================

Раздел содержит описание микросервисов Citeck: управление приложениями и артефактами, файловые хранилища, выполнение BPMN-процессов, трансформации документов, электронный документооборот и коммуникации. В статьях приведены назначение сервисов, API, параметры развёртывания и настройки.

.. note::

   Для **ecos-content** и **ecos-edi** в соответствующих статьях указано ограничение Enterprise. Доступность функций **ecos-transformations** зависит от состава и условий поставки, включая подключённые библиотеки и конвертеры.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: ECOS Applications (ecos-apps)
      :link: apps_service
      :link-type: ref

      Источники приложений и артефактов, неизменяемые ревизии, политики загрузки и доставка конфигураций в микросервисы.

   .. grid-item-card:: Content-микросервис
      :link: content_service
      :link-type: ref

      S3-совместимые хранилища, маршрутизация контента, потоковая и чанковая загрузка, развёртывание и настройка.

   .. grid-item-card:: Process Engine
      :link: process
      :link-type: ref

      Выполнение BPMN-процессов на Camunda 7, архитектура, репозитории, миграции и требования к отказоустойчивости.

   .. grid-item-card:: Transformations-микросервис
      :link: transformation
      :link-type: ref

      Генерация по шаблонам, API трансформаций и настройка компонентов преобразования контента.

   .. grid-item-card:: EDI-микросервис
      :link: ecos-edi
      :link-type: ref

      Юридически значимый электронный документооборот с контрагентами, подключение и настройка сервиса.

   .. grid-item-card:: Коммуникации (ecos-ecom)
      :link: ecom_service
      :link-type: ref

      Обработка входящей почты CRM и Service Desk, почтовые активности и операции объединения записей CRM.

.. toctree::
    :maxdepth: 2
    :hidden:

    Ms_description/Apps_microservice
    Ms_description/Content_microservice
    Ms_description/Process_Engine
    Ms_description/Transformations_microservice
    Ms_description/EDI_microservice
    Ms_description/ecom
