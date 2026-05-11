Controlled Elements
===================
**Problem:** Form elements maintain their own state inside the HTML element, hence the DOM.
This makes it hard to read their value and also introduces some state of the
application be in the DOM instead of the respective component.

In React, we want to keep **all state** inside the React application, never inside the DOM.

For this to work in form elements, we need to use so-called *controlled elements*. Three steps:

#. Inside the form element, create a piece of state for a form field

    .. code-block:: jsx

        function Form() {
          const [description, setDescription] = useState("");
        }

#. Inside the form element JSX, set the value of the input field to the state variable:

    .. code-block:: jsx
        :emphasize-lines: 11

          return (
            <form className="add-form" onSubmit={handleSubmit}>
              <h3>What do you need for your trip? </h3>
              <select>
                {Array.from({ length: 20 }, (_, i) => (
                  <option value={i + 1} key={`amount_${i}`}>
                    {i + 1}
                  </option>
                ))}
              </select>
              <input type="text" placeholder="Item..." value={description}></input>
              <button>Add</button>
            </form>
          );

#. Define the event handler (here: ``onChange``), passing in the event object (here: ``e``),
   and passing the form field value (here: ``e.target.value``) into the the state variables
   setter function (here: ``setDescription()``):

    .. code-block:: jsx
        :emphasize-lines: 15

          return (
            <form className="add-form" onSubmit={handleSubmit}>
              <h3>What do you need for your trip? </h3>
              <select>
                {Array.from({ length: 20 }, (_, i) => (
                  <option value={i + 1} key={`amount_${i}`}>
                    {i + 1}
                  </option>
                ))}
              </select>
              <input
                type="text"
                placeholder="Item..."
                value={description}
                onChange={(e) => setDescription(e.target.value)}
              ></input>
              <button>Add</button>
            </form>
          );

When now changing the text inside the form field, the connected state variable
is automatically updated.

Now, we are able to modify the ``handleSubmit()`` function to create an item:

.. code-block:: jsx
    :emphasize-lines: 4

      function handleSubmit(event) {
        event.preventDefault();

        const newItem = { description, quantity, packed: false, id: Date.now() };
      }
