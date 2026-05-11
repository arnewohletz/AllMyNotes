Setting classes and text conditionally
======================================
The ternary operator is very useful to set classes and text of elements conditionally.

Example:

.. code-block:: jsx
    :emphasize-lines: 3,8

    function Pizza({ pizzaObj }) {
      return (
        <li className={`pizza ${pizzaObj.soldOut ? "sold-out" : ""}`}>
          <img src={pizzaObj.photoName} alt={pizzaObj.name} />
          <div>
            <h3>{pizzaObj.name}</h3>
            <p>{pizzaObj.ingredients}</p>
            <span>{pizzaObj.soldOut ? "SOLD OUT" : pizzaObj.price + 5}</span>
          </div>
        </li>
      );
    }

In both cases, either a classname or a string is set depending on the value of
``pizzaObj.soldOut``. In line 3, the expression must defined in a template string,
which requires the JavaScript-Mode (``{}``). Inside of it, we can access variables
via ``${}``.
