How to create a Flask web application
=====================================
Create initial project structure
--------------------------------
Create a new folder which will contain your Flask web application. In this folder,
create the following files and directories:

.. code-block:: none

    mywebapp
        |--- templates/
                |--- base.html
                |--- index.html
        |--- static/
                |--- main.css
        |--- mywebapp.py
    log
        |--- uwsgi
                |--- uswgi.log
    runner.py (or dev-runner.py)
    requirements.txt
    MANIFEST.ini

Open ``requirements.txt`` and add the following content::

    flask

Install the packages::

    pip install -r requirements.txt

Open ``sample_app\sample_app.py`` and insert the following content:

.. code-block::

    from flask import Flask, render_template

    import threading
    import webbrowser

    app = Flask(__name__)

    URL = "http://127.0.0.1"
    PORT = 5000


    def main(autostart=False, debug=False, test=False):
        global PORT, URL
        url = f"{URL}:{PORT}"

        if autostart and not test:
            threading.Timer(1.25, lambda: webbrowser.open(url)).start()
            if not debug:
                return URL, PORT

        if debug:
            app.run(port=PORT, debug=debug)

        if test:
            app.run(port=PORT, debug=True)


    @app.route("/")
    def form_page():
        return render_template("index.html")


Open ``main.py`` and insert the following content:

.. code-block::

    from mywebapp.mywebapp import app, main


    if __name__ == "__main__":
        url, port = main(autostart=True)
        app.run(port=port)

Inside the *mywebapp/templates* folder create a new file ``base.html``, then insert
this content:

.. code-block:: html

    <!DOCTYPE html>
    <html>
      <head>
          <title>{{the_title}}</title>
          <link type="text/css" rel="stylesheet" href="static/main.css"/>
      </head>
      <body>
        {% block body %}

        {% endblock %}
      </body>
    </html>

Inside the *mywebapp/templates* folder create a new file ``index.html``, then insert
this content:

.. code-block:: html

    <!-- base.html is inherited and <body> block is overwritten -->

    {% extends 'base.html' %}

    {% block body %}

    <div class="mainframe">
        <p>This is the only content</p>
    </div>

    {% endblock %}

Inside *mywebapp/static* create a new file ``mywebapp.css``. Here you can define
all your style rules.

Set up a WSGI server
--------------------
Install and setup nginx
```````````````````````
Flask comes with a built-in webserver, but which is only supposed to be used during development.
Once you move your application into a production environment, you are strongly advised to
use a production WSGI server. Here, we will use `uwsgi`_ as the WSGI server running on an
`nginx`_ web server to host our app.

.. _uwsgi: https://uwsgi-docs.readthedocs.io/en/latest/
.. _nginx: https://nginx.org/

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
    .. prompt:: bash

        sudo add-apt-repository ppa:nginx/stable
        sudo apt-get update && sudo apt-get upgrade
        sudo apt-get install nginx

**macOS**
(Homebrew_ must be installed)

    .. prompt:: bash

        brew install nginx

.. _Homebrew: https://brew.sh/index_de

An nginx server is able to host multiple applications while each must use a different port.
In order to define the port an applications uses (among other settings), your application
requires a configuration file for nginx.

But before creating it, we must tell nginx to use such config files, since by default it
only knows about its default config.

Linux
'''''
On Linux, the default config should be removed, because future application should each be
defined in a separate config file:

    .. prompt:: bash

        sudo rm /etc/nginx/sites-enabled/default

This ``default`` configuration extends the base configuration found at ``/etc/nginx/nginx.conf``.
If you open it, you should find the line::

    include /etc/nginx/sites-enabled/*;

which tells nginx to add all configurations files found within this directory. Don't change it.

In case that line is not present, add it, save the file and restart nginx:

    .. prompt:: bash

        nginx /etc/init.d/nginx restart

macOS
'''''
On macOS, create a new directory, that will hold this application's config file:

**macOS only:**
    .. prompt:: bash

         mkdir /usr/local/etc/nginx/init.d

Open nginx's default config and include your new config folder:

    .. prompt:: bash

        nano /usr/local/etc/nginx/nginx.conf

Go to the bottom of the file and add

    .. code-block:: none

        include /usr/local/etc/nginx/init.d/*.conf;

before the last closing curly bracket, then save and close the file.

Restart the nginx server to apply your changes:

    .. prompt:: bash

        nginx -c /usr/local/etc/nginx/nginx.conf

    .. prompt:: bash

        brew services start nginx

.. hint::

    On macOS, Nginx uses the port 8080 as default. This might conflict with applications already running on
    that same port (e.g. some Java application). In order to change the default port, you need to
    adapt the default config.

    .. prompt:: bash

        nano /usr/local/etc/nginx/nginx.conf

    Find the uncommented line

    .. code-block::

        server {
            listen       8080;

    and change the port to your desired default port, then save and exit the file.
    Now, restart the nginx server with

    .. prompt:: bash

        brew services start nginx

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

.. prompt:: bash

    tail /etc/service
    netstat -an | grep LISTEN

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

.. prompt::

    ln -s /path/to/my/application/nginx.conf /usr/local/etc/nginx/init.d./mywebapp.conf

**Linux**:

.. prompt::

    ln -s /path/to/my/application/nginx.conf /etc/nginx/sites-enabled/mywebapp.conf

Now, you are ready to launch the uWSGI server for your application on the server machine. First make sure, you
activate your project's virtual environment, then type:

.. prompt:: bash (venv)

    uwsgi --ini /absolute/path/to/my/application/uwsgi.ini

This launches the uWSGI server using your project's configuration. Now open a browser on your local
machine and type your server machines IP, colon and the port specified in ``nginx.conf`` (e.g. ``10.180.2.75:1050``)
into the address bar, which will open the index page of your application.

.. _common default ports: https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers

Manually start application on remote server (Linux)
```````````````````````````````````````````````````
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

To switch back to the original window, type ``Ctrl + A`` followed by ``Ctrl + D`` (for detach). This does not close
the screen, which continues in the background, even after closing your terminal window.

Running ``screen -ls`` will list you all available screens. Each screen name starts with session ID (e.g. 32196).
To enter a specific screen (let's say 32196.pts-10) , type

    .. prompt:: bash

        screen -r 32196

to resume a detached session. To kill a window, enter it, then type ``Ctrl + A`` followed by ``k``, then confirm
with ``y``.

Automatically start application on system startup
`````````````````````````````````````````````````

