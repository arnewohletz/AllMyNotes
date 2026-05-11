Passing and receiving props
===========================
* props are used to pass data into components, in particular, from **parent components**
  to **child components** (down the component tree)
* data is first passed into a component, then received by it

    .. code-block:: jsx
        :caption: Passing data as props
        :emphasize-lines: 6-9

        function Menu() {
          return (
            <div className="menu">
              <h2>Our Menu</h2>
              <Pizza
                name="Pizza Spinaci"
                ingredient="Tomato, mozarella, spinach, and ricotta cheese"
                photoName="pizzas/spinaci.jpg"
                price="10"
              />
            </div>
          );
        }

    .. code-block:: jsx
        :caption: Receive data
        :emphasize-lines: 1, 4-6

        function Pizza(props) {
          return (
            <div className="pizza">
              <img src={props.photoName} alt={props.name} />
              <h3>{props.name}</h3>
              <p>{props.ingredients}</p>
            </div>
          );
        }

    Data is passed as element properties. The called component function must
    accept a ``props`` argument, which contains all these properties. They can
    then be accessed via JavaScript.

* When creating the component, these props must be defined (order is irrelevant):

    .. code-block:: jsx
        :caption: Create component
        :emphasize-lines: 5-16

        function Menu() {
          return (
            <div className="menu">
              <h2>Our Menu</h2>
              <Pizza
                name="Pizza Spinaci"
                ingredients="Tomato, mozarella, spinach, and ricotta cheese"
                photoName="pizzas/spinaci.jpg"
                price="10"
              />
              <Pizza
                name="Pizza Funghi"
                ingredients="Tomato, Mushrooms"
                price="12"
                photoName="pizzas/funghi.jpg"
              />
            </div>
          );
        }

.. hint::

    **How to use value types other than strings**

    For example, to use a number instead of a string, it must be passed inside
    curly braces to enable the JavaScript-Mode. Outside of it, only Strings are
    allowed.

    .. code-block:: jsx
        :emphasize-lines: 5

          <Pizza
            name="Pizza Spinaci"
            ingredients="Tomato, mozarella, spinach, and ricotta cheese"
            photoName="pizzas/spinaci.jpg"
            price={10}
          />

    Anything can be passed as a props!


