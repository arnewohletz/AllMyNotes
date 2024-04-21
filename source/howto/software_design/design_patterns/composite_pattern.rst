Composite Pattern
-----------------
Idea
````
* Be able to treat a collection of objects with whole-part relationships uniformly
* Whole-part relationship means having a top level component, that contains composite objects
  (component object holding other components) and leaf objects (component object that contain no other components)
* On any composite and any leaf object the client can call the same methods (i.e. *print()*)
  -> the composite objects display by telling their components to call *print()* and the leaf
  objects will call print on themselves
* Each composite or leaf object must implement the same component interface
* Components have a different method implementation as the leafs
* Not every method makes sense for every object implementing the component interface
  -> those can be ignored by returning null or false or throw an exception the client needs to
  handle (i.e. ignoring by offering an empty catch block)
* From the client side there is no difference between a composite object or a leaf object within
  the tree structure

.. admonition:: Definition
    :class: pattern_definition

    The **Composite Pattern** allows you to compute objects into tree structures to
    represent part-whole hierarchies. Composite lets clients treat individual object and
    compositions of objects uniformly.

.. mermaid::
    :align: center

    classDiagram
        Component <|-- Leaf : implements
        Component <|-- Composite : implements
        Component "1..*" <-- Composite : ___HAS-A___
        class Component {
            <<interface>>
            +operation()
        }
        class Leaf {
            +operation()
        }
        class Composite {
            +operation()
        }

.. hint::

    In the book, the components interface (or abstract class) also features an
    *add(Component)* and a *remove(Component)* method in order to add and remove
    Components from the hierarchy structure.

    This violates the :ref:`Open-Closed Principle <open_closed_principle>`, which does
    not allow to change the hierarchy structure once it has been created.

    It probably depends on the application, if these methods are absolutely required.

    But stating these in the *Component* class will pass these methods onto *Leaf* classes,
    which clearly are not supposed to use it (must return None or throw an error, if so).
    Defining those methods in the *Composite* class breaks the pattern, since both *Composite*
    and *Leaf* classes should be uniform, so the client mustn't differentiate (client needed to
    check the type of the class before using it).

    The way a hierarchy should be changed is by **creating a modified copy of it** (same as when
    changing the value of a string or integer)

Application
```````````
* Applied to data, which can be hierarchically represented, to compute it easily
* Often applied in **GUIs** (main page consists of sub-components, which itself are made up of sub-components,
  and a *refresh()* call on an higher-level component will trigger *refresh()* on all of it's sub-components and leaves)

Find a template example for Python at https://refactoring.guru/design-patterns/composite/python/example

.. literalinclude:: _code/composite.py
    :language: python
