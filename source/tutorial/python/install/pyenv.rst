.. _install_pyenv:

Install and manage Python versions with pyenv
---------------------------------------------
As a alternative, the tool `pyenv <https://github.com/pyenv/pyenv>`_ is able to install and manage multiple Python versions.
It also features an extension called `pyenv-virtualenv <https://github.com/pyenv/pyenv-virtualenv>`_ which is able to manage
virtual environments deriving from any Python installation of pyenv.

Install pyenv on Linux
``````````````````````
The easiest way to install is by using the `pyenv-installer <https://github.com/pyenv/pyenv-installer>`_ script,
which also installs the *pyenv-virtualenv* extension.

#. Run the command

    .. prompt:: bash

        curl https://pyenv.run | bash

#. To make ``pyenv`` available append this content to ``~/.profile``::

    # pyenv
    export PYENV_ROOT="$HOME/.pyenv"
    export PATH="$PYENV_ROOT/bin:$PATH"
    eval "$(pyenv init --path)"

#. Also add these lines to to the bottom of ``~/.bashrc``::

    # pyenv
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

#. Apply both files by typing:

    .. prompt:: bash

        source ~/.profile
        source ~/.bashrc

#. Log off from your user profile and login again, then try to run ``pyenv``.

    .. warning::

        Before installing any Python versions, make sure the required build libraries are installed. Run:

        .. prompt:: bash

            sudo apt-get update; sudo apt-get install make build-essential libssl-dev zlib1g-dev \
            libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
            libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

#. To update pyenv, simply run:

    .. prompt:: bash

        pyenv update

Install pyenv on macOS
``````````````````````
The recommended way to install pyenv on macOS is via `Homebrew`_:

.. prompt:: bash

    brew install pyenv

Also, install the extension *pyenv-virtualenv*:

.. prompt:: bash

    brew install pyenv-virtualenv

.. TODO: Add missing bash profile setting and similar stuff

Same as on Linux, add the auto-initializing commands to your ``~/.zshrc`` file:

.. code-block:: none

    # pyenv
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)"

Afterwards, start a new shell.

Before installing any Python interpreters
'''''''''''''''''''''''''''''''''''''''''
xz
**
Some Python modules, like `pandas`_, require the data compression package which
supports the `lzma`_ compression algorithm. If this isn't preinstalled on your system
(not preinstalled on macOS), it will not be built into Python when building it.

Pandas for instance will prompt such error message, when using the module in environments without
the module:

.. code-block:: none

    UserWarning: Could not import the lzma module. Your installed Python is incomplete.
    Attempting to use lzma compression will result in a RuntimeError.

Install the `xz`_ formulaee via Homebrew, which contains these dependencies:

.. prompt:: bash

    brew install xz

Now go ahead and install your desired Python interpreter.

.. _pandas: https://pandas.pydata.org/
.. _lzma: https://en.wikipedia.org/wiki/Lempel%E2%80%93Ziv%E2%80%93Markov_chain_algorithm
.. _xz: https://formulae.brew.sh/formula/xz

Tcl/Tk
******
Before installing any `CPython <https://en.wikipedia.org/wiki/CPython>`_ version, you will need
to install a newer version of Tcl/Tk on your system. As `mentioned on python.org`_, macOS as of now
does not provide a safe and recent version of the GUI framework. Since *pyenv* builds Python distributions
from source and does not include a later version of Tcl/Tk with it, as the regular installers from python.org do,
it uses the preinstalled version from the OS.

First install the latest Tcl/Tk version:

.. prompt:: bash

    brew install tcl-tk

Open the python-build script of pyenv and point it towards the newly installed Tcl/Tk installation.

.. prompt:: bash

    nano /usr/local/Cellar/pyenv/<version>/plugins/python-build/bin/python-build

Find the line::

    $CONFIGURE_OPTS ${!PACKAGE_CONFIGURE_OPTS} "${!PACKAGE_CONFIGURE_OPTS_ARRAY}" || return 1

and replace it with::

    $CONFIGURE_OPTS --with-tcltk-includes='-I/usr/local/opt/tcl-tk/include' --with-tcltk-libs='-L/usr/local/opt/tcl-tk/lib -ltcl8.6 -ltk8.6' ${!PACKAGE_CONFIGURE_OPTS} "${!PACKAGE_CONFIGURE_OPTS_ARRAY}" || return 1

Any new CPython version installed via ``pyenv install`` should now utilize your Tcl/Tk installation.

.. important::

    If *pyenv* is updated to a newer version, the ``python-build`` script needs to be edited again,
    while navigating to the new <version> directory.

.. _Homebrew: https://brew.sh/
.. _mentioned on python.org: https://www.python.org/download/mac/tcltk/