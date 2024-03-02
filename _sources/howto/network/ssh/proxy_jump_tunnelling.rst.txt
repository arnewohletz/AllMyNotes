Set up Proxy Jump
-----------------
The Proxy Jump is a feature introduced in OpenSSH 7.3 and allows connecting to a remote machine
using an intermediate machine. It can be used, if the target machine is only reachable by
the intermediate machine.

.. hint::

    It's recommended to use key authentication to authenticate on the
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