.. role:: python(code)
    :language: python
    :class: highlight

Inline Code Highlighting
========================
By default, Sphinx does utilize Pygments to highlight code snippets, when used
in the *code-block* directive.

For very small snippets, code can also be written inline, utilizing syntax the
same syntax highlighting as in regular code blocks, like here:

Printing to console in Python is easy as :python:`print("Hello World")`.

Follow these steps:

#. Within root directory (where ``conf.py`` is located) create a new file named
   ``docutils.conf``. Add this content:


    .. code-block:: ini

        [restructuredtext parser]
        syntax_highlight = short

#. In the ``conf.py`` define the Pygment theme used for the syntax highlighting, e.g.:

    .. code-block:: python

        pygments_style = "default"

    .. hint::

        To get a list of all available themes, execute:

        .. code-block:: python

            >>> from pygments.styles import get_all_styles
            >>> print(*get_all_styles(), sep = "\n")

        You may preview the styles at https://pygments.org/demo/.

#. When using `sphinx-rtd-theme <https://github.com/readthedocs/sphinx_rtd_theme>`__
   the default color for inline code snippets is set to red (color code #e74c3c).
   This leads to all elements whose color is not defined by the Pygments style to
   stay red, when in fact it should be black.

   To overcome this, add the following snippet to your ``_static/css/custom.css``
   file:

        .. code-block:: css

            code.code.highlight span.p {
                color: black;
            }

#. Define a new role within the file that you want to use inline code syntax
   highlighting with (e.g. on the very top of the document). Here is an example
   for python:

    .. code-block:: rst

        .. role:: python
            :language: python
            :class: highlight

    .. hint::

        You may define roles for all `supported languages <https://pygments.org/languages/>`__.

#. Use the role to add code snippets into your text, e.g.:

    .. code-block:: rst

        Printing to console in Python is easy as :python:`print("Hello World")`.

    which will output to:

        Printing to console in Python is easy as :python:`print("Hello World")`.

