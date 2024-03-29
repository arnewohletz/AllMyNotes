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

Third-party extensions
----------------------
Autodoc
```````
* `sphinx-autodoc-typehints`_: Use type annotations for documenting acceptable argument
  types and return value types of function
* `sphinx-click`_: Automatically extract documentation from a Click-based application and
  include it in your docs

Code blocks & prompts
`````````````````````
* `sphinx-copybutton`_: Adds a copy button to all code and command line blocks
* `sphinx-prompt`_: Directive for unselectable prompts (nice for bash sections)

Design Elements
```````````````
* `sphinx-datatables`_: Add data tables, which allow sorting entries
* `sphinx-design`_: Designing beautiful, screen-size responsive web-components
* `sphinx-tabs`_: Directive to add tabbed content for output HTML
* `sphinxcontrib-images`_: Directive for thumbnail images which can be magnified
  (as of early 2024, apply `this change <sphinxcontrib_images_use_non_deprecation_>`_
  to remove deprecation warning during building HTML)
* `sphinxemoji`_: Roles for adding emojis

Jupyter Notebooks
`````````````````
* `nbsphinx`_: Extension that provides a source parser for \*.ipynb files
* `jupyter_sphinx`_: Directive to define Jupyter-like code cells, embedding its output

Git
```
* `sphinx-git`_: Directive for adding latest git commits information to docs
* `sphinx-gitstamp`_: Directive for inserting a git datestamp into the context

Graphs
``````
* `plantuml <sphinx_plantuml_>`_: Directives for `PlantUML`_ graphs
* `sphinxcontrib-mermaid`_: Directive for `mermaid graphs`_ (as of early 2024, conflicts
  with `nbsphinx`_ and `jupyter_sphinx`_; if used together with either of these, apply
  `this workaround <mermaid_jupyter_fix_>`_ to load ``mermaid.min.js`` after the Jupyter notebook JavaScript)

Publish
```````
* `sphinxcontrib-confluencebuilder`_: Sphinx extension to build Atlassian Confluence Storage Markup
* `sphinx-sitemap`_: Generate multi-version and multi-language sitemaps.org compliant sitemaps
  for the HTML version of your Sphinx documentation

Quoting
```````
* `sphinxcontrib-bibtex`_: Allows `BibTeX`_ citations into the documentation

Search
``````
* `sphinx-docsearch`_: Replaces built-in search engine with `Algolia DocSearch`_. Check out
  the setup manual for :ref:`v2 <docsearch_v2_sphinx>` or :ref:`v3 <docsearch_v3_sphinx>`
  of the crawler.

Substitution
````````````
* `sphinx-issues`_: Create links to project's issue tracker (useful if doc only covers single repo)
* `sphinx-substitution-extensions`_: Allow substitutions within code blocks, prompts and inline

Themes
``````
* `furo`_: A clean customisable Sphinx documentation theme.
* `sphinxawesome-theme`_
* `sphinx-book-theme`_: A clean book theme for scientific explanations and documentation with Sphinx
* `sphinx-rtd-theme`_: Theme used for the web page of this documentation (provided by `ReadTheDocs.com`_)

Additional themes can be browsed in the `Sphinx Themes Gallery`_.

Tweaks
``````
* `sphinxnotes-comboroles`_: Sphinx extension for composing multiple roles
* `sphinxnotes-strike`_: An extension that adds strikethrough text support to Sphinx

Videos
``````
* `sphinxcontrib-video`_: Embed ``.mp4``, ``.webm`` and ``.ogg`` videos into RST documents
* `sphinxcontrib-youtube`_: Insert videos from YouTube and Vimeo (by reference)


.. Extensions links
.. _furo: https://github.com/pradyunsg/furo
.. _jupyter_sphinx: https://jupyter-sphinx.readthedocs.io/en/latest/
.. _nbsphinx: https://nbsphinx.readthedocs.io/en/latest/
.. _sphinx-autodoc-typehints: https://github.com/tox-dev/sphinx-autodoc-typehints
.. _sphinx-book-theme: https://github.com/executablebooks/sphinx-book-theme
.. _sphinx-click: https://github.com/click-contrib/sphinx-click
.. _sphinx-copybutton: https://sphinx-copybutton.readthedocs.io/en/latest/
.. _sphinx-datatables: https://sharm294.github.io/sphinx-datatables/
.. _sphinx-design: https://sphinx-design.readthedocs.io/en/latest/index.html
.. _sphinx-docsearch: https://sphinx-docsearch.readthedocs.io/en/latest/
.. _sphinx-git: https://github.com/OddBloke/sphinx-git
.. _sphinx-gitstamp: https://github.com/jdillard/sphinx-gitstamp
.. _sphinx-issues: https://github.com/sloria/sphinx-issues
.. _sphinx-prompt: http://sbrunner.github.io/sphinx-prompt/
.. _sphinx-rtd-theme: https://sphinx-rtd-theme.readthedocs.io/en/latest/
.. _sphinx-sitemap: https://sphinx-sitemap.readthedocs.io/en/latest/index.html
.. _sphinx-substitution-extensions: https://github.com/adamtheturtle/sphinx-substitution-extensions
.. _sphinx-tabs: https://sphinx-tabs.readthedocs.io/en/latest/
.. _sphinx_plantuml: https://github.com/sphinx-contrib/plantuml/
.. _sphinxawesome-theme: https://sphinxawesome.xyz/
.. _sphinxcontrib-bibtex: https://github.com/mcmtroffaes/sphinxcontrib-bibtex
.. _sphinxcontrib-confluencebuilder: https://sphinxcontrib-confluencebuilder.readthedocs.io/en/stable/
.. _sphinxcontrib-images: https://sphinxcontrib-images.readthedocs.io/en/latest/
.. _sphinxcontrib-mermaid: https://github.com/mgaitan/sphinxcontrib-mermaid
.. _sphinxcontrib-video: https://github.com/sphinx-contrib/video
.. _sphinxcontrib-youtube: https://github.com/sphinx-contrib/youtube
.. _sphinxemoji: https://github.com/sphinx-contrib/emojicodes
.. _sphinxnotes-comboroles: https://sphinx.silverrainz.me/comboroles/index.html
.. _sphinxnotes-strike: https://sphinx.silverrainz.me/strike/

.. Other Links
.. _Algolia Docsearch: https://docsearch.algolia.com/
.. _BibTeX: https://www.bibtex.org/
.. _mermaid graphs: https://mermaid.js.org/
.. _mermaid_jupyter_fix: https://github.com/mgaitan/sphinxcontrib-mermaid/issues/74#issuecomment-1937184257
.. _PlantUML: https://plantuml.com/
.. _ReadTheDocs.com: https://about.readthedocs.com/
.. _Sphinx Themes Gallery: https://sphinx-themes.org/
.. _sphinxcontrib_images_use_non_deprecation: https://github.com/sphinx-contrib/images/compare/master...j9ac9k:images:use-non-deprecated-sphinx-api

Custom extensions
-----------------
Plug-ins
````````
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
``````````
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
`````
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

.. code-block:: rst

    :strike:`Struck through` text parts

renders into

:strike:`Struck through` text parts
