Displaying Questions
====================
Adding new state ``index``, which is the current question index and pass it into
the ``Question`` component:

.. code-block:: jsx
    :emphasize-lines: 5,11,27

    const initialState = {
      questions: [],
      status: "loading",
      // index of currently displayed question
      index: 0,
    };

    {/* more stuff */}

    export default function App() {
      const [{ questions, status, index }, dispatch] = useReducer(
        reducer,
        initialState
      );

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
            {status === "active" && <Question question={questions[index]} />}
          </Main>
        </div>
      );
    }

Inside the ``Question`` component, we'll receive the question and display it:

.. code-block:: jsx
    :emphasize-lines: 1,4-11

    function Question({ question }) {
      return (
        <div>
          <h4>{question.question}</h4>
          <div className="options">
            {question.options.map((option) => (
              <button className="btn btn-option" key={option}>
                {option}
              </button>
            ))}
          </div>
        </div>
      );
    }

We can further move out the options as a separate component:

.. code-block:: jsx

    function Options({ question }) {
      return (
        <div className="options">
          {question.options.map((option) => (
            <button className="btn btn-option" key={option}>
              {option}
            </button>
          ))}
        </div>
      );
    }

    export default Options;

and import it into the ``Question`` component:

.. code-block:: jsx
    :emphasize-lines: 1,8

    import Options from "./Options";

    function Question({ question }) {
      console.log(question);
      return (
        <div>
          <h4>{question.question}</h4>
          <Options question={question} />
        </div>
      );
    }

    export default Question;