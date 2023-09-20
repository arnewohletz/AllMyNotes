Create selective custom style using classes
===========================================
If specific HTML elements (e.g. tables or lists) need to be styled differently
as the output theme defines, `a custom CSS file`_ (e.g. ``custom.css``) is used.
However, this will then apply to **all** these elements, not a custom selection.

To apply a certain style to a manually configurable selection of element types,
the `class`_ option can be used.

.. _a custom CSS file: https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
.. _class: https://docutils.sourceforge.io/docs/ref/rst/directives.html#common-options

Example: Custom table
---------------------
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

#. Add the class option to the directive, here :rst:`:class: red_header`:

    .. code-block:: rst

        .. list-table:: USS Enterprise, Private Quarters Location
            :header-rows: 1
            :class: red_header

#. You may build the HTML doc to easier extract the CSS path. You will see that
   the element has the specified name among its class attributes (e.g.
   :html:`class="red-header docutils align-default"`).
#. Define the style in your `custom.css` file, for example:

    .. code-block:: css

        .red-header thead tr.row-odd {
            background-color: #e60000;
        }

#. Build the HTML doc again. The style is now applied. In our example, the styled
   variant will render as

    .. list-table:: USS Enterprise, Private Quarters Location
        :header-rows: 1
        :class: red-header

        * - Name
          - Quarter Location
        * - Jean-Luc Picard
          - Deck 5, Cabin 1
        * - Geordi La Forge
          - Deck 4, Cabin 12

    whereas the un-styled tables renders as

    .. list-table:: USS Enterprise, Private Quarters Location
        :header-rows: 1

        * - Name
          - Quarter Location
        * - Jean-Luc Picard
          - Deck 5, Cabin 1
        * - Geordi La Forge
          - Deck 4, Cabin 12

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

.. _docutil elements: https://docutils.sourceforge.io/docs/ref/doctree.html#element-hierarchy

Appendix: Custom admonition
---------------------------
Docutils features `several admonitions`_. But it might become necessary to create additional
ones, since none of the existing fit or a different style is needed for better understanding.

The steps are explained via an example, which demonstrates the creation of admonition for a
*Problem definition* (for example used within a troubleshooting section).

#. Define the admonition:

    .. code-block:: rst

        .. admonition:: Problem
            :class: problem

            Some content for the custom problem admonition which is not important here.

    This translates to the following HTML:

    .. code-block:: html

        <div class="problem admonition">
          <p class="admonition-title">Problem</p>
          <p>
            ::before
            Some content for the custom problem admonition which is not important here
          </p>
        </div>

#. Define the style for the custom admonition in the `custom.css`_ file, for our example
   (defining a red title background):

    .. code-block:: css

        .rst-content .problem .admonition-title {
            background: #ff9999;
        }

#. Define a custom symbol for the admonition. The default symbol, if any, is defined by the
   used HTML theme (default in sphinx-rtd-theme: exclamation mark). As `sphinx-rtd-theme`_
   supports FontAwesome symbols, any freely available icon from https://fontawesome.com/icons can be used.

    #. Visit https://fontawesome.com/icons and find a suitable icon (make sure the **Free**
       filter is selected).
    #. Select the chosen icon and select :unicode-guilabel:`&#128276;` (Copy Glyph) to
       copy its glyph representation.
    #. Add an additional CSS rule to ``custom.css``, in our example:

        .. code-block:: css

            .rst-content .problem .admonition-title::before {
                content: "";
            }

    #. Put the copied glyph (here: triangle-exclamation) into the *content* attribute
       between the quotes.

        .. important::

            It is possible, that the used editor is not able to display the characters
            and enters a simple square (for example |replacement_character_A| or |replacement_character_B|)
            as a replacement character. That does **not** mean, the browser won't be able to display it.

    .. important::

        **Apply Unicode symbol (for other sphinx themes)**

        Not every theme supports FontAwesome symbols, but can still display any Unicode
        symbol.

        #. Visit https://symbl.cc/en/ and search for a suitable symbol.
        #. Copy the *CSS Code* of the symbol (for example ``\2615``).
        #. Add a new CSS rule to ``custom.css``, in this example:

            .. code-block:: css

                .rst-content .problem .admonition-title::before {
                    content: "";
                }

          and add the copied CSS code between the quotes, for example:

            .. code-block:: css

                content: "\2625"


#. Build the HTML documentation. The admonition defined in step 1 should render to

    .. admonition:: Problem
        :class: problem

            Some content for the custom problem admonition which is not important here.


.. |replacement_character_A| unicode:: U+FFFD
.. |replacement_character_B| unicode:: U+F071

.. _several admonitions: https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions
.. _custom.css: https://docs.readthedocs.io/en/stable/guides/adding-custom-css.html
.. _sphinx-rtd-theme: https://pypi.org/project/sphinx-rtd-theme/
