Thinking about state and Lifting State Up
=========================================
See ``04-travel-list`` project.

Update immutable state variables (e.g. Array)
---------------------------------------------
In the *travel-list* application, we define an empty Array to be the initial value
of the ``items`` state variable:

.. code-block:: jsx
    :emphasize-lines: 4

    function Form() {
      const [description, setDescription] = useState("");
      const [quantity, setQuantity] = useState(1);
      const [items, setItems] = useState([]);

However, as state variables are **immutable**, we cannot change the ``items`` array
by pushing new items onto it.

.. code-block:: jsx
    :emphasize-lines: 2

      function handleAddItems(item) {
        setItems((items) => items.push(item));  /* THIS IS NOT ALLOWED!!! */
      }

Instead, we need to **create a new array**:

.. code-block:: jsx
    :emphasize-lines: 2

      function handleAddItems(item) {
        setItems((items) => items.push([...items, item]));  /* THIS WORKS! */
      }

Make state available to sibling component
-----------------------------------------
The ``items`` state variable is updated inside the ``Form`` component, but to display
it, it must be accessible to the ``PackingList`` component, which is a sibling component
of ``Form``.

To resolve, ``items`` must be moved to the closest common parent component
``App`` -> **lift up** state. Moving up ``ìtems`` and ``handleAddItems()`` function:

.. code-block:: jsx

    export default function App() {
      const [items, setItems] = useState([]);

      function handleAddItems(item) {
        setItems((items) => [...items, item]);
      }

      return (
        <div>
          <Logo />
          <Form onAddItems={handleAddItems} />
          <PackingList items={items} />
          <Stats />
        </div>
      );
    }

.. important::

    It is a convention to name property functions passed down to a component
    starting with ``on`` and remove ``handle`` from the name. So ``handleAddItems``
    becomes ``onAddItems``.

... and accepting the props in the components:

.. code-block:: jsx
    :emphasize-lines: 1, 11, 18, 22

    function Form({ onAddItems }) {
      const [description, setDescription] = useState("");
      const [quantity, setQuantity] = useState(1);

      function handleSubmit(event) {
        event.preventDefault();

        if (!description) return; // prevent submit if description is empty

        const newItem = { description, quantity, packed: false, id: Date.now() };
        onAddItems(newItem);

        // set back input fields to original state
        setQuantity(1);
        setDescription("");
      }

    function PackingList({ items }) {
      return (
        <div>
          <ul className="list">
            {items.map((item) => (
              <Item item={item} key={`item_${item.id}`} />
            ))}
          </ul>
        </div>
      );
    }

.. hint::

    **Child-to-parents communication (inverse data flow)**

    By passing down setter-functions as props to child components, these components
    have the possibility to change the associated (otherwise immutable) state despite
    it being defined in the parent component.

Delete an item from parent component state variable
---------------------------------------------------
The delete action is implemented in the ``Item`` component, though it affects the
``App`` component, which now defines the state of ``items`` array.

Define a ``handleDeleteItem()`` function inside ``App``component, which creates a
new array by filtering out the item with the passed ``id``:

.. code-block:: jsx

    export default function App() {
      const [items, setItems] = useState([]);

      function handleDeleteItem(id) {
        setItems((items) => items.filter((item) => item.id !== id));
      }

As ``Item`` resides inside the ``PackingList`` component, it must first be passed
in there:

.. code-block:: jsx
    :emphasize-lines: 7

    export default function App() {
      /* not showing state stuff */
      return (
        <div>
          <Logo />
          <Form onAddItems={handleAddItems} />
          <PackingList items={items} onDeleteItem={handleDeleteItem} />
          <Stats />
        </div>
      );
    }

and inside ``PackagingList`` (won't use itself, only passes it along) also pass down
the function to each ``Item`` component:

.. code-block:: jsx
    :emphasize-lines: 1, 9

    function PackingList({ items, onDeleteItem }) {
      return (
        <div>
          <ul className="list">
            {items.map((item) => (
              <Item
                item={item}
                key={`item_${item.id}`}
                onDeleteItem={onDeleteItem}
              />
            ))}
          </ul>
        </div>
      );
    }

In the ``Item`` component, we receive the function and add it to the ``onClick``
property of the delete button. Though this **won't work**:

.. code-block:: jsx

    function Item({ item, onDeleteItem }) {
      return (
        <li>
          <span style={item.packed ? { textDecoration: "line-through" } : {}}>
            {item.id} {item.description}
          </span>
          <button onClick={onDeleteItem}>X</button>
        </li>
      );
    }

This calls the ``onDeleteItem`` method, but not passing the item's ``id``, but
the **event object**. So instead, a new function must be defined like this:

.. code-block:: jsx
    :emphasize-lines: 7

    function Item({ item, onDeleteItem }) {
      return (
        <li>
          <span style={item.packed ? { textDecoration: "line-through" } : {}}>
            {item.id} {item.description}
          </span>
          <button onClick={() => onDeleteItem(item.id)}>X</button>
        </li>
      );
    }

Update a item from parent component state variable
--------------------------------------------------
The same as above applies for updating an item which is managed inside the parent
component, here toggling an items *packed*  status checkbox.

Again, define the function inside the ``App`` component:

.. code-block:: jsx
    :emphasize-lines: 4-10

    export default function App() {
      const [items, setItems] = useState([]);

      function handleToggleItem(id) {
        setItems((items) =>
          items.map((item) =>
            item.id === id ? { ...item, packed: !item.packed } : item
          )
        );
      }

    }

which essentially creates a new item if the passed ``id`` matches, toggling the
``packed`` boolean value. Then passing it down to the ``Item`` component as above
and use it as follows:

.. code-block:: jsx
    :emphasize-lines: 1, 7-9

    function Item({ item, onDeleteItem, onToggleItem }) {
      return (
        <li>
          <input
            type="checkbox"
            value={item.packed}
            onChange={() => {
              onToggleItem(item.id);
            }}
          ></input>
          <span style={item.packed ? { textDecoration: "line-through" } : {}}>
            {item.id} {item.description}
          </span>
          <button onClick={() => onDeleteItem(item.id)}>X</button>
        </li>
      );
    }
