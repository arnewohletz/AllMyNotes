SSH
===
.. important::

    SSH directories are commonly hidden. Make sure to enable visibility on hidden folders in your file explorer.

    * Windows: In Explorer, select the *View* pane and check *Hidden items*
    * Linux (Ubuntu): In File Manager, select *View / Show Hidden Files*
    * macOS: In Finder, hit :kbd:`Shift` + :kbd:`Cmd` + :kbd:`.` to show/hide hidden
      directories and files.

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

.. _homebrew: https://brew.sh/

How to use keys for authentication
----------------------------------
It is recommended to handle authentication of SSH connections via keys, instead of a password.
Most of the steps only need to be executed on the server machine.

Prerequisites
`````````````
**Client & Server**:

#. Create a new directory ``C:\Users\%USERNAME%\.ssh`` (Windows) or ``~/.ssh`` (Linux/macOS,
   where it should already exist).
#. Within it, create these empty files (no suffix):

    * ``config``
    * **Server only**: ``authorized_keys``

Server & Client: Create key pair
````````````````````````````````
#. Start the Key Generator via the command line (Windows) or shell (Linux/macOS)

    .. prompt:: bash

        ssh-keygen -t ed25519

#. Set the path and filename of the keys (default: ~/.ssh/id_ed25519).
   In case, you don't need separate keys pairs for different connections, you don't need to
   specify a custom path or filename.

    .. warning::

        I experienced errors from the server upon connection, stating the clients private key
        contains an invalid format::

            Load key "/Users/arnewohletz/.ssh/imac_ed25519.pub": invalid format

        This issue was resolved by not defining a custom named key pair (like ``imac_ed25519``
        in the example above), but using the default name (here: ``id_ed25519``).

#. Enter a passphrase to encrypt the private key, if needed (more secure, but might conflict with
   applications using the key).
#. Check if the ``.ssh`` directory contains both the private and the public key file (\*.pub).
#. If you used a custom name for the key pair or stored the files at a separate location, add the
   private key to the authentication agent (otherwise you'd need to state your public key when
   attempting an SSH connection, like ``ssh -i /path/to/my/key.pub USER@HOST``):

    .. prompt:: bash

        ssh-add /path/to/private_key

Server: Set permissions
```````````````````````
To prevent the authentication keys from being manipulated, only the respective user must
be able to interact with them.

.. hint::

    The commands are used on Linux/macOS only. See here, how to permissions on Windows:
    https://www.howtogeek.com/301768/how-to-take-ownership-of-files-and-folders-in-windows/

    On Windows, it is highly recommended to use the included PowerShell scripts to check or
    set the proper access rights. Open a PowerShell instance as administrator, navigate
    to the OpenSSH directory and run:

    .. prompt:: powershell

        powershell.exe -ExecutionPolicy Bypass -File .\FixHostFilePermissions.ps1

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

Client: Set permissions
```````````````````````
Same as for the server, each connecting client needs to set the correct permissions for
the key pair. OpenSSH is very sensitive here and does not hint you to wrong permissions,
when trying to establish a connection, so always make sure, those are set correctly.

.. hint::

    The commands are used on Linux/macOS only. See here, how to permissions on Windows:
    https://www.howtogeek.com/301768/how-to-take-ownership-of-files-and-folders-in-windows/

    On Windows, it is highly recommended to use the included PowerShell scripts to check or
    set the proper access rights. Open a PowerShell instance as administrator, navigate
    to the OpenSSH directory and run:

    .. prompt:: powershell

        powershell.exe -ExecutionPolicy Bypass -File .\FixUserFilePermissions.ps1

OpenSSH does not allow the key pair files to be editable by anyone except the owner.
The private key must also be protected (here: id_ed25519):

    .. prompt:: bash

        chmod 700 ~/.ssh/id_ed25519
        chmod 700 ~/.ssh/id_ed25519.pub

Server: Set-up key authentication
`````````````````````````````````
#. Add your private key to the authentication agent (it will handle the authorizations via keys):

    .. prompt:: bash

        ssh-add

    .. hint::

        In case you are using a private key using a different name and/or path, you must pass it:

        .. prompt:: bash

            ssh-add /path/to/custom_private_key_file

#. On the **client**, open the public key file (e.g. id_ed25519.pub) and copy the entire content into the
   ``authorized_keys`` file on the **server** (should be a single line starting with *ssh-rsa* and ending
   with *<username>@<hostname>*). Save and close both files.

    .. important::

        The public key of **each** client, that wants to authorize itself, needs to be added into a
        separate line within the server's ``authorized_keys`` file. Each time, this file is edited,
        the SSH server must be restarted.

        This can also be done from the client via:

        .. prompt:: bash

            ssh-copy-id -i ~/.ssh/id_ed25519.pub <HOST_USERNAME>@<HOST>

#. Open the OpenSSH config file in a text editor:

    * Windows: ``C:\ProgramData\ssh\sshd_config``
    * Linux: ``/etc/ssh/sshd_config``
    * macOS: ``/private/etc/ssh/sshd_config``

#. Change the following content:

    .. code-block:: none

        RSAAuthentication yes
        PubkeyAuthentication yes
        AuthorizedKeysFile .ssh/authorized_keys

    .. important::

        Don't disable the password authentication (``PasswordAuthentication``) until the
        key authentication has been proven to work.

#. **Windows only**: Make sure, the following content is commented out (starts with #):

    .. code-block:: none

        # Match Group administrators
        # AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys

#. Save and close the file.
#. Restart the SSH Server.

    **Windows:**

        #. Type :kbd:`Windows+R`, type ``services.msc`` and confirm to open the service manager.
        #. Right-click the service and select *Restart*.
        #. Ensure that the ``OpenSSH SSH Server`` service's startup type is set to *Automatic*
           (right click service and choose ``Properties`` to edit).

    **Linux:**

        .. prompt:: bash

            service ssh restart

    **macOS:**

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
          IdentityFile C:\Users\<USERNAME>\.ssh/id_ed25519

    On Linux/macOS:

    .. code-block:: none

        Host *
          IdentityFile ~/.ssh/id_ed25519

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

SSH connection config
---------------------
This is a convenience feature. Right now, connecting to a host system is done, for example,
like this:

.. prompt:: bash

    ssh -i ~/.ssh/all_my_keys/imac.ed25519.pub someuser@some.host.system

To shorten this you may create a config file to store all these parameters.

#. Create the config file in your .ssh directory:

    touch ~/.ssh/config

#. Open the file and add your config, for example, like this:

    .. code-block:: none

        Host imac
            HostName imac.fritz.box
            User arnewohletz
            IdentityFile ~/.ssh/id_ed25519

        Host someotherhost
            HostName some.other.host
            User some.user
            IdentityFile ~/.ssh/id_ed25519

    You may specify settings for any number of host systems. Check out all
    possible settings via:

        .. prompt:: bash

            man ssh_config

#. Save and close the file.
#. You may connect to a specified host system by only stating its name:

    .. prompt::

        ssh imac

Set up Proxy Jump
-----------------
The Proxy Jump is a feature introduced in OpenSSH 7.3 and allows connecting to a remote machine
using an intermediate machine. It can be used, if the target machine is only reachable by
the intermediate machine.

.. hint::

    It is recommended to use key authentication to authenticate on the
    machines to save yourself from entering passwords for the connection.

..  rubric:: Prerequisites

* Access over SSH to the intermediate machine
* Intermediate machine has access to target machine

.. rubric:: Steps

To create a proxy jump, execute this command from your shell:

.. prompt:: bash

    ssh -J <user_intermediate>@<ip_or_domain_name_intermediate> <user_target>@<ip_or_domain_name_target>

e.g. :code:`ssh -J testpc@ulm-ntg7-testb1 root@10.120.1.91`

.. hint::

    **Proxy Jump in WinSCP**

    WinSCP also supports connections over a proxy jump. Steps:

    #. Select a new session.
    #. Enter the *Host name* and *User name* of the **target machine**.
    #. Open :menuselection:`Advanced --> Connection --> Tunnel`.
    #. Check *Connect through SSH tunnel*.
    #. Enter *Host name* and *User name* of the **intermediate machine**.
    #. In case key authentication is used to connect to intermediate machine:
       Add path to *Private key file*.
    #. Close settings.

Set up SSH Tunneling :footcite:p:`ssh_tunnel_gentoo`
----------------------------------------------------
As proxy jumping is not supported on older versions of OpenSSH (before v7.3), the SSH
tunnel is another way to connect to a target machine (here, called server) over an
intermediate machine (here, called gateway).

.. hint::

    Older Linux distributions (such as Ubuntu 16.04) are not supporting proxy jumping.

#. Set up the tunnel on you local machine:

    .. prompt:: bash

        ssh -f GATEWAY_USERNAME -L localhost:CPORT:SERVER:SPORT -N

    .. hint::

        When using key authentication towards the gateway machine, execute:

            .. prompt:: bash

                ssh - i /path/to/private/key -f GATEWAY_USERNAME -L localhost:CPORT:SERVER:SPORT -N

#. Create a connection:

    .. prompt:: bash

        ssh -p CPORT SUSERNAME@localhost

:GATEWAY_USERNAME:

    User name on the gateway machine

:GATEWAY:

    IP address or domain name of gateway machine

:CPORT:

    Port number used on Client (should be greater than 1024)

:SERVER:

    IP address or domain name of server machine

:SPORT:

    Port number the SSH server is listening to (default: 22)

:SUSERNAME:

    User name on the server machine

Example:

.. prompt:: bash

    ssh -f testpc@ulm-ntg7-testb1 -L localhost:1025:10.120.1.91:22 -N
    ssh -p 1025 root@localhost

.. footbibliography::