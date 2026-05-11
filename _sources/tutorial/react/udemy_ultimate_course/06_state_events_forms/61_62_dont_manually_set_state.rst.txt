Don't set state manually!
=========================
State must always be updated using the setter functions, not manually.
State is supposed to be **considered as immutable** (only changeable by setter methods).

For example:

.. code-block:: jsx
    :emphasize-lines: 5

      let [step, setStep] = useState(1);

      function handleNext() {
        // if (step < 3) setStep(step + 1);
        step = step + 1;
      }

|:warning:| The ``step`` variable change is **not registered** by React and the
**component is not updated**.

.. hint::

    State variables are not supposed to be mutable directly, so always use type
    ``const``, not ``let``.

.. hint::

    It is possible to change object type state variables without setter methods,
    which trigger a re-render:

    .. code-block:: jsx
        :emphasize-lines: 3,7

        export default function App() {
          const [step, setStep] = useState(1);
          const [test] = useState({ name: "fred" });

          function handleNext() {
            if (step < 3) setStep(step + 1);
            test.name = "mike";
          }

    This works here, but not in more complex scenarios and is considered a
    **very bad practice**. Don't do it, always use the setter method.

The Mechanics of State
======================
* the DOM is not directly manipulated in React (due to declarative nature)
* a view is updated by re-rendering the component whenever its state changes
* state is saved inside a state variable
