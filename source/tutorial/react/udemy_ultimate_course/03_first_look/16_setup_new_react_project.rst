Setup a new React project
=========================
There are two options:

    * use `create-react-app`_

        - complete *starter-kit* for React applications
        - already configured: ESLint (JavaScript linter, Prettier (code formatter),
          Jest (test framework) and `Babel`_ (compiler, allows latest JS features)
        - uses slow and outdated technologies
        - not recommended for real-world applications (only for learning)

    .. attention::

        The **create-react-app** has been deprecated as of February 2025.
        It still works with current React version (v19 as of Nov 2025), but
        might become incompatible with future React versions. Though it is not
        recommended to use it any longer.

    * use `vite`_

        - modern build tool, that contains a React application template
        - requires manual setup of linter (e.g. `ESLint`_), formatter (e.g. `Prettier`_)
          or a test framework (e.g. `Jest`_)

            .. hint::

                Setting up ESLint to play nicely with React is a bit cumbersome.

        - used for real-world-applications
        - incredibly fast reloads and bundling (almost instant refresh)

React now officially recommends using React frameworks like `NextJS`_ and `Remix`_
to setup a React project. Those frameworks include solutions for routing, data fetching
and server-side rendering (React does not include that). Those will not be used
in this course, as those are unsuitable for learning React.

.. hint::

    Not all React applications require the usage of a React framework, but can
    work using "vanilla" React.

.. _create-react-app: https://create-react-app.dev/
.. _vite: https://vite.dev/
.. _Babel: https://babeljs.io/
.. _ESLint: https://eslint.org/
.. _Prettier: https://prettier.io/
.. _Jest: https://jestjs.io/
.. _NextJS: https://nextjs.org/
.. _Remix: https://remix.run/

Setup using create-react-app
----------------------------
Navigate to the folder in which to create the application and run:

.. code-block:: none

    $ npx create-react-app@5 <project_name>

    .. hint::

        The ``@5`` makes usage of version 5 of the ``create-react-app``.
        Used here to avoid any incompatibilities in future versions.

The basic project structure is created (see below).

To run the application, execute

.. code-block:: none

    $ npm start

which starts a web server and opens the application automatically.

    .. hint::

        The ``package.json`` file defines the ``start`` script alias, which runs
        the command ``react-scripts start``.

Project structure
-----------------
This is a very basic project structure:

.. code-block:: none

    my-project/
    ├── public/
    │   └── index.html
    ├── src/
    │   ├── App.css
    │   ├── App.js
    │   ├── index.css
    │   └── index.js
    ├── node_modules
    └── package.json

* ``/public`` contains all files served directly by the web server

    * ``index.html`` is the application's index HTML file, which defines a root,
      element like :html:`<div id="root"></div>`

* ``/src`` contains all JavaScript files, CSS and other content

    * ``App.js`` defines the :javascript:`App()` component, which is used by ``ìndex.js``

        .. code-block:: jsx
            :caption: App.js

            function App() {
              return (
                <div className="App">
                  // some content
                </div>
              );
            }

    * ``index.js`` embeds the :html:`<App />` component element into the :html:`<React>`
      element and triggers the rendering of the element

        .. code-block:: jsx
            :caption: index.js

            import React from 'react';
            import ReactDOM from 'react-dom/client';
            import './index.css';
            import App from './App';

            const root = ReactDOM.createRoot(document.getElementById('root'));
            root.render(
              <React.StrictMode>
                <App />
              </React.StrictMode>
            );

    * corresponding ``*.css`` files contain the respective styling rules

* ``/node_modules`` contains all project dependencies
* ``package.json`` defines all project dependencies
