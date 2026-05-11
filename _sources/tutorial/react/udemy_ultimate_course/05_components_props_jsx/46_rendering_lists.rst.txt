.. _tutorial_react_ultimate_rendering_lists:

Rendering Lists
===============
List can be iterated over via the ``[list].map()`` function, returning a JSX element:

.. code-block:: jsx
    :emphasize-lines: 6-8

    function Menu() {
      return (
        <div className="menu">
          <h2>Our Menu</h2>
          <div>
            {pizzaData.map((pizza) => (
              <Pizza name={pizza.name} photoName={pizza.photoName} />
            ))}
          </div>
        </div>
      );
    }

Though this is **not a good practice**. The data object (here: ``pizza``) should be passed
down as a prop and the receiving component (here: ``Pizza``) describes the output:

.. code-block:: jsx
    :emphasize-lines: 6-8, 18, 20-22

    function Menu() {
      return (
        <div className="menu">
          <h2>Our Menu</h2>
          <div>
            {pizzaData.map((pizza) => (
              <Pizza pizzaObj={pizza} />
            ))}
          </div>
        </div>
      );
    }

    function Pizza(props) {
      console.log(props);
      return (
        <div className="pizza">
          <img src={props.pizzaObj.photoName} alt={props.pizzaObj.name} />
          <div>
            <h3>{props.pizzaObj.name}</h3>
            <p>{props.pizzaObj.ingredients}</p>
            <span>{props.pizzaObj.price + 5}</span>
          </div>
        </div>
      );
    }

This works, but causes an error, as now all instance of ``Pizza`` use the same
``key`` property (unspecified above, though always the same). To avoid this, pass
a unique value (here: ``pizza.name``, as unique for each ``pizza`` object):

.. code-block:: javascript

    {pizzaData.map((pizza) => (
      <Pizza pizzaObj={pizza} key={pizza.name}/>
    ))}

The ``[list].map()`` function creates and returns a new array containing the JSX
elements of component ``Pizza`` type. It is the same as writing this:

.. code-block:: jsx
    :emphasize-lines: 7-13

    function Menu() {
      return (
        <div className="menu">
          <h2>Our Menu</h2>
          <ul className="pizzas">
            {pizzaData.map((pizza) => (
              <li className="pizza">
                <img src={pizza.photoName} alt={pizza.name} />
                <div>
                  <h3>{pizza.name}</h3>
                  <p>{pizza.ingredients}</p>
                  <span>{pizza.price + 5}</span>
                </div>
              </li>
            ))}
          </ul>
        </div>
      );
    }

It is not a recommended practice. You should always put elements of different
concern into a separate component.
