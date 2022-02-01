Others
======
KISS :footcite:p:`kiss_itexico`
-------------------------------
.. admonition:: Definition
    :class: design_principle

    **Keep it simple, stupid.**

The simpler your code is, the simpler it will be to maintain it. Most systems
work best if they are kept simple rather than making them complex; therefore,
simplicity should be a key goal in design and unnecessary complexity should be avoided.

Try to avoid fancy features, only if those are required to solve your problem.

YAGNI :footcite:p:`kiss_itexico`
--------------------------------
.. admonition:: Definition
    :class: design_principle

    **You ain't gonna need it.**

Sometimes, you want to think ahead in your project and want to add some extra
features "just in case I'll them" or thinking "I will eventually need this". This
is wrong thinking: Don't implement something you don't need right away!

YAGNI is the principle behind the extreme programming (XP) practice of "Do the Simplest Thing
That Could Possibly Work".

.. footbibliography::

Low Coupling, High Cohesion (Constantine's Law) :footcite:p:`principles_wiki`
-----------------------------------------------------------------------------
.. admonition:: Definition
    :class: design_principle

    **A structure is stable if cohesion is strong and coupling is low.**

The *Cohesion* of a class is a measure of how well the internal parts of a module
(e.g. the methods and attributes of a class) belong together. Having a high cohesion means,
that a module should only comprise responsibilities which belong together.

Having a low cohesion means one module has several unrelated or only loosely related
responsibilities. A change in the requirements for one of these things also affect the
others which would not be the case in a highly cohesive module.

The *Coupling* of a module defines, how much it interacts with other modules. Having
a low coupling means, that these interactions are minimal. Those necessary interactions
must then be loose, which means module A must not have too many assumptions about module B.

This principle is backed by the :ref:`Dependency Inversion Principle <dependency_inversion_principle>`,
where module B contains interface implementations, whereas module A only knows about the interface,
but not the implementations.

.. footbibliography::

Links
-----
* http://wiki.c2.com/?PeopleProjectsAndPatterns
* http://principles-wiki.net/
* https://luminousmen.com/post/what-are-the-best-engineering-principles
