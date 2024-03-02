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
