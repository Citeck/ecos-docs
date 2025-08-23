Готовые функциональные модули
==============================

.. _ecos_modules:

.. note:: 

    С релиза 2025.1.3 функциональные модули распределены по :ref:`рабочим пространствам<workspaces>`.

.. list-table:: 
      :widths: 20 5
      :header-rows: 1
      :class: tight-table 

      * - **Рабочее пространство**
        - **Модули в его составе**

      * - | **Делопроизводство**
          | Пространство для управления распорядительной документацией, обработкой входящей и исходящей корреспонденции, а также организации и документирования совещаний и их итогов.

            .. image:: _static/paperwork_space.png
                :width: 700
                :align: center

        - | :ref:`Внутренние документы<ecos-order-ORD>`
          | :ref:`Входящие документы<ecos-indoc>`
          | :ref:`Исходящие документы<ecos-outdoc>`
          | :ref:`Работа с документами ЭДО<EDI_in_out>`
          | :ref:`Совещания<ecos-meetings>`
          | :ref:`Поручения<ecos-assignments>`

      * - | **Договоры**
          | Пространство для работы с договорными документами. 

            .. image:: _static/contracts_space.png
                :width: 700
                :align: center

        - | :ref:`Договоры<ecos-contract>`
          | :ref:`Работа с документами ЭДО<EDI_in_out>`
          | :ref:`Поручения<ecos-assignments>`

      * - | **Service desk**
          | Пространство для работы с клиентскими обращениями (заявками) и сбора аналитики по работе технической поддержки.

            .. image:: _static/sd_space.png
                :width: 700
                :align: center

        - | :ref:`Service desk<ecos-service-desk>`
          | :ref:`Учет времени<ecos-worklog>`

      * - | **Рекрутинг**
          | Пространство для выполнения задач по подбору персонала по заявкам подразделений.

            .. image:: _static/hr_space.png
                :width: 700
                :align: center

        - | :ref:`Офферы<ecos-offer>`
          | :ref:`Поручения<ecos-assignments>`

      * - | **CRM**
          | Пространство для работы с лидами, клиентами, ведения сделок.

            .. image:: _static/crm_space.png
                :width: 700
                :align: center

        - | :ref:`CRM<ecos-crm>`
          | :ref:`Поручения<ecos-assignments>`

      * - | **Справочники**
          | Пространство содержит основные справочники, данные из которых используются при создании большинства документов системы.

            .. image:: _static/datalist_space.png
                :width: 700
                :align: center

        - | :ref:`Справочники<datalists>`

      * - | **Корпоративный портал**
          | Пространство предоставляет доступ к материалам компании, новостям и базам знаний, а также поддерживает основные рабочие процессы

            .. image:: _static/corp_space.png
                :width: 700
                :align: center

        - | :ref:`Корпоративный портал<corp_portal>`
          | :ref:`Заявления на отпуск<ecos-vacation>`
          | :ref:`Пропуска<ecos-order-pass>`

      * - | **Рабочее пространство проекта**
          | Пространство для управления проектом, организации рабочего процесса команды, мониторинга задач.

            .. image:: _static/project_space.png
                :width: 700
                :align: center

        - | :ref:`Project tracker<ecos_ept>`
          | :ref:`Релизы<ecos-releases>`
          | :ref:`Учет времени<ecos-worklog>`

.. note:: 

   Экземпляры типов данных **CRM**, **Договоры** и **Service desk** - приватные, т.е.  доступны в рамках рабочего пространства, в котором созданы.

.. _demo_accounts:

Установите **Citeck Community** любым из описанных ниже способов: 

    * :ref:`Развертывание Citeck с использованием кросплатформенного лончера <quick_start>`; 
    * :ref:`Установка Citeck c помощью Docker Compose<docker_compose>`;
    * :ref:`Развертывание виртуальной машины с Citeck в VirtualBOX <virtualbox>`

и воспользуйтесь следующими учетными записями для работы:

.. list-table:: 
      :widths: 10 10 10 10 10
      :header-rows: 1
      :class: tight-table 

      * - Подразделение	
        - Роль	
        - Рабочее пространство	
        - Роль в пространстве	
        - Пользователь
      * - **Руководители**
        - Генеральный директор 
        - | Рекрутинг
          | Договоры 
        - | Менеджер
          | Менеджер
        - avraam.libertov 
      * - 
        - Коммерческий директор  
        - CRM
        - Менеджер
        - elvira.danilenko 
      * - 
        - Директор по производству 
        - Рекрутинг
        - Менеджер
        - pavel.elbrusov
      * - **Бухгалтерия**
        - Главный бухгалтер
        - | Рекрутинг
          | Договоры 
        - | Пользователь
          | Пользователь
        - ekaterina.dudina
      * - 
        - Бухгалтер 
        - | Рекрутинг
          | Договоры 
        - | Пользователь
          | Пользователь
        - alexandra.filchenko 
      * - **Отдел продаж и маркетинга**
        - Маркетолог
        - CRM
        - Пользователь
        - boris.alexeev
      * - 
        - Специалист отдела продаж
        - CRM
        - Пользователь
        - veniamin.ivanov
      * - **Делопроизводители**
        - Делопроизводитель
        - | Делопроизводство
          | Договоры 
        - | Менеджер
          | Пользователь
        - elizaveta.kim
      * - 
        - Делопроизводитель
        - | Делопроизводство
          | Договоры 
        - | Менеджер
          | Пользователь
        - alia.tarasova
      * - **Отдел кадров**
        - Руководитель отдела
        - Рекрутинг
        - Пользователь
        - alexey.kozlovskiy
      * - 
        - Специалист отдела продаж
        - Рекрутинг
        - Пользователь
        - eva.zaoblachnaya
      * - **Отдел технической поддержки**
        - Руководитель отдела
        - Service Desk
        - Менеджер
        - yaroslav.staroverov
      * - 
        - 1 линия ТП
        - Service Desk
        - Пользователь
        - evgenia.makarenko
      * - 
        - 2 линия ТП
        - Service Desk
        - Пользователь
        - petr.frolov
      * - 
        - 3 линия ТП
        - Service Desk
        - Пользователь
        - luka.muradov
      * - **Юридический отдел**
        - Юрист
        - Договоры
        - Пользователь
        - fedor.shishkin
      * - 
        - Юрист
        - Договоры
        - Пользователь
        - victor.drozdov

Пароль для всех пользователей: **123**

Предзаполннный пример :ref:`персонального рабочего пространства<ws_personal>` доступен для пользователя **elvira.danilenko**.

Предзаполннный пример :ref:`совместного рабочего пространства<ws_collaborative>` доступен для пользователей **elvira.danilenko** и **pavel.elbrusov**.

:ref:`Корпоративный портал<corp_portal>` доступен для всех пользователей.


.. toctree::
    :hidden:

    ecos_modules/ORD
    ecos_modules/tasks
    ecos_modules/contract
    ecos_modules/edo
    ecos_modules/InDoc
    ecos_modules/OutDoc
    ecos_modules/crm_new
    ecos_modules/service_desk
    ecos_modules/meeting
    ecos_modules/offer
    ecos_modules/order_pass
    ecos_modules/poa
    ecos_modules/vacation   
    ecos_modules/ept
    ecos_modules/releases
    ecos_modules/worklog
    ecos_modules/portal_sd   
    
