.. _docker_compose:


Установка Citeck ECOS c помощью Docker-compose
===============================================

.. contents::
    :depth: 5


Общие требования к системе
---------------------------

* Все действия рекомендуется выполнять в командной строке или окне терминала, или в Git CMD Windows, запущенного с повышенными правами.
* В файле **hosts** прописать ``127.0.0.1 ecos-community-demo``. Путь к папке, где лежит файл hosts, зависит от операционной системы, которая установлена на вашем компьютере: 
  
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
  * 4 ГБ оперативной памяти
  * Поддержка аппаратной виртуализации на уровне BIOS должна быть включена в настройках BIOS. Дополнительные сведения см. `в разделе Виртуализация <https://docs.docker.com/desktop/troubleshoot/topics/#virtualization>`_

* Загрузить и установить `пакет обновления ядра Linux <https://docs.microsoft.com/windows/wsl/wsl2-kernel>`_

`Официальное руководстов по установке Docker на Windows <https://docs.docker.com/desktop/install/windows-install/>`_

Linux
~~~~~~~~~~~~

* Поддержка 64-битного ядра и процессора для виртуализации.
* Поддержка виртуализации KVM. Следуйте `инструкциям поддержки виртуализации KVM <https://docs.docker.com/desktop/install/linux-install/#kvm-virtualization-support>`_ для проверки включены или нет модули ядра KVM и как предоставить доступ к устройству kvm.
* QEMU должен быть версии 5.2 или новее. Рекомендуем обновиться до последней версии.
* подсистема инициализации и управления службами systemd.
* Gnome или среда рабочего стола KDE.
* Не менее 4 ГБ оперативной памяти.
* Включите настройку сопоставления идентификаторов в пространствах имен пользователей, см. `Общий доступ к файлам <https://docs.docker.com/desktop/install/linux-install/#file-sharing>`_

`Официальное руководстов по установке Docker на Linux <https://docs.docker.com/desktop/install/linux-install/>`_

`Официальное руководстов по установке Docker на Ubuntu <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_

MacOS
~~~~~~~~~~~~

* MacOS версии 10.15 или выше.
* Не менее 4 ГБ оперативной памяти.

`Официальное руководстов по установке Docker на MacOS <https://docs.docker.com/desktop/install/mac-install/>`_

Установка и запуск проекта
---------------------------

•	Установить `docker и docker-compose <https://docs.docker.com/get-docker/>`_ на Вашу ОС
•	Установить `Git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_ для Вашей ОС
•	Скачать `репозиторий <https://gitlab.citeck.ru/ecos-community/ecos-community-demo/-/archive/master/ecos-community-demo-master.zip>`_ , распаковать на диске С
•	В командной строке выполнить команды: 

    - для перехода в распакованный архив ``cd c:\ecos-community-demo-master`` 
    - для запуска ``docker-compose up -d`` 

•	Подождать некоторое время (в зависимости от мощности системы) для того, чтобы система запустилась
•	Перейти в браузере по адресу http://ecos-community-demo/

Войти в систему, используя следующие учётные данные:

    Логин – **admin**

    Пароль - **admin**

При первом развертывании keycloak попросит сменить пароль.  Если необходимо еще раз сменить пароль, `см. инструкцию  <https://www.keycloak.org/docs/latest/getting_started/index.html#creating-a-user>`_

Подготовка окружения CentOS 7.x для установки Citeck Ecos
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

    curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod +x /usr/local/bin/docker-compose
    ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

В случае, если локальная сеть, может пересекаться с сетью докера, лучше предопределить подсеть докера. Сделать это можно в файле:

``/etc/docker/daemon.json, переменная default-address-pools``

.. code-block::

    {
    "default-address-pools":
    [
        {"base":"172.19.0.0/16","size":24}
    ]
    }

Следующим этапом необходимо получить комплект поставки, в который входят `docker-compose.yaml и environments <https://gitlab.citeck.ru/ecos-community/ecos-community-demo/-/archive/master/ecos-community-demo-master.zip>`_ и поместить его на сервер.

После этого в директории, куда поместили проект, выполнить:

.. code-block::

    docker-compose pull
    docker-compose up -d

Система будет инициализирована, и после полного запуска, будет готова к работе.


Сервисы Docker
---------------

:ref:`По ссылке <docker_services>` перечислены сервисы с точки зрения Docker’а и их настройки.

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
