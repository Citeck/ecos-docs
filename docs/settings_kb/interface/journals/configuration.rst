Конфигурация журналов
======================

Конфигурация журналов хранится в ``ecos-uiserv``. Список загруженных журналов можно посмотреть в системных журналах → :guilabel:`Журналы`.
Варианты создания записи берутся из связанного типа.

#. Для добавления нового журнала нужно описать тип, для которого будет описан журнал **Типы кейсов**.
#. Затем добавляем ``yml`` (предпочтительнее) или ``json`` конфигурацию в любом микросервисе по пути **eapps/artifacts/ui/journal**.

**Примеры**

Журнал с дашбордами:

.. code-block:: yaml

	id: ecos-dashboards
	name: { ru: Дашборды, en: Dashboards }

	actions:
	  - uiserv/action@ecos-module-download
	  - uiserv/action@delete
	  - uiserv/action@edit

	columns:

	  - id: moduleId
	    name: { ru: Идентификатор, en: Id }

	  - id: typeRef
	    name: { ru: Тип ECOS, en: ECOS Type }

	  - id: authority
	    name: { ru: Человек или группа, en: User or group }

Использование свойств записи в качестве конфигурации
------------------------------------------------------

В журналах предусмотрена возможность использования атрибутов записи для конфигурации форматтеров и редакторов.
Чтобы воспользоваться данной возможностью достаточно в конфигурации указать значение необходимого свойства с помощью ${...}

Пример

.. code-block:: yaml

  formatter:
    type: script
    config:
      fn: 'return "Контрагент " + vars.inn;'
      vars:
        // атрибут ecos:inn будет загружен вместе со всеми другими в запросе поиска
        inn: "${ecos:inn}"

Использование свойств связанных сущностей для форматирования ячейки
---------------------------------------------------------------------

Если у нас есть некоторая ассоциация (множественная или нет не важно) и мы хотим отформатировать 
каждую связанную сущность используя её поля, то можно воспользоваться следующей конфигурацией колонки:

.. code-block:: yaml

  - id: some-assoc-attribute
    attSchema: '{field0,field1}'
    formatter:
      type: script
      config:
        fn: 'return cell.field0 + " - " + cell.field1;'

Здесь attSchema - это перечисление внутренних атрибутов, которые нужно загрузить у связанных сущностей 

Итоговый запрос для атрибута ``some-assoc-attribute`` формируется из следующих частей:

1. ``some-assoc-attribute`` // id колонки или если есть, то attribute
2. ``[]`` // добавляется к части из п.1 в конец если multiple == true
3. ``{value:?assoc,disp:?disp}`` // на основе типа колонки определяется какие скаляры мы подгружаем для атрибута (для ассоциаций это ?assoc и ?disp)

Получаем в итоге: ``some-assoc-attribute[]{value:?assoc,disp:?disp}``

Пункт 3 можно переопределить параметром attSchema и в примере выше будет загружаются следующий атрибут:

``some-assoc-attribute[]{field0,field1}``

По правилам RecordsAPI если алиасы для значений не заданы, то они будут доступны под именем field0 и field1.
Вариант с алиасами будет выглядеть следующим образом:

``some-assoc-attribute[]{alias0:field0,alias1:field1}``

При загрузке такого атрибута мы получим результат в следующем формате:

.. code-block:: yaml

  {
    "some-assoc-attribute": [
      {
          "alias0": "значение атрибута field0 для первой связанной сущности",
          "alias1": "значение атрибута field1 для первой связанной сущности"
      },
      {
          "alias0": "значение атрибута field0 для второй связанной сущности",
          "alias1": "значение атрибута field1 для второй связанной сущности"
      }
    ]
  }

Вычисляемые свойства
---------------------

Не редко бывают ситуации, когда для работы фильтров, форматтеров или редакторов требуются дополнительные данные, которые могут загружаться с удаленного сервера.
Для таких случаев предусмотрены вычисляемые свойства (computed), которые описываются для колонки или для конфига журнала в целом.

Все вычисляемые свойства делятся на два уровня:

1. Уровень конфигурации
2. Уровень записи

Уровень конфигурации означает, что свойство может быть вычислено независимо от отображаемых записей в журнале.
Уровень записи полагается на атрибуты записи для своих вычислений.
Если в конфигурации вычисляемого свойства присутствуют вставки ${...}, то предполагается, что это свойство уровня записи
и требуется его вычислять отдельно для каждой строки в журнале. Если же подобных вставок нет, то это уровень конфигурации
и сервис может вычислить это свойство только один раз при первом открытии журнала.

.. list-table:: Список поддерживаемых вычисляемых свойств
    :header-rows: 1

    *   - Название
        - Свойства
        - Описание
    *   - attributes
        - | ``record: String`` запись, у которой нужно получить атрибуты
          | ``attributes: String|List<String>|Map<String, String>`` атрибуты, которые нужно загрузить.
        - | Загрузить атрибуты через
          | Records.get(record).load(attributes)
    *   - query
        - | ``query: String`` поисковый запрос, который нужно выполнить
          | ``attributes: String|List<String>|Map<String, String>`` атрибуты, которые нужно загрузить.
        - | Отправить поисковый запрос через
          | Records.query(query, attributes)
    *   - script
        - | ``fn: String`` скрипт для вычислений. Может вернуть Promise.
          | ``vars: Map<String, Any>`` переменные, которые будут переданы в скрипт.
        - Вычислить скрипт

Пример использования вычисляемого свойства для вариантов выбора:

.. code-block:: yaml

  // колонка с идентификатором 'category'
  - id: category

    computed:

        // идентификатор свойства
      - id: options

        // тип вычисляемого свойства
        type: attributes

        // конфигурация вычисляемого свойства
        config:
          record: app/sourceId@someCategoryRef
          attributes: subcategories[]{label:?disp,value:?id}

    editor:

      // Указываем, что тип фильтра и inline-редактора - выбор из списка
      type: select

      config:

        // ссылаемся на вычисляемое свойство с помощью ${...} и префикса '$computed.'
        options: '${$computed.options}'


Модель конфигурации журнала
----------------------------

Модель:

.. code-block::

    // Конфигурация журнала
    JournalDef {

        // Идентификатор журнала
        id: String,

        // Отображаемое имя журнала
        name: MLText,

        // Идентификатор источника данных, из которого будут загружаться записи.
        // Как правило задается в типе, а здесь нужен только для особых случаев.
        sourceId: String,

        // Запись, из которой будет загружаться мета-информация для фильтров.
        // По умолчанию - "{sourceId}@"
        metaRecord: RecordRef,

        // Предикат для поиска отображаемых записей.
        // По умолчанию в журнале отображаются записи связанного типа.
        // Используя это поле можно наложить дополнительные условия.
        predicate: Predicate,

        // Дополнительные данные для запроса при поиске записей.
        // Если это поле задано, то язык поиска устанавливается predicate-with-data
        // и структура query становится
        // {
        //   data: {queryData},
        //   predicate: {predicate}
        // }
        queryData: ObjectData,

        // Тип записей в журнале. Как правило это поле следует оставлять пустым,
        // чтобы связь с типом указывалась в конфигурации типа.
        // Данное поле полезно для случая когда у одного типа может быть несколько журналов.
        typeRef: RecordRef,

        // Список атрибутов для группировки записей
        groupBy: List<String>,

        // Сортировка по умолчанию
        sortBy: List<JournalSortByDef>,

        // Флаг, который определяет необходимость загрузки действий из типа.
        // true - действия из типа загружаются
        // false - действия из типа не загружаются
        // null - действия из типа загружаются если поле actions пустое
        actionsFromType: Boolean?,

        // Ссылки на UI действия над записями в журнале
        actions: List<RecordRef>,

        // Описание UI действий в конфиге журнала. Если действие специфично только для определенного журнала
        // и его использование в других частях системы не предполагается, то можно использовать данное поле.
        actionsDef: List<JournalActionDef>,

        // Флаг, которые определяет доступно ли inline-редактирование в журнале
        editable: Boolean,

        // Конфигурация колонок
        columns: List<JournalColumnDef>,

        // Вычисляемые значения в контексте журнала. Полезны для использования в форматтерах и редакторах.
        computed: List<JournalComputedDef>,

        // Флаг, который определяет что форма системная. Системные формы нельзя добавить в приложение ECOS.
        system: Boolean,

        // Дополнительные свойства для поддержки произвольных настроек,
        // которые очень специфичны, чтобы стать частью основного конфига.
        properties: ObjectData
    }

    // Структура для описания сортировки
    JournalSortByDef {

        // Атрибут для сортировки
        attribute: String,

        // Порядок сортировки. true - по возрастанию. false - по убыванию.
        ascending: Boolean
    }

    JournalActionDef(

        // Идентификатор действия. Не обязательный
        id: String,

        // Отображаемое имя действия
        name: MLText,

        // Отображаемое имя действия во множественном числе
        pluralName: MLText,

        // Иконка для действия
        icon: String,

        // Настройка для подтверждения действия
        confirm: ActionConfirmDef,

        // Тип действия
        type: String,

        // Конфигурация действия
        config: ObjectData,

        // Доступные возможности (execForRecord, execForRecords, execForQuery)
        features: Map<String, Boolean>,

        // Предикат для определения доступности действия
        predicate: Predicate
    )

    // Конфигурация колонки
    JournalColumnDef {

        // Идентификатор колонки
        val id: String,

        // Отображаемое имя
        val name: MLText,

        // Тип атрибута (Строка, Число и др.)
        val type: AttributeType?,

        // Атрибут для загрузки данных. Служит для указания атрибута для загрузки, который отличен от {id}.
        // Может быть вложенным (напр. ecos:counterparty.ecos:inn). Должен содержать только верхнеуровневый путь
        // к загружаемому значению без скаляров
        val attribute: String,

        // Внутренняя схема атрибута. Используется для случаев, когда стандартная схема для AttributeType не подходит.
        // Данная схема может содержать один из скаляров ('?str', '?disp', '?num' и др.) или
        // пару из двух вложенных атрибутов: '{value:name,disp:?disp}'. Для пары атрибутов обязательно
        // в качестве алиасов должны использоваться 'value' и 'disp'
        val attSchema: String,

        // Описание редактора, который будет использован в фильтрах и при инлайн редактировании.
        val editor: ColumnEditorDef,

        // Описание форматтера, который будет использован при отрисовке ячеек в колонке.
        val formatter: ColumnFormatterDef,

        // Можно ли искать по колонке
        val searchable: Boolean?,

        // Можно ли искать по колонке используя произвольный текст
        val searchableByText: Boolean?,

        // Можно ли сортировать по колонке
        val sortable: Boolean?,

        // Можно ли группировать по колонке
        val groupable: Boolean?,

        // Доступно ли инлайн редактирование в колонке
        val editable: Boolean?,

        // Отображается ли клонка по умолчанию.
        val visible: Boolean?,

        // Есть ли возможность добавить колонку в журнал для отображения.
        // Полезно когда отображать колонку нельзя, но искать по ней можно (searchable=true).
        val hidden: Boolean?,

        // Значения в колонке множественные или нет
        val multiple: Boolean?,

        // Вычисляемые значения для использования в форматтерах и редакторах
        val computed: List<JournalComputedDef>,

        // Дополнительные свойства для поддержки произвольных настроек,
        // которые очень специфичны, чтобы стать частью основного конфига.
        val properties: ObjectData = ObjectData.create()
    }

    // Конфигурация редактора
    ColumnEditorDef {
        type: String,
        config: ObjectData
    }

    // Конфигурация форматтера
    ColumnFormatterDef {
        type: String,
        config: ObjectData
    }

    // Конфигурация вычисляемого значения
    JournalComputedDef {
        id: String,
        type: String,
        config: ObjectData
    }


Инструменты для разработчиков
-----------------------------

1. Если на странице журналов нажать :guilabel:`Ctrl` + :guilabel:`Shift` + :guilabel:`ЛКМ` на заголовке журнала, то откроется его конфигурация для просмотра.
