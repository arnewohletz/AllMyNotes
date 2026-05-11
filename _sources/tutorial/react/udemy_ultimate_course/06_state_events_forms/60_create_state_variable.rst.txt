Create state variable with useState
===================================
The ``useState`` method requires the default value of the state variable as argument
and returns an array with the state variable value and a setter method for this state
variable:

.. code-block:: jsx

    import { useState } from "react"

    export default function App() {
      const [step, setStep] = useState(1);

      function handlePrevious() {
        if (step > 1) setStep(step - 1);
      }
      function handleNext() {
        if (step < 3) setStep(step + 1);
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

``useState()`` is a hook, so it can only be called on the top level of a function,
but not inside if/else statement or loops.