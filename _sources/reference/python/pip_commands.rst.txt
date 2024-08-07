pip
===

List available package versions (not possible for PyPI)
--------------------------------------------------------

.. code-block:: bash

    $ pip index versions <package_name>

.. note::

    Package index URL must be added to ``pip.ini`` or ``pip.conf`` first,
    for example:

    .. code-block:: ini

        [global]
        ...
        extra-index-url = <python.package.index.url>
        ...
        trusted-host = <python.package.index.domain>
        ...
