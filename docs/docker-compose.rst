=============================================================
Инструкция по установке Citeck ECOS c помощью Docker-compose
=============================================================



1.	Общие требования к системе
-------------------------------------------------------------
Просим обратить внимание, что:
 *	Docker Desktop for Windows требует для работы Microsoft Hyper-V.
 *	Установщик Docker Desktop for Windows самостоятельно включает системную компоненту Hyper-V, если это требуется, и перезапускает вашу ЭВМ.
 *	После настройки Hyper-V, VirtualBox не будет работать, но VirtualBox VM останутся нетронутыми.
 *	Выделенные жирным шрифтом, команды в данной инструкции необходимо выполнять в эмуляторе терминала или в Git CMD Windows.
 *	Все действия рекомендуется выполнять в командной строке или окне терминала, запущенные с повышенными правами.
Системные требования:
 *	Windows 10 64bit: Pro, Enterprise или Education (1607 Anniversary Update, Build 14393 или более поздний).
 *	Linux kernel version 3.10.0 или выше.
 *	Виртуализация разрешена в BIOS.
 *	Процессор	с	поддержкой	CPU	SLAT	(Second	Level	Address Translation).
 *	Минимум 10 GB ОЗУ.
 *	Минимум 4 ядра

2.	Быстрый старт
-------------------------------------------------------------
 •	Установите docker и docker-compose на Вашу ОС
 •	Установите `Git <https://git-scm.com/book/en/v2/Getting-Started-Installing-Git>`_ для Вашей ОС
 •	Скачать репозиторий по `ссылке <https://bitbucket.org/citeck/ecos-community-demo/get/4a3f6e5.zip>`_, распаковать в диске С
 •	Выполнить	команду	cd	c:\ecos-community-demo	(переход	в распакованный архив)
 •	Выполнить docker-compose -f docker-compose.yaml up -d
 •	Необходимо подождать некоторое время (в зависимости от мощности системы) для того, чтобы система запустилась
 •	Перейти в браузере по адресу http://localhost/ Войти в систему, используя следующие учётные данные:
 Логин – admin | 
 Пароль - alfr3sc0

 .. caution:: Данные, внесенные в систему в режиме быстрого  старта  после  перезапуска,  не  сохранятся. Для сохранения данных используйте расширенный режим.

3.	Установка Docker
-------------------------------------------------------------
3.1. На ОС Windows
~~~~~~~~~~~~~~~~~~~~~~
 *	Скачать установщик  `Docker <https://hub.docker.com/editions/community/docker-ce-desktop-windows>`_
 *	Следуйте шагам мастера установки, чтобы принять лицензионное соглашение, авторизовать и продолжить установку. В процессе установки ОС попросит авторизовать Docker.app с вашим системным паролем. Привилегированный доступ необходим для того, чтобы установить сетевые компоненты, ссылки на Docker apps и для управления виртуальными машинами Hyper-V. Docker не запускается автоматически после установки. Его необходимо запустить вручную. Когда иконка приложения в трее перейдёт в состояние готова, Docker готов к использованию и доступен из окна терминала.
 *	Docker Desktop for Windows уже включает в себя docker-compose, поэтому отдельно устанавливать его не нужно. Проверить можно, выполнив в окне командной строки docker-compose –version.

 `Офф. руководство <https://docs.docker.com/docker-for-windows/install/>`_ 


.. attention:: На виртуальной машине Windows Lunix-контейнеры не работают

3.2.	На ОС MacOS
~~~~~~~~~~~~~~~~~~~~
 *	Скачать установщик `Docker Desktop for Mac <https://hub.docker.com/editions/community/docker-ce-desktop-mac>`_ 
 *	Двойным щелчком по Docker.dmg запустите установщик.
 *	В открывшемся окне перетащите ярлык в папку приложений
 *	В процессе установки ОС попросит авторизовать Docker.app с вашим системным паролем. Привилегированный доступ необходим для того, чтобы установить сетевые компоненты и ссылки на Docker apps. Через
 
некоторое время приложение сообщит, что оно готово к работе, и иконка в статус баре примет соответствующий вид.
 *	Docker Desktop for Mac уже включает в себя docker-compose, поэтому отдельно устанавливать его не нужно. Проверить можно, выполнив в окне терминала docker-compose –version

 `Офф. руководство <https://hub.docker.com/editions/community/docker-ce-desktop-mac>`_ 

3.3.	На ОС Linux
~~~~~~~~~~~~~~~~~~~~~
На примере ОС Ubuntu для установки docker и docker-compose
необходимо в эмуляторе терминала выполнить следующие команды:
*	Обновить список пакетов
::

 sudo apt-get update

*	Установить необходимые зависимости
::

 sudo apt-get install \ apt-transport-https \ ca-certificates \
 curl \
 gnupg-agent \
 software-properties-common

* 	Добавить официальный GPG ключ
::

 curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key
 add -

*	Добавить репозиторий
::

 sudo add-apt-repository \
 "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
 $(lsb_release -cs) \
 
 stable"

*	Установить docker-ce
::

 sudo apt-get update
 sudo apt-get install docker-ce docker-ce-cli containerd.io

*	Включить текущего непривилегированного пользователя в группу
docker с полномочиями доступа к демону docker
::

 sudo usermod -aG docker $(whoami)

*	Запустить сервис docker
::

 systemctl start docker

*	Установить автозапуск для сервиса docker
::
 systemctl enable docker

*	Установить docker-compose
::
 sudo	curl	-L "https://github.com/docker/compose/releases/download/1.25.0/docker- compose-$(uname -s)-$(uname -m)" -o 
 /usr/local/bin/docker-compose
 sudo chmod +x /usr/local/bin/docker-compose

`Офф. руководство <https://docs.docker.com/install/linux/docker-ce/ubuntu/>`_ 

4.	Запуск проекта в расширенной конфигурации
----------------------------------------------
4.1.	На ОС Windows
~~~~~~~~~~~~~~~~~~~~~~~~~
 *	Запустите Docker Compose. Запустите Git с повышенными правами
 *	Скачать репозиторий по `ссылке <https://bitbucket.org/citeck/ecos-community-demo/get/4a3f6e5.zip>`_  , распаковать в диске С
 *	Выполнить	команду	cd	c:\ecos-community-demo	(переход	в распакованный архив)
 *	Выполнить переключение на Linux-контейнеры switch to linux containers3
 *	Создайте каталоги для баз данных, выполнив скрипт ./init- volumes-win.bat
 *	Выполнить docker-compose -f docker-compose-win-pv.yaml up -d
 *	Зайти в настройки Docker-compose. Перейти во вкладку Resources
 -> File sharing -> установить чекбокс «диск С»
 *	Необходимо подождать некоторое время (в зависимости от мощности системы) для того, чтобы система запустилась
 *	Перейти в браузере по адресу `localhost <http://localhost/>`_ 
 *	Войти в систему, используя следующие учётные данные: 
Логин – admin | 
Пароль - alfr3sc0

.. attention:: Проект запускается только на Linux-контейнерах
.. attention:: Если значение Switch to Windows, изменять ничего не нужно

4.2.	На ОС Linux или MacOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 •	Установите docker и docker-compose на Вашу ОС
 •	Установите Git для Вашей ОС
 •	Создать каталог "/opt/ecos" и дать на него права в docker4
 •	Скачать репозиторий по `ссылке <https://bitbucket.org/citeck/ecos-community-demo/get/4a3f6e5.zip>`_, распаковать в диске С
 •	Выполнить	команду	**cd c:\ecos-community-demo** (переход в распакованный архив)
 •	Выполнить **docker-compose -f docker-compose-pv.yaml up -d**
 •	Необходимо подождать некоторое время (в зависимости от мощности системы) для того, чтобы система запустилась
 •	Перейти в браузере по адресу http://localhost/
 •	Войти в систему, используя следующие учётные данные: 
Логин – admin | 
Пароль - alfr3sc0

5.	Сервисы Docker
-------------------
В приложенных файлах перечислены сервисы с точки зрения Docker’а и их настройки.

ДОКУМЕНТЫ БУДУТ ПЕРЕНЕСЕНЫ ПОЗЖЕ!

6.	Известные проблемы
------------------------

6.1.	ОС Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
6.1.1.	Порт 8080 уже занят
""""""""""""""""""""""""""""""""
Ecos-ui использует порт 8080 и, если этот порт уже занят другой программой, то можно получить ошибку:
«Error starting userland proxy: listen tcp 0.0.0.0:8080:bind: Only one usage of each socket address is normally permitted.»

.. image:: _static\docker_8080.jpg
       :align: center

Если команда **netstat -ono** (или **netstat -ono | findstr 8080**) не находит, чем занят порт, то нужно скачать программу, например, CurrPorts и уже с ее помощью найти занятые порты.

6.1.2.	Порт зарезервирован Windows
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
К примеру, каталог ecos-postgres использует порт 50432, но этот порт зарезервирован Windows. Проверить такие порты можно командой **netsh int ipv4 show excludedportrange protocol=tcp.**

.. image:: _static\docker_port_win.jpg
       :align: center

Команда покажет диапазон зарезервированных портов. Видно, что порт 50432 находится в данном диапазоне и поэтому при установке была получена ошибка:
«Cannot start service ecos-postgress: driver failed proogramming external
connectivity on endpoint»
Чтобы это исправить, нужно в командной строке, запущенной с повышенными правами:

1)	Остановить Hyper-V::
 
 dism.exe /Online /Disable-Feature:Microsoft-Hyper- V 
 (выполнить перезагрузку)
2)	Добавить	нужный	порт	в	исключения::

 netsh	int	ipv4	add excludedportrange protocol=tcp startport=50432 numberofports=1

3)	Запустить Hyper-V::
 dism.exe /Online /Enable-Feature:Microsoft-Hyper-V
 /All 
 (после потребуется перезагрузка)

Порт попадет в исключения, и подобной ошибки не возникнет.

6.1.3.	Если не удается выполнить switch to Linux Containers
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
•	Необходимо открыть Windows Security (Защитник Windows)
•	Открыть App & Browser control (Упр. Приложениями и Браузером)
•	Перейти в Защита от эксплойтов
•	Перейти в параметры программ
 
•	Найти	или	добавить	в	исключения
"C:\WINDOWS\System32\vmcompute.exe"
•	Запустить powershell. Выполнить команду **vmcompute**

6.1.4.	Docker не запускается из-за нехватки памяти
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
При запуске может возникнуть ошибка запуска Docker Desktop

.. image:: _static\docker_memory_1.jpg
       :align: center

Чтобы решить эту проблему нужно выделить Докеру больше памяти:

1)	В системном трее нужно отыскать значок Docker. ПКМ -> Settings.

.. image:: _static\docker_memory_2.jpg
       :align: center

2)	Вкладка Advansed, ползунок Memory. Выделить хотя бы 4 Гб и нажать
**Apply**:

.. image:: _static\docker_memory_3.jpg
       :align: center

Если проблема продолжает возникать, то нужно завершить ресурсоёмкие процессы и/или дать Docker`у чуть меньше памяти (3-3,5 Гб).
