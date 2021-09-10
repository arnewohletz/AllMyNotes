SSH
===
How to use custom private key for authentication
------------------------------------------------
Preconditions
`````````````
    * A key pair has been created (e.g. via ``ssh-keygen``)
    * Key pair either has a different name as ``ìd_rsa``, ``id_dsa``, ``id_ecdsa``,
      ``id_ed25519`` or ``id_xmss`` (default names for different encryption methods) or
      is located at a different location as ``C:\<Username>\.ssh`` or ``/home/<username>/.ssh``

Steps
`````
#. On the *Client* machine go to ``C:\<Username>\.ssh`` or ``/home/<username>/.ssh``.
#. Create a new file called ``config`` and only give creator read and write access:

    .. prompt:: bash

        chmod 600 ~/.ssh/config

#. Inside the file add the following content:

    .. code-block:: none

        Host *
          IdentityFile </path/to/my/id_rsa_file>

    .. attention::

        The path should point to the private key file, not the public key file.

#. Try to establish a connection via as usual:

    .. prompt:: bash

        ssh <user>@<host>

Install and setup OpenSSH
-------------------------
Both the *Client* (the machine from which you want to connect) as well as the *Server* (the machine
you want to connect to, need to have OpenSSH installed.

#. Windows only:

    * Download the latest OpenSSH for Windows from https://github.com/PowerShell/Win32-OpenSSH/tags.
    * Follow installation instructions on https://github.com/PowerShell/Win32-OpenSSH/wiki/Install-Win32-OpenSSH.

    .. hint::

        OpenSSH should be preinstalled on macOS and Linux. Check via ``ssh -V``to see the version.
        Consider upgrading, if version is old.

        On macOS, it is recommended to use Homebrew for updating ssh (requires OpenSSL):

            .. prompt:: bash

                brew install openssl
                brew install openssh --with-brewed-openssl

        On Linux, OpenSSH should be upgradable via you package manager (e.g. ``apt``), for example:

            .. prompt:: bash

                sudo apt-get upgrade ssh

#. Create a new directory ``C:\Users\<username>\.shh`` (Windows) or ``/home/<username>/.ssh`` if not existing.
#. Within it, create a new file ``authorized_keys`` (if not existing).
#. Open ``authorized_keys`` and insert the following content (all in one line):
   ```
   ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDnLaeMV3tqiF0IKq3HbdzI4tgMUEmtGpb0fKNCU0LSOGzIrM8vq72pymcl29Lob6vxjqw6/UdeQWZXby+5OVAQzaOS2ptmpxVHssfMducXXmf4pNkIV2VvVYoz4NSsU/BGXahSuFkZGAUxkn3zu3bSDKkYs39PGxSjLgyzuLa1029dY+Atw7rLcwwuwDM/6fUEadrFoh382ElRkdZjue+ioAX6GBTlBDqyyv55QA/vpZyHCJhBGc4CNZnQDFAx3fZ/AMuPNV/PzVT11HzviBsm1bkjw/jVI3gF9B7JadaA7ED9YeO73c1b213mK+aul/TvWiOugXkhGpu0MtauNP4rYU2Qx6EgpyIYrnBFkFiF0kUQcpm8CnkDdS66pEjft9TtEkzXl9SdtyvP5jRe/z9VvJZTP9xohYo4vrSaDdXc24we0nhaZzP9a8nPnUMwX2DW4VCmnLVgVQhCQ5vWbR5iDdzxoOKvNFAKP+iR6MbNVxonlMEu1HAdxxH8TFtRVgWxOBSyo27NTMn7e84FExDJIZ1l0V7c+JghNpdL7aMZvNZabyHSpIm5UDf532JfVnpeI7gE2Dvfo92ymdR7fFD9hyr0N3YlgxE3Qd33Hk/PXtfEOL2yVP20E8R9/gRWtt4N3IkzTI7f08e96LqKRO/LBCwnGGytMIO3F7toeJkD5w== nuance@ulm-ntg7-lbui08
   ```
6. Save and close the file.
7. It is important that ``$USERPROFILE$\.ssh`` and ``authorized_keys`` have the correct permissions and owner
   * ``$USERPROFILE$\.ssh`` must be owned by you (%USERNAME%)
   * ``$USERPROFILE$\.ssh`` must only be writable, readable, executable by the owner (``700`` in Linux)
   * ``authorized_keys`` must be owned by you /%USERNAME%)
   * ``authorized_keys`` must only be writable and readable by the owner (``600`` in Linux)
   * See here, how to adapt these in Windows: https://www.howtogeek.com/301768/how-to-take-ownership-of-files-and-folders-in-windows/
8. Run ``Windows+R``, type ``services.msc`` and confirm to open the service manager.
9. Ensure that the ``OpenSSH SSH Server`` service is executed and startup type is set to automatic
   (right click service and choose ``Properties`` to edit).
10. Open ``C:\ProgramData\ssh\sshd_config`` in a text editor (ProgramData is a hidden folder.
    Enable it by opening the *View* pane in File Explorer and check *Hidden items*).
11. To enable authorization via ``authorized_keys``, comment out (put ``#`` in front) these lines:
    ````
    # Match Group administrators
    # AuthorizedKeysFile __PROGRAMDATA__/ssh/administrators_authorized_keys
    ````
12. To allow access via RSA keys, adapt the line (and uncomment, if needed):
    ````
    PubKeyAuthentication yes
    ````
13. Additionally, you may disable the authentication via password. Beware, that this enforces
    any computer to have a valid key pair to connect to the ET-Framework laptop:
    ````
    PasswordAuthentication no
    ````
14. Save and close the file, then restart OpenSSH via the service manager.