Общее описание
===============

.. contents::
		:depth: 4
		

Основные компоненты
--------------------

Text Field
~~~~~~~~~~~~~~~

Однострочное текстовое поле. В модели данных соответствует типу **d:text**.

 .. image:: _static/Text_Field_Component.png
       :width: 400
       :align: center

`См. подробное описание Text Field на Form.io <https://help.form.io/userguide/forms/form-components#text-field>`_ 

Select Journal
~~~~~~~~~~~~~~~

Компонент, отвечающий за выбор из журнала. Работает только в том случае, если для ссылочного типа существует журнал.

 .. image:: _static/Select_Journal_Component.png
       :width: 400
       :align: center

`См. подробное описание Select Journal <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/select%20journal.html>`_

Select Orgstruct
~~~~~~~~~~~~~~~~~~

Компонент, отвечающий за выбор из оргструктуры пользователей/групп. Что именно будет выбираться (пользователи с группами вместе, или что-то одно), – регулируется внутри компонента.

 .. image:: _static/Select_Orgstruct_Component.png
       :width: 400
       :align: center

`См. подробное описание Select Orgstruct  <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/select%20orgstruct.html>`_

Number
~~~~~~~~~~~~~~~

Числовое поле. Может принимать в себя как целочисленные значения, так и с плавающей точкой. Это регулируется внутри компонента. В модели данных соответствует типам **d:int** и **d:double**.

`См. подробное описание Number на Form.io <https://help.form.io/userguide/forms/form-components#number>`_ 

Date/Time
~~~~~~~~~~~~~~~

Поле, отвечающее за отображение даты и времени. Отображение регулируется внутри компонента. В модели данных соответствует типам **d:date** и **d:datetime**.

 .. image:: _static/Date_Time_Component.png
       :width: 400
       :align: center

`См. подробное описание Date/Time на Form.io <https://help.form.io/userguide/forms/form-components#date-time>`_  

Text Area
~~~~~~~~~~~~~~~

Аналог Text Field. Многострочное текстовое поле. В модели данных соответствует типу **d:text**.

 .. image:: _static/Text_Area_Component.png
       :width: 400
       :align: center

`См. подробное описание Text Area на Form.io <https://help.form.io/userguide/forms/form-components#text-area>`_ 

Checkbox
~~~~~~~~~~~~~~~

Поле выбора нескольких значений из списка параметров.

 .. image:: _static/Checkbox_Component.png
       :width: 200
       :align: center

`См. подробное описание Checkbox на Form.io <https://help.form.io/userguide/forms/form-components#check-box>`_  


Day
~~~~~~~~~~~~~~~

Поле для ввода значений «День», «Месяц» и «Год» с использованием числа или выбора типа поля.

`См. подробное описание Day на Form.io <https://help.form.io/userguide/forms/form-components#day>`_  


Ecos Select
~~~~~~~~~~~~~~~

Поле, отвечающее за выбор из списка. Основан на стандартном formio-компоненте Select, был модифицирован.

 .. image:: _static/ECOS_Select_Component.png
       :width: 400
       :align: center

`См. подробное описание EcosSelect <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/select%20orgstruct.html>`_  


Button
~~~~~~~~~~~~~~~

Добавление кнопок для выполнения различных действий в форме.

 .. image:: _static/Button_Component.png
       :width: 400
       :align: center

`См. подробное описание Button на Form.io <https://help.form.io/userguide/forms/form-components#button>`_  


Расширенные
------------

ML Text
~~~~~~~~~~~~~~~

Однострочное текстовое поле.

Для выбора языка предусмотрен переключатель в виде флага России /США. После выбора языка вводится в поле вводится текст.

Сохраняются оба введенных зачения.

Если поле содержит постфикс ML и является объектом (содержитключ EN/RU), то элемент отрисовывается.

 .. image:: _static/ML_Text_Component.png
       :width: 400
       :align: center


Table Form
~~~~~~~~~~~~~~~

Компонент позволяет отображать выбранные значения в виде таблицы.

`См. подробное описание Table Form <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/table%20form.html>`_ 


Task Outcome
~~~~~~~~~~~~~~~

Компонент для автоматической отрисовки кнопок для форм задач.

В настройках кейса для "Пользовательской задачи" если заполнено поле "Варианты результатов", то должны создаваться кнопки действий согласно статье ...

Важно чтобы соблюдался порядок кнопок: слева серым цветом отрицательные действия, справа положительные синим цветом. 

Пример такой формы - **wfcperformTask**, это стандартная форма в которой список действий указывается только в свойстве "Варианты результатов".

Кнопки могут быть без надписи. 

Добавлена возможность указать позитивный/негативный тип действия кнопки ccc^n|Отмена#alf#bbb^p|Согласовать
- p - позитивный (по умолчанию, можно не указывать)
- n - негативный

Кнопки сортируются по типу действия - сначала позитивные, потом негативные

Import Button
~~~~~~~~~~~~~~~

Компонент позволяет добавить на форму настраиваемую кнопку для загрузки файлов.

`См. подробное описание Import Button <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/import%20button.html>`_ 

Email
~~~~~~~~~~~~~~~

Компонент для настройки ввода электронной почты.

`См. подробное описание Email на Form.io <https://help.form.io/userguide/forms/form-components#email>`_ 

URL
~~~~~~~~~~~~~~~

Компонент имеет настраиваемый параметр проверки, который, если он настроен правильно, может гарантировать, что введенное значение является допустимым URL-адресом.

`См. подробное описание URL на Form.io <https://help.form.io/userguide/forms/form-components#url>`_ 

Phone Number
~~~~~~~~~~~~~~~

Компонент можно использовать для ввода номеров телефонов в форму.

`См. подробное описание Phone Number на Form.io <https://help.form.io/userguide/forms/form-components#phone-number>`_ 

Address Field
~~~~~~~~~~~~~~~

Cпециальный компонент, выполняющий поиск введенных адресов.

`См. подробное описание Address Field на Form.io <https://help.form.io/userguide/forms/form-components#address>`_ 

ML Textarea
~~~~~~~~~~~~~~~

Многострочное текстовое поле для ввода на русском/анлийском языках. 

Для выбора языка предусмотрен переключатель в виде флага России /США. После выбора языка вводится в поле вводится текст.

Сохраняются оба введенных зачения.

Если поле содержит постфикс ML и является объектом (содержитключ EN/RU), то элемент отрисовывается.


HTML Element
~~~~~~~~~~~~~~~

Компонент может быть добавлен в форму для отображения одного элемента HTML.

 .. image:: _static/HTML_Element_Component.png
       :width: 400
       :align: center

`См. подробное описание HTML Element на Form.io <https://help.form.io/userguide/forms/layout-components#html-element>`_

File
~~~~~~~~~~~~~~~

Компонент для загрузки файлов. 

 .. image:: _static/File_Component.png
       :width: 400
       :align: center

`См. подробное описание File на Form.io <https://help.form.io/userguide/forms/premium-components#file>`_ 

`См. подробное описание File <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/file.html>`_ 


Select Action
~~~~~~~~~~~~~~~

Компонент для отображения список значений в раскрывающемся списке. Пользователи могут выбрать одно из значений.


`См. подробное описание Select Action на Form.io <https://help.form.io/userguide/forms/form-components#select>`_ 

Макет
-------

Horizontal Line
~~~~~~~~~~~~~~~

Компонент для отображения разделителя блоков.

`См. подробное описание Horizontal Line <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/horizontal%20line.html>`_ 


Columns
~~~~~~~~~~~~~~~

Компонент, отвечающий за разделение формы на столбцы. Основан на стандартном formio-компоненте Columns, был модифицирован.

 .. image:: _static/Columns_Component.png
       :width: 400
       :align: center

|

 .. image:: _static/Columns_Component_1.png
       :width: 400
       :align: center

|

 .. image:: _static/Columns_Component_form.png
       :width: 400
       :align: center

`См. подробное описание Columns на Form.io <https://help.form.io/userguide/forms/layout-components#columns>`_ 

`См. подробное описание Columns <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/columns.html>`_ 


Panel
~~~~~~~~~~~~~~~

Панель, в которую можно поместить свойство. Нужна для зонирования. В неё помещаются близкие по смыслу компоненты и им присваивается заголовок.

 .. image:: _static/Panel_Component.png
       :width: 400
       :align: center

`См. подробное описание Panel на Form.io <https://help.form.io/userguide/forms/layout-components#panel>`_ 

Table
~~~~~~~~~~~~~~~

Компонент позволяет создать таблицу со столбцами и строками.

 .. image:: _static/Select_Journal_Component.png
       :width: 400
       :align: center

`См. подробное описание Table на Form.io <https://help.form.io/userguide/forms/layout-components#table>`_ 

Tabs
~~~~~~~~~~~~~~~

Компонент твечает за вкладки на форме. Вкладка скрывается, когда на ней все компоненты скрыты, либо компонентов нет совсем.

`См. подробное описание Tabs на Form.io <https://help.form.io/userguide/forms/layout-components#tabs>`_ 

Данные
--------		

Hidden
~~~~~~~~~~~~~~~

Компонент можно добавить в форму, чтобы создать свойство ресурса, которое можно настроить в форме. Внешнего виджета для скрытых компонентов нет. Они не отображаются в визуализированных формах.

`См. подробное описание Hidden на Form.io <https://help.form.io/userguide/forms/data-components#hidden>`_ 

Async Data
~~~~~~~~~~~~~~~

Невидимый компонент для загрузки асинхронных данных.

 .. image:: _static/Async_Data_Component.png
       :width: 400
       :align: center

`См. подробное описание Async Data <https://citeck-ecos.readthedocs.io/ru/latest/settings_kb/interface/forms/form_components/components/async%20data.html>`_

Include Form
~~~~~~~~~~~~~~~

Компонент для включения одной формы в другие.

В свойствах одно поле - **formRef** с выбором из журнала форм (ecos-forms).

Внеший вид в билдере (как у компонента Hidden, но имя формируется по шаблону "Форма: имя_формы"). 

Вариант на английском: Form: form_name

где **form_name** и **имя_формы** - это атрибут **"?disp"** выбраной формы. Если форма не выбрана, то пишется No form (Нет формы)

При отрисовке формы не в билдере компонент рисовать не нужно (на сервере он будет автоматически заменяться на все компоненты, которые есть в выбранной форме).

 .. image:: _static/Include_Form_Component.png
       :width: 400
       :align: center

Container
~~~~~~~~~~~~~~~

Оболочка для набора полей, аналогичная Field Set.

 .. image:: _static/Container_Component.png
       :width: 400
       :align: center

`См. подробное описание Container на Form.io <https://help.form.io/userguide/forms/data-components#container>`_ 

Data Grid
~~~~~~~~~~~~~~~

Компонент управления отображением данных, который извлекает информацию из коллекции объектов и визуализирует ее в сетке со строками и ячейками. Каждая строка соответствует отдельному объекту, а каждый столбец — свойству в этом объекте.

 .. image:: _static/Data_Grid_Component.png
       :width: 400
       :align: center

`См. подробное описание Data Grid на Form.io <https://help.form.io/userguide/forms/data-components#data-grid>`_ 

Data Grid  Assoc
~~~~~~~~~~~~~~~~~~

Компонент управления отображением данных, основанный на использовании Bootstrap Grid. 

Система **Bootstrap Grid** нужна для разметки страницы, в частности, для создания адаптивных макетов.

Фреймворк определяет 5 уровней адаптивности (брейкпоинтов), которые основаны на ширине области просмотра:

* **xs** — extra small, супермаленький — ширина < 576px (это уровень по умолчанию);
* **sm** — small, маленький — ширина ≥ 576px;
* **md** — medium, средний — ширина ≥ 768px;
* **lg** — large, большой — ширина ≥ 992px;
* **xl** — extra large, супербольшой — ширина ≥ 1200px.

Сетка состоит из групп рядов и колонок, расположенных внутри одного или нескольких контейнеров.

Основные правила сетки в Bootstrap:

* колонки находятся строго внутри ряда на первом уровне вложенности;
* ряды нужны только для размещения колонок;
* ряды должны располагаться внутри контейнера.

Ряды и колонки всегда работают вместе,  их нельзя разделять.

Элемент с классом **.container** является корневым блоком сетки в Bootstrap, то есть располагается на внешнем уровне. Контейнер подходит для хранения любых элементов, а не только рядов и колонок.

Внутри ряда должны находиться только колонки, а контент – уже внутри них.

Колонки нужны для разделения области просмотра по горизонтали, при этом в одном ряду могут быть столбцы разной ширины. 

Классическая Bootstrap-сетка состоит из 12 колонок. 

В большинстве случаев, не требуется использование всех, их можно объединять по мере надобности. Представьте, что вся область просмотра разделена на 12 равных частей – единиц ширины. В одной колонке может быть от 1 до 12 таких единиц.

`См. подробное описание Bootstrap Grid system <https://getbootstrap.com/docs/4.0/layout/grid/>`_ 

Data Map
~~~~~~~~~~~~~~~

Компонент позволяет пользователям создавать пары ключ/значение.

`См. подробное описание Data Map на Form.io <https://help.form.io/userguide/forms/data-components#data-map>`_ 




