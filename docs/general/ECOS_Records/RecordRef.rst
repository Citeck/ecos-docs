RecordRef
==========

.. _RecordRef:


**RecordRef** - это идентификатор записи, который состоит из трех частей:

 #. **appName** - идентификатор приложения, к которому относится запись;
 #. **sourceId** - идентификатор локального (для приложения) источника данных, к которому относится запись;
 #. **id** - локальный идентификатор, который должен быть уникален в пределах источника.

Общий вид: ``appname/sourceId@id`` 

  где **/** и **@** - особые разделители.

* Если в **RecordRef** не задан **sourceId**, то источником по умолчанию считается - "" (пустая строка).

RecordRef является реализацией интерфейса EntityRef.

Уровни детализации от меньшего к большему:

 * /@localId == @localId == localId
 * /sourceId@localId == sourceId@localId
 * appName/sourceId@localId

.. code-block:: java

  RecordRef.create("emodel", "type", "testdl-counterpartyToAuthority");

* **"emodel"** – appName
* **"type"** – sourceId