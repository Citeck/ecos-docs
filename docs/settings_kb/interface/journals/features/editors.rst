.. _editors:

Редакторы
==========

.. contents:: Содержание
   :depth: 3

Редакторы (editors) определяют внешний вид и поведение поля при инлайн-редактировании записи в журнале и при фильтрации. Каждому типу атрибута соответствует свой редактор, который задаётся в конфигурации колонки журнала в поле ``editor``.

.. important::

   ``formatter`` и ``editor`` в конфигурации колонки — независимые поля:

   - ``formatter`` управляет **отрисовкой ячейки** в таблице;
   - ``editor`` управляет **инлайн-редактором** и **контролом фильтра** в заголовке колонки.

   Если у колонки не задан ``editor``, то поле ввода значения в фильтре будет пустым — даже если ``formatter`` настроен корректно. Наиболее частый случай — колонки типа ``ASSOC``: форматтер ``assoc`` отвечает только за отображение, а для фильтра обязательно нужен ``editor`` (обычно ``type: journal``).

   Соответствие типов колонки и редакторов:

   .. list-table::
      :widths: 30 20
      :header-rows: 1

      * - Тип колонки (``type``)
        - Редактор (``editor.type``)
      * - ``ASSOC``
        - ``journal``
      * - ``PERSON`` / ``AUTHORITY_GROUP`` / ``AUTHORITY``
        - ``orgstruct``
      * - ``TEXT`` / ``MLTEXT``
        - ``text``
      * - ``NUMBER`` / ``INT`` / ``LONG`` / ``FLOAT`` / ``DOUBLE``
        - ``number``
      * - ``DATE``
        - ``date``
      * - ``DATETIME``
        - ``datetime``
      * - ``BOOLEAN``
        - ``boolean``

.. note::

   В редакторах могут использоваться :ref:`вычисляемые атрибуты <computed_attributes>`.

Настройки
---------

Перейти в раздел администрирования > :guilabel:`Журналы` > найти необходимый журнал > действие :guilabel:`Редактировать`. Перейти в :guilabel:`Дополнительно`.

.. list-table::
   :widths: 40
   :align: center

   * - .. image:: _static/editor/editor_1.png
          :width: 500
          :align: center

       .. image:: _static/editor/editor_2.png
          :width: 500
          :align: center

Типы
---------

BooleanEditor
~~~~~~~~~~~~~~~~~~

Тип: ``boolean``

.. list-table::
   :widths: 5 40 40
   :header-rows: 1

   * - Ключ
     - Значение
     - По умолчанию
   * - **mode**
     - Режим редактора ``select``:

       .. image:: _static/editor/editor_3.png
          :width: 200

       ``checkbox``:

       .. image:: _static/editor/editor_4.png
          :width: 200

     - ``select``

DateEditor
~~~~~~~~~~~~~~~~~~

Тип: ``date``

DateTimeEditor
~~~~~~~~~~~~~~~~~~

Тип: ``datetime``

JournalEditor
~~~~~~~~~~~~~~~~~~

Тип: ``journal``

Используется для колонок типа ``ASSOC`` — отвечает и за инлайн-редактирование значения ассоциации, и за контрол фильтра в заголовке колонки. Отдельного редактора с типом ``assoc`` не существует: для любой ассоциации нужно задавать именно ``editor.type: journal``.

.. list-table::
   :widths: 5 40 40
   :header-rows: 1

   * - Ключ
     - Значение
     - По умолчанию
   * - **journalId**
     - Идентификатор журнала, из которого будет выбираться значение. Обычно — журнал, связанный с целевым типом ассоциации.
     -

Пример полной конфигурации ASSOC-колонки с ``formatter`` и ``editor``:

.. code-block:: yaml

  - id: urgencyClass
    name:
      ru: Класс срочности
    type: ASSOC
    multiple: true
    searchable: true
    formatter:
      type: assoc
      config:
        sourceId: emodel/ecos-urgency-class
    editor:
      type: journal
      config:
        journalId: ecos-urgency-class

Здесь ``formatter`` определяет, как отрисовывается ячейка, а ``editor`` — как выглядит фильтр в заголовке и инлайн-редактор значения. Без блока ``editor`` фильтр останется пустым.

NumberEditor
~~~~~~~~~~~~~~~~~~

Тип: ``number``

OrgstructEditor
~~~~~~~~~~~~~~~~~~

Тип: ``orgstruct``

Конфигурация:

.. list-table::
   :widths: 5 40 40
   :header-rows: 1

   * - Ключ
     - Значение
     - По умолчанию
   * - **allowedAuthorityTypes**
     - строка вариантов: ``GROUP``, ``USER``
     -
   * - **multiple**
     - множественный выбор boolean
     - false

SelectEditor
~~~~~~~~~~~~~~~~~~

Тип: ``select``

Конфигурация:

Можно задавать статические варианты или получаемые с использованием ``recordRef + attribute`` записи и параметра ``optionsAtt``.

.. list-table::
   :widths: 5 40 40
   :header-rows: 1

   * - Ключ
     - Значение
     - По умолчанию
   * - **options**
     - | json-строка вариантов
       | пр. ``[{"label":"priority.high","value":1},``
       | ``{"label":"priority.low","value":3},``
       | ``{"label":"priority.medium","value":2}]``
     -
   * - **optionsAtt**
     - пр. ``_edge.${attribute}.options{value:?str,label:?disp}``
     - ``_edge.${attribute}.options{value:?str,label:?disp}``

TextEditor
~~~~~~~~~~~~~~~~~~

Тип: ``text``
