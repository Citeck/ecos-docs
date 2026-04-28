Best practice
=============

This page contains recommendations for designing and formatting forms in the Citeck platform. Following the listed rules ensures interface consistency and improves the user experience when working with references, requests, and tasks.

.. _best_practice_form:

Reference forms, child elements (table-form)
----------------------------------------------------

 1. All form elements are placed inside a container. The form header and buttons are static, and only the fields on the form can be scrolled. Using the counterparties reference as an example:

     .. image:: _static/form_best_practice/02.png
       :width: 600
       :align: center

 2. Columns:

    * If there are 1 to 3 fields on the form, they are laid out in a single column.
    * If there are 4 or more fields on the form, all fields must be arranged in 2 columns.
    * If functional division of columns is required, panels with headers are used. Column division can be placed inside a panel, or a panel can be placed inside a column.

      .. image:: _static/form_best_practice/07.png
       :width: 600
       :align: center

|

      .. image:: _static/form_best_practice/03.png
       :width: 600
       :align: center

 3. Buttons

    * are located at the bottom of the form,
    * on the left, occupying 1/4 of the form's width, is the gray **”Cancel”** button,
    * on the right, occupying 1/4 of the form's width, is the blue **”Save”** button.
    * it is necessary to remove the large padding below the buttons at the bottom of the form.

 Example of ideal button placement and appearance:

      .. image:: _static/form_best_practice/04.png
       :width: 600
       :align: center

Request creation forms
-----------------------

 1. All form elements must be placed inside a container. The form header and buttons must be static, and only the fields on the form can be scrolled. Using the contract form as an example:

 2. All fields on the form must be arranged in 2 columns. If functional division of columns is required, panels with headers are used. Panels are also placed inside columns.

 3. Criteria for **panels**:

    * Fields in panels are grouped by meaning.
    * A panel must have a title.
    * It is necessary to optimize the placement of panels to minimize empty space, but all fields should be formatted in width and height, i.e., arranged in a tabular manner.

      .. image:: _static/form_best_practice/03.png
       :width: 600
       :align: center

 4. Buttons

    * buttons are located at the bottom of the form,
    * on the left, occupying 1/4 of the form's width, is the gray **”Cancel”** button,
    * on the right, occupying 1/4 of the form's width, is the blue **”Create”** button.
    * to the left of the **”Create”** button, occupying 1/4 of the form's width, is the gray **”Save”** button.
    * it is necessary to remove the large padding below the buttons at the bottom of the form.

Example of button placement and appearance:

      .. image:: _static/form_best_practice/05.png
       :width: 600
       :align: center

 Usually, the task form contains a “Comment” field and approval buttons. Depending on the process requirements, the content may vary.

Task forms
-------------

.. _best_practice_task_form:

Button requirements:

    1. All buttons are aligned to the left edge of the form.
    2. Buttons with a negative resolution (gray color) are placed first.
    3. Buttons with a positive resolution (blue color) are placed on the right edge.
    4. If required, buttons with a neutral resolution (gray color) are placed between the negative and positive resolution buttons.

Example of a task form:

      .. image:: _static/form_best_practice/06.png
       :width: 600
       :align: center

Using the Citeck.helpers.getMLValue(nameObj) function
---------------------------------------------------------

The ``Citeck.helpers.getMLValue(nameObj)`` function accepts a parameter - an object with keys that match the keys of existing localizations and values - the names in those localizations.

      .. image:: _static/form_best_practice/getMLValue_01.png
       :width: 600
       :align: center

.. code-block::

    var statuses  = _.get(data, “stats.statuses”);
    var arr = [];

    for(var i = 0; i < statuses.length; i++) {
    var val = { value: statuses[i].id, label: Citeck.helpers.getMLValue(statuses[i].name) };
    arr.push(val);
    }

    values = arr;

**Implementation example:**

When Russian language is selected in the system – statuses are displayed in Russian:

      .. image:: _static/form_best_practice/getMLValue_02.png
       :width: 600
       :align: center

When English language is selected in the system – statuses are displayed in English:

      .. image:: _static/form_best_practice/getMLValue_03.png
       :width: 600
       :align: center

Using the main form submission function
---------------------------------------------------------

In any component, it is possible to trigger the submission of the main (parent) form immediately after some action in the child form by handling the ``instance.on('change')`` event.

      .. image:: _static/form_best_practice/submitForm_01.png
       :width: 600
       :align: center

.. code-block::

    instance.on('change' , function(event) {
    if (event.changed && event.changed.value) {
    instance.root.submit()
    }
    });

When using ``instance.root.submit()``, it is possible to specify two optional parameters:

    1. If you need to perform validation or prepare data before submission, you can define a callback function as the first argument, which will perform the necessary actions.

    2. As the second argument, you can also pass options if they are needed for the callback function. Options are passed as an object.
