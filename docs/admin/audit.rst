Аудит
======

.. contents::

**Аудит (журнал событий)** предназначен для ведения лог-файлов, в которые записываются события системы, а именно:

  * Поиск записей
  * Получение атрибутов записей по их ID
  * Изменение атрибутов или создание новой записи
  * Удаление записей

Запись о событии содержит заданный в настройках набор информации о событии.

Основная логика аудита располагается в библиотеке **ecos-audit-lib**: https://gitlab.citeck.ru/citeck-projects/ecos-audit-lib

Аудит в ECOS настраивается через Spring-конфигурацию. 

Префикс конфигурации: ecos.webapp.audit

Доступные настройки
--------------------

.. code-block::

    enabled: Boolean // включить или выключить аудит. По умолчанию false
    pipelines: Map<String, PipelineProps> // конфигурация конвееров
    outputs: Map<String, OutputProps> // конфигурация выходов

PipelineProps:

.. code-block::

    enabled: Boolean // включен или нет конвеер. По умолчанию true
    filter: EcosAuditEventFilterProps // настройки фильтрации
    processors: List<EcosAuditProcessorProps> // процессоры
    outputs: List<String> // выходы    

EcosAuditEventFilterProps:

.. code-block::

    type: TypeFilter // фильтр по типу
    authority: AuthorityFilter // фильтр по текущему пользователю 
    headers: Predicate // фильтр по хидерам. Предикат задается в виде строки.
    eventData: Predicate // фильтр по содержимому события. Предикат задается в виде строки.

TypeFilter

.. code-block::

    includes: List<String> // обрабатывать только события из этого списка
    excludes: List<String> // исключить обработку событий из этого списка

.. note::

    в includes и excludes для типов поддерживаются шаблоны. Тип события разбивается по символам “.“ на слова и дальше идет сопоставление с includes и excludes. Если в настройках встречается символ #, то он означает “любое количество слов включая 0”, символ * означает - одно любое слово.


AuthorityFilter

.. code-block::

    includes: List<String> // обрабатывать только события от пользователей, ролей и/или групп из этого списка
    excludes: List<String> // исключать события от пользователей, ролей и/или групп из этого списка
    includeSystem: Boolean // фиксировать действия системы. По умолчанию false 

Пример настройки
-----------------

.. code-block::

    ecos:
    webapp:
        audit:
        enabled: true
        pipelines:
            main:
            filter:
                type:
                includes: [
                    "records.query-records",
                    "records.get-records-atts",
                    "records.mutate-record",
                    "records.delete-records"
                ]
                headers: |
                {"t":"like","att":"sourceId","val":"%-cipher"}
            outputs: ["rabbitmq", "log"]
        outputs:
            rabbitmq:
            type: rabbitmq
            log:
            type: log

.. list-table::
      :widths: 10 10 40
      :header-rows: 1
      :align: center 

      * - type
        - Конфигурация
        - Описание
      * - rabbitmq
        - 
        - Отправлять события в RabbitMQ на  exchange “ecos-audit“ с RoutingKey == {тип_события}
      * - log
        - 
        - Выводить события в лог микросервиса

Типы событий:

.. list-table:: 
      :widths: 10 30 30 30
      :header-rows: 1
      :align: center 

      * - type
        - Поля
        - Хидеры
        - Описание
      * - records.query-records
        - |

          .. code-block::

            sourceId: String
            query: RecordsQuery
            records: List<EntityRef>
            attributes: Map<String, String>

        - |

          .. code-block::

            sourceId: String
            appName: String
            appInstanceId: String

        - Поиск записей
      * - records.get-records-atts
        - |

          .. code-block::

            sourceId: String
            record: EntityRef
            attributes: Map<String, String>

        - |

          .. code-block::

            sourceId: String
            appName: String
            appInstanceId: String

        - Получение атрибутов записей по их ID
      * - records.mutate-record
        - |

          .. code-block::

            sourceId: String,
            record: EntityRef,
            attributes: ObjectData,
            attsToLoad: Map<String, String>

        - |

          .. code-block::

            sourceId: String
            appName: String
            appInstanceId: String

        - Изменение атрибутов или создание новой записи
      * - records.delete-records
        - |

          .. code-block::

            sourceId: String
            records: List<EntityRef>

        - |

          .. code-block::

            sourceId: String
            appName: String
            appInstanceId: String

        - Удаление записей

Общий вид события
-----------------

.. code-block::

    id: UUID // уникальный идентификатор события
    type: String // тип события
    user: String // пользователь
    admin: Boolean // флаг определяющий является ли пользователь администратором
    client: ClientInfo // информация о клиенте. На данный момент одно поле внутри - ip: String
    time: String // ISO8601 время события
    success: Boolean // успешно или нет выполнилось действие
    actionTimeMs: Long // время выполнения действия в миллисекундах
    error: ErrorInfo // информация об ошибке. Присутствует только если success == false
    data: ObjectData // данные по событию. Для каждого типа событий свой набор данных
    appName: String // имя приложения, в котором произошло событие
    appInstanceId: String // инстанс приложения, в котором произошло событие

**ErrorInfo**

.. code-block::

    message: String // текст ошибки
    javaClass: String // класс ошибки

Описание аудита
-----------------

Модель события аудита
~~~~~~~~~~~~~~~~~~~~~~

**id:** UUID // уникальный идентификатор события. Автоматически генерируется для каждого события.

**type:** String // тип события

**user:** String // пользователь

**admin:** Boolean // флаг определяющий является ли пользователь администратором

**client:** ClientInfo // информация о клиенте. На данный момент одно поле внутри - ip: String

**time:** String // ISO8601 время события

**success:** Boolean // успешно или нет выполнилось действие

**actionTimeMs:** Long // время выполнения действия в миллисекундах

**error: ErrorInfo** // информация об ошибке. Присутствует только если **success == false**. Описание этой структуры ниже.

**data:** Map<String, Object> // данные по событию. Для каждого типа событий свой набор данных. Ниже будет список данных по типу события.

**appName:** String // имя приложения, в котором произошло событие

**appInstanceId:** String // инстанс приложения, в котором произошло событие

Модель ErrorInfo
~~~~~~~~~~~~~~~~~~~~~~

**message:** String // текст ошибки. Может формироваться произвольным образом и напрямую зависит от участка кода где эта ошибка возникла. Если нужно обрабатывать и отлавливать определенные типы ошибок, то следует сформировать список таких ошибок и сделать доработку.

**javaClass:** String // java класс ошибки. Так же как и message может быть любым, но с привязкой к существующим классам в системе.


Типы событий
~~~~~~~~~~~~~

records.query-records
""""""""""""""""""""""

Данные в поле **data**:

**sourceId:** String // Идентификатор источника данных. По нему можно сгруппировать или отфильтровать все операции (чтение, изменение, создание, удаление) в определенном источнике данных.

**query:** RecordsQuery // Поисковый запрос за данными (записями) в источнике данных.

**records:** List<EntityRef> // Список записей, который вернулись в результате запроса. :ref:`Описание EntityRef<EntityRef>`

**attributes:** Map<String, String> // Список атрибутов, которые клиент запросил у записей из списка records.

records.get-records-atts
"""""""""""""""""""""""""

Данные в поле **data**:

**sourceId:** String // Идентификатор источника данных. По нему можно сгруппировать или отфильтровать все операции (чтение, изменение, создание, удаление) в определенном источнике данных. **sourceId** всегда является частью record и если отдельное поле для фильтрации и группировки ``query/get-atts/mutate/delete`` действий не требуется, то можно **sourceId** убрать из события.

**record:** EntityRef // Ссылка на запись в источнике данных. :ref:`Описание EntityRef<EntityRef>`

**attributes:** Map<String, String> // Атрибуты, которые мы запрашиваем у записи

records.mutate-record
"""""""""""""""""""""""""

Данные в поле **data**: 

**sourceId:** String // Идентификатор источника данных. По нему можно сгруппировать или отфильтровать все операции (чтение, изменение, создание, удаление) в определенном источнике данных. **sourceId** всегда является частью record и если отдельное поле для фильтрации и группировки ``query/get-atts/mutate/delete`` действий не требуется, то можно sourceId убрать из события.

**record:** EntityRef // Ссылка на запись в источнике данных. Если record имеет вид ``"{{appName}}/{{sourceId}}@"`` (т.е. после знака @ ничего нет), то это означает, что пришел запрос на создание новой сущности. :ref:`Описание EntityRef<EntityRef>`

**attributes:** Map<String, Object> // Атрибуты, которые отправлены от клиента для обновления. Т.е. если в **attributes** мы видим {"field0": "field1"}, то это означает, что клиент пытается изменить поле "field0" присвоив ему значение "field1".

**attsToLoad:** Map<String, String> // Атрибуты для загрузки после мутации. В ряде случаев клиент отправляет в запросе помимо атрибутов, которые следует изменить так же и атрибуты, которые следует загрузить из записи после успешного окончания мутации.

records.delete-records
"""""""""""""""""""""""""

Данные в поле **data**:

**sourceId:** String // Идентификатор источника данных. По нему можно сгруппировать или отфильтровать все операции (чтение, изменение, создание, удаление) в определенном источнике данных. sourceId всегда является частью каждого элемента в records и если отдельное поле для фильтрации и группировки query/get-atts/mutate/delete действий не требуется, то можно sourceId убрать из события.

**records:** List<EntityRef> // Список записей для удаления. :ref:`Описание EntityRef<EntityRef>`

.. _EntityRef:

Описание EntityRef
~~~~~~~~~~~~~~~~~~~

**EntityRef** - это уникальный идентификатор сущности в системе ECOS. Он формируется по следующему шаблону:

``{{appName}}/{{sourceId}}@{{localId}}``

**appName** - имя приложения где располагается источник данных (см. поле appName в модели события). Примеры приложений: **uiserv, emodel, integrations и т.д.**

**sourceId** - это идентификатор источника данных в пределах приложения (см. поле **sourceId**)

**localId** - это локальный идентификатор сущности в пределах источника данных. Отсутствие **localId** для мутации означает создание новой записи.


Описание атрибутов для загрузки
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Атрибуты для загрузки могут иметь следующий вид:

.. code-block::

  {

    "name": "name?disp",    

    "counterparty": "counterparty.fullOrgName?str"

  }

Подобный формат атрибутов - это часть Records API (на базе которого строится все общение в ECOS).

В RecordsAPI клиент может запросить атрибуты, указав сложную вложенную струтуру, но для аудита в основном полезны только ключи в этой мапе.

То есть из примера выше мы можем получить информацию о том, что клиент запросил два атрибута - **"name"** и **"counterparty"**

Подробнее про :ref:`Records API<Records_API>`