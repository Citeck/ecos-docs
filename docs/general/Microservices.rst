Разработка и создание микросервисов Citeck
===========================================

.. _mcs_develop_setup:

Citeck предоставляет инструменты и SDK для разработки собственных микросервисов, расширяющих функциональность платформы. Обычно микросервис представляет собой Spring Boot приложение, которое интегрируется с инфраструктурой Citeck через
набор библиотек (ecos-webapp-lib и др.). 

Микросервисы взаимодействуют с платформой через Records API и систему команд, что позволяет добавлять собственную бизнес-логику и интеграции.

Раздел включает следующие темы:

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Демо микросервис
      :link: demo_microservice
      :link-type: ref

      Эталонный микросервис ecos-demo-app с примерами реализации ключевых механизмов платформы.

   .. grid-item-card:: Создание нового микросервиса
      :link: mcs_setup
      :link-type: ref

      Руководство по разработке собственного микросервиса с нуля.

   .. grid-item-card:: Тестирование с WorkspaceApiMock
      :link: testing_workspace_api
      :link-type: ref

      Мок WorkspaceWebApi для тестирования сервисов, работающих с рабочими пространствами.

.. toctree::
    :maxdepth: 3
    :hidden:

    Microservices/demo_microservice
    Microservices/new_microservice
    Microservices/testing_workspace_api
