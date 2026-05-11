React vs. plain JavaScript
==========================
https://www.udemy.com/course/the-ultimate-react-course/learn/lecture/37350394#overview

Comparing ``App.js`` with ``vanilla-JS.html``:

.. literalinclude:: _file/10_App.js
    :language: react
    :caption: App.js

.. literalinclude:: _file/10_vanilla-JS.html
    :language: html
    :caption: vanilla-JS.html

Context:

    * Plain JavaScript: JS code is embedded inside HTML (HTML is the driver)
    * React: JS code contains HTML elements (JS is the driver)

State:

    * Plain JavaScript: state is saved inside JavaScript code
    * React: saved inside Application state variables

UI Update:

    * Plain JavaScript: must manually update changed DOM elements
    * React: automatically updates components which alter its state

.. important::

    Main difference is that React handles keeping UI in sync with the state
    whereas when using plain JavaScript, the UI has be manually updated and JS
    must manage the state.
