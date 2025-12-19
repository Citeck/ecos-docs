Примеры запросов Citeck Records
=================================

Пример работы с рекордами из javascript
---------------------------------------

Добавление пользователя или группы в группу
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    let rec = Records.get('emodel/person@someuser'); // пользователь или группа, которого(ую) нужно добавить в группу
    rec.att('att_add_authorityGroups', 'emodel/authority-group@accountant'); // группа, в которую нужно добавить
    rec.save();

Удаление пользователя или группы из группы
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    let rec = Records.get('emodel/person@someuser'); // пользователь или группа, которого(ую) нужно удалить из группы
    rec.att('att_rem_authorityGroups', 'emodel/authority-group@accountant'); // группа, из которой нужно удалить
    rec.save();

Проверка вхождения пользователя или группы в группу
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Проверка вхождения текущего пользователя в группу:

.. code-block:: javascript

    await Citeck.Records.get('emodel/person@CURRENT').load('authorities._has.GROUP_ECOS_ADMINISTRATORS?bool!')

Проверка вхождения конкретного пользователя в группу:

.. code-block:: javascript
  
  await Citeck.Records.get('emodel/person@someuser').load('authorities._has.GROUP_testers?bool!')

Проверка вхождения группы в группу пока не поддерживается.

Получения списка assignee (authority, реципиентов) из роли документа
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    await Citeck.Records.get('emodel/sd-request-type@you-doc').load('_roles.assigneesOf.impl-first-line-role[]?str', true)

Поиск записей и их изменение в цикле
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    var typeId = 'deal';

    var typeRef = "emodel/type@" + typeId;

    var sourceId = await Records.get(typeRef).load('sourceId');
    var queryResult = await Records.query({
        sourceId,
        query: { t: 'eq', att: '_type', val: typeRef },
        language: 'predicate',
        page: { maxItems: 4000 }
    });
    var records = queryResult.records;

    console.log("Found " + records.length);

    var newStatus = 'old';
    for (let i = 0; i < records.length; i++) {
        let record = Records.get(records[i]);
        let currentStatus = await record.load('_status?str', true);
        if (currentStatus == 'new') {
            console.log('change status for ' + record.id + " from " + currentStatus + " to " + newStatus);
            record.att('_status', newStatus);
            await record.save();
        }
    }

Здесь скрипт ищет объекты (max = 4000) с типом данным **deal** и статусом new, и меняет статус на **old** (такие статусы должны быть заданы для типа deal).

Получение значения из конфига (ecos config)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    Citeck.Records.get('eapps/meta@').load('$cfg.service-desk-groups')
    // либо
    Citeck.Records.get('eapps/cfg@service-desk-groups').load('value')
    
Скоуп нужен если цель - вытащить из одного микросервиса конфиг, который определен в другом микросервисе

Получения разных локализованный значения у атрибута Статус (_status)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    await Citeck.Records.get('emodel/ecos-contract@you-doc').load('_status._disp?json', true)

Ответ:

.. code-block:: json

    {
        "ru": "Новый",
        "en": "New"
    }
    
Либо можно получить значение на конкретном языке:

.. code-block:: javascript

    await Citeck.Records.get('emodel/ecos-contract@you-doc').load('_status._disp.en', true)

Проверка, существует ли конкретный record
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    await Citeck.Records.get('emodel/ecos-contract@you-doc').load('_notExists?bool!', true)


Проверить, что record это подтип определенного типа
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    await Citeck.Records.get('emodel/ecos-contract@you-doc').load('_type.isSubTypeOf.case?bool!', true)


Проверка прав доступа к записи
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript
  
    // Проверка права на чтение
    await Citeck.Records.get('emodel/ecos-contract@you-doc').load('permissions._has.Read?bool!', true)
    
    // Проверка права на запись
    await Citeck.Records.get('emodel/ecos-contract@you-doc').load('permissions._has.Write?bool!', true)
    
    // Проверка кастомного права
    await Citeck.Records.get('emodel/ecos-contract@you-doc').load('permissions._has.bpmn-process-instance-read?bool!', true)

Проверка связи между микросервисами, notifications -> eproc -> uiserv
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    await Citeck.Records.get('notifications/meta@').load('rec.eproc/meta@.rec.uiserv/meta@.time', true)


Получение атрибутов напрямую через ассоциацию
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

У объекта контракт, получаем контрагента и у него ИНН, дату создания и отображаемое имя:

.. code-block:: javascript

    await Citeck.Records.get('emodel/ecos-contract@you-doc').load('counterparty{?disp,inn,_created}', true)

Пример ответа:

.. code-block:: json

    {
        "?disp": "ООО Стальпром",
        "inn": "111111111111",
        "_created": "2023-08-03T09:28:49.071Z"
    }



Если ассоциация множественная, то можно получить атрибуты всех объектов:

.. code-block:: javascript

    await Citeck.Records.get('emodel/ecos-contract@you-doc').load('payments[]{plannedPaymentDate,amount?num}', true)

Пример ответа:

.. code-block:: json

    [
        {
            "plannedPaymentDate": "2025-02-10T00:00:00Z",
            "amount": 1000
        },
        {
            "plannedPaymentDate": "2025-02-20T00:00:00Z",
            "amount": 10500
        }
    ]


Если ассоциация множественная и нужно получить атрибуты только первого объекта:

.. code-block:: javascript
  
  await Citeck.Records.get('emodel/ecos-contract@you-doc').load('payments{plannedPaymentDate,amount?num}', true)
  
Пример ответа:

.. code-block:: json

  {
    "plannedPaymentDate": "2025-02-10T00:00:00Z",
    "amount": 1000
  }

Получение нескольких атрибутов вместе c вложенными атрибутами
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Получить несколько атрибутов вместе с атрибутами из ассоциации:

.. code-block:: javascript

    await Citeck.Records.get('emodel/ecos-contract@you-doc').load(['?disp', 'payments[]{plannedPaymentDate,amount?num}'], true)
    
Пример ответа:

.. code-block:: json

  {
    "?disp": "Договор №16808",
    "payments[]{plannedPaymentDate,amount?num}": [
      {
        "plannedPaymentDate": "2025-02-10T00:00:00Z",
        "amount": 1000
      },
      {
        "plannedPaymentDate": "2025-02-20T00:00:00Z",
        "amount": 10500
      }
    ]
  }

Так же можно задать имена получаемых атрибутов:

.. code-block:: javascript

    await Citeck.Records.get('emodel/ecos-contract@you-doc').load({'contractName': '?disp', 'payments': 'payments[]{plannedPaymentDate,amount?num}'}, true)

Пример ответа:

.. code-block:: json

  {
    "contractName": "Договор №16808",
    "payments": [
      {
        "plannedPaymentDate": "2025-02-10T00:00:00Z",
        "amount": 1000
      },
      {
        "plannedPaymentDate": "2025-02-20T00:00:00Z",
        "amount": 10500
      }
    ]
  }


Получать вложенные атрибуты можно не только у ассоциаций, но и у всех атрибутов, которые представляют собой объекты, например, у атрибута **_content**:

.. code-block:: javascript

    await Citeck.Records.get('emodel/ecos-contract@you-doc').load({'name': '?disp', 'content': '_content{size,mimeType}'}, true)
    
Пример ответа:

.. code-block:: json

  {
    "name": "Договор №16808",
    "content": {
      "size": "248446",
      "mimeType": "application/pdf"
    }
  }



Работа с файлами
~~~~~~~~~~~~~~~~

Работа с файлами из UI возможна либо через загрузку контента в виде  base64 строки, либо получения ссылки для скачивания. |br|
Скрипт получает контент файла в виде base64 строки из атрибута **_content**:

.. code-block:: javascript

    await Records.get('emodel/ecos-contract@3a4e11cf-4227-44f4-98dd-1eeefba30e28').load('_content.bytes')

Скрипт получает ссылку для скачивания файла из атрибута **_content**:

.. code-block:: javascript

    await Records.get('emodel/ecos-contract@3a4e11cf-4227-44f4-98dd-1eeefba30e28').load('_content.url')

Можно загрузить файл в виде **formData** по адресу:

.. code-block::

    /gateway/emodel/api/ecos/webapp/content 

или через base64 (подходит только для небольших файлов). 


Старт бизнес-процесса для документа
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: javascript

    let rec = Records.get('eproc/bpmn-proc@process_different_1'); // id процесса
    rec.att('action', 'START');
    rec.att('document', 'emodel/contract@0b54aed0-d288-4d29-aec3-c1ff37cfa089'); // Документ, для которого стартуем процесс
    rec.save();


.. |br| raw:: html

     <br>
