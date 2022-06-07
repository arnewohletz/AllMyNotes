Create selective custom style using classes
===========================================
If specific HTML elements (e.g. tables or lists) need to be styled differently
as the output theme defines, `a custom CSS file`_ (e.g. ``custom.css``) is used.
However, this will then apply to **all** these elements, not a custom selection.

To apply a certain style to a manually configurable selection of element types,
the `class`_ option can be used:

#. Create the element using the respective directive, e.g.:

    .. code-block:: rst

        .. list-table:: USS Enterprise, Private Quarters Location
            :header-rows: 1

            * - Name
              - Quarter Location
            * - Jean-Luc Picard
              - Deck 5, Cabin 1
            * - Geordi La Forge
              - Deck 4, Cabin 12

#. Add the class option to the directive, here :rst:`:class: read_bg_header`:

    .. code-block:: rst

        .. list-table:: USS Enterprise, Private Quarters Location
            :header-rows: 1
            :class: red_bg_header

#. You may build the HTML doc to easier extract the CSS path.
#. Define the style in your `custom.css` file:

    .. code-block:: css

        .red-header thead tr.row-odd {
            background-color: #e60000;
        }

#. Build the HTML doc again. The style is now applied.

.. hint::

    You may add the same class option to any other compatible element you like
    to apply this style on. All `docutil elements`_ support the **class** option,
    although some styles rules might depend on a specific element type.

.. hint::

    You can add multiple classes to one element, e.g.

    .. code-block:: rst

        .. list-table:: USS Enterprise, Private Quarters Location
            :header-rows: 1
            :class: red_bg_header, last_row_green_bg, italic_font

    It's better to add multiple classes with lesser style than a single class
    with lots of style.

.. _a custom CSS file: https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
.. _class: https://docutils.sourceforge.io/docs/ref/rst/directives.html#common-options
.. _docutil elements: https://docutils.sourceforge.io/docs/ref/doctree.html#element-hierarchy