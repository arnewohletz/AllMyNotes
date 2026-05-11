Pure React
==========
Using React without a build tool from scratch. This is **not** how React is used
in modern applications.

#. Create a new HTML file (and give it a title) and create a ``<div id="root">``
   element inside the body:

    .. code-block:: html
        :emphasize-lines: 6, 9

        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Hello React!</title>
          </head>
          <body>
            <div id="root"></div>
          </body>
        </html>

#. Add the two React libraries to the project:

    .. code-block:: html
        :emphasize-lines: 7,8

        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Hello React!</title>
            <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
            <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
          </head>
          <body>
            <div id="root"></div>
          </body>
        </html>

    * ``react.development.js`` is the core library, which includes components or state
    * ``react-dom.development.js`` is the rendering layer, which puts React components
      into the DOM (components can also be rendered into other environments e.g. native
      application with ``react-application``)

#. Create first component (a JavaScript function with an upper-case name, which returns
   an HTML element using JSX):

    .. important::

        Here, we cannot return a JSX element, as the browser lacks the functionality
        to convert JSX into a React element. So, we must use the ``React.createElement()``
        function to create it.

    .. code-block:: html
        :emphasize-lines: 14-16

        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Hello React!</title>
            <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
            <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
          </head>
          <body>
            <div id="root"></div>
          </body>
          <script>
            function App() {
              return React.createElement("header");
            }
          </script>
        </html>

    The ``React`` object is available due to the import of ``react.development.js``.

#. The ``<header>`` element must now be added to the page and the ``<div id=root>`` element
   must be rendered by giving it an instance of our ``App`` component:


    .. code-block:: html
        :emphasize-lines: 17-18

        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Hello React!</title>
            <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
            <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
          </head>
          <body>
            <div id="root"></div>
          </body>
          <script>
            function App() {
              return React.createElement("header");
            }
            const root = ReactDOM.createRoot(document.getElementById("root"));
            root.render(React.createElement(App));
          </script>
        </html>

#. When opening the page inside the browser, the ``<header>`` is rendered inside
   the ``<div id=root>`` Element, but is still empty. Let's add some content:

    .. code-block:: html
        :emphasize-lines: 15-16

        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Hello React!</title>
            <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
            <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
          </head>
          <body>
            <div id="root"></div>
          </body>
          <script>
            function App() {
              const time = new Date().toLocaleTimeString();
              return React.createElement("header", null, "Hello React");
            }
            const root = ReactDOM.createRoot(document.getElementById("root"));
            root.render(React.createElement(App));
          </script>
        </html>

    The ``createElement()`` function accepts ``props`` as second argument (won't use,
    so passing ``null``) and any amount of children nodes. Here, we simply pass
    a string.

#. In order to update the time with each change, the current time must be saved
   as a **state** using the ``React.useState()`` function. Moreover, in order to
   update the time every second, the ``React.useEffect()`` function must be used,
   which is a hook, that makes sure, the component stays in sync with the data
   (here, the ``setInterval()`` JavaScript method is used to call the time state
   setter function ``setTime()`` every 1000 milliseconds):

    .. code-block:: html
        :emphasize-lines: 16-21

        <!DOCTYPE html>
        <html lang="en">
          <head>
            <meta charset="UTF-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            <title>Hello React!</title>
            <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
            <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
          </head>
          <body>
            <div id="root"></div>
          </body>
          <script>
            function App() {
              // const time = new Date().toLocaleTimeString();
              const [time, setTime] = React.useState(new Date().toLocaleTimeString());
              React.useEffect(function () {
                setInterval(function () {
                  setTime(new Date().toLocaleTimeString());
                }, 1000);
              }, []);
              return React.createElement("header", null, `Hello React! It is ${time}`);
            }
            const root = ReactDOM.createRoot(document.getElementById("root"));
            root.render(React.createElement(App));
          </script>
        </html>

    The time is now updated every second.

    .. hint::

        Read these pages before starting the advance section of this tutorial:

        * `You Might Not Need an Effect`_
        * `Removing Effect Dependencies`_

.. _You Might Not Need an Effect: https://react.dev/learn/you-might-not-need-an-effect
.. _Removing Effect Dependencies: https://react.dev/learn/removing-effect-dependencies
