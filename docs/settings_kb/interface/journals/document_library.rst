.. _document_library:

Библиотека документов (Document Library)
==========================================

.. contents::
    :depth: 3

**Document Library (Библиотека документов)** - иерархический интерфейс для работы с папками и документами.

 .. image:: _static/doclib/DocLib_1.png
       :width: 600
       :align: center

В данном режиме можно просмотреть дерево иерархии папок и документов, произвести действия над документами и папками по аналогии действиям в проводнике Windows. 

Проводник отображается в правом меню по нажатию на **«Показать дерево папок»**. Сворачивается по кнопке **«Скрыть дерево папок»**:

 .. image:: _static/doclib/DocLib_2.png
       :width: 600
       :align: center

|

 .. image:: _static/doclib/DocLib_3.png
       :width: 600
       :align: center

1.	Выбранная папка подсвечивается среди других папок **(1)**.
2.	При клике на иконку или название папки она раскрывается **(1)**, и в левой части отражаются файлы, находящиеся в папке **(2)**.
3.	Для отображения документов и папок используются иконки, соответствующие формату файлов по аналогии с проводником Windows:

	-	Microsoft Word (doc, docx);
	-	Microsoft Excel (xls, xlsx);
	-	Microsoft Powerpoint (ppt, pptx);
	-	Adobe Acrobat (pdf);
	-	Файлы изображений (jpg, bmp, png, gif, tif);
	-	OpenOffice/ LibreOffice (odf);
	-	Файл сообщения из электронной почты (.msg).

4.	Загрузка файлов осуществляется по кнопке **+** и используя drag&drop. Файлы добавляться как по одному, так и группой.
5.	Перемещение файлов из каталога в каталог осуществляется с использованием drag&drop. Файлы могут быть перемещены как по одному, так и группой.
6.	Над журналом размещено название текущей раскрытой папки **(4)**, чуть ниже - полный путь к открытой папке **(3)**.
7.	Выделение документов и папок работает аналогично выбору в файловых менеджерах с учетом кнопок Ctrl, Shift и левой кнопки мыши:

	-	**левая кнопка мыши и Shift** приводит к выделению диапазона файлов и папок;
	-	**левая кнопка мыши и Ctrl** добавляет выделение, не сбрасывая уже выделенные файлы;
	-	**левая кнопка мыши без других клавиш** сбрасывает предыдущее выделение и устанавливает новое на том файле или папке куда произошел клик.

8.	Поиск документов внутри выбранной папки **(5)**. Результат поиска отображается в виде списка.
9.	При наведении курсора на файл или папку отображаются действия см. Действия с файлом **(6)**.

Действия с файлом
------------------

.. list-table:: 
      :widths: 5 10 
      :align: center

      * - 
           			.. image:: _static/doclib/ic_1.png
						:width: 25
						:align: center

        - Переход к просмотру карточки в новой вкладке.
      * - 
           			.. image:: _static/doclib/ic_2.png
						:width: 25
						:align: center

        - Переименование файла или папки:

           			.. image:: _static/doclib/DocLib_5.png
						:width: 400
						:align: center

		  | Можно изменить название файла, или сам вложенный файл.

      * - 
           			.. image:: _static/doclib/ic_3.png
						:width: 25
						:align: center

        - Редактировать документ в OnlyOffice. Доступно только для файлов форматов MS Office и  OpenDocument.
      * - 
           			.. image:: _static/doclib/ic_4.png
						:width: 25
						:align: center

        - Скачать файл.

      * - 
           			.. image:: _static/doclib/ic_5.png
						:width: 25
						:align: center

        - Удаление файла или папки:
           			.. image:: _static/doclib/DocLib_4.png
						:width: 400
						:align: center


Создание папки / Загрузка файла
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Создание папки или загрузка файла осуществляется по кнопке **+**:

 .. image:: _static/doclib/DocLib_6.png
       :width: 600
       :align: center

При загрузке файла необходимо ввести его название, которое будет отображаться, и выбрать или перетащить файл для прикрепления:

 .. image:: _static/doclib/DocLib_8.png
       :width: 600
       :align: center

При создании папки укажите ее название:

 .. image:: _static/doclib/DocLib_7.png
       :width: 600
       :align: center

Карточка файла
----------------

Карточка состоит из виджетов.

 .. image:: _static/doclib/DocLib_9.png
       :width: 600
       :align: center

Для файла доступны следующие действия:

	- Редактировать свойства;
	- Редактировать документ (только для файлов форматов MS Office и  OpenDocument)
	- Скачать;
	- Удалить.

Создание библиотеки документов 
---------------------------------

Создайте новый :ref:`тип данных<data_types_main>`. На вкладке **«Основное»** укажите **id**, **Имя**, в качестве родителя выберите **Файл библиотеки документов**. В созданный тип будут автоматически добавлены действия. 
 
 .. image:: _static/doclib/DocLib_10.png
       :width: 600
       :align: center

Так же для создания библиотеки документов можно использовать аспект **doclib**. **[TBD]**

API
----

**to be updated**

Для примеров взят тип **emodel/type@TEST_TYPE**

1. Корень для библиотеки документов всегда доступен по составному id: **alfresco/doclib@TEST_TYPE$** (от id типа отбрасывается префикс **emodel/type@**, добавляется префикс **alresco/doclib@** и постфикс **$**)

2. Получение дочерних элементов::
  
	Records.get('alfresco/doclib@TEST_TYPE$').load('children[]{id:?id,displayName:?disp,nodeType,hasChildrenDirs:hasChildrenDirs?bool,typeRef:typeRef?id}');

Все получаемые id нужно проверять на наличие префикса **alfresco/doclib@**. Если возвращается просто **doclib@…**, то нужно добавить **alfresco/** чтобы получилось **alfresco/doclib@**

3. Узнать поддерживает ли тип режим doclib::

	Records.get('emodel/type@TEST_TYPE').load('resolvedDocLib.enabled?bool')


4. Получить список типов файлов, которые могут быть в данной библиотеке::

	Records.get('emodel/type@TEST_TYPE').load('resolvedDocLib.fileTypeRefs[]?id')

5. Получить тип директории в библиотеке документов::

	Records.get('emodel/type@TEST_TYPE').load('resolvedDocLib.dirTypeRef?id')

6. Создать новый файл или папку в библиотеке::

	var record = Citeck.Records.get('alfresco/doclib@TEST_TYPE$');
	record.att('_parent', 'alfresco/doclib@TEST_TYPE$workspace://SpacesStore/16fffdd9-c37a-4d4f-8e40-9e698c8f194f'); // для корня библиотеки следует использовать alfresco/doclib@TEST_TYPE$
	record.att('cm:title', 'Папка #1000');
	record.att('_type', 'emodel/type@file'); //здесь должен быть один из типов пункта 4 или пункта 5 (по этому типу определяется, что именно нужно создать - папку или файл)
	record.save();

7. Получить дочерние элементы по типу::

	Records.query({
	    sourceId: 'alfresco/doclib',
	    query: {
	        parentRef: 'alfresco/doclib@TEST_TYPE$',
	        nodeType: 'DIR'
	    },
	    language: 'children'
	});

8. Поиск дочерних элементов с фильтрацией (для поиска через полосу поиска над таблицей флаг recursive должен быть true)::

	 Records.query({
	    sourceId: 'alfresco/doclib',
	    query: {
	        parentRef: "alfresco/doclib@TEST_TYPE$",
	        recursive: false,
	        filter: {
	            t: 'contains',
	            att: 'ALL',
	            val: '111'
	        }
	    },
	    language: 'children'
	  })

9. Получение пути для документа (можно объединять с другими атрибутами)::

	Records.get('alfresco/doclib@nsd-attorney$workspace://SpacesStore/fab07cb3-cf5a-4c07-a17a-4e3f56e208d2').load('path[]{disp:?disp,id:?id}')
