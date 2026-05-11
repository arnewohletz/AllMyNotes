Conditional rendering
=====================
Entire components or parts of a JSX element can be rendered only if certain conditions
are true.

With &&
-------
Using the ``&&`` operator (see :ref:`javascript_alfatraining_logic_operators`) an
if/else structure can be avoided (hence this method called short circuiting) to
enable conditional rendering:

.. code-block:: jsx
    :emphasize-lines: 6

    function Footer() {
      const hour = new Date().getHours();
      const openHour = 12;
      const closeHour = 22;
      const isOpen = hour >= openHour && hour <= closeHour;
      return <footer className="footer">{isOpen && <p>Open</p>}</footer>;
    }

Here, if the condition returns false, the statement returns ``false`` (though
``false`` or ``true`` are not rendered by React, so this works), otherwise
returns the :html:`<p>Open</p>` element.

.. attention::

    Other *truthy* and *falsy* values **will be rendered**.

.. hint::

    An **empty array** is still a **truthy** value.

With ternary operator
---------------------
More common approach, to avoid some pitfalls with the ``&&`` operator, use the
:ref:`javascript_alfaview_ternary_operator`:

.. code-block:: jsx
    :emphasize-lines: 8, 14

    function Menu() {
      const pizzas = pizzaData;
      const numPizzas = pizzas.length;

      return (
        <div className="menu">
          <h2>Our Menu</h2>
          {numPizzas ? (
            <ul className="pizzas">
              {pizzaData.map((pizza) => (
                <Pizza pizzaObj={pizza} key={pizza.name} />
              ))}
            </ul>
          ) : null}
        </div>
      );
    }

If *truthy*, the JSX element is returned, otherwise ``null`` (is not rendered).

The advantage also is, that alternatives can be returned:

.. code-block:: jsx
    :emphasize-lines: 10

    return (
    <div className="menu">
      <h2>Our Menu</h2>
      {numPizzas ? (
        <ul className="pizzas">
          {pizzaData.map((pizza) => (
            <Pizza pizzaObj={pizza} key={pizza.name} />
          ))}
        </ul>
      ) : <p>We are still working on our menu. Please come back later</p>}
    </div>

.. important::

    We **cannot use** *if/else* because it **does not produce a value**, so it
    cannot return a JSX element, which is needed here. For example

    .. code-block:: jsx

        {if(numPizzas > 0) <ul className="pizzas">
          {pizzaData.map((pizza) => (
            <Pizza pizzaObj={pizza} key={pizza.name} />
          ))}
        </ul>}

    produces a SyntaxError (unexpected token).

With multiple returns
---------------------
A component can have multiple conditional ``return`` statements.

.. code-block:: jsx
    :emphasize-lines: 7, 18

    function Footer() {
      const hour = new Date().getHours();
      const openHour = 20;
      const closeHour = 22;
      const isOpen = hour >= openHour && hour <= closeHour;

      if (!isOpen) {
        return (
          <div className="order">
            <p>
              We are happy to welcome to between {openHour}:00 - {closeHour}:00
            </p>
          </div>
        );
      }

      return (
        <footer className="footer">
            {*/ other JSX element, returned if upper condition is false */}
        </footer>
      )
    }

In the above example, the :html:`<footer>` element is not returned, if condition
in line 7 is fulfilled. Commonly, multiple returns are **not used to return an**
**individual part of a JSX, for entire components**:

.. code-block:: jsx

    function Pizza(props) {
      console.log(props);

      if (props.pizzaObj.soldOut) return null;

      return (
        <li className="pizza">
          <img src={props.pizzaObj.photoName} alt={props.pizzaObj.name} />
          <div>
            <h3>{props.pizzaObj.name}</h3>
            <p>{props.pizzaObj.ingredients}</p>
            <span>{props.pizzaObj.price + 5}</span>
          </div>
        </li>
      );
    }
