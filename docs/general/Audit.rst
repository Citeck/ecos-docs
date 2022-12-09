Аудит
======

Основная логика аудита располагается в библиотеке ecos-audit-lib: https://gitlab.citeck.ru/citeck-projects/ecos-audit-lib

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

