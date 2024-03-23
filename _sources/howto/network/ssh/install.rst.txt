Installation
------------
Windows
```````
There is no SSH connection tool preinstalled on Windows, but a Windows binary for the OpenSSH tool,
the popular SSH tool on many Linux distributions is also available (although it might be one or two
versions behind the Linux build).

#. Download the latest OpenSSH for Windows from https://github.com/PowerShell/Win32-OpenSSH/tags.
   (either as \*.msi or zip-archive).
#. Follow installation instructions on
   https://github.com/PowerShell/Win32-OpenSSH/wiki/Install-Win32-OpenSSH.

    .. hint::

        Alternatively, you may install OpenSSH via `winget`_:

        .. prompt:: batch

            winget install "openssh beta"

.. _winget: https://learn.microsoft.com/en-us/windows/package-manager/winget/

Linux
`````
OpenSSH is pre-installed on many Linux distributions. To check that, open a shell windows
and run

.. prompt:: bash

    ssh -V

which prints the version of OpenSSH, if installed. If the command is not recognized, you probably
need to install an SSH tool. To install OpenSSH, use the package manager (e.g. apt on Ubuntu based Linux):

.. prompt:: bash

    sudo apt install openssh-client
    sudo apt install openssh-server

.. note::

    OpenSSH provides two installations, one for the Client, one for the server.
    If you only need to onto another PC, the ``openssh-client`` suffices. But if
    you also want other systems to connect onto your machine, you will also need
    the ``openssh-server``.

As always, consider upgrading your OpenSSH version:

.. prompt:: bash

    sudo apt upgrade openssh-client
    sudo apt upgrade openssh-server

macOS
`````
As on Linux, macOS comes with a preinstalled version of OpenSSH, although it might
not be the latest version of it (check via ``ssh -V``).

In case, you want to update to a later versions (or, for some reasons, don't have OpenSSH
installed), best use `homebrew`_:

#. Install Homebrew.
#. Install OpenSSH (also installs OpenSSL, which is a precondition):

    .. prompt:: bash

        brew install openssh

.. hint::

    To update your OpenSSH version, run:

    .. prompt:: bash

        brew upgrade openssh

.. hint::

    It may be, that remote login via SSH or SFTP is deactivated in the system
    settings. Make sure it is activated.

    #. Go to :menuselection:`System Settings --> General --> Sharing --> Advanced`
    #. Make sure the :guilabel:`Remote Login` option is active.
    #. Also select the :unicode-guilabel:`&#128712;` icon and see if the remote login is
       not limited to certain users.

.. _homebrew: https://brew.sh/
