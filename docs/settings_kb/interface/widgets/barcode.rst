.. _widget_barcode:

Виджет «Штрих-код»
===================

Ключ ``barcode``

Виджет отображает сгенерированный штрих-код документа, основанный на числовом поле документа.

По умолчанию используется поле ``barcode``.

Если нужно другое поле, то следует зарегистрировать это поле по типу данных в бине ``core.barcode-attribute.type-to-property.mappingRegistry``
Пример:

.. code-block:: xml

    <bean id="records.contracts.barcode-attribute.type-to-property.mapping"
        class="ru.citeck.ecos.spring.registry.MappingRegistrar">
        <constructor-arg ref="core.barcode-attribute.type-to-property.mappingRegistry"/>
        <property name="mapping">
            <map>
                <entry key="contracts-cat-doctype-contract" value="contracts:barcode"/>
            </map>
        </property>
    </bean>

.. list-table::
      :widths: 5 40
      :class: tight-table

      * - | **Настройка**


        - |

            .. image:: ../_static/widgets/barcode_1.png
                 :width: 250
                 :align: center

          | Условие отображения кнопки:
          | Если отсутствует условие, то кнопка отображается. Иначе для отображения, API по заданному условию должно возвращать **true**.
          | В текущей версии сохраняется как json строка.
          | Написание условия в соответствии статье :ref:`Язык предикатов <ecos-predicate_main>`

      * - | **Настроенный вид**


        - |  Для типа дашборда Case-details

            .. image:: ../_static/widgets/barcode_2.png
                 :width: 250
                 :align: center
