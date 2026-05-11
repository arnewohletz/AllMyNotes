One More Effect: Listening to a keypress
========================================
Feature: the user presses the kbd:`ESC` key to close the movie details view
(alternatively, to clicking the *Close* button). For this, we want to
**globally listen** to the keypress.

For this, we attach an event listener to the entire application. For this, we
step out of React, by adding an event listener to the document:

.. hint::

    React calls this method an *escape hatch*, as we directly manipulating the DOM,
    instead of doing it the "React way".

.. code-block:: jsx
    :emphasize-lines: 5-12

    export default function App() {

        {/* more here */}

      useEffect(function () {
        document.addEventListener("keydown", function (e) {
          if (e.code === "Escape") {
            handleCloseMovie();
            console.log("Closing");
          }
        });
      }, []);

        {/* more here */}
    }

Moreover, we only want the event listener to be added, when a movie is opened.
So, we **move it** into the ``MovieDetails`` component (requires renaming the
``handleCloseMovie()`` function to ``onCloseMovie()``):

.. code-block:: jsx
    :emphasize-lines: 1,8,12

    export default function MovieDetails() {

        {/* more here */}

      useEffect(function () {
        document.addEventListener("keydown", function (e) {
          if (e.code === "Escape") {
            onCloseMovie();
            console.log("Closing");
          }
        });
      }, [onCloseMovie]);

        {/* more here */}
    }

This also requires to add ``onCloseMovie`` into the dependency array - more on
why we need that later.

The next problem is, that now for each movie a separate event listener is added
to the document.
Opening multiple movies add multiple event listeners. What we want is only to
have one event handler at a time, from the movie, which is currently open.

To fix, we must remove the event listener inside the effect's cleanup function:

.. code-block:: jsx

      useEffect(
        function () {
          function callback(e) {
            if (e.code === "Escape") {
              onCloseMovie();
              console.log("Closing");
            }
          }
          document.addEventListener("keydown", callback);
          return function () {
            document.removeEventListener("keydown", callback);
          };
        },
        [onCloseMovie]
      );

As the ``removeEventListener`` must remove the **exact same listener**, that was previously
added, the listener function must match exactly, so we define it separately inside a ``callback``
function and use it for both the ``addEventListener`` call and the ``removeEventListener`` call.


