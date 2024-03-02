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

.. admonition:: Principle 1
    :class: design_principle

    **Depend upon abstraction. Do not depend upon concrete classes.**

    This is known as the *Dependency Inversion Principle*. It appears similar to
    the principle, to program against an interface, not an implementation, but goes
    one step further: It defines, that even the high level classes (e.g. a Zoo class),
    should depend on an abstraction (e.g. an Animal class), as well a low level
    classes (e.g. Rabbit), which implements the abstraction.

    Some guidelines which help to follow the *Dependency Inversion Principle*:

        * No variable should hold reference to a concrete class
        * No class should derive from a concrete class
        * No method should overwrite an implemented method of any of its base classes

    Naturally, these rules must often be broken, but it is a guideline to strive for.

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
