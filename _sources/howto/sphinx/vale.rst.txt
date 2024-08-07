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

    .. code-block:: bash

        $ brew install vale

    **Windows:**

    .. code-block:: bash

        $ choco install vale

#. Open the project directory which contains the documents you want to lint.
#. Make sure the project's Python interpreter has sphinx or docutils installed
   (to parse \*.rst files, vale requires the `rst2hmtl`_ tool, which comes with
   either of them).

    .. important::

        Don't use a sphinx or docutils installation from `pipx`_ (to have it available
        from outside of your project's virtual environment, as vale expects it inside
        your Python environment.

#. In your project documentation directory create these additional directory and file:

    .. code-block:: none

        .
        ├── styles/
        └── .vale.ini

#. Define one or multiple styles to check your input texts against. Check the `Package Hub`_
   for available styles.

    .. hint::

        You may adapt existing styles to your liking or define a custom style from scratch.
        Check https://vale.sh/docs/topics/styles/ for guidance.

        It happens that styles have conflicting rules. In that case either adapt the rule of
        any style or reduce the amount of styles in the configuration.

#. Open the ``.vale.ini`` file and define the config (here: `Microsoft Writing Style Guide`_):

    .. code-block:: ini

        StylesPath = ./.vale_styles
        MinAlertLevel = suggestion
        [*.{rst}]
        BasedOnStyles = Vale, Microsoft

    .. hint::

        Exchange the *BasedOnStyles* parameter value with your downloaded style.

#. Download and install external configuration sources via

    .. code-block:: bash

        $ vale sync

    .. warning::

        Executing ``sync`` re-downloads **all** specified styles . Any adjustments to the
        original styles have been done are overwritten. It is highly advised to save a
        backup of your adjustments in a separate location before running ``sync`` or
        adding the styles folder to version control to revert files, if needed.

.. hint::

    **Additional styles**

    Other styles, not present on `Package Hub`_ may also be installed manually,
    but **not** via ``vale sync``. To activate the style, add the style's directory
    name to the *BasedOnStyles* option in ``.vale.ini``.

    ======      ====
    Name        URL
    ======      ====
    gitlab      https://gitlab.com/gitlab-org/gitlab/-/tree/master/doc/.vale/gitlab
    ======      ====

.. _release page: https://github.com/errata-ai/vale/releases/
.. _rst2hmtl: https://docutils.sourceforge.io/docs/user/tools.html#rst2html-py
.. _pipx: https://github.com/pypa/pipx
.. _style: https://github.com/errata-ai/packages#available-styles
.. _Package Hub: https://vale.sh/hub/
.. _Microsoft Writing Style Guide: https://github.com/errata-ai/Microsoft/releases

Usage
-----
.. important::

    Make sure your Python environment is activated before running ``vale``.

To execute a check on a single document execute:

    .. code-block:: bash

        $ vale </path/to/some.rst>

It will list you all the detected violations. You may open the respective grammar
file and edit the rules to your liking.
