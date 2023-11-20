reStructuredText & Sphinx
=========================
Basics (docutils)
-----------------
* `Quick reStructuredText`_: Short reference for most the basic syntax
* `reStructuredText Markup Specification`_: Comprehensive syntax guide
* `reStructuredText Directives`_: Guide on directives (special sections)

.. _Quick reStructuredText: https://docutils.sourceforge.io/docs/user/rst/quickref.html
.. _reStructuredText Markup Specification: https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html
.. _reStructuredText Directives: https://docutils.sourceforge.io/docs/ref/rst/directives.html

Extensions by Sphinx
--------------------
* `reStructuredTest Primer`_: Short reference for most the basic syntax (similar to docutils description)
* `Directives`_: Guide on directives (special sections)
* `Roles`_: Special inline text markups

.. _reStructuredTest Primer: https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html
.. _Directives: https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html
.. _Roles: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html

Docs for used plugins
---------------------
* `jupyter_sphinx`_: Directive to define Jupyter-like code cells, embedding its output
  (Warning: as of Oct 2023, conflicts with `sphinxcontrib-mermaid`_ &
  `sphinxcontrib-images`_ - use `nbsphinx`_ as an alternative)
* `nbsphinx`_: Extension that provides a source parser for \*.ipynb files
* `sphinx-copybutton`_: Adds a copy button to all code and command line blocks
* `sphinx-design`_: Designing beautiful, screen-size responsive web-components
* `sphinx-git`_: Directive for adding latest git commits information to docs
* `sphinx-gitstamp`_: Directive for inserting a git datestamp into the context
* `sphinx-prompt`_: Directive for unselectable prompts (nice for bash sections)
* `sphinx-rtd-theme`_: Theme used for the web page of this documentation
* `sphinx-tabs`_: Directive to add tabbed content for output HTML
* `sphinxcontrib-bibtex`_: Allows `BibTeX`_ citations into the documentation
* `sphinxcontrib-images`_: Directive for thumbnail images which can be magnified
* `sphinxcontrib-mermaid`_: Directive for `mermaid graphs`_
* `sphinxemoji`_: Roles for adding emojis


.. _jupyter_sphinx: https://jupyter-sphinx.readthedocs.io/en/latest/
.. _nbsphinx: https://nbsphinx.readthedocs.io/en/latest/
.. _sphinx-copybutton: https://sphinx-copybutton.readthedocs.io/en/latest/
.. _sphinx-design: https://sphinx-design.readthedocs.io/en/latest/index.html
.. _sphinx-git: https://github.com/OddBloke/sphinx-git
.. _sphinx-gitstamp: https://github.com/jdillard/sphinx-gitstamp
.. _sphinx-prompt: http://sbrunner.github.io/sphinx-prompt/
.. _sphinx-rtd-theme: https://sphinx-rtd-theme.readthedocs.io/en/latest/
.. _sphinx-tabs: https://sphinx-tabs.readthedocs.io/en/latest/
.. _sphinxcontrib-bibtex: https://github.com/mcmtroffaes/sphinxcontrib-bibtex
.. _sphinxcontrib-images: https://sphinxcontrib-images.readthedocs.io/en/latest/
.. _sphinxcontrib-mermaid: https://github.com/mgaitan/sphinxcontrib-mermaid
.. _sphinxemoji: https://github.com/sphinx-contrib/emojicodes

.. _BibTeX: https://www.bibtex.org/
.. _mermaid graphs: https://mermaid.js.org/


Custom extensions
-----------------
Plug-ins
''''''''
* unicode-guilabel: Support single unicode character (e.g. emoji) inside `guilabel`_ role.

    Usage Example:

    .. code-block:: rst

        You can click the :unicode-guilabel:`&#5130;` and :unicode-guilabel:`&#5125;`
        buttons to navigate.

    renders into

    You can click the :unicode-guilabel:`&#5130;` and :unicode-guilabel:`&#5125;`
    buttons to navigate.

    .. hint::

        You can get Unicode HTML Codes at https://symbl.cc/en/.

.. _guilabel: https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-guilabel


Directives
''''''''''
The following custom directives are available in this documentation:

.. rubric:: Admonitions

.. code-block:: rst

    .. admonition:: Design Principle
        :class: design_principle

        Functions should either be **queries** or **commands**. Queries are for getting
        data, but must not change the state. Commands are supposed to change the state,
        but must not return any data. Functions must not do both.

    .. admonition:: Pattern Definition
        :class: pattern_definition

        The **Abstract Factory Pattern** provides an interface for creating families
        of related or dependent objects without specifying their concrete classes.

    .. admonition:: Problem
        :class: problem

        Some content for the custom problem admonition which is not important here.

renders into

    .. admonition:: Design Principle
        :class: design_principle

        Functions should either be **queries** or **commands**. Queries are for getting
        data, but must not change the state. Commands are supposed to change the state,
        but must not return any data. Functions must not do both.

    .. admonition:: Pattern Definition
        :class: pattern_definition

        The **Abstract Factory Pattern** provides an interface for creating families
        of related or dependent objects without specifying their concrete classes.

    .. admonition:: Problem
        :class: problem

        Some content for the custom problem admonition which is not important here.


Roles
'''''
The following custom roles are available in this documentation:

**Inline Code Highlighting**

Syntax highlighting for inline code for various languages:

.. code-block:: rst

    * **Python**: Use the command :python:`print "Hello World"` to say hi.
    * **Java**: Use the command :java:`System.out.println("Hello World");` to say hi.
    * **JavaScript**: Use command :javascript:`console.log("Hello World");` to say hi.
    * **HTML**: Use line :html:`<p>Hello World</p>` to say hi.
    * **RST**: Use line :rst:`**Hello World**` to boldly say hi.
    * **Bash**: Use line :bash:`echo "Hello World"` to say hi.


renders into

    * **Python**: Use the command :python:`print "Hello World"` to say hi.
    * **Java**: Use the command :java:`System.out.println("Hello World");` to say hi.
    * **JavaScript**: Use command :javascript:`console.log("Hello World");` to say hi.
    * **HTML**: Use line :html:`<p>Hello World</p>` to say hi.
    * **RST**: Use line :rst:`**Hello World**` to boldly say hi.
    * **Bash**: Use line :bash:`echo "Hello World"` to say hi.

**Raw HTML**

Sometimes reStructureText does not offer a proper symbol or styling capabilities
for a desired HTML output, in which case a *raw HTML* string can be used:

.. code-block:: rst

    This is my phone number: :raw-html:`&#9742;` 0170-123456789.
    This is called a :raw-html:`<span style="font-family: Courier">description</span>`.

renders into

    | This is my phone number: :raw-html:`&#9742;` 0170-123456789.
    | :raw-html:`This is called a <span style="font-family: Courier">description</span>.`

**Colors**

.. code-block:: rst

    Background colors in :rbg:`red` and :gbg:`green`, as well as foreground color in
    :rfg:`red` and :gfg:`green`.

renders into

Background colors in :rbg:`red` and :gbg:`green`, as well as foreground color in
:rfg:`red` and :gfg:`green`.

**Other formatting**

.. code-block:: rst

    :ulined:`Underlined` text parts

renders into

:ulined:`Underlined` text parts