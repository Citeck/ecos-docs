Component configuration
========================

.. _manual_override:

Allow Manual Override of Calculated Value
------------------------------------------

The setting is located on the **"Data"** tab.

Using **Allow Manual Override of Calculated Value**, the field is recalculated until the user changes this value.

 .. image:: _static/calculated_value.png
       :width: 600
       :align: center

Operation description
~~~~~~~~~~~~~~~~~~~~~~

Creation mode
""""""""""""""

For **calculated value** to be set, **valueChangedByUser = false** is required (provided that **Allow Manual Override of Calculated Value** is enabled). Then in creation mode, it's sufficient to simply clear the component, and **calculatedValue** will fill it again.

Edit mode
""""""""""

In edit mode, if you clear the component, this is also considered a user edit, therefore, there is no way to get the value from **calculatedValue** again.

Field and logic description
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
      :widths: 5 10 20
      :header-rows: 1
      :class: tight-table

      * - Name
        - Default value
        - Description
      * - **calculatedValue**
        - null
        - calculated value
      * - **dataValue**
        - value from server
        - value in field
      * - **form mode**
        -
        - | set value "CREATE" by default.
          | Possible values - CREATE, EDIT
      * - **calculatedValueWasCalculated**
        -
        - | Internal flag that determines whether this is the first value calculation or not.
          | Set to true after first calculation.
      * - **valueChangedByUser**
        - false
        - Internal flag that indicates the current value (dataValue) is detached from the calculated value

Before setting **dataValue** for all fields, it is checked that no logic from the form starts calculating.

For each recalculation of **calculatedValue**:

    1. After the first calculation of **calculatedValue** (whether it's the first or not is determined by the **calculatedValueWasCalculated** flag), the **valueChangedByUser** flag value is set.
    2. **calculatedValueWasCalculated** is set to **true**
    3. If the flag **valueChangedByUser = false**, then **dataValue** is changed, otherwise no actions are performed with **dataValue**

Additional logic:

    1. If the dataValue is changed by the user, the flag **valueChangedByUser = true** is set

Example of working with TableForm component
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Task
"""""

Data should be calculated based on component 1 and placed in component 2, and after that the user should be able to modify them.

And if the user made a mistake or changed their decision, then delete data from component 2 and again through reselection in component 1 get other data and also modify them:

 .. image:: _static/calculated_value_table.png
       :width: 600
       :align: center

Implementation:
    1. Using the **allow Manual Override** flag,
    2. but instead of **calculated value**, the record retrieval logic is moved to the component's **«Logic»** section (table form)
    3. The logic is triggered by a button click event (only when the user actually wants to overwrite their values with calculated ones)

Result: overwrite works, manual data calculation launch works (on creation and edit forms). Did not work previously, before using **instance.setValue()**.

.. _custom_default_value:

Custom Default Value
---------------------

The setting is located on the **"Data"** tab.

The **customDefaultValue** property allows setting a dynamic default value using a JavaScript expression. The result is assigned to the ``value`` variable. The expression is executed when the form is initialized in creation mode.

.. note::

   The static ``defaultValue`` property is intended only for fixed values. For dynamic values (current date, current user, etc.) use ``customDefaultValue``.

Examples
~~~~~~~~~

Current date for the Date/Time component:

.. code-block:: javascript

   value = new Date();

Fixed string for a text field:

.. code-block:: javascript

   value = "default value";

Example JSON configuration of the Date/Time component with the current date:

.. code-block:: json

   {
     "key": "startDate",
     "type": "datetime",
     "input": true,
     "format": "yyyy-MM-dd",
     "enableTime": false,
     "customDefaultValue": "value = new Date();",
     "defaultValue": ""
   }

.. _current_user_by_default:

Current User by Default (selectOrgstruct)
------------------------------------------

The setting is located on the **"Custom"** tab of the **selectOrgstruct** component.

The **currentUserByDefault** property automatically substitutes the current user into the field when opening the form for creation. The setting works only in creation mode (``formMode = CREATE``) and only for the ``selectOrgstruct`` component.

Example JSON configuration:

.. code-block:: json

   {
     "key": "responsible",
     "type": "selectOrgstruct",
     "input": true,
     "allowedAuthorityType": "USER",
     "currentUserByDefault": true,
     "defaultValue": ""
   }

.. note::

   For dynamic default values in other component types, use ``customDefaultValue`` (see :ref:`Custom Default Value <custom_default_value>`).
