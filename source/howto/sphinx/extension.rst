Create extension (custom role) :footcite:p:`sphinx_role_extension_doug` :footcite:p:`sphinx_role_extension_thai`
================================================================================================================
In some cases, there is no adequate role available for your purpose, for instance,
when nesting two roles. In such cases, adding an extension to your Sphinx project
can overcome this limitation.

In this example case, the `guilabel`_ role will be extended to support displaying
a single unicode character, like a symbol, to describe buttons or GUI item which show
such symbols instead of regular text.

Create a new Python module in a proper location (e.g. ``./source/_ext/``).

First off, we need to register our role in our Sphinx application:

.. code-block:: python

    def setup(app):
        app.add_role("unicode-guilabel", unicode_guilabel_role)

Here, we are adding the role *unicode-guilabel* and assign it to the function *unicode_guilabel_role*.

Next, we need to define this role processor function. The docutils parser used by Sphinx converts the input
text into tree, made up of different types of nodes. That tree is then parsed by a *writer*
which creates the desired output format, hence your role processor function must return such a node,
taking arguments describing the marked-up text:


.. code-block:: python

    from docutils import nodes

    def unicode_guilabel_role(name, rawtext, text, lineno, inliner,
                              options={}, content=[]):
        """Returns a guilabel node including a single unicode html-code"""

        if not text.startswith("&#"):
            msg = inliner.reporter.error("Wrong Unicode! "
                                         "Must start with '&#'.", line=lineno)
            prb = inliner.problematic(rawtext, rawtext, msg)
            return [msg], [prb]

        if not text.endswith(";"):
            msg = inliner.reporter.error("Wrong Unicode! "
                                         "Must end with ';'.", line=lineno)
            prb = inliner.problematic(rawtext, rawtext, msg)
            return [msg], [prb]

        html = f"<span class=\"guilabel\">{text}</span>"
        node = nodes.raw("\n".join(content), html, format="html", **options)

        return [node], []


The arguments are expected in a certain order (see more under
`Creating reStructuredText Interpreted Text Roles`_). The return value is a tuple
containing two lists. The first contains any new nodes to be added to the parse tree,
the second list contains error or warning messages to show the user (processors
are defined to return errors instead of raising exceptions because the error messages
can be inserted into the output instead of halting all processing.

In this example, the node itself is a `raw data node`_, which passes the node data as is.
The nodes text is an HTML expression, wrapping a passed in *text* within a *guilabel* span
assigned to the guilabel class.

Lastly, your extension must be added to ``conf.py``:

.. code-block:: python

    import sys
    import os

    sys.path.insert(0, os.path.abspath(".") + "/_ext")

    extensions = [
    # your other extensions
    "unicode_guilabel"
    ]

You can now use the new role like this:

.. code-block:: rst

    You can click the :unicode-guilabel:`&#5130;` and :unicode-guilabel:`&#5125;`
    buttons to navigate.

translates into:

    You can click the :unicode-guilabel:`&#5130;` and :unicode-guilabel:`&#5125;`
    buttons to navigate.


Full ``unicode_guilabel.py``:

.. literalinclude:: _file/unicode_guilabel.py

.. footbibliography::

.. _guilabel: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-guilabel
.. _Creating reStructuredText Interpreted Text Roles: https://docutils.sourceforge.io/docs/howto/rst-roles.html
.. _raw data node: http://code.nabla.net/doc/docutils/api/docutils/nodes/docutils.nodes.raw.html#raw-class