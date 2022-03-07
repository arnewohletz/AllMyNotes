Mock - Cheatsheet
=================
.. thebe-button:: Enable live code execution

Basic methods
-------------
.. rubric:: Create a Mock object

.. jupyter-execute::

    from unittest import mock
    m = mock.Mock()

.. rubric:: Set a default return value when calling mock object

.. jupyter-execute::

    m.return_value = 42
    m()

.. rubric:: Assign different return values for successive calls

.. jupyter-execute::

    m.side_effect = ['foo', 'bar', 'baz']
    print(m())
    print(m())
    print(m())

.. rubric:: Check whether mock object has been called at least once

.. jupyter-execute::
    :raises:

    m = mock.Mock()
    m()
    m.assert_called()

Returns *None*, if called, otherwise raises *AssertionError*

.. rubric:: Check whether mock object has been called exactly once
.. jupyter-execute::

    m = mock.Mock()
    try:
        m.assert_called_once()
    except AssertionError:
        print("No, I wasn't called (yet)")
    m()
    if not m.assert_called_once():
        print("Yeah, now I was called")

.. rubric:: Get number of call to mock object
.. jupyter-execute::

    m = mock.Mock()
    m()
    m()
    m.call_count

.. rubric:: Get call arguments of last mock call
.. jupyter-execute::

    m = mock.Mock()
    m(1, foo='bar')
    m.call_args

If mock object hasn't been called yet, *None* is returned.

.. rubric:: Get call arguments of all mock calls
.. jupyter-execute::

    m = mock.Mock()
    m()
    m(1, foo='bar')
    m(4, baz='bar2')
    m.call_args_list

.. rubric:: Reset call previous call (won't change mock configuration)
.. jupyter-execute::

    m = mock.Mock()
    m()
    m(1, foo='bar')
    m(4, baz='bar2')
    m.reset_mock()
    m.call_args_list

Patching an import module from a project module in our unit test
----------------------------------------------------------------
.. rubric:: Project module (work.py)
.. code-block:: python

    import os

    def work_on():
        path = os.getcwd()
        print(f'Working on {path}')
        return path

The project module imports *os* and uses its *getcwd()* method , which
we want to mock in our test.

.. rubric:: Defining the unit test
.. code-block:: python

    from unittest import TestCase, mock

    from work import work_on

    class TestWorkMockingModule(TestCase):

        def test_using_context_manager(self):
            with mock.patch('work.os') as mocked_os:
                work_on()
                mocked_os.getcwd.assert_called_once()


* The test module imports the project module's method *work_on()*
* At the beginning of the test, the work.os module (which is the os module in
  our work.py module) is patched with `MagicMock`_ object (here called *mocked_os*)
* When the *work_on()* method is called afterwards, the *MagicMock* object is
  returned instead of the original module (os)
* The returned *MagicMock* object assigned the attribute name to the function
  that is called on the patched module (here: *os.getcwd()*)

.. _MagicMock: https://docs.python.org/3/library/unittest.mock.html?highlight=magicmock#unittest.mock.MagicMock

.. rubric:: Executing the test
.. code-block:: python

    import unittest
    unittest.main(argv=[''], verbosity=2, exit=False)

Alternatively, the :ulined:`patch decorator` can be used:

.. code-block:: python

    @mock.patch('work.os')
    def test_using_decorator(self, mocked_os):
        work_on()
        mocked_os.getcwd.assert_called_once()

To define a **return value** for the mocked *os.getcwd()* function, define it
like this:

.. code-block:: python

    def test_using_return_value(self):
    """Note 'as' in the context manager is optional"""
    with mock.patch('work.os.getcwd', return_value='testing'):
        assert work_on() == 'testing'

Applying a :python:`return_value='testing'` will return the string when
calling the :python:`work.os.getcwd()` function.

Running the test leads to this output

.. code-block:: python

    >>> import unittest
    >>> unittest.main()
    Working on testing

Patching classes
----------------
To test project classes that interact with other project classes in isolation,
the other project classes must be mocked (in order to determine test failure
to a specific class and method, not it's depending classes).

Example:

.. rubric:: Project module (worker.py)
.. code-block:: python

