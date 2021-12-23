Building
========
How to re-build all sources
---------------------------
By default, sphinx only builds the sources that have changed since the last build
in order to make builds faster.

Some changes, like in static files (e.g. css), that have an effect on a doc file
are not rebuild unless the content of that doc files itself changes.

In order to force sphinx to rebuild all sources, call sphinx-build directly using this
command in the documentations root folder:

.. prompt:: bash

    sphinx-build <my_source_directory> <my_output_directory> -a

for instance

.. prompt:: bash

    sphinx-build source _build -a

.. hint::

    A common source, why changes in style are not applied when refreshing the browser
    is that the browser's cache still references the previous version. In Firefox, to force the
    browser to refresh and discard the cache, hold down the :kbd:`Shift` key, when refreshing
    the page.