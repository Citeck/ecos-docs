Поиск по вложенным атрибутам ассоциации в журналах
===================================================

При настройке журналов есть возможность искать по вложенным атрибутам ассоциаций в журналах.

Пример - с конфигурацией ниже мы пытаемся найти договоры, у которых у юр лица **ИНН** начинается на строку **“123456“**. Что сделает ECOS:

Обнаружит, что в виде поискового значения по ассоциации ему пришел не ``nodeRef``.

Выполнит поиск записей юр лиц по атрибутам, которые указаны в типе в модели Alfresco. Если указаны конкретные поля - поиск будет по ним.

``NodeRef``'ы найденных на шаге 2 записей - добавит в запрос для поиска по ассоциации.

Таким образом, получится искать в журналах по вложенным атрибутам.

Ограничение - шаг 2 сейчас ищет только 20 записей.

1) Пример настройки столбца с атрибутом в журнале:

.. code-block::

    	  - id: contracts:agreementLegalEntity
		name:
		  ru: Юридическое лицо (ИНН)
		  en: Legal entity (INN)
		type: TEXT
		sortable: false
		editable: false
		formatter:
		  type: script
		  config:
			vars:
			  idocs_inn: ${contracts:agreementLegalEntity.idocs:inn}
			fn: >
			  return vars.idocs_inn;

Данная конфигурация отображает **ИНН юр лица** вместо **.disp**.

2) Пример указания конкретного поля для поиска:

.. code-block::

    		<bean class="ru.citeck.ecos.records.language.predicate.converters.AssocToCustomSearchFieldsConfig">
			<property name="assocQName" value="{http://www.citeck.ru/model/contracts/1.0}agreementLegalEntity"/>
			<property name="customSearchFields">
				<list>
					<value>{http://www.citeck.ru/model/content/idocs/1.0}inn</value>
				</list>
			</property>
		</bean>

После регистрации данного бина - поиск по вложенным атрибутам будет учитывать только атрибут **ИНН**.
