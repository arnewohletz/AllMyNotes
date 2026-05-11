Loading questions from Fake API
===============================
Instead of loading data from a "real" API, we want to serve data (here: quiz questions)
from a JSON file.

**Prerequisites**

* JSON file containing questions. Here in this form (excerpt):

    .. code-block:: json

        {
          "questions": [
            {
              "question": "Which is the most popular JavaScript framework?",
              "options": ["Angular", "React", "Svelte", "Vue"],
              "correctOption": 1,
              "points": 10
            },
            {
              "question": "Which company invented React?",
              "options": ["Google", "Apple", "Netflix", "Facebook"],
              "correctOption": 3,
              "points": 10
            }
        }

**Steps**

#. Place file somewhere within your React project (e.g. ``data/questions.json``).
#. Install the `json-server`_ NPM package:

    .. code-block:: none

        $ npm install json-server

#. Add a launch command to the ``"scripts"`` section of your ``packages.json`` file
   (adjust port number to your liking):

    .. code-block:: json
        :emphasize-lines: 6

          "scripts": {
            "start": "react-scripts start",
            "build": "react-scripts build",
            "test": "react-scripts test",
            "eject": "react-scripts eject",
            "server": "json-server --watch data/questions.json --port 8000"
          }

#. Start the server:

    .. code-block:: none

        $ npm run server

#. Access the served file in the browser (here: ``http://localhost:8000/questions``).

    .. note::

        The server uses the JSON's root keys (here: ``questions``) as endpoints,
        which will display the entire content of this key (here, the array).

.. _json-server: https://www.npmjs.com/package/json-server

**Add data loading to project**

#. Define a effect, which loads the data from the fake API
#. Define a default *reducer*, which will manage the state

    .. code-block:: jsx
        :emphasize-lines: 2, 4-9

        export default function App() {
          const [state, dispatch] = useReducer(reducer, initialState);

          useEffect(function () {
            fetch("http://localhost:8000/questions")
              .then((res) => res.json())
              .then((data) => dispatch({ type: "dataReceived", payload: data }))
              .catch((err) => dispatch({ type: "dataFailed" }));
          }, []);

          return (
            <div className="App">
              <Header />
              <Main>
                <p>1/15</p>
                <p>Question</p>
              </Main>
            </div>
          );
        }

#. Define the ``initialState`` and the ``reducer()`` function:

    .. code-block:: jsx
        :emphasize-lines: 1,3,6,8-10,12-13,15

        const initialState = {
          // questions is empty array before those are fetched from JSON file
          questions: [],
          // instead of isLoading, isError, ... we have a status with those values:
          // "loading", "error", "ready", "active", "finished"
          status: "loading",
        };
        function reducer(state, action) {
          switch (action.type) {
            case "dataReceived":
              // reducer allows for setting multiple state at once (here: questions + status)
              return { ...state, questions: action.payload, status: "ready" };
            case "dataFailed":
              // in case of an error during fetching data
              return { ...state, state: "error" };
            default:
              throw new Error("Action unknown");
          }
        }

    * the initial state will contain the ``questions`` array and the ``status``
    * the ``reducer`` again contains a switch-statement, returning the new state
      for the types ``"dataReceived"`` and ``"dataFailed"`` (and a default error
      for unhandled action types), being able to **set multiple state variables at once**

Handling Loading, Error and Ready Status
========================================
Using `nested destructuring`_, we can declare the ``questions`` and ``status`` state
variables right inside the ``useReducer`` statement:

.. code-block:: javascript
    :emphasize-lines: 2

    export default function App() {
      const [{ questions, status }, dispatch] = useReducer(reducer, initialState);
      {/* more stuff */}
    }

.. _nested destructuring: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Destructuring#object_destructuring

and use the ``status`` to load some conditional JSX:

.. code-block:: jsx
    :emphasize-lines: 3, 11-13

    export default function App() {
      const [{ questions, status }, dispatch] = useReducer(reducer, initialState);
      const numQuestions = questions.length;

      {/* more stuff */}

      return (
        <div className="App">
          <Header />
          <Main>
            {status === "loading" && <Loader />}
            {status === "error" && <Error />}
            {status === "ready" && <StartScreen />}
          </Main>
        </div>
      );
    }

and including a new component ``StartScreen`` which receives the ``numQuestions``:

.. code-block:: jsx

    function StartScreen({ numQuestions }) {
      return (
        <div className="start">
          <h2>Welcome to the React Quiz</h2>
          <h3>{numQuestions} questions to test your React mastery</h3>
          <button className="btn btn-ui">Let us start</button>
        </div>
      );
    }

    export default StartScreen;

Start new quiz
==============
In order to start a quiz, a question must be displayed. So adding another conditional
rendering using a new ``Question`` component:

.. code-block:: jsx
    :emphasize-lines: 13-15

    export default function App() {
      const [{ questions, status }, dispatch] = useReducer(reducer, initialState);
      const numQuestions = questions.length;

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
            {status === "active" && <Question />}
          </Main>
        </div>
      );
    }

* we pass the ``dispatch`` function as prop, since the ``Question`` component
  needs to call it, changing the ``status`` state when clicking the *Start*-Button

Next we need an additional handler inside the ``reducer`` function naming the
*action* ``"start"``:

.. code-block:: jsx
    :emphasize-lines: 9-10

    function reducer(state, action) {
      switch (action.type) {
        case "dataReceived":
          // reducer allows for setting multiple state at once (here: questions + status)
          return { ...state, questions: action.payload, status: "ready" };
        case "dataFailed":
          // in case of an error during fetching data
          return { ...state, status: "error" };
        case "start":
          return { ...state, status: "active" };
        default:
          throw new Error("Action unknown");
      }
    }

Inside the ``StartScreen`` component, the button needs to call the ``dispatch`` function
with the new type:

.. code-block:: jsx
    :emphasize-lines: 8

    function StartScreen({ numQuestions, dispatch }) {
      return (
        <div className="start">
          <h2>Welcome to the React Quiz</h2>
          <h3>{numQuestions} questions to test your React mastery</h3>
          <button
            className="btn btn-ui"
            onClick={() => dispatch({ type: "start" })}
          >
            Let us start
          </button>
        </div>
      );
    }

    export default StartScreen;

And finally, creating the new ``Question`` component:

.. code-block:: jsx

    function Question() {
      return <div>Question</div>;
    }

    export default Question;
