
.. _data_sources:

Источники данных
=================

REST Data Source
-----------------

Источник данных, который работает через Rest запросы

 .. image:: _static/data_sources/data_sources_1.png
       :width: 600
       :align: center

* **Id** - идентификатор источника
* **Name** - произвольное имя
* **URL** - адрес, по которому будут отправляться запросы Есть поддержка переменных запроса в фигурных скобках - *{key}*
* **Internal** - запрос будет отправляться только в сети микросервисов зарегистрированных в Eureka (в таких запросах прокидываются header'ы и cookie)
* **HTTP Method** - можно выбрать методы http post, get, put и т.д.
* **Request headers** - заголовки запроса. Есть поддержка переменных запроса в фигурных скобках - *${key}*
* **Request body** - тело запроса. Есть поддержка переменных запроса в фигурных скобках - *${key}*
* **Json response transform specification** - Спецификация, которая описывает преобразование ответа. Формат спецификации - `Jolt  <https://jolt-demo.appspot.com/>`_

DB Data Source
-----------------

Источник данных из базы данных.

SSL при запросах к бд через ECOS db-data-source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**1. Общая информация по настройке**

Начиная с версии 2.8.0 микросервиса интеграции - появилась возможность указывать в конфиге на форме **DataSource** следующие параметры:

Можно использовать при настройке внешней БД в **recsrc**.

 .. image:: _static/data_sources/data_sources_2.png
       :width: 400
       :align: center

Общий принцип таков, что исходя из конфига - создается **HikariDataSource**.

При указании данных свойств - в наш создаваемый **HikariDataSource** попадут дополнительные атрибуты, которые принудят используемый драйвер ходить не по http, а по https.

Доступные сейчас режимы:

* **none** - флаг ssl выключен, поля НЕ заполнены. Ходим по HTTP протоколу (трафик не защищен).
* **require** - флаг ssl включен, остальные поля НЕ заполнены. Ходим по HTTPS, трафик защищен шифрованием, но мы не проверяем что БД именно та, которой мы доверяем. БД так же не уверена что соединяется с нашим приложением.
* **verify-ca** - флаг ssl включен, SSL root cert path и SSL cert path указаны, SSLkey path не указан. Ходим по HTTPS, трафик защищен шифрованием. Мы знаем что БД именно та, к которой мы хотим подключиться (при успехе рукопожатия). БД еще не уверена что соединяется с нашим приложением.
* **verify-full** - флаг ssl включен, остальные поля заполнены. Ходим по HTTPS, трафик защищен. Мы уверены в БД, а БД уверена в нас. 

Более подробно по настройкам можно посмотреть тут: `Configuring the Client <https://jdbc.postgresql.org/documentation/head/ssl-client.html>`_ и тут: `Connecting to the Database <https://jdbc.postgresql.org/documentation/head/connect.html#ssl>`_ Connecting to the Database.

Настройки со стороны БД описаны тут:  `SSL Support <https://www.postgresql.org/docs/9.0/libpq-ssl.html>`_ 

.. important:: 

    ВАЖНО! Тестировались только варианты require и verify-ca для БД Postgres.

**2. Подъем БД в докере с возможностью общаться по HTTPS**

Для каждой системы подход прокидывания сертификатов в образ контейнера будет разный, так как постгрису важно чтоб на файл еще были минимальные права (640 и меньше от рута, 600 и меньше при запуске в других случаях).

Расскажу как обойти это на примере Windows.

В Windows, к сожалению, такой контейнер в докере можно запустить только собирая его сразу с сертификатами.

1. Сгенерим ключи и серт:

.. code:: 

    openssl genrsa -out root.key 2048
    openssl req -x509 -new -key root.key -days 10000 -out root.crt
    openssl genrsa -out server.key 2048
    openssl req -new -key server.key -out server.csr
    openssl x509 -req -in server.csr -CA root.crt -CAkey root.key -CAcreateserial -out server.crt -days 5000

2. Добавить в директорию с сертификатами DockerFile:

.. code:: 

    FROM postgres:10.4-alpine

    # On Windows root will own the files, and they will have permissions 755
    COPY root.crt /var/lib/postgresql/root.crt
    COPY server.crt /var/lib/postgresql/server.crt
    COPY server.key /var/lib/postgresql/server.key

    # update the privileges on the .key, no need to touch the .crt  
    RUN chmod 600 /var/lib/postgresql/server.key
    RUN chown postgres:postgres /var/lib/postgresql/server.key

3. Собираем и запускаем:

.. code:: 

    docker build -t mypg:01 .

    docker run -e "POSTGRES_USER=test_user" -e "POSTGRES_PASSWORD=test_password" -p 5430:5432 -d --name postgres mypg:01 -c ssl=on -c ssl_cert_file=/var/lib/postgresql/server.crt -c ssl_key_file=/var/lib/postgresql/server.key

**3. Проверка соединения**

Проверить клиентов и признак использования шифрования с их стороны можно с помощью SQL скрипта:

.. code:: 

    SELECT * 
    FROM pg_stat_ssl
    JOIN pg_stat_activity
        ON pg_stat_ssl.pid = pg_stat_activity.pid;


MQ Data Source
---------------

Источник данных для подключения к очереди сообщений

 .. image:: _static/data_sources/data_sources_3.png
       :width: 600
       :align: center

* **Id** - идентификатор источника данных
* **Name** - произвольное имя источника данных
* **URI** - строка для подключения к очереди
* **Type** - тип очереди
* **Credentials** - ссылка на credentials где указаны login/pass для подключения к очереди