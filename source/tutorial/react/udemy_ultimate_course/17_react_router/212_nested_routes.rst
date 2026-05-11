Nested Routes
=============
We need them if we want to **control a part of the user interface by a part of the URL**,
for instance in ``http:localhost:3000/app/cities``, the ``cities`` part defines a
specific component to be displayed.

Nested routes are defined inside ``<Route>`` elements. For the above example:

.. code-block:: jsx
    :emphasize-lines: 10

    function App() {
      return (
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Homepage />} />
            <Route path="product" element={<Product />} />
            <Route path="pricing" element={<Pricing />} />
            <Route path="login" element={<Login />} />
            <Route path="*" element={<PageNotFound />} />
            <Route path="app" element={<AppLayout />} />
          </Routes>
        </BrowserRouter>
      );
    }

changes to

.. code-block:: jsx
    :emphasize-lines: 10-12

    function App() {
      return (
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<Homepage />} />
            <Route path="product" element={<Product />} />
            <Route path="pricing" element={<Pricing />} />
            <Route path="login" element={<Login />} />
            <Route path="*" element={<PageNotFound />} />
            <Route path="app" element={<AppLayout />}>
              <Route path="cities" element={<p>List of cities</p>} />
            </Route>
          </Routes>
        </BrowserRouter>
      );
    }

Note, that the ``element`` property of the nested route can be any JSX (here for now:
``<p>List of cities</p>``) or a component.

Additional nested routes are possible:

.. code-block:: jsx

    <Route path="app" element={<AppLayout />}>
      <Route path="cities" element={<p>List of cities</p>} />
      <Route path="countries" element={<p>Countries</p>} />
      <Route path="form" element={<p>Form</p>} />
    </Route>

A nested route builds up upon its enclosing Route (here: ``"app"``), so it does only
need the **additional path** (e.g. ``cities"``, **not** the entire path (e.g. ``"app/cities"``).

But where to display the actual component element of nested routes? These are defined
inside the enclosing component using the ``<Outlet>`` element.

For instance, the ``<Cities>`` element is supposed to be rendered inside the ``<Sidebar>``
element (if the URL shows ``app/cities``). This is done via the ``<Outlet>`` element:

.. code-block:: jsx
    :emphasize-lines: 6

    function Sidebar() {
      return (
        <div className={styles.sidebar}>
          <Logo />
          <AppNav />
          <Outlet />
          <Footer />
        </div>
      );
    }
    export default Sidebar;

When navigating to

* ``app/cities`` now, the defined element (here: ``<p>List of cities</p>``)
* ``app/form`` now, the defined element (here: ``<p>Form</p>``)

is displayed.

The ``<Outlet />`` element defines **where** the element, that is associated
with the routing of the URL is supposed to be inserted.

Index Route
===========
Additionally, there is the *Index Route*. It defines the route to take, if the
URL matches none of the other defines ``<Route>`` elements. It is defined like this:

.. code-block:: jsx
    :emphasize-lines: 2

    <Route path="app" element={<AppLayout />}>
      <Route index element={<p>List of cities</p>} />
      <Route path="cities" element={<p>List of cities</p>} />
      <Route path="countries" element={<p>Countries</p>} />
      <Route path="form" element={<p>Form</p>} />
    </Route>

When navigating just to ``/app`` now, it displays the defined element at the
position of the ``<Outlet />`` element. If this were not defined, **nothing** would
be rendered at the ``<Outlet />`` element's position.

In fact, we can transform any ``path="/"`` to ``index``:

.. code-block:: jsx
    :emphasize-lines: 2

      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="product" element={<Product />} />
        <Route path="pricing" element={<Pricing />} />
        <Route path="login" element={<Login />} />
        <Route path="*" element={<PageNotFound />} />
        <Route path="app" element={<AppLayout />}>
          <Route index element={<p>List of cities</p>} />
          <Route path="cities" element={<p>List of cities</p>} />
          <Route path="countries" element={<p>Countries</p>} />
          <Route path="form" element={<p>Form</p>} />
        </Route>
      </Routes>

becomes

.. code-block:: jsx
    :emphasize-lines: 2

      <Routes>
        <Route index element={<Homepage />} />
        <Route path="product" element={<Product />} />
        <Route path="pricing" element={<Pricing />} />
        <Route path="login" element={<Login />} />
        <Route path="*" element={<PageNotFound />} />
        <Route path="app" element={<AppLayout />}>
          <Route index element={<p>List of cities</p>} />
          <Route path="cities" element={<p>List of cities</p>} />
          <Route path="countries" element={<p>Countries</p>} />
          <Route path="form" element={<p>Form</p>} />
        </Route>
      </Routes>

To conclude, we can now define Links to those routes inside the ``AppNav`` component.
Here, we only define the **relative path**, for which the component must only be placed
inside components, which are associated with a compatible URL. For example, when defining

.. code-block:: jsx
    :emphasize-lines: 6,9

    export default function AppNav() {
      return (
        <nav className={styles.nav}>
          <ul>
            <li>
              <NavLink to="cities">Cities</NavLink>
            </li>
            <li>
              <NavLink to="countries">Countries</NavLink>
            </li>
          </ul>
        </nav>
      );
    }

adding the component inside ``Sidebar`` navigates to defined routes, where defining
it someplace else like inside ``Homepage`` navigates to undefined routes.

.. code-block:: none
    :emphasize-lines: 2,6

    Homepage                /
    └── AppNav              --> WON'T WORK! Routes to /cities  and  /countries
    └── App                 /app
        └── Sidebar
            └── Outlet      reacts to  /app/cities  or  /app/countries
            └── AppNav      --> THIS WORKS! Routes to /app/cities and /app/countries

This is similar to creating a *Tab* component, but there we had to store the current
state using ``useState`` to manage the currently opened and displayed tab content.
Here, we are storing that information inside the URL.