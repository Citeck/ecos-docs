Создание пользователей для ecos-community-demo
===============================================

.. note::

      ECOS может быть настроен для работы со службой LDAP.
      Так же пользователи могут быть созданы через Keycloak.

.. _demo_user:

Создание пользователя в Keycloak
----------------------------------

На запущенном проекте перейти по ссылке `http://ecos-community-demo/ecos-idp/auth <http://ecos-community-demo/ecos-idp/auth>`_

Перейти в раздел **Administration Console**:

 .. image:: _static/new_user/User_1.png
       :width: 600
       :align: center

|

 .. image:: _static/new_user/User_2.png
       :width: 400
       :align: center

Для входа в Keycloak используйте логин и пароль: **admin/VeryStrongPassword**


 .. image:: _static/new_user/User_3.png
       :width: 600
       :align: center

Перейдите в **Users**. По кнопке **View all users** можно посмотреть список всех пользователей.

 .. image:: _static/new_user/User_4.png
       :width: 600
       :align: center

Для добавления пользователя нажмите **Add user**:

 .. image:: _static/new_user/User_5.png
       :width: 600
       :align: center

Введите данные и нажмите **Сохранить**.

Для ввода пароля необходимо перейти во вкладку **Credentials**, ввести и подтвердить пароль.

 .. image:: _static/new_user/User_6.png
       :width: 600
       :align: center

Если пароль необходимо сделать временным, то выставите **Temporary ON**.

Нажмите **Set Password** и подтвердите:

 .. image:: _static/new_user/User_7.png
       :width: 400
       :align: center

Далее необходимо залогиниться под созданным пользователем в ECOS. В ECOS будет передано **имя пользователя**, остальные данные необходимо ввести дополнительно.

Ввод дополнительных данных пользователя в ECOS
------------------------------------------------

Перейдите в **Пользователи**, откройте созданного пользователя в режиме редактирования:

 .. image:: _static/new_user/User_8.png
       :width: 600
       :align: center

Введите обязательно **имя** и **электронную почту**, заполните остальные поля при необходимости:

 .. image:: _static/new_user/User_9.png
       :width: 600
       :align: center

Далее пользователей необходимо добавить в **Группы** EVERYONE и **_orgstruct_home_** - нажмите **Выбрать** и выберите группы **EVERYONE** и **_orgstruct_home_**:

 .. image:: _static/new_user/User_10.png
       :width: 600
       :align: center

|

 .. image:: _static/new_user/User_11.png
       :width: 600
       :align: center


Для сохранения нажмите **Submit**

Пользователю будут выданы права в соответствии с выбранными группами.
