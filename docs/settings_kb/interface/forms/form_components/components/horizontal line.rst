.. _horizontal_line:

Horizontal line
===============

**Horizontal Line** - компонент для отображения разделителя блоков. В конструкторе форм располагается в блоке :guilabel:`Layout`.

 .. image:: _static/horizontal_line/horizontal_line_1.png
       :width: 300
       :align: center

Для добавления вертикальных отступов предусмотрена опция **Add vertical indents**.

Так как формы в основном отображаются в модальных окнах, а модальные окна имеют отступ, было решено добавить опцию **Use negative indents** (включена по-умолчанию), которая позволяет увеличить ширину разделителя до границ модального окна.

 .. image:: _static/horizontal_line/horizontal_line_2.png
       :width: 500
       :align: center

Чтобы отображать компонент разделителя только в режиме просмотра, требуется установить следующее условие **Advanced Conditions** на вкладке :guilabel:`Conditional`:

.. code-block::

    show = instance.options.readOnly && instance.options.viewAsHtml

