New Project Setup
=================
This guideline shows how to set up a standard Python project. It features, how
to structure the project and installing helping packages.

.. _project_dev_packages_overview:

Package Overview :footcite:p:`popular_python_project_tools`
-----------------------------------------------------------
.. csv-table:: Essential project tools
    :file: _file/project_tools.csv
    :header-rows: 1
    :widths: auto

\* optional

Create project structure
------------------------
`Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`__ creates a
project structure based on predefined templates. This saves you the effort of
having to manually add various files and folder structures.

Since you will need *cookiecutter* only once, at the beginning of your project, it
is recommended to install it outside of your :ref:`project's virtual environment <setup_virtual_environment>`.

Cookiecutter & pip-tools installation
`````````````````````````````````````
A recommendation is to make both tools globally available using
`pipx <https://github.com/pypa/pipx>`_.
The installation only needs to be done once (afterwards you can use *cookiecuttter* and
the pip-tools commands *pip-compile* and *pip-sync* anywhere).

First, let's create a virtual environment for *pipx* (here: via *pyenv*):

.. note::

    The <PYTHON_VERSION> must not be the same as the future project's interpreter.
    Choose the latest version, which both tools (pip-tools & cookiecutter) and
    of course, pipx itself, support:

    * `pipx <https://github.com/pypa/pipx>`__
    * `cookiecutter <https://github.com/cookiecutter/cookiecutter>`__
    * `pip-tools <https://github.com/jazzband/pip-tools>`__

.. prompt:: bash

    pyenv virtualenv <PYTHON_VERSION> pipx

Activate the environment:

.. prompt:: bash

    pyenv activate pipx

Next, let's install pipx:

.. prompt:: bash (pipx)

    pip install pipx

Now, we'll have to ensure that the packages installed via pipx are added to our PATH
variable so they are executable from anywhere (only needs to be done once):

.. prompt:: bash (pipx)

    pipx ensurepath

Now we're ready to install cookiecutter & pip-tools in it:

.. prompt:: bash (pipx)

    pipx install cookiecutter
    pipx install pip-tools

Open a new terminal window and run ``cookiecutter -V``, which should print the
installed cookiecutter package's version. Also run ``pip-compile --version`` and
``pip-sync --version`` to verify the installation success.

Adjust cookiecutter template
````````````````````````````
First you need to select a template, from which to generate your project structure.
Browse https://github.com/search?q=cookiecutter&type=Repositories to find the best match
for the technology, you want to use.

A general purpose template from the original author of cookiecutter is
https://github.com/audreyfeldroy/cookiecutter-pypackage. Follow the instructions on
https://cookiecutter.readthedocs.io/en/1.7.2/usage.html#usage to clone the template and
make adaptions on ``cookiecutter.json``.

There is already an adapted version of this template available at
https://github.com/horsewithnoname1985/my-cookiecutter-pypackage, which we will use in
this tutorial.

The template sets up a `makefile <https://en.wikipedia.org/wiki/Make_(software)>`_, which
features commands for

* building distribution & documentation (as well as link checks)
* executing tests (regular & code coverage)
* linting code
* static type check
* installing the package (into your active Python environment)
* cleaning build, test, coverage and Python artifacts

and more.

Create project
``````````````
Now we're ready to create the project based on our slightly adapted template:

.. prompt:: bash

    cd /my/project/root/dir
    cookiecutter /path/to/cookiecutter/template/root/dir

For example:

.. prompt:: bash

    mkdir ~/best_practice_project
    cd ~/best_practice_project
    cookiecutter ~/my_templates/cookiecutter-pypackage

Define your project parameters in the wizard.

.. _setup_virtual_environment:

Create your project's virtual environment
-----------------------------------------
It is recommended to create a virtual environment using ``pyenv <install_pyenv>``
(with the pyenv-virtualenv extensions).

Create virtual environment via:

.. prompt:: bash

    pyenv virtualenv <PYTHON-VERSION> <VENV_NAME>

Alternatively, use may use Python's built-in `venv <https://docs.python.org/3/library/venv.html>`_
via

.. prompt:: bash

    python -m venv <VENV_NAME>

which uses the interpreter which is referred to via ``python`` and creates a virtual
environment named <VENV_NAME> inside your current directory (you may also specify an absolute path).

As a second alternative, the module `virtualenv <https://pypi.org/project/virtualenv/>`_ can
also be used. Although, it has to be installed into the Python environment (from which to
create the virtual environment from) first:

.. prompt:: bash

    pip install virtualenv
    virtualenv <VENV_NAME>

Same as for Python's built in *venv* module, it creates a virtual environment in your
current directory.

A major difference of *virtualenv* is that the created environment is autonomous of its
originating interpreter, whereas the other two still require resources from the original
interpreter.

Install dependencies
````````````````````
First, install `pip-tools <https://github.com/jazzband/pip-tools>`_, which we use
to manage our dependencies (activate your project's virtual environment first):

.. prompt:: bash, (project_venv)

    pip install pip-tools

All requirements for development as mentioned in the :ref:`overview table <project_dev_packages_overview>`
are already listed in ``requirements-dev.in``. To create a ``requirements-dev.txt``,
execute:

.. prompt:: bash, (project_venv)

    pip-compile requirements-dev.in -o requirements-dev.txt

This produces the \*.txt file containing our dependencies plus all required
packages for those dependecies (all using pinned versions). To install all these
dependencies, execute:

.. prompt:: bash, (project_venv)

    pip-sync requirements-dev.txt

.. hint::

    All dependencies which are required to **execute** our project will be gathered
    in ``requirements.in``. Same workflow here:

    .. prompt:: bash, (project_venv)

        pip-compile requirements.in -o requirements.txt
        pip-sync requirements.txt

.. footbibliography::