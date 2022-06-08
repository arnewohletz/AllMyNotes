Documentation linting with vale
===============================
`Vale`_ is a command-line tool for linting text documents. It also supports
linting \*.rst files, so can be used for Sphinx documentation.

Only the most basic steps are described. For more info go to https://vale.sh/docs/vale-cli/installation/.

.. _Vale: https://github.com/errata-ai/vale

Setup
------
#. Install vale. Either download it from the `release page`_ extract it at a
   proper location (add directory to your PATH variable) or download via a
   package manager:

    **macOS:**

    .. prompt:: bash

        brew install vale

    **Windows:**

    .. prompt:: bash

        choco install vale

#. Open the project directory which contains the documents you want to lint.
#. Make sure the project's Python interpreter has sphinx or docutils installed
   (to parse \*.rst files, vale requires the `rst2hmtl`_ tool, which comes with
   either of them).

    .. important::

        Don't use a sphinx or docutils installation from `pipx`_ (to have it available
        from outside of your project's virtual environment, as vale expects it inside
        your Python environment.

#. Download a `style`_ (you may adapt it to your needs later) for example the
   `Microsoft Writing Style Guide`_.
#. In your project documentation directory create these additional directory and file:

    .. code-block:: none

        .
        ├── styles/
        └── .vale.ini

#. Extract your downloaded style into the ``style``directory (e.g. ``style/microsoft``).
#. Open the ``.vale.ini`` file and enter this content:

    .. code-block:: ini

        StylesPath = ./vale
        MinAlertLevel = suggestion
        [*.{rst}]
        BasedOnStyles = Microsoft

    .. hint::

        Exchange the *BasedOnStyles* parameter value with your downloaded style.

.. _release page: https://github.com/errata-ai/vale/releases/
.. _rst2hmtl: https://docutils.sourceforge.io/docs/user/tools.html#rst2html-py
.. _pipx: https://github.com/pypa/pipx
.. _style: https://github.com/errata-ai/packages#available-styles
.. _Microsoft Writing Style Guide: https://github.com/errata-ai/Microsoft/releases

Usage
-----
.. important::

    Make sure your Python environment is activated before running ``vale``.

To execute a check on a single document execute:

    .. prompt:: bash

        vale </path/to/some.rst>

It will list you all the detected violations. You may open the respective grammar
file and edit the rules to your liking.