Быстрый запуск Citeck Community
---------------------------------

.. _quick_start:

1. Убедитесь, что установлены следующие необходимые компоненты и соблюдены требования к ОЗУ:

    - Установлен `Docker <https://docs.docker.com/get-docker/>`_
    - **16 ГБ** ОЗУ для корректной работы Docker

2. Запустите Docker.
3. Скачайте актуальный дистрибутив **citeck-launcher** для вашей операционной системы со `страницы релизов <https://github.com/Citeck/citeck-launcher/releases>`_ и запустите.

.. note::

    При установке на Windows, если **SmartScreen** предотвратил запуск приложения, то нажмите **«Запустить в любом случае»**:

     .. image:: _static/01.png
         :width: 300
         :align: center

3. Для быстрого запуска Citeck Community:

    - с предзаполненными :ref:`демонстрационными данными<ecos_modules>` - нажмите **Quick Start With Demo Data**:

        .. image:: _static/fast_start.png
            :width: 600
            :align: center

    - без демонстрационных данных - нажмите **Quick Start Without Demo Data**.

 Дождитесь загрузки и проверки данных:

    .. image:: _static/data_load.png
        :width: 600
        :align: center

4. 

.. list-table::
      :widths: 20 20
      :align: center

      * - | Нажмите **Update&Start**:       

            .. image:: _static/starting.png
                  :width: 600
                  :align: center

        - | Начнется скачивание и разворачивание образов:

            .. image:: _static/pulling.png
                  :width: 600
                  :align: center

5. Дождитесь статуса **Running** всех микросервисов и приложений и нажмите **Open In Browser**:

.. image:: _static/open.png
    :width: 600
    :align: center

6. 

.. list-table::
      :widths: 20 20
      :align: center

      * - | Войдите в систему, используя следующие учётные данные **admin/ admin**:

            .. image:: _static/page_01.png
                  :width: 350
                  :align: center

        - | При первом развертывании keycloak попросит сменить пароль:

            .. image:: _static/page_02.png
                  :width: 350
                  :align: center


7.  Далее по адресу http://localhost/ откроется страница :ref:`персонального рабочего пространства<ws_personal>`:

.. image:: _static/page_04.png
    :width: 700
    :align: center

.. note::

    При первом запуске в течение первых 5 минут после успешной установки и входа в систему может возникать ошибка:

     .. image:: _static/page_05.png
         :width: 300
         :align: center

    Развертывание и запуск Citeck продолжается, необходимо подождать.

В левом верхнем углу доступна кнопка для выбора доступных рабочих пространств и создания нового:

.. image:: _static/page_03.png
    :width: 450
    :align: center

Подробно о: 

    * :ref:`рабочих пространствах<workspaces>`; 
    * :ref:`корпоративном портале<corp_portal>`;
    * :ref:`модулях и учетных записях<ecos_modules>`; 
    * :ref:`разделе администратора<admin>`.

