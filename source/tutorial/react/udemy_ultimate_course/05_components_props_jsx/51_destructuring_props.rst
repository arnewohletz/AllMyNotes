Destructuring Props
===================
Instead of referencing :javascript:`props.somePropName` in a receiving component,
it can be shortended to :javascript:`somePropName` by destructuring the ``props``
object in the function header.

For example, instead of

.. code-block:: jsx

    function Pizza(props) {
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

we can do

.. code-block:: jsx
    :emphasize-lines: 1

    function Pizza({ pizzaObj }) {
      if (pizzaObj.soldOut) return null;
      return (
        <li className="pizza">
          <img src={pizzaObj.photoName} alt={pizzaObj.name} />
          <div>
            <h3>{pizzaObj.name}</h3>
            <p>{pizzaObj.ingredients}</p>
            <span>{pizzaObj.price + 5}</span>
          </div>
        </li>
      );
    }

The ``props`` object no longer exists within ``Pizza``, but only the ``pizzaObj``
property is passed into the function.

.. important::

    The name of the destructured property in the receiving function must have the
    **same name** as used in the passing function (here: ``pizzaObj``).

**Multiple properties** can be destructured from the props object via comma, e.g.

.. code-block:: jsx

    function Order({ closeHour, closeHour }) {
      {/* doing stuff */}
    }

when using ``Order`` like this:

.. code-block:: jsx

    <Order closeHour={closeHour} openHour={openHour}/>

When attempting to destructure a property that does not exist, it is ``undefined``.
