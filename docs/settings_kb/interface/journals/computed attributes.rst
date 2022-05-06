Вычисляемые атрибуты (computed attributes)
==========================================

Вычисляемые атрибуты могут быть описаны в области журнала или конкретной колонки:

.. code-block::

    "computed": [
		{
		  "id": "someAttribute",
		  "type": "script",
		  "config": {
			"script": "return \"abcd\";"  
		  }
		}
	]

Есть 2 основных вида вычисляемых атрибутов: **Record** и **Config**. 

**Record Computed Attributes (R атрибуты)** - атрибуты, которые вычисляются для каждой записи;

**Config Computed Attributes (C атрибуты)** - атрибуты, которые вычисляются глобально для конфига;

Для обращения к атрибутам из записи в конфиге можно использовать плейсхолдеры ${…}. Например:

.. code-block::

    "computed": [
		{
		  "id": "someAttribute",
		  "type": "script",
		  "config": {
			"vars": {
			  "documentDisplayName": "${?disp}"
			}
			"script": "return \"abcd\" + vars.documentDisplayName;"  
		  }
		}
	]

При наличии в конфиге плейсхолдеров ``${…}`` атрибут автоматически становится R атрибутом.

Использование computed атрибутов доступно в полях колонки **formatter** и **editor**. Доступ аналогичен доступу к атрибутам записи, но с префиксом ``“$computed”``. Например:

.. code-block::

    "formatter": {
	  "type": "value",
	  "config": {
		"value": "${$computed.someAttribute}"
	  }
	}
	"computed": [
		{
		  "id": "someAttribute",
		  "type": "script",
		  "config": {
			"vars": {
			  "documentDisplayName": "${?disp}"
			}
			"script": "return \"abcd\" + vars.documentDisplayName;"  
		  }
		}
	]

Типы вычисляемых атрибутов
---------------------------

.. list-table:: 
      :widths: 5 40 5
      :header-rows: 1

      * - Тип
        - Конфиг
        - Примечание
      * - **script**
        - | ``vars:  Object<String, Any>`` - переменные, которые будут доступны в скрипте
          | ``script: String`` - текст скрипта
        - | В контексте скрипта доступны:
          | **Records** - то же самое что и Citeck.Records
          | **_** - lodash библиотека
          | **vars** - переменные из конфига
          | **t** - функция для получения локализованного сообщения по ключу
      * - **value**
        - | ``value: Any`` - значение
          | Может быть выбрано несколько значений.
        - 
