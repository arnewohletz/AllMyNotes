More Details on useState
========================
useState's default value is only used at initial rendering
----------------------------------------------------------
The ``useState`` default value is only used **at the initial render**. When defining

.. code-block:: jsx
    :emphasize-lines: 3,10,26

    function MovieDetails({ selectedId, onCloseMovie, onAddWatched, watched }) {
      const [movie, setMovie] = useState({});
      const [isTop, setIsTop] = useState(imdbRating > 8);

      const {
        Title: title,
        Year: year,
        Poster: poster,
        Runtime: runtime,
        imdbRating,
        Plot: plot,
        Released: released,
        Actors: actors,
        Director: director,
        Genre: genre,
      } = movie;

      useEffect(
        function () {
          async function getMovieDetails() {
            setIsLoading(true);
            const res = await fetch(
              `http://www.omdbapi.com/?apikey=${KEY}&i=${selectedId}`
            );
            const data = await res.json();
            setMovie(data);
            setUserRating(userRating);
            setIsLoading(false);
          }
          getMovieDetails();
        },
        [selectedId, userRating]
      );

        {/* more stuff */}
    }

where ``imdbRating`` is first assigned to a value **within** a ``useEffect()``
function call, then **at the initial render**, which is done **before** executing
any ``useEffect`` hooks, the initial default value is set to ``undefined`` (as
``imdbRating`` is ``undefined``).

To fix it, the state needs has be updated inside a ``useEffect`` function:

.. code-block:: jsx
    :emphasize-lines: 5-10

    function MovieDetails({ selectedId, onCloseMovie, onAddWatched, watched }) {
      const [movie, setMovie] = useState({});
      const [isTop, setIsTop] = useState(imdbRating > 8);

      useEffect(
        function () {
          setIsTop(imdbRating > 8);
        },
        [imdbRating]
      );

      {/* more stuff */}

    }

A better solution is not to define ``isTop`` as a state variable, but to derive
the variable from the ``imdbRating`` state:

.. code-block:: jsx
    :emphasize-lines: 8,16

    function MovieDetails({ selectedId, onCloseMovie, onAddWatched, watched }) {
      const [movie, setMovie] = useState({});
      const {
        Title: title,
        Year: year,
        Poster: poster,
        Runtime: runtime,
        imdbRating,
        Plot: plot,
        Released: released,
        Actors: actors,
        Director: director,
        Genre: genre,
      } = movie;

      const isTop = imdbRating > 8;

      {/* more stuff */}

    }

State variables are set asynchronously
--------------------------------------
In a handler function, when setting a state variable, like this

.. code-block:: jsx
    :emphasize-lines: 5,18-19

    function MovieDetails({ selectedId, onCloseMovie, onAddWatched, watched }) {

      {/* more stuff */}

      const [avgRating, setAvgRating] = useState(0);

      function handleAdd() {
        const newWatchedMovie = {
          imdbID: selectedId,
          title,
          year,
          poster,
          imdbRating: Number(imdbRating),
          runtime: Number(runtime.split(" ").at(0)),
          userRating,
        };
        onAddWatched(newWatchedMovie);
        setAvgRating(Number(imdbRating));
        alert(avgRating);
        // onCloseMovie();
      }

      {/* more stuff */}

    }

the alert reports the value ``0``, not the value of ``imdbRating``. This is because
the state variable update happens asynchronously. We don't get the new value right
after setting it. Once finished, React updates the state variable and re-renders the UI.

As they update synchronously, when defining a state variable value based on another
state variable's value, use a callback function. This is called **after** the depending
state variable has been updated (due to asynchronous update and update batching):

.. code-block:: jsx
    :emphasize-lines: 19

    function MovieDetails({ selectedId, onCloseMovie, onAddWatched, watched }) {

      {/* more stuff */}

      const [userRating, setUserRating] = useState("");
      const [avgRating, setAvgRating] = useState(0);

      function handleAdd() {
        const newWatchedMovie = {
          imdbID: selectedId,
          title,
          year,
          poster,
          imdbRating: Number(imdbRating),
          runtime: Number(runtime.split(" ").at(0)),
          userRating,
        };
        onAddWatched(newWatchedMovie);
        setAvgRating((x) => (x + userRating) / 2);
        // onCloseMovie();
      }

      {/* more stuff */}

    }

.. hint::

    The variable name passed into the callback function can be anything, here ``x``.
    It is assumed by React, that this is the current value of that setter's state variable.


