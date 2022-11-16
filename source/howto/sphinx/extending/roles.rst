Custom Roles
============
How to apply a special inline font style
----------------------------------------
.. role:: rbg
.. role:: gfg
.. role:: ulined

Sphinx only supports a few inline text format options such as **bold** or *italic*.
But sometimes, you need more options, such as a colored font or background or underlines.

#. Create ``_static/css/custom.css`` in your project if you haven't already.
#. Define the style you want to apply to your text for a descriptive class. For instance

    .. code-block:: css

        .rbg {
            background-color: #ff9999;
        }

        .gfg {
            color: #2eb82e;
        }

        .ulined {
            text-decoration: underline;
        }

#. Open to the \*.rst file, which should use those styles and add the references at the very top:

    .. code-block:: RST

        .. role:: rbg
        .. role:: gfg
        .. role:: ulined

    Your styles can now be applied just like the built-in cross references.

    .. important::

        If you like to have your role(s) available in every \*.rst file without
        the need for an declaration in all files, you can add the respective roles
        to the `rst_prolog`_ variable in your ``conf.py`` file, like this:

        .. code-block:: python

            rst_prolog = """
            .. role:: rbg
            .. role:: gfg
            .. role:: ulined
            """

    .. _rst_prolog: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-rst_prolog

#. Apply a style to a certain piece of text like this:

    .. code-block:: RST

        It is :ulined:`important` not to put a :rbg:`red background` on :gfg:`green text`.

    This results in the following output:

        It is :ulined:`important` not to put a :rbg:`red background` on :gfg:`green text`.

:Further sources: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html