Set up a WSGI server
--------------------
Flask comes with a built-in webserver, but which is only supposed to be used during development.
Once you move your application into a production environment, you are strongly advised to
use a production WSGI server. Here, we will use `uwsgi`_ as the WSGI server running on an
`nginx`_ web server to host our app.

.. _uwsgi: https://uwsgi-docs.readthedocs.io/en/latest/
.. _nginx: https://nginx.org/

.. _install_setup_nginx:

Install and setup nginx
```````````````````````
At this point, your app should be deployed onto a dedicated machine (preferably Linux) as the
configuration must match its setup. Execute these steps on the server machine before proceeding:

* Deploy your application project onto the server machine (e.g. git clone)
* Create a virtual environment for your application

This enables you to set up the configuration of your web server.

.. hint::
    For actual production use, it is recommended to host from a Linux machine. For installation and
    usage on Windows, please follow the instructions on http://nginx.org/en/docs/windows.html

Let's start by adding the uWSGI package to our ``requirements.txt`` file::

    flask
    uwsgi

Then we need to install and configure nginx on the server machine.

**Linux**
    .. code-block:: bash

        $ sudo add-apt-repository ppa:nginx/stable
        $ sudo apt-get update && sudo apt-get upgrade
        $ sudo apt-get install nginx

**macOS**
(Homebrew_ must be installed)

    .. code-block:: bash

        $ brew install nginx

.. _Homebrew: https://brew.sh/

An nginx server is able to host multiple applications while each must use a different port.
In order to define the port an applications uses (among other settings), your application
requires a configuration file for nginx.

But before creating it, we must tell nginx to use such config files, since by default it
only knows about its default config.

Linux
'''''
On Linux, the default config should be removed, because future application should each be
defined in a separate config file:

    .. code-block:: bash

        $ sudo rm /etc/nginx/sites-enabled/default

This ``default`` configuration extends the base configuration found at ``/etc/nginx/nginx.conf``.
If you open it, you should find the line::

    include /etc/nginx/sites-enabled/*;

which tells nginx to add all configurations files found within this directory. Don't change it.

In case that line is not present, add it, save the file and restart nginx:

    .. code-block:: bash

        $ nginx /etc/init.d/nginx restart

macOS
'''''
On macOS, create a new directory, that will hold this application's config file:

**macOS only:**
    .. code-block:: bash

         $ mkdir /usr/local/etc/nginx/init.d

Open nginx's default config and include your new config folder:

    .. code-block:: bash

        $ nano /usr/local/etc/nginx/nginx.conf

Go to the bottom of the file and add

    .. code-block:: none

        include /usr/local/etc/nginx/init.d/*.conf;

before the last closing curly bracket, then save and close the file.

Restart the nginx server to apply your changes:

    .. code-block:: bash

        $ nginx -c /usr/local/etc/nginx/nginx.conf

    or restart as brew service via

    .. code-block:: bash

        $ brew services start nginx

.. hint::

    On macOS, Nginx uses the port 8080 as default. This might conflict with applications already running on
    that same port (e.g. some Java application). In order to change the default port, you need to
    adapt the default config.

    .. code-block:: bash

        $ nano /usr/local/etc/nginx/nginx.conf

    Find the uncommented line

    .. code-block::

        server {
            listen       8080;

    and change the port to your desired default port, then save and exit the file.
    Now, restart the nginx server with

    .. code-block:: bash

        $ brew services start nginx

Add a configuration to your application
```````````````````````````````````````
Now create a nginx config file within your application's root directory e.g. ``nginx.conf``.
Insert the following content:

    .. code-block:: none
        :linenos:

        server {
            listen         1050;
            server_name    localhost;
            charset        utf-8;
            client_max_body_size    75M;
            location / { try_files @uri @mywebapp; }
            location @mywebapp {
                include uwsgi_params;
                uwsgi_pass unix:/path/to/my/application/uwsgi.sock;
            }
        }

Adapt the application name (here: mywebapp) in line 6 and 7 with a descriptive name.
Also put in the path where your socket file should reside (e.g. put it to your project root directory).

The socket (line 9) is a service file that acts as the server's endpoint for the network traffic of your Python application
and is created when your application is launched on the server machine (i.e. when nginx is launched). Please note, that
you need a valid path from your server machine.

The *listen* parameter (line 2) defines the port your application will use. It is recommended to use a free
port anywhere within the range between 1024 and 32767. You can check all used ports by running these commands:

.. code-block:: bash

    $ tail /etc/service
    $ netstat -an | grep LISTEN

You can also check this list of `common default ports`_.

It is recommended to use a separate launcher to run the app over the WSGI server. Create a new Python file
in the project's root directory e.g. ``wsgi-runner.py`` and insert this content:

.. code-block::

    from mywebapp.mywebapp import app as application

    if __name__ == "__main__":
        application.run()

Adapt the module path where your Flask app instance is created (here: mywebapp.mywebapp).

Next up, create a uwsgi config file within your application's root directory e.g. ``uwsgi.ini``
and put in the following content:

.. code-block:: none
    :linenos:

    [uwsgi]
    # application's base folder
    base = /path/to/my/application/root/directory
    # change current directory to application base
    chdir = %(base)
    # python's module to import
    app = wsgi-runner
    module = %(app)
    # python interpreter root path (outside of bin/)
    home = /path/to/my/python/interpreter/or/venv
    pythonpath = %(base)
    # socket file's location
    socket = %(base)/%n.sock
    # permissions to socket file
    chmod-socket = 666
    # the variable that holds a flask application inside the module imported at line 6
    callable = application
    # location of log files
    logto = %(base)/log/uwsgi/%n.log

Adapt the *base* (line 3) and *home* (line 10) variables to your deployed application.
Also adapt *app* runner script (line 7) to your launcher.

Now, once again deploy your current project state onto the server machine.

On the server machine, create the log directory structure defined in *logto* (line 22) including an empty ``uwsgi.log`` file.

To make nginx host our application, we need to supply the ``nginx.conf`` to your nginx configuration directory.
Since the config file is part of the project (hence, it might be changed in the future) the server machine should
stay within the project structure, we create a symlink for it:

**macOS**:

.. code-block:: bash

    $ ln -s /path/to/my/application/nginx.conf /usr/local/etc/nginx/init.d/mywebapp.conf

**Linux**:

.. code-block:: bash

    $ ln -s /path/to/my/application/nginx.conf /etc/nginx/sites-enabled/mywebapp.conf

Now, you are ready to launch the uWSGI server for your application on the server machine. First make sure, you
activate your project's virtual environment, then type:

.. code-block:: bash

    (venv) $ uwsgi --ini /absolute/path/to/my/application/uwsgi.ini

This launches the uWSGI server using your project's configuration. Now open a browser on your local
machine and type your server machines IP, colon and the port specified in ``nginx.conf`` (e.g. ``10.180.2.75:1050``)
into the address bar, which will open the index page of your application.

.. _common default ports: https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

Manually start application on remote server (Linux)
---------------------------------------------------

Starting the uWSGI process commonly needs the command window to remain open. If it is closed,
the application is also terminated.

To prevent that, the process must be detached from the shell instance. On Linux, you can
achieve this by creating separate session via `screen`_, which is not terminated when the
console is closed.

.. _screen: https://www.gnu.org/software/screen/

Check, if your server already features ``screen`` by typing

    .. code-block:: bash

        $ screen -h

If that command is not available, install *screen* via

    .. code-block:: bash

        $ sudo apt-get install screen

Now open a new screen via

    .. code-block:: bash

        $ screen

A new screen is opened. Now you can start the uWSGI server (first activate the virtual environment):

    .. code-block:: bash

        (venv) $ uwsgi --ini /absolute/path/to/my/application/uwsgi.ini

To switch back to the original window, type ``Ctrl + A`` followed by a simple ``d`` (for detach). This does not close
the screen, which continues in the background, even after closing your terminal window.

Running ``screen -ls`` will list you all available screens. Each screen name starts with session ID (e.g. 32196).
To enter a specific screen (let's say 32196.pts-10) , type

    .. code-block:: bash

        $ screen -r 32196

to resume a detached session. To kill a window, enter it, then type ``Ctrl + a`` followed by simple ``k``, then confirm
with ``y``. Alternatively, you may send a quit command while outside the screen (let's say 32196.pts-10 again):

    .. code-block:: bash

        $ screen -XS 32196 quit

Automatically start application on system startup
-------------------------------------------------
**macOS**:

Copy the \*.plist file into ``/Library/LaunchDaemons`` to start nginx as a brew service on startup:

.. code-block:: bash

    $ sudo cp /usr/local/opt/nginx/*.plist /Library/LaunchDaemons

**Linux**:

*coming later*
