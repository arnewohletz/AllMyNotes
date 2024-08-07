Set up key authentication
-------------------------
It's recommended to handle authentication of SSH connections via keys, instead of a password.
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

    .. code-block:: bash

        $ ssh-keygen -t ed25519

    .. hint::

        To customize the key pair even further you may also run

        .. tabs::
            .. group-tab:: macOS

                .. code-block:: bash

                    $ ssh-keygen -t ed25519 -C "$USER@$(scutil --get LocalHostName) - `date +%Y%m%d`"

            .. group-tab:: Linux

                .. code-block:: bash

                    $ ssh-keygen -t ed25519 -C "$USER@$HOSTNAME - `date +%Y%m%d`"

            .. group-tab:: Windows

                Run in git bash (comes with `Git for Windows`_):

                .. code-block:: bash

                    $ ssh-keygen -t ed25519 -C "$USERNAME@$COMPUTERNAME - `date +%Y%m%d`"

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

.. _Git for Windows: https://gitforwindows.org/

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

    .. code-block:: powershell

        PS C:\> powershell.exe -ExecutionPolicy Bypass -File .\FixHostFilePermissions.ps1

#. **Linux/macOS only**: Make sure, your home directory is only writable by the respective user:

    .. code-block:: bash

        $ ls -l /home
        $ ls -l /Users

    should output ``drwxr-xr-x`` for the user's directory.

    If not, execute:

        .. code-block:: bash

            $ chmod 755 ~/

#. It is important that ``$HOME/.ssh`` (``%USERPROFILE%\.ssh`` on Windows) and the ``authorized_keys``
   file have the correct permissions and owner:

       * ``$USERPROFILE$\.ssh`` must be owned by the user
       * ``$USERPROFILE$\.ssh`` must only be writable, readable and executable by the owner
       * ``authorized_keys`` must be owned by the user
       * ``authorized_keys`` must only be writable and readable by the owner

    .. code-block:: bash bash

        $ chown $USER ~/.ssh
        $ chown $USER ~/.ssh/authorized_keys
        $ chown $USER ~/.ssh/config

    .. code-block:: bash bash

        $ chmod 700 ~/.ssh
        $ chmod 600 ~/.ssh/authorized_keys
        $ chmod 600 ~/.ssh/config

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

    .. code-block:: powershell

        PS C:\> powershell.exe -ExecutionPolicy Bypass -File .\FixUserFilePermissions.ps1

OpenSSH does not allow the key pair files to be editable by anyone except the owner.
The private key must also be protected (here: id_ed25519):

    .. code-block:: bash bash

        $ chmod 700 ~/.ssh/id_ed25519
        $ chmod 700 ~/.ssh/id_ed25519.pub

Server: Set-up key authentication
`````````````````````````````````
#. Add your private key to the authentication agent (it will handle the authorizations via keys):

    .. code-block:: bash bash

        $ ssh-add

    .. hint::

        * In case you received the message

            .. code-block:: none

                Could not open a connection to your authentication agent.

            start the *ssh-agent* via

            .. code-block:: bash

                eval `ssh-agent -s`

          To autostart the ssh-agent add this content to your ``~/.bashrc`` or
          ``~/.zshrc`` file:

            .. code-block:: none

                # auto-start ssh-agent
                if [ ! -S ~/.ssh/ssh_auth_dock ]; then
                    eval `ssh-agent` >/dev/null
                    ln -sf "$SSH_AUTH_DOCK" ~/.ssh/ssh_auth_sock
                fi
                export SSH_AUTH_SOCK=~/.ssh/ssh_auth_sock
                ssh-add -l >/dev/null || ssh-add


        In case you are using a private key using a different name and/or path, you must pass it:

        .. code-block:: bash

            $ ssh-add /path/to/custom_private_key_file

#. On the **client**, open the public key file (e.g. id_ed25519.pub) and copy the entire content into the
   ``authorized_keys`` file on the **server** (should be a single line starting with *ssh-rsa* and ending
   with *<username>@<hostname>*). Save and close both files.

    .. important::

        The public key of **each** client, that wants to authorize itself, needs to be added into a
        separate line within the server's ``authorized_keys`` file. Each time, this file is edited,
        the SSH server must be restarted.

        This can also be done from the client via:

        .. code-block:: bash

            $ ssh-copy-id -i ~/.ssh/id_ed25519.pub <HOST_USERNAME>@<HOST>

#. Open the OpenSSH config file in a text editor:

    * Windows: ``C:\ProgramData\ssh\sshd_config``
    * Linux: ``/etc/ssh/sshd_config``
    * macOS: ``/private/etc/ssh/sshd_config``

#. Change the following content:

    .. code-block:: none

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

        .. code-block:: bash

            $ service ssh restart

    **macOS:**

        If using Homebrew installation:

        .. code-block:: bash

            $ brew services start ssh

        If using preinstalled SSH:

        .. code-block:: bash

            $ sudo launchctl stop com.openssh.sshd
            $ sudo launchctl start com.openssh.sshd

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

    .. code-block:: bash

        $ ssh <HOST_USERNAME>@<HOST>

The connection should be established without asking for the password, stating that
the public key was used for authentication.

If the connection is not successful, check the log output, by running the connection in
verbose mode:

    .. code-block:: bash

        $ ssh <HOST_USERNAME>@<HOST> -v

Configure connections
---------------------
This is a convenience feature. Right now, connecting to a host system is done, for example,
like this:

.. code-block:: bash

    $ ssh -i ~/.ssh/all_my_keys/imac.ed25519.pub someuser@some.host.system

To shorten this you may create a config file to store all these parameters.

#. On the client machine, create the config file in your ``.ssh`` directory
   (if not already present):

    .. code-block:: bash

        $ touch ~/.ssh/config

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

        .. code-block:: bash

            $ man ssh_config

#. Save and close the file.
#. You may connect to a specified host system by only stating its name:

    .. code-block:: bash

        $ ssh imac

.. hint::

    To list all configured hosts, specify this command under an alias in your
    ``~/.bashrc`` or ``~/.zshrc`` file:

    .. code-block:: none

        alias ssh-hosts="cat ~/.ssh/config | grep -E '^\s*Host\s' | awk '{print $2}'"

    When running ``ssh-hosts`` in a new shell, it will print all configured hosts.

    On Windows create a Batch script in a folder defined in your PATH variable,
    for example ``ssh-hosts.bat`` and insert the following content:

    .. code-block:: none

        @echo off
        type %USERPROFILE%\.ssh\config | findstr /R "^Host "
