How To
=======

Изменить http://ecos-community-demo на http://mydomain.ru
-----------------------------------------------------------

С чистой БД
~~~~~~~~~~~~~~~~~~

Поменять в:

1. **ecos-community-demo/services/environments/ecos-identity-app.env**

.. code-block::

 KEYCLOAK_FRONTEND_URL=http://ecos-community-demo/ecos-idp/auth 

на 

.. code-block::

    KEYCLOAK_FRONTEND_URL=http://mydomain.ru/ecos-idp/auth

2. **ecos-community-demo/services/environments/ecos-proxy-app.env**

.. code-block::

    EIS_ID=ecos-community-demo на EIS_ID=mydomain.ru + REDIRECT_LOGOUT_URI=http://ecos-community-demo 

на 

.. code-block::

    REDIRECT_LOGOUT_URI=http://mydomain.ru

3. Шаг имеет смысл, если разворачивать на чистых БД:

**ecos-community-demo/services/configs/ecos-identity-app/realm-export.json**

.. code-block::

    "redirectUris": [
        "http://ecos-community-demo*"
    ],

на

.. code-block::

    "redirectUris": [
        "http://mydomain.ru*"
    ],
    
4. Шаг имеет смысл, если разворачивать на чистых БД:

**ecos-community-demo/services/configs/ecos-identity-app/realm-export.yaml**

.. code-block::

    "redirectUris": [
        "http://ecos-community-demo*"
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
~~~~~~~~~~~~~~~~~~

1. Зайти в панель администратора keycloak.
2. Открыть реалм **ecos-app**.
3. Открыть раздел **clients**.
4. Открыть **ecos-proxy-app**.
5. Изменить в поле **Valid Redirect URIs** значение http://ecos-community-demo на http://mydomain.ru
6. Сохранить.


Исключить адрес из авторизации Keycloak
-----------------------------------------

Временно можно сделать на уровне модификации **Ecos-Proxy-APP**.

Проверить можно,  зайдя в контейнер: 

**docker-compose exec ecos-proxy-app /bin/bash**

и модифицировав: 

**/etc/nginx/conf.d/default.conf**

После этого выполнить:

.. code-block::

    nginx -s reload

На постоянной основе только собрав свою версию контейнера **ecos-proxy-app**

Второй вариант: предложив Pull-реквест нам с возможностью передавать не защищаемые URL в качестве параметра.