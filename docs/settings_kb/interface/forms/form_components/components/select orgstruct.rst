.. _Select_orgstruct:

Select orgstruct
================

.. contents::
   :depth: 4
   
Настройка доступных для выбора элементов
-----------------------------------------

 .. image:: _static/select_orgstruct/select_orgstruct_1.png
       :width: 600
       :align: center

**Таб по умолчанию: Все пользователи, По уровням** - таб, показываемый по умолчанию:

 .. image:: _static/select_orgstruct/select_orgstruct_2.png
       :width: 500
       :align: center

**Разрешенный тип полномочий/Allowed authority type** - типы элементов, доступные до выбора. Доступные значения: **USER** - пользователи, **GROUP** - группы. Можно указать оба типа через запятую.

**Разрешенный тип группы/Allowed group type** - типы групп, доступных для выбора. Работает в случае, если **Allowed authority type** содержит **'GROUP'**. Можно указать несколько групп через запятую.

**Разрешенный подтип группы/Allowed group subtype** - типы подгрупп, доступных для выбора. Можно указать несколько подгрупп через запятую. Если поле заполнено, для выбора будут доступны только те элементы, которые проходят фильтр по этому полю, остальные группы выбрать нельзя.


Скрытие групп и подгрупп
------------------------

 .. image:: _static/select_orgstruct/select_orgstruct_3.png
       :width: 500
       :align: center

**Исключить авторитеты по имени/Exclude authorities by name** -  список групп, перечисленных через запятую, для фильтрации по имени . Группы, добавленные в это поле, и все их дочерние элементы не отображаются в оргструктуре

Для того чтобы дочерние группы скрытых групп не появлялись в результатах поиска была добавлена следующая нотация:
``GROUP_NAME/*`` - для того чтобы убрать дочерние элементы только первого уровня
``GROUP_NAME/**`` - для того чтобы убрать дочерние элементы на любом уровне вложенности

**Исключить авторитеты по типу или подтипу группы/Exclude authorities by group type or subtype** - список групп, перечисленных через запятую, для фильтрации по типу. Элементы, соответствующие этим типам, не отображаются в оргструктуре.

Настройка полей для поиска пользователя
-----------------------------------------

.. note::

    Пользовательские значения по умолчанию:
    ``value = user;``

По-умолчанию поиск пользователей осуществляется по трём полям: **cm:userName, cm:firstName и cm:lastName**. Есть два варианта расширить список полей для поиска пользователей:

* локальная настройка **Поиск пользователя: дополнительное поле/User search: extra fields** на вкладке :guilabel:`Кастомные`. Настройка доступна только в случае, если в поле **Allowed authority type** содержится вариант **USER**.
  
* глобальная настройка ``uiserv/config@orgstruct-search-user-extra-fields``
  
 Добавить в проект конфигурационный json-файл (``alfresco\module\{module-name}\ui\config\``) с содержимым:

.. code-block::
    
    {
        "id": "orgstruct-search-user-extra-fields",
        "title": "SelectOrgstruct user search: extra fields",
        "value": "someFieldName1,field:name2"
    }
 
либо выполнить в консоли команду (вариант подходит только для отладочных целей, при обновлении сервера настройка может сброситься):
 
.. code-block::

    const config = Citeck.Records.get('uiserv/config@orgstruct-search-user-extra-fields');
    config.att('value', 'someFieldName1,field:name2');
    config.save();

В обоих случаях в качестве значения принимается строка с названиями полей, разделёнными между собой запятыми.

* глобальная настройка ``uiserv/config@orgstruct-search-user-middle-name`` для использования Отчества при поиске пользователей 
  
 Добавить в проект конфигурационный json-файл (``alfresco\module\{module-name}\ui\config\``) с содержимым:

.. code-block::
    
    {
        "id": "orgstruct-search-user-middle-name",
        "title": "SelectOrgstruct user search with cm:middleName",
        "value": true
    }

.. code-block::

Прочее
--------

 .. image:: _static/select_orgstruct/select_orgstruct_3.png
       :width: 500
       :align: center

**Current user by default** - в случае, если флажок отмечен, по умолчанию будет установлено значение с **id** текущего пользователя. Работает только для форм в режиме создания записи ('CREATE').
