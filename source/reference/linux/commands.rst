Commands
========

Memory
------
**Check currently used memory**

.. code-block:: bash

    $ cat /proc/meminfo

Ports
-----
**Check currently listing TCP ports**

.. code-block:: bash

    $ sudo lsof -nP -iTCP -sTCP:LISTEN

