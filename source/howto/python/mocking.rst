Mock Cheatsheet
===============
Basic methods
-------------
**Create a Mock object**

.. code-block:: python

    from unittest import mock
    m = mock.Mock()

**Set a default return value when calling mock object**

.. code-block:: python

    m.return_value = 42
    m() # returns 42

**Assign different return values for successive calls**

.. todo: finish this section

