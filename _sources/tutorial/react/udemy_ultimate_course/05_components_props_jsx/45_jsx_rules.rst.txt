JSX Rules
=========
General rules
-------------
* JSX essentially works like HTML, but allows a "JavaScript-Mode" by using ``{}``
  (for text or attributes)
* Inside ``{}`` JavaScript expressions are allowed. Example: reference variable,
  create arrays or objects, [].map(), ternary operator.
* Statements are **not allowed** (e.g. if/else, for, switch)
* JSX produces a JavaScript expression (for example a JSX HTML element is translated
  into a :javascript:`React.create()` function call, which is an expression)

    .. image:: _file/jsx_element_equals_js_expression.jpg

    #. Other pieces of JSX can be placed inside ``{}``
    #. JSX can be written **anywhere** inside a component (e.g. inside if/else,
       assign JSX to variables, pass JSX into functions)

* a piece of JSX can only have **one root element**. If more are needed, use
  :javascript:`<React.Fragment>` (or use short ``<>``):

    .. code-block:: jsx

        <>
          <OneChild />
          <AnotherChild />
        </>

Differences between JSX and HTML
--------------------------------
* ``className`` instead of HTML's ``class``
* ``htmlFor`` instead of HTML's ``for``
* Every tag needs to be closed. Examples: ``<img /> or ``<br />``
* All event handlers and other properties need to be **camelCased**. Examples:
  ``onClick`` or ``onMouseOver``
* **Exception**: ``aria-*`` and ``data-*`` are written with dashes like in HTML
* CSS inline styles are written like this: {{<style>}} (to reference a variable and
  then an object)
* CSS property names are also **camelCased**
* Comments need to be in ``{}`` (because they are JS)
