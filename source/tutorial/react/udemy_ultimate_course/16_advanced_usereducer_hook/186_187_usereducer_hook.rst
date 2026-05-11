Yet another hook: useReducer
============================
* ``useReducer`` is a more advanced and complex way to manage state (when compared
  to ``useState``)
* it requires the initial state and a "reducer" function, returning the new state and
  a ``dispatch`` function
* the "reducer" function requires the current ``state`` and an ``action`` as argument
  and must return the new state
* the ``dispatch`` function is used to update the state

Instead of:

.. code-block:: jsx

    function DateCounter() {
      const [count, setCount] = useState(0);
      const [step, setStep] = useState(1);

      // This mutates the date object.
      const date = new Date("june 21 2027");
      date.setDate(date.getDate() + count);

      const dec = function () {
        setCount((count) => count - step);
      };

      const inc = function () {
        setCount((count) => count + step);
      };
      {/* more stuff */}
    }

We do:

.. code-block:: jsx
    :emphasize-lines: 1,3-6,9,17,21

    import { useState, useReducer } from "react";

    function reducer(state, action) {
      console.log(state, action);
      return state + action;
    }

    function DateCounter() {
      const [count, dispatch] = useReducer(reducer, 0);
      const [step, setStep] = useState(1);

      // This mutates the date object.
      const date = new Date("june 21 2027");
      date.setDate(date.getDate() + count);

      const dec = function () {
        dispatch(-1);
      };

      const inc = function () {
        dispatch(1);
      };

* we use ``useReducer`` for the ``count`` state variable
* we pass a ``reducer`` function and the initial value ``0`` and receive
  the state variable and the ``dispatch`` function (which usually accepts a function
  whose return value determines the new state)
* we define the ``reducer`` function, which accepts the current state ``state``
  and the action object ``action``
* in this case, we only pass in a value as ``action`` by calling ``dispatch(-1)``
  and ``dispatch(1)`` inside the handler functions, thereby reducing or increasing
  the ``count`` value by 1.

Although the ``action`` argument when calling ``dispatch(action)`` should be an
object of this content:

.. code-block:: jsx
    :emphasize-lines: 2,6

      const dec = function () {
        dispatch({ type: "dec", payload: -1 });
      };

      const inc = function () {
        dispatch({ type: "inc", payload: 1 });
      };

The object can have **any shape**, but it is a convention to always pass ``type``
and ``payload`` (also used in Redux).

In the ``reducer()`` function, we must now decide the return value according to the
passed ``type`` attribute:

.. code-block:: jsx
    :emphasize-lines: 3-11

    function reducer(state, action) {
      console.log(state, action);
      if (action.type === "inc") {
        return state + action.payload;
      }
      if (action.type === "dec") {
        return state - action.payload;
      }
      if (action.type === "setCount") {
        return action.payload;
      }
    }

.. hint::

    ``"setCount"`` is a third type, which allows setting the value to a specific value:

    .. code-block:: jsx

      const defineCount = function (e) {
        dispatch({ type: "setCount", payload: Number(e.target.value) });
      };

To simplify, the ``reducer`` may define the reduce and increase step, as it is always
``1`` or ``-1`` respectively:

.. code-block:: jsx
    :emphasize-lines: 4,7

    function reducer(state, action) {
      console.log(state, action);
      if (action.type === "inc") {
        return state + 1;
      }
      if (action.type === "dec") {
        return state - 1;
      }
      if (action.type === "setCount") {
        return action.payload;
      }
    }

so we can call it without ``payload``:

.. code-block:: jsx

      const dec = function () {
        dispatch({ type: "dec" });
      };

      const inc = function () {
        dispatch({ type: "inc" });
      };

Managing related pieces of state
================================
Usually, ``useReducer`` is used for more complex state variables (not just increasing
and decreasing a value), like an object:

.. code-block:: jsx

    function DateCounter() {

      const initialState = { count: 0, step: 1 };
      const [state, dispatch] = useReducer(reducer, initialState);
      const { count, step } = state;

      {/* more stuff */}
    }

* we define an ``initialState`` object, holding ``count`` and ``step``
* we set ``initialState`` as initial state for the ``state`` state variable
* we destructure ``count`` and ``step`` variables from ``state``

The ``reducer()`` function now receives

    * ``initialState`` object as ``state``
    * the object with passed into ``dispatch()`` as ``action``

Adapt it to this (using ``switch``):

.. code-block:: jsx

    function reducer(state, action) {
      console.log(state, action);

      switch (action.type) {
        case "inc":
          return { ...state, count: state.count + 1 };
        case "dec":
          return { ...state, count: state.count - 1 };
        case "setCount":
          return { ...state, count: action.payload };
        default:
          throw new Error("Unknown action");
      }
    }

* we use ``switch`` to return based on ``action.type``
* we must return an object of the same shape as ``state`` (which is ``{ count: xx, step: xx}``),
  which we do by *spreading* the passed in ``state`` object and overriding the
  ``count`` value
* as default, we throw an error (if ``dispatch()`` is called with an unknown type)

Last, we also add the type "setStep" and call it from ``defineStep()`` function
and also take the ``state.step`` into account when increasing/decreasing the ``state.count``:

.. code-block:: jsx
    :emphasize-lines: 11-12,23

    function reducer(state, action) {
      console.log(state, action);

      switch (action.type) {
        case "inc":
          return { ...state, count: state.count + state.step };
        case "dec":
          return { ...state, count: state.count - state.step };
        case "setCount":
          return { ...state, count: action.payload };
        case "setStep":
          return { ...state, step: action.payload };
        default:
          throw new Error("Unknown action");
      }
    }

    function DateCounter() {

      {/* more stuff */}

      const defineStep = function (e) {
        dispatch({ type: "setStep", payload: Number(e.target.value) });
      };

      {/* more stuff */}
    }

Though all above can also be realized using ``useState``, this one can't:

.. code-block:: jsx
    :emphasize-lines: 12-13

    function reducer(state, action) {

      switch (action.type) {
        case "inc":
          return { ...state, count: state.count + state.step };
        case "dec":
          return { ...state, count: state.count - state.step };
        case "setCount":
          return { ...state, count: action.payload };
        case "setStep":
          return { ...state, step: action.payload };
        case "reset":
          return { count: 0, step: 1 };
        default:
          throw new Error("Unknown action");
      }
    }

    function DateCounter() {

      {/* more stuff */}

      const reset = function () {
        dispatch({ type: "reset" });
      };

      {/* more stuff */}
    }

* it is possible to update both ``count`` and ``step`` **at the same time**
* also, the ``initialState`` can be moved outside of the component:

.. code-block:: jsx
    :emphasize-lines: 1,13

    const initialState = { count: 0, step: 1 };

      switch (action.type) {
        case "inc":
          return { ...state, count: state.count + state.step };
        case "dec":
          return { ...state, count: state.count - state.step };
        case "setCount":
          return { ...state, count: action.payload };
        case "setStep":
          return { ...state, step: action.payload };
        case "reset":
          return initialState;
        default:
          throw new Error("Unknown action");
      }
    }

.. important::

    Instead of defining event handler functions, the ``dispatch()`` calls can also
    happen right inside the JSX.
