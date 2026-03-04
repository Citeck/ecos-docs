.. _forms:

Формы
======

**Форма** — графическое представление объекта в виде набора элементов интерфейса для манипуляции данными объекта. Элементы интерфейса ссылаются на атрибуты, заданные в :ref:`типе данных <data_types_main>`.

Формы реализованы на базе движка `formio.js <https://github.com/formio/formio.js>`_ и описываются в json-формате. Они используются для создания и редактирования записей через :ref:`Citeck Records <Records_API>`.

Функция :ref:`визуального конструктора форм <form_builder>` доступна только в Citeck **Enterprise**.

Раздел охватывает:

* :ref:`Общую информацию <forms_main>` — что такое формы, журнал форм, способы создания и загрузки
* :ref:`Конструктор форм <form_builder>` — визуальное моделирование форм: компоненты, расположение, условия видимости
* :ref:`Компоненты формы <form_components>` — описание всех доступных компонентов и их настроек
* :ref:`Примеры компонент <form_examples>` — практические how-to по использованию компонентов
* :ref:`Локализацию <form_localisation>` — настройка мультиязычных меток полей
* :ref:`Черновики <form_draft>` — сохранение записей без отправки по процессу
* :ref:`Связь формы с задачей <form_to_task>` — настройка кнопок завершения задачи (outcome)
* :ref:`Best practice <best_practice_form>` — рекомендации по проектированию форм

.. toctree::
    :maxdepth: 20

    forms/forms
    forms/form_builder
    forms/form_components
    forms/form_examples
    forms/form_localisation
    forms/form_draft
    forms/form_for_task
    forms/form_best_practice
