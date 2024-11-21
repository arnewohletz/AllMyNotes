unittest.mock.patch
===================

Anything can be patched, meaning that it is replaced with a Mock object:

* modules
* classes
* functions and methods
* built-in functions and environmental variables
* class attributes

Patch an import module
----------------------
``unittest.mock`` is able to patch imports in the module under test using the
`patch`_ function. This is useful to mock the behaviour of module functions
(like ``os.getcwd()``).

``patch`` will intercept ``import`` statements identified by a string and return
a Mock instance, which you can preconfigure using the techniques from ``unittest.Mock``
(see `unittest.mock.Mock <mock.ipynb>`_).

Module under test (``work.py``):

.. code-block:: python
    :caption: work.py

    import os

    def work_on():
        path = os.getcwd()
        print(f'Working on {path}')
        return path

The project module imports ``os`` and uses its :python:`getcwd()` method , which
we want to mock in our test.

Patch using a context manager (``with`` statement)
``````````````````````````````````````````````````
When using the context manager ``patch``, the patch ends when the ``with``
statement ends.

.. code-block:: python
    :caption: test_work.py

    from unittest import TestCase, mock
    from work import work_on

    class TestWorkMockingModule(TestCase):

        def test_using_context_manager(self):
            with mock.patch('work.os') as mocked_os:
                work_on()
                mocked_os.getcwd.assert_called_once()

We specifically patch the ``work.os`` module, not ``os``, as this
would patch ``os`` for all modules, not just for ``work.py``.

* The test module imports the project module's method ``work_on()``
* At the beginning of the test, the ``work.os`` module (which is the ``os``
  module in our ``work.py`` module) is patched with a `MagickMock`_ object
  (here called ``mocked_os``)
* When the ``work_on()`` method is called afterward, that ``MagicMock`` object is
  called instead of the original module (``os``) - as no return value is defined
  ``work_on()`` returns another MagicMock object - as we are not testing the
  correctness of the return value here, only checking if the ``mocked_os`` executed
  the ``getcwd()`` method, we do not care about the return value

The ``as`` statement in the decorator is optional. You may as well not mock the
entire ``work.os`` module, but rather define a return value for the single
function, that is called (``getcwd()``):

.. code-block:: python
    :caption: test_work.py

    from unittest import TestCase, mock
    from work import work_on

    class TestWorkMockingModule(TestCase):
        def test_using_return_value(self):
            with mock.patch('work.os.getcwd', return_value='testing'):
                assert work_on() == 'testing'

Patch using the decorator (``@patch``)
``````````````````````````````````````
Using the ``@patch`` decorator allows to inject a mock into the test function.
The patch is available for the entire function.

.. code-block:: python

    from unittest import TestCase, mock

    from work import work_on

    class TestWorkMockingModule(TestCase):

        @mock.patch('work.os')
        def test_using_decorator(self, mocked_os):
            work_on()
            mocked_os.getcwd.assert_called_once()

Here the ``work.os`` module is replaced with a MagicMock object.

Patch classes
-------------
To test project classes that interact with other project classes in isolation,
the other project classes must be mocked (in order to determine test failure
to a specific class and method, not by any of its dependency classes).

In this ``worker.py`` module, the `Worker` class needs to be tested for these
two things:

- the ``Worker`` calls ``Helper`` with ``db``
- the ``Worker`` returns the expected path supplied by ``Helper``

.. code-block:: python
    :caption: worker.py

    import os


    class Helper:

        def __init__(self, path):
            self.path = path

        def get_path(self):
            base_path = os.getcwd()
            return os.path.join(base_path, self.path)


    class Worker:

        def __init__(self):
            self.helper = Helper('db')

        def work(self):
            path = self.helper.get_path()
            print(f'Working on {path}')
            return path

Patch the entire class
``````````````````````
To test this, the ``Worker`` needs to be isolated from ``Helper``,
so that failures can be associated with the ``Worker`` class only.

Consequently, the entire ``Helper`` class must be patched:

.. code-block:: python
    :caption: test_worker.py

    from unittest import TestCase, mock
    from worker import Worker


    class TestWorkerModule(TestCase):

        def test_patching_class(self):
            with mock.patch('worker.Helper') as MockHelper:
                MockHelper.return_value.get_path.return_value = 'testing'
                worker = Worker()
                MockHelper.assert_called_once_with('db')
                self.assertEqual(worker.work(), 'testing')

Note the double ``return_value`` in the example, simply using
``MockHelper.get_path.return_value`` would not work since in the code
we call get_path on an instance, not the class itself.

Alternatively, we can preconfigure the ``MockHelper`` instance and
assign it as the return value of the ``worker.Helper`` call. The following
shows the respective test in two ways: one uses the context manager (``with``)
and the other the ``@mock.patch`` decorator:

.. code-block:: python
    :caption: test_worker.py

    from unittest import TestCase, mock
    from worker import Worker


    class TestWorkerModule(TestCase):

        mockHelperInstance = mock.MagicMock()
        mockHelperInstance.get_path.return_value = 'testing'

        # using patch context manager
        def test_patch_class_context_manager(self):
            with mock.patch('worker.Helper',
                            return_value=self.mockHelperInstance) as MockHelper:
                worker = Worker()
                MockHelper.assert_called_once_with('db')
                self.assertEqual(worker.work(), 'testing')

        # using patch class decorator
        @mock.patch('worker.Helper', return_value=mockHelperInstance)
        def test_patch_class_decorator(self, mock_helper):
            worker = Worker()
            mock_helper.assert_called_once_with('db')
            self.assertEqual(worker.work(), 'testing')

.. important::

    It is important to distinguish between **mocking a class** and
    **mocking the instance of a class**. Sometimes, it is necessary to mock the
    entire class, sometimes it might be sufficient to mock only an instance from
    that class.

    Mocking the entire class allows for

        * checking, in what way that class has been initialized
        * instantiating multiple instances from it, which return a Mock object and
          raises the call count

    For the above ``worker.py`` module, both these tests pass:

    .. code-block:: python
        :caption: test_worker.py

        from unittest import TestCase, mock
        from worker import Worker

        mockHelper = mock.MagicMock()


        class TestWorkerModule(TestCase):

            def setUp(self):
                mockHelper.reset_mock()
                self.mock_helper_instance = mockHelper.return_value

            @mock.patch('worker.Helper', new=mockHelper)
            def test_initialization(self):
                Worker()
                mockHelper.assert_called_once_with('db')

            @mock.patch('worker.Helper', new=mockHelper)
            def test_get_path(self):
                self.mock_helper_instance.get_path.return_value = 'testing'
                worker = Worker()
                self.assertEqual(worker.work(), 'testing')

Speccing
````````
The danger with mocks is that a ``Mock`` object returns a new ``MagicMock`` object to
basically every attribute or method it is queried for, no matter if that attribute or
method actually exists. If the mocked class changes signatures or an attribute, the
``Mock`` object will still return the requested "thing" as another Mock, simply said:

.. code-block:: none

    The Mock does not know about the object it is mocking.

To prevent this, *speccing* can be added to a Mock, which makes it behave as the object
being mocked. The easiest to use is ``autospec=True`` option.

**Example**

Assuming the ``Helper`` class changed its ``get_path()`` method to ``get_folder()``,
but the call is **not** changed in the ``Worker`` class:

.. code-block:: python
    :caption: worker.py

    import os


    class Helper:

        def __init__(self, path):
            self.path = path

        def get_folder(self):
            base_path = os.getcwd()
            return os.path.join(base_path, self.path)


    class Worker:

        def __init__(self):
            self.helper = Helper('db')

        def work(self):
            path = self.helper.get_path()
            print(f'Working on {path}')
            return path

When running the previous test without the ``speccing`` option, this would pass,
as we mock the ``get_path`` method for the Mock instance although the original
class does not contain this method anymore.

But with the ``autospec=True`` method, the Mock ``get_path()`` method, the Mock
object checks for consistence with the original object. So

.. code-block:: python

    @mock.patch('worker.Helper', new=mockHelper, autospec=True)
    def test_get_path(self):
        self.mock_helper_instance.get_path.return_value = 'testing'
        worker = Worker()
        self.assertEqual(worker.work(), 'testing')

will raise an ``AttributeError``:

.. code-block:: none

    AttributeError: Mock object has no attribute 'get_path'

Patch class methods
-------------------
A class can also be partially mocked by using :python:`mock.patch.object` on
one of its methods:

.. code-block:: python
    :caption: test_worker.py

    from unittest import TestCase, mock
    from worker import Worker, Helper


    class TestWorkerModule(TestCase):

        def test_partial_patching_decorator(self):
            with mock.patch.object(Helper, 'get_path', return_value='testing'):
                worker = Worker()
                self.assertEqual(worker.helper.path, 'db')
                self.assertEqual(worker.work(), 'testing')

        @mock.patch.object(Helper, 'get_path', return_value='testing')
        def test_partial_patching_decorator(self, mocked_helper_get_path):
            worker = Worker()
            self.assertEqual(worker.helper.path, 'db')
            self.assertEqual(worker.work(), 'testing')
            mocked_helper_get_path.assert_called_once()


Patching built-in functions and environment variables
-----------------------------------------------------
Previously, the ``print()`` call in ``Worker.work()`` was neglected, though
it might be important to test, if that call was made.

Assuming this version of the ``work()`` method inside ``worker.py``:

.. code-block:: python

    import os

    def work_on_env():
        path = os.path.join(os.getcwd(), os.environ['MY_VAR'])
        print(f'Working on {path}')
        return path

The path is concatenated by a ``MY_VAR`` environment variable and the
``os.getcwd()`` return value. The test:

.. code-block:: python

    from unittest import TestCase, mock

    from worker import work_on_env

    class TestBuiltin(TestCase):

        def test_patch_dict_context_manager(self):
            with mock.patch('worker.print') as mock_print:
                with mock.patch('os.getcwd', return_value='/home/'):
                    with mock.patch.dict('os.environ', {'MY_VAR': 'testing'}):
                        self.assertEqual(work_on_env(), '/home/testing')
                        mock_print.assert_called_once_with('Working on /home/testing')

* we patch the built-in ``print()`` function for the ``worker`` module as ``mock_print`` (patch on import)
* we patch the ``worker.work_on_env()`` method assigning "/home/" as the return value
* we patch the ``os.environ`` dictionary with a ``{'MY_VAR': 'testing'}`` dictionary

Nesting multiple context managers can be prevented by using multiple patch decorators:

.. code-block:: python

    from unittest import TestCase, mock

    from worker import work_on_env

    class TestBuiltin(TestCase):
        @mock.patch('os.getcwd', return_value='/home/')
        @mock.patch('worker.print')
        @mock.patch.dict('os.environ', {'MY_VAR': 'testing'})
        def test_patch_builtin_dict_decorators(self, mock_print, mock_getcwd):
            self.assertEqual(work_on_env(), '/home/testing')
            mock_print.assert_called_once_with('Working on /home/testing')

Note that the ``mock_getcwd`` must be passed into the test function, though it isn't used.
Also note, that the order of mock objects passed into the test function are in
reversed order: the first patch context decorator is passed in last and vice versa.


--- skipped 'Mocking context managers' here, might document later ---

Patching class attributes
-------------------------
Mocking class attributes of classes under test provide the advantage of your
test failing due to a renaming of that attribute will pinpoint directly to that
mismatch.

Assuming, you want to test the following class

.. code-block:: python

    class Pricer:

        DISCOUNT = 0.80

        def get_discounted_price(self, price):
            return price * self.DISCOUNT

You could test it the following ways:

.. code-block:: python

    from unittest import TestCase, mock, expectedFailure

    from pricer import Pricer


    class TestClassAttribute(TestCase):

        def test_patch_instance_attribute(self):
            pricer = Pricer()
            pricer.DISCOUNT = 0.5
            self.assertAlmostEqual(pricer.get_discounted_price(100), 50.0)

        def test_set_class_attribute(self):
            Pricer.DISCOUNT = 0.75
            pricer = Pricer()
            self.assertAlmostEqual(pricer.get_discounted_price(100), 75.0)

        @expectedFailure
        def test_patch_incorrect_class_attribute(self):
            with mock.patch.object(Pricer, 'PERCENTAGE', 1):
                pricer = Pricer()
                self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

        def test_patch_class_attribute(self):
            with mock.patch.object(Pricer, 'DISCOUNT', 1):
                pricer = Pricer()
                self.assertAlmostEqual(pricer.get_discounted_price(100), 100)

            self.assertAlmostEqual(pricer.get_discounted_price(100), 80)

* |:-1:| **test_patch_instance_attribute**: Here, we assign the ``DISCOUNT`` attribute
  after initializing the ``Pricer()`` class. This is fairly safe, but renaming the
  attribute will fail the test **without hinting towards the mismatch**

* |:-1:| |:-1:| **test_set_class_attribute**: Here, we assign the ``DISCOUNT`` attribute before
  initializing the ``Pricer()`` class. This isn't good, as it changes the attribute
  for all later running tests

Mocking class helpers
---------------------

*NEEDS TO BE CONTINUED...*

https://yeraydiazdiaz.medium.com/what-the-mock-cheatsheet-mocking-in-python-6a71db997832


.. _patch: https://docs.python.org/3/library/unittest.mock.html#patch
.. _MagickMock: https://docs.python.org/3/library/unittest.mock.html?highlight=magicmock#unittest.mock.MagicMock
