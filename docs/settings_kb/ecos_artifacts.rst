.. _ecos_artifacts:

ECOS Артефакты
===============

.. contents::
  :depth: 2

Определения
-------------

**Артефакт** - единица расширения в Citeck ECOS. Артефактами являются формы, журналы, типы, матрицы прав, действия, описания процессов и многие другие сущности в системе.

Микросервис ecos-apps управляет артефактами, ведя их версионность и доставляя их до целевого микросервиса. Контент артефактов в системе неизменяемый и при любом изменении артефакта всегда создается новая версия, а старая сохраняется в списке версий.

Примеры артефактов: :guilabel:`Тип`, :guilabel:`Форма`, :guilabel:`Журнал`.

  -	**Тип данных** - основной артефакт ECM, описывающий объект. В типе данных определяются метаданные, которые будет содержать объект, статусы жизненного цикла, роли, которые могут работать с объектом. Тип данных связан с формой и журналом. 
  -	**Форма** - графическое представление объекта в виде набора элементов интерфейса для манипуляции данными объекта. Элементы интерфейса ссылаются на атрибуты, заданные в типе данных.
  -	**Журнал** - табличная форма представления объектов с возможностью настройки отображения столбцов, фильтрации и манипуляции объектами. Столбцы соответствует данным объекта или могут вычисляться на их основе.

Тип артефакта как правило состоит из двух частей разделенных символом ``/``.

* Первая часть - это область системы к которой относится артефакт. Обычно за одну область отвечает один микросервис.
* Вторая часть - локальный идентификатор типа

Например, в типе ``ui/form`` **ui** - это область, а **form** - локальный идентификатор.

**Расположение артефактов**

Все артефакты располагаются в директориях, которые соответствуют типу.
В приложении настраивается корневая папка с артефактами и в ней можно создавать подпапки ui/form, model/type и тд.
По умолчанию корневой папкой с артефактами является ``src/main/resources/eapps/artifacts``

Типы артефактов
---------------

.. list-table::
      :widths: 10 10 40
      :header-rows: 1

      * - Тип
        - Микросервис
        - Примечание
      * - ui/dashboard
        - ecos-uiserv
        - 
      * - ui/action
        - ecos-uiserv
        - 
      * - ui/admin-sections-group
        - ecos-uiserv
        - 
      * - ui/form
        - ecos-uiserv
        - 
      * - ui/i18n
        - ecos-uiserv
        - 
      * - ui/icon
        - ecos-uiserv
        - 
      * - ui/journal
        - ecos-uiserv
        - 
      * - ui/menu
        - ecos-uiserv
        -
      * - ui/theme
        - ecos-uiserv
        - 
      * - ui/board
        - ecos-uiserv
        - Канбан доска
      * - model/num-template
        - ecos-model
        - 
      * - model/permissions
        - ecos-model
        - 
      * - model/type
        - ecos-model
        - 
      * - app/ecosapp
        - ecos-apps
        - 
      * - app/artifact-patch
        - ecos-apps
        - 
      * - app/dev-module
        - ecos-apps
        -
      * - app/config
        - ecos-apps
        - 
      * - integrations/credentials
        - ecos-integrations
        - 
      * - integrations/datasource
        - ecos-integrations
        - 
      * - integrations/file-import-config
        - ecos-integrations
        - 
      * - integrations/recsrc
        - ecos-integrations
        - 
      * - integrations/sync
        - ecos-integrations
        - 
      * - process/cmmn
        - ecos-process
        - 
      * - process/bpmn
        - ecos-process
        - 
      * - process/bpmn-section
        - ecos-process
        -
      * - notification/file
        - ecos-notifications
        - 
      * - notification/template
        - ecos-notifications
        - 
      * - notification/sender
        - ecos-notifications
        -   

Переопределение артефактов
--------------------------

Для переопределения артефактов можно создать папку с именем override в корне директории с артефактами.

Пример структуры папок::

  eapps:
    - artifacts:
        - ui:
            - form:
                - some-form.json
            - journal:
                - some-journal.yml
        - override:
            - ui:
                - form:
                    - some-form.json

Для формы some-form.json будет создан патч с типом override и порядком -100 (по умолчанию). Если требуется настроить порядок,
то следует в корне папки override создать файл ``meta.yml``. В нем возможны следующие настройки:

.. list-table:: Список возможных настроек в override/meta.yml
    :header-rows: 1

    *   - Название
        - Тип данных
        - Описание
    *   - order
        - float
        - Порядок патча для перезаписи артефакта. Сначала применяются патчи с меньшим порядком.
    *   - scope
        - string
        - | Параметр служит для исключения коллизий идентификаторов override патчей.
          | Идентификатор патча формируется по следующему шаблону: override[_{{scope}}]$ui/form$some-form

**Особенности**

1. Перезапись артефактов работает вне зависимости от того откуда деплоится основной артефакт

Создание нового типа артефакта
-------------------------------

1. Определяемся в какой микросервис должен попасть артефакт после деплоя (Alfresco ведет себя аналогично микросервисам и тоже может быть целевым приложением для деплоя).

2. В целевом приложении находим папку eapps в ресурсах и создаем там подпапки следующего содержания:

   * первый уровень - раздел к которому относится артефакт (обычно 1 раздел == 1 микросервис. Например, ui → ecos-uiserv, integration → ecos-integrations, model → ecos-model и тд.)

   * второй уровень - локальный идентификатор типа (action, form, menu, dashboard, type, section и т.д.)

Не обязательно создавать именно 2 уровня, но желательно. Механизм поддерживает уровни любой вложенности от 1 до ограничений файловой системы).

.. note:: 

  Следует учитывать, что создаваемая иерархия директорий будет использована как идентификатор типа артефакта. Поэтому следует внимательно к ней отнестись.

3. Создаем в получившейся директории файл type.yml примерно со следующим содержанием:

.. code-block::

  modelVersion: "1.0"

  source-id: "eform"

  controller:
      type: json

**modelVersion** - тип модели. В будущем будет спользоваться для миграции старых артефактов.

**source-id** - ID источника данных (RecordsDAO) через который будет доступ к данным артефактам. Это поле необходимо если потребуется механизм разрешения зависимостей на стороне ECOS Apps. Если у артефакта не будет зависимостей, то можно поставить пустую строку.

**controller.type** - тип контроллера для типа артефакта. Определяет логику, по которой будут загружаться артефакты из директории и записываться в директорию. json - самый простой и понятный контроллер, который следует использовать при добавлении простых типов артефактов. Для сложных случаев существует script controller, который поддерживает описание логики чтения и записи артефактов на языке groovy (в перспективе добавятся другие языки вроде Kotlin).

1. Описываем хендлер для нашего артефакта:

.. code-block::

  @Slf4j
  все реализаци интерфейса EcosModuleHanlder в контексте будут зарегистрированы автоматически
  @Component
  @RequiredArgsConstructor
  public class FormModuleHandler implements EcosModuleHandler<EcosFormModel> {

      private final EcosFormService formService;

      При деплое артефакта он попадает в этот метод
      @Override
      public void deployModule(@NotNull EcosFormModel formModel) {
          log.info("Form module received: " + formModel.getId() + " " + formModel.getFormKey());
          formService.save(formModel);
      }

      callback для отправки изменного артефакта в ECOS Apps. Нужен для ведения истории всех ревизий
      @Override
      public void listenChanges(@NotNull Consumer<EcosFormModel> consumer) {
          formService.addChangeListener(consumer);
      }

      метод, который вызывается перед деплоем. Если он вернет null, то деплой артефакта не произойдет
      @Nullable
      @Override
      public ModuleWithMeta<EcosFormModel> prepareToDeploy(@NotNull EcosFormModel formModule) {
          return getModuleMeta(formModule);
      }

      Получение метаданных по артефакту (его ID и зависимости)
      @NotNull
      @Override
      public ModuleWithMeta<EcosFormModel> getModuleMeta(@NotNull EcosFormModel formModule) {
          return new ModuleWithMeta<>(formModule, new ModuleMeta(formModule.getId(), Collections.emptyList()));
      }

      ID типа артефакта, для которого мы описали Handler. Должен соответствовать иерархии папок из п.2
      @NotNull
      @Override
      public String getModuleType() {
          return "ui/form";
      }
  }


На этом описание типа артефакта можно считать законченным. Можно класть **.json** файлы в ``ecos-app/ui/form`` (для alfresco это ``{alfresco_module_id}/src/main/resources/alfresco/module/{alfresco_module_id}``) где вместо ui/form будет тип из п.2.

При добавлении нового типа перезагрузки требует только микросервис, где мы этот тип описываем.

.. _ecos-artifacts_yaml:

YAML формат артефакта
----------------------

С версии 3.25.0 ядра community добавлена поддержка формата yaml для описания артефактов. Версия формата YAML 1.2

Описывать в виде yaml можно любые артефакты, которые загружаются в json формате (типы, журналы, формы и др.).

После прочтения yaml файл будет преобразован в json и далее в таком виде и попадет на целевой микросервис. 

При скачивании артефакта из журнала мы все равно будем получать json вне зависимости от того как описана исходная конфигурация.

Пример описания журнала форм:

.. code-block::

  id: ecos-forms
  label: { ru: Формы, en: Forms }

  typeRef: emodel/type@form
  sourceId: uiserv/eform

  attributes:
    actionFormatter: '' #include include/legacy-actions.js

  actions:
    - uiserv/action@ecos-module-download
    - uiserv/action@delete
    - uiserv/action@edit

  columns:

    - name: moduleId
      label: { ru: Идентификатор, en: Id }

    - name: formKey
      label: { ru: Ключ формы, en: Form key }

    - name: title
      label: { ru: Название, en: Name }

    - name: description
      label: { ru: Описание, en: Description }

Возможности и особенности формата (ст - стандарные возможности, нм - наша модификация):

1. (ст) YAML 1.2 - это надмножество формата JSON. Из этого следует, что можно просто изменить расширение у артефакта с **.json** на **.yaml** и все будет работать как раньше без дополнительных изменений.

2. (нм) Поддержка #include, которая позволяет включать содержимое внешних файлов в текущую конфигурацию. 

Общий вид использования: somekey: ``'' #include filename`` 

На месте ‘' могут быть следующие значения: ‘’, ““ (для импорта содержимого файла как текста) и {} (для импорта внешней yaml конфигурации). 

filename - относительный путь до включаемого файла.

При чтении конфигурации все места с #import будут заменены на содержимое указанного файла (если будет два include одного файла, то он дважды добавится в конфиг)

3. (ст) Поддержка переиспользования частей конфига ( `https://confluence.atlassian.com/bitbucket/yaml-anchors-960154027.html <https://confluence.atlassian.com/bitbucket/yaml-anchors-960154027.html>`_ ):

.. code-block::

  some-reusable-value: &my-anchor
    aa: bb
    cc: dd

  other-key: *my-anchor
  other2-key: *my-anchor

4. (нм) Поддержка переиспользование частей конфига с переопределением значений (полу-стандартный механизм, но используемая библиоткека его не поддерживала): 

.. code-block::

  some-reusable-value: &my-anchor
    aa: bb
    cc: dd

  other-key:
    <<: *my-anchor
    cc: ee

В other-key мы получим {“aa”: “bb“, “cc“: “ee“}

Патчи для артефактов
--------------------

С версии ecos-apps 1.9.0 добавлена поддержка патчей для артефактов. Патчи сами являются артефактами и могут быть так же пропатчены. 

Патчи служат заменой механизма override, когда мы в артефакте заказчика полностью перезаписывали файлы конфигурации. Как показала практика такой подход приводит к множеству багов при переходе на новую версию коробки т.к. базовые конфигурации со временем меняются.

Патчи обновляют целевой артефакт “на лету” при каждом изменении артефакта или самого патча. Например, удалив патч в журнале мы увидим через 3-7 секунд, что изменения, которые он накладывал откатились и артефакт приобрел стандартную конфигурацию.

Список патчей в системе можно посмотреть в **системных журналах → патчи артефактов**.

Так же для них действуют возможности, которые описаны в разделе "YAML формат артефактов".

Если менять запись, на которую действует патч через интерфейс, то патч сам не переприменится. Если загружать новую версию артефакта через **ecos-apps** (подкладывая в target или при перезапуске сервера), то патч применится.

Формат патча:

.. list-table:: 
      :widths: 5 5 5 5 40
      :header-rows: 1

      * - Поле
        - Тип
        - Обязательность
        - Значение по умолчанию
        - Описание
      * - **order**
        - Float
        - Нет
        - 0
        - | Порядок патча.
          | Если в системе есть несколько патчей для одного артефакта. то они применяются в соответствии с этим порядком от меньшего к большему.
      * - **id**
        - String
        - Да
        - `-`
        - | Идентификатор. 
          | Уникальный среди всех патчей для артефактов в системе.
      * - **target**
        - ModuleRef
        - Да
        - `-`
        - | Целевой артефакт, который будет пропатчен.  
          | Записывается в виде ``тип_артефакта$локальный_id``. Пример: ``ui/journal$ecos-journals`` 
      * - **type**
        - String
        - Да
        - `-`
        - | Тип патча.
          | На данный момент поддерживается только json тип.
      * - **config**
        - ObjectData
        - Да
        - `-`
        - | Конфигурация патча
          | 

Патчи описываются в **ecos-app/module/app/module-patch** директории (для alfresco **{moduleId}-repo/src/main/resources/alfresco/module/{moduleId}-repo/app/module-patch**)

Типы патчей
~~~~~~~~~~~~

Тип патча “json”
""""""""""""""""""

В конфигурации указывается 1 параметр - **operations** с типом **“массив объектов”**.

Все операции из массива **operations** применяются последовательно к результату изменений предыдущей операции.

Тип операции определяется в ключе op и может быть следующим:

.. list-table:: 
      :widths: 5 5 40
      :header-rows: 1

      * - op
        - Описание
        - Параметры
      * - **add**
        - Добавить элемент или массив элементов в массив по пути.
        - | **path** - JsonPath до массива, в который нужно добавить элемент
          | **value** - значение или массив значений, которые следует добавить
          | **idx** - индекс, по которому следует добавить значение. По умолчанию значение добавляется в конец. Можно указывать значения вне диапазона существующего массива. В таком случае элементы будут добавляться или в начало или в конец.
      * - **set**
        - Установить явное значение любому полю.
        - | **path** - JsonPath до элемента, в который нужно поместить value
          | **key** - опциональное поле, которое определяет ключ, по которому следует поместить значение
          | **value** - значение или массив значений, которые следует установить
      * - **remove**
        - Удалить элемент из конфигурации
        - | **path** - JsonPath до элемента, в который нужно удалить
      * - **rename-key**
        - Переименовать ключ в объекте внутри конфигурации.
        - | **path** - JsonPath до объекта, в котором нужно переименовать ключ.
          | **oldKey** - старое наименование ключа
          | **newKey** - новое наименование ключа

Примеры
"""""""""

Изменить атрибут для формы:

.. code-block::

  id: change-label-for-form-field

  name:
    ru: Изменить название кнопки на форме
    en: Change button label on form

  target: ui/form$ECOS_FORM

  type: json
  config:
    operations:
      - { op: set, path: '$..[?(@.key == "localization")].label', value: 'Свое название для кнопки локализации' }

Добавить действие для типа:

.. code-block::

  id: add-some-action-for-case

  name:
    ru: Добавить действия для кейса
    en: Add actions for case

  target: model/type$cat-doc-type-general-case

  type: json
  config:
    operations:
      - { op: add, path: 'actions', value: 'uiserv/action@pdf-content-with-barcode' }

Изменить текст в локализации по ключу:

.. code-block::

  id: change-ui-admin-localization

  name:
    ru: Изменить локализацию для раздела администратора
    en: Change localization for admin section

  target: ui/i18n$menu-messages

  type: json
  config:
    operations:
      - { op: set, path: '$["messages"]["menu.header.admin-tools"][1]', value: 'Опциональный заголовок для меню администратора' }

Удалить действие:

.. code-block::

  id: delete-action

  name:
    ru: Удалить действие из типа
    en: Delete action from type

  target: model/type$contracts-cat-doctype-contract

  type: json
  config:
    operations:
      - { op: remove, path: '$.actions[?(@==\"uiserv/action@edit-in-onlyoffice\")]'}

Изменить значение параметра Конфигурации ECOS some-config-id на 123:

.. code-block::

  id: some-patch-id
  
  name:
    ru: Изменение значения параметра конфигурации some-config-id
    en: Change some-config-id config value
  
  target: app/config$app/notifications$some-config-id
  
  type: json
  config:
    operations:
      - { op: set, path: '$.value', value: [ 123 ] }
      - { op: set, path: '$.version', value: 1 }

Пример патча для добавления раздела меню:

.. code-block::

  id: menu-change-test
  name: {ru: Добавить раздел, en: Add section }
  target: 'ui/menu$default-menu-v1'
  type: json
  config:
    operations:
      - op: add
        path: '$..[?(@.id == "sections")].items'
        value: {
          "id": "custom-meetings-section",
          "label": {
            "ru": "Совещания"
          },
          "icon": "ui/icon@i-leftmenu-meetings",
          "type": "SECTION",
          "items": [
            {
              "id": "123-123-123-123-123",
              "label": {
                "en": "Совещания"
              },
              "type": "JOURNAL",
              "config": {
                "recordRef": "uiserv/journal@meetings"
              },
              "items": [],
              "allowedFor": []
            }
          ]
        }

Пример патча к булевым атрибутам компонента формы:

.. code-block::

  {
    "operations": [
      {
        "op": "set",
        "path": "$..[?(@.key==\"meetDateTime\")]",
        "key": "hidden",
        "value": true
      }
    ]
  }


Отображение артефактов разных категорий
---------------------------------------

В журналах **«Типы данных», «Формы» и «Журналы»** в фильтрах настройки таблицы можно выбрать какую категорию артефакта отражать – бизнес-данные или системные.

В фильтрах по умолчанию стоит Системный тип(форма|журнал)= **НЕТ**. 

Если выставить **ДА**, то в списке будут отражены несистемные записи. 

Если выставить **Выбрать**, то будут отражены все записи.

  .. image:: _static/artifacts/artifact_type.png
       :width: 600
       :align: center