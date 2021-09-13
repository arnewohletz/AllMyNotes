Iterator Pattern
----------------
Issue
`````
* I want to iterate through a collection, but I don't want to care about its structure
* Known iterable types are not sufficient or I don't know about the structure, just need a way to get
  all elements from the structure
* The structure must not be of any known iterator type (e.g. list), but can be anything I want
* Trying to reshape the data of differently structured classes to become compatible with
  each other might be difficult to achieve and the logic to get to this format will be
  different for each structure

Solution
````````
* Uniform way to iterate over various collections of items, which derive from the same
  interface, but vary in its structure
* The iterate method is not returning all elements as flattened list at once, but returns
  item after item with each time the iterate method is called
* That way the collection does not expose it's structure
* Lazy Evaluation: By return only the next item, a result can be immediately checked and stopped
  if wanted item is returned. This allows infinite collections
* the iterator knows its current item, as well as the last and next one
* The Iterator Pattern is a way of encapsulating the iteration specifics, to move it out of the
  code using it

.. admonition:: Definition
    :class: pattern_definition

    The **Iterator Pattern** provides a way to access the elements of an aggregate object
    sequentially without exposing its underlying representation.

.. mermaid::
    :align: center

    classDiagram
        Iterable <|-- ConcreteIterable : implements
        Iterator <|-- ConcreteIterator : implements
        Iterable <-- Client : HAS-A
        Iterator <-- Client : HAS-A
        ConcreteIterator <-- ConcreteIterable : creates
        ConcreteIterable <-- ConcreteIterator : HAS-A
        class Iterable {
            +get_iterator() Iterator
        }
        class ConcreteIterable {
            +get_iterator() Iterator
        }
        class Iterator {
            +has_next() bool
            +next()
            +current() Item
        }
        class ConcreteIterator {
            +has_next() bool
            +next()
            +current() Item
        }

* the *get_iterator()* method will return an object of type *Iterator*
* Each *ConcreteIterable* may have a different structure, so *get_iterator()* will return
  a different *ConcreteIterator*
* a *ConcreteIterable* is a factory, that produces *ConcreteIterators*
* the *has_next()* method returns, if the iterator has a next element (or is at its end)
* the *next()* method moves the pointer to the next element
* the *current()* method returns the element the iterator's index is currently pointing to
  (here: using the type *Item*)
* the *has_next()*, *next()* and *current()* methods can be combined (either all of them or just two),
  but this violates the `Command-query separation`_ principle (see below)

.. admonition:: Command-Query separation
    :class: design_principle

    Functions should either be **queries** or **commands**. Queries are for getting
    data, but must not change the state. Commands are supposed to change the state, but
    must not return any data. Functions must not do both.

* *ConcreteIterable* create *ConcreteIterator* instances, not *Iterator* instances
* The *HAS-A* relationship between *ConcreteIterator* and *ConcreteIterable* is **optional**. In case
  it exists, the *ConcreteIterable* must pass itself into the *ConcreteIterator* constructor, so the
  *ConcreteIterator* has a reference to what it is supposed to iterate over. The other way is, not to
  pass the *ConcreteIterable* into the constructor, but only the data, the *ConcreteIterator* is
  supposed to iterate over

The reason why to keep *Iterable* and *Iterator* separate and not combine them in one class, is
that it had more than one responsibility: defining how to iterate over a set of item (*Iterable*) and
performing iteration over an iterable (*Iterator*). This violates the
`Single-responsibility principle`_:

.. admonition:: Single-Responsibility Principle
    :class: design_principle

    **A class should have only one reason to change**

    This implies a class must have only one purpose. For instances, printing a set of data.
    In that case, the only reason to change the class is because the way the data is printed
    should be different.

.. _Command-query separation: https://en.wikipedia.org/wiki/Command%E2%80%93query_separation
.. _Single-responsibility principle: https://en.wikipedia.org/wiki/Single-responsibility_principle

Example
```````
Find a template example for Python at https://refactoring.guru/design-patterns/iterator/python/example

.. literalinclude:: _code/iterator.py
    :language: python

continue at 1:26:59 https://www.youtube.com/watch?v=uNTNEfwYXhI