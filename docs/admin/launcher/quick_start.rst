.. _quick_start:

Быстрый запуск Citeck Community
================================

1. Убедитесь, что установлены необходимые компоненты:

   - Установлен `Docker <https://docs.docker.com/get-docker/>`_
   - Не менее **16 ГБ** ОЗУ

2. Запустите **Docker**.

   .. note::

       По умолчанию Windows выделяет 50 % общей памяти для WSL 2. Для увеличения объёма воспользуйтесь `инструкцией <https://learn.microsoft.com/ru-ru/windows/wsl/wsl-config#configuration-settings-for-wslconfig>`_.

3. Скачайте и установите актуальный дистрибутив **citeck-launcher** для вашей ОС со `страницы релизов <https://github.com/Citeck/citeck-launcher/releases>`_:

   - **.msi** — для Windows
   - **.deb** — для Linux-подобных ОС
   - **.dmg** — для macOS

   .. note::

       При установке на Windows, если **SmartScreen** предотвратил запуск приложения, нажмите **«Подробнее»**, а затем **«Выполнить в любом случае»**:

       .. image:: _static/01.png
           :width: 300
           :align: center

4. Запустите **citeck-launcher**:

   .. image:: _static/01_1.png
       :width: 400
       :align: center

5. Выберите вариант запуска **Citeck Community**:

   - с предзаполненными :ref:`демонстрационными данными <ecos_modules>` — нажмите **Quick Start With Demo Data**:

     .. image:: _static/fast_start.png
         :width: 600
         :align: center

   - без демонстрационных данных — нажмите **Quick Start Without Demo Data**.

   Дождитесь загрузки и проверки данных:

   .. image:: _static/data_load.png
       :width: 600
       :align: center

6. Скачивание и разворачивание образов начнётся автоматически:

   .. image:: _static/pulling.png
       :width: 700
       :align: center

7. Дождитесь статуса **Running** всех микросервисов и приложений, затем нажмите **Open In Browser**:

   .. image:: _static/open.png
       :width: 700
       :align: center

8. Войдите в систему:

   .. list-table::
       :widths: 50 50
       :align: center

       * - | Используйте учётные данные **admin / admin**:
           |

             .. image:: _static/page_01.png
                 :width: 350
                 :align: center

         - | При первом развёртывании без демонстрационных данных
           | Keycloak попросит сменить пароль:

             .. image:: _static/page_02.png
                 :width: 350
                 :align: center

9. По адресу http://localhost/ откроется страница :ref:`персонального рабочего пространства <ws_personal>`:

   .. image:: _static/page_04.png
       :width: 700
       :align: center

   .. note::

       В первые 5 минут после запуска могут появляться ошибки — это нормально, развёртывание продолжается:

       .. image:: _static/page_05.png
           :width: 300
           :align: center

|

В левом верхнем углу доступна кнопка для выбора рабочего пространства и создания нового:

.. image:: _static/page_03.png
    :width: 450
    :align: center

.. note::

    Для экономии ресурсов можно остановить микросервис **onlyoffice** и изменить аутентификацию с Keycloak на **basic**.

Подробно о:

- :ref:`модулях и учётных записях <ecos_modules>`;
- :ref:`рабочих пространствах <workspaces>`;
- :ref:`корпоративном портале <corp_portal>`;
- :ref:`разделе администратора <admin>`.
