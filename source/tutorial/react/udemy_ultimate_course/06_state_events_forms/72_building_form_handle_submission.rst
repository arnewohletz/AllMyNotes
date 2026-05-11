Building a Form and Handling Submission
=======================================
Using the :javascript:`Array.from()` method, a finite number of elements can be
created:

.. code-block:: jsx
    :emphasize-lines: 6-10

    function Form() {
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
          <input type="text" placeholder="Item..."></input>
          <button>Add</button>
        </form>
      );
    }

When we submit a form, we **don't want the page to reload**, which is the common
HTML behavior, but we want React to handle the reload. To deactive it, disable
the default behavior in the handler function:

.. code-block:: jsx

    function handleSubmit(event) {
        event.preventDefault();
    }

Same as in regular JavaScript, React passes the event object to the event handler
function (here named ``event``).
