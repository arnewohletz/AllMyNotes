Advanced Pattern: A Custom Provider and Hook
============================================
Custom Provider
---------------
Using the regular context provider and hook is perfectly fine, though created customized
versions may improve the structure, cleaning up the ``App`` component.

The idea is to move all state and *state-updating* logic into the Provider, so
only a refactoring of the existing functionality.

For this, we create ``PostContext.js``, containing a ``PostProvider`` class and
put all the required content here:

.. code-block:: jsx
    :linenos:
    :emphasize-lines: 5,7,14,40,48,52

    import { faker } from "@faker-js/faker";
    import { createContext, useState } from "react";

    // 1) Create new context
    const PostContext = createContext();

    function createRandomPost() {
      return {
        title: `${faker.hacker.adjective()} ${faker.hacker.noun()}`,
        body: faker.hacker.phrase(),
      };
    }

    function PostProvider({ children }) {
      const [posts, setPosts] = useState(() =>
        Array.from({ length: 30 }, () => createRandomPost()),
      );
      const [searchQuery, setSearchQuery] = useState("");

      // Derived state. These are the posts that will actually be displayed
      const searchedPosts =
        searchQuery.length > 0
          ? posts.filter((post) =>
              `${post.title} ${post.body}`
                .toLowerCase()
                .includes(searchQuery.toLowerCase()),
            )
          : posts;

      function handleAddPost(post) {
        setPosts((posts) => [post, ...posts]);
      }

      function handleClearPosts() {
        setPosts([]);
      }

      return (
        // 2) Provide value to child components
        <PostContext.Provider
          value={{
            posts: searchedPosts,
            onAddPost: handleAddPost,
            onClearPosts: handleAddPost,
            searchQuery,
            setSearchQuery,
          }}
        >{children}</PostContext.Provider>
      );
    }

    export { PostProvider, PostContext };

:line 5:
    Create the ``PostContext`` as a regular Context (as before).

:line 7-12:
    Copy of the ``createRandomPost()`` method (original stays in ``App.js`` as it
    it also needed there -> usually, this should be moved to separate file).

:line 14:
    Declaration of ``PostProvider``. It requires the ``children`` property, because
    it will contain all JSX of the component which uses it, e.g.:

    .. code-block:: jsx
        :emphasize-lines: 13-18

        function App() {

            {/* other stuff */}

          return (
            <section>
              <button
                onClick={() => setIsFakeDark((isFakeDark) => !isFakeDark)}
                className="btn-fake-dark-mode"
              >
                {isFakeDark ? "☀️" : "🌙"}
              </button>
              <PostProvider>
                <Header />
                <Main />
                <Archive />
                <Footer />
              </PostProvider>
            </section>
          );
        }

    .. note::

        The ``PostProvider`` only encloses the components that actually need it,
        excluding the ``<button>`` element.

:line 15-36:
    All state updating logic functions of ``PostProvider``.

:line 40-48:
    The ``PostContext`` must return its ``Provider`` (as before) passing the ``value``
    object. Also, it must pass down the ``children`` property, which contains all the
    JSX that the component wraps into the ``PostContext`` (see example on comment to
    line 14).

:line 52:
    Both the ``PostProvider`` and the ``PostContext`` must be exported, as they both
    used in ``App.js``.

    As before, ``PostContext`` is used to access the contents of ``value``, whereas
    ``<PostProvider>`` is used instead of ``<PostContext.Provider>`` inside the
    JSX of the top level component (here: ``App``).

Custom Hook
-----------
So far, we consume the context by calling the ``useContext()`` method, e.g.:

.. code-block:: jsx

    const { onClearPosts } = useContext(PostContext);

The ``useContext()`` call be refactored into a custom hook. This is **common pattern**
to put it into the same file as the custom provider (here ``PostContext.js``):

.. code-block:: jsx
    :emphasize-lines: 5-8,10

    function PostProvider({ children }) {
      {/* my custom provider stuff */}
    }

    function usePosts() {
      const context = useContext(PostContext);
      return context;
    }

    export { PostProvider, usePosts };

The new ``usePosts`` hook then replaces the ``useContext`` hook (in ``Apps.js``):

.. code-block:: jsx
    :emphasize-lines: 1,8,14

    import { PostProvider, usePosts } from "./PostContext";

    function App() {
      {/* other stuff */}
    }

    function Header() {
      const { onClearPosts } = usePosts();

      {/* other stuff */}
    }

    function Results() {
      const { onClearPosts } = usePosts();

      {/* other stuff */}
    }

    {/* more components now using usePosts() */}

Finally, we want to prevent the usage of ``usePosts()`` in components, which don't
have access to the respective context provider (here ``PostsProvider``), such as
the ``<App>`` component in our example:

.. code-block:: jsx
    :emphasize-lines: 2-3,15,20

    function App() {
      const context = usePosts();
      console.log(context);     // prints 'undefined'

      {/* other stuff */}

      return (
        <section>
          <button
            onClick={() => setIsFakeDark((isFakeDark) => !isFakeDark)}
            className="btn-fake-dark-mode"
          >
            {isFakeDark ? "☀️" : "🌙"}
          </button>
          <PostProvider>
            <Header />
            <Main />
            <Archive />
            <Footer />
          </PostProvider>
        </section>
      );
    }

Calling the ``usePosts()`` method returns an ``undefined`` because the required
``PostProvider`` (or previously ``PostContext.Provider`` before using our custom provider)
is not available, only for its subcomponents as seen in the component tree:

.. code-block:: none

    App
    └── PostProvider
        └── Context.Provider
            ├── Header
            ├── Main
            └── ...

To prevent that, let's add a check to ``usePosts()`` and throw an error in case
of misuse (so the developers knows it right away):

.. code-block:: jsx
    :emphasize-lines: 3-4

    function usePosts() {
      const context = useContext(PostContext);
      if (context === undefined)
        throw new Error("PostContext was used outside of the PostProvider");
      return context;
    }
