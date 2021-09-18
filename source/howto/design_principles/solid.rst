SOLID
=====
Single-Responsibility Principle (SRP)
-------------------------------------
.. admonition:: Definition
    :class: design_principle

    **"There should never be more than one reason for a class to change."**

If a class has only one responsibility, it only had to be changed because that responsibility
has to be changed.

Having a single responsibility does not mean, this class should be only one method, but that everything
it contains is there for only one purpose, which the class is fulfilling within a program.

A responsibility of a class might be to print a set of data. Following the
principle, it should not also be responsible for getting the data from a file or database, but
only to print it, maybe in hundreds of ways, each implemented in a different method,
but each only does print the data.

For two different change request, never should the same class be changed for both these requests.

Open-Closed Principle (OCP)
---------------------------
.. admonition:: Definition
    :class: design_principle

    **Modules should be open for extension, but closed for modification.**

It means, you should be able to change **what** the module (or class) does, without changing the module.

Adding a new feature to an application should be possible without changing the existing code, but only
by adding new one.

A code smell for violating the Open-Closed principle is, that introducing a change in one module will
require a lot of other modules to recompile, because they depend on it.

The :ref:`decorator pattern <decorator_pattern>` addresses this issue by wrapping object,
that are not supposed to be modified with a another object, that adds to the functionality
of the wrapped class by having a logic that makes use of the methods of the wrapped class.

Liskov substitution principle
-----------------------------
.. admonition:: Definition
    :class: design_principle

    **Derived subclasses must be usable through the base interface, without the need
    for users to know the difference.**

It means, that every subclass of an interface must be compatible to inherit the behaviour
of its superclass.

A common code smell is, if you need to check the type of an object (not always, but often),
since you cannot trust, that the object will behave the way it is expected.

An example of the Liskov's substitution principle is to substitute a ``Square`` for a
``Rectangle`` (Square is a subclass of Rectangle), because a rectangle can have two
different sized sides, whereas the square always has two equally sized sides.

Interface segregation principle
-------------------------------
.. admonition:: Definition
    :class: design_principle

    **It is better to have many small interfaces, rather than a few large interfaces.**

    or

    **Clients should not be forced to depend upon interfaces that they do not use.**

As an example, stating all methods which need to be implemented by a concrete subclass
inside one single interface may lead to the subclass having to implemented methods it does
not need or must not have.

.. mermaid::
    :align: center
    :caption: All concrete animal behavior is defined in one interface (Animal)

    classDiagram
        IAnimal <|-- Animal
        class IAnimal {
            <<interface>>
            +eat()
            +move()
            +sleep()
        }

Instead, smaller *Roles* for a concrete classes behavior should be defined and passed to
the concrete class during instantiation.

.. mermaid::
    :align: center
    :caption: Animal behavior is defined in separate interfaces

    classDiagram
        ICanEat <-- Animal
        ICanMove <-- Animal
        ICanSleep <-- Animal
        class ICanEat {
            <<interface>>
            +eat()
        }
        class ICanMove {
            <<interface>>
            +move()
        }
        class ICanSleep {
            <<inteface>>
            +sleep()
        }

Each concrete Animal then may implement all three interfaces. This favors composition over
inheritance and decoupling over coupling, as behavior for concrete Animal classes is more
flexibel. There might be Animals, that cannot move, so those won't be forced to implement
a method they don't use.

Moreover, other concrete classes like *Plant* could implement some of these interfaces
(e.g. only the *ICanEat*), so an interface originally defined for one type of concrete class
can also be used by other classes.

.. _dependency_inversion_principle:

Dependency inversion principle
------------------------------
.. admonition:: Definition
    :class: design_principle

    **Depend upon abstraction. Do not depend upon concrete classes.**

This principle takes the principle to program against an interface one step further.
It defines, that even the high level classes (e.g. a Zoo class), should depend on an
abstraction (e.g. an Animal class), as well a low level classes (e.g. Rabbit), which
implements the abstraction.

The *inversion* means, that the lower level classes derive from a higher level abstraction,
and high level classes referencing these abstraction instead of the lower level implementations
(instead of high level classes directly depending on these lower level concretions).

.. mermaid::
    :align: center
    :caption: High level class (Zoo) depends on lower level implementations (animal types) -> Bad!

    classDiagram
        Rabbit <-- Zoo
        Zebra <-- Zoo
        Monkey <-- Zoo

.. mermaid::
    :align: center
    :caption: High level & low level classes both depend on abstraction (Animal) -> Good!

    classDiagram
        Zoo <-- Animal
        Animal <|-- Rabbit
        Animal <|-- Zebra
        Animal <|-- Monkey
        class Animal {
            <<interface>>
        }

As an example, the :ref:`Factory Method Pattern <factory_method_pattern>` follows the principle
by providing an abstract factory class which implementations eventually create an instance
of a concrete class (based on its internal logic), which also depend on an abstract class.

Some guidelines which help to follow the *Dependency Inversion Principle*:

    * No variable should hold reference to a concrete class
    * No class should derive from a concrete class
    * No method should overwrite an implemented method of any of its base classes

Naturally, these rules must often be broken, but it is a guideline to strive for.
