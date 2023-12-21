Действия
========

Раздел содержит описание работы действий в ECOS с Alfresco.

Типы действий
-------------

edit-task-assignee
~~~~~~~~~~~~~~~~~~~~~~~~

id типа: ``edit-task-assignee``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table 
      
      * - Описание
        - Конфигурация
      * -  
          | Редактировать исполнителя задачи (запускается окно с выбором исполнителя).
          | Действие связано с бизнес-процессом записи. 
        - | **actionOfAssignment [claim , release]** 
          | **orgstructParams:{ userSearchExtraFields: custom:property1, custom:property2 }**
          | custom:property1, custom:property2 - строка. Свойста ноды пользователя, по которым будет осущетствлен поиск

set-task-assignee
~~~~~~~~~~~~~~~~~~~~~~~~

id типа: ``set-task-assignee``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table 
      
      * - Описание
        - Конфигурация
      * -  
          | Назначение исполнителя задачи 
          | (расширенный вариант edit-task-assignee)
        - | **assignTo** - на кого назначить [me , group , someone]:
 
              * ``someone`` - если не указан assignee, запускается ``edit-task-assignee`` для выбора 
              * ``me`` - исполнитель устанавливается автоматически (текущий пользователь)
              * ``group`` - возврат в группу

          | Необязательные параметры (можно использовать дополнительно или вместо assignTo):

              * **actionOfAssignment** - [claim , release]
                
                * ``release`` - вернуть в группу

              * **assignee** -  ``workspace исполнителя`` - если ``claim`` и значения нет - выбор через окно
              * **errorMsg** - сообщение об ошибки выполнения

          ``assignTo: 'me'`` или 

          ``actionOfAssignment: 'claim'``

          ``assignee: 'workspace://SpacesStore/......'``
            
          |

            .. code-block::

              
              config: { 
                      errorMsg: 'text'
                          }

alf-download-report-group-action-xlsx
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Действие предназначено для выгрузки выбранных записей в формат **xlsx**.

В конфигурацию группового действия **alf-download-report-group-action-xlsx** добавлены параметры:

  * ``dateFormat``-  формат даты https://docs.oracle.com/javase/7/docs/api/java/text/SimpleDateFormat.html, который применяется при выгрузке атрибутов с типом ``DATE``
  * ``decimalFormat``-  числовой формат https://docs.oracle.com/javase/tutorial/i18n/format/decimalFormat.html, который применяется при выгрузке атрибутов с типом ``NUMBER``

Пример конфига действия с заданными параметрами:

.. code-block::

  {
    "id": "alf-download-report-group-action-xlsx",
    "name": {
      "ru": "Скачать Excel-файл",
      "en": "Download Excel-file"
    },
    "type": "server-group-action",
    "config": {
      "id": "download-report-xlsx-action",
      "params": {
        "template": "alfresco/templates/reports/ru/citeck/default.xlsx",
        "reportTitle": "REPORT",
        "actionId": "download-report-xlsx-action",
        "evaluateBatch": "true",
        "columns": "${reportColumns}",
        "batchSize": 1000,
        "pageSize": 1000,
        "elementsLimit": 20000,
        "dateFormat": "dd.MM.yyyy",
        "decimalFormat": "#,##0.00",
        "output": {
          "type": "email",
          "config": {
            "templateRef": "notifications/template@skif-report-email-notification"
          }
        }
