Handling answers
================
We need to save the selected answer as a new piece of state and make the ``reducer``
handle the selection of an answer and destructure it from ``initialState``:

.. code-block::
    :emphasize-lines: 5,15-16,23

    const initialState = {
      questions: [],
      status: "loading",
      index: 0,
      answer: null,
    };

    function reducer(state, action) {
      switch (action.type) {
        case "dataReceived":
          return { ...state, questions: action.payload, status: "ready" };

        {/* more stuff */}

        case "newAnswer":
          return { ...state, answer: action.payload };
        default:
          throw new Error("Action unknown");
      }
    }

    export default function App() {
      const [{ questions, status, index, answer }, dispatch] = useReducer(
        reducer,
        initialState
      );
      {/* more stuff */}
    }

The "newAnswer" action will dispatched in the ``Options`` component, again by passing
the ``dispatch`` function into it:

.. code-block:: jsx
    :emphasize-lines: 14-18

    export default function App() {
      {/* more stuff */}

      return (
        <div className="App">
          <Header />
          <Main>
            {status === "loading" && <Loader />}
            {status === "error" && <Error />}
            {status === "ready" && (
              <StartScreen numQuestions={numQuestions} dispatch={dispatch} />
            )}
            {status === "active" && (
              <Question
                question={questions[index]}
                dispatch={dispatch}
                answer={answer}
              />
            )}
          </Main>
        </div>
      );
    }

receiving those props inside ``Question`` and passing them into ``Options``:

.. code-block:: jsx
    :emphasize-lines: 1,6

    export default function Question({ question, dispatch, answer }) {
      console.log(question);
      return (
        <div>
          <h4>{question.question}</h4>
          <Options question={question} dispatch={dispatch} answer={answer} />
        </div>
      );
    }

and here calling the ``dispatch`` function passing the index of each option:

.. code-block:: jsx
    :emphasize-lines: 1,4,8

    export default function Options({ question, dispatch, answer }) {
      return (
        <div className="options">
          {question.options.map((option, index) => (
            <button
              className="btn btn-option"
              key={option}
              onClick={() => dispatch({ type: "newAnswer", payload: index })}
            >
              {option}
            </button>
          ))}
        </div>
      );
    }

Then, we'll use the ``answer`` state to conditionally assign another classname
to the selected answer button:

.. code-block:: jsx
    :emphasize-lines: 2,7-13,15

    export default function Options({ question, dispatch, answer }) {
      const hasAnswered = answer !== null;
      return (
        <div className="options">
          {question.options.map((option, index) => (
            <button
              className={`btn btn-option ${index === answer ? "answer" : ""} ${
                hasAnswered
                  ? index === question.correctOption
                    ? "correct"
                    : "wrong"
                  : ""
              }`}
              key={option}
              disabled={hasAnswered}
              onClick={() => dispatch({ type: "newAnswer", payload: index })}
            >
              {option}
            </button>
          ))}
        </div>
      );
    }

* ``${index === answer ? "answer" : ""}`` styles the selected answer option
* ``${hasAnswered ? index === question.correctOption ? "correct" : "wrong" : ""}`` styles the correct
  and false answer options **after** an answer has been given
* ``disabled={hasAnswered}`` disables the option buttons after an answer has been given

To display a progress score, we need another state variable:

.. code-block:: jsx
    :emphasize-lines: 6

    const initialState = {
      questions: [],
      status: "loading",
      index: 0,
      answer: null,
      points: 0,
    };

The points are supposed to be updated upon the user giving an answer, so inside the
``"newAnswer"`` case of the ``reducer`` function. Points should be added, if the
answer is correct only:

.. code-block:: jsx
    :emphasize-lines: 6,10-13

    function reducer(state, action) {

        {/* more stuff */}

        case "newAnswer":
          const question = state.questions.at(state.index);
          return {
            ...state,
            answer: action.payload,
            points:
              action.payload === question.correctOption
                ? state.points + 1
                : state.points,
          };

        {/* more stuff */}

    }

* to validate, we first get the current question from the state (at current index)
* we then check if the selected answer (``action.payload``) is matching the correct
  answer (``question.correctOption``), in which case increasing the value by 1

.. important::

    As shown above for the ``points``, it is encouraged to put as much logic for
    updating the state into the ``reducer`` function.