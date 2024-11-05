Intersphinx
===========
This extension generates links to external Sphinx documentation objects. For this,
it uses the external documentation's auto-generated ``objects.inv`` file, which
contain all navigable references of that Sphinx documentation.

Configuration
-------------
First, add the extension to your extensions variable:

.. code-block:: python
    :caption: conf.py

    extensions = [
        ...
        'sphinx.ext.intersphinx'
    ]

As the `official documentation <sphinx.ext.intersphinx_>`_ explains, each
external documentation to be used by intersphinx must be declared in the
``intersphinx_mapping`` config value. This can be done in the following ways:

.. code-block:: python
    :caption: conf.py

    intersphinx_mapping = {
        # use default objects.inv (here: https:/example.url/objects.inv)
        'basic_external_doc': ('https:/example.url', None),
        # use custom objects file (here: https:/example.url/custom-inv.txt)
        'custom_objects_file_doc': ('https:/example.url', 'custom-inv.txt')
        # multiple objects files (iterated from left to right, use first valid one)
        # here: local objects file --(if not found)--> default
        'basic_with_local_objects_file_doc': ('https:/example.url', ('../local/objects.inv', None))
    }

Each entry must contain a unique key (e.g. ``basic_external_doc``, in the usage schema below
referred to as ``invname``), under which the external documentation can be referenced in
`external <intersphinx_external_role_>`_ (see :ref:`intersphinx_usage`) and a value,
containing a tuple with the base URL of the hosted external documentation as the first
item and a reference to at least one ``objects.inv`` file as the second item. By default,
this objects file is automatically created during building the HTML and put into the build
output's root directory, e.g. ``build/html/objects.inv``. In this case, the reference
must be set to ``None`` (as for ``'basic_external_doc'`` above).

.. hint::

    The objects file stores all explicit and implicit reference targets of the project.
    See :ref:`intersphinx_inspect_objects_inv_file` to learn more about it.


.. _intersphinx_usage:

Usage
-----
If an external documentation is listed in ``intersphinx_mapping`` and the corresponding
``objects.inv`` file (or any specified custom files) is found, all the references inside
it can be used for referencing from your local documentation in the following ways:

* As a fallback solution: if a reference target cannot be found in the local documentation,
  Sphinx searches for a map in any declared external documentation objects file, or

    .. hint::

        The `intersphinx_disabled_reftypes`_ config value controls, which
        non-`external <intersphinx_external_role>`_ reference types are attempted to
        be resolved by intersphinx)

* explicitly by using the `external <intersphinx_external_role>`_ role

Schema:

.. code-block:: none

    # Fallback method

    ## Standard domain
    :reftype:`target`

    ## Non-standard domain
    :domain:reftype:`target`

    ## Look specific external documentation only
    :invname:domain:reftype:`target`

    # Explicit method (using the external role)

    ## Standard domain
    :external:reftype:`target`

    ## Non-standard domain
    :external:domain:reftype:`target`

    ## Look specific external documentation only
    :external+invname:domain:reftype:`target`

Examples:

.. code-block:: rst
    :caption: For a label (``:ref:``)

    :ref:`some_external_reference_target_label`
    :external:ref:`some_external_reference_target_label`
    :external+basic_external_doc:ref:`some_external_reference_target_label`

.. code-block:: rst
    :caption: For a document (``:doc:``)

    :doc:`some/external/document`
    :external:doc:`some/external/document`
    :external+basic_external_doc:doc:`some/external/document`

.. important::

    The ``std:doc`` domain (documents referenced via the `:doc: <std.doc_>`_ role) is,
    by default, deactivated in intersphinx (see `intersphinx_disabled_reftypes`_), which means,
    Sphinx does not search for external documents when using just ``:doc:``, but
    requires using the `external <intersphinx_external_role>`_ role.
    To disable this restriction, define the ``intersphinx_disabled_reftypes``
    in ``conf.py``, making sure, ``std:doc`` is not listed, for example:

    .. code-block:: python
        :caption: conf.py

        intersphinx_disabled_reftypes = []


.. hint::

    External reference links can also be renamed, just like internal references.
    For example:

    .. code-block:: rst

        :external:ref:`Create extension (custom role) <extend_sphinx_create_custom_role>`


.. _intersphinx_external_role: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#role-external
.. _intersphinx_disabled_reftypes: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#confval-intersphinx_disabled_reftypes

Understanding domains
---------------------
In Sphinx, in order to allow references to the same type of objects for different
programming languages, for example Python and C++, Sphinx provides multiple `domains`_,
which must be prepended to the reference type: For example

.. code-block:: rst

    :py:class:`Foo`

checks the current documentation and all external documentations listed under
``intersphinx_mapping`` (see above) for a matching Python class definition (``py:class``),
like:

.. code-block:: rst

    .. py:class:: Foo

       .. py:method:: quux()

General cross-reference types, such as ``:ref:`` or ``:doc:`` are part of the `standard domain`_,
abbreviated with ``std`` (see :ref:`intersphinx_inspect_objects_inv_file`).
Reference types from the standard domain may skip the declaration of the domain,
hence these two lines

.. code-block:: rst

    :external:std:ref:`some_external_reference_target_label``
    :external:ref:`some_external_reference_target_label`

behave exactly the same. References to all non-standard domains, for example the
`Python domain <sphinx_python_domain_>`_, must be explicitly mentioned:

    .. code-block:: rst
        :caption: This is OK

        :external:py:class:`Foo`

    .. code-block:: rst
        :caption: This may not work!

        :external:class:`Foo`

The only exception is, if the `primary domain`_ is set to that particular domain.
For example:

    .. code-block:: python
        :caption: conf.py

        primary_domain = 'cpp'

    then a C++ function could be abbreviated as

    .. code-block:: rst

        :external:method:`do_something`

    instead of ``:external:cpp:method:`do_something``` to reference to an external
    C++ function.

    .. hint::

        You may override the global default domain within a single RST file using the
        `default-domain`_ directive.


.. _domains: https://www.sphinx-doc.org/en/master/usage/domains/index.html
.. _sphinx_python_domain: https://www.sphinx-doc.org/en/master/usage/domains/python.html#the-python-domain
.. _primary domain: https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-primary_domain
.. _default-domain: https://www.sphinx-doc.org/en/master/usage/domains/index.html#directive-default-domain


.. _intersphinx_inspect_objects_inv_file:

Inspect the objects.inv file
----------------------------
As mentioned, each Sphinx projects creates a ``objects.inv`` file during HTML build,
which stores all explicit and implicit reference targets of the project.

It is stored in binary format, so to view all stored targets, use the
``sphinx.ext.intersphinx`` module to inspect its contents, for example:

.. code-block:: bash

    $ python -m sphinx.ext.intersphinx build/html/objects.inv

The output shows each reference in a single line in the following pattern:

.. code-block:: none

    <domain>:<reference_type>
        <label_name_A> <name_A> : <document_path_A>
        <label_name_B> <name_B> : <document_path_B>

for example

.. code-block:: none

    std:doc
        howto/docker/index               Docker                  : howto/docker/index.html
        howto/docker/tricks              Docker Cheatsheet       : howto/docker/tricks.html
        howto/docker/troubleshoot        Troubleshooting         : howto/docker/troubleshoot.html
    std:label
        /howto/docker/index.rst          Docker                  : howto/docker/index.html
        /howto/docker/index.rst#docker   Docker                  : howto/docker/index.html#docker
        /howto/docker/tricks.rst         Docker Cheatsheet       : howto/docker/tricks.html

The example, above shows a few references to *documents* (``std:doc``, cross-referenced
via `:doc: <std.doc>`_) and *labels* (``std:label``, cross-referenced via `:ref: <std.ref>`_).
Both are part of the `standard domain`_, which is abbreviated with ``std``.

.. hint::

    All `cross-reference targets`_ belong to the standard domain.


.. _sphinx.ext.intersphinx: https://www.sphinx-doc.org/en/master/usage/extensions/intersphinx.html#module-sphinx.ext.intersphinx
.. _cross-reference targets: https://www.sphinx-doc.org/en/master/usage/referencing.html#cross-references
.. _std.doc: https://www.sphinx-doc.org/en/master/usage/referencing.html#role-doc
.. _std.ref: https://www.sphinx-doc.org/en/master/usage/referencing.html#role-ref
.. _standard domain: https://www.sphinx-doc.org/en/master/usage/domains/standard.html
