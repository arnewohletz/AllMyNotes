Routing and Single Page Applications
====================================
Routing
-------
* matching **different URLs** to **different UI views** (React components): **routes**
* enables user to **navigate between different application screens** using the browser URL
* keeps the UI **in sync** with the current browser URL

.. important::

    Apart from other web development frameworks, React does not contains a routing
    mechanism, but relies on third-party libraries for that.

React commonly uses `React Router`_ to add routing functionality. It is the most
used React third-party library.

.. hint::

    Calling a non-existing route (e.g. ``127.0.0.1:3000/product``) will load the
    root page instead, but not result in an error by default.

.. _React Router: https://reactrouter.com/

Single Page Applications
------------------------
* Application is **executed entirely on the client side** (browser)
* **Routes**: different URLs correspond to different views (components). The React
  component corresponding to the new URL is rendered

* In "multi-page" web applications, changing the URL loads a complete new page,
  whereas in single page applications, **JavaScript** (here: React) is used to update the
  page (DOM).

.. important::

    With SPAs, there will **never** be a complete page reload. The entire application
    exists within a single page. It feels like a **native app**.

* **Additional data can be loaded** from a web API when rendering the component, though
  we cannot load an entire different page (wouldn't be a single page application anymore)

.. hint::

    All React apps are single page applications.
