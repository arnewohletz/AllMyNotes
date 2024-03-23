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

How to apply a custom role containing raw HTML
----------------------------------------------
Sometimes a special HTML content is needed to achieve the correct formatting in
the HTML output.

For instance, the `csv-table`_ does not feature line breaks within cells, but a
raw HTML substitution can add this feature.

#. Open the ``conf.py`` file and create an `rst_prolog`_ variable, if not already
   existing.
#. Add the following content:

    .. code-block:: python
        :linenos:

        rst_prolog="""
        .. |br| raw:: html

            <br />
        """

    This makes the substitution available on every RST file within the documentation.

    .. attention::

        The empty **line 3** between the raw directive and its content (``<br />``)
        is needed by Sphinx to differentiate between the directive's option (even
        though `raw`_ does not allow any) and its content.

#. Add the ``|br|`` to the CSV file referenced by the :rst:`.. csv-table::` directive
   or into the directive content directly. For example

    .. code-block:: rst

        .. csv-table:: Open Days

            Week 1, Monday |br| Tuesday |br| Wednesday
            Week 2, Monday |br| Thursday |br| Friday

   renders into

    .. csv-table:: Open Days

        Week 1, Monday |br| Tuesday |br| Wednesday
        Week 2, Monday |br| Thursday |br| Friday


.. _csv-table: https://docutils.sourceforge.io/docs/ref/rst/directives.html#csv-table-1
.. _raw: https://docutils.sourceforge.io/docs/ref/rst/directives.html#raw-data-pass-through
