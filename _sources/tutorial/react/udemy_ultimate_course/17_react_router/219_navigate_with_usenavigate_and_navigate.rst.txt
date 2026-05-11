Navigate using useNavigate
==========================
``useNavigate`` allows to programmatically navigate to a URL. We want to navigate
to a form, when clicking anywhere inside the ``<Map>`` component:

.. code-block:: jsx
    :emphasize-lines: 1,5,13-15

    import { useNavigate, useSearchParams } from "react-router-dom";
    import styles from "./Map.module.css";

    function Map() {
      const navigate = useNavigate();
      const [searchParams, setSearchParams] = useSearchParams();
      const lat = searchParams.get("lat");
      const lng = searchParams.get("lng");

      return (
        <div
          className={styles.mapContainer}
          onClick={() => {
            navigate("form");
          }}
        >
        {/* more stuff */}
        </div>
          );
        }

We can also implement a *Go back* button inside our form with this. First we create
the component:

.. code-block:: jsx

    import styles from "./Button.module.css";

    function Button({ children, onClick, type }) {
      return (
        <button onClick={onClick} className={styles.btn}>
          {children}
        </button>
      );
    }
    export default Button;

The *Button* element accepts a ``onClick`` event function, and a ``type`` variabel.
Next, we define the buttons

.. code-block:: jsx

    <Button type="primary">Add</Button>
    <Button type="back">&larr; Back</Button>

and use the ``type`` to select the style class in the Button component:

.. code-block:: jsx
    :emphasize-lines: 5

    import styles from "./Button.module.css";

    function Button({ children, onClick, type }) {
      return (
        <button onClick={onClick} className={`${styles.btn} ${styles[type]}`}>
          {children}
        </button>
      );
    }
    export default Button;

The we again use the ``useNavigate`` hook to navigate back to the previous page:

.. code-block:: jsx
    :emphasize-lines: 1,6-9

    const navigate = useNavigate();

    <Button type="primary">Add</Button>
    <Button
      type="back"
      onClick={() => {
        navigate(-1);
      }}
    >

.. note::

    Using ``-2`` will navigate back to pages.

Note, as this ``<Button>`` element is inside a form, it triggers the form to be
submitted. To prevent that, we must disable the default behavior:

.. code-block:: jsx
    :emphasize-lines: 3,4

    <Button
      type="back"
      onClick={(e) => {
        e.preventDefault();
        navigate(-1);
      }}
    >

This will now work.

Redirect using the Navigate component
=====================================
The ``<Navigate>`` component isn't used much any more, but there is one important
use case for it, which is inside nested routes.

Problem: When we navigate to ``/app``, we have access to our Cities, but those
rely on the URL to be ``/app/cities``. Both routes show the ``<CitiesList>`` element.

To fix it, we change the

.. code-block:: jsx
    :emphasize-lines: 1,6

    import { BrowserRouter, Route, Routes, Navigate } from "react-router-dom";

    {/* other stuff */}

    <Route path="app" element={<AppLayout />}>
      <Route index element={<Navigate replace to="cities" />} />
      <Route path="cities/:id" element={<City />} />
      <Route
        path="cities"
        element={<CityList cities={cities} isLoading={isLoading} />}
      />
      <Route
        path="countries"
        element={<CountryList cities={cities} isLoading={isLoading} />}
      />
      <Route
        path="form"
        element={
          <p>
            <Form />
          </p>
        }
      />
    </Route>

This is basically a *re-route*, navigating to ``/app/cities`` whenever we navigate
to ``app``. The ``replace`` keyword replaces the current element in the history stack,
which enables to go back in the browser after this re-redirect.
