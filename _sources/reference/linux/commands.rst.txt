Commands
========

Memory
------
**Check currently used memory**

.. prompt:: bash

    cat /proc/meminfo

Ports
-----
**Check currently listing TCP ports**

.. prompt:: bash

    sudo lsof -nP -iTCP -sTCP:LISTEN

