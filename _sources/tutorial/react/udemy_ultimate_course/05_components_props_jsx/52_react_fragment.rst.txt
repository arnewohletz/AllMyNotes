React Fragments
===============
As we know, JSX only allow **one** root element. Before, we added something like
a ``<div>`` element around multiple JSX elements to fulfil the requirement.

This is possible, but may impact the style, since CSS rules might not catch the
element anymore.

A React Fragment allows to **bundle multiple elements without actually enclosing it**
**into a common root element** (leaves no trace in HTML tree). In JSX, it uses ``<>``
for opening and ``</>`` for closing.

For example:

.. code-block:: jsx
    :emphasize-lines: 1,11

    <>
      <p>
        Authentic Italian cuisine. 6 creative dishes to choose from. All
        from our stone oven, all organic, all delicious.
      </p>
      <ul className="pizzas">
        {pizzaData.map((pizza) => (
          <Pizza pizzaObj={pizza} key={pizza.name} />
        ))}
      </ul>
    </>

If working with lists using the ``map()`` method, it creates multiple elements
using the same key (see :ref:`tutorial_react_ultimate_rendering_lists`),
the fragment requires to have a unique key. To enable this, the Fragement must
be created like this:

.. code-block:: jsx
    :emphasize-lines: 1,11

    <React.Fragment key="somekey">
      <p>
        Authentic Italian cuisine. 6 creative dishes to choose from. All
        from our stone oven, all organic, all delicious.
      </p>
      <ul className="pizzas">
        {pizzaData.map((pizza) => (
          <Pizza pizzaObj={pizza} key={pizza.name} />
        ))}
      </ul>
    </React.Fragment>

Of course, the above example does not require a key.
