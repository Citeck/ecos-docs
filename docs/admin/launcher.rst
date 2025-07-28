Кросплатформенный лончер для запуска Citeck
=============================================

.. _citeck_launcher:


Возможности:

 • Быстрый локальный запуск Citeck Community одной кнопкой с демонстрационными данными и без них
 • Разворачивание приватных комплектов в отдельных рабочих пространствах для разработки

.. contents::
    :depth: 3

Системные требования
---------------------

.. tabs::

   .. tab:: Windows   

     * Windows 11 64bit: Home, Pro, Enterprise или Education версии 21H2 или выше.
     * Windows 10 64bit: Home или Pro 21H1 (сборка 19043) или выше, Enterprise или Education 20H2 (сборка 19042) или выше
     * Включите функцию WSL 2 в Windows. Подробные инструкции см. `в документации Microsoft <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_.
     * Для успешного запуска WSL 2 в Windows 10 или Windows 11 необходимы следующие предварительные требования к оборудованию:

       * 64-битный процессор с трансляцией адресов второго уровня (`SLAT <https://en.wikipedia.org/wiki/Second_Level_Address_Translation>`_)
       * Не менее 16 ГБ оперативной памяти.
       * 80 Гб свободного дискового пространства.
       * Поддержка аппаратной виртуализации на уровне BIOS должна быть включена в настройках BIOS. Дополнительные сведения см. `в разделе Виртуализация <https://docs.docker.com/desktop/troubleshoot/topics/#virtualization>`_

     * Загрузить и установить `пакет обновления ядра Linux <https://docs.microsoft.com/windows/wsl/wsl2-kernel>`_

    `Официальное руководство по установке Docker на Windows <https://docs.docker.com/desktop/install/windows-install/>`_

   .. tab:: Linux   

     * Поддержка 64-битного ядра и процессора для виртуализации.
     * Поддержка виртуализации KVM. Следуйте `инструкциям поддержки виртуализации KVM <https://docs.docker.com/desktop/install/linux-install/#kvm-virtualization-support>`_ для проверки включены или нет модули ядра KVM и как предоставить доступ к устройству kvm.
     * QEMU должен быть версии 5.2 или новее. Рекомендуем обновиться до последней версии.
     * Подсистема инициализации и управления службами systemd.
     * Gnome или среда рабочего стола KDE.
     * Не менее 16 ГБ оперативной памяти.
     * 80 Гб свободного дискового пространства.
     * Включите настройку сопоставления идентификаторов в пространствах имен пользователей, см. `Общий доступ к файлам <https://docs.docker.com/desktop/install/linux-install/#file-sharing>`_

    `Официальное руководство по установке Docker на Linux <https://docs.docker.com/desktop/install/linux-install/>`_

    `Официальное руководство по установке Docker на Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_

   .. tab:: MacOS   

     * MacOS версии 10.15 или выше.
     * Не менее 16 ГБ оперативной памяти.
     * 80 Гб свободного дискового пространства.

    `Официальное руководстов по установке Docker на MacOS <https://docs.docker.com/desktop/install/mac-install/>`_


Установка и запуск проекта
---------------------------

Установите `Docker <https://docs.docker.com/get-docker/>`_ на Вашу ОС.

Скачайте (ссылка) для вашей операционной системы дистрибутив **citeck-launcher**

 - Windows ...
 - Debian, Ubuntu ...
 - Mac ...

и запустите.

.. note::

    При установке на Windows, если **SmartScreen** предотвратил запуск приложения, то нажмите **«Запустить в любом случае»**:

     .. image:: _static/launcher/01.png
         :width: 300
         :align: center

Для быстрого запуска **Citeck Community** с предзаполненными :ref:`демонстрационными данными<ecos_modules>` нажмите **Quick Start With Demo Data**:

.. image:: _static/launcher/fast_start.png
    :width: 600
    :align: center

.. note::

    Для запуска без :ref:`демонстрационных данных<ecos_modules>` нажмите **Quick Start Without Demo Data**.

См. подробно о создании :ref:`нового пространства имен (namespace)<launcher_new_space>`

.. note::

    На странице загрузки можно посмотреть логи и выгрузить состояние системы на случай проблем:

     .. image:: _static/launcher/loading.png
         :width: 600
         :align: center

Дождитесь загрузки и проверки данных:

.. image:: _static/launcher/data_load.png
    :width: 600
    :align: center

Нажмите **Update&Start**:

.. image:: _static/launcher/starting.png
    :width: 600
    :align: center

Начнется скачивание и разворачивание образов:

.. image:: _static/launcher/pulling.png
    :width: 600
    :align: center

Дождитесь статуса **Running** всех микросервисов и приложений и нажмите **Open In Browser**:

.. image:: _static/launcher/open.png
    :width: 600
    :align: center

Войдите в систему, используя следующие учётные данные:

.. code-block::

    Username: admin
    Password: admin

.. image:: _static/launcher/page_01.png
    :width: 350
    :align: center

При первом развертывании keycloak попросит сменить пароль:

.. image:: _static/launcher/page_02.png
    :width: 350
    :align: center

Далее станет доступна страница :ref:`персонального рабочего пространства<ws_personal>`:

.. image:: _static/launcher/page_04.png
    :width: 700
    :align: center

В левом верхнем углу доступна кнопка для выбора доступных рабочих пространств и создания нового:

.. image:: _static/launcher/page_03.png
    :width: 450
    :align: center

Подробно о: 

    * :ref:`рабочих пространствах<workspaces>`; 
    * :ref:`корпоративном портале<corp_portal>`;
    * :ref:`разделе администратора<admin>`.

.. note::

    При первом запуске в течение первых 5 минут после успешной установки и входа в систему может возникать ошибка:

     .. image:: _static/launcher/page_05.png
         :width: 300
         :align: center

    Развертывание и запуск Citeck продолжается, необходимо подождать.


Описание интерфейса
----------------------

При первом запуске доступны установка Citeck Community с :ref:`демонстрационными данными<ecos_modules>` **(a)**, без демо данных **(b)** создание иного пространства имен для разворачивания Citeck **(с)**:

.. image:: _static/launcher/namespaces.png
    :width: 600
    :align: center

После успешного запуска будет отображаться список доступных namespace:

.. image:: _static/launcher/namespaces_1.png
    :width: 600
    :align: center

|

.. image:: _static/launcher/overview.png
    :width: 600
    :align: center

1. **Запускаемые микросервисы и приложения**: микросервисы ядра, приложения Citeck, сторонние, статус. Доступные действия:

    - **1a** – остановить/запустить
    - **1b** – лог микросервиса
    - **1c** – настройка микросервиса/приложения вручную:

.. image:: _static/launcher/ms_settings.png
    :width: 500
    :align: center

2. **Обновить/ запустить** все микросервисы и приложения. При клике правой кнопкой мыши доступно действие **Force Update And Start** для принудительного обновления данных из git репозиториев с конфигурацией рабочего пространства и bundle (китов):

.. image:: _static/launcher/force_update.png
    :width: 250
    :align: center

3. **Остановка** всех микросервисов и приложений.
4. Актуальный **статус** процесса разворачивания.
5. **Открыть Citeck в браузере** (только для статуса Running).
6. Доступ к **сопутствующим сервисам**. Открываются в браузере в отдельной вкладке.

    -	**Keycloak Admin** – интерфейс управления Keycloak, системой управления идентификацией и авторизацией.
    -	**Spring Boot Admin** – :ref:`интерфейс <spring_boot_admin>` для мониторинга и администрирования Spring Boot-приложений, предоставляет удобный интерфейс для просмотра состояния, метрик, логов и управления Spring Boot-приложениями.
    -	**PG Admin** - интерфейс для администрирования и управления базами данных PostgreSQL.
    -	**MailHog** – интерфейс инструмента для тестирования и отладки электронной почты во время разработки, предоставляет удобный веб-интерфейс для их просмотра, без реальной отправки на почтовые серверы.
    -	**RabbitMQ** – интерфейс брокер сообщений (message broker), который обеспечивает асинхронный обмен данными между компонентами распределённых систем.

7. Переход в **директорию лончера** (папка с логами, данными конфигурации, рабочими пространствами).
8. Открыть **лог** лончера.
9. **Список volumes**, которые используются. Их можно очистить:

    .. image:: _static/launcher/volumes.png
        :width: 400
        :align: center

10. **Работа с секретами**, используемыми в лончере. Сначала необходимо задать мастер-пароль: 

    .. image:: _static/launcher/secret_1.png
        :width: 400
        :align: center

 См. подробно о работе с :ref:`секретами<launcher_secrets>`

11.  **Экспорт информации о системе** (выгрузка данных о системе, информации о билде, экспорт thread dump).
12.  **Настройки пространства имен**. См. подробно о настройках :ref:`пространства имен (namespace)<launcher_new_space>`

    .. image:: _static/launcher/namespace_settings.png
        :width: 400
        :align: center



Создание нового пространства имен
----------------------------------

.. _launcher_new_space:

Для запуска другого комплекта поставки создайте новый namespace. Нажмите **Create New Namespace**.

.. image:: _static/launcher/new_namespace.png
    :width: 600
    :align: center

Укажите **имя**, выберите **вариант поставки**, **версию поставки**, **снэпшот данных**, **вид авторизации**:

.. image:: _static/launcher/new_namespace_1.png
    :width: 500
    :align: center

Нажмите **Confirm**. 

Если выбираете снэпшот данных, то дождитесь загрузки и проверки данных:

.. image:: _static/launcher/new_namespace_1_1.png
    :width: 600
    :align: center

Для запуска нажмите **Update&Start**:

.. image:: _static/launcher/new_namespace_2.png
    :width: 600
    :align: center

Введите мастер пароль или установите его, если не установили ранее:

.. image:: _static/launcher/new_namespace_2_1.png
    :width: 400
    :align: center

Введите пароль для скачивания закрытых образов:

.. image:: _static/launcher/new_namespace_3.png
    :width: 400
    :align: center

Далее процесс аналогичен запуску версии Community:

.. image:: _static/launcher/new_namespace_4.png
    :width: 600
    :align: center


Работа с секретами и мастер паролем
-------------------------------------

.. _launcher_secrets:

Для работы с секретами, используемыми для запуска Citeck, кликните:

.. image:: _static/launcher/secret_0.png
    :width: 600
    :align: center


Установка мастер пароля
~~~~~~~~~~~~~~~~~~~~~~~~~

Введите и подтвердите мастер пароль:

.. image:: _static/launcher/secret_1.png
    :width: 400
    :align: center


Просмотр и удаление секретов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Для просмотра списка введите пароль:

.. image:: _static/launcher/secret_4.png
    :width: 400
    :align: center

Становится доступен список секретов с возможностью удаления:

.. image:: _static/launcher/secret_2.png
    :width: 400
    :align: center


Сброс мастер-пароля
~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    Все используемые секреты будут удалены.


.. image:: _static/launcher/reset_secret_1.png
    :width: 400
    :align: center 

Подтвердите выбор:

.. image:: _static/launcher/reset_secret_2.png
    :width: 400
    :align: center 

И введите новый мастер пароль:

.. image:: _static/launcher/reset_secret_3.png
    :width: 400
    :align: center 

Рабочие пространства
---------------------

.. image:: _static/launcher/ws_1.png
    :width: 600
    :align: center

Создание нового
~~~~~~~~~~~~~~~~

.. image:: _static/launcher/ws_2.png
    :width: 500
    :align: center  

Введите **имя**, **адрес** и **ветку репозитория**, **период обновления** в формате ISO 8601, **тип авторизации**:

.. image:: _static/launcher/ws_3.png
    :width: 500
    :align: center  

Нажмите **Confirm**.

Для типа авторизации **token** – введите `персональный access токен <https://docs.gitlab.com/user/profile/personal_access_tokens/>`_  в Gitlab и подтвердите:

.. image:: _static/launcher/ws_4.png
    :width: 500
    :align: center  

Нажмите **Confirm**. Рабочее пространство будет создано.

Выбор из созданных
~~~~~~~~~~~~~~~~~~~

.. image:: _static/launcher/ws_5_1.png
    :width: 600
    :align: center  

В списке пространство можно отредактировать, удалить. В пространстве будет доступен запуск настроенного namespace и создание нового:

.. image:: _static/launcher/ws_6.png
    :width: 600
    :align: center  