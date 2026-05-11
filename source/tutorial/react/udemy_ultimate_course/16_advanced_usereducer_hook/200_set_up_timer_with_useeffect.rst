Setting up a timer with useEffect
=================================
We want a timer to count down to 0 after the quiz game is started. When the timer
reaches zero before the game has finished, ...

Creating a new ``Timer`` component inside the app's ``Footer`` component:

.. code-block:: jsx
    :emphasize-lines: 8

    export default function App() {

    {/* more stuff */}

      return(
        {/* more stuff */}
            <Footer>
              <Timer />
              <NextButton
                dispatch={dispatch}
                answer={answer}
                index={index}
                numQuestions={numQuestions}
              ></NextButton>
            </Footer>
        {/* more stuff */}
      )

.. note::

    The ``Footer`` component merely returns all children:

    .. code-block:: jsx

        function Footer({ children }) {
          return <footer>{children}</footer>;
        }
        export default Footer;

Add ``secondsRemaining`` as additional state and create a case inside the ``reducer()``
function:

.. code-block:: jsx
    :emphasize-lines: 3,9-10,15-16,23

    const initialState = {
      {*/ more stuff */}
      secondsRemaining: 10,
    };

    function reducer(state, action) {
      switch (action.type) {
      {*/ more stuff */}
        case "countdown":
          return { ...state, secondsRemaining: state.secondsRemaining - 1 };
      {*/ more stuff */}
    }

    export default function App() {
      const [{ questions, status, index, answer, points, highscore, secondsRemaining }, dispatch] =
        useReducer(reducer, initialState);

      {/* more stuff */}

      return(
        {/* more stuff */}
            <Footer>
              <Timer dispatch={dispatch}/>
              <NextButton
                dispatch={dispatch}
                answer={answer}
                index={index}
                numQuestions={numQuestions}
              ></NextButton>
            </Footer>
        {/* more stuff */}
      )

The ``dispatch`` and ``secondsRemaining`` are accepted as props inside the ``Timer``
component and the ``secondsRemaining`` are reduced by 1 every second (1000 ms) using
the ``dispatch`` function:

.. code-block:: jsx

    import { useEffect } from "react";

    function Timer({ dispatch, secondsRemaining }) {
      useEffect(
        function () {
          // runs function every second
          setInterval(() => dispatch({ type: "countdown" }), 1000);
        },
        [dispatch]
      );
      return <div className="timer">{secondsRemaining}</div>;
    }

    export default Timer;

.. hint::

    Usually, larger components shouldn't be forced to re-render as often as every
    second. But for this small counter, this is no problem.

The countdown starts upon the initial rendering of ``Timer`` (dependency array is empty, ``[]``),
though the ``useEffect`` function as of now, runs endlessly (until the component is destroyed).
To fix that, we must check if the ``secondsRemaining`` reached zero, then update the ``state``
to ``"finished"`` to finish the game:

.. code-block:: jsx
    :emphasize-lines: 4-9

    function reducer(state, action) {
      switch (action.type) {
      {*/ more stuff */}
        case "countdown":
          return {
            ...state,
            secondsRemaining: state.secondsRemaining - 1,
            status: state.secondsRemaining === 0 ? "finished" : state.status,
          };
      {*/ more stuff */}
    }


.. note::

    The ``secondsRemaining`` are reset when the user restarts the game due to

    .. code-block:: jsx
        :emphasize-lines: 6

        function reducer(state, action) {
          switch (action.type) {
          {*/ more stuff */}
            case "restart":
              return {
                ...initialState,
                questions: state.questions,
                status: "ready",
                highscore: state.highscore,
          };
          {*/ more stuff */}
        }

A problem is seen, that the ``Timer`` never stops reducing the ``secondsRemaining``
leading to an immediate state change when starting a new game. As the timer is never
ended, starting a new game adds another timer - all of them subtracting from the
``secondsRemaining``, which count down to zero very fast after a while. To fix that we need
a **cleanup function** which runs, when the component is unmounted (also see
:ref:`tutorial_react_ultimate_useeffect_cleanup_function`). For this, the effect
function must return the cleanup function:

.. hint::

    Each ``setIntervall()`` call returns an id of the timer, which we can use to
    cancel the timer at any time using the ``cancelInterval()`` function.

.. code-block:: jsx
    :emphasize-lines: 8

    import { useEffect } from "react";

    function Timer({ dispatch, secondsRemaining }) {
      useEffect(
        function () {
          // runs function every second
          const id = setInterval(() => dispatch({ type: "countdown" }), 1000);
          return () => clearInterval(id);
        },
        [dispatch]
      );
      return <div className="timer">{secondsRemaining}</div>;
    }

    export default Timer;

.. hint::

    In *StrictMode* (which we use), each component is rendered twice, so before
    the change, two timers are started when starting the game. After closing them,
    only the timer of the second rendered component remains.

Further activities:

    * calculate total time for counter from the number of total questions
    * display ``secondsRemaining`` in format MM:SS
