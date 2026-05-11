Creating and providing a context
================================
To create the *Provider*, we first create a new Context (in our case, we want it to
store the posts, hence the constant name) outside of any component:

.. code-block:: jsx

    import { createContext, useEffect, useState } from "react";

    // 1) Create new context
    const PostContext = createContext();

The *PostContent* starts with a capital letter, as it is a component.

Inside the parent component, we then wrap the JSX into the context's ``Provider``:

.. code-block:: jsx
    :emphasize-lines: 6-14,24-27,29-30,33

    function App() {
      {/* other stuff */}

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
        >
          <section>
            <button
              onClick={() => setIsFakeDark((isFakeDark) => !isFakeDark)}
              className="btn-fake-dark-mode"
            >
              {isFakeDark ? "☀️" : "🌙"}
            </button>

            <Header
              posts={searchedPosts}
              onClearPosts={handleClearPosts}
              searchQuery={searchQuery}
              setSearchQuery={setSearchQuery}
            />
            <Main posts={searchedPosts} onAddPost={handleAddPost} />
            <Archive onAddPost={handleAddPost} />
            <Footer />
          </section>
        </PostContext.Provider>
      );
    }

Note, that we need to pass the ``value`` property into the ``<PostContext.Provider>``,
which contains an object of all props, that we originally pass down to the deeper
components here.

.. hint::

    Practically, it is cleaner to provide different contexts for different purposes.
    Here, we may only use the ``PostContext`` for post props and create a second
    ``SearchContext`` for the search related props. Though we put them into one here.

Consuming the context
=====================
First, lets remove all passed down props from the component's JSX and inside the
receiving component's arguments.

.. code-block:: jsx
    :emphasize-lines: 23-25

    function App() {
      {/* other stuff */}

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
        >
          <section>
            <button
              onClick={() => setIsFakeDark((isFakeDark) => !isFakeDark)}
              className="btn-fake-dark-mode"
            >
              {isFakeDark ? "☀️" : "🌙"}
            </button>

            <Header />
            <Main />
            <Archive />
            <Footer />
          </section>
        </PostContext.Provider>
      );
    }

If a component requires a certain prop, the removed prop must be replaced by calling
the ``useContext`` hook (here: ``Header``):

.. code-block:: jsx
    :emphasize-lines: 1,5,14

    import { createContext, useContext, useEffect, useState } from "react";

    function Header() {
      // 3) Consuming the context value
      const { onClearPosts } = useContext(PostContext);
      return (
        <header>
          <h1>
            <span>OOO</span>The Atomic Blog
          </h1>
          <div>
            <Results />
            <SearchPosts />
            <button onClick={onClearPosts}>Clear posts</button>
          </div>
        </header>
      );
    }

The ``useContext(PostContext)`` hook returns the entire content of the ``value``
object from the *Provider*, so we can destructure any prop that we need at this point
(here: onClearPosts).
