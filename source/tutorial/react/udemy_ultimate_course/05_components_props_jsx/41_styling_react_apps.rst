Styling React Applications
==========================
* As React is "only" a library, it does not enforce a certain way to style its components
* Inline styling, external CSS files, `Sass`_ files, `CSS modules`_, `styled-components`_,
  `Tailwind CSS`_ - all is possible

Example inline CSS:

.. code-block:: jsx

    function Header() {
        return <h1 style={{ color: "red", fontSize: "32px" }}>Fast React Pizza Company</h1>;
    }

    // alternatively
    function Header() {
        const style = { color: "red", fontSize: "48px", textTransform: "uppercase" };
        return <h1 style={style}>Fast React Pizza Company</h1>;
    }

.. hint::

    Double curly braces needed. Outer braces define JavaScript section, inner braces
    defines a JavaScript style object (see `CSSStyleProperties`_).

Example include CSS file (``index.css``):

.. code-block:: jsx
    :emphasize-lines: 1, 5

    import "./index.css";

    function Menu() {
      return (
        <div className="menu">
          <h2>Our Menu</h2>
          <Pizza />
          <Pizza />
          <Pizza />
          <Pizza />
        </div>
      );
    }

.. hint::

    The CSS file must be imported (handled by webpack).

    In JSX, the property ``className`` must be used, not ``class`` (is probably already
    reserved keyword).


.. _Sass: https://sass-lang.com/
.. _CSS modules: https://www.w3schools.com/react/react_css_modules.asp
.. _styled-components: https://styled-components.com/
.. _Tailwind CSS: https://tailwindcss.com/
.. _CSSStyleProperties: https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleProperties#description
