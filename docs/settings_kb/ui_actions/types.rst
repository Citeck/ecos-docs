.. _ui_actions_types:

Типы действий
=============

Справочник по встроенным типам действий Citeck: идентификатор типа (``type``) и доступные параметры ``config``.

.. contents::
    :depth: 3

Общедоступные действия
------------------------

view
~~~~~~~~~

id типа: ``view``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * - Открыть запись на просмотр.
        -
           | Дополнительные параметры для config:
           | **background: Bool** - открыть запись в новой вкладке приложения в фоновом режиме;
           | **reopen: Bool** - открыть запись в текущей вкладке приложения;
           | **newBrowserTab: Bool** - открыть запись в новой вкладке браузера
           | **reopenBrowserTab: Bool** - открыть запись в текущей вкладке браузера (с перезагрузкой страницы).


edit
~~~~~~~~~~

id типа: ``edit``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * - Редактировать запись.
        - **attributes: Object<String, String>** - атрибуты, которые будут прокинуты на форму создания. Необязательный параметр


download
~~~~~~~~~~~~~~

id типа: ``download``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
           | Скачать некоторый контент связанный (или не связанный) с записью.
           | По умолчанию скачивается контент записи
        - **url** - URL для скачивания. Можно добавлять ``${recordRef}`` для подстановки текущей записи.

delete
~~~~~~~~~~~~

id типа: ``delete``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * - Удалить запись
        -
          .. code-block:: json

            {
              "config" : {
                  "isWaitResponse" : false,
                  "withoutConfirm" : true
              },
              "type" : "delete"
            }

          | **isWaitResponse** - ожидание ответа удаления (по умолчанию ``true``)
          | **withoutConfirm** - удаление без подтверждения (по умолчанию ``false``)

download-card-template
~~~~~~~~~~~~~~~~~~~~~~~~~~~

id типа: ``download-card-template``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Скачать печатную версию документа
        - | **templateType** - тип шаблона
          | **format** - формат (html, pdf, pdf2, docx)

download-by-template
~~~~~~~~~~~~~~~~~~~~~~~~~~~

id типа: ``download-by-template``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Скачать документ по шаблону
        - | **templateRef** - ссылка на шаблон
          | **resultName** - имя файла, который будет скачан
          | **requestParams** - дополнительные параметры, которые будут отправлены на сервер

view-card-template
~~~~~~~~~~~~~~~~~~~~~~~~~

id типа: ``view-card-template``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Просмотр печатной версии документа в новой вкладке браузера
          | (возвращаемый документ такой же как для события ``download-card-template``)
        - | **templateType** - тип шаблона
          | **format** - формат (html, pdf, pdf2, docx)
          | **includeTimezone** (по умолчанию - ``true``)

create
~~~~~~~~~~

id типа: ``create``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Действие для создания нового документа.
          | Обычно применяется когда требуется создать новый документ, в котором некоторые поля будут предзаполнены из данных текущего открытого документа.
        - | **typeRef: String** - тип данных для создания. Обязательный параметр;
          | **createVariantId: String** - Идентификатор варианта создания для типа. Если не указан, то используется первый доступный вариант
          | **createVariant: Object** - Вариант создания для ситуаций, когда ни один вариант создания из типа не походит и требуется его полностью определить в действии
          | **attributes: Object** - Предопределенные атрибуты для создания новой сущности. Для прокидывания атрибутов с текущей записи (т.е. той, с которой выполняется действие) на форму создания можно использовать вставки вида ``${attribute_name}``
          | **options: Object** - Опции формы
          |
          | **Пример:**
          |
          | Создание сущности с типом emodel/type@request-to-manager и проставлением в атрибут "incident" ссылки на текущий документ

            .. code-block:: yaml

                id: request-to-manager
                name:
                  en: Request to manager
                  ru: Запрос руководителю
                type: create
                config:
                  typeRef: emodel/type@request-to-manager
                  redirectToPage: false
                  attributes:
                    incident: "${?id}"


save-as-case-template
~~~~~~~~~~~~~~~~~~~~~~~~~~

id типа: ``save-as-case-template``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Создается шаблон, затем по условию конфигурации - скачивание или переход на дашборд.
        - | **download**
          | По умолчанию скачивается контент записи.

              * ``true`` (по умолчанию) - скачивается шаблон;
              * ``false`` - редирект на дашборд шаблона

open-url
~~~~~~~~~~~~~~

id типа: ``open-url``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Открывает заданный URL относительно текущего стенда.
        - | **URL** - можно добавлять ``${recordRef}`` для подстановки текущей записи


assoc-action
~~~~~~~~~~~~~~~~~

id типа: ``assoc-action``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Выполняет действие над указанной ассоциацией.
        - | **assoc** - ассоциация
          | **action** - объект действия

content-preview-modal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

id типа: ``content-preview-modal``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Модальное окно с предпросмотром документа.
          | В конфигурации действия ожидается поле **scale**.
          | Возможные значения:
              | **auto**
              | **0…4**
              | **page-fit**
              | **page-height**
              | **page-width**
        - | **recordRef**


fetch
~~~~~~~~~~~

id типа: ``fetch``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Отправляет запрос на указанный URL
        - | **url**
          | **method**
          | **args** - аргументы, которые будут переданы в URL
          | **body** - аргументы, которые будут переданы в тело запроса


view-business-process
~~~~~~~~~~~~~~~~~~~~~~~~~~

id типа: ``view-business-process``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Просмотреть Бизнес-процесс
          | (окно с превью процесса и доп. действиями).
        - | **workflowFromRecord [true/ false]**

              * ``workflowFromRecord = true`` => получает **workflow id** из переданного **record** в действие
              * ``workflowFromRecord = false`` => указанное значение **record** является **workflow id**

mutate
~~~~~~~~~~~~

.. _mutate_action:

id типа: ``mutate``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Внесение изменений без участия пользователя посредством передачи атрибутов.
          | Доступно для ``execForRecord``, ``execForRecords``
        - |

          .. code-block:: yaml

            config: {
              implSourceId: "ARTIFACTID_ПРОЕКТА/id_действия@"
              record: {
                  id: "${recordRef}",
                    attributes: { "key": "value" }
                  }
                }

          | **implSourceId** - возможность получить ссылку для скачивания файла с карточки и определенной записи в журнале
          | **record.id** - необязательный параметр
          | **record.attributes** - изменяемые поля и их значения

.. dropdown:: Пример: Настройка группового действия Изменить инициатора
   :color: secondary

   1. В журнале перейти во вкладку **«Действия»**:

   .. image:: ../_static/ui_actions/Mutate/mutate_1.png
      :width: 600
      :align: center

   .. list-table::
      :widths: 10 30 30 30
      :header-rows: 1
      :align: center
      :class: tight-table

      * - п/п
        - Наименование
        - Описание
        - Пример заполнения
      * - 1
        - **Id**
        - уникальный идентификатор
        - guide-action
      * - 2
        - **Имя**
        - наименование действия
        - Изменить инициатора
      * - 3
        - **Тип**
        - тип действия
        - mutate
      * - 4
        - **Ключ**
        - ключ конфигурации
        - ``record``
      * - 5
        - **Значение**
        - значение конфигурации
        - ``{attributes:{requester:requester}}``
      * - 6
        - **Форма**
        - выбрать форму ввода данных
        - Изменить инициатора (form-action-guide)
      * - 7
        - **Ключ**
        - ключ параметра формы подтверждения
        - ``record.attributes.requester``
      * - 8
        - **Значение**
        - значение параметра формы подтверждения
        - ``requester``
      * - 9
        - **Применимость**
        - Применить для записи, записей, поискового запроса. См. :ref:`подробно<applicability>`
        - все в true

   2. Пользователь отмечает некоторые строки в журнале и выбирает в выпадающем меню над журналом действие:

   .. image:: ../_static/ui_actions/Mutate/mutate_2.png
      :width: 600
      :align: center

   3. Открывается форма для уточнения значений атрибута для выполнения действия и нажимает кнопку:

   .. image:: ../_static/ui_actions/Mutate/mutate_3.png
      :width: 400
      :align: center

.. dropdown:: Пример: Настройка действия Изменить статус
   :color: secondary

   Конфиг действия:

   .. code-block:: json

     {
         "id": "change-status",
         "name": {
           "ru": "Изменить статус",
           "en": "Change status"
         },
         "confirm":{
           "title": {
           "ru": "Изменить",
           "en": "Change"
           },
         "message":{},
         "formRef":"uiserv/form@change-status-form",
         "formAttributes":{},
         "attributesMapping":{
           "record.attributes._status": "statuses"
           }
         }
         "type": "mutate",
         "config": {
           "record": {
             "id": "${recordRef}"
             "attributes": {}
             }
           }
         }
       }

   Форма, которая предлагается пользователю:

   .. image:: ../_static/ui_actions/Change_status/change_1.png
      :width: 600
      :align: center

   Через компонент **Async Data** добавляются статусы типа данных:

   .. image:: ../_static/ui_actions/Change_status/change_2.png
      :width: 600
      :align: center

   Настройки компонента **ECOS Select**:

   .. grid:: 2
      :gutter: 2

      .. grid-item::

         .. image:: ../_static/ui_actions/Change_status/change_3.png
            :width: 500
            :align: left

      .. grid-item::

         .. image:: ../_static/ui_actions/Change_status/change_4.png
            :width: 500
            :align: left

   Скрипт для перебора массива для получения id статуса:

   .. code-block:: javascript

     var statuses = _.get(data, "stats.statuses");
     var arr = [];

     for(var i = 0; i < statuses.length; i++) {
       var id = statuses[i].id;
       arr.push(id);
     }
     values = arr;

   Полученные статусы в форме :ref:`локализуются<form_localisation>`:

   .. image:: ../_static/ui_actions/Change_status/change_5.png
      :width: 600
      :align: center

   Действие в интерфейсе:

   .. grid:: 2
      :gutter: 2

      .. grid-item::

         .. image:: ../_static/ui_actions/Change_status/change_6.png
            :width: 500
            :align: left

      .. grid-item::

         .. image:: ../_static/ui_actions/Change_status/change_7.png
            :width: 500
            :align: left

.. dropdown:: Пример: Настройка группового действия Выгрузить данные в файл
   :color: secondary

   Пример группового действия для выгрузки в txt файл некоторых данных из выбранных записей (в примере - ``_created``) с возможностью скачивания.

   Конфиг действия:

   .. code-block:: yaml

     id: example-unload-to-file
     type: mutate
     name:
       ru: Выгрузить в файл
       en: Unload
     confirm:
       title:
         ru: Подтвердите действие
         en: Confirm the action
       message:
         ru: Выгрузить в файл
         en: Unload
     config:
       implSourceId: ЗДЕСЬ_ARTIFACTID_ВАШЕГО_ПРОЕКТА/example-unload
     features:
       execForQuery: false
       execForRecord: true
       execForRecords: true

   RecordsDAO для действия (метод ``getId()`` должен возвращать значение из implSourceId в конфигурации):

   .. code-block:: java

     import lombok.extern.slf4j.Slf4j;
     import org.jetbrains.annotations.NotNull;
     import org.jetbrains.annotations.Nullable;
     import org.springframework.beans.factory.annotation.Autowired;
     import org.springframework.stereotype.Component;
     import ru.citeck.ecos.commons.data.DataValue;
     import ru.citeck.ecos.records3.RecordsService;
     import ru.citeck.ecos.records3.record.dao.mutate.ValueMutateDao;
     import ru.citeck.ecos.webapp.api.content.EcosContentApi;
     import ru.citeck.ecos.webapp.api.entity.EntityRef;

     import java.util.*;

     @Component
     @Slf4j
     public class ExampleUnloadToFileRecordsDao implements ValueMutateDao<DataValue> {

         private final RecordsService recordsService;
         private final EcosContentApi contentApi;

         @Autowired
         public ExampleUnloadToFileRecordsDao(RecordsService recordsService, EcosContentApi contentApi) {
             this.recordsService = recordsService;
             this.contentApi = contentApi;
         }

         @NotNull
         @Override
         public String getId() {
             return "example-unload";
         }

         @Nullable
         @Override
         public Object mutate(@NotNull DataValue selectedRecords) throws Exception {
             List<String> recordRefs = selectedRecords.get("records").asList(String.class);
             List<String> data = new ArrayList<>(Collections.emptyList());

             for (String record : recordRefs) {
                 data.add(recordsService.getAtt(record,"_created").asText());
             }

             EntityRef tempRef = contentApi.uploadTempFile()
                 .writeContent(writer -> {
                     writer.writeText(data.toString());
                     return null;
                 });

             String url = recordsService.getAtt(tempRef, "_content.url").asText();

             return DataValue.createObj()
                 .set("type", "link")
                 .set("data", DataValue.createObj()
                     .set("url", url)
                 );
         }

     }

   В интерфейсе при активации действия из выбранных записей были получены их ``_created`` и записаны в файл, который доступен для скачивания:

   .. image:: ../_static/ui_actions/Data_to_file/data_to_file_1.png
      :width: 600
      :align: center

   Подробнее о :ref:`EcosContentApi<EcosContentApi>`

.. dropdown:: Пример: Действие для вывода в консоль информации о данных
   :color: secondary

   .. image:: ../_static/ui_actions/to_console_1.png
      :width: 600
      :align: center

   |

   .. image:: ../_static/ui_actions/to_console_2.png
      :width: 600
      :align: center

   Конфиг действия:

   .. code-block:: json

     {
       "id": "print-to-console",
       "name": {
         "ru": "Вывести в консоль",
         "en": "Print to console"
       },
       "confirm": {
         "title": {
           "ru": "Подтвердите действие",
           "en": "Confirm the action"
         },
         "message": {
           "ru": "Вывести в консоль",
           "en": "Print to console"
         },
         "formRef": "",
         "formAttributes": {},
         "attributesMapping": {}
       },
       "type": "mutate",
       "config": {
         "record": {
           "id": "minimal-webapp/print-to-console@",
           "attributes": {
             "employee": "${employee}",
             "position": "${position}",
             "start_date": "${start_date}"
           }
         }
       },
       "features": {
         "execForRecords": false,
         "execForQuery": false,
         "execForRecord": true
       }
     }

   DTO для необходимого набора данных - SalaryDataDto.java

   .. code-block:: java

     package ru.citeck.ecos.webapp.sample.minimal.dto;

     import lombok.Data;

     import java.util.Date;

     @Data
     public class SalaryDataDto {
         private String employee;
         private String position;
         private Date start_date;
     }

   И DAO класс, который будет все это обрабатывать - JavaPrintToConsoleRecordsDao.java

   .. code-block:: java

     package ru.citeck.ecos.webapp.sample.minimal.service.java.action;

     import org.jetbrains.annotations.NotNull;
     import org.jetbrains.annotations.Nullable;
     import org.springframework.stereotype.Component;
     import ru.citeck.ecos.records3.record.dao.mutate.ValueMutateDao;
     import ru.citeck.ecos.webapp.sample.minimal.dto.SalaryDataDto;


     @Component
     public class JavaPrintToConsoleRecordsDao implements ValueMutateDao<SalaryDataDto> {

         @NotNull
         @Override
         public String getId() {
             return "print-to-console";
         }

         @Nullable
         @Override
         public Object mutate(@NotNull SalaryDataDto salaryDataRecord) {
             String salaryInfo = String.format("Сотрудник: %s%nДолжность: %s%nДата приема: %s%n",
                     salaryDataRecord.getEmployee(), salaryDataRecord.getPosition(), salaryDataRecord.getStart_date());
             System.out.println("###################\n");
             System.out.println(salaryInfo);
             System.out.println("###################");
             return null;
         }

     }

   Обратите внимание, связь между конфигой и обработчиком осуществляется за счет указания ID обработчика в конфиге.

.. dropdown:: Пример: Групповое действие с выгрузкой данных в файл
   :color: secondary

   .. image:: ../_static/ui_actions/unload_to_file_1.png
      :width: 600
      :align: center

   |

   .. image:: ../_static/ui_actions/unload_to_file_2.png
      :width: 600
      :align: center

   Конфиг действия:

   .. code-block:: json

     {
       "id": "unload-salary-data-to-file",
       "name": {
         "ru": "Выгрузить в файл",
         "en": "Unload to file"
       },
       "confirm": {
         "title": {
           "ru": "Подтвердите действие",
           "en": "Confirm the action"
         },
         "message": {
           "ru": "Выгрузить в файл",
           "en": "Unload to file"
         },
         "formRef": "",
         "formAttributes": {},
         "attributesMapping": {}
       },
       "type": "mutate",
       "config": {
         "implSourceId": "minimal-webapp/unload-to-file"
       },
       "features": {
         "execForRecords": true,
         "execForQuery": false,
         "execForRecord": false
       }
     }

   DAO класс - JavaUnloadToFileRecordsDao.java

   .. code-block:: java

     package ru.citeck.ecos.webapp.sample.minimal.service.java.action;

     import lombok.AllArgsConstructor;
     import lombok.Data;
     import lombok.NoArgsConstructor;
     import org.jetbrains.annotations.NotNull;
     import org.jetbrains.annotations.Nullable;
     import org.springframework.beans.factory.annotation.Autowired;
     import org.springframework.stereotype.Component;
     import ru.citeck.ecos.commons.data.DataValue;
     import ru.citeck.ecos.records3.RecordsService;
     import ru.citeck.ecos.records3.record.dao.mutate.ValueMutateDao;
     import ru.citeck.ecos.webapp.api.content.EcosContentApi;
     import ru.citeck.ecos.webapp.api.entity.EntityRef;

     import java.util.Date;
     import java.util.List;


     @Component
     public class JavaUnloadToFileRecordsDao implements ValueMutateDao<DataValue> {
         private final RecordsService recordsService;
         private final EcosContentApi contentApi;

         @Autowired
         public JavaUnloadToFileRecordsDao(RecordsService recordsService, EcosContentApi contentApi) {
             this.recordsService = recordsService;
             this.contentApi = contentApi;
         }

         @NotNull
         @Override
         public String getId() {
             return "unload-to-file";
         }

         @Nullable
         @Override
         public Object mutate(@NotNull DataValue selectedRecords) {
             List<String> recordRefs = selectedRecords.get("records").asList(String.class);
             List<SalaryRecordData> salaryRecordsData = recordsService.getAtts(recordRefs, SalaryRecordData.class);

             String salaryDataAsPrettyString = formatSalaryDataList(salaryRecordsData);

             EntityRef tempRef = contentApi.uploadTempFile()
                     .writeContentJ(writer -> {
                         writer.writeText(salaryDataAsPrettyString);
                     });

             String url = recordsService.getAtt(tempRef, "_content.url").asText();

             return DataValue.createObj()
                     .set("type", "link")
                     .set("data", DataValue.createObj()
                             .set("url", url)
                     );
         }

         public String formatSalaryDataList(List<SalaryRecordData> salaryRecordsData) {
             StringBuilder sb = new StringBuilder();
             for (SalaryRecordData record : salaryRecordsData) {
                 sb.append("\nСотрудник: ").append(record.getEmployee()).append(",\n");
                 sb.append("Должность: ").append(record.getPosition()).append(",\n");
                 sb.append("Дата приема: ").append(record.getStart_date()).append(",\n\n");
             }
             sb.append("\n");
             return sb.toString();
         }

         @Data
         @NoArgsConstructor
         @AllArgsConstructor
         static class SalaryRecordData {
             private String employee;
             private String position;
             private Date start_date;
         }
     }

task-outcome
~~~~~~~~~~~~~~~~~~

id типа: ``task-outcome``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Действие используется в связке с ``tasks-actions``.
          | Действие связано с бизнес-процессом записи.
        - |
          | **label** - заголовок варианта завершения задачи
          | **outcome** - идентификатор варианта завершения задачи
          | **formRef** - ссылка на форму задачи (uiserv/eform@...)
          | **taskRef** - ссылка на задачу (wftask@flowable$12345)

tasks-actions
~~~~~~~~~~~~~~~~~~~

id типа: ``tasks-actions``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          | Действие для загрузки вариантов завершения задач
        - |
          | На выходе для каждой задачи получается основное действие и ``variants`` с типом ``task-outcome`` где перечислены варианты завершения

           .. image:: ../_static/ui_actions/actions_1.png
              :width: 200
              :align: center

          | Отображаются только задачи, которые может завершить текущий пользователь. Т.е. то же самое что и в виджете "Мои задачи".
          | Варианты завершения загружаются из конфигурации формы для задачи.
          | Находятся все кнопки с ключом outcome_* и преобразуются в варианты создания.
          | Если у задачи на форме есть поля, то показывается всплывающая форма с этими полями:

           .. image:: ../_static/ui_actions/actions_2.png
              :width: 400
              :align: center

          | Если у задачи на форме нет полей, то показывается следующее окно:

           .. image:: ../_static/ui_actions/actions_3.png
              :width: 300
              :align: center

          | Если форма пустая и в конфигурации для tasks-actions задано как ``hideConfirmEmptyForm=true``, окно не появляется, форма выполняется, действие завершается, уведомление, если успешно, появляется.

              .. code-block::

                {
                  "id": "tasks-actions",
                  "name": {
                    "ru": "Действия для завершения задач",
                    "en": "Actions to complete tasks"
                  },
                  "type": "tasks-actions",
                  ------------------------new-------------------
                  "config": {
                    "hideConfirmEmptyForm": true <<<
                  }
                  ----------------------------------------------
                }

          | При выполнение вариантов действия, в каждый вариант передаются некоторые конфигурации:
          | то есть ``config`` из ``tasks-actions`` передается в ``task-outcome``.
          | При этом у ``task-outcome`` может быть свой конфиг, который может перезаписать прошедшие настройки.

open-submit-form
~~~~~~~~~~~~~~~~~~~~

id типа: ``open-submit-form``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          |
          | Вызов формы редактирования с попыткой отправить в рассмотрение.
          | Действие связано с бизнес-процессом записи.
        - |
          | Если все поля заполнены корректны, форма отправляется и закрывается.
          | Иначе отображается список ошибок, после их исправления отправление вручную.
          | **config.formId** - необязательный параметр; без указания загружается форма по умолчанию.

            .. code-block:: json

                "config": {
                    "formId": "...",
                            }

user-event
~~~~~~~~~~~

.. _user_event_action:

id типа: ``user-event``

Для формирования пользовательских эвентов и возможности на них реагировать :ref:`в BPMN<user_event_bpmn>` добавлен новый тип действия user-event, которое кидает ecos-event.

Например:

.. code-block:: yaml

  ---
  id: user-event-action1

  name:
    ru: Пользовательское действие 1
    en: User event action 1

  type: user-event

  config:
    record: ${?id}
    eventData:
      priority: 1
      counterpartInitiator: ${counterparty.initiator}
      counterpartyRef: ${counterparty?id}
      house:
        kitchen: red
        livingRoom: blue


В итоге в системе будет сформирован **ecos event**:

   * **Тип**. Всегда равен id действия. В данном случае *user-event-action1*
   * **Рекорд**, по которому произошел эвент. То, что указано в record, *${?id*} означает, что по текущему документу, из которого вызывается действие. Если record не указан, эвент глобальный (не привязан к какому-то конкретному рекорду)
   * **Полезная нагрузка эвента**. Все, что указано в *eventData*. На первом уровне атрибутов можно передавать данные в виде *entityRef*, для этого можно воспользоваться синтаксисом ${some_attribute?id}.

Типы без дополнительных параметров
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Действия ниже не принимают собственных параметров в ``config`` (кроме отмеченных примечанием):

.. grid:: 1
   :gutter: 2

   .. grid-item-card:: Открыть в фоне
      :class-header: sd-font-weight-bold

      ``open-in-background``

      - Открыть запись в новой фоновой вкладке.

   .. grid-item-card:: Загрузить новую версию
      :class-header: sd-font-weight-bold

      ``upload-new-version``

      - Загрузка новой версии документа.

   .. grid-item-card:: Отменить бизнес-процесс
      :class-header: sd-font-weight-bold

      ``cancel-business-process``

      - Отменить бизнес-процесс.

   .. grid-item-card:: Изменить пароль
      :class-header: sd-font-weight-bold

      ``edit-password``

      - Изменение пароля.

   .. grid-item-card:: edit-menu
      :class-header: sd-font-weight-bold

      ``edit-menu``

      - Запустить редактор конфигурации меню.
      - Действие для версии конфигурации > 0.

   .. grid-item-card:: view-menu
      :class-header: sd-font-weight-bold

      ``view-menu``

      - Запустить редактор конфигурации меню.
      - Действие для версии конфигурации > 0.


Enterprise действия
-------------------

transform
~~~~~~~~~~

id типа: ``transform``

.. list-table::
      :widths: 10 10
      :header-rows: 1
      :class: tight-table
      :align: center

      * - Описание
        - Конфигурация
      * -
          |
          | Трансформация содержимого по заданным правилам и его скачивание или загрузка в атрибут с типом "контент"
        -
          |
          | **input: Object** // источник содержимого. По умолчанию - основное содержимое текущего документа;
          | **transformations: Object[]** // описание трансформаций;
          | **output: Object** // цель для результата трансформации. По умолчанию - временный файл, контент которого сразу же скачивается.
          |
          | Подробнее о возможных настройках input, transformations и output можно прочитать :ref:`здесь<Content_transformation>`
          |
          | **Пример:**
          |
          | 1. Сконвертировать содержимое в PDF и скачать:

            .. code-block:: yaml

                id: download-as-pdf
                type: transform
                name: Скачать как PDF
                config:
                  transformations:
                    - type: convert
                      config: { toMimeType: 'application/pdf' }

.. _download_with_barcode:

.. dropdown:: Пример: Настройка действия Скачать с штрихкод
   :color: secondary

   Конфиг действия:

   .. code-block:: json

     {
       "id": "test-action-transform",
       "name": {
         "ru": "Скачать с штрих-код",
         "en": "Download with barcode"
       },
       "type": "transform",
       "config": {
         "transformations": [
           {
             "type": "convert",
             "config": {
               "toMimeType": "application/pdf"
             }
           },
           {
             "type": "barcode",
             "config": {
               "entityRef": "${?id}",
               "layout": "BOTTOM_RIGHT",
               "pages": "ALL"
             }
           }
         ]
       }
     }

   ``layout`` - выбор положения баркода с возможными значениями: TOP_LEFT, TOP_CENTER, TOP_RIGHT, BOTTOM_LEFT, BOTTOM_CENTER, BOTTOM_RIGHT

   До добавления действия в тип данных необходимо:

   - добавить :ref:`аспект Имеет штрих-код<barcode_aspect>` в тип данных;

   - добавить :ref:`шаблон нумерации<number_template>` в тип данных.
