Creating and reusing a component
================================
See ``02-pizza-menu``.

* A component is a JavasScript function which

    * starts with an upper case letter
    * must return one HTML markup element

* The returned markup element can contain other nested components

    .. code-block:: jsx

        function App() {
          return (
            <div>
              <h1>Hello React!</h1>
              <Pizza />
            </div>
          );
        }

        function Pizza() {
          return <h2>Pizza</h2>;
        }

* A components can be used multiple times, for example:

    .. code-block:: jsx

        function App() {
          return (
            <div>
              <h1>Hello React!</h1>
              <Pizza />
              <Pizza />
              <Pizza />
            </div>
          );
        }

