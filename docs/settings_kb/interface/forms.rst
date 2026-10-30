.. _forms:

Формы
======

**Форма** — графическое представление объекта в виде набора элементов интерфейса для манипуляции данными объекта. Элементы интерфейса ссылаются на атрибуты, заданные в :ref:`типе данных <data_types_main>`.

Формы реализованы на базе движка `formio.js <https://github.com/formio/formio.js>`_ и описываются в json-формате. Они используются для создания и редактирования записей через :ref:`Citeck Records <Records_API>`.

.. note::

   Функция :ref:`визуального конструктора форм <form_builder>` доступна только в Citeck **Enterprise**.

.. grid:: 1
   :gutter: 2

   .. grid-item-card:: Общая информация
      :link: forms_main
      :link-type: ref

      Что такое формы, журнал форм, способы создания и загрузки.

   .. grid-item-card:: Конструктор форм
      :link: form_builder
      :link-type: ref

      Визуальное моделирование форм: компоненты, расположение, условия видимости.

   .. grid-item-card:: Компоненты формы
      :link: form_components
      :link-type: ref

      Описание всех доступных компонентов и их настроек.

   .. grid-item-card:: Примеры компонент
      :link: form_examples
      :link-type: ref

      Практические how-to по использованию компонентов.

   .. grid-item-card:: Локализация
      :link: form_localisation
      :link-type: ref

      Настройка мультиязычных меток полей.

   .. grid-item-card:: Черновики
      :link: form_draft
      :link-type: ref

      Сохранение записей без отправки по процессу.

   .. grid-item-card:: Связь формы с задачей
      :link: form_to_task
      :link-type: ref

      Настройка кнопок завершения задачи (outcome).

   .. grid-item-card:: Best practice
      :link: best_practice_form
      :link-type: ref

      Рекомендации по проектированию форм.

.. toctree::
    :maxdepth: 20
    :hidden:

    forms/forms
    forms/form_builder
    forms/form_components
    forms/form_examples
    forms/form_localisation
    forms/form_best_practice
    forms/form_draft
    forms/form_for_task
