.. _form_components_detailed:

Подробное описание отдельных компонентов
========================================

В этом разделе описаны настройки и примеры использования отдельных компонентов форм Citeck: источники данных, создание и выбор записей, загрузка файлов, компоновка и условия отображения. Выберите компонент, чтобы перейти к подробной инструкции.

Полный перечень доступных компонентов и их назначение приведены в :ref:`общем обзоре компонентов<form_components_overview>`.

.. grid:: 2
   :gutter: 2

   .. grid-item-card:: Text Field
      :link: text_field_component
      :link-type: ref

      Однострочный ввод, маски и автодополнение из статического списка или асинхронного источника.

   .. grid-item-card:: Table Form
      :link: table_form_component
      :link-type: ref

      Таблица связанных записей: создание, редактирование, копирование из справочника и импорт из файлов.

   .. grid-item-card:: Async Data
      :link: async_data_component
      :link-type: ref

      Загрузка атрибутов записей, поисковые запросы, Ajax и пользовательские вычисления. Настройка событий обновления и кеширования.

   .. grid-item-card:: Select Journal
      :link: select_journal_component
      :link-type: ref

      Выбор записей из журнала: фильтры, сортировка, рабочие пространства и динамическое определение ID журнала.

   .. grid-item-card:: Select Orgstruct
      :link: select_orgstruct_component
      :link-type: ref

      Выбор пользователей и групп: фильтры, поиск, корневая группа и формат сохраняемого значения.

   .. grid-item-card:: ECOS Select
      :link: ecos_select_component
      :link-type: ref

      Выбор из списка, автоматическое получение допустимых значений атрибута и отображение результата текстом или ссылкой.

   .. grid-item-card:: File
      :link: file_component
      :link-type: ref

      Загрузка файлов, настройка их названий, действий при нажатии и видимости элементов компонента.

   .. grid-item-card:: Columns
      :link: columns_component
      :link-type: ref

      Размещение полей по столбцам: ширина для разных размеров экрана и CSS-классы ячеек.

   .. grid-item-card:: Panel
      :link: panel_component
      :link-type: ref

      Группировка полей в блок с заголовком, подстановка значений формы в заголовок и оформление панели.

   .. grid-item-card:: Horizontal Line
      :link: horizontal_line_component
      :link-type: ref

      Разделитель блоков формы: вертикальные и отрицательные отступы, особенности режима чтения.

   .. grid-item-card:: Import Button
      :link: import_button_component
      :link-type: ref

      Кнопка загрузки файлов на заданный URL: обработка ответов, несколько файлов и подтверждение перед загрузкой.

   .. grid-item-card:: Checkbox
      :link: checkbox_component
      :link-type: ref

      Флажок с двумя или тремя состояниями. Условия видимости, Logic и особенности работы внутри Columns.

.. toctree::
    :maxdepth: 5
    :hidden:

    components/text field
    components/table form
    components/async data
    components/select journal
    components/select orgstruct
    components/ecos select
    components/file
    components/columns
    components/panel
    components/horizontal line
    components/import button
    components/checkbox
