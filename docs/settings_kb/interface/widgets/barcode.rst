.. _widget_barcode:

'Barcode' Widget
================

Key ``barcode``

The widget displays a generated barcode for the document, based on a numeric field of the document.

The ``barcode`` field is used by default.

If a different field is needed, register it by data type in the bean ``core.barcode-attribute.type-to-property.mappingRegistry``.
Example:

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

      * - | **Settings**


        - |

            .. image:: ../_static/widgets/barcode_1.png
                 :width: 250
                 :align: center

          | Button display condition:
          | If no condition is set, the button is displayed. Otherwise, the API must return **true** for the given condition in order for the button to be shown.
          | In the current version, it is saved as a JSON string.
          | Write the condition in accordance with the :ref:`Predicate Language <ecos-predicate_main>` article.

      * - | **Configured view**


        - |  For the Case-details dashboard type

            .. image:: ../_static/widgets/barcode_2.png
                 :width: 250
                 :align: center
