Виджеты
========

.. contents::
		:depth: 4

Для некоторых виджетов доступна настройка. Настройка отмечена следующей иконкой:

 .. image:: _static/widgets/widget_1.png
       :width: 600
       :align: center

Виджет «Журнал»
----------------

Ключ ``journal``

Виджет для настройки отображения журнала.


.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
       

        - |  

            .. image:: _static/widgets/widget_2.png
                 :width: 400   

          | 

             .. image:: _static/widgets/widget_3.png
                  :width: 400   

      * - | **Настроенный вид**
       

        - |  

            .. image:: _static/widgets/widget_4.png
                 :width: 400   

Виджет «Веб страница»
----------------------

Ключ ``web-page``

Виджет отображает любую web-страницу, заданную в его настройках.

.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
       

        - |  

            .. image:: _static/widgets/widget_5.png
                 :width: 400   


      * - | **Настроенный вид**
       

        - |  

            .. image:: _static/widgets/widget_6.png
                 :width: 400   


Виджет «Предпросмотр»
-----------------------

Ключ ``doc-preview``

Виджет предпросмотра служит для отображения основного документа и всех связанных из атрибута «Содержимое». Позволяет осуществлять скачивание не только основного, а текущего открытого документа.

Оригиналы документов могут быть других расширений, но виджет показывает только картинки или сгенерированные pdf на базе основного.

С включённой настройкой в виджете показываются все связанные документы.
 
 .. image:: _static/widgets/Preview_2.png
       :width: 400


Первым отображается основной контент **cm:content**, затем дочерние элементы с типом **idocs:doc**. 

Если основной отсутствует, то отобразится следующий документ.

Переход между документами осуществляется через дропдаун или скролл. Количество документов указано в дропдауне:

 .. image:: _static/widgets/Preview_1.png
       :width: 800

Содержимое виджета обновляется при изменениях основного и связанных документов.


Виджет «Комментарии»
----------------------

Ключ ``comments``

Виджет для отображения комментариев к документу.

 .. image:: _static/widgets/widget_8.png
       :width: 600

Так же см. `Транслирование комментариев в виджет комментариев <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/%D0%9A%D0%BE%D0%BC%D0%BC%D0%B5%D0%BD%D1%82%D0%B0%D1%80%D0%B8%D0%B8.html>`_

Виджет «Свойства»
-------------------

Ключ ``properties``

Виджет для отображения атрибутов карточки формы и их значений. Предоставляет возможность инлайн редактирования значений атрибутов (с учетом статуса кейса, наличия прав у просматривающего кейс пользователя). 

Список для выбора - формы из журнала форм.

.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
          | Список для выбора - формы из журнала форм.

        - |  

            .. image:: _static/widgets/widget_9.png
                 :width: 400   

          | 

             .. image:: _static/widgets/widget_10.png
                  :width: 400   

      * - | **Настроенный вид**
       

        - |  Для типа дашборда Case-details 

            .. image:: _static/widgets/widget_11.png
                 :width: 400   

          |  Для типа дашборда Site-dashboard

            .. image:: _static/widgets/widget_12.png
                 :width: 400   

Для виджета так же доступен переход в конструктор формы для дополнительной настройки полей: 

.. list-table:: 
      :widths: 5 10

      *  - |  

            .. image:: _static/widgets/form_builder_icon.png
                 :width: 200   

         - | 

             .. image:: _static/widgets/form_builder_form.png
                  :width: 400   

См. подробную статью `"Формы" <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms.html>`_

Виджет «Мои задачи»
--------------------

Ключ ``current-tasks``

Виджет для отображения задач по данному кейсу у просматривающего его пользователя и варианты их завершения.

 .. image:: _static/widgets/widget_13.png
       :width: 600


Виджет «Все задачи»
--------------------

Ключ ``tasks``

Виджет для отображения задач по данному кейсу и их исполнителей.

.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
       

        - |  

            .. image:: _static/widgets/widget_14.png
                 :width: 400   


      * - | **Настроенный вид**
       

        - |  

            .. image:: _static/widgets/widget_15.png
                 :width: 400   


Виджет «Статус»
----------------
Ключ ``doc-status``

Виджет отображает текущий статус кейса (определяется системой автоматически, не доступен для редактирования пользователем).

 .. image:: _static/widgets/widget_16.png
       :width: 400

Виджет «История событий»
-------------------------

Ключ ``events-history``

Виджет служит для отображения событий таких, как создание, обновление, смена статуса кейса с фиксацией даты и времени их происшествия, участников и комментариев.

Виджет представлен в виде таблицы.

 .. image:: _static/widgets/History_1.png
       :width: 600

Для каждого столбца можно настроить фильтрацию и поиск событий:

 .. image:: _static/widgets/History_2.png
       :width: 300

Виджет «Журнал версий»
-----------------------

Ключ ``versions-journal``

Виджет содержит актуальную и предшествующие версии документа. 

Служит для загрузки новой версии документа, а также для сравнения файлов.

 .. image:: _static/widgets/widget_18.png
       :width: 600

Виджет «Связи документа»
--------------------------

Ключ ``doc-associations``

Виджет используется для установки связей данного кейса с другими в системе и отображения установленных связей.

 .. image:: _static/widgets/widget_19.png
       :width: 600

Настройки
~~~~~~~~~~

С версии RC4 появилась возможность настройки виджета.

Для найтройки виджета необходимо: 

* добавить в тип ассоциацию с ``id assoc:associatedWith``;
* задать название связи в атрибут **name** и вид связи в **direction (обязательный атрибут)**, где:
  
    * **BOTH** - двухсторонняя связь, 
    * **TARGET** - связь отображается только у документа, который хотим привязать, 
    * **SOURCE** - обратное к **target** связь у источника.

В **target (обязательный атрибут)** необходимо указывать тип связанного документа.

Атрибут **journalsFromTarget** подтягивает журналы из **target**, можно оставить в неопределенном состоянии:

.. code-block::

  associations:
  - id: assoc:associatedWith
    name:
      ru: Связан с
      en: Associated with
    target: emodel/type@your-type
    direction: BOTH

Если необходимо создавать связи не с одним определенным типом, то  в **journals** нужно добавить необходимые журналы (**journalsFromTarget** не должен быть true).

Пример настройки типа со связями:

.. code-block::

  id: direction
  name:
    ru: Направление
    en: Direction
  parentRef: emodel/type@data-list
  formRef: uiserv/form@direction-form
  journalRef: uiserv/journal@direction-journal
  inheritActions: false
  defaultCreateVariant: true
  associations:
    - id: assoc:associatedWith
      name:
        ru: Связан с
        en: Associated with
      target: emodel/type@direction
      journals:
        - uiserv/journal@agreement-journal
        - uiserv/journal@direction-journal
      direction: SOURCE

.. image:: _static/widgets/doc-associations.png
       :width: 600


Виджет «Действия»
------------------

Ключ ``record-actions``

Виджет содержит перечень доступных действий с кейсом на данном статусе.

Настройки подтягиваются из типа данных. См. подробную статью `"Действия" <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/ui_actions.html>`_

 .. image:: _static/widgets/widget_20.png
       :width: 200

Виджет «Штрих-код»
-------------------

Ключ ``barcode``

Виджет отображает отображает сгенерированный штрих-код документа, основанный на числовом поле документа. 

По умолчанию используется поле ``idocs:barcode``.

Если нужно другое поле, то следует зарегистрировать это поле по типу ECOS в бине ``core.barcode-attribute.type-to-property.mappingRegistry``
Пример:

.. code-block::

    <bean id="records.contracts.barcode-attribute.type-to-property.mapping"
        class="ru.citeck.ecos.spring.registry.MappingRegistrar">
        <constructor-arg ref="core.barcode-attribute.type-to-property.mappingRegistry"/>
        <property name="mapping">
            <map>
                <entry key="contracts-cat-doctype-contract" value="contracts:barcode"/>
            </map>
        </property>
    </bean>

.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
       

        - |  

            .. image:: _static/widgets/widget_21.png
                 :width: 200   

          | Условие отображения кнопки:
          | Если отсутствует условие, то кнопка отображается. Иначе для отображения, API по заданному условию должно возвращать **true**.
          | В текущей версии сохраняется как json строка.
          | Написание условия в соответствии статье `Язык предикатов <https://citeck-ecos.readthedocs.io/ru/latest/general/%D0%AF%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%B5%D0%B4%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D0%B2.html>`_

      * - | **Настроенный вид**
       

        - |  Для типа дашборда Case-details 

            .. image:: _static/widgets/widget_22.png
                 :width: 200   



Виджет «Документы»
-------------------

Ключ ``documents``

Виджет служит для загрузки сопутствующих документов/ синхронизации пользователей и групп.

.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
       

        - |  Документы

            .. image:: _static/widgets/widget_23.png
                 :width: 400   

          | Синхронизация пользователей

             .. image:: _static/widgets/widget_24.png
                  :width: 400   

      * - | **Настроенный вид**
       

        - |  Документы

            .. image:: _static/widgets/widget_25.png
                 :width: 400   

          |  Синхронизация пользователей

            .. image:: _static/widgets/widget_26.png
                 :width: 400   

Виджет «Doc.One»
-----------------

Ключ ``doc-constructor``

Виджет для использования конструктора документов Doc.one.

Doc.one - программа по составлению документов, с помощью которой можно преобразовать любые типовые документы, в умные шаблоны Doc.one.


.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
       

        - |  

            .. image:: _static/widgets/widget_27.png
                 :width: 300   


      * - | **Настроенный вид**
       

        - |  

            .. image:: _static/widgets/widget_28.png
                 :width: 600   

Виджет «Статистика процесса»
-----------------------------

Ключ ``process-statistics``

Виджет визуализирует статистику по бизнес-процессу с отображением тепловой карты (heatmap).

**Heatmap** – способ визуализации статистических данных с помощью цветовой палитры.

В виджете реализованы два представления: 

* **Процесс** - модель бизнес-процесса с heatmap
  
            .. image:: _static/widgets/Process_statistics_1.png
                 :width: 600  

Heatmap для каждого шага процесса отображает количество инстансов, находящихся на данном шаге. 

 .. image:: _static/widgets/Process_statistics_5.png
       :width: 400

Так же можно включить/выключить отображение счетчиков, тепловой карты активных и завершённых процессов, отображение самого бизнес-процесса останется.

Для **масштабирования** используйте сочетание **ctrl и скролл мыши**.
Для перемещения по heatmap **влево- вправо** - сочетание **shift и скролл мыши**.

* **Журнал**. 

            .. image:: _static/widgets/Process_statistics_2.png
                 :width: 600    

В журнале для каждого столбца можно настроить **фильтрацию и поиск событий**. Визуализация будет перерисована в соответствии с выбранными фильтрами.
 
 .. image:: _static/widgets/Process_statistics_4.png
       :width: 600

В настройках виджета выбираются отображаемые по умолчанию элементы виджета, и включено/ выключено отображение цветовой панели тепловой карты:

 .. image:: _static/widgets/Process_statistics_3.png
       :width: 600


Виджет «Статистика по задачам»
------------------------------
Ключ ``report``

Виджет отображает статистику по задачам.

 .. image:: _static/widgets/widget_31.png
       :width: 400


Виджет «День рождения»
-----------------------

Ключ ``birthdays``

Виджет отображает ближайшие дни рождения.

 .. image:: _static/widgets/widget_32.png
       :width: 400


Виджет «Профиль»
----------------

Ключ ``user-profile``

Виджет профиля пользователя

 .. image:: _static/widgets/widget_33.png
       :width: 200


