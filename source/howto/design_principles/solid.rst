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

    **dsfdsf**


Dependency inversion principle
------------------------------


