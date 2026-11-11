.. _forms:

Формы
======

**Форма** — интерфейс для создания, просмотра и редактирования записей, работы с вложениями и выполнения задач. Поля формы связываются с атрибутами записи; их модель задаётся в :ref:`типе данных<data_types_main>`.

Формы описываются в JSON и работают на базе движка `Form.io <https://github.com/formio/formio.js>`_ с компонентами и настройками Citeck. Загрузка и сохранение данных выполняются через :ref:`Records API<Records_API>`. В разделах ниже описаны выбор формы для записи, визуальная настройка, примеры и особенности отдельных сценариев.

.. note::

   Функция :ref:`визуального конструктора форм <form_builder>` доступна только в Citeck **Enterprise**.

.. grid:: 1
   :gutter: 2

   .. grid-item-card:: Общая информация
      :link: forms_main
      :link-type: ref

      Создание и загрузка форм, привязка к типу данных или ключу, выбор разных форм для создания и редактирования записи.

   .. grid-item-card:: Конструктор форм
      :link: form_builder
      :link-type: ref

      Добавление и компоновка компонентов, привязка полей к атрибутам, валидация, условия отображения и Logic.

   .. grid-item-card:: Компоненты формы
      :link: form_components
      :link-type: ref

      Обзор компонентов, подробные инструкции и общие настройки: вычисляемые значения, ручное переопределение и значения по умолчанию.

   .. grid-item-card:: Примеры компонентов и How to
      :link: form_examples
      :link-type: ref

      Настройка полей и источников данных, иерархический выбор, управление видимостью, загрузка файлов и автосабмит.

   .. grid-item-card:: Локализация
      :link: form_localisation
      :link-type: ref

      Глобальные словари, переводы формы и атрибутов, многоязычные названия, описания и подсказки полей.

   .. grid-item-card:: Черновики
      :link: form_draft
      :link-type: ref

      Состояния draft и submitted, настройка кнопок сохранения и чтение флага черновика. Связь отправки формы с серверной обработкой.

   .. grid-item-card:: Связь формы с задачей
      :link: form_to_task
      :link-type: ref

      Ручные кнопки outcome и компонент Task Outcome, обязательный комментарий, атрибуты задачи и связанного документа.

   .. grid-item-card:: Рекомендации по проектированию
      :link: best_practice_form
      :link-type: ref

      Компоновка форм справочников, заявок и задач: колонки, панели, расположение и оформление кнопок.

.. toctree::
    :maxdepth: 20
    :hidden:

    forms/forms
    forms/form_builder
    forms/form_components
    forms/form_examples
    forms/form_localisation
    forms/form_draft
    forms/form_for_task
    forms/form_best_practice
