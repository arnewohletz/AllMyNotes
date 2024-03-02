.. _factory_method_pattern:

Factory Method Pattern
----------------------
Issue
`````
* At a certain point in the program, you need an object of a certain type, but you
  don't know which sub-class you actually need
* Decisions which type of object is created depends on business logic
* Multiple business logic sets might exist in parallel (e.g. create totally randomly, create
  by making sure each object type is equally often instantiated)
* The instantiation logic might be needed at different places in the code -> duplication
* If the logic changes, these changes must be done to any usage in the code -> hard to maintain

To summarize, we should use the *Factory Method Pattern* where there is logic involved in the
creation of an object and when this logic repeats itself

Design Principles & Definition
``````````````````````````````
.. admonition:: Definition
    :class: pattern_definition

    The **Factory Method Pattern** defines an interface for creating an object, but lets
    subclasses decide which class to instantiate. Factory Method lets a class defer
    instantiation to subclasses.

Solution
````````
* Object instantiation is moved into separate classes
* These classes do nothing but instantiate the proper object and return it
* These classes are called *Factory classes*
* Various amount of *Factories classes* for the same object may exist, each implementing
  a different type of business logic on which object is instantiated and returned
* Multiple factories should implement the same *Factory interface*, which thereby defines a
  blueprint for these *Factory classes*

.. mermaid::
    :align: center

    classDiagram
        Product <|-- ConcreteProduct : implement
        ConcreteProduct <|-- ConcreteCreator : creates
        Creator <|-- ConcreteCreator : implement
        class Creator {
            +factory_method()
        }
        class ConcreteCreator {
            +factory_method()
        }

* The *ConcreateCreator* creates objects of type *Product*, in which the internal logic
  of its *factory_method()* decides which *ConcreteProduct* is eventually returned
* The *Creator* also assigns *Product* as the return type of *factory_method()*

Example
```````
Find a template example for Python at https://refactoring.guru/design-patterns/factory-method/python/example.

    .. literalinclude:: _code/factory_method.py
        :language: python

.. hint::

    There might be scenarios where the *Adaptee* is external and out of our control and not
    instantiatable (e.g. only using static methods). In that case, *Adaptee* cannot be passed
    into the constructor of *Adapter*, but needs to be directly called in the *Adapter*'s methods
    (e.g. *requests()*):

        .. code-block:: python

            class Adapter:

                def __init__(self):
                    pass

                def request():
                    Adaptee.specific_request()