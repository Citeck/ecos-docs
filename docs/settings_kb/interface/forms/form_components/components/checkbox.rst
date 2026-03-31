.. _checkbox_component:

Checkbox
========

Компонент **Checkbox** позволяет пользователю выбрать одно булево значение (да/нет, true/false).

`См. описание Checkbox на Form.io <https://help.form.io/userguide/forms/form-components#check-box>`_

:ref:`См. общее описание компонента Checkbox<Checkbox>`

.. contents::
   :depth: 3
   :local:

Видимость компонента: customConditional и Logic
------------------------------------------------

Checkbox поддерживает два независимых механизма управления видимостью:

* **customConditional** — JavaScript-выражение на вкладке **Conditional**, которое вычисляется при каждом изменении данных формы. Результат (``true`` / ``false``) определяет, должен ли компонент отображаться.
* **Logic** — правила на вкладке **Logic**, которые могут программно устанавливать свойство ``component.hidden``.

Оба механизма работают **независимо** и применяются совместно:

* компонент скрыт, если ``customConditional`` вернул ``false`` **или** Logic установила ``hidden = true``.
* если ни одно из условий не задано, компонент отображается.

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

.. note::

   До версии, включающей исправление задачи **#96**, ``customConditional`` игнорировался при наличии Logic-правил.
   Убедитесь, что используете актуальную версию ecos-ui, если формы с обоими механизмами работали некорректно.

Особенности реализации (для разработчиков)
-------------------------------------------

Checkbox в Citeck переопределяет метод ``updateVisible`` базового класса formiojs.
Это необходимо для корректной работы в контейнере **Columns** с включённым ``autoAdjust``
(элемент скрывается через ``visibility: hidden`` вместо атрибута ``hidden``,
чтобы ячейка колонки не сжималась).

Видимость вычисляется как:

.. code-block:: javascript

   const shouldBeHidden = !!component.hidden || _visible === false;

где:

* ``component.hidden`` — устанавливается Logic-правилами (Pipeline 2 в formiojs).
* ``_visible`` — устанавливается ``customConditional`` / стандартной логикой ``conditional`` (Pipeline 1 в formiojs).

Строгая проверка ``=== false`` для ``_visible`` важна: она предотвращает ложное скрытие компонента,
пока formiojs ещё не инициализировал это поле (значение ``undefined`` трактуется как «видим»).

Логика работы ``updateVisible``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 1
   :class: tight-table

   * - ``component.hidden``
     - ``_visible``
     - Результат
     - Примечание
   * - ``false``
     - ``true``
     - Отображается
     - Нормальное состояние
   * - ``false``
     - ``false``
     - Скрыт
     - customConditional запретил показ
   * - ``true``
     - ``true``
     - Скрыт
     - Logic скрыла компонент
   * - ``true``
     - ``false``
     - Скрыт
     - Оба механизма скрывают
   * - ``false``
     - ``undefined``
     - Отображается
     - formiojs ещё не инициализировал _visible

При скрытии внутри **Columns** с ``autoAdjust``:

.. code-block:: javascript

   // Компонент не удаляется из DOM, только визуально скрывается:
   element.style.visibility = 'hidden';
   element.style.position = 'relative';

Это сохраняет ширину колонки, пока соседние элементы не перестроятся через ``autoAdjust``.

Тестирование логики видимости
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Функция ``applyCheckboxVisibility`` вынесена как именованный экспорт из ``Checkbox.js``,
что позволяет тестировать её без рендеринга полного компонента:

.. code-block:: javascript

   import { applyCheckboxVisibility } from '.../Checkbox';

   const ctx = {
     options: { builder: false },
     component: { hidden: false, logic: [{ ... }] },
     _visible: false,
     element: document.createElement('div')
   };
   applyCheckboxVisibility(ctx);
   // ctx.element.hidden === true

Это тот же паттерн, который используется в ``overrideTriggerChange`` (``misc.js``).

.. seealso::

   * :ref:`Компоненты формы — общее описание<form_components>`
   * :ref:`Columns<columns_component>` — контейнер с autoAdjust
   * :ref:`Настройки компонентов<manual_override>` — customDefaultValue, Allow Manual Override и другие настройки
