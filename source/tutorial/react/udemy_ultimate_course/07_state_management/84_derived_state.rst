Derived state
=============
Derived state: state that is computed from an existing piece of state or from props.

.. code-block:: jsx

    const [cart, setCart] = useState([
        { name: "JavaScript Course", price: 15.99 },
        { name: "Node.js Bootcamp", price: 14.99 },
    ]};
    const [numItems, setNumItems] = useState(2);
    const [totalPrice, setTotalPrice] = useState(30.98);

Here, ``numItems`` and ``totalPrice`` depend on the items inside ``cart``, so they
are obsolete and its even dangerous to do so (needs manual update). Also, changing
all three state variables triggers three re-renders, that are unnecessary.

Make them regular variables, deriving their value from ``cart`` (single source of truth):

.. code-block:: jsx

    const [cart, setCart] = useState([
        { name: "JavaScript Course", price: 15.99 },
        { name: "Node.js Bootcamp", price: 14.99 },
    ]}
    const numItems = cart.length;
    const totalPrice = cart.reduce((acc, cur) => acc + cur.price, 0);

The ``numItems`` and ``totalPrice`` variables are re-calculated on each change of
``cart`` due to the auto-triggered re-render.

.. hint::

    Always derive from state, if those don't have to be their own state variable.

