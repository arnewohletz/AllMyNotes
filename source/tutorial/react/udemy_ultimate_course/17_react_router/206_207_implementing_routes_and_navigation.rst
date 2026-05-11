Implementing main pages and routes
==================================
Install ``react-router-dom`` (does routing for browser applications):

.. code-block:: none

    $ npm install react-router-dom

    .. hint::

        You might want to install an earlier version using e.g. version 6:

        .. code-block:: none

            $ npm install react-router-dom@6

        Note that using version 6 raises some warning concerning changes in version 7.
        To remove those use

        .. code-block:: jsx

                <BrowserRouter
                  future={{
                    v7_relativeSplatPath: true,
                    v7_startTransition: true,
                  }}
                >

        in the code below.

Since ``react-router-dom`` version 6.4, there are two ways to defines routes.
The more traditional way, we use ``BrowserRouter, Route, Routes`` elements:

.. code-block:: jsx
    :emphasize-lines: 1,6-10

    import { BrowserRouter, Route, Routes } from "react-router-dom";
    import Product from "./pages/product";

    function App() {
      return (
        <BrowserRouter>
          <Routes>
            <Route path="product" element={<Product />} />
          </Routes>
        </BrowserRouter>
      );
    }

    export default App;

.. hint::

    Pages, so React components which are rendered according to the URL, are commonly
    put into a ``.comp/pages`` folder. Other regular components still are put into ``./components``.

The ``element`` property must receive a **React element**, not a component, so
we need to create it as an element, e.g. ``<Product />``. Doing so allows us to
pass props down these component instances.

Now, when navigating to ``/product`` it renders the ``Product`` component.

.. hint::

    When adding other elements outside of the ``<BrowserRouter>`` element, those will
    **always be displayed** when changing the URL, e.g.

    .. code-block::
        :emphasize-lines: 4

        function App() {
          return (
            <div>
              <h3>Hello Router</h3>
              <BrowserRouter>
                <Routes>
                  <Route index element={<Homepage />} />
                  <Route path="product" element={<Product />} />
                  <Route path="pricing" element={<Pricing />} />
                </Routes>
              </BrowserRouter>
            </div>
          );
        }

    will always show *Hello Router* at the top of each URL.

    Though instead of hardcoding those elements, we always let the component decide,
    which content to shows outside of the routing components.

We can also define a component, which catches all non-covered URLs e.g. ``PageNotFound``
using the ``*`` (star) path:

.. code-block:: jsx
    :emphasize-lines: 8

    function App() {
      return (
        <BrowserRouter>
          <Routes>
            <Route index element={<Homepage />} />
            <Route path="product" element={<Product />} />
            <Route path="pricing" element={<Pricing />} />
            <Route path="*" element={<PageNotFound />} />
          </Routes>
        </BrowserRouter>
      );
    }

Link between routes with <Link /> and <NavLink />
=================================================
Providing a clickable link to a route.

Traditionally, this is done via a Anchor element:

.. code-block:: jsx
    :emphasize-lines: 4

    function Homepage() {
      return (
        <div>
          <h1>WorldWise</h1>
          <a href="/pricing">Pricing</a>
        </div>
      );
    }

but this is **not how to do it**, as it **reloads the entire page**, all requests
are repeated.

Instead we will use the ``<Link>`` element:

.. code-block:: jsx
    :emphasize-lines: 1,7

    import { Link } from "react-router-dom";

    function Homepage() {
      return (
        <div>
          <h1>WorldWise</h1>
          <Link to="/pricing">Pricing</Link>
        </div>
      );
    }

When clicking the link, the page does not reload, **no new request are made** as
the *Pricing* component, which is now displayed already has been loaded before.
The only thing that changed is the React Element tree from

.. code-block:: none
    :emphasize-lines: 6,7

    App
    └── ...
        └── Routes
            └── RenderedRoute
                └── Route.Provider
                    └── Homepage
                        └── Link

to

.. code-block:: none
    :emphasize-lines: 6

    App
    └── ...
        └── Routes
            └── RenderedRoute
                └── Route.Provider
                    └── Pricing

Putting a navigation component into each page:

* regular components are located in ``/components`` directory

.. code-block:: jsx

    function PageNav() {
      return (
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/pricing">Pricing</Link>
            </li>
            <li>
              <Link to="/product">Product</Link>
            </li>
          </ul>
        </nav>
      );
    }

* the *PageNav* component is then added to the page components e.g.:

.. code-block:: jsx
    :emphasize-lines: 1,6

    import PageNav from "../components/PageNav";

    function Homepage() {
      return (
        <div>
          <PageNav />
          <h1>WorldWise</h1>
        </div>
      );
    }

React-Router brings the ``<NavLink>`` element, which is better suited for navigation
bars than ``<Link>`` as it **marks the current page element**:

.. code-block:: jsx

    function PageNav() {
      return (
        <nav>
          <ul>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/pricing">Pricing</Link>
            </li>
            <li>
              <Link to="/product">Product</Link>
            </li>
          </ul>
        </nav>
      );
    }

This marks the currently selected page by adding the ``class="active"`` attribute
to the resulting HTML link element, allowing for better styling.