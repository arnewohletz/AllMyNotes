Important numpy methods
=======================
To shorten things, the numpy module is referred to as ``np`` here. Think of
all code examples using this import statement:

.. code-block:: python

    import numpy as np

Arrays
------
.. rubric:: Reshape
.. code-block:: python

    rows = 10
    columns = 5
    new_array = np.reshape((rows, columns))

Creates ``new_array`` from ``some_array``, setting ``rows`` as new amount of rows and
``columns`` as new amount of columns. If -1 is used for either ``rows`` or ``columns``,
the amount is calculated, depending on the amount of a values of ``some_array`` and the
specified rows or columns.

.. rubric:: Insert element
.. code-block:: python

    np.insert(my_array, 0, 1, axis=1)

Inserts a single column of 1s in the position 0 of ``my_array``. If ``my_array``
has multiple rows, the value is put into the same position in each row. A ``axis=0`` means, the insert
is done as new row (here: at position 0, a ``axis=1`` means the insert is done as column (here: at position 0)
If ``axis`` is not defined (or None), the array is flattened first (-> 1D) and the insert value is inserted
at the defined position.

.. rubric:: Convert element type
.. code-block:: python

    new_array = (my_array == 10).astype(int)

Creates ``new_array`` out of ``my_array``, while checking each value in ``my_array`` if it
matches 5, replacing the value with 0 if false or 1 if true for ``new_array``.

.. rubric:: Multiply elements of two arrays
.. code-block:: python

    my_array = np.arrange(9.0).shape((3,3))  # 3x3 row-wise filled from 1.0 to 9.0
    squared = np.multiply(my_array, my_array)  # 3x3 matrix, row-wise with square values

Multiplies two compatible arrays, which means either

    a) both matrices must have the same shape
    b) one matrix must have a single row
    c) one matrix must have a single column

Each case returns an array with the shape biggest array. Case a) multiplies each
both values at the same location in each array. Case b) multiplies all values
of the bigger array's column with the respective value at the same column of the
smaller. Case c) is like b) but multiplying each value of the bigger arrays row
with the respective value in the smaller array.

.. rubric:: Find maximum value
.. code-block:: python

    max_index = np.argmax(some_array, axis=1)

Returns a the index of the highest number in ``some_array``. If
``my_array`` has multiple rows, the highest value of all rows is returned, if
``axis`` is undefined or ``axis=None``, ``some_array`` is flattened first (-> 1D).
If ``axis=0``, the indexes of the row containing the highest values are given,
if ``axis=1``, the indexes of the column containing the highest values are given.
In both cases, the index is returned as array if ``my_array`` has is 2-D. Adding
more dimensions, offers further axes (e.g. ``axis=2``), which returns the index
of the highest number within the


Files
-----
.. rubric:: Read file into 1D array
.. code-block:: python

    with gzip.open(filename, 'rb') as f:
        my_array = np.frombuffer(f.read(), dtype=np.unint8)

Read data values (here: unsigned 8-bit integers) from file and put them into an array.


Others
------
.. rubric:: Get exponential (e to the power of all input elements)
.. code-block:: python

    e_power_ten = np.exp(10)

Calculates the value of a given exponent using *e* as base (exponential function)
(here: e^10). Can also process arrays.