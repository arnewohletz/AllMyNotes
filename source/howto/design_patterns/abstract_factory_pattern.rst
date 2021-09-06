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

Example
```````
The interface factory implements multiple creation methods, in which each is supposed
to instantiate a different type of object.

.. thumbnail:: _img/Abstract_Factory_Pattern.jpg

