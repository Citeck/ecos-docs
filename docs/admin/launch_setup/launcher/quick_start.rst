.. _quick_start:

Быстрый запуск Citeck
=====================

1. Убедитесь, что установлены необходимые компоненты:

   - Установлен `Docker <https://docs.docker.com/get-docker/>`_
   - Не менее **16 ГБ** ОЗУ для Community, **24–32 ГБ** для Enterprise
   - Дополнительно около **1 ГБ** ОЗУ при использовании S3-хранилища SeaweedFS
   - Не менее **50 ГБ** свободного места на диске для образов и данных

2. Запустите **Docker**.

   .. note::

       По умолчанию Windows выделяет 50 % общей памяти для WSL 2. Для увеличения объёма воспользуйтесь `инструкцией <https://learn.microsoft.com/ru-ru/windows/wsl/wsl-config#configuration-settings-for-wslconfig>`_.

3. Скачайте и установите актуальный пакет **citeck-desktop_<version>_<os>_<arch>** для вашей ОС и архитектуры **amd64** или **arm64** со `страницы релизов <https://github.com/Citeck/citeck-launcher/releases>`_:

   - **.msi** — для Windows
   - **.deb** или **.rpm** — для Linux
   - **.dmg** — для macOS

   .. note::

       При установке на Windows, если **SmartScreen** предотвратил запуск приложения, нажмите **«Подробнее»**, а затем **«Выполнить в любом случае»**:

       .. image:: _static/01.png
           :width: 300
           :align: center

   .. note::

       На macOS неавторизованное приложение может вызвать предупреждение о непроверенном разработчике. Для первого запуска нажмите на приложение правой кнопкой мыши и выберите **Открыть** либо разрешите запуск в **Системные настройки → Конфиденциальность и безопасность → Всё равно открыть**.

4. Запустите **Citeck Launcher**:

   .. image:: _static/01_1.png
       :width: 400
       :align: center

5. Выберите вариант запуска **Citeck**:

   Доступные варианты и их названия определяются выбранным workspace. Например:

   - с предзаполненными :ref:`демонстрационными данными <ecos_modules>` — нажмите **Quick Start With Demo Data**:

     .. image:: _static/fast_start.png
         :width: 600
         :align: center

   - без демонстрационных данных — нажмите **Quick Start Without Demo Data**.

   Дождитесь загрузки и проверки данных:

   .. image:: _static/data_load.png
       :width: 600
       :align: center

.. dropdown:: Enterprise: ввод учётных данных Harbor
   :color: secondary

   При установке Enterprise версии для скачивания закрытых образов необходимо ввести учетные данные:

   .. grid:: 2
      :gutter: 2

      .. grid-item::

         .. image:: _static/harbor_1.png
            :width: 350
            :align: center

      .. grid-item::

         .. image:: _static/harbor_2.png
            :width: 350
            :align: center

6. Скачивание и разворачивание образов начнётся автоматически:

   .. image:: _static/pulling.png
       :width: 700
       :align: center

7. Дождитесь статуса **Работает** всех микросервисов и приложений, затем нажмите **Открыть в браузере**:

   .. image:: _static/open.png
       :width: 700
       :align: center

8. Войдите в систему:

   .. grid:: 2
       :gutter: 2

       .. grid-item::

          Используйте учётные данные **admin / admin**:

          .. image:: _static/page_01.png
              :width: 350
              :align: center

       .. grid-item::

          При первом развёртывании Keycloak может потребовать сменить пароль. Это зависит от настроек выбранной поставки и данных:

          .. image:: _static/page_02.png
              :width: 350
              :align: center

9. По ссылке **Открыть в браузере** откроется страница :ref:`персонального рабочего пространства <ws_personal>`. По умолчанию используется http://localhost/. После включения HTTPS или изменения настроек прокси используйте адрес, который открывает Launcher:

   .. image:: _static/page_04.png
       :width: 700
       :align: center

   .. note::

       Во время первого запуска приложения могут быть ещё не готовы принимать запросы. Дождитесь завершения развёртывания; если ошибки сохраняются, проверьте статусы и логи приложений в Launcher:

       .. image:: _static/page_05.png
           :width: 300
           :align: center

|

В левом верхнем углу доступна кнопка для выбора рабочего пространства и создания нового:

.. grid:: 2
   :gutter: 2

   .. grid-item::

      .. image:: _static/page_03.png
         :width: 500
         :align: center

   .. grid-item::

      .. image:: _static/page_03_1.png
         :width: 500
         :align: center


.. note::

    Для экономии ресурсов можно остановить микросервис **onlyoffice** и изменить аутентификацию с Keycloak на **basic**.

Подробно о:

- :ref:`модулях и учётных записях <ecos_modules>`;
- :ref:`рабочих пространствах <workspaces>`;
- :ref:`корпоративном портале <corp_portal>`;
- :ref:`разделе администратора <admin>`.
