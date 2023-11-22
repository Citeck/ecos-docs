.. _docker_compose:

Установка Citeck ECOS c помощью Docker-compose
===============================================

.. contents::
    :depth: 5


Общие требования к системе
---------------------------

* Все действия рекомендуется выполнять в командной строке или окне терминала, или в Git CMD Windows, запущенного с повышенными правами.
* В файле **hosts** прописать ``127.0.0.1 ecos-community-demo``. Путь к папке, где лежит файл **hosts**, зависит от операционной системы, которая установлена на вашем компьютере: 
  
  *  Windows— **c:/windows/system32/drivers/etc/hosts** 
  *  Linux, Ubuntu, Unix, BSD — **/etc/hosts** 
  *  Mac OS — **/private/etc/hosts**

Системные требования
---------------------

Windows
~~~~~~~~~~~~

* Windows 11 64bit: Home, Pro, Enterprise или Education версии 21H2 или выше.
* Windows 10 64bit: Home или Pro 21H1 (сборка 19043) или выше, Enterprise или Education 20H2 (сборка 19042) или выше
* Включите функцию WSL 2 в Windows. Подробные инструкции см. `в документации Microsoft <https://docs.microsoft.com/en-us/windows/wsl/install-win10>`_.
* Для успешного запуска WSL 2 в Windows 10 или Windows 11 необходимы следующие предварительные требования к оборудованию:

  * 64-битный процессор с трансляцией адресов второго уровня (`SLAT <https://en.wikipedia.org/wiki/Second_Level_Address_Translation>`_)
  * 16 ГБ оперативной памяти
  * Поддержка аппаратной виртуализации на уровне BIOS должна быть включена в настройках BIOS. Дополнительные сведения см. `в разделе Виртуализация <https://docs.docker.com/desktop/troubleshoot/topics/#virtualization>`_

* Загрузить и установить `пакет обновления ядра Linux <https://docs.microsoft.com/windows/wsl/wsl2-kernel>`_

`Официальное руководстов по установке Docker на Windows <https://docs.docker.com/desktop/install/windows-install/>`_

.. note:: 

    Клонировать репозиторий и запускать скрипты необходимо из-под Ubuntu

Linux
~~~~~~~~~~~~

* Поддержка 64-битного ядра и процессора для виртуализации.
* Поддержка виртуализации KVM. Следуйте `инструкциям поддержки виртуализации KVM <https://docs.docker.com/desktop/install/linux-install/#kvm-virtualization-support>`_ для проверки включены или нет модули ядра KVM и как предоставить доступ к устройству kvm.
* QEMU должен быть версии 5.2 или новее. Рекомендуем обновиться до последней версии.
* подсистема инициализации и управления службами systemd.
* Gnome или среда рабочего стола KDE.
* Не менее 16 ГБ оперативной памяти.
* Включите настройку сопоставления идентификаторов в пространствах имен пользователей, см. `Общий доступ к файлам <https://docs.docker.com/desktop/install/linux-install/#file-sharing>`_

`Официальное руководстов по установке Docker на Linux <https://docs.docker.com/desktop/install/linux-install/>`_

`Официальное руководстов по установке Docker на Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_

MacOS
~~~~~~~~~~~~

* MacOS версии 10.15 или выше.
* Не менее 16 ГБ оперативной памяти.

`Официальное руководстов по установке Docker на MacOS <https://docs.docker.com/desktop/install/mac-install/>`_

Установка и запуск проекта
---------------------------

.. important:: 

    Комплект поставляется с предзаполненными демонстрационными данными. 
    
    Для отключения данной настройки перед разверачиванием стенда перейдите в папку ``\services\environments`` в файлах **ecos-microservices-postgresql.env** и **mongodb-app.env**
    в настройке ``WITH_DEMO_DATA`` укажите **false**.


•	Установите `docker и docker-compose <https://docs.docker.com/get-docker/>`_ на Вашу ОС
•   Клонируйте репозиторий: ``git clone https://github.com/citeck/ecos-community-demo.git``
•	В терминале: 

    - перейдите в папку с клонированным репозиторием ``cd полный путь до папки`` 
    - запустите ``docker-compose up -d`` 

•	Подождите некоторое время (в зависимости от мощности системы) для того, чтобы система запустилась.
•	Перейдите в браузере по адресу http://ecos-community-demo/

Войдите в систему, используя следующие учётные данные:

    Логин – **admin**

    Пароль - **admin**

При первом развертывании keycloak попросит сменить пароль. 

Если необходимо еще раз сменить пароль, то `см. инструкцию  <https://www.keycloak.org/docs/latest/getting_started/index.html#creating-a-user>`_

.. note:: 

    При первом запуске в течение первых 5 минут после успешной установки и входа в систему может возникать ошибка:

    .. image:: _static/docker-compose/08.png
        :width: 600
        :align: center

    Развертывание и запуск ECOS продолжается, необходимо подождать.

Подготовка окружения CentOS 7.x для установки Citeck ECOS
----------------------------------------------------------

Обновить систему и пакеты до последней актуальной версии:

.. code-block::

    yum update -y && yum upgrade -y

Отключить SELinux и перезагрузить сервер:

.. code-block::

    sed -i 's/enforcing/disabled/g' /etc/selinux/config
    reboot

Устанавить Python:

.. code-block::

    yum install epel-release -y
    yum install python3 -y && yum install python3-pip -y

Устанавить пакеты, для комфортной работы:

.. code-block::

    yum install -y mc yum-utils nano ethtool ntp ntpdate firewalld lvm2 device-mapper-persistent-data htop fail2ban mc wget screen pigz

Установить Docker Engine:

.. code-block::

    yum-config-manager --add-repo https://http://download.docker.com /linux/centos/docker-ce.repo
    yum install -y docker-ce docker-ce-cli http://containerd.io 
    systemctl enable docker && systemctl start docker

Установить docker-compose:

.. code-block::

    curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose

В случае, если локальная сеть, может пересекаться с сетью докера, лучше предопределить подсеть докера. Сделать это можно в файле:

``/etc/docker/daemon.json, переменная default-address-pools``

.. code-block::

    {
    "default-address-pools":
    [
        {"base":"172.19.0.0/16","size":24}
    ]
    }

Следующим этапом необходимо получить комплект поставки, в который входят `docker-compose.yaml и environments <https://github.com/Citeck/ecos-community-demo/archive/refs/heads/master.zip>`_ и поместить его на сервер.

После этого в директории, куда поместили проект, выполнить:

.. code-block::

    docker-compose pull
    docker-compose up -d

Система будет инициализирована, и после полного запуска, будет готова к работе.

Настройка Proxy в Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~

Настройки прокси задаются в файле:

.. code-block::

    /etc/systemd/system/docker.service.d/http-proxy.conf 

Если этого файла или папки нет, нужно их создать. Содержимое файла должно быть примерно таким:

.. code-block::

    [Service]
    Environment="HTTP_PROXY=http://<USER_NAME>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>"
    Environment="HTTPS_PROXY=http://<USER_NAME>:<PASSWORD>@<PROXY_HOST>:<PROXY_PORT>"
    Environment="NO_PROXY=localhost,127.0.0.1,ecos-app, ecos-apps-app, ecos-gateway-app, ecos-history-app, ecos-identity-app, ecos-integrations-app, ecos-logger-app, ecos-microservices-postgresql-app, ecos-model-app, ecos-notifications-app, ecos-process-app, ecos-proxy-app, ecos-registry-app, ecos-search-app, ecos-uiserv-app, mailhog-app, mongodb-app, node-exporter-app, only-office-app, portainer-agent-app, postgres-exporter-app, rabbitmq-app, zookeeper-app"

Также в раздел *NO_PROXY* можно добавить внутренние домены вашей компании (через запятую и также можно использовать звездочку например ``*.someco.com,`` ``*.someco.ru``)

После добавления данного файла нужно перезапустить демон Docker

.. code-block::

    systemctl daemon-reload
    systemctl restart docker


Подготовка окружения Astra Linux Орел для установки Citeck ECOS
---------------------------------------------------------------

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

Установка Docker-compose:

.. code-block::

    wget https://github.com/docker/compose/releases/download/1.27.4/docker-compose-Linux-x86_64
    mv ./docker-compose-Linux-x86_64 /usr/local/bin/docker-compose
    sudo chmod +x /usr/local/bin/docker-compose

.. note:: 

    Версию можно изменить на более актуальную, заменив 1.27.4

Установка Ecos-Community-Demo (выполняется в терминале, Alt+T):

.. code-block::

    wget https://github.com/Citeck/ecos-community-demo/archive/refs/heads/master.zip
    unzip master.zip
    cd ecos-community-demo-master
    docker-compose pull

Добавить ecos-community-demo в локальный **hosts** файл:

.. code-block::

    vim /etc/hosts     - открываем файл
    127.0.0.1      ecos-community-demo     - производим запись в файл
    :wq!     - выходим из редактора vim

Запуск Ecos-Community-Demo:

.. note:: 

    Выполнять из директории ecos-community-demo-master

.. code-block::

    docker-compose up -d

В случае, если локальная сеть, может пересекаться с сетью докера, лучше предопределить подсеть докера. Сделать это можно в файле ``/etc/docker/daemon.json``, переменная ``default-address-pools``

.. code-block::

    {
      "default-address-pools":
      [
        {"base":"172.19.0.0/16","size":24}
      ]
    }

Подготовка окружения Ред ОС (Red OS) для установки Citeck ECOS
---------------------------------------------------------------

.. note:: 

    Инструкция проверялась на РЕД ОС 7.3| Ядро Linux 5.15.72 

Обновить пакеты и выключить SELINUX:

.. code-block::

    dnf update
    echo 'SELINUX=disabled' > /etc/sysconfig/selinux
    reboot

Установка Docker и Docker-compose:

.. code-block::

    sudo dnf install docker-ce docker-ce-cli docker-compose
    systemctl enable docker

Установка Ecos-Community-Demo (выполняется в терминале, Alt+T):

.. code-block::

    wget https://github.com/Citeck/ecos-community-demo/archive/refs/heads/master.zip
    unzip master.zip
    cd ecos-community-demo-master
    docker-compose pull

Запуск Ecos-Community-Demo:

.. code-block::

    docker-compose up -d

.. note:: 

    Если встречается ошибка ``unknown log opt 'max-size' for journald log driver``, открыть ``/etc/docker/deamon.json`` и изменить там ``"log-driver": "journald "`` на ``"log-driver": "json-file"``

Добавить ecos-community-demo в локальный **hosts** файл:

.. code-block::

    vim /etc/hosts     - открываем файл
    127.0.0.1      ecos-community-demo     - производим запись в файл
    :wq!     - выходим из редактора vim

В случае, если локальная сеть, может пересекаться с сетью докера, лучше предопределить подсеть докера. Сделать это можно в файле ``/etc/docker/daemon.json``, переменная ``default-address-pools``

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

  1. ``nano ecos-community-demo-master/services/environments/ecos-proxy-app.env`` заменить строку ``ENABLE_OIDC_FULL_ACCESS=true`` на ``ENABLE_OIDC_FULL_ACCESS=false``
  2. в этом же файле добавить - ``BASIC_AUTH_ACCESS=admin:admin,fet:fet``

.. note:: 

    | ``admin:admin,fet:fet`` - это список пользователей, которые будут иметь доступ в систему. 
    | Формат значения следующий - ``{{пользователь_0}}:{{пароль_0}},{{пользователь_1}}:{{пароль_1}}`` 
    | После изменения ecos-proxy-app.env необходима перезагрузка контейнера ecos-proxy-app, чтобы изменения вступили в силу.

После внесения изменений запустите проект.

``docker-compose down`` в директории ``ecos-community-demo-master`` для остановки проекта

``docker-compose up -d`` в директории ``ecos-community-demo-master`` для запуска проекта

Тестировать можно с локальной машины при наличии корректной записи в ``/etc/hosts``.

Данные для входа в ecos - ``admin`` | ``admin``

Сервисы Docker
---------------

:ref:`По ссылке <docker_services>` перечислены сервисы с точки зрения Docker’а и их настройки.

.. attention::

    Следующие контейнеры запускаются 1 раз:

        - ecos-community-demo-master-ecos-meetings-ecos-apps-1
        - ecos-community-demo-master-ecos-order-pass-ecos-apps-1
        - ecos-community-demo-master-ecos-common-data-list-ecos-apps-1
        - ecos-community-demo-master-ecos-assignments-ecos-apps-1

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

    ``dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart``

2)	Скачать и установить пакет обновления ядра Linux:
    
    `Пакет обновления ядра Linux в WSL 2 для 64-разрядных компьютеров <https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi>`_ 

3)	Выбрать WSL 2 в качестве версии по умолчанию:

    ``wsl --set-default-version 2``

Проверить можно командой. Более подробная версия инструкции см. `https://docs.microsoft.com/ru-ru/windows/wsl/install-win10 <https://docs.microsoft.com/ru-ru/windows/wsl/install-win10>`_ 

    ``wsl --list --verbose``

4)	При установке Docker в окне конфигурации установите галочку в поле **Use WSL 2 instead of Hyper-V (recommended)**. Более подробная версия инструкции см. `https://docs.docker.com/docker-for-windows/wsl/  <https://docs.docker.com/docker-for-windows/wsl/>`_ 


Порт 8080 уже занят
""""""""""""""""""""

Ecos-ui использует порт 8080 и, если этот порт уже занят другой программой, то можно получить ошибку:

**«Error starting userland proxy: listen tcp 0.0.0.0:8080:bind: Only one usage of each socket address is normally permitted.»**

 .. image:: _static/docker-compose/01.png
       :width: 400
       :align: center

Если команда ``netstat -ono (или netstat -ono | findstr 8080)`` не находит, чем занят порт, то нужно скачать программу, например, CurrPorts и уже с ее помощью найти занятые порты. 

Порт зарезервирован Windows
""""""""""""""""""""""""""""

К примеру, каталог **ecos-postgres** использует порт **50432**, но этот порт зарезервирован Windows. Проверить такие порты можно командой ``netsh int ipv4 show excludedportrange protocol=tcp``. 

 .. image:: _static/docker-compose/02.png
       :width: 400
       :align: center
 
Команда покажет диапазон зарезервированных портов. Видно, что порт 50432 находится в данном диапазоне и поэтому при установке была получена ошибка:

**«Cannot start service ecos-postgress: driver failed proogramming external connectivity on endpoint»**

Чтобы это исправить, нужно в командной строке, запущенной с повышенными правами:

1)	Остановить Hyper-V: ``dism.exe /Online /Disable-Feature:Microsoft-Hyper-V`` (выполнить перезагрузку)

2)	Добавить нужный порт в исключения: ``netsh int ipv4 add excludedportrange protocol=tcp startport=50432 numberofports=1``

3)	Запустить Hyper-V: ``dism.exe /Online /Enable-Feature:Microsoft-Hyper-V /All`` (после потребуется перезагрузка)

Порт попадет в исключения, и подобной ошибки не возникнет.

Настройка дополнительных параметров  WSL в Windows
""""""""""""""""""""""""""""""""""""""""""""""""""""

 `Настройка дополнительных параметров  WSL в Windows <https://learn.microsoft.com/en-us/windows/wsl/wsl-config#configure-global-options-with-wslconfig>`_

MacOS
~~~~~~

Запускаются не все контейнеры
"""""""""""""""""""""""""""""""

Если при разворачивании приложения в докере запускаются не все контейнеры:

 .. image:: _static/docker-compose/06.png
       :width: 400
       :align: center

необходимо в настройках докера добавить путь **/opt**:

 .. image:: _static/docker-compose/07.png
       :width: 600
       :align: center
