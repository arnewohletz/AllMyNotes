.. _gnu_screen_reference:

Screen
======
`Screen`_ allows to manage multiple shells and keep them running in the background
without a active terminal.

For instance, it's' useful when hosting applications or services.

.. _screen: https://www.gnu.org/software/screen/


Create and open a new screen
----------------------------
.. prompt:: bash

    screen -S my_screen_session_name

Each screen receives a unique PID.

Switch between original window and screens
------------------------------------------
Screen --> Original (Detach)
````````````````````````````
To switch back to the original window, type :kbd:`Ctrl + A` followed by a
:kbd:`d` (for detach).

Original --> Screen (Re-attach)
```````````````````````````````
.. prompt:: bash

    screen -r SCREEN_PID

List all screens
----------------
.. prompt:: bash

    screen -ls

This list all screen in the following manner::

    SCREEN_PID.SESSION_NAME (CREATION_TIMEDATE) (STATUS)

The status shows *ATTACHED* if the screen in attached to your terminal, or
*DETACHED* in case not.

Kill a screen
-------------
To kill the currently attached screen, type :kbd:`Ctrl + A` followed by a
:kbd:`k` (for kill).

Alternatively, while not being detached to any screen, kill a screen via

.. prompt:: bash

    screen -XS SCREEN_PID quit

passing the that screen's SCREEN_PID.