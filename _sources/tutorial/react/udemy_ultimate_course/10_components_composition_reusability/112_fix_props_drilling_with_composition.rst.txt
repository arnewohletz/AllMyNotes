.. _tutorial_react_ultimate_component_composition:

Fix Props Drilling by using Component Composition
=================================================
Problem A: Props drilling

    When a state variable is needed deep inside different component tree, the state
    lives in the highest common parent and must be dragged through numerous components
    which don't use it, except passing it along.

Problem B: Nesting components

    A component A, nesting a component B, cannot be reused to contains something
    else but component B. So there must exists A.1 containing B and A.2 containing
    component C.

Solution: Component Composition

    Instead of "hardcoding" the inner component into the outer component, like this:

    .. code-block:: jsx

        function Modal() {
            return (
                <div className="modal">
                    <Success />
                </div>
            )
        }

    .. hint::

        The above component might as well be called ``SuccessModal`` because the
        the ``Success`` component is always included.

    make the outer component (here: Modal) accept the ``children`` prop and return
    it inside the JSX:

    .. code-block:: jsx

        function Modal( {children} ) {
            return (
                <div className="modal">
                    {children}
                </div>
            )
        }

    That way, whenever the component is needed, it can be composed as desired:

    .. code-block:: jsx

        <Modal>
            <Success />
        <Modal />

**Component composition** is the combination of different components using the
``children`` prop (or explicitly defined props).

We compose component when

    * create highly reusable and flexible components
    * fix prop drilling problem (great for layouts)

Fix prop drilling problem:

Instead of

.. code-block:: jsx

    export default function App() {
      const [movies, setMovies] = useState(tempMovieData);
      return (
        <>
          <NavBar movies={movies} />
          <Main movies={movies} />
        </>
      );
    }

    function NavBar({ movies }) {
      return (
        <nav className="nav-bar">
          <Logo />
          <Search />
          <NumResults movies={movies} />
        </nav>
      );
    }

    function NumResults({ movies }) {
      return (
        <p className="num-results">
          Found <strong>{movies.length}</strong> results
        </p>
      );
    }

we pass components of ``NavBar`` into the ``App``'s JSX, receiving it as ``children``
inside ``NavBar``:

.. code-block:: jsx

    export default function App() {
      const [movies, setMovies] = useState(tempMovieData);
      return (
        <>
          <NavBar>
            <Logo />
            <Search />
            <NumResults movies={movies} />
          </NavBar>
          <Main movies={movies} />
        </>
      );
    }

    function NavBar({ children }) {
      return <nav className="nav-bar">{children}</nav>;
    }

    function NumResults({ movies }) {
      return (
        <p className="num-results">
          Found <strong>{movies.length}</strong> results
        </p>
      );
    }

It is basically, defining all components higher up in the component tree (where
the prop state variable lives) and passing it through all props-forwarding components
via the ``children`` property (only explicitly passing it from the second last to
the component, which actually uses the prop).

Another advantage is that we are able to a bigger part of the **component tree**
inside a parent component's JSX.