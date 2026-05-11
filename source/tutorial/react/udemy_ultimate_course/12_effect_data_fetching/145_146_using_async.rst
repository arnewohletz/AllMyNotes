Using the async function
========================
The ``useEffect()`` method **does not** accept an asynchronous function as
callback methods (to avoid race conditions), so this **is not allowed**:

.. code-block:: javascript

    {*/ NOT OK */}
      useEffect(async function () {
        await fetch(
          `http://www.omdbapi.com/?apikey=${KEY}&s=goldeneye`
            .then((res) => res.json())
            .then((data) => setMovies(data.Search))
        );
      }, []);

To make the code cleaner using an ``async / await``, such a function must be
put inside a synchronous wrapper function:

.. code-block:: javascript

    {*/ GOOD */}
      useEffect(function () {
        async function fetchMovies() {
          const res = await fetch(
            `http://www.omdbapi.com/?apikey=${KEY}&s=goldeneye`
          );
          const data = await res.json();
          setMovies(data.Search);
        }
        fetchMovies();
      }, []);

In the anonymous function, the asynchronous ``fetchMovies()`` function is first
declared, then executed.

.. hint::

    In development mode, the effect is called **twice** due to the Strict-Mode
    being active:

    .. code-block:: jsx

        root.render(
          <React.StrictMode>
            <App />
          </React.StrictMode>
        );

Adding a loading state
======================
In order to add a loading message, while data is fetched, do the following:

#. Create a state variable, like ``isLoading``, with ``false`` as default
#. Inside the async fetch function set it to ``true``
#. After the fetch, set is it to ``false``
#. Do conditional rendering, giving it a *loading* component when ``isLoading``
   is ``true``, otherwise display the real data component
#. Create a *loading* component which displays something like *Loading...*


.. code-block:: jsx
    :emphasize-lines: 4,8,14,26,38-40

    export default function App() {
      const [movies, setMovies] = useState([]);
      const [watched, setWatched] = useState([]);
      const [isLoading, setIsLoading] = useState(false);

      useEffect(function () {
        async function fetchMovies() {
          setIsLoading(true);
          const res = await fetch(
            `http://www.omdbapi.com/?apikey=${KEY}&s=goldeneye`
          );
          const data = await res.json();
          setMovies(data.Search);
          setIsLoading(false);
        }
        fetchMovies();
      }, []);

      return (
        <>
          <NavBar>
            <Search />
            <NumResults movies={movies} />
          </NavBar>
          <Main>
            <Box>{isLoading ? <Loader /> : <MovieList movies={movies} />}</Box>
            <Box>
              <>
                <WatchedSummary watched={watched} />
                <WatchedMovieList watched={watched} />{" "}
              </>
            </Box>
          </Main>
        </>
      );
    }

    function Loader() {
      return <p className="loader">Loading ...</p>;
    }
