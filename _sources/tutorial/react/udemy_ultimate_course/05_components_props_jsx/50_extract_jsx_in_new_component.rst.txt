Extracting JSX into a new component
===================================
If JSX return elements become too large, it is wise to move them to a separate component.
For example, the ``<footer>`` element is getting too long

.. code-block:: jsx
    :emphasize-lines: 9-12

    function Footer() {
      const hour = new Date().getHours();
      const openHour = 20;
      const closeHour = 22;
      const isOpen = hour >= openHour && hour <= closeHour;
      return (
        <footer className="footer">
          {isOpen ? (
            <div className="order">
              <p>We're open until {closeHour}:00. Come visit us or order online.</p>
              <button className="btn">Order</button>
            </div>
          ) : (
            <div className="order">
              <p>
                We're happy to welcome to between {openHour}:00 - {closeHour}:00
              </p>
            </div>
          )}
        </footer>
      );

so the *order* part is supposed to be moved to a new ``Order`` component component:

.. code-block:: jsx

    function Order(props) {
      return (
        <div className="order">
          <p>
            We are open until {props.closeHour}:00. Come visit us or order online.
          </p>
          <button className="btn">Order</button>
        </div>
      );
    }

and replace the JSX with the component in the ``Footer`` component with an ``<Order />``
component element:

.. code-block:: jsx
    :emphasize-lines: 9

    function Footer() {
      const hour = new Date().getHours();
      const openHour = 20;
      const closeHour = 22;
      const isOpen = hour >= openHour && hour <= closeHour;
      return (
        <footer className="footer">
          {isOpen ? (
            <Order closeHour={closeHour} />
          ) : (
            <div className="order">
              <p>
                We are happy to welcome to between {openHour}:00 - {closeHour}:00
              </p>
            </div>
          )}
        </footer>
      );
    }

Note, that the ``closeHour`` variable must be passed down as a props value.
