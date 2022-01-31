SSH
===
.. important::

    SSH directories are commonly hidden. Make sure to enable visibility on hidden folders in your file explorer.

    Windows: In Explorer, select the *View* pane and check *Hidden items*
    Linux (Ubuntu): In File Manager, select *View / Show Hidden Files*
    macOS: In Finder, hit :kbd:`Shift+Cmd+.` to show/hide hidden directories and files.

Installation
------------
Windows
```````
There is no SSH connection tool preinstalled on Windows, but a Windows binary for the OpenSSH tool,
the popular SSH tool on many Linux distributions is also available (although it might be one or two
versions behind the Linux build).

#. Download the latest OpenSSH for Windows from https://github.com/PowerShell/Win32-OpenSSH/tags.
#. Follow installation instructions on
   https://github.com/PowerShell/Win32-OpenSSH/wiki/Install-Win32-OpenSSH.

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

To update your OpenSSH version, simply run:

.. prompt:: bash

    brew upgrade openssh

.. _homebrew: https://brew.sh/index_de

How to use keys for authentication
----------------------------------
It is recommended to handle authentication of SSH connections via keys, instead of a password.
Most of the steps only need to be executed on the server machine.

Server & Client: Create key pair
````````````````````````````````
Execute these steps **on both the client and the server**.

#. Create a new directory ``C:\Users\%USERNAME%\.ssh`` (Windows) or ``~/.ssh`` (Linux/macOS,
   where it should already exist).
#. Within it, create two new empty file named ``authorized_keys`` and ``config``.
#. Start the Key Generator via the command line (Windows) or shell (Linux/macOS)

    .. prompt:: bash

        ssh-keygen

#. Set the path and filename of the keys (default: ~/.ssh/id_rsa).
   In case, you don't need separate keys pairs for different connections, you don't need to
   specify a custom path or filename.
#. Enter a passphrase to encrypt the private key, if needed (more secure, but might conflict with
   applications using the key).
#. Check if the .ssh directory contains both the private and the public key file (\*.pub).

Server: Set permissions
```````````````````````
To prevent the authentication keys from being manipulated, only the respective user must
be able to interact with them.

.. hint::

    The commands are used on Linux/macOS only. See here, how to permissions on Windows:
    https://www.howtogeek.com/301768/how-to-take-ownership-of-files-and-folders-in-windows/

#. **Linux/macOS only**: Make sure, your home directory is only writable by the respective user:

    .. prompt:: bash

        ls -l /home
        ls -l /Users

    should output ``drwxr-xr-x`` for the user's directory.

    If not, execute:

        .. prompt:: bash

            chmod 755 ~/

#. It is important that ``$HOME/.ssh`` (``%USERPROFILE%\.ssh`` on Windows) and the ``authorized_keys``
   file have the correct permissions and owner:

       * ``$USERPROFILE$\.ssh`` must be owned by the user
       * ``$USERPROFILE$\.ssh`` must only be writable, readable and executable by the owner
       * ``authorized_keys`` must be owned by the user
       * ``authorized_keys`` must only be writable and readable by the owner

    .. prompt:: bash

        chown $USER ~/.ssh
        chown $USER ~/.ssh/authorized_keys
        chown $USER ~/.ssh/config

    .. prompt:: bash

        chmod 700 ~/.ssh
        chmod 600 ~/.ssh/authorized_keys
        chmod 600 ~/.ssh/config

#. The private key must also be protected (here: id_rsa):

    .. prompt:: bash

        chmod 700 ~/.ssh/id_rsa

Server: Set-up key authentication
`````````````````````````````````
#. Add your private key to the authentication agent (it will handle the authorizations via keys):

    .. prompt:: bash

        ssh-add

    .. hint::

        In case you are using a private key using a different name and/or path, you must pass it:

        .. prompt:: bash

            ssh-add /path/to/custom_private_key_file

#. On the **client**, open the public key file (e.g. id_rsa.pub) and copy the entire content into the
   ``authorized_keys`` file on the **server** (should be a single line starting with *ssh-rsa* and ending
   with *<username>@<hostname>*). Save and close both files.

    .. important::

        The public key of **each** client, that wants to authorize itself, needs to be added into a
        separate line within the server's ``authorized_keys`` file. Each time, this file is edited,
        the SSH server must be restarted.

#. Open the OpenSSH config file in a text editor:

    * Windows: ``C:\ProgramData\ssh\sshd_config``
    * Linux: ``/etc/ssh/ssh_config``
    * macOS: ``/private/etc/ssh/sshd_config``

#. Change the following content:

    .. code-block:: none

        RSAAuthentication yes
        PubkeyAuthentication yes
        AuthorizedKeysFile .ssh\authorized_keys

    .. important::

        Don't disable the password authentication (``PasswordAuthentication``) until the
        key authentication has been proven to work.

#. **Windows only**: Make sure, the following content is commented out (starts with #):

    .. code-block:: none

        # Match Group administrators
        # AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys

#. Save and close the file.
#. Restart the SSH Server.

    Windows:

        #. Type :kbd:`Windows+R`, type ``services.msc`` and confirm to open the service manager.
        #. Right-click the service and select *Restart*.
        #. Ensure that the ``OpenSSH SSH Server`` service's startup type is set to *Automatic*
           (right click service and choose ``Properties`` to edit).

    Linux:

        .. prompt:: bash

            service ssh restart

    macOS:

        If using Homebrew installation:

        .. prompt:: bash

            brew services start ssh

        If using preinstalled SSH:

        .. prompt:: bash

            sudo launchctl stop com.openssh.sshd
            sudo launchctl start com.openssh.sshd

Client: Set-up key authentication
`````````````````````````````````
#. Open the ``config`` file inside the ``.ssh`` directory.
#. Insert the following content (adapt path to private key file a.k.a. Identity file, if necessary):

    On Windows (adapt USERNAME):

    .. code-block:: none

        Host *
          IdentityFile C:\Users\<USERNAME>\.ssh/id_rsa

    On Linux/macOS:

    .. code-block:: none

        Host *
          IdentityFile ~/.ssh/id_rsa

    This enables the client to use its private key file as an identity to authenticate
    towards the server.

Test key authentication
```````````````````````
Connect to the server (using the server username):

    .. prompt:: bash

        ssh <HOST_USERNAME>@<HOST>

The connection should be established without asking for the password, stating that
the public key was used for authentication.

If the connection is not successful, check the log output, by running the connection in
verbose mode:

    .. prompt:: bash

        ssh <HOST_USERNAME>@<HOST> -v
