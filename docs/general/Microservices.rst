Разработка и создание микросервисов Citeck
===========================================

.. _mcs_develop_setup:

Citeck предоставляет библиотеки для создания Spring Boot приложений, которые расширяют платформу через Records API, команды и события. Раздел помогает подготовить собственный микросервис, изучить примеры ecos-demo-app и настроить тесты компонентов, зависящих от рабочих пространств.

Раздел включает следующие темы:

.. grid:: 1
   :gutter: 3

   .. grid-item-card:: Демо микросервис
      :link: demo_microservice
      :link-type: ref

      Учебное приложение ecos-demo-app: Records DAO, UI-действия, команды и фоновые задачи.

   .. grid-item-card:: Создание нового микросервиса
      :link: mcs_setup
      :link-type: ref

      Выбор базового проекта, подключение библиотек и настройка интеграции Spring Boot приложения с Citeck.

   .. grid-item-card:: Тестирование с WorkspaceApiMock
      :link: testing_workspace_api
      :link-type: ref

      Подмена WorkspaceWebApi в Spring-тестах без запущенного ecos-model и ожидания его доступности.

.. toctree::
    :maxdepth: 3
    :hidden:

    Microservices/demo_microservice
    Microservices/new_microservice
    Microservices/testing_workspace_api
