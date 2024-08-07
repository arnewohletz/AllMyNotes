New Project Setup
=================
This guideline shows how to set up a standard Python project. It features, how
to structure the project and installing helping packages.

.. _project_dev_packages_overview:

Used packages :footcite:p:`popular_python_project_tools`
--------------------------------------------------------
.. csv-table:: Essential project tools
    :file: _file/project_tools.csv
    :header-rows: 1
    :widths: auto

\* optional

Create project structure
------------------------
`Cookiecutter <https://cookiecutter.readthedocs.io/en/latest/>`__ creates a
project structure based on predefined templates. This saves you the effort of
manually adding various files and folder structures.

Because you need *cookiecutter* only once, at the beginning of your project, it
is recommended to install it outside of your :ref:`project's virtual environment <setup_virtual_environment>`.

Cookiecutter installation
`````````````````````````
A recommendation is to make both tools globally available using
`pipx <https://github.com/pypa/pipx>`_.
The installation only must be done once (afterwards you can use *cookiecutter*
command from anywhere).

First, let's create a virtual environment for *pipx* (here: via *pyenv*):

.. note::

    The <PYTHON_VERSION> must not be the same as the future project's interpreter.
    Choose the latest version, which both *cookiecutter and *pipx* itself support:

    * `pipx <https://github.com/pypa/pipx>`__
    * `cookiecutter <https://github.com/cookiecutter/cookiecutter>`__

.. code-block:: bash

    $ pyenv virtualenv <PYTHON_VERSION> pipx

Activate the environment:

.. code-block:: bash

    $ pyenv activate pipx

Next, let's install pipx:

.. code-block:: bash

    (pipx) $ pip install pipx

Now, we have to ensure that the packages installed via pipx are added to our PATH
variable. This ensures that those are executable from anywhere (only must to be done once):

.. code-block:: bash

    (pipx) $ pipx ensurepath

Now we're ready to install cookiecutter & pip-tools in it:

.. code-block:: bash

    (pipx) pipx install cookiecutter

Open a new terminal window and run ``cookiecutter -V``, which should print the
installed cookiecutter package's version.

Adjust cookiecutter template
````````````````````````````
First you must select a template, from which to generate your project structure.
Browse https://github.com/search?q=cookiecutter&type=Repositories to find the best match
for the technology, you want to use.

A general purpose template from the original author of cookiecutter is
https://github.com/audreyfeldroy/cookiecutter-pypackage. Follow the instructions on
https://cookiecutter.readthedocs.io/en/1.7.2/usage.html#usage to clone the template and
make adaptions on ``cookiecutter.json``.

There is already an adapted version of this template available at
https://github.com/arnewohletz/my-cookiecutter-pypackage, which we use in
this tutorial.

The template sets up a `makefile <https://en.wikipedia.org/wiki/Make_(software)>`_, which
features commands for

* building distribution & documentation (as well as link checks)
* executing tests (regular & code coverage)
* linting code
* static type check
* installing the package (into your active Python environment)
* cleaning, build, test, determine test coverage of Python artifacts

and more.

Create project
``````````````
Now we're ready to create the project based on our slightly adapted template:

.. code-block:: bash

    $ cd /my/project/root/dir
    $ cookiecutter /path/to/cookiecutter/template/root/dir

For example:

.. code-block:: bash

    $ mkdir ~/best_practice_project
    $ cd ~/best_practice_project
    $ cookiecutter ~/my_templates/cookiecutter-pypackage

Define your project parameters in the wizard.

.. _setup_virtual_environment:

Create your project's virtual environment
-----------------------------------------
We recommended to create a virtual environment using ``pyenv <install_pyenv>``
(with the pyenv-virtualenv extensions).

Create virtual environment via:

.. code-block:: bash

    $ pyenv virtualenv <PYTHON-VERSION> <VENV_NAME>

Alternatively, use may use Python's built-in `venv <https://docs.python.org/3/library/venv.html>`_
via

.. code-block:: bash

    $ python -m venv <VENV_NAME>

It uses the venv module and creates a virtual environment named <VENV_NAME> inside
your current directory (you may also specify an absolute path).

As a second alternative, the module `virtualenv <https://pypi.org/project/virtualenv/>`_ can
also be used. Although, it has to be installed into the Python environment (from which to
create the virtual environment from) first:

.. code-block:: bash

    $ pip install virtualenv
    $ virtualenv <VENV_NAME>

Same as for Python's built in *venv* module, it creates a virtual environment in your
current directory.

A major difference of *virtualenv* is that its created environment is autonomous of its
originating interpreter. The virtual environment from *venv* and *pyenv* require
resources from the original interpreter (Pro: they are smaller).

Install dependencies
````````````````````
First, install `pip-tools <https://github.com/jazzband/pip-tools>`_, which we use
to manage our dependencies (activate your project's virtual environment first):

.. code-block:: bash

    (project_venv) $ pip install pip-tools

.. important::

    *pip-tools* must be installed into the project's virtual environment. You must
    not use a pip-tools installation from a different environment (e.g. from a
    *pipx* installation), because ``pip-sync`` installs into the environment it
    is called from.

Run ``pip-compile --version`` and ``pip-sync --version`` to verify the installation success.
All requirements for development as mentioned in the :ref:`overview table <project_dev_packages_overview>`
are already listed in ``requirements-dev.in``. To create a ``requirements-dev.txt``,
execute:

.. code-block:: bash

    (project_venv) $ pip-compile requirements-dev.in -o requirements-dev.txt

This produces the \*.txt file containing our dependencies plus all required
packages for those dependencies (all using pinned versions). To install all these
dependencies, execute:

.. code-block:: bash

    (project_venv) $ pip-sync requirements-dev.txt

.. hint::

    All dependencies which are required to **execute** our project are gathered
    in ``requirements.in``. Same workflow here:

    .. code-block:: bash

        (project_venv) $ pip-compile requirements.in -o requirements.txt
        (project_venv) $ pip-sync requirements.txt

.. footbibliography::