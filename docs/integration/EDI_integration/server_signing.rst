Серверное подписание
====================

В микросервисе ecos-integrations начиная с версии 2.3.5 добавлен функционал серверного подписания документов электронной подписью без использования плагина **КриптоПро ЭЦП Browser plug-in**.

Для этого был разработан дополнительный сервис **ecos-crypto-sign** (репозиторий `https://gitlab.citeck.ru/citeck-projects/ecos-crypto-sign <https://gitlab.citeck.ru/citeck-projects/ecos-crypto-sign>`_)

Общая схема работы:

 .. image:: _static/server_signing/server_signing_1png.png
       :width: 600
       :align: center

Описание 
----------

1. Клиент API аутентифицируется в KeyCloak. KeyCloak выдает токен.

2. Клиент API передает свой запрос в ecos-proxy, указав в заголовке токен.

3. Компонент ecos-proxy проверяет токен в KeyCloak. Если токен валидный - пропускает запрос дальше. Иначе - ошибка.

4. Компонент ecos-proxy маршрутизирует запрос на целевой микросервис ecos-gateway. Заголовок с токеном транслируется.

5. Этот микросервис маршрутизирует запрос на один из доступных микросервисов ecos-integrations. Заголовок с токеном транслируется.

6. Микросервис интеграций отправляет запрос в микросервис подписания. Заголовок с токеном транслируется.

7. Микросервис подписания проверяет токен в KeyCloak. Если токен валидный - происходит подписание. Иначе - ошибка. Возврат ответа клиенту API

Сервис подписания это стандартное spring-boot приложение.

На данный момент доступно 2 REST запроса:

**Подписание контента**

.. code-block::

    {host:port}/ecos/crypto/sign

headers: 

.. code-block::

    Authorization: Bearer access_token //keycloak bearer access token

body:

.. code-block::

    {
        "documentContent":"QQMTIzNDU2Nzg5",
        "keyStoreInfo":{
            "providerType":"JCSP",
            "keyStoreType":"FAT12_D"
        },
        "certificateInfo":{
            "pin":"1",   
            "alias":"null",
            "serialNumber":"5927a700f7ac223d9548e8628fe9c2c302",
            "thumbprint":"A14BFD6503EFD7116AFCE95A6FAA2097E0883DEAD811",
            "signatureAlgorithm":""
        }
    }

* **documentContent** - Контент для подписания (Base64 encoded byte[])

* **providerType** - Тип провайдера (По умолчанию у нас используется JCSP)

* **keyStoreType** - Тип хранилища сертификата (Например HDD в разделе D, как в текущем примере или registry и т.д.)

* **pin** - пароль от контейнера для получения приватного ключа

* **alias** - alias сертификата для поиска нужного сертификата для подписи

* **serialNumber** - серийный номер сертификата? если **alias** не известен

* **thumbprint** - отпечаток сертификата, используется **alias** и **serialNumber**  неизвестны

* **signatureAlgorithm** - алгоритм подписи (в данный момент передаваемый алгоритм не используется, берется из найденного сертификата)

В текущей реализации сертификат ищется:

1. Во-первых по aliasу (если он не пустой, если пустой, то пропускаем данный шаг)

2. Если не найден, то по серийному номеру (если он не пустой, если пустой, то пропускаем данный шаг)

3. Если опять не найден, то по отпечатку (если пустой и сертификат не найден, то возвращаем ошибку подписания)

Ожидаемый ответ:

.. code-block::

    {
        "success": true,
        "error": "",
        "signatureContent": "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"
    }

* **success** - результат выполнения rest запроса (успешно/неуспешно)

* **error** - Строка ошибки (При ошибке подписания)

* **signatureContent** - контент полученной подписи (Base64 encoded byte[])

При подписании создается подпись в формате CMS. Возвращается зашифрованная в Base64 строка подписи (аналогично подписанию через плагин).

**Валидация подписи**

.. code-block::

    {host:port}/ecos/crypto/signVerify

headers: 

.. code-block::

    Authorization: Bearer access_token //keycloak bearer access token

body:

.. code-block::

    {
        "documentContent":"QQMTIzNDU2Nzg5",
        "signatureContent":"MIIMoQYJKoZIh",
        "keyStoreInfo":{
            "providerType":"JCSP",
            "keyStoreType":"FAT12_D"
        },
        "certificateInfo":{
            "pin":"1",
            "alias":null,
            "serialNumber":"5927a700f713a4c2d9548e8628fe559c2c302",
            "thumbprint":"A14BFD6503E123FD76AFCE95A6FAA2097E0883DEAD811"
            "signatureAlgorithm":"GOST3411_2012_256withGOST3410DH_2012_256"
        }
    }

* **documentContent** - Контент, который был подписан (Base64 encoded byte[])

* **signatureContent** - Непосредственно сама подпись (Base64 encoded byte[])

* **providerType** - Тип провайдера (По умолчанию у нас используется JCSP)

* **keyStoreType** - Тип хранилища сертификата (Например HDD в разделе D, как в текущем примере или registry и т.д.)

* **pin** - пароль от контейнера для получения приватного ключа

* **alias** - alias сертификата для поиска нужного сертификата для подписи

* **serialNumber** - серийный номер сертификата если **alias** неизвестен

* **thumbprint** - отпечаток сертификата, используется если **alias** и **serialNumber** неизвестны

* **signatureAlgorithm** - алгоритм подписи (в данный момент передаваемый алгоритм не используется, берется из найденного сертификата)

В текущей реализации сертификат ищется:

1. Во-первых по aliasу (если он не пустой, если пустой, то пропускаем данный шаг)

2. Если не найден, то по серийному номеру (если он не пустой, если пустой, то пропускаем данный шаг)

3. Если опять не найден, то по отпечатку (если пустой и сертификат не найден, то возвращаем ошибку подписания)

Ожидаемый ответ:

.. code-block::

    {
        "success": true,
        "error": "",
        "result": true
    }

* **success** - результат выполнения rest запроса (успешно/неуспешно)

* **error** - Строка ошибки (При ошибке валидации)

* **result** - результат валидации подписи

Проверку токена можно отключить выставив соответствующие свойства:

В микросервисе интеграции: **ecos-integrations.server-sign.keycloak.isTokenCheckEnabled**

В сервисе подписания: **keycloak.enabled**

Полный конфиг настроек keycloak сервиса подписания:

.. code-block::

    keycloak:
        enabled: true
        auth-server-url: http://localhost:8484/auth
        realm: "master"
        resource: "service_client"
        bearer-only: true
        security-constraints:
          - authRoles:
              - uma_authorization
          securityCollections:
              - patterns:
                  - /ecos/*

* **enabled** - включена/отключена проверка токена перед подписью/валидацией

* **auth-server-url** - адрес эндпоинта auth для keycloak

* **realm** - realm для которого происходит проверка токена.

* **resource** - ID клиента к которому необходим доступ (В данном сервисе неактуально, можно добавить любого валидного клиента в указанном realm)

* **bearer-only** - если выставлено true, то приложение может только проверять токены, и в приложении нельзя будет залогиниться

* **security-constraints** - для описания ролевой политики

    - **authRoles** - список ролей Keycloak (uma_authorization по умолчанию, так как она выдается всем клиентам)

    - **securityCollections**

        * **patterns** - URL-паттерны для методов REST API, которые требуется закрыть соответствующими ролями (в данном случае два метода /ecos/'*')

Конфиг дополнительных настроек для микросервиса интеграции:

.. code-block::

    ecos-integrations:
    server-sign:
        root-uri: http://localhost:8083
        keycloak:
            host: http://localhost
            port: 8484
            client-id: service_client
            client-secret: 5307e923-570b-4fed-ad18-cc6320056bf9
            realm: master
            isTokenCheckEnabled: false
            isTrustAllEnabled: false

* **root-uri** - адрес сервиса подписания

* **keycloak.host**  - host keycloak

* **keycloak.port**  - порта keycloak

* **keycloak.client-id**  - id сервисного клиента keycloak

* **keycloak.client-secret**  - secret сервисного клиента keycloak

* **keycloak.realm**  - realm для которого происходит проверка токена.

* **keycloak.isTokenCheckEnabled**  - при включенном флаге в сервис подписания передается access токен сервисного клиента

* **keycloak.isTrustAllEnabled**  - включение/отключение политики TrustAll при запросе токена у кейклока (выставляется в true если падает ошибка доступа, однако нужно учитывать что в таком случае появляется уязвимость)

Создание сервисного клиента keycloak
-------------------------------------

Сервисного клиента необходимо создать в соответствующем realm keycloak. Он необходим для получения access токена.

1. Зайти в консоль администратора непосредственно на сервер keycloak

2. Переключится на нужный realm

3. Пункт **Clients → Добавить нового (Имя клиента - любое) → Cоздать**

4. Пункт **Access Type = confidential**

5. Флаг **Service Accounts Enabled = true**

6. **Valid Redirect URIs** - добавит любой uri редиректа на основной сервер alfresco, хотя в данном случае это не обязательно, так как от клиента нам нужен лишь токен и не нужны ресурсы

7. Save

После этого на вкладке **Credentials** данного клиента можно найти его secret, id же является заданное нами имя.

Запрос из ecos
--------------

Для того чтобы можно было запрашивать валидацию подписи и подписывание любого контента в микросервисе интеграции были реализованы соотвествующие **RecordsDao**

**Подписание - ServerSignRecords**

ID - “server-sign“

Dto - SignRequest

.. code-block::

    public class SignRequest {
        private String documentContent;
        private KeyStoreInfo keyStoreInfo;
        private CertificateInfo certificateInfo;
    }

CertificateInfo:

.. code-block::

    public class CertificateInfo {
        private String pin;
        private String alias;
        private String serialNumber;
        private String thumbprint;
        private String signatureAlgorithm;
    }

KeyStoreInfo:

.. code-block::

    public class KeyStoreInfo {
        private String providerType;
        private String keyStoreType;
    }

Пример запроса из консоли браузера:

.. code-block::

    Citeck.Records.query(
        {
            sourceId: "integrations/server-sign",
            query: {
                "documentContent":"MTIzNDU2Nzg5",
                "keyStoreInfo":{
                    "providerType":"JCSP",
                    "keyStoreType":"FAT12_D"
                },
                "certificateInfo":{
                    "pin":"1",
                    "alias":null,
                    "serialNumber":"",
                    "thumbprint":"A1424BFD6503EFD7236AFCE95A1236FAA2097E0883DEAD8123",
                    "signatureAlgorithm":""
                }
            }
        },{
        signatureContent: "signatureContent",
        error: "error"
        }
    ).then(res => console.log(res));

**Валидация - ServerSignVerificationRecords**

ID - “server-sign-verify“

Dto - SignVerifyRequest

.. code-block::

    public class SignVerifyRequest {
        private String documentContent;
        private String signatureContent;
        private KeyStoreInfo keyStoreInfo;
        private CertificateInfo certificateInfo;
    }

CertificateInfo:

.. code-block::

    public class CertificateInfo {
        private String pin;
        private String alias;
        private String serialNumber;
        private String thumbprint;
        private String signatureAlgorithm;
    }

KeyStoreInfo:

.. code-block::

    public class KeyStoreInfo {
        private String providerType;
        private String keyStoreType;
    }

Пример запроса из консоли браузера:

.. code-block::

    Citeck.Records.query(
        {
            sourceId: "integrations/server-sign-verify",
            query: {
                "documentContent":"MTIzNDU2Nzg5",
                "signatureContent":"asdasdfbvhadsfbdhasbfks",
                "keyStoreInfo":{
                    "providerType":"JCSP",
                    "keyStoreType":"FAT12_D"
                },
                "certificateInfo":{
                    "pin":"1",
                    "alias":null,
                    "serialNumber":"",
                    "thumbprint":"A14BFD6503EFD1276AFCE952A6FAA205197E0883DEAD813",
                    "signatureAlgorithm":""
                }
            }
        },{
        result: "result",
        error: "error"
        }
    ).then(res => console.log(res));

Для локального запуска функционала необходимо клонировать репозиторий **ecos-crypto-sign** и запустить приложение **CryptoSignApp**

Недостающие библиотеки (при возникновении ошибок компиляции и NoClassDefFoundException) можно взять с официально сайта КриптоПро

Необходимо установить в нужную jre функционал JCP + JCSP

