Handling errors
===============
Cover the case, that there is a network issue while fetching data:

#. new state variable for ``error``
#. put fetch function inside the ``useEffect()`` call inside a try-catch block
#. put isLoading to ``false`` reset into ``finally`` block (to run it even in case
   of an error)
#. define conditional rendering for all cases:

    * data is loading
    * data has been loaded
    * data loading failed (e.g. network error)


.. code-block:: jsx
    :emphasize-lines: 7,11-24,37-39

    const KEY = "38602acf";

    export default function App() {
      const [movies, setMovies] = useState([]);
      const [watched, setWatched] = useState([]);
      const [isLoading, setIsLoading] = useState(false);
      const [error, setError] = useState("");

      useEffect(function () {
        async function fetchMovies() {
          try {
            setIsLoading(true);
            const res = await fetch(
              `http://www.omdbapi.com/?apikey=${KEY}&s=goldeneye`
            );
            if (!res.ok)
              throw new Error("Something went wrong with fetching movies");
            const data = await res.json();
            setMovies(data.Search);
          } catch (error) {
            setError(error.message);
          } finally {
            setIsLoading(false);
          }
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
            <Box>
              {isLoading && <Loader />}
              {!isLoading && !error && <MovieList movies={movies} />}
              {error && <ErrorMessage message={error.message} />}
            </Box>
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

Cover the case, if no movie is found:

#. define another condition if API returns zero result (here: return {``data.Response === false``}
   throwing another error

.. code-block:: jsx
    :emphasize-lines: 22-24

    const KEY = "38602acf";
    const query = "gdgdfgdfgdf";

    export default function App() {
      const [movies, setMovies] = useState([]);
      const [watched, setWatched] = useState([]);
      const [isLoading, setIsLoading] = useState(false);
      const [error, setError] = useState("");

      useEffect(function () {
        async function fetchMovies() {
          try {
            setIsLoading(true);
            const res = await fetch(
              `http://www.omdbapi.com/?apikey=${KEY}&s=${query}`
            );
            if (!res.ok) {
              throw new Error("Something went wrong with fetching movies");
            }

            const data = await res.json();
            if (data.Response === "False") {
              throw new Error("No matching movies found");
            }
            setMovies(data.Search);
          } catch (err) {
            setError(err.message);
          } finally {
            setIsLoading(false);
          }
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
            <Box>
              {isLoading && <Loader />}
              {!isLoading && !error && <MovieList movies={movies} />}
              {error && <ErrorMessage message={error} />}
            </Box>
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

    function ErrorMessage({ message }) {
      return <p className="error">{message}</p>;
    }
