RecordRef
==========

.. _RecordRef:

**RecordRef** - идентификатор записи, вида ``appName/sourceId@localId``, где **/** и **@** - особые разделители.
  
Состоящий из трех частей:

 * **appName** - идентификатор приложения, к которому относится запись, например системные микросервисы (например,emodel, eproc) или пользовательские микросервисы;
 * **sourceId** - идентификатор локального (для приложения) источника данных, к которому относится запись;
 * **id** - локальный идентификатор, который должен быть уникален в пределах источника.

**RecordRef**, например, указывается в строке браузера при обращении к сущности:

.. image:: _static/recordref.png
       :width: 800
       :align: center

RecordRef является реализацией интерфейса EntityRef.

.. code-block:: java

  RecordRef.create("emodel", "type", "testdl-counterpartyToAuthority");

* **emodel** – appName
* **type** – sourceId
* **testdl-counterpartyToAuthority** - localId

Примеры ссылок для пользователей и групп
----------------------------------------

.. list-table::
      :widths: 10 20 20
      :header-rows: 1
      :align: center
      :class: tight-table

      * - Тип сущности
        - Формат ссылки
        - Пример
      * - Пользователь
        - ``emodel/person@{username}``
        - ``emodel/person@ivan.petrov``
      * - Группа
        - ``emodel/authority-group@{localId}``
        - ``emodel/authority-group@accountant``

.. _broken_refs:

Корректный формат ссылок
--------------------------

При записи значений в ASSOC-like атрибуты (Association, Authority, Person, Group) важно использовать полные ссылки в формате ``{appName}/{sourceId}@{localId}``.

Проверить формат хранимых ссылок можно через:

.. code-block:: javascript

    Records.get('emodel/your-type@doc-id').load('myAssocAtt[]?raw')
