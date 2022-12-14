.. _keycloak_postman:

Настройки аутентификации для работы с Records API из внешних систем
===================================================================

В статье описана последовательность настроек ECOS для обеспечения корректной отправки http-запросов Records API.
На примере Postman описана аутентификация в ECOS через OAuth 2.0 и отправка запросов.

Получение и работа с Client ID и Client Secret в Keycloak
-----------------------------------------------------------------------

Для получения токена для отправки запросов необходимо выполнить следующую последовательность действий:

1.	В **keycloak** создать клиента, из которого будет взят **Client ID** и **Client Secret**, которые будут использованы для получения bearer-токена.
2.	Cоздать пользователя в ECOS по паттерну ``service-account-%имя созданного клиента%`` (знак % указывает, что переменная шаблонная. В самом имени указывать их не нужно).

Создание клиента в Keycloak
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.	Зайти в админскую консоль keycloak. 
URL для доступа: ``%host%/auth/admin/master/console/`` 

2.	Выбрать необходимый реалм. 

 .. image:: _static/keycloack_postman/Keycloack_1.png
       :width: 700
       :align: center
 
3.	После перехода в реалм выбрать вкладку :guilabel:`clients`. Как видно на скриншоте, клиент service_qa уже создан. Пример создания будет на пункт ниже, но само конфигурирование будет показано на уже существующем service_qa.

 .. image:: _static/keycloack_postman/Keycloack_2.png
       :width: 600
       :align: center

4.	Нажать кнопку :guilabel:`Create`

 .. image:: _static/keycloack_postman/Keycloack_3.png
       :width: 700
       :align: center

5.	На появившемся окне заполнить только **Client ID**, сохранить его куда-нибудь и нажать :guilabel:`Save`

 .. image:: _static/keycloack_postman/Keycloack_4.png
       :width: 600
       :align: center

6.	Откроется окно редактирования клиента. Для примера был создан клиент с **Client ID test**

 .. image:: _static/keycloack_postman/Keycloack_5.png
       :width: 600
       :align: center

7.	Заполнить вкладку :guilabel:`Settings` клиента согласно скриншоту ниже

**Access Type**: confidential
**Service Account Enabled**: true
**Valid Redirect URLs**: Указывать URL'ы, которые нужны для использования. Для тестов можно просто указать * (На продуктивных средах так делать крайне не рекомендуется!)

В самом низу страницы нажать :guilabel:`Save`.

 .. image:: _static/keycloack_postman/Keycloack_6.png
       :width: 700
       :align: center

8.	Открыть вкладку :guilabel:`Credentials`, найти поле **Secret**. Это и есть **Client Secret**. Сохранить его себе туда же, где был сохранен Client ID в п.5. 
В случае компроментирования, или любой другой необходимости, его можно перегенерировать, используя кнопку :guilabel:`Regenerate Secret`.

 .. image:: _static/keycloack_postman/Keycloack_7.png
       :width: 700
       :align: center

Cоздание пользователя в ECOS
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1.	Перейти в соответствующий реалм ecos. Открыть пункт меню **“Пользователи”**, для добавления нового пользователя нажать кнопку :guilabel:`+`:

 .. image:: _static/keycloack_postman/Keycloack_8.png
       :width: 700
       :align: center

2.	Заполнить форму. 

Заполнить поле **“Системное Имя”** по паттерну ``service-account-%имя созданного клиента%``. Остальные поля можно не заполнять, так как пользователь сервисный и заходить под ним никто не будет.

 .. image:: _static/keycloack_postman/Keycloack_9.png
       :width: 700
       :align: center
 
3.	Теперь можно совершать запросы к системе через gateway.


Отправка запросов в ECOS
-----------------------------

При работе с системой ECOS используется авторизация OAuth 2.0. 
Для отправки запросов ее также нужно настроить в Postman, SoapUI или другом инструменте тестирования, который вы используете.

Рассмотрим настройку на примере Postman. 

1.	Перейти на вкладку авторизации и выбрать тип **OAuth 2.0**.
 
 .. image:: _static/keycloack_postman/Postman_1.png
       :width: 700
       :align: center

2.	В разделе :guilabel:`Current Token` указать префикс **Bearer**.

 .. image:: _static/keycloack_postman/Postman_2.png
       :width: 700
       :align: center
 
3.	Далее в разделе :guilabel:`Configure New Token` указать тип выдачи прав **Client Credentials** и **URL откуда запрашивать токен авторизации**. 
 
 .. image:: _static/keycloack_postman/Postman_3.png
       :width: 700
       :align: center
       
4.	Указать **Client ID** и **Client Secret**. Задать имя токена, имя может быть любым. 
 
 .. image:: _static/keycloack_postman/Postman_4.png
       :width: 700
       :align: center

5.	В настройке **Client Authentication** установить значение **Send as Basic Auth header** для отправки токена в заголовке. 
Попробовать получить токен и указать и использовать его в запросе, в результате значение токена подставится в раздел :guilabel:`Current Token`.

 .. image:: _static/keycloack_postman/Postman_5.png
       :width: 700
       :align: center

 .. image:: _static/keycloack_postman/Postman_6.png
       :width: 700
       :align: center
 
 .. image:: _static/keycloack_postman/Postman_7.png
       :width: 700
       :align: center

6.	Если тело запроса заполнено, то можно выполнять основной запрос на стенд. Срок действия токена можно посмотреть при его получении. 

 .. image:: _static/keycloack_postman/Postman_8.png
       :width: 700
       :align: center

В дальнейшей работе по истечении срока действия токена его нужно обновить, повторно нажав **Get New Access Token → Use Token**.


