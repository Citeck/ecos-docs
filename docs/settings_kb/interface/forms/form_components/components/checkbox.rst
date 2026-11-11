.. _checkbox_component:

Checkbox
========

Компонент **Checkbox** позволяет пользователю выбрать логическое значение (да/нет, ``true``/``false``). Настройка ``hasThreeStates`` включает третье состояние — ``null`` (значение не задано).

`См. описание Checkbox на Form.io <https://help.form.io/userguide/forms/form-components#check-box>`_

:ref:`См. общее описание компонента Checkbox<Checkbox>`

.. contents::
   :depth: 3
   :local:

Видимость компонента: customConditional и Logic
------------------------------------------------

Checkbox поддерживает два независимых механизма управления видимостью:

* **customConditional** — JavaScript-выражение на вкладке **Conditional**. Переменной ``show`` присваивается ``true`` или ``false``, определяющее, должен ли компонент отображаться.
* **Logic** — правила на вкладке **Logic**, которые могут программно устанавливать свойство ``component.hidden``.

Оба механизма работают **независимо** и применяются совместно:

* компонент скрыт, если ``customConditional`` вернул ``false`` **или** Logic установила ``hidden = true``.
* при отсутствии запрещающих условий компонент доступен для показа с учётом общих настроек видимости формы.

Пример customConditional
~~~~~~~~~~~~~~~~~~~~~~~~~~

Скрыть Checkbox, пока поле ``status`` не равно ``"active"``:

.. code-block:: javascript

   show = data.status === 'active';

Пример совместного использования
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

На форме есть Checkbox с:

* **customConditional**: ``show = data.role === 'manager';``
* **Logic**: при событии ``change`` поля ``department`` устанавливает ``component.hidden = true``.

В этом случае Checkbox отображается только если **оба** условия разрешают показ:
компонент скрыт, когда ``data.role !== 'manager'`` **или** когда Logic установила ``hidden = true``.

Особенности реализации (для разработчиков)
-------------------------------------------

Checkbox в Citeck переопределяет метод ``updateVisible`` базового класса formiojs и вызывает функцию ``applyCheckboxVisibility``. Она не изменяет DOM в режиме редактора форм (``options.builder``) и при пустом списке ``component.logic``.

В остальных случаях вычисляется признак необходимости скрытия:

.. code-block:: javascript

   const shouldBeHidden = !!component.hidden || _visible === false;

где:

* ``component.hidden`` — свойство, которое в том числе может задаваться Logic-правилами;
* ``_visible`` — результат обработки условий видимости, включая ``customConditional`` и ``conditional``.

Строгая проверка ``=== false`` для ``_visible`` важна: она предотвращает ложное скрытие компонента,
пока formiojs ещё не инициализировал это поле. Само значение ``undefined`` не запрещает показ.

Логика работы ``updateVisible``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1
   :class: tight-table

   * - ``component.hidden``
     - ``_visible``
     - ``shouldBeHidden``
     - Примечание
   * - ``false``
     - ``true``
     - ``false``
     - Нормальное состояние
   * - ``false``
     - ``false``
     - ``true``
     - customConditional запретил показ
   * - ``true``
     - ``true``
     - ``true``
     - Logic скрыла компонент
   * - ``true``
     - ``false``
     - ``true``
     - Оба механизма скрывают
   * - ``false``
     - ``undefined``
     - ``false``
     - formiojs ещё не инициализировал _visible

DOM обновляется только при наличии ``element`` и отличии ``shouldBeHidden`` от текущего состояния атрибута ``hidden``:

* Если ``shouldBeHidden === true``, устанавливаются атрибут ``hidden``, ``visibility: hidden`` и ``position: absolute``. Эта ветка применяется и внутри Columns.
* Если ``shouldBeHidden === false`` и компонент находится в Columns с ``autoAdjust``, устанавливаются ``visibility: hidden`` и ``position: relative``. Эта ветка не снимает атрибут ``hidden``.
* В остальных случаях показа атрибут ``hidden`` снимается, устанавливаются ``visibility: visible`` и ``position: relative``.

Таким образом, таблица описывает вычисляемый признак скрытия, а не гарантирует итоговую видимость элемента во всех режимах компоновки.

Тестирование логики видимости
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Функция ``applyCheckboxVisibility`` вынесена как именованный экспорт из ``Checkbox.js``,
что позволяет тестировать её без рендеринга полного компонента:

.. code-block:: javascript

   import { applyCheckboxVisibility } from '.../Checkbox';

   const ctx = {
     options: { builder: false },
     component: { hidden: false, logic: [{}] },
     _visible: false,
     element: document.createElement('div')
   };
   applyCheckboxVisibility(ctx);
   // ctx.element.hidden === true

.. seealso::

   * :ref:`Компоненты формы — общее описание<form_components>`
   * :ref:`Columns<columns_component>` — контейнер с autoAdjust
   * :ref:`Настройки компонентов<manual_override>` — customDefaultValue, Allow Manual Override и другие настройки
