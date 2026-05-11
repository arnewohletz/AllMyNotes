State Update Batching
=====================
State updates are *batched*:

    * renders are **not** triggered immediately, but **scheduled** for when the
      JS engine has some "free time". There is also batching of multiple ``setState``
      calls in event handlers:

        If a event handler functions sets multiple state variables, not each
        variable triggers a separate re-render, but all state changes are *batched*
        and done **in one go**, triggering a **single re-render + commit**

    * the moment, when a state variable is already changed, but the result is not
      yet rendered is called the *stale state* -> therefor updating state in React
      is **asynchronous** (only updated **after** the re-render)

    * same applies, when there is only **one state variable** to be updated

    .. important::

        The updated state is only available **after** the re-render, not immediately.

    * if we need the state variable to be updated immediately, e.g. a second state
      depends on the updated value of the first state, we use ``setState`` with
      callback (:javascript:`setAnswer(answer=>...)`)

From *React v18* onwards, *automatic batching* is also applied to

    * timeouts (function is called after a certain time), e.g.

        .. code-block:: javascript

            setTimeout(reset, 1000);

    * after a promise has been fulfilled, e.g.

        .. code-block:: javascript

            fetchStuff().then(reset);

    * native events, e.g.

        .. code-block:: javascript

            el.addEventListener("click", reset);

    .. hint::

        Before React 18, a re-render + commit was executed for each updated state variable.

.. hint::

    *Automatic batching* can be escaped by wrapping state update in ``ReactDom.flushSync()``
    (but we will never need this).

In Practice
-----------
How to update a state variable multiple times within the same handler function?

**Problem**

The state variable is only updated after re-render. This makes multiple calls to
the same setter function impossible:

.. code-block:: javascript

    function TabContent({ item }) {
      const [likes, setLikes] = useState(0);

      function handleTripleInc() {
        setLikes(likes + 1);
        setLikes(likes + 1);
        setLikes(likes + 1);
      }

The ``likes`` variable still will only increase by 1.

**Solution**

Use a callback function to change the state, as previously explained in
:ref:`tutorial_react_ultimate_update_state_based_on_current_state`:

.. code-block:: javascript

      function handleTripleInc() {
        setLikes((likes) => likes + 1);
        setLikes((likes) => likes + 1);
        setLikes((likes) => likes + 1);
      }

This works, because the callback function is only executed **after** the re-render
has happened. Here, ``setLikes`` is passed the callback function argument
:javascript:`(likes) => likes + 1`. The setter function just sets the new value to
this callback function, but does not execute it. After exiting ``handleTripleInc()``,
React updates the state to the callback function, only then executing it.

As mentioned above, state batching also is applied, when the event handler function
uses a :javascript:`setTimeout(handleSomething, 1000)` function call. Here, ``handleSomething``
is called after 1000 ms:

.. code-block:: javascript
    :emphasize-lines: 7

      function handleUndo() {
        setShowDetails(true);
        setLikes(0);
      }

      function handleUndoLater() {
        setTimeout(handleUndo, 2000);
      }
