Примеры реализации
====================

.. _Excel-import:

Пример импорта данных из Excel в ECOS
--------------------------------------------

В данном примере будет показан пример роута с использованием следующих camel-элементов:

 - FileFromCamelDslEndpoint

 - ExcelToListOfDataProcessor

 - MappingProcessor

 - AssocRefByAttributeProcessor

 - EcosRecordsMutateEndpoint

Допустим в системе есть два пользовательских типа данных - **Работник** и **Позиция**

**Работник**:

.. image:: _static/examples/XLS_import_01.png
       :width: 700
       :align: center   

**Позиция** (справочный тип, является ассоциацией в типе Работник):

.. image:: _static/examples/XLS_import_02.png
       :width: 700
       :align: center   

Необходимо импортировать следующие данные из Excel-файла (xlsx):

.. image:: _static/examples/XLS_import_03.png
       :width: 700
       :align: center   

Комментарии к столбцам таблицы: 

   1. **Работник** - никакая дополнительная обработка не требуется. Значение будет записано в виде строки
   2. **Должность** - тут видно, что в таблице используется свойство "Наименование" (системное название name) ассоциации с типом Должность. Для корректного сохранения в систему нужно будет определить RecordRef должности
   3. **Работает больше года** -  логическое значение которое перед сохранением в систему надо преобразовать в соответствующие true - false
   4. **Зарплата** - числовое значение. Показаны разные варианты записи: с разрядностью, точкой и запятой в качестве разделителя, отрицательные числа (просто ради примера). Текст заголовка намекает на то, что он может периодически редактироваться. Кроме работы с заголовком никакая дополнительная обработка числовых значений не потребуется. Они корректно запишутся как соответствующие числовые значения
   5. **Дата приема** - данный столбец в таблице имеет тип Дата и для примера показаны разные типы форматирования. Никакая дополнительная обработка значений не потребуется

Для импорта данных необходимо будет прикрепить Excel файл на форму Camel DSL и прописать следующую конфигурацию:

.. code-block::

   - beans:
       - name: "excelProcessor"
         type: ru.citeck.ecos.camel.processor.reader.ExcelToListOfDataProcessor
         properties:
             sheetName: Таблица персонала
             tableStartCellReference: C4
             customAttNames:
                 F: salary
       - name: "mappingProcessor"
         type: ru.citeck.ecos.camel.processor.data.MappingProcessor
         properties:
           keysMapping:
             Работник: name
             Должность: position
             Работает больше года: moreThenYear
             Дата приема: startDate
           valuesMapping:
             moreThenYear: 
                Да: true
                Нет: false
       - name: "assocRefByAttributeProcessor"
         type: ru.citeck.ecos.camel.processor.data.AssocRefByAttributeProcessor
   - route:
        from:
            uri: "file-from-camel-dsl:randomName"
            steps:
                - process:
                      ref: excelProcessor
                - process:
                      ref: mappingProcessor
                - setHeader:
                      name: AssocRefByAttributeConfig
                      constant:
                        sourceId: "emodel/camel-example-position"
                        findByAttribute: "name"
                        attributeKey: "position"
                - process:
                       ref: assocRefByAttributeProcessor
                - split:
                     simple: "${body}"
                     steps:
                         - to: ecos-records-mutate:?sourceId=emodel/camel-example-employee

Комментарии:

.. image:: _static/examples/XLS_import_04.png
       :width: 800
       :align: center   

После импорта получаем:

.. image:: _static/examples/XLS_import_05.png
       :width: 700
       :align: center 