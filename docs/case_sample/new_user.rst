Создание пользователей для ecos-community-demo
===============================================

Создание пользователя в Keycloack
----------------------------------

На запущенном проекте перейти по ссылке `http://ecos-community-demo/ecos-idp/auth <http://ecos-community-demo/ecos-idp/auth>`_

Перейти в **Administration Console**:

 .. image:: _static/new_user/User_1.png
       :width: 600
       :align: center

|

 .. image:: _static/new_user/User_2.png
       :width: 400
       :align: center

Логин и пароль для входа в Keycloack: **admin/VeryStrongPassword**


 .. image:: _static/new_user/User_3.png
       :width: 600
       :align: center

Перейти в **Users**. По кнопке **View all users** можно посмотреть список всех пользователей.

 .. image:: _static/new_user/User_4.png
       :width: 600
       :align: center

Для добавления пользователя нажать **Add user**:

 .. image:: _static/new_user/User_5.png
       :width: 600
       :align: center

Ввести данные. **Сохранить**.

Для ввода пароля перейти во вкладку **Credentials**, ввести и подтвердить пароль.

 .. image:: _static/new_user/User_6.png
       :width: 600
       :align: center

Если пароль необходимо сделать временным, то выставить **Temporary ON**.

Нажать **Set Password**. Подтвердить:

 .. image:: _static/new_user/User_7.png
       :width: 400
       :align: center

Далее необходимо залогиниться под созданным пользователем в ECOS.
В ECOS будет передано имя пользователя, остальные данные необходимо ввести дополнительно.

Создание пользователя в ECOS
-----------------------------

Перейти в **Пользователи**, открыть созданного пользователя в режиме редактирования:

 .. image:: _static/new_user/User_8.png
       :width: 600
       :align: center

Ввести обязательно имя и электронную почту, заполнить остальные поля при необходимости:

 .. image:: _static/new_user/User_9.png
       :width: 600
       :align: center

Далее необходимо добавить пользователя в **Группы** EVERYONE и _orgstruct_home_

Нажать **Выбрать** и выбрать группы **EVERYONE** и **_orgstruct_home_**:

 .. image:: _static/new_user/User_10.png
       :width: 600
       :align: center

|

 .. image:: _static/new_user/User_11.png
       :width: 600
       :align: center


Для сохранения нажать **Submit**

Пользователю будут выданы права в соответствии с выбранными группами.
