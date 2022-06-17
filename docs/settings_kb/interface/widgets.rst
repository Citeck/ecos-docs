Виджеты
========

Для некоторых виджетов доступна настройка. Настройка отмечена следующей иконкой:

 .. image:: _static/widgets/widget_1.png
       :width: 600
       :align: center

Виджет «Журнал»
----------------

Ключ **'journal'**.

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

Ключ **'web-page'**.

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


Виджет «Предпросмотр» (обновить)
--------------------------------
Ключ **'doc-preview'**

Виджет предпросмотра содержимого основного документа и всех вложенных. 

Документы переключаются скроллированием. Первым отображается основной контент **cm:content**, затем дочерние элементы с типом **idocs:doc**.

 .. image:: _static/widgets/Preview_1.png
       :width: 800


Настройка виджета, чтобы можно было переключаться между просмотром только основного контент и основного контента + дополнительных документов.
 
 .. image:: _static/widgets/Preview_2.png
       :width: 400

При переключениях между документами перегружается не виджет целиком, а только контент внутри.


Виджет «Комментарии»
----------------------

Ключ **'comments'**.

Виджет для отображения комментариев к документу.

 .. image:: _static/widgets/widget_8.png
       :width: 600

Виджет «Свойства»
-------------------

Ключ **'properties'**.

Виджет для отображения свойств документа.

.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
       

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

Виджет «Мои задачи»
--------------------

Ключ **'current-tasks'**.

Виджет для отображения текущих задач пользователя в документе.

 .. image:: _static/widgets/widget_13.png
       :width: 800


Виджет «Все задачи»
--------------------

Ключ **'tasks'**.

Виджет для отображения активных и завершенных бизнес-процессов в документе.

.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
       

        - |  

            .. image:: _static/widgets/widget_14.png
                 :width: 400   


      * - | **Настроенный вид**
       

        - |  

            .. image:: _static/widgets/widget_15.png
                 :width: 600   


Виджет «Статус»
----------------
Ключ **'doc-status'**.

Виджет статуса документа.

 .. image:: _static/widgets/widget_16.png
       :width: 600

Виджет «История событий»
-------------------------

Ключ **'events-history'**.

История событий отображается в виде таблицы.

 .. image:: _static/widgets/History_1.png
       :width: 600

В виджете можно настроить фильтрацию и поиск событий:

 .. image:: _static/widgets/History_2.png
       :width: 300

Виджет «Журнал версий»
-----------------------

Ключ **'versions-journal'**.

Виджет для отображения версий документа.

 .. image:: _static/widgets/widget_18.png
       :width: 600

Виджет «Связи документа»
--------------------------

Ключ **'doc-associations'**.

Виджет связей документ с другими документами.

 .. image:: _static/widgets/widget_19.png
       :width: 600


Виджет «Действия»
------------------

Ключ **'record-actions'**.

Виджет доступных действий. Настройки тянутся из типа данных.

См. подробню статью `"Действия" <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/ui_actions.html>`_

 .. image:: _static/widgets/widget_20.png
       :width: 200

Виджет «Штрих-код»
-------------------

Ключ **'barcode'**.

Виджет отображает штрих-код основанный на числовом поле документа. По умолчанию используется поле ``idocs:barcode``.

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

Ключ **'documents'**.

Виджет отображения документов/ синхронизации пользователей и групп.

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

Ключ **'doc-constructor'**.

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

Виджет «Статистика процесса» (обновить)
----------------------------------------

Ключ **'process-statistics'**.

Виджет отображает статистику по бизнес-процессу с heatmap.

В виджете два представления: Модель с heatmap и Журнал. 

Heatmap для каждого шага отображает количество инстансов, которые находятся на данном шаге.

В журнале представлен список активных инстансов, которые отображаются на heatmap.


.. list-table:: 
      :widths: 5 40

      * - | **Настройка**
       

        - |  

            .. image:: _static/widgets/Process_statistics_3.png
                 :width: 500   

      * - | **Настроенный вид**
       
        - |  Процесс:

            .. image:: _static/widgets/Process_statistics_1.png
                 :width: 600   

          |  Журнал:

            .. image:: _static/widgets/Process_statistics_2.png
                 :width: 600   

Виджет «Статистика по задачам»
------------------------------
Ключ **'report'**.

Виджет отображает статистику по задачам.

 .. image:: _static/widgets/widget_31.png
       :width: 400


Виджет «День рождения»
-----------------------

Ключ **'birthdays'**.

Виджет отображает ближайшие дни рождения.

 .. image:: _static/widgets/widget_32.png
       :width: 400


Виджет «Профиль»
----------------

Ключ **'user-profile'**.

Виджет профиля пользователя

 .. image:: _static/widgets/widget_33.png
       :width: 200


