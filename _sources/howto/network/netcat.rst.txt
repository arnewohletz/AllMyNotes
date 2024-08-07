Netcat
======

Check port availability
-----------------------
Use `netcat`_ to get port information (preinstalled on Linux and macOS).

Check if a certain port is available via TCP connection:

.. code-block:: bash

    $ nc -v -z <host_ip> <port>

In case, the port is actively used and open, a success message is reported,
if not, a connection refused message appears.

Same for UDP connection:

.. code-block:: bash

    $ nc -v -z -u <host_ip> <port>

To check for an available port on your local system, run:

.. code-block:: bash

    $ nc -zv <host_ip> <port_from>-<port_until> 2>&1 | grep -m 1 failed

to receive the first unused port within the specified range.

.. hint::

    Don't assign port numbers 1 to 1024 for your services, as `well-known services`_
    reserve those.

.. _netcat: https://nc110.sourceforge.io/
.. _well-known services: https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers#Well-known_ports

.. admonition:: Alternative

    You may also run :download:`open_ports.sh <_file/open_ports.sh>` to receive information on a
    port range (<from_port> until <to_port>):

    .. code-block:: bash

        $ ./open_ports <host_ip> <from_port> <to_port>

Send chat messages between two machines
---------------------------------------
Netcat is able to send simple chat messages between two machines. One machine
acts as the server, other devices can connect to the server as client. All machines
must have netcat installed.

On the server machine, create a netcat instance to listen to a specific port (here: 10001):

.. code-block:: bash

    $ nc -n -v -l 10001

On the client side, create a connection to the specified port on the server (host):

.. code-block:: bash

    $ nc -n -v <server_ip_address> 10001

Now, you may enter a message on either the server or any client machine and all
connection machines will receive the message.


