Linux: Install Python on Ubuntu
===============================
.. note::

    There is no installer for Python on Linux, but the source code must be compiled locally.
    Python can also be installed via ``sudo apt-get python``, but usually does not install
    the latest version.

.. _linux_install_python_from_source:

Manual install from sources
---------------------------
#. Run these commands to make sure, all packages required for building Python from sources
   is available on the local system:

    .. code-block:: bash

        $ sudo apt-get update
        $ sudo apt-get install build-essential
        $ sudo apt-get install libncurses5-dev libncursesw5-dev libgdbm-dev libc6-dev
        $ sudo apt-get install zlib1g-dev libsqlite3-dev tk-dev
        $ sudo apt-get install libssl-dev openssl python-openssl
        $ sudo apt-get install libffi-dev wget
        $ sudo apt-get install libbz2-dev libreadline-dev llvm xz-utils liblzma-dev

#. Open https://www.python.org, select *Downloads / Source code* and select *Download
   XZ compressed source tarball* of the version you like to install

    .. hint::

        Alternatively, you may download the file to the current directory via

        .. code-block:: bash

            $ wget https://www.python.org/ftp/python/<version>/Python-<version>.tgz

        where <version> is the Python version, you want to install (e.g. 3.9.4)

#. Extract the archive:

    .. code-block:: bash

        $ tar xzf Python-<version>.tgz

#. Create system dependent Makefile and other dependencies:

    .. code-block:: bash

        $ cd Python-<version>
        $ sudo ./configure --enable-optimizations

#. After completion, run the installation (using alternative-installation to allow us install
   additional Python versions, as Ubuntu has a system default installed):

    .. code-block:: bash

        $ sudo make altinstall

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

    .. code-block:: bash

        $ sudo make uninstall

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

    .. code-block:: bash

        $ sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1
        $ sudo update-alternatives --install /usr/bin/python2 python2 /usr/bin/python2.7 1

#. Add the user installed installations as alternative (here: 2.7, 3.6, 3.7, 3.8 and 3.9):

    .. code-block:: bash

        $ sudo update-alternatives --install /usr/local/bin/python2.7 python2 /usr/local/bin/python2.7 2
        $ sudo update-alternatives --install /usr/local/bin/python3.6 python3 /usr/local/bin/python3.6 2
        $ sudo update-alternatives --install /usr/local/bin/python3.7 python3 /usr/local/bin/python3.7 2
        $ sudo update-alternatives --install /usr/local/bin/python3.8 python3 /usr/local/bin/python3.8 2
        $ sudo update-alternatives --install /usr/local/bin/python3.9 python3 /usr/local/bin/python3.9 2

    .. hint::

        You may also define alternative for the general ``python`` command, by stating ``python`` instead
        of ``python3`` in the above commands.

.. _updates-alternatives: https://linux.die.net/man/8/update-alternatives
