Handling Events
===============
.. hint::

    Nothing new in previous lecture (57 - Building a Steps Component), see
    ``03-steps`` project.

**No event listeners or event handlers are used**, which is the imperative way of
classic JavaScript. Instead a kind of inline event listener is used directly when
specifying the element:

.. code-block:: jsx
    :emphasize-lines: 4, 10

      <div className="buttons">
        <button
          style={{ backgroundColor: "#7950f2", color: "#fff" }}
          onClick={() => alert("Previous")}
        >
          Previous
        </button>
        <button
          style={{ backgroundColor: "#7950f2", color: "#fff" }}
          onClick={() => alert("Next")}
        >
          Next
        </button>

.. important::

    React executes all function calls immediately when rendering a JSX element,
    so **a function call cannot be passed assigned to event**, but require a
    **function**. This immediately runs:

    .. code-block:: jsx

        {*/ NOK */}
        onMouseEnter={alert("TEST")}

        {/* OK */}
        onMouseEnter={() => alert("TEST")}

Usually, event handler functions are created within the component function and
then passed to the JSX element event handler (often starts with ``handle*``):

.. code-block:: jsx
    :emphasize-lines: 3-8,14,20

    export default function App() {

      function handlePrevious() {
        alert("Previous");
      }
      function handleNext() {
        alert("Next");
      }

      return (
          <div className="buttons">
            <button
              style={{ backgroundColor: "#7950f2", color: "#fff" }}
              onClick={handlePrevious}
            >
              Previous
            </button>
            <button
              style={{ backgroundColor: "#7950f2", color: "#fff" }}
              onClick={handleNext}
            >
              Next
            </button>
          </div>
        )
