Rendering the Root Component in Strict Mode
===========================================
``create-react-app`` uses the `webpack`_ builder, which requires a ``index.js`` to
be the root JavaScript file:

.. code-block:: jsx
    :linenos:
    :caption: src/index.js

    import React from "react";
    import ReactDOM from "react-dom/client";

    function App() {
      return <h1>Hello React!</h1>;
    }

    const root = ReactDOM.createRoot(document.querySelector("#root"));
    root.render(<App />);

:line 1-2:
    import of ``React`` and ``ReactDOM`` components of npm-installed React packages

:line 4-6:
    define ``App()`` function. The name can be random (*App* is commonly used), but
    as every component, must start in upper-case.

:line 8:
    create a React Component from the :html:`<div id="root"></div>` element on ``public/index.html``

:line 9:
    render a :html:`<App />` component into the ``root`` component

.. _webpack: https://webpack.js.org/

The *Strict Mode* is helpful during development to find rendering bugs. It

    * renders components twice
    * checks if outdated parts of the React API is used

so it is recommended to always use it. To active, change **line 9** above to

.. code-block:: jsx

    root.render(
      <React.StrictMode>
        <App />
      </React.StrictMode>
    );
