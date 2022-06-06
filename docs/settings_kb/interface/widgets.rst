Виджеты
========

Список виджетов / ключи:

  * DOC_PREVIEW: 'doc-preview',
  * JOURNAL: 'journal',
  * REPORT: 'report',
  * COMMENTS: 'comments',
  * PROPERTIES: 'properties',
  * TASKS: 'tasks',
  * CURRENT_TASKS: 'current-tasks',
  * DOC_STATUS: 'doc-status',
  * EVENTS_HISTORY: 'events-history',
  * VERSIONS_JOURNAL: 'versions-journal',
  * DOC_ASSOCIATIONS: 'doc-associations',
  * RECORD_ACTIONS: 'record-actions',
  * WEB_PAGE: 'web-page',
  * BARCODE: 'barcode',
  * BIRTHDAYS: 'birthdays',
  * DOCUMENTS: 'documents',
  * USER_PROFILE: 'user-profile',
  * DOC_CONSTRUCTOR: 'doc-constructor',
  * PROCESS_STATISTICS: 'process-statistics'

DOC_PREVIEW: 'doc-preview'
-----------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

JOURNAL: 'journal',
-----------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

REPORT: 'report'
-------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

COMMENTS: 'comments'
----------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

PROPERTIES: 'properties'
--------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

TASKS: 'tasks'
----------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

CURRENT_TASKS: 'current-tasks'
--------------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

DOC_STATUS: 'doc-status'
-----------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

EVENTS_HISTORY: 'events-history'
---------------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

VERSIONS_JOURNAL: 'versions-journal'
------------------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

DOC_ASSOCIATIONS: 'doc-associations'
------------------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

RECORD_ACTIONS: 'record-actions
--------------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

WEB_PAGE: 'web-page"
----------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

Виджет "Штрих-код документа" BARCODE: 'barcode'
------------------------------------------------

 .. image:: _static/widgets/code_1.png
       :width: 200
       :align: center

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

Настройки виджета
~~~~~~~~~~~~~~~~~~

 .. image:: _static/widgets/code_2.png
       :width: 200
       :align: center

Условие отображения кнопки:

Если отсутствует условие, то кнопка отображается. Иначе для отображения, API по заданному условию должно возвращать **true**.

В текущей версии сохраняется как json строка. 

Написание условия в соответствии статье `Язык предикатов <https://citeck-ecos.readthedocs.io/ru/latest/general/%D0%AF%D0%B7%D1%8B%D0%BA_%D0%BF%D1%80%D0%B5%D0%B4%D0%B8%D0%BA%D0%B0%D1%82%D0%BE%D0%B2.html>`_

BIRTHDAYS: 'birthdays'
-----------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

DOCUMENTS: 'documents'
-----------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

USER_PROFILE: 'user-profile'
-----------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

DOC_CONSTRUCTOR: 'doc-constructor'
-----------------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.

PROCESS_STATISTICS: 'process-statistics'
-----------------------------------------

Настройки виджета
~~~~~~~~~~~~~~~~~~

Если предусмотрена.
