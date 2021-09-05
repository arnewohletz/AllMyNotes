Install Python on Ubuntu Linux
==============================
.. note::

    There is no installer for Python on Linux, but the source code must be compiled locally.
    Python can also be installed via ``sudo apt-get python``, but usually does not install
    the latest version.

.. _linux_install_python_from_source:

Install from sources at python.org
----------------------------------
#. Run these commands to make sure, all packages required for building Python from sources
   is available on the local system:

    .. prompt:: bash

        sudo apt-get update
        sudo apt-get install build-essential
        sudo apt-get install libncurses5-dev libncursesw5-dev libgdbm-dev libc6-dev
        sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
        sudo apt-get install libssl-dev openssl python-openssl
        sudo apt-get install libffi-dev wget
        sudo apt-get install libbz2-dev libreadline-dev llvm xz-utils liblzma-dev

#. Open https://www.python.org, select *Downloads / Source code* and select *Download
   XZ compressed source tarball* of the version you like to install

    .. hint::

        Alternatively, you may download the file to the current directory via

        .. prompt:: bash

            wget https://www.python.org/ftp/python/<version>/Python-<version>.tgz

        where <version> is the Python version, you want to install (e.g. 3.9.4)

#. Extract the archive:

    .. prompt:: bash

        tar xzf Python-<version>.tgz

#. Create system dependent Makefile and other dependencies:

    .. prompt:: bash

        cd Python-<version>
        sudo ./configure --enable-optimizations

#. After completion, run the installation (using alternative-installation to allow us install
   additional Python versions, as Ubuntu has a system default installed):

    .. prompt:: bash

        sudo make altinstall

#. Python binaries now reside in the ``/usr/local/bin/`` directory, library files
   reside in ``/usr/local/lib/``.
#. Try, if the Python installation is referenced by the ``python3`` command (it should
   have been set as default Python interpreter).
#. Delete or archive downloaded archive and unzipped directory.

Uninstall a Python version
--------------------------
Prerequisites
`````````````
* Python has to be installed according to :ref:`upper description <linux_install_python_from_source>`
* Python installation files reside on system (may need to re-download and configure)

Steps
`````
#. Navigate into the installation files directory (e.g. ``~/Downloads/Python-<x.x.x>``).
#. Run

    .. prompt:: bash

        sudo make uninstall

Install and manage multiple Python version
------------------------------------------
Installing various minor version (e.g. 3.6, 3.7, 3.8 and 3.9) in parallel is possible,
but your ``python3`` command will always refer to a particular Python version, likely
the one you installed last.

The out-of-the-box solution is to use the version-specific executable like ``python3.9`` for
your Python 3.9 installation or ``python2.7`` for the Python 2.7 installation.

Additionally, Ubuntu already has a version Python 2 and Python 3 preinstalled on its system by default,
which are not responding to any ``python``, ``python2``or ``python3`` or even the more specific
``python<x.x>`` commands, once you installed your own versions.

Assigning multiple versions as alternatives for any of these commands and switch the installation
to be used for it can be achieved by using the `updates-alternatives`_ command.

#. Add the system installations as alternative (here: 3.8 and 2.7):

    .. prompt:: bash

        sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
        sudo update-alternatives --install /usr/bin/python2 python2 /usr/bin/python2.7 1

#. Add the user installed installations as alternative (here: 2.7, 3.6, 3.7, 3.8 and 3.9):

    .. prompt:: bash

        sudo update-alternatives --install /usr/local/bin/python2.7 python2 /usr/local/bin/python2.7 2
        sudo update-alternatives --install /usr/local/bin/python3.6 python3 /usr/local/bin/python3.6 2
        sudo update-alternatives --install /usr/local/bin/python3.7 python3 /usr/local/bin/python3.7 2
        sudo update-alternatives --install /usr/local/bin/python3.8 python3 /usr/local/bin/python3.8 2
        sudo update-alternatives --install /usr/local/bin/python3.9 python3 /usr/local/bin/python3.9 2

    .. hint::

        You may also define alternative for the general ``python`` command, by stating ``python`` instead
        of ``python3`` in the above commands.

.. _updates-alternatives: https://linux.die.net/man/8/update-alternatives

Install and manage Python version with pyenv
--------------------------------------------
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

Install pyenv on macOS
``````````````````````
The recommended way to install pyenv on macOS is via `Homebrew`_:

.. prompt:: bash

    brew install pyenv

Also, install the extension *pyenv-virtualenv*:

.. prompt:: bash

    brew install pyenv-virtualenv

.. TODO: Add missing bash profile setting and similar stuff

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

.. _Homebrew: https://brew.sh/
.. _mentioned on python.org: https://www.python.org/download/mac/tcltk/