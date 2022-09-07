PyScript :footcite:p:`merket22_pyscript`
========================================
`PyScript`_ is a framework, which enables using Python instead of JavaScript to program
web pages. It acts as a wrapper for `Pyodide`_, a CPython port which translates Python
code into WebAssembly, which can be processed by a web browser.

Basic setup
-----------
PyScript does not require an installation as the resources are provided by a
Content Delivery Network (CDN) by the PyScript developers. To include PyScript to
a project, add these statements into you :html:`<head>` section:

.. code-block:: html

    <html>
        <head>
            ...
            <link rel="stylesheet" href="https://pyscript.net/alpha/pyscript.css"/>
            <script defer src="https://pyscript.net/alpha/pyscript.js"></script>
        </head>
        <body>
        ...
        </body>
    </html>

Python code is inserted between :html:`<py-script>` tags within the HTML's body:

.. code-block:: html

    <html>
        <head>
        ...
        </head>
        <body>
            <py-script>
                print("Hello World")
            <py-script>
        </body>
    </html>

Apart from the Python Standard Library, Pyodide includes a lot of additional packages,
which must be imported for usage, using the :html:`<py-env>` tags:

.. code-block:: html

    <html>
        <head>
        ...
        </head>
        <body>
            <py-env>
                - numpy
                - matplotlib
            </py-env>
            <py-script>
                import numpy
                import matplotlib
                ...
            <py-script>
        </body>
    </html>

Please note, that the imported modules must also be imported into your Python code
using the :python:`import` statement. A list of all supported packages can be found
`here <https://pyodide.org/en/stable/usage/packages-in-pyodide.html#packages-in-pyodide>`_.

.. _PyScript: https://pyscript.net/
.. _Pyodide: https://pyodide.org/en/stable/index.html

Accessing the DOM
-----------------
While PyScript is supposed to be a replacement for JavaScript it is still required
to utilize JavaScript to access the DOM, hence accessing HTML objects. For this,
Pyodide provides a JavaScript API for Python, which offers access to the entire
`JavaScript global namespace`_ such as the `Document`_ or the `console`_ interface:

.. code-block:: html

    <html>
    ...
    <py-script>
        from js import document, console
        table = document.getElementById("some_table").childNodes
    </py-script>
    <div>
        <table id="some_table"></table>
    </div>
    </html>

As shown, the element's JavaScript methods can be applied here.

If a Python function wants to interact with the DOM, a function reference is required.
The reason is that JavaScript doesn't recognize Python functions, only JavaScript functions,
for example Python functions cannot be passed to :javascript:`addEventListener()`.
For this, pyodide offers the function :python:`create_proxy()` to wrap a Python
function into a JavaScript function:

.. code-block:: python

    from pyodide import create_proxy

    def button_clicked(e):
        print(e.target.textContent)

    js_button_clicked = create_proxy(key_clicked)

The proxy function can the be used by other DOM objects:

.. code-block:: python

    from js import document, console

    ...

    button = document.getElementById("some_button")
    button.addEventListener("click", js_button_clicked)

As shown above, typical JavaScript data structures such as Event objects can be
used in the Python function, just like in JavaScript itself.

.. _JavaScript global namespace: https://developer.mozilla.org/en-US/docs/Web/API#interfaces
.. _Document: https://developer.mozilla.org/en-US/docs/Web/API/Document
.. _console: https://developer.mozilla.org/en-US/docs/Web/API/console

Asynchron Loading
-----------------
Loading external resources, such as a text file, can be downloaded via Ajax, instead of putting
the data straight into the code. In Python, this might be done using the `requests`_
library, which is not available in Pyodide, but it offers the :python:`pyfetch()` method
for this.

Since Ajax calls are asynchronous by nature, :python:`pyfetch()` can only be called from
within asynchronous functions (:python:`async def`). As those don't block the code, calling
:python:`await` to wait for the response is fine:

.. code-block:: python

    from pyodide.http import pyfetch
    from pyodide import JsException
    from js import console

    async def load_resource():
        try:
            response = wait pytech(url="/some/url/containing/resources.txt",
                                   method="GET",
                                   headers={"Content-Type": "text/plain"})
            if response.ok:
                data = await response.string()
                console.log(data.split())
                return data.split()
        except JSException:
            return None

The :python:`JsException` is the base class of any JavaScript error, which is encapsulated
by PyScript. Using a more specific exception type is possible.

The resources can now be further processed, like here using :python:`pick_data()`:

.. code-block:: python

    async def pick_data():
        data = await load_resource()
        data_value = random.choice(data)
        console.log(f"Value: {dat_value}")

Same as the :python:`load_resource()` function, the :python:`pick_data()` function is
defined as an asynchronous function, as it needs to wait for :python:`load_resource()`.

In call those methods in a way, that they don't block the code, an old JavaScript trick
can be applied:

    .. code-block:: python

        from js import setTimeout
        from pyodide import create_proxy
        ...
        setTimeout(create_proxy(load_resource), 0)

Setting the timeout to 0 prevents the code from having to wait for :python:`load_resource()`
to finish. The method is executed in parallel.

.. _requests: https://requests.readthedocs.io/en/latest/

Other stuff
-----------
PyScript provides a :python:`write()` method, which sends strings into labeled elements
on the page. No import statement is necessary:

.. code-block:: python

    element = document.getElementById("my_id")
    pyscript.write("element", "Hello World")

Further Resources
-----------------
* `Tutorial from RealPython <https://realpython.com/pyscript-python-in-browser/>`_
* `Tutorial from ct (German) <../../../_static/ct.22.17.154-159.pdf>`__

.. footbibliography::