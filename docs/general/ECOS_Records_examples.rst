Примеры запросов ECOS Records
==============================

Оргструктура
-------------

Cоздание пользователя
~~~~~~~~~~~~~~~~~~~~~


Добавление в группу
~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    let rec = Records.get('emodel/person@admin'); // пользователь или группа, которого(ую) нужно добавить в группу
    rec.att('att_add_authorityGroups', 'emodel/authority-group@accountant'); // группа в которую нужно добавить
    rec.save();

Удаление из группы
~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    let rec = Records.get('emodel/person@admin'); // пользователь или группа, которого(ую) нужно удалить из группы
    rec.att('att_rem_authorityGroups', 'emodel/authority-group@accountant'); // группа из которой нужно удалить
    rec.save();

Полное удаление из системы
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block::

    Records.remove('emodel/person@admin'); // пользователь или группа, которого(ую) нужно удалить из системы

Пример работы с рекордами их javascript
---------------------------------------

Можно вызвать в консоле разработчиков в браузере. 

Скрипт меняет статус для всех объектов с типом данных deal и статусом new на old (такие статусы должны быть заданы для типа deal).

.. code-block::

    var typeId = 'deal';

    var typeRef = "emodel/type@" + typeId;

    var sourceId = await Citeck.Records.get(typeRef).load('sourceId');
    var queryResult = await Citeck.Records.query({
        sourceId,
        query: { t: 'eq', att: '_type', val: typeRef },
        language: 'predicate',
        page: { maxItems: 4000 }
    });
    var records = queryResult.records;

    console.log("Found " + records.length);

    var newStatus = 'old';
    for (let i = 0; i < records.length; i++) {
        let record = Citeck.Records.get(records[i]);
        let currentStatus = await record.load('_status?str', true);
        if (currentStatus == 'new') {
            console.log('change status for ' + record.id + " from " + currentStatus + " to " + newStatus);
            record.att('_status', newStatus);
            await record.save();
        }
    }


Формы
-----

Поиск формы
~~~~~~~~~~~

Журналы
--------

