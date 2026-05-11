Initializing State With a Callback (Lazy Initial State)
=======================================================
Save data in localStorage
-------------------------
We want to persist data into the *local storage*.

.. hint::

    The *local storage* is a key-value pair storage inside the browser, which is
    specific to a URL.

Two places to do that:

    #. inside the handler function (here: ``handleAddWatched(movie)``
    #. inside an effect function (here: called whenever the ``watched`` state variable
       is updated

**Inside handler function**

.. code-block:: jsx
    :emphasize-lines: 4

      function handleAddWatched(movie) {
        setWatched((watched) => JSON.stringify([...watched, movie]));

        localStorage.setItem("watched", [...watched, movie]);
      }

* at the time of saving the updated ``watched`` to the local storage, the variabel
  hasn't been updated yet (still without the new ``movie``, hence it is in *stale state*),
  so we must create the array to be stored manually via :javascript:`[...watched, movie]`
* the local storage cannot store arrays, but needs a string type, so we convert the
  array to a string via :javascript:`JSON.stringify()`

**Inside an effect function**

This way, we can reuse that effect function at various occurrences.

.. code-block:: jsx

      useEffect(
        function () {
          localStorage.setItem("watched", JSON.stringify(watched));
        },
        [watched]
      );

* at the point of calling the effect function, the ``watched`` state variable has
  **already been updated**, so no need to manually create it
* when refreshing the page, the localStorage's watched variable becomes an empty array,
  it is the default value of ``watched``

Load data from localStorage
---------------------------
Next up, we want to restore the watched movies from localStorage.

.. code-block:: jsx

      const [watched, setWatched] = useState(function () {
        const storedValue = JSON.parse(localStorage.getItem("watched"));
        return storedValue;
      });

* Define a callback function as the default value of the ``watched`` state variable
* This function is **only called on initial render** (just like the default value is
  only set during initial render)
* you **must not** use a function call, e.g.

    .. code-block:: javascript

        // this is not good
        const [watched, setWatched] = useState(JSON.parse(localStorage.getItem("watched"));

    React would call this function **on every re-render**, though ignoring its value.

.. hint::

    The function **must** be pure JavaScript (no JSX) and **must not** receive any arguments!

.. hint::

    **Use effects over handler functions**

    Thanks to the nature of effects, when **deleting an item** from the ``watched`` state variable,
    the effect function we previously defined would run. If we had used the *handler function*
    ``handleAddWatched``, we'd also have to manually delete the item from ``watched`` within
    the ``handleDeleteWatched`` handler function.