.. _docker_compose:

Установка Citeck c помощью Docker Compose
==========================================

.. contents::
    :depth: 5

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

.. important:: 

    Комплект поставляется с предзаполненными :ref:`демонстрационными данными<ecos_modules>`. 
    
    Для отключения данной настройки перед разворачиванием стенда перейдите в папку  ``\services\environments`` в файле **demo_data.env** в настройке **WITH_DEMO_DATA** укажите **false**.

    Мы анонимно собираем статистику с использованием сервиса `Umami <https://umami.is/docs>`_. Сервис не собирает и не хранит персональные данные, избегая необходимости использования файлов cookie.

*	Установите `Docker и Docker Compose <https://docs.docker.com/get-docker/>`_ на Вашу ОС
*   Клонируйте репозиторий: 

        .. code-block::

            git clone https://github.com/citeck/citeck-community.git

*	В терминале: 

    * перейдите в папку с клонированным репозиторием:

         .. code-block::

            cd полный путь до папки

    * запустите: 

         .. code-block::

            docker-compose up -d

*	Подождите некоторое время (в зависимости от мощности системы) для того, чтобы система запустилась.
*	Перейдите в браузере по адресу http://localhost/
*   Войдите в систему, используя следующие учётные данные:

    .. image:: _static/docker-compose/09.png
        :width: 600
        :align: center

    .. code-block::

        Username: admin
        Password: admin

Если необходимо сменить пароль, то `см. инструкцию  <https://www.keycloak.org/docs/latest/getting_started/index.html#creating-a-user>`_

*   Далее станет доступна страница :ref:`персонального рабочего пространства<ws_personal>`:

    .. image:: _static/docker-compose/11.png
        :width: 700
        :align: center

    В левом верхнем углу доступна кнопка для выбора доступных рабочих пространств и создания нового:

    .. image:: _static/docker-compose/11_1.png
        :width: 450
        :align: center

Подробно о: 

    * :ref:`рабочих пространствах<workspaces>`; 
    * :ref:`корпоративном портале<corp_portal>`;
    * :ref:`разделе администратора<admin>`.

.. note:: 

    При первом запуске в течение первых 5 минут после успешной установки и входа в систему может возникать ошибка:

    .. image:: _static/docker-compose/08.png
        :width: 300
        :align: center

    Развертывание и запуск Citeck продолжается, необходимо подождать.

Обновление до последнего релиза
--------------------------------

В терминале:

* Остановите Citeck:

    .. code-block::

        docker-compose down

* Перейдите в папку ``citeck-community``:

         .. code-block::

            cd полный путь до папки citeck-community

* Получите актуальную версию Citeck:

    .. code-block::

        git pull

* Загрузите последние версии образов:

    .. code-block::

        docker-compose pull

* Запустите:

    .. code-block::

        docker-compose up -d

Подготовка окружения и установка Citeck
------------------------------------------

.. tabs::

   .. tab:: CentOS 7.x   

        Обновить систему и пакеты до последней актуальной версии:

        .. code-block::

            yum update -y && yum upgrade -y

        Отключить SELinux и перезагрузить сервер:

        .. code-block::

            sed -i 's/enforcing/disabled/g' /etc/selinux/config
            reboot

        Установить Python:

        .. code-block::

            yum install epel-release -y
            yum install python3 -y && yum install python3-pip -y

        Установить пакеты для комфортной работы:

        .. code-block::

            yum install -y mc yum-utils nano ethtool ntp ntpdate firewalld lvm2 device-mapper-persistent-data htop fail2ban mc wget screen pigz

        Установить Docker Engine:

        .. code-block::

            yum-config-manager --add-repo https://http://download.docker.com /linux/centos/docker-ce.repo
            yum install -y docker-ce docker-ce-cli http://containerd.io 
            systemctl enable docker && systemctl start docker

        Установить Docker Compose:

        .. code-block::

            curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
            chmod +x /usr/local/bin/docker-compose

        В случае, если локальная сеть, может пересекаться с сетью docker, лучше предопределить подсеть docker. Сделать это можно в файле **/etc/docker/daemon.json, переменная default-address-pools**

        .. code-block::

            {
            "default-address-pools":
            [
                {"base":"172.19.0.0/16","size":24}
            ]
            }

        Следующим этапом необходимо получить комплект поставки, в который входят **docker-compose.yaml** и **environments** и поместить его на сервер.

        .. code-block::

            git clone https://github.com/citeck/citeck-community.git && cd citeck-community

        После этого в директории, куда поместили проект, выполнить:

        .. code-block::

            docker-compose pull
            docker-compose up -d

        Система будет инициализирована, и после полного запуска, будет готова к работе.

        **Настройка Proxy в Docker**
        
        Настройки прокси задаются в файле:

        .. code-block::

            /etc/systemd/system/docker.service.d/http-proxy.conf 

        Если этого файла или папки нет, нужно их создать. Содержимое файла должно быть примерно таким:

        .. code-block::

            [Service]
            Environment="HTTP_PROXY=http://<USER_NAME>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>"
            Environment="HTTPS_PROXY=http://<USER_NAME>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>"
            Environment="NO_PROXY=localhost,127.0.0.1,ecos-app, ecos-apps-app, ecos-gateway-app, ecos-history-app, ecos-identity-app, ecos-integrations-app, ecos-logger-app, ecos-microservices-postgresql-app, ecos-model-app, ecos-notifications-app, ecos-process-app, ecos-proxy-app, ecos-registry-app, ecos-search-app, ecos-uiserv-app, mailhog-app, mongodb-app, node-exporter-app, only-office-app, portainer-agent-app, postgres-exporter-app, rabbitmq-app, zookeeper-app"

        Также в раздел **NO_PROXY** можно добавить внутренние домены вашей компании (через запятую и также можно использовать звездочку например ``*.someco.com,`` ``*.someco.ru``)

        После добавления данного файла нужно перезапустить демон Docker:

        .. code-block::

            systemctl daemon-reload
            systemctl restart docker

   .. tab:: Ubuntu Server 24.04 LTS

        Установка Docker:

        .. code-block::

            sudo apt-get update
            sudo apt-get install ca-certificates curl
            sudo install -m 0755 -d /etc/apt/keyrings
            sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
            sudo chmod a+r /etc/apt/keyrings/docker.asc
            
            # Add the repository to Apt sources:
            echo \
            "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
            $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
            sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
            sudo apt-get update
            
            ## Чтобы установить последнюю доступную версию, выполните команду::
            sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
            
            ## Чтобы установить конкретную версию, выполните команду:
            apt-cache madison docker-ce | awk '{ print $3 }'
            VERSION_STRING={Your Specific version}
            sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io docker-buildx-plugin docker-compose-plugin

        Настройка docker на запуск при старте системы:

        .. code-block::

            sudo systemctl enable docker

        Установка Docker-compose:

        .. code-block::

            curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
            chmod +x /usr/local/bin/docker-compose
            Проверить:
            docker-compose --version

        На этом установка Docker Engine и Docker-Compose завершена. 

        Получаем конфигурации docker-compose, переходим в директорию с файлом **docker-compose.yaml**. Проходим аутентификацию в нужное нам **docker registry - docker login**.

        .. note:: 

            Registry URL и данные для аутентификации можно запросить у контактного лица со стороны Citeck.

        Запуск Citeck Сommunity: 

        .. code-block::

            docker-compose up -d

        **Установка citeck-community**

        .. code-block::

            wget https://github.com/Citeck/citeck-community/archive/refs/heads/master.zip
            unzip master.zip
            cd citeck-community-master
            docker-compose pull

        Запуск Citeck Сommunity:

        .. code-block::

            docker-compose up -d

        .. note:: 

            Выполнять из директории citeck-community-master

        В случае, если локальная сеть, может пересекаться с сетью docker, лучше предопределить подсеть docker. Сделать это можно в файле **/etc/docker/daemon.json**, переменная **default-address-pools**

        .. code-block::

            {
            "default-address-pools":
            [
                {"base":"172.19.0.0/16","size":24}
            ]
            }

   .. tab:: Debian 11 "Bullseye"

        Установка Docker:

        .. code-block::

            sudo apt-get update
            sudo apt-get install ca-certificates curl
            sudo install -m 0755 -d /etc/apt/keyrings
            sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
            sudo chmod a+r /etc/apt/keyrings/docker.asc
            
            # Add the repository to Apt sources:
            echo \
            "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
            $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
            sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
            sudo apt-get update
            
            ## Чтобы установить последнюю доступную версию, выполните команду::
            sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
            
            ## Чтобы установить конкретную версию, выполните команду:
            apt-cache madison docker-ce | awk '{ print $3 }'
            VERSION_STRING={Your Specific version}
            sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io docker-buildx-plugin docker-compose-plugin

        Настройка docker на запуск при старте системы:

        .. code-block::

            sudo systemctl enable docker

        Установка Docker-compose:

        .. code-block::

            wget https://github.com/docker/compose/releases/download/v2.29.1/docker-compose-Linux-x86_64
            mv ./docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
            sudo chmod +x /usr/local/bin/docker-compose

        .. note:: 

            Версию можно изменить на более актуальную, заменив v2.29.1

        На этом установка Docker Engine и Docker-Compose завершена. 

        Получаем конфигурации docker-compose, переходим в директорию с файлом **docker-compose.yaml**. Проходим аутентификацию в нужное нам **docker registry - docker login**.

        .. note:: 

            Registry URL и данные для аутентификации можно запросить у контактного лица со стороны Citeck.

        Запуск Citeck Сommunity: 

        .. code-block::

            docker-compose up -d

        **Установка citeck-community**

        .. code-block::

            wget https://github.com/Citeck/citeck-community/archive/refs/heads/master.zip
            unzip master.zip
            cd citeck-community-master
            docker-compose pull

        Запуск Citeck Сommunity:

        .. code-block::

            docker-compose up -d

        .. note:: 

            Выполнять из директории citeck-community-master

        В случае, если локальная сеть, может пересекаться с сетью docker, лучше предопределить подсеть docker. Сделать это можно в файле **/etc/docker/daemon.json**, переменная **default-address-pools**

        .. code-block::

            {
            "default-address-pools":
            [
                {"base":"172.19.0.0/16","size":24}
            ]
            }

   .. tab:: Astra Linux Орел

        .. note:: 

            Инструкция проверялась с Astra Linux Common Edition 2.12.46.

        Установка Docker:

        .. code-block::

            sudo apt update
            sudo apt install apt-transport-https ca-certificates curl gnupg2 software-properties-common
            curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
            sudo printf "deb [arch=amd64] https://download.docker.com/linux/debian stretch stable \n" > /etc/apt/sources.list.d/docker.list
            sudo apt-get update
            sudo apt-get install docker-ce docker-ce-cli containerd.io

        Настройка групп docker:

        .. code-block::

            sudo groupadd docker
            sudo usermod -aG docker $USER
            sudo systemctl enable docker.service
            sudo systemctl enable containerd.service

        Установка Docker Compose:

        .. code-block::

            wget https://github.com/docker/compose/releases/download/1.27.4/docker-compose-Linux-x86_64
            mv ./docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
            sudo chmod +x /usr/local/bin/docker-compose

        .. note:: 

            Версию можно изменить на более актуальную, заменив 1.27.4

        **Установка citeck-community** (выполняется в терминале, Alt+T):

        .. code-block::

            git clone https://github.com/Citeck/citeck-community.git && cd citeck-community
            docker-compose pull

        
        Запуск Citeck Сommunity:

        .. note:: 

            Выполнять из директории citeck-community

        .. code-block::

            docker-compose up -d

        В случае, если локальная сеть, может пересекаться с сетью docker, лучше предопределить подсеть docker. Сделать это можно в файле **/etc/docker/daemon.json**, переменная **default-address-pools**

        .. code-block::

            {
              "default-address-pools":
              [
                {"base":"172.19.0.0/16","size":24}
              ]
            }

   .. tab:: Ред ОС (Red OS)

        .. note:: 

            Инструкция проверялась на РЕД ОС 7.3| Ядро Linux 5.15.72 

        Обновить пакеты и выключить SELINUX:

        .. code-block::

            dnf update
            echo 'SELINUX=disabled' > /etc/sysconfig/selinux
            reboot

        Установка Docker и Docker Compose:

        .. code-block::

            sudo dnf install docker-ce docker-ce-cli docker-compose
            systemctl enable docker

        **Установка citeck-community** (выполняется в терминале, Alt+T):

        .. code-block::

            git clone https://github.com/Citeck/citeck-community.git && cd citeck-community
            docker-compose pull

        Запуск Citeck Сommunity:

        .. code-block::

            docker-compose up -d

        .. note:: 

            Если встречается ошибка **unknown log opt 'max-size' for journald log driver**, открыть **/etc/docker/deamon.json** и изменить там **"log-driver": "journald"** на **"log-driver": "json-file"**

        В случае, если локальная сеть, может пересекаться с сетью docker, лучше предопределить подсеть docker. Сделать это можно в файле **/etc/docker/daemon.json**, переменная **default-address-pools**

        .. code-block::

            {
              "default-address-pools":
              [
                {"base":"172.19.0.0/16","size":24}
              ]
            }

   .. tab:: Oracle Enterprise Linux 8.9

        Установка Docker:

        .. code-block::

            sudo apt-get update
            sudo apt-get install ca-certificates curl
            sudo install -m 0755 -d /etc/apt/keyrings
            sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
            sudo chmod a+r /etc/apt/keyrings/docker.asc
            
            # Add the repository to Apt sources:
            echo \
            "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian \
            $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
            sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
            sudo apt-get update
            
            ## Чтобы установить последнюю доступную версию, выполните команду::
            sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
            
            ## Чтобы установить конкретную версию, выполните команду:
            apt-cache madison docker-ce | awk '{ print $3 }'
            VERSION_STRING={Your Specific version}
            sudo apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING containerd.io docker-buildx-plugin docker-compose-plugin

        Настройка Docker на запуск при старте системы:

        .. code-block::

            sudo systemctl enable docker

        Установка Docker-compose:

        .. code-block::

            wget https://github.com/docker/compose/releases/download/v2.29.1/docker-compose-Linux-x86_64
            mv ./docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
            sudo chmod +x /usr/local/bin/docker-compose

        .. note:: 

            Версию можно изменить на более актуальную, заменив v2.29.1

        На этом Установка Docker Engine и Docker-Compose завершена.
       
        Получаем конфигурации docker-compose, переходим в директорию с файлом **docker-compose.yaml**.

        .. note:: 

            В случае если используется Enterprise сборка, необходимо подключиться к registry. 
            
            Проходим аутентификацию в нужное нам docker registry - docker login (registry host).
            
            **Registry URL** и **данные для аутентификации** можно запросить у контактного лица со стороны Citeck.

        Запуск Citeck Сommunity: 

        .. code-block::

            docker-compose up -d

        **Установка citeck-community** (выполняется в терминале, Alt+T):

        .. code-block::

            wget https://github.com/Citeck/citeck-community/archive/refs/heads/master.zip
            unzip master.zip
            cd citeck-community-master
            docker-compose pull

        Запуск Citeck Сommunity:

        .. note:: 

            Выполнять из директории citeck-community-master

        .. code-block::

            docker-compose up -d

        В случае, если локальная сеть, может пересекаться с сетью docker, лучше предопределить подсеть docker. Сделать это можно в файле **/etc/docker/daemon.json**, переменная **default-address-pools**

        .. code-block::

            {
              "default-address-pools":
              [
                {"base":"172.19.0.0/16","size":24}
              ]
            }

Переключение на BASIC аутентификацию вместо Keycloak
----------------------------------------------------

Если нужен простой способ настройки для доступа в систему минуя Keycloak, то можно настроить BASIC Auth (не рекомендуется для production сред).

  1. В  файле **ecos-proxy-app.env**:

     .. code-block::

        nano citeck-community-master/services/environments/ecos-proxy-app.env     

    заменить строку **ENABLE_OIDC_FULL_ACCESS=true** на **ENABLE_OIDC_FULL_ACCESS=false**

  2. в этом же файле добавить - **BASIC_AUTH_ACCESS=admin:admin,fet:fet**

.. note:: 

    | ``admin:admin,fet:fet`` - это список пользователей, которые будут иметь доступ в систему. 
    | Формат значения следующий - ``{{пользователь_0}}:{{пароль_0}},{{пользователь_1}}:{{пароль_1}}`` 
    | После изменения **ecos-proxy-app.env** необходима перезагрузка контейнера ecos-proxy-app, чтобы изменения вступили в силу.

После внесения изменений запустите проект.

.. code-block::

    docker-compose down

в директории **citeck-community-master**  для остановки проекта

.. code-block::

    docker-compose up -d

в директории **citeck-community-master** для запуска проекта

Данные для входа в Citeck:

.. code-block::

    Username: admin
    Password: admin

Сервисы Docker
---------------

:ref:`По ссылке <docker_services>` перечислены сервисы с точки зрения Docker’а и их настройки.

.. note::

    Некоторые контейнеры запускаются 1 раз, например:

        - citeck-community-master-ecos-meetings-ecos-apps-1
        - citeck-community-master-ecos-order-pass-ecos-apps-1
        - citeck-community-master-ecos-common-data-list-ecos-apps-1
        - citeck-community-master-ecos-assignments-ecos-apps-1

    и далее находятся в статусе **exited**

Возможные проблемы
-------------------

ОС Windows
~~~~~~~~~~~~

Включение функции WSL 2 в Windows
""""""""""""""""""""""""""""""""""""""""

Docker Desktop использует функцию динамического распределения памяти в WSL 2, чтобы значительно снизить потребление ресурсов. Кроме того, WSL 2 улучшает совместное использование файловой системы, время загрузки и предоставляет пользователям Docker Desktop доступ к некоторым новым интересным функциям.

1)	Перед установкой WSL 2 необходимо включить необязательный компонент **Платформа виртуальных машин**. 
    
    В **PowerShell** ввести команду:

    .. code-block:: 

        dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

2)	Скачать и установить пакет обновления ядра Linux:
    
    `Пакет обновления ядра Linux в WSL 2 для 64-разрядных компьютеров <https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi>`_ 

3)	Выбрать WSL 2 в качестве версии по умолчанию:

    .. code-block:: 

        wsl --set-default-version 2

Проверить можно командой. Более подробная версия инструкции см. `https://docs.microsoft.com/ru-ru/windows/wsl/install-win10 <https://docs.microsoft.com/ru-ru/windows/wsl/install-win10>`_ 

    .. code-block::

        wsl --list --verbose
  

4)	При установке Docker в окне конфигурации установите галочку в поле **Use WSL 2 instead of Hyper-V (recommended)**. Более подробная версия инструкции см. `https://docs.docker.com/docker-for-windows/wsl/  <https://docs.docker.com/docker-for-windows/wsl/>`_ 


Порт 8080 уже занят
""""""""""""""""""""

Citeck UI использует порт 8080 и, если этот порт уже занят другой программой, то можно получить ошибку:

**«Error starting userland proxy: listen tcp 0.0.0.0:8080:bind: Only one usage of each socket address is normally permitted.»**

 .. image:: _static/docker-compose/01.png
       :width: 400
       :align: center

Если команда:

.. code-block::

    netstat -ono (или netstat -ono | findstr 8080)  

не находит, чем занят порт, то нужно скачать программу, например, CurrPorts и уже с ее помощью найти занятые порты. 

Порт зарезервирован Windows
""""""""""""""""""""""""""""

К примеру, каталог **ecos-postgres** использует порт **50432**, но этот порт зарезервирован Windows. Проверить такие порты можно командой

.. code-block::

    netsh int ipv4 show excludedportrange protocol=tcp 

.. image:: _static/docker-compose/02.png
    :width: 400
    :align: center
 
Команда покажет диапазон зарезервированных портов. Видно, что порт 50432 находится в данном диапазоне и поэтому при установке была получена ошибка:

**«Cannot start service ecos-postgress: driver failed proogramming external connectivity on endpoint»**

Чтобы это исправить, нужно в командной строке, запущенной с повышенными правами:

    1)	Остановить Hyper-V: 

        .. code-block::
    
            dism.exe /Online /Disable-Feature:Microsoft-Hyper-V 
            
        Выполнить перезагрузку.

    2)	Добавить нужный порт в исключения: 

        .. code-block::
    
            netsh int ipv4 add excludedportrange protocol=tcp startport=50432 numberofports=1

    3)	Запустить Hyper-V: 

        .. code-block::
    
            dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All 
            
        После потребуется перезагрузка.

Порт попадет в исключения, и подобной ошибки не возникнет.

Настройка дополнительных параметров  WSL в Windows
""""""""""""""""""""""""""""""""""""""""""""""""""""

 `Настройка дополнительных параметров  WSL в Windows <https://learn.microsoft.com/en-us/windows/wsl/wsl-config#configure-global-options-with-wslconfig>`_

MacOS
~~~~~~

Запускаются не все контейнеры
"""""""""""""""""""""""""""""""

Если при разворачивании приложения в docker запускаются не все контейнеры:

 .. image:: _static/docker-compose/06.png
       :width: 400
       :align: center

необходимо в настройках docker добавить путь **/opt**:

 .. image:: _static/docker-compose/07.png
       :width: 600
       :align: center

How to
-------------------

Изменить http://localhost на http://mydomain.ru
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

С чистой БД
""""""""""""""

Поменять в:

1. **citeck-community/services/environments/ecos-identity-app.env**

.. code-block::

 KEYCLOAK_FRONTEND_URL=http://localhost/ecos-idp/auth 

на 

.. code-block::

    KEYCLOAK_FRONTEND_URL=http://mydomain.ru/ecos-idp/auth

2. **citeck-community/services/environments/ecos-proxy-app.env**

.. code-block::

    EIS_ID=citeck-community на EIS_ID=mydomain.ru + REDIRECT_LOGOUT_URI=http://localhost

на 

.. code-block::

    REDIRECT_LOGOUT_URI=http://mydomain.ru

3. Шаг имеет смысл, если разворачивать на чистых БД:

**citeck-community/services/configs/ecos-identity-app/realm-export.json**

.. code-block::

    "redirectUris": [
        "http://localhost*"
    ],

на

.. code-block::

    "redirectUris": [
        "http://mydomain.ru*"
    ],
    
4. Шаг имеет смысл, если разворачивать на чистых БД:

**citeck-community/services/configs/ecos-identity-app/realm-export.yaml**

.. code-block::

    "redirectUris": [
        "http://localhost*"
    ],

на

.. code-block::

    "redirectUris": [
        "http://mydomain.ru*"
    ],

5. В **hosts** добавить запись:

.. code-block::

    127.0.0.1 mydomain.ru

Не с чистой БД
"""""""""""""""""

1. Зайти в панель администратора keycloak.
2. Открыть реалм **ecos-app**.
3. Открыть раздел **clients**.
4. Открыть **ecos-proxy-app**.
5. Изменить в поле **Valid Redirect URIs** значение http://localhost на http://mydomain.ru
6. Сохранить.


Исключить адрес из авторизации Keycloak
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Временно можно сделать на уровне модификации **ecos-Proxy-app**.

Проверить можно,  зайдя в контейнер: 

**docker-compose exec ecos-proxy-app /bin/bash**

и модифицировав: 

**/etc/nginx/conf.d/default.conf**

После этого выполнить:

.. code-block::

    nginx -s reload

На постоянной основе только собрав свою версию контейнера **ecos-proxy-app**

Второй вариант: предложив Pull-реквест нам с возможностью передавать не защищаемые URL в качестве параметра.