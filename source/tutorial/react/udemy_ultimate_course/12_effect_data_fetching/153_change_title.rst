Changing the page title
=======================
* Changing the page title is done via a side effect, as we need to interact with
  the world outside our React application
* in our case, we want to update the title whenever the displayed movie changed,
  in which case the ``MovieDetails`` page is re-rendered or mounted
* we need to add another ``useEffect`` method to ``MovieDetails``

.. important::

    An effect is only supposed to **do one thing**. For two things, we need two
    separate effects.

Adding the effect to ``MovieDetails``:

.. code-block:: jsx
    :emphasize-lines: 24-30

    function MovieDetails({ selectedId, onCloseMovie, onAddWatched, watched }) {
      const [movie, setMovie] = useState({});
      const [isLoading, setIsLoading] = useState(false);
      const [userRating, setUserRating] = useState("");
      const isWatched = watched.map((movie) => movie.imdbID).includes(selectedId);

      const watchedUserRating = watched.find(
        (movie) => movie.imdbID === selectedId
      )?.userRating;

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
          if (!title) return;
          document.title = `Movie | ${title}`;
        },
        [title]
      );

