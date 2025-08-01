Сигналы
========

.. _ecos_bpmn_events:

.. contents:: Содержание

**Событие «Сигнал»** обозначает ожидание или отправку сигнала между процессами. |br|
**Событие «Сигнал»** — событие, которое ссылается на именованный сигнал. |br|
**Сигнал** — событие глобального масштаба (broadcast semantics), которое доставляется всем активным обработчикам. |br|
Throw и Catch сигналов происходит по его имени. |br|
BPMN Сигналы используются для интеграции :ref:`Событий Citeck<bpmn_events_integrations>`

Определение событий (сигналов)
------------------------------

Форма
~~~~~

.. image:: _static/signal_event_form.png
  :align: center
  :width: 400

Атрибуты
~~~~~~~~

.. list-table::
      :widths: 20 40
      :align: center
      :class: tight-table 
      
      * - **Ручная настройка**
        - Флаг, который позволяет переключить настройку сигнала в ручной режим - указание имени сигнала, а не выбор из предустановленных типов событий.
      * - **Имя сигнала**
        - | Служит для идентификации сигнала. 
          | Данное поле становится доступно если включена опция ``Ручная настройка``. 
          | Если выбран ``тип события``, то имя генерируется автоматически.
      * - **Модель данных**
        - | Каждое событие имеет свою полезную нагрузку (payload).
          | Например, событие ``Статус изменен`` содержит информацию о новом и предыдущем статусе.
          | Модель данных представляет собой ``map``, где ``ключ`` - это имя атрибута, по которому будет доступно вычисленное значение, а ``значение`` - это :ref:`Records API атрибут.<Records API attribute>` 
          | Таким образом, модель данных позволяет указать какие данные будут передаваться в сигнале, при этом пользовательская модель данных имеет высший приоритет над :ref:`payload по умолчанию. <ecos_bpmn_signal_event_defaut_payload>` 
      * - **Фильтр события по документу**
        - | Позволяет отфильтровать события на основе документа, по которому возникает данное событие. 
          | Поле имеет 3 значения:

           * ``Любой документ`` - событие будет происходить для любого документа. 
           * ``Текущий документ`` - событие будет происходить только для документа по которому идет бизнес процесс.
           * ``Документ по из переменной процесса`` - событие будет возникать только для документа, который указан в поле ``Имя переменной``.

      * - **Имя переменной**
        - | Поле становится доступно, если в ``Фильтр события по документу`` выбрано значение ``Документ из переменной процесса``. 
          | В данном поле указывается имя переменной процесса, по которой будет определяться документ, для которого будет возникать событие.
          | Переменная должна содержать EntityRef документа в виде String.
      * - **Фильтр события по предикатам**
        - | Используется для фильтрации catch событий.
          | Моделью для вычисления предиката является payload события. B предикатах можно ссылаться на атрибуты из payload события через ``{{someAttribute}}``. Если атрибут используется только в предикате, то его можно испоьзовать напрямую без объявления в модели.
          | :ref:`Подробнее о предикатах<ecos-predicate_main>`

.. important::

  При сохранении, сохранении/публикации процесса проверяется обязательность заполнения следующих полей:

   - **«Тип события»**, если поле «Ручная настройка» = false;
   - **«Имя сигнала»**, если поле «Ручная настройка» = true;
   - **«Фильтр события по документу»**;
   - **«Имя переменной»**, если поле «Фильтр события по документу» = «Документ из переменной процесса»;
   - **«Фильтр события по типу документа»** или **«Фильтр события по предикатам»**, если «Тип события» = «Record создан»

  Иначе в :ref:`линтере<bpmn_linter>` будет выдана ошибка. 

Payload событий
---------------

.. _ecos_bpmn_signal_event_defaut_payload:


.. code-block:: json
    :caption: Пример payload события **Статус изменен**

    {
      "_meta": {
          "id": "0944c87d-7d4a-482f-881a-3b84ec9b740d",
          "type": "record-status-changed",
          "time": 1670576506017,
          "user": "system"
      },
      "record": "emodel/hr-person@7d2455c4-26b5-408a-913c-6affd9eb3a19",
      "recordType": "emodel/type@hr-person",
      "before": "prepare",
      "after": "fill-data"
    }

Payload по умолчанию для всех событий
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Каждое событие имеет payload по умолчанию, который содержит:

-  ``_meta`` - мета информация о событии. Содержит:

   -  ``id`` - уникальный идентификатор события (UUID)

   -  ``type`` - тип события (String)

   -  ``time`` - время возникновения события (Instant)

   -  ``user`` - username пользователя, который вызвал событие (String)
- ``record`` - документ по которому произошло событие (EntityRef)
- ``recordType`` - тип документа по которому произошло событие (EntityRef)

.. note:: 
    
   По соглашению, каждое событие должно содержать атрибут ``record`` в виде EntityRef. Если событие не содержит этого поля, то фильтрация по документу не будет работать.

Payload по умолчанию для предопределенных событий
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Record создан
_____________

Дополнительная модель отсутствует.

Record удален
_____________

Дополнительная модель отсутствует.

Record изменен
______________

- ``before`` - атрибуты до изменения (Map<String, Any>)
- ``after`` - атрибуты после изменения (Map<String, Any>)
- ``diff`` - объект описывающий изменения (`Diff <https://github.com/Citeck/ecos-events/blob/master/ecos-events2/src/main/java/ru/citeck/ecos/events2/type/RecordEventTypes.kt>`_)

  - ``list`` - список изменений (List<`DiffValue <https://github.com/Citeck/ecos-events/blob/master/ecos-events2/src/main/java/ru/citeck/ecos/events2/type/RecordEventTypes.kt>`_>), например *diff.list?json*

  - ``has`` - предоставляет возможность проверить был ли изменен атрибут (Boolean), например *diff._has.youAttName?bool*


Статус изменен
______________

.. list-table::
      :widths: 20 20
      :align: center

      * - |

            .. image:: _static/status_change_01.png
                  :width: 400
                  :align: center

        - |

            .. image:: _static/status_change_02.png
                  :width: 400
                  :align: center

**Тип изменения**:

  *	**Предыдущий** - статус до изменения;
  *	**Новый** - статус после изменения.

**Статус** выбирается из выпадающего списка. Список статусов формируется из привязанного типа данных.


Комментарий создан
__________________

- ``text`` - текст комментария (String)
- ``commentRecord`` - рекорд созданного комментария (EntityRef)

Комментарий изменен
___________________

- ``textBefore`` - текст комментария до изменения (String)
- ``textAfter`` - текст комментария после изменения (String)
- ``commentRecord`` - рекорд созданного комментария (EntityRef)

Комментарий удален
__________________

- ``text`` - текст удалленого комментария (String)
- ``commentRecord`` - рекорд удаленного комментария (EntityRef)

Пользовательское действие
__________________________

.. _user_event_bpmn:

Реализована возможность из виджета «Действия» тригерить Citeck-events.

.. note::

  Предварительно создайте действия с типом :ref:`user-event<user_event_action>`

При выборе типа  **Пользовательское действие** появляется возможность выбора действий из выпадающего списка.

.. image:: _static/user_event_01.png
      :width: 400
      :align: center

При этом работает стандартный функционал фильтрации эвентов, позволяющий фильтровать события:

.. image:: _static/user_event_02.png
      :width: 400
      :align: center

Использование payload события в Script Task
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

После возникновениия события, его payload доступен в переменной ``event`` в рамках текущей транзакции. Если необходимо сохранить какую-то информацию из payload в execution процесса, то это можно осуществить через обычное сохранение переменных в execution.

Переменная ``event``, это класс-обертка `BpmnDataValue <https://github.com/Citeck/ecos-process/blob/master/src/main/java/ru/citeck/ecos/process/domain/bpmn/engine/camunda/impl/variables/convert/BpmnDataValue.kt>`_, который позволяет удобно работать с json представлением данных - безопасно обращаться к полям, получать значения по умолчанию, приводить к нужному типу и многое другое, подробнее см. методы класса.

Пример использования payload в скрипте:

.. code-block:: javascript

    print("---HELLO FROM SCRIPT---");


    print("event id from base: " + event.get("_meta").get("id"));
    print("event id from $: " + event.get("$._meta.id"));
    print("event id from JsonPointer: " + event.get("/_meta/id"));

    print("event time as instant: " + event.get("/_meta/time").takeAsInstant());
    print("event field names list: " + event.fieldNamesList());

    print("call undefined prop is safe: " + event.get("/_meta/a/b/c/"));

    print("event id is boolean " + event.get("_meta").get("id").isBoolean());


    print("-------END--------------");

Результат выполнения скрипта:

.. code-block:: text

    ---HELLO FROM SCRIPT---
    event id from base: "5cf00981-6da6-414e-a82f-d0320f91f7a4"
    event id from $: "5cf00981-6da6-414e-a82f-d0320f91f7a4"
    event id from JsonPointer: "5cf00981-6da6-414e-a82f-d0320f91f7a4"
    event time as instant: 2022-12-09T14:17:24.027Z
    event field names list: [text, commentRecord, docDisp, myText, myText2, _meta, record, recordType]
    call undefined prop is safe: null
    event id is boolean: false
    -------END--------------

Примеры конфигураций событий
----------------------------

Start Event - старт процесса
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. _signal_start_event:

При изменении статуса по любому документу будет запущен процесс, который выполнит скрипт.

.. list-table::
      :widths: 20 20
      :align: center

      * - |

            .. image:: _static/bpmn_start_event_example.png
                  :width: 300
                  :align: center

        - |

            .. image:: _static/bpmn_start_event_form_example.png
                  :width: 300
                  :align: center

.. _start_event_subprocess:

Start Event - старт событийного подпроцесса
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Каждый раз при создании комментария по текущему документу, пока основной процесс активен, будет запущен подпроцесс, который отправит уведомление.

.. list-table::
      :widths: 20 20
      :align: center

      * - |

            .. image:: _static/bpmn_start_event_sub_process_example.png
                  :width: 300
                  :align: center

        - |

            .. image:: _static/bpmn_start_event_sub_process_form_example.png
                  :width: 300
                  :align: center

.. _Bondary_Event:

Bondary Event - событие с предикатом
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

При активной задаче, если был добавлен комментарий, который содержит текст "Галя, отмена!", то задача будет отменена и отправлено уведомление.

.. list-table::
      :widths: 20 20
      :align: center

      * - |

            .. image:: _static/bpmn_boundary_event_with_predicate_example.png
                  :width: 300
                  :align: center

        - |

            .. image:: _static/bpmn_boundary_event_with_predicate_form_example.png
                  :width: 300
                  :align: center


.. _End_Throw_Event:

End Throw Event - ручная настройка и события с фильтрами
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

При завершении подпроцесса сработает **signal end event** и будет сформировал сигнал с именем "manual-throw-signal" с фильтрацией - любой документ, тип "Найм сотрудника". При этом запустится событийный подпроцесс, так как он подходит по названию сигнала, документу и типу документа.

.. list-table::
      :widths: 20 20 20
      :align: center

      * - |

            .. image:: _static/bpmn_throw_event_with_filters_example.png
                  :width: 400
                  :align: center

        - |

            .. image:: _static/bpmn_throw_event_with_filters_throw_form_example.png
                  :width: 250
                  :align: center

        - |

            .. image:: _static/bpmn_throw_event_with_filters_start_form_example.png
                  :width: 250
                  :align: center

.. _Intermediate_Catch_Event:

Intermediate Catch Event - событие с пользовательской моделью и предикатом с expression
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Создается задача, в результате которой, пользователь определяет, комментарий с каким текстом нужно удалить, текст комментария сохраняется в переменную документа ``textForDelete``. |br|
После выполнения задачи процесс ожидается события ``Комментарий удален`` по текущему документу и предикатом, который проверяет, что текст удаленного комментария совпадает с текстом переменной ``delText``, которая определена в модели данных и ссылается на атрибут документа.

.. image:: _static/bpmn_intermediate_catch_event_with_model_expression_predicate_example.png
  :align: center
  :width: 600

Если атрибут используется только в предикате, то его можно не объявлять в модели, а использоваться напрямую, таким образом, пример выше можно упростить до:

.. code-block:: yaml

   {
    "t": "eq",
    "att": "text",
    "val": "{{record.textForDelete}}"
   }


.. |br| raw:: html

     <br>
