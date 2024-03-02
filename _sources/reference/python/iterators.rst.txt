Iterators & Generators
======================
Iterators are containers for objects which allow to loop over them using a "for" loop.
In contrast to *lists*, they don't store the objects in a specific order (you can't
pull one out from the middle), but *yields* those objects in a specific order,
often creating them on the fly, when needed. That is the purpose of a
*generator function*.

As an effect, they are much smaller in size than comparable lists (one million integer,
for instance, don't need to be in memory at once, but one by one).

| list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
| iterator: [generator function: count from 1 to 10, step-size 1]

* iterators are much faster to create than comparable lists
* iterators can be of unknown length, whereas the length of a list is always given

:Iterable:

    Any object which can be looped over using a *for* loop e.g.

    .. code-block:: python

        for item in some_iterable:
            print(item)

    Any iterable object must implement the :python:`__iter__()` method, which
    must return an *Iterator* object, which defines, how to loop over these
    particular object type in a for-loop.

    .. code-block:: python

        class MyIterable:

            def __init__(self, values: list):
                self.values = values

            def __iter__(self):
                return MyIterator(self)

:Iterator:

    Objects that define :ulined:`how` to loop over a sequence of *Iterables*.

    For instance, not all *Iterable* objects support indexing (0, 1, 2,...) like
    a list, but follow a different logic when they're used in a for-loop.

    An *Iterator* must implement these methods:

    * :python:`__init__(self)` ... called upon creation e.g. :python:`MyIterator()`.
      It commonly accepts the items, it is supposed to iterate over (and initializes
      an index, if items support indexes):

        .. code-block:: python

            def __init__(self, items):
                self._items = items
                self._index = 0

    * :python:`__iter__(self)` ... called when running :python:`iter(object)`.
      It must return an Iterator, so itself:

        .. code-block:: python

            def __iter__(self):
                return self

    * :python:`__next__(self)` ... called when running :python:`next(object)`.
      It returns an Iterable object and defines a logic to decide, which object
      is returned. If no object are left to produce, it commonly returns a
      *StopIteration* exception.

        .. code-block:: python

            def __next__(self):
                if(self._index < len(self._items)):
                    result = self._item(self._index)
                    index += 1
                    return result
                raise StopIteration

    .. important::

        An *Iterator* is also an *Iterable*, which means you can loop over iterators:

        .. code-block:: python

            numbers = [1, 2, 3]
            iterator1 = iter(numbers)
            iterator2 = iter(iterator1)
            print(iterator1 is iterator2) # True


.. admonition:: Definition

    #. Anything that can be passed to iter without a TypeError is an iterable
    #. Anything that can be passed to next without a TypeError is an iterator
    #. Anything that returns itself when passed to iter is an iterator

:Generator:

    A generator is a function which returns an *Iterator* of passed in *Iterables*.
    The generator function uses the :python:`yield` statement, which puts the
    function on pause between calls from the :python:`next()` function.

    .. code-block:: python

        def square_all(numbers):
            for n in numbers:
                yield n**2

    Generators are considered an easier, more common way to create Iterators objects,
    as defining an entire Iterator class (see above). The generator function
    commonly implements some logic which are applied to the *Iterable* items before
    yielding them. In case the Iterable does not support indexing, an index must be
    set to the next item manually.

    The same iterator can also be implemented using a :ulined:`generator expression`:

    .. code-block:: python

        def square_all(numbers):
            return (n**2 for n in numbers)

List comprehension statements can be transformed into a generator expression by
replacing the square brackets:

.. code-block:: python

    lines = [line.strip("\n") for line in poem_file if line != "\n"] # list comprehension
    lines = (line.strip("\n") for line in poem_file if line != "\n") # generator expression

Both generators functions and generator expressions return an iterator object.
Generator functions :ulined:`can be replaced` by a generator expression:

.. code-block:: python

    def get_a_generator(some_iterable):
        for item in some_iterable:
            if some_condition(item):
                yield item

    def get_a_generator(some_iterable):
        return(item for item in some_iterable if some_condition(item))

A generator expression always has common brackets ("()") around it. When using square
brackets ("[]") then the return type is not a generator, but a simple list (with all
possible values inside):

.. code-block:: python

    return (n**2 for n in favourite_numbers) # returns generator
    return [n**2 for n in favourite_nunbers] # returns list

**yield_from** in generator functions:

.. code-block:: python

    for num in range(start, stop):
        yield num

    # same as
    yield from range(start, stop)


Example
-------
This example shows the use of an custom Iterator *TeamIterator* class looping over
an Iterable *Team* class, which contains of *Member* objects, which are looped over:

.. code-block:: python

    class Member:

        def __init__(self, name):
            self.name = name


    class Team:

        def __init__(self):
            self.members = list()

        def add_member(self, member):
            self.members.append(member)

        def __iter__(self):
            return TeamIterator(self)


    class TeamIterator:

        def __init__(self, team):
            self._team = team
            self._index = 0

        def __iter__(self):
            return self

        def __next__(self):
            if(self._index < len(self._team.members)):
                result = self._team.members[self._index]
                self._index += 1
                return result
            raise StopIteration


    team = Team()
    team.add_member(Member("Frank"))
    team.add_member(Member("Lucy"))
    team.add_member(Member("Ole"))

    team_iterator = iter(team)
    while True:
        try:
            member = next(team_iterator)
            print(member.name)
        except StopIteration:
            break

which outputs:

.. code-block:: none

    Frank
    Lucy
    Ole

**Sources**

https://thispointer.com/python-how-to-make-a-class-iterable-create-iterator-class-for-it/
https://treyhunner.com/2019/06/loop-better-a-deeper-look-at-iteration-in-python/#Generators_are_iterators