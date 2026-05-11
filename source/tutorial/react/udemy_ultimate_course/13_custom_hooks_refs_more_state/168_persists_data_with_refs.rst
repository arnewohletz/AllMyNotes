Refs to persist data between renders
====================================
The other use case of *refs* are to persist data between re-renders.

**Task:** Add counter, which stores the number of how many times the user changed
the rating of a movie. The data is not supposed to appear on screen (does not cause
a re-render on update). The counter value is eventually stored when adding the movie
to the watched list.

.. code-block:: jsx
    :emphasize-lines: 3

    function MovieDetails({ selectedId, onCloseMovie, onAddWatched, watched }) {

      const countRef = useRef(0);

      {/* more stuff */}
    }

As the Ref **must not** be updated in render logic, it must be put into an effect:

.. code-block:: jsx
    :emphasize-lines: 5-12

    function MovieDetails({ selectedId, onCloseMovie, onAddWatched, watched }) {

      const countRef = useRef(0);

      useEffect(
        function () {
          if (userRating) {
            countRef.current = countRef.current + 1;
          }
        },
        [userRating]
      );

      {/* more stuff */}
    }


* the effect runs at every change of ``userRating`` and during initial rendering
* the if-statement prevents the counter from increasing during initial render,
  where the user has not yet rated the movie

To save the counter, it is added to the ``newWatchedMovie`` object inside the respective
event handler function (here: ``handleAdd()``):

.. code-block:: jsx
    :emphasize-lines: 10

      function handleAdd() {
        const newWatchedMovie = {
          imdbID: selectedId,
          title,
          year,
          poster,
          imdbRating: Number(imdbRating),
          runtime: Number(runtime.split(" ").at(0)),
          userRating,
          countRatingDecisions: countRef.current,
        };
        onAddWatched(newWatchedMovie);
      }

The Ref value can now be checked in the React Devtool's Component View under the
respective component and, in our case, in the localStorage.

.. hint::

    This does not work for "normal" variables -> state is re-set back to initial
    value at each re-render.
