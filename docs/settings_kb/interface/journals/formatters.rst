.. _formatters:

Форматтеры
===========

.. contents:: Содержание
   :depth: 3

Настройки
---------

Перейти в раздел администрирования > :guilabel:`Журналы` > найти необходимый журнал > действие :guilabel:`Редактировать`. Перейти в :guilabel:`Дополнительно`

.. list-table:: 
      :widths: 40
      :align: center

      * - |

             .. image:: _static/formatter/formatter_1.png
                 :width: 500   
                 :align: center

          | 

             .. image:: _static/formatter/formatter_2.png
                  :width: 500 
                  :align: center  


.. important::

    Если форматер не указан в списке ниже вероятно он еще не мигрировал или ассоциируется с другим новым

Типы
---------

AssocFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``assoc``

ActionFormatter
~~~~~~~~~~~~~~~~~~

Тип : ``action``

.. list-table:: 
      :widths: 5 40
      :header-rows: 1

      * - Ключ
        - Значение
      * - **type**
        - <id типа действия>
      * - *другие*
        - параметры необходимые для выполнения действия

Предполагается в строке журнала наличие **id** или **recordRef** - ref записи, необходимый для выполнения действия

BooleanFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``bool``

ColoredFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``colored``

DateFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``date``

DateTimeFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``datetime``

DefaultFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``default``

FileNameFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``filename``

HtmlFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``html``

LinkFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``link``

NumberFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``Number``

Пример:

.. code-block::

  mask: {value} руб.
  locales: ru
  maximumFractionDigits: 16
  decimalSeparator: .
  thousandSeparator: ,

Конфигурация:

.. list-table:: 
      :widths: 5 40
      :header-rows: 1

      * - Ключ
        - Описание
      * - **mask**
        - маска, где ``{value}`` — само число
      * - **locales**
        - | какую локаль для форматирования использовать. 
          | От нее зависит как будут разделяться тысячи и дробные числа. (Точкой, запятой или пробелом) По умолчанию текущая локаль.
      * - **maximumFractionDigits**
        - сколько чисел после запятой
      * - **decimalSeparator**
        - как отделяются дробные числа. По умолчанию зависит от локали
      * - **thousandSeparator**
        - как разделяются тысячи. По умолчанию зависит от локали.


ScriptFormatter
~~~~~~~~~~~~~~~~~~

Тип: ``script``

Конфигурация:

.. list-table:: 
      :widths: 5 40
      :header-rows: 1

      * - Ключ
        - Значение
      * - **fn**
        - | формат ``function``
          | в функцию передаются параметры fn(p1, p2, p3, p4, p5, p6, p7)
          | **p1** - Records
          | **p2** - _ lodash
          | **p3** - t
          | **p4** - vars - переменные из конфигурации
          | **p5** - cell - ячейка
          | **p6** - row - строка
          | **p7** - index -строка
          |
          | формат ``string (eval)``
          | в конфигурацию передается тело функции
      * - **vars**
        - | формат ``Object``
          | Дополнительные переменные, функции и т.п., что может пригодиться при исполнении функции. Пробрасывается в **p4** (объект со вспомогательными функциями и переменными)

Пример использования:

.. code-block::

    {
	  type: 'script',
	  config: {
		fn: function(cell, rec, col, data, rowIndex, utils) {
		  return data ? data.replace(":", "_") : null;
		}
	  }
	}

Если есть необходимость вызвать другой форматтер, например **LinkFormatter**:

.. code-block::

    {
	  type: 'script',
	  config: {
		fn: function(cell, rec, col, data, rowIndex, utils) {
		  const type = data ? data.replace(":", "_") : null;
		  
		  return {
			row: data,
			cell: utils.lodash.get(window, ['Citeck.messages.global', `property.samwf_caseType.${type}.title`], cell),
			type: 'link'
		  };
		}
	  }
	}

 ! В форматер передается функция **t** - для локализации значений, которая не работает на формах, т.к. у нее свой словарь; внутри компонента формы следует использовать функцию формы ``instance.i18next.t``

WorkflowPriorityFormatter
~~~~~~~~~~~~~~~~~~~~~~~~~~

Тип: ``workflowPriority``  
