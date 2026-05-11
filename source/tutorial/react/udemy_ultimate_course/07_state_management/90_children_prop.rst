The "children" Prop: Making a reusable button
=============================================
We want to make a customizable button, which accepts its settings as props:

.. code-block:: jsx

    function Button({ textColor, bgColor, onClick, text, emoji }) {
      return (
        <button
          style={{ backgroundColor: bgColor, color: textColor }}
          onClick={onClick}
        >
          <span>{emoji}</span>
          {text}
        </button>
      );
    }

and use it in another component's JSX:

.. code-block:: jsx

      <div className="buttons">
        <Button
          textColor="#fff"
          bgColor="#7950f2"
          onClick={handlePrevious}
          text="Previous"
          emoji="some_other_emoji"
        />
        <Button
          textColor="#fff"
          bgColor="#7950f2"
          onClick={handleNext}
          text="Next"
          emoji="some_emoji"
        />
      </div>

As we see, this **increases the amount of props**, making it harder to handle.

The solution is to pass some JSX as its content into the component element, inside
its tags, using non-self-closing component elements, but regular closing components,
like this:

.. code-block:: jsx
    :emphasize-lines: 2-7

          <div className="buttons">
            <Button textColor="#fff" bgColor="#7950f2" onClick={handlePrevious}>
              Previous <span>some_other_emoji</span>
            </Button>
            <Button textColor="#fff" bgColor="#7950f2" onClick={handleNext}>
              Next <span>some_emoji</span>
            </Button>
          </div>

This allows for direct customization of the button's text, including the emoji.

In the ``Button`` component, this requires accessing the **children** property,
which the component receives automatically. This contains everything that is inside
the starting and closing tags (here, e.g :html:`Next <span>"some_emoji"</span>`):

.. code-block:: jsx
    :emphasize-lines: 1,7

    function Button({ textColor, bgColor, onClick, children }) {
      return (
        <button
          style={{ backgroundColor: bgColor, color: textColor }}
          onClick={onClick}
        >
          {children}
        </button>
      );
    }

The ``children`` prop is like a hole, which can be filled with JSX-content that we
want the component to show:

* children prop allows us to **pass JSX into an element** (besides regular props)
* essential tool to make **reusable** and **configurable** components (especially
  component **content**)
* really useful for **generic** components that **don't know their content** before
  being used (e.g. modal)

**Example**: For this ``Button`` component

.. code-block:: jsx

    <Button textColor="#fff" bgColor="#7950f2" onClick={handleNext}>
      Next <span>some_emoji</span>
    </Button>

**anything** between the opening ``<Button>`` and the closing tag ``</Button>``
is passed as the ``children`` prop, so here:

.. code-block:: jsx

    Next <span>some_emoji</span>
