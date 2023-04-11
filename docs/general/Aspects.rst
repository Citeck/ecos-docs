.. _aspects:

Аспекты
=========

**Аспекты** - это гибкая возможность расширения функционала типов ECOS и сущностей.

Журнал аспектов доступен по адресу: ``/v2/admin?journalId=ecos-aspects&type=JOURNAL``

Модель аспекта
--------------

.. code-block::

    id: String // Идентификатор аспекта
    name: MLText // Имя аспекта (справочная информация)
    prefix: String // Префикс аспекта. Будет добавляться перед идентификатором каждого атрибута, которые описаны в attributes и systemAttributes
    configFormRef: EntityRef // Ссылка на форму, которую следует использовать для редактирования конфигурации аспекта в типе ECOS
    attributes: List<AttributeDef> // Атрибуты аспекта, которые будут добавлены к сущностям с данным аспектом
    systemAttributes: List<AttributeDef> // Системные атрибуты аспекта, которые будут добавлены к сущностям с данным аспектом

В конфигурации типа предусмотрено поле ``aspects``, которое содержит список аспектов и их конфигурацию:

.. code-block::

    TypeDef
    ...
    aspects: List<TypeAspectDef>
    ...

    TypeAspectDef
    ref: EntityRef // ссылка на аспект
    config: ObjectData // конфигурация аспекта

API
----

Проверить наличие аспекта у сущности
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    await Citeck.Records.get('emodel/some-id@local-id').load('_aspects._has.aspectToTest?bool!')

где,

``emodel/some-id@local-id`` - идентификатор сущности, у которой мы хотим проверить наличие аспекта

``aspectToTest`` - идентификатор аспекта, наличие которого мы проверяем 

Получить конфиг аспекта из сущности
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    await Citeck.Records.get('emodel/some-id@local-id').load('_type.aspectById.you-aspect-id.config')

Добавить аспект к сущности
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::

    Добавление так же происходит автоматически когда мы проставляем для сущности атрибут из аспекта

.. code-block::

    var rec = Citeck.Records.get('emodel/some-id@local-id');
    rec.att('att_add__aspects', 'emodel/aspect@aspectToAdd');
    await rec.save();

где,

``emodel/some-id@local-id`` - идентификатор сущности, к которой мы хотим добавить аспект

``aspectToAdd`` - идентификатор аспекта, который мы добавляем

Удаление аспекта
~~~~~~~~~~~~~~~~

.. code-block::

    var rec = Citeck.Records.get('emodel/some-id@local-id');
    rec.att('att_rem__aspects', 'emodel/aspect@aspectToRemove');
    await rec.save();

где,

``emodel/some-id@local-id`` - идентификатор сущности, у которой мы хотим удалить аспект

``aspectToRemove`` - идентификатор аспекта, который мы удаляем.

:ref:`Пользовательское описание работы с аспектами <aspects_user>`
