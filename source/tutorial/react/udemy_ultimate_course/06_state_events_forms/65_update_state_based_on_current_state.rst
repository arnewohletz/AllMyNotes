.. _tutorial_react_ultimate_update_state_based_on_current_state:

Change state based on current state
===================================
In a scenario, where we want to call a setter method more than once. For example:

.. code-block:: jsx
    :emphasize-lines: 5,6

    const [step, setStep] = useState(1);

    function handleNext() {
        if (step < 3) {
          setStep(s + 1);   {/* 1 -> 2 */}
          setStep(s + 1);   {/* 2 -> 3 */}
        }
    }

The ``setStep`` setter method is called twice, but when the method is executed,
**the state is only updated once** (``step`` becomes 2, but not 3).

Note, that a state variable should never be updated based on its current state,
but instead of passing the state value into a setter method, pass in a callback
function which receives the state variable as argument:

.. code-block:: jsx
    :emphasize-lines: 5,6

    const [step, setStep] = useState(1);

    function handleNext() {
        if (step < 3) {
          setStep((s) => s + 1);
          setStep((s) => s + 1);
        }
    }

This works well, ``step`` is changed to 3.

.. important::

    When using the functional form, React automatically passes the current state
    variable value into the callback function. You can name the state variable
    anything you want (here ``s``), e.g.

    .. code-block:: jsx

        setStep((thisIsTheCurrentStepValue) => thisIsTheCurrentStepValue + 1);

.. hint::

    Always pass a callback function into a state setter method, when the state
    variable is changed based on its current value.

    If the new value **is not based** on the current value, passing a callback
    function is **not necessary**.
