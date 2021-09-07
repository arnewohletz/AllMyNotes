Abstract Factory Pattern
------------------------
Is a sub-set of the :ref:`Factory Method Pattern <factory_method_pattern>`. Difference:

Each factory (creator) is able to create **multiple** products, not only one
-> ability to create families of related or dependent objects (the abstract factory is a blueprint,
that defines what type of Product a factory must be able to instantiate)

.. admonition:: Definition
    :class: pattern_definition

    The **Abstract Factory Pattern** provides an interface for creating families of related
    or dependent objects without specifying their concrete classes.

.. thumbnail:: _img/Abstract_Factory_Pattern.jpg

The interface factory implements multiple creation methods, in which each is supposed
to instantiate a different type of object.

Example
```````
Use the Abstract Factory when your code needs to work with various families of related
products, but you don’t want it to depend on the concrete classes of those products—they
might be unknown beforehand or you simply want to allow for future extensibility.

Find a template example for Python at https://refactoring.guru/design-patterns/abstract-factory/python/example

Applications are
* User interfaces (compatability for multiple OS)
* Light Theme / Dark Theme implementations


.. literalinclude:: _code/abstract_factory.py
    :language: python
