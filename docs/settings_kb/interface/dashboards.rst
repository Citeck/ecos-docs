Дашборды
=========

Для отображения домашней страницы пользователя или информации по кейсу, или информации по сайту в ECOS предусмотрены дашборды.

Дашборд позволяет добавлять и убирать виджеты, конфигурировать каждый виджет индивидуально. См. отдельную статью <Виджеты>

Все настройки хранятся в том же json, что и конфигурация дашборда. 

Виды дашбордов
---------------
На момент написания статьи существует 3 вида dashboard:

.. list-table:: 
      :widths: 5 40
      :header-rows: 1

      * - Тип/Ключ
        - Описание
      * - **Case-details**
        - | Дашборд карточки кейса - информация по документу (задачи, свойства, действия, история и др.). 
          | Ключ dashboard'а берется из **RecordRef** в URL страницы и как правило он связан с типом/видом ECOS. 
          | Формирование ключа построено по следующему правилу:
          | **type_uuid/kind_** 
          | **type_uuid**
          | **alf_alfresco_type**	
          | То есть для договоров (contracts:agreement) это будет:  
          | 1. **contracts-cat-doctype-contract/contracts-cat-contract-rent**	
          | 2. **contracts-cat-doctype-contract**	
          | 3. **alf_contracts:agreement**  
          | Порядок - от более приоритетного к менее приоритетному	
      * - **Site-dashboard**
        - | Страница раздела, которая позволяет отображать общие данные по разделу. Например - профиль пользователя.
          | Ключ dashboard'а берется из **RecordRef** в URL страницы. На момент написания ключ формируется по правилу **"site"** + **siteId**.
          | Если идентификатор сайта **contracts**, то его приоритетный dashboardKey будет **site_contracts**. 
      * - **User-dashboard**
        - | Домашняя страница пользователя. Открывается если в URL не указано никакого **recordRef**.
          | Например: ``localhost/v2/dashboard`` 	
          | Ключ dashboard'а всегда DEFAULT если явно не задано обратного (возможно указание dashboardKey в URL) 

Алгоритм поиска dashboard следующий:

1. Смотрим наличие **recordRef** в URL,
2. Если **recordRef** отсутствует - отправляется запрос на конфигурацию домашней страницы пользователя,
3. Если **recordRef** присутствует, то запрашиваем аттрибуты **_dashboardKey[]** (массив) и **_dashboardType** (одно значение),
4. Дальше перебираем каждый полученный **dashboardKey** и запрашиваем у сервера конфигурацию для ключа + типа,
5. Если на сервере конфигурации не нашлось, то пробуем следующий **dashboardKey**,
#. Если ни по одному ключу не нашелся dashboard, то запрашиваем конфигурацию по ключу **DEFAULT**.

Кэширование
-----------
Кеширование возможно в пределах открытой вкладки браузера:

1. **_dashboardKey[]** и **_dashboardType** по recordRef (они достаточно редко меняются),
2. Конфигурация **dashboard** (или её отсутствие) по **dashboardKey** + **dashboardType**.

Конфигурация дашборда
------------------------

При открытии впервые карточки кейса, профиля пользователя или домашней страницы будет показан дашборд по умолчанию для соответствующего типа.

Конфигурация дашборда происходит непосредственно из выбранного типа данных.

Чтобы дополнительно конфигурировать дашборд – изменить настройки, убрать или добавить виджеты, необходимо перейти в карточку кейса, профиль пользователя или домашнюю страницу и **нажать шестеренку- > «Настроить страницу»**:

 .. image:: _static/dashboards/dashboards_1.png
       :width: 300
       :align: center

Общая форма настройки имеет следующий вид:

 .. image:: _static/dashboards/dashboards_2.png
       :width: 400
       :align: center

Разделы дашборда
~~~~~~~~~~~~~~~~~~

«Принадлежность»
""""""""""""""""""

 .. image:: _static/dashboards/dashboards_3.png
       :width: 600
       :align: center

В верхней части указан **id дашборда** и **тип данных**, для которого он настраивается.

Тип данных может быть изменен из доступного выпадающего списка. Например:

 .. image:: _static/dashboards/dashboards_4.png
       :width: 400
       :align: center

Отдельный дашборд может быть настроен для определенного документа (если на примере выбрать тип «Договор№512», то при открытии карточки данного договора будет отображаться дашборд, сконфигурированный именно для данного документа).

При выставленном чекбоксе **«Применить для всех пользователей»** настроенный дашборд будет применен для всех пользователей, открывших указанный тип данных.

«Представление»
""""""""""""""""""

Доступен выбор настройки для десктопной или мобильной версии ECOS.

Укажите количество и содержимое вкладок, выберите расположение и количество колонок для каждой вкладки.

 .. image:: _static/dashboards/dashboards_5.png
       :width: 600
       :align: center

Только для типа дашборда Site-dashboard доступно следующее расположение (Количество колонок подстраивается под размер окна браузера):

 .. image:: _static/dashboards/dashboards_6.png
       :width: 100
       :align: center


.. important::

  Для мобильной версии отображаются только те виджеты, которые уже были настроены для десктопной версии:
   
 .. image:: _static/dashboards/dashboards_7.png
       :width: 400
       :align: center


«Виджеты»
""""""""""""""""""

Созданные колонки можно заполнить доступными виджетами – перетащите виджет в необходимую колонку:

 .. image:: _static/dashboards/dashboards_8.png
       :width: 400
       :align: center

Набор доступных виджетов зависит от вида дашборда:

.. list-table:: 
      :widths: 5 5 5 5
      :header-rows: 1
      :align: center      
      :class: tight-table  
      
      * - 
        - | Case-details
          | Карточка кейса
        - | Site-dashboard
          | Профиль пользователя
        - | User-dashboard
          | Домашняя страница
      * - | **JOURNAL: 'journal'**
          | `См. Журнал <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id2>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20
      * - | **WEB_PAGE: 'web-page'**
          | `См. Веб-страница <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id3>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

      * - | **DOC_PREVIEW: 'doc-preview'**
          | `См. Предпросмотр <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id4>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **COMMENTS: 'comments'**
          | `См. Комментарии <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id5>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **PROPERTIES: 'properties'**
          | `См. Свойства <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id6>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
      * - | **CURRENT_TASKS: 'current-tasks'**
          | `См. Мои задачи <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id7>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **TASKS: 'tasks'**
          | `Все задачи <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id8>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **DOC_STATUS: 'doc-status'**
          | `См. Статус <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id9>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **EVENTS_HISTORY: 'events-history'**
          | `См. История событий <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id10>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
      * - | **VERSIONS_JOURNAL: 'versions-journal'**
          | `См. Журнал версий <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id11>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **DOC_ASSOCIATIONS: 'doc-associations'**
          | `См. Связи документа <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id12>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **RECORD_ACTIONS: 'record-actions'**
          | `См. Действия <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id13>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
      * - | **BARCODE: 'barcode'**
          | `См. Штрих-код <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id14>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **DOCUMENTS: 'documents'**
          | `См. Документы <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id16>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
      * - | **DOC_CONSTRUCTOR: 'doc-constructor'**
          | `Doc.One <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#doc-one>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **PROCESS_STATISTICS: 'process-statistics'**
          | `См. Статистика процесса <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id18>`_
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 
        - 
      * - | **REPORT: 'report'**
          | `См. Статистика по задачам <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id19>`_
        - 
        - 
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

      * - | **BIRTHDAYS: 'birthdays'**
          | `См. Дни рождения <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id20>`_
        - 
        - 
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

      * - | **USER_PROFILE: 'user-profile**
          | `См. Профиль <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/widgets.html#id21>`_
        - 
        - 
            .. image:: _static/dashboards/dashboards_0.png
                :width: 20

        - 

Настройки виджетов на дашбордах
--------------------------------

Настройка виджета осуществляется в карточке каждого виджета. См. отдельную статью <Виджеты>

Информация по доступности виджета хранится в самом виджете (без участия сервера).

В конфигурации виджета в поле **config.widgetDisplayCondition** задается условие как **json-строка**. Написание условия в соответствии статье `Язык_предикатов.  <https://citeck-ecos.readthedocs.io/ru/latest/general/%D0%AF%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%B5%D0%B4%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D0%B2.html>`_.

Если отсутствует условие, то виджет отображается. 

Журнал дашбордов
-----------------

Журнал расположен в **разделе администратора - > Конфигурация UI**:

 .. image:: _static/dashboards/dashboards_9.png
       :width: 600
       :align: center

Дашборд можно отредактировать, удалить, внести изменения через конфиг:

.. list-table:: 
      :widths: 5 10
      :align: center
      :class: tight-table  

      * - |
 
            .. image:: _static/dashboards/dashboards_10.png
                :width: 30

        - Скачать
      * - |
 
            .. image:: _static/dashboards/dashboards_11.png
                :width: 30

        - Удалить
      * - |
 
            .. image:: _static/dashboards/dashboards_12.png
                :width: 30

        - Редактировать в форме
      * - |
 
            .. image:: _static/dashboards/dashboards_13.png
                :width: 30

        - | Редактировать json

            .. image:: _static/dashboards/dashboards_15.png
                :width: 400
      * - |
 
            .. image:: _static/dashboards/dashboards_14.png
                :width: 30

        - Копировать

