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

Формы
-----

Поиск формы
~~~~~~~~~~~

Журналы
--------

