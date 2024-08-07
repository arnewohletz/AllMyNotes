Use built-in HTTP server
------------------------
Python comes with a `http server module`_, allowing to host web applications or
a sphinx documentation for development purposes.

To keep it running, move it to a separate `screen`_ session named *http_server*:

.. code-block:: bash

    $ screen -S http_server

Inside the new screen start the HTTP server via

.. code-block:: bash

    $ python -m http.server --bind 127.0.0.1 --directory ~/my_sphinx_doc/build 31500

* The ``--bind`` option sets the URL to localhost
* The ``--directory`` option must point to the web application (usually
  where the ``index.html`` file resides)
* The **31500** defines the port and should be a number between 1024 (numbers
  from 0 to 1023 are reserved for system services) and 65535
  (as long as no other service already uses that port)

To switch back to the original window, type :kbd:`Ctrl + A` followed by a
simple :kbd:`d` (for detach). See :ref:`screen reference <gnu_screen_reference>`
for more info.

.. _http server module: https://docs.python.org/3/library/http.server.html
.. _screen: https://www.gnu.org/software/screen/
