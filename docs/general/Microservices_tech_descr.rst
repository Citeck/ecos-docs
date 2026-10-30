Описание отдельных микросервисов
==================================

Платформа Citeck реализована на основе микросервисной архитектуры. Каждый микросервис решает обособленную задачу и взаимодействует с остальными через стандартизированные API. В данном разделе приведено техническое описание отдельных микросервисов платформы: их назначение, принципы работы, параметры развёртывания и особенности настройки.

.. note::

   Микросервисы **ecos-content**, **ecos-transformations** и **ecos-edi** доступны только в Enterprise-версии платформы.

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: ECOS Applications (ecos-apps)
      :link: apps_service
      :link-type: ref

      Деплой и версионирование артефактов платформы, доставка их между микросервисами.

   .. grid-item-card:: Content-микросервис
      :link: content_service
      :link-type: ref

      Хранение файлов системы, поддержка нескольких файловых хранилищ.

   .. grid-item-card:: Process Engine
      :link: process
      :link-type: ref

      Управление жизненным циклом BPMN-процессов на базе Camunda.

   .. grid-item-card:: Transformations-микросервис
      :link: transformation
      :link-type: ref

      Генерация документов по шаблонам.

   .. grid-item-card:: EDI-микросервис
      :link: ecos-edi
      :link-type: ref

      Функционал ЮЗДО (электронный документооборот с контрагентами).

.. toctree::
    :maxdepth: 2
    :hidden:

    Ms_description/Apps_microservice
    Ms_description/Content_microservice
    Ms_description/Process_Engine
    Ms_description/Transformations_microservice
    Ms_description/EDI_microservice