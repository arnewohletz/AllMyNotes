Decorator Pattern
-----------------
Issue
`````
An object behavior (-> base object or *component*) is supposed to be changed at runtime (not compile time),
which means that the object's code is not supposed to be changed, but merely adapted for one call.

Design Principles & Definition
``````````````````````````````
.. _open_closed_principle:

.. admonition:: Open-Closed Principle
    :class: design_principle

    **Classes should be open for extension, but closed for modification**

    The goal is to allow classes to be easily extendable to incorporate new behavior
    without modifying existing code. Focus its appliance to those areas, which are most
    likely to change as applying this principle everywhere in your code is unnecessary
    and can lead to complex, hard-to-understand code.

.. admonition:: Definition
    :class: pattern_definition

    The **Decorator Pattern** attaches additional responsibilities to an object dynamically.
    Decorators provide a flexible alternative to subclassing for extending functionality.

Idea
````
* The base object is "wrapped" by additional objects, that add behavior to it without the need
  to change the base class
* The amount and type of wrappers used for a function call defines the behavior
* Each wrapper layer may define custom behavior to the function call or its return value

.. figure:: _img/DecoratorPattern1.jpg

    Outmost wrapper function is called first (*speak()*), which calls the next inner function
    until base object returns something, which is then again eventually passed along to the original function call

How wrappers work:
    * All wrappers must be of the same type as the base class is (IS-A) in order to act like it
      (from outside they behave just like the base class) -> implementing a wrapper super-class which itself extends
      the base class supertype
    * All wrappers must contain an object of the base class type (HAS-A) to use composition (adding behavior dynamically)
      (required to call the next inner wrapper or base class) -> wrapped object is assigned during wrapper instantiation
    * Each wrapper implements the desired base class functions differently
    * When a method is called on a wrapped object, the method call is first processed by the outermost wrapper
    * That outermost wrapper calls the same function of its wrapped object and make some characteristic
      changes to the result returned from it
    * That wrapped object can be the base object or another wrapper of the same type or any other type inheriting
      from the same wrapper super-class

.. mermaid::
    :align: center

    classDiagram
        Beverage <|-- Decaf
        Beverage <|-- Espresso
        Beverage <|-- AddonDecorator : IS-A
        Beverage <-- AddonDecorator : HAS-A
        AddonDecorator <|-- CaramelDecorator
        AddonDecorator <|-- SoyDecorator
        class Beverage{
            +get_desc()
            +cost()
        }
        class Decaf{
            +cost()
        }
        class Espresso{
            +cost()
        }
        class AddonDecorator{
            +get_desc()
        }
        class CaramelDecorator{
            +get_desc()
            +cost()
        }
        class SoyDecorator{
            +get_desc()
            +cost()
        }

* In this example, all classes of type *Beverage* function as the base class and all classes of type *AddonDecorator*
  function as decorator classes (wrappers)
* Instead of creating lots of concrete Beverage classes (like DecafWithCaramelAndSoy), we are able to decorate the
  base class (e.g. *Decaf*) with a random amount of decorators (e.g. *CaramelDecorator* & *SoyDecorator*)

In general

* each decorator refers to the inner object (may it be the base class or another wrapper). For this, it needs an object of
  that type (HAS-A), but the same time it can be used as that inside object by another wrapper of the same type (therefore IS-A)
* a wrapper function implementations are completely dependent on the scenario. Some may not even refer to the inner wrapped object
  (e.g. purpose is to multiple input with 0, which always will be zero, no matter what the inner "thing" is), but immediately turn
  direction and return a value to the outside layer
* it is an flexible alternative to sub-classing by providing more functionality to a base object

:Component:
    Base class for all concrete component (undecorated classes)

:Decorator:
    Base class for all concrete decorator

Appliance
`````````
Find a template example for Python on https://refactoring.guru/design-patterns/decorator/python/example

Implementation of the upper example:

    .. literalinclude:: _code/decorator.py
        :language: python

.. warning::

    The decorator pattern is not very suitable for this example, as

        * the decorator implementation of *cost()* don't significantly differ (only added value is different differs).
          This could be more easily done within constructor of a concrete beverage, passing in a list of addon prices.
        * using the decorator pattern here violates the rule of separating concerns: here the *cost()*
          method implementation does specify the way of how (*logic*) the addon affects the cost of the base object **and**
          also specifies the value by how much (*magnitude*) the cost is changed. In this particular case, it is unnecessary
          to specify the logic in each concrete addon decorator, since that is unlikely to change (costs for each addon will
          probably always be added to base price, not multiplied or in more complex ways).
        * the added change of any decorator does not affect the *behavior* of the decorate object (*Beverage*)
          but merely its *state* (cost parameter), whereas the decorator pattern should foremost be used for the former.
