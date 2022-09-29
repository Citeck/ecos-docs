Связь типов ECOS и типов Alfresco
----------------------------------

В типе ECOS предусмотрены настройки для связи с Alfresco. Настройка происходит в Дополнительных свойствах.

.. image:: _static/ecos_type_with_alfresco.png
       :width: 600       
       :align: center
       :alt: ECOS type with Alfresco

Список настроек:

1. **alfType** - тип alfresco, который должен устанавливаться у новых сущностей с типом ECOS;
2. **alfRoot** - корневая директория, которая должна использоваться для размещения новых сущностей;
3. **alfChildAssocs** - дочерние ассоциации. Это свойство настраивается в родительском типе и в значении у него находится json объект в виде строки, где ключ - ECOS тип дочерней сущности и значение - тип дочерней ассоциации Alfresco.

Пример::

  properties:
    alfChildAssocs: '{"ecos-fin-request-attachments":"ufrm:requestAttachments"}'

Означает, что когда будет создана дочерняя сущность с типом ECOS ecos-fin-request-attachments, то она разместится в дочерней ассоциации ufrm:requestAttachments


