nginx
=====
Manually start application on remote server (Linux)
---------------------------------------------------
Starting the uWSGI process commonly needs the command window to remain open. If it is closed,
the application is also terminated.

To prevent that, the process must be detached from the shell instance. On Linux, you can
achieve this by creating separate session via `screen`_, which is not terminated when the
console is closed.

.. _screen: https://www.gnu.org/software/screen/

Check, if your server already features ``screen`` by typing

    .. prompt:: bash

        screen -h

If that command is not available, install *screen* via

    .. prompt:: bash

        sudo apt-get install screen

Now open a new screen via

    .. prompt:: bash

        screen

A new screen is opened. Now you can start the uWSGI server (first activate the virtual environment):

    .. prompt:: bash (venv)

        uwsgi --ini /absolute/path/to/my/application/uwsgi.ini

To switch back to the original window, type ``Ctrl + A`` followed by a simple ``d`` (for detach). This does not close
the screen, which continues in the background, even after closing your terminal window.

Running ``screen -ls`` will list you all available screens. Each screen name starts with session ID (e.g. 32196).
To enter a specific screen (let's say 32196.pts-10) , type

    .. prompt:: bash

        screen -r 32196

to resume a detached session. To kill a window, enter it, then type ``Ctrl + a`` followed by simple ``k``, then confirm
with ``y``. Alternatively, you may send a quit command while outside the screen (let's say 32196.pts-10 again):

    .. prompt:: bash

           screen -XS 32196 quit

Automatically start application on system startup
-------------------------------------------------
**macOS** [#macos_autostart]_:

Copy the \*.plist file into ``/Library/LaunchDaemons`` to start nginx as a brew service on startup:

.. prompt:: bash

    sudo cp /usr/local/opt/nginx/*.plist /Library/LaunchDaemons

**Linux**:

*coming later*

.. rubric:: Sources:
.. [#macos_autostart] https://derickbailey.com/2014/12/27/how-to-start-nginx-on-port-80-at-mac-osx-boot-up-log-in/
