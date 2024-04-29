Create a new directive
======================
`Sphinx`_ can be extended with new directives. Similar to defining
:ref:`new roles <extend_sphinx_create_custom_role>`, such can be defined in
Python modules, which are attached to the Sphinx application.

Docutils offers a manual on how to `create RST directives`_, and also Sphinx
offers `some tutorials`_ on the subject. Though this How-To guide bases on my
actual experiences and attempts to be as thorough and hands-on as possible.

Understand the concept of directives
------------------------------------
It is important to understand what *directives* actually represent in a Sphinx
application. *Directives* actually are an implementation in `docutils`_, which
Sphinx extends with additional capabilities.

Docutils itself translates the *reStructuredText* syntax in XML, which, similar to
HTML, is a markup language, which consists of *nodes*. These nodes stand in a particular
relation to each other, forming the `Docutils Document Tree`_. Docutils provides
a `docutils.nodes.py`_ Python module, which implements the tree data structure.

The important thing to understand here is, that each piece of content inside a
``*.rst`` file is translated to a class of type ``Node`` or an attribute of it.

Basically, each ``Node`` is represented by a class of type ``Element``, whereas
concrete element classes (detected by docutil's ``NodeVisitor`` instance) inherit
from them. In addition, there are so-called *element category* classes, which the
concrete element class inherit from. The graph below shows the inheritance graph
of a small fraction of available element and  category classes.

.. mermaid::

        classDiagram
            Node <-- Text
            Node <-- Element
            Element <-- TextElement
            Element <-- document
            TextElement <-- title
            TextElement <-- subtitle
            TextElement <-- rubric
            Structural <-- document
            Root <-- document
            Titlebar <-- title
            Body <-- Admonition
            Element <-- admonition
            Admonition <-- admonition

            style Text fill: #85ff83ff
            style Element fill: #85ff83ff
            style TextElement fill: #85ff83ff

            style Admonition fill: #6fb8ffff
            style Structural fill: #6fb8ffff
            style Root fill: #6fb8ffff
            style Titlebar fill: #6fb8ffff

As a naming convention, concrete element classes are named in **camelcase**.
To differentiate, parent element classes are colored in green, category classes
are colored in blue.

When creating a new directive, we have to create two things:

    * the **directive class**, so that the directive is detected as such in an
      RST text (as opposed to regular paragraph text). In other word, *docutils*
      must *know* about the directive.
    * the corresponding **node class** into which the detected directive instance
      (which is created for any match of that directive) is translated into.
      As said above, docutils creates a doctree document out of each RST document,
      which can then be translated into HTML or other format by Sphinx.

Example: Create a custom admonition directive
---------------------------------------------
It is highly advised to make use of existing elements, and extending those, instead
of creating entire new directives from scratch, thereby leveraging code that is
already included in *docutils*. In this example, we will create a *waiting*
admonition, which is used like this:

    .. code-block:: rst

        .. waiting:: 30 min

            Just you wait ...

to be rendered into

    .. waiting:: 30 min

        Just you wait ...

Define the admonition
`````````````````````
For that, we create a new file inside ``source/_ext/`` named ``waiting_admonition.py``.

In here, we import the necessary base classes for both our custom admonition
directive and our custom admonition node:

    .. code-block:: python
        :linenos:
        :lineno-start: 1

        from docutils.parsers.rst.directives.admonitions import BaseAdmonition
        from docutils.nodes import Admonition, Element
        from sphinx.application import Sphinx
        from sphinx.util.typing import ExtensionMetadata

Note, that the imports from line 3 and 4 will be used for type hinting only later on.

The :python:`BaseAdmonition` will be used as a parent of our :python:`WaitingAdmonition`
directive class, where both :python:`Admonition` and :python:`Element` will be the parents
of our :python:`waiting` node class:


    .. code-block:: python
        :linenos:
        :lineno-start: 7

        class waiting(Admonition, Element):
            pass


        class WaitingAdmonition(BaseAdmonition):
            pass

To find out, which classes are best suited to inherit from for both the custom
node class and the directive or role element class, check out these modules

    * Nodes: `docutils.nodes.py`_
    * Directives: `docutils.parsers.rst.directives`_ (choose the respective module)
    * Roles: `docutils.parsers.rst.roles.py`_

The ``waiting`` class is already done. Usually, it doesn't have anything to do
except inheriting from the standard *docutils* class(es) (defined in ``docutils.nodes``).

Let's continue with the implementation of the ``WaitingAdmonition`` class:

    .. code-block:: python
        :linenos:
        :lineno-start: 11

        class WaitingAdmonition(BaseAdmonition):
            required_arguments = 1
            final_argument_whitespace = True
            has_content = True

            node_class = waiting

            def run(self):
                title = " ".join(self.arguments)
                waiting_node = waiting(title=title)
                self.state.nested_parse(self.content, self.content_offset,
                                        waiting_node)
                return [waiting_node]

Each class inheriting from :python:`docutils.parsers.rst.Directive` (which
``BaseAdmonition`` does) may define a list of attributes, which specify how the
*WaitingAdmonition* is supposed to be used.

:line 12-13:
    ``required_arguments = 1`` specifies that the directive expects exactly one
    argument. The ``final_argument_whitespace = True`` attribute declares that
    the last (in this case, the last is also the first, as
    ``optional_arguments`` is not defined, therefore is considered as ``0``)
    argument is expected to contain whitespace.
    Both attributes allow for such syntax:

    .. code-block:: rst

        .. waiting:: 30 min

    Here, ``30 min`` is considered as one argument, as only one is allowed, though
    it may contain whitespaces. Note, that this declaration is optional, as the
    default value is already ``True``.

:line 14:
    ``has_content = True`` allows for providing content inside the admonition.
    Providing content, while this is set to ``False`` will throw an error during
    parsing the directive. It allows for the following syntax:

    .. code-block:: rst

        .. waiting:: 30 min

            Please wait patiently, a good time to get a coffee.

:line 16:
    This line is a special attribute added by th :python:`BaseAdmonition` class,
    which specifies the admonition node class, the *WaitingAdmonition* element
    is set to in the doctree. This will be our :python:`waiting` class, which
    will be defined next.

:line 18:
    Defining the :python:`run()` method is mandatory, as it is called to
    transform the associated directive into one or more nodes.

    Additional arguments are defined in the ``rst.Directive`` docstring:

        .. code-block:: python

            >>> from docutils.parsers import rst
            >>> print rst.Directive.__doc__

:line 19:
    All arguments values, separated by space, are mapped into a list. The
    ``title`` variable is created by concatenating this list of all input
    arguments. So, for

    .. code-block:: rst

        .. waiting:: 30 min or more

    the ``title`` will be ``30 min or more``.

:line 20:
    Creating the node that the *waiting* admonition is supposed to be translated
    to. Here, it passes the ``title`` variable as *title*, so that the node can
    make use of it.

:line 21-22:
    Calling the ``self.state.nested_parse()`` method, the content body of the
    directive is parsed. The first argument gives the content body, and the second
    one gives content offset. The third argument gives the parent node of parsed
    result, in our case the waiting node. Following this, the waiting node is
    added to the environment. This is needed to be able to insert the waiting
    directive's *content* into the directive entries.

:line 23:
    Return the node to be put into the doctree (here, the waiting node). As multiple
    nodes may be returned for a directive, a list of one or more nodes is expected.

As a next step, the custom waiting node must receive methods on how the *waiting*
doctree node is translated into a HTML node, specifically ``sphinx.writers.html5.HTML5Translator``
(other writer, such as for *latex*, each require separate methods. A method for
visiting the node and departing from the node is needed. The former defines what
HTML nodes to insert **before** any further nested nodes (see line 1 below), the latter
defines what nodes to insert **after** any further nested nodes (see line 3 blow):

    .. code-block:: html

        <div my_custom_node>
            // further nested contents
        </div>

In the easiest case, the ``visit_waiting_node()`` and ``depart_waiting_node()``
methods may simply call the predefined Sphinx ``sphinx.writers.html5.HTML5Translator``
methods for visiting and departing from admonition nodes:

    .. code-block:: python

        def visit_waiting_node(self, node):
            self.visit_admonition(node)

        def depart_waiting_node(self, node):
            self.depart_admonition(node)

    .. note::

        The ``self`` argument is the writer instance, in case of HTML,
        the ``sphinx.writers.html5.HTML5Translator`` instance. It must be declared
        like that even though the functions are defined outside of a class.

In our case, this is not sufficient, because passing only the ``node`` into the
predefined methods, will create an admonition without title. Calling it like
:python:`self.visit_admonition(node, 'waiting')` will lead to an error, as the
admonition label :python:`'waiting'` is not known to sphinx. We could pass in a
known label, such as :python:`self.visit_admonition(node, 'warning')`, but this
will treat our custom *waiting* node exactly like a built-in *warning* node,
which obscures the existence of this custom admonition (we could have used a
warning admonition, in that case).

For this reason, we will define a custom body for the *waiting* node:

    .. code-block:: python
        :linenos:
        :lineno-start: 26

        def visit_waiting_node(self, node):
            self.body.append("<div class=\"admonition waiting\">")
            self.body.append("<p class=\"admonition-title\">")
            self.body.append(f"{node.get('title')}")
            self.body.append("</p>")


        def depart_waiting_node(self, node):
            self.body.append("</div>")

    .. note::

        Besides the ``self`` argument, both methods require the ``node`` argument,
        even if it is not used (as is the case for :python:`depart_waiting_node()`).

:line 27:
    Append a :html:`<div>` element to the HTML writer ``body``, with the
    :html:`class=\"admonition waiting\"` attribute. The ``admonition`` class is
    present for all admonition nodes, whereas the ``waiting`` class is a new
    class, allowing for customized styling.

    Note, that the :html:`<div>` element is not closed here (will be done in
    the :python:`depart_waiting_node()` method in line 34.

    .. hint::

        The same is achieved by adding the ``:class: waiting`` option to a
        admonition directives:

        .. code-block:: rst

            .. admonition::
                :class: waiting

:line 28:
    Appends the admonition title bar into the admonition.

    .. hint::

        Even though this element is contained in the :html:`<div>` admonition element,
        there is no need to indent the string. The rendering browser will handle
        this automatically.

:line 29:
    The admonition-title is appended. This ``title`` value was defined and
    inserted into the *waiting* node in the ``WaitingAdmonition.run()`` method.
    Node attributes can be retrieved by the ``Element.get()`` method.

:line 30:
    This adds a closing line for the admonition-title paragraph node. This line
    can actually be omitted, as a closing statement for this element is automatically
    set by the rendering browser before the next element starts. This is because
    the following node will be another paragraph (:html:`<p>`) which will contain the
    contents of the waiting admonition. Nesting one paragraph into another is
    not possible in HTML, so the paragraph is closed, before another one is opened.


Last but not least, both the defined *waiting* admonition and the *waiting* node
must be registered in Sphinx, so they are known to the Sphinx builder:

    .. code-block:: python
        :linenos:
        :lineno-start: 37

        def setup(app: Sphinx):
            app.add_node(waiting, html=(visit_waiting_node, depart_waiting_node))
            app.add_directive('waiting', WaitingAdmonition)

            return {'version': '0.1'}

:line 37:
    The ``setup()`` method is a required method to plug new directives into Sphinx.
    It requires the Sphinx application instance as an argument.

:line 38:
    The :python:`add_node()` method registers the *waiting* node. For the ``html``
    builder, it expects a tuple, consisting of the *visiting* and the *departing*
    method for the node. For this, we pass the previously defined respective methods.

:line 39:
    The :python:`add_directive` method register the 'waiting* directive. It requires
    the name value of the directive (here: :python:`'waiting'`) and the admonition,
    this name is connected to (here: :python:`WaitingAdmonition`).

:line 41:
    This return statement is optional. It may return a dictionary, which is treated
    as the extensions metadata. For more info, see `Extension metadata`_.

This concludes the definition of the *waiting* admonition.

This is the entire content of the ``waiting_admonition.py`` module:

.. literalinclude:: _file/waiting_admonition.py
    :language: python
    :linenos:

Add the admonition to the config
````````````````````````````````
The *waiting* admonition can now be added the documentation's ``conf.py`` file.
Under the :python:`extensions=[...]` list, add the module name of the extension:

    .. code-block:: python

        extensions = [
            # other extensions
            'waiting_admonition'
        ]

Make sure, the ``source/_ext/`` directory is added to the interpreter's
PYTHONPATH. Add the following line near the top of the ``conf.py`` file:

    .. code-block:: python

        import os
        import sys

        sys.path.insert(0, os.path.abspath('.') + '/_ext')

On the next build, the extension will allow for using *waiting* admonitions:

    .. code-block:: rst

        .. waiting:: 30 min

            You just missed to the train. Have to catch the next one.

Style the admonition
````````````````````
For the rendered HTML output, the style of the waiting admonition will be
defined by the used theme. And those themes naturally don't provide a custom
style for nodes that are not part of basic Sphinx. Hence, it is the responsibility
of the extension to provide a decent style.

.. note::

    A customized style might only work for a particular theme, as each may use
    different HTML templates. Effectively, CSS rules customized for a particular
    theme's HTML template, are likely not considered for those of other themes.

    As a general rule, when starting to add custom CSS rules, be certain to
    stay on a particular theme for the documentation project. It is not a
    solution to make CSS rules more general, making it match for templates
    on various themes, as the rules likely have low `specificity`_, that they
    are overridden by the theme's own, more specific, CSS rules.

    As a workaround, you may define a ``custom.css`` file for each used theme:

    .. code-block:: python

        if html_theme == 'sphinx_rtd_theme':
            html_css_files = [
                'css/custom_rtd.css',
            ]
        elif html_theme == 'nature':
            html_css_files = [
                "css/custom_nature.css"
            ]

Make sure, the ``conf.py`` contains the variable definition to support custom styling:

    .. code-block:: python

        html_static_path = ['_static']
        html_css_files = [
                'css/custom.css',
            ]

In your ``source/_static/css/custom.css`` file, add the following content:

    .. code-block:: css

        .admonition.waiting { background: #e7ffc2ff; }
        .admonition.waiting p.admonition-title { background: #7eab48ff; }
        .admonition.waiting p.admonition-title::before { content: "\2615   "; }

The style is applied after at the next ``sphinx-build`` run.


.. _create RST directives: https://docutils.sourceforge.io/docs/howto/rst-directives.html
.. _Docutils Document Tree: https://docutils.sourceforge.io/docs/ref/doctree.html
.. _docutils.nodes.py: https://docutils.sourceforge.io/docutils/nodes.py
.. _docutils.parsers.rst.directives: https://docutils.sourceforge.io/docutils/parsers/rst/directives/
.. _docutils.parsers.rst.roles.py: https://docutils.sourceforge.io/docutils/parsers/rst/roles.py
.. _docutils: https://docutils.sourceforge.io/
.. _Extension metadata: https://www.sphinx-doc.org/en/master/extdev/index.html#extension-metadata
.. _some tutorials: https://www.sphinx-doc.org/en/master/development/tutorials/index.html
.. _specificity: https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity
.. _Sphinx: https://www.sphinx-doc.org/en/master/
