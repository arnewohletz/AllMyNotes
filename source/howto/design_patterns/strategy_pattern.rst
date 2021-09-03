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

    * Each sub-class of parent class (*Duck*) potentially implements any method
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

    *