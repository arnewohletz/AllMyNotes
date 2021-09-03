Strategy Pattern
----------------
Issue
`````
Pure subclassing approach:

    .. mermaid::
        :align: center

        classDiagram
            Duck <|-- CityDuck
            Duck <|-- WildDuck
            Duck <|-- RubberDuck
            class Duck{
                +quack()
                +display()
                +fly()
            }
            class CityDuck{
                +display()
                +fly()
            }
            class WildDuck{
                +display()
                +fly()
            }
            class RubberDuck{
                +display()
                +fly()
            }

    * Each sub-class of the parent class (*Duck*) potentially implements any method
      differently than the parent class (no code reuse)
    * Multiple sub-classes might share common implementations of the same method but
      not the one from the parent class (e.g. *fly()*) -> code duplication
    * Letting sub-classes inherit method implementations from another
      class is not a good idea (-> multiple inheritance "Deadly Diamond Of Death") as
      it might lead to conflicts. Moreover, there are combinations of implementations
      which cannot be established over pure inheritance

Design Principles
`````````````````
.. admonition:: Principle 1
    :class: design_principle

    **Program to an interface, not an implementation**

    * Never create instances of implementing classes, but instead refer to an interface
    * Each interface sets a blueprint for its implementing subclasses, which do the actual
      implementation
    * When the class, holding references to these interfaces in form of class variables,
      itself is subclassed, then the children classes assign individual implementations of
      the interface to these class variables

.. admonition:: Principle 2
    :class: design_principle

    **Favor composition over inheritance**

    * Composition means building a HAS-A relationship with a class, which cannot be
      instantiated, either an abstract class or an interface
    * Sub-classes that have a composition relationship allows them to select an interface
      implementation during runtime
    * Defining behaviours during runtime occurs when the sub-class instantiates an interface
      implementation and assigns it to the inherited class variable of the interface type

Appliance
`````````
    .. mermaid::
        :align: center

        classDiagram
            FlyBehavior <-- Duck
            FlyBehavior <|-- SimpleFly
            FlyBehavior <|-- NoFly
            Duck <|-- CityDuck
            Duck <|-- WildDuck
            Duck <|-- RubberDuck
            class FlyBehavior{
                <<interface>>
                +fly()
            }
            class SimpleFly{
                +fly()
            }
            class NoFly{
                +fly()
            }
            class Duck{
                +quack()
                +display()
                +fly()
            }
            class CityDuck{
                +display()
                +fly()
            }
            class WildDuck{
                +display()
                +fly()
            }
            class RubberDuck{
                +display()
                +fly()
            }

    * Here, the various *fly()* method implementation are moved from the duck sub-classes
      and put into proper classes, that implement the *FlyBehavior* interface
    * Same can be done with the *quack()* or the *display()* method, if required
    * That way, each sub-class of Duck has the desired behavior without implementing any
      of it themselves

:Context:
    Parent class for all *Client* classes

:Client:
    Subclass of the *Context* class

:Strategy:
    Interface class for all Strategy implementations

Find a template example for Python at https://refactoring.guru/design-patterns/strategy/python/example

Taking it one step further, it is also possible to refrain from using actual *Clients*, but
instead instantiate the *Context* class (here: Duck) **with** passing the wanted behavior into
the constructor (*dependency injection*):

.. code-block:: python

    from abc import ABC, abstractmethod

    class Duck:
        def __init__(fly_behavior: FlyBehavior,
                     quack_behavior: QuackBehavior):
            self.fly_behavior = fly_behavior
            self.quack_behavior = quack_behavior

        def fly():
            self.fly_behavior.fly()

        def quack():
            self.quack_behavior.quack()

    class FlyBehavior(ABC):
        @abstractmethod
        def fly():
            pass

    class QuackBehavior(ABC):
        @abstractmethod
        def quack():
            pass

    # some classes implementing FlyBehavior & QuackBehavior
    # e.g. FlyNoWay, QuackNoWay

    if __name__ == "__main__":
        no_use_duck = Duck(fly_behavior=FlyNoWay(), quack_behavior=QuackNoWay())
        no_use_duck.fly()
        no_use_duck.quack()