Типы данных
=============

Маппинг старых типов и видов на новые типы кейсов
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Старые типы и виды кейса записываются в полях tk:type и tk:kind в виде nodeRef. Например:

* **tk:type = workspace://SpacesStore/contracts-cat-doctype-contract** (Договор),
* **tk:kind = workspace://SpacesStore/contracts-cat-contract-services** (Услуги).

Для преобразования в новый тип кейса следует взять значения из этих полей, убрать у каждого из них **workspace://SpacesStore/** и оставшиеся части объединить в одну строку через "/" (слева - ``tk:type``, а справа ``tk:kind``): **contracts-cat-doctype-contract/contracts-cat-contract-services**.

Если ``tk:kind`` не задан, то правой части и знака "/" не нужно. Например: **contracts-cat-doctype-contract**.

При добавлении новых типов кейсов следует учитывать, что тип с ``tk:kind`` должен наследоваться от типа без ``tk:kind`` чтобы унаследовать его свойства:

.. image:: _static/case_type_legacy_1.png
       :align: center
       :alt: Наследование типа

Связь с типом Alfresco
~~~~~~~~~~~~~~~~~~~~~~~~~~

Чтобы у записей с определенным типом ``alfresco`` был нужный тип ECOS можно сделать следующее (на выбор):

Для новых нод:

		1. Сделать аспект, который унаследован от **etype:hasType** и переопределить там свойство **etype:type** (!тип следует указывать *без* emodel/type@ префикса). После этого можно навесить данный аспект на тип ``alfresco`` и новые ноды будут иметь нужный тип ECOS.
		2. В варианте создания добавить атрибут **_type=emodel/type@нужный-тип**. Новые ноды, создаваемые через данный вариант создания будут иметь нужный тип.

Для новых и старых нод:

        3. Добавить **Registrar** бин, который зарегистрирует связь тип alfresco → тип ECOS:

            **ecosTypeService.register(QName nodeType, Function<AlfNodeInfo, RecordRef> evaluator)**.

Для примера см. конфигурацию **ru.citeck.ecos.node.EcosTypeConfiguration**.