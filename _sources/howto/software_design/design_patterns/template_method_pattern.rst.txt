Template Method Pattern
-----------------------
* A *Template* is a class which contains template methods
* A template class might leave gaps for subclasses to fill i.e. abstract methods
* A subclass of a template class is a concretization of the template class
* Invariant parts -> Base class
* Variant parts -> Concrete subclass
* Example for applications following the :ref:`Open-Closed Principle <open_closed_principle>`
* The concrete implementation fo the template class is then instantiated for usage

Principles & Definition
```````````````````````
.. admonition:: Hollywood Principle
    :class: design_principle

    **Don't call use, we call you.**



.. admonition:: Definition
    :class: pattern_definition

    The **Template Method Pattern** defines the skeleton of an algorithm in a method,
    deferring some steps to subclasses. Template Method lets subclasses redefine certain
    steps of an algorithm without changing the algorithm's structure.


.. mermaid::
    :align: center

    classDiagram
        AbstractClass <|-- ConcreteClassA
        AbstractClass <|-- ConcreteClassB
        class AbstractClass{
            +template_method()
            +operation_1()*
            +operation_2()*
        }
        class ConcreteClassA{
        }
        class ConcreteClassB{
        }

operation_1() &operation_2() are abstract methods

* the *template_method()* uses the abstract operations within its own implementation (abstract
  operations: subclasses define the concrete operation methods)
* that way we cannot say what the *template_method()* actually does, but only know about its structure
* the *Template Method Pattern* is similar to the *Strategy Pattern*, but the Template Method Pattern
  defines invariant parts that are certain to stay valid over time whereas the *Strategy Pattern* does not
* the *Template Method Pattern* is often used for frameworks, where the interface must stay solid for
  users to use it

COPIED FROM EVERNOTE

CAUTION: Think careful, if your system applies for the Template Pattern, because the Strategy Pattern might suffice here (and doesn't state invariable parts)
* The TemplateMethod() could be replaced by a set of behavior methods injected by Strategy classes and methods
* The execution order would be fix, but the methods itself can be changed for all concrete implementations of the composing interface
* Composition should be preferred over inheritance and the Template Pattern is built around inheritance

.. figure:: _img/templatepattern2.jpg

    Example: Blog Posts System with database save

Hook operations:
* provides an empty implementations
* concrete subclasses may override the hook functions

Hollywood Principle (Don't call us, we call you):
* The Record class says to the User not to worry about saving a User object. If anything fails, Record will call the User's FailedSave() method
