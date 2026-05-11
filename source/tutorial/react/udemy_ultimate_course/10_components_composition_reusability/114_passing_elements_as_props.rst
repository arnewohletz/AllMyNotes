Passing Elements as Props
=========================
As an alternative to :ref:`composing components <tutorial_react_ultimate_component_composition>`,
component elements can also be passed as props:

The receiving component receives a prop, e.g. called ``element`` (name can be anything):

.. code-block:: jsx
    :emphasize-lines: 1,8

    function Box({ element }) {
      const [isOpen, setIsOpen] = useState(true);
      return (
        <div className="box">
          <button className="btn-toggle" onClick={() => setIsOpen((open) => !open)}>
            {isOpen ? "–" : "+"}
          </button>
          {isOpen && element}
        </div>
      );
    }

In the parent component, an equally named prop must be passed, which contains
all the JSX:

.. code-block:: jsx
    :emphasize-lines: 11,13-18

    export default function App() {
      const [movies, setMovies] = useState(tempMovieData);
      const [watched, setWatched] = useState(tempWatchedData);
      return (
        <>
          <NavBar>
            <Search />
            <NumResults movies={movies} />
          </NavBar>
          <Main>
            <Box element={<MovieList movies={movies} />} />
            <Box
              element={
                <>
                  <WatchedSummary watched={watched} />
                  <WatchedMovieList watched={watched} />{" "}
                </>
              }
            />
            {/* <Box>
              <MovieList movies={movies} />
            </Box>
            <Box>
              <>
                <WatchedSummary watched={watched} />
                <WatchedMovieList watched={watched} />{" "}
              </>
            </Box> */}
          </Main>
        </>
      );
    }

This method is used in some libraries, like `React Router`_.

This method is mainly used, if **multiple elements with different names** are
supposed to be passed into a component. With ``children`` **only one** such element
can be passed:

.. code-block:: jsx

    function PassMultiple() {
      return <ReceiveMultiple one={<One />} two={<Two />} three={<Three />} />;
    }

    function ReceiveMultiple({ one, two, three }) {
      return (
        <>
          <p>{one}</p>
          <p>{two}</p>
          <p>{three}</p>
        </>
      );
    }

.. hint::

    Composing components using the ``children`` prop is the **preferred way** to
    compose components and prevent prop drilling. The prop method should only be
    used, if needed.

.. _React Router: https://reactrouter.com/