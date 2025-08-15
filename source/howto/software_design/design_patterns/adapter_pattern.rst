Adapter Pattern
---------------
Issue
`````
* A class (*Client*) wants to call a method of another class (*Adaptee*) using a certain
  method call
* The *Adaptee* class doesn't have the method the *Client* wants to use -> their interfaces
  are incompatible

Applications
````````````
* The *Adaptee* class is part of an external library (out of our control), but we still want to
  use a different function name internally for the external call
* or we aren't sure whether we will use this particular external library forever and then be able
  to switch to another external function quickly
* The methods which the *Client* is trying to call is not constant, but open for change. In this case
  we don't want to change the method calls everywhere in the code, but only in one place

.. hint::

    An adapter can also be called wrapper. The purpose of the adapter is not to add, remove or
    change any behavior of the wrapped class, but merely to offer an expected signature to outside
    callers.

Definition
``````````
.. admonition:: Definition
    :class: pattern_definition

    The **Adapter Pattern** converts the interface of a class into another interface the clients
    expect. Adapter lets classes work together that couldn't otherwise because of incompatible
    interfaces.

:Client:
    The class which wants to execute a method on an incompatible *Adaptee* class

:Target:
    The interface class, which contains the method(s), a *Client* expects to be able to call
    upon the actual targeted class (*Adaptee*)

:Adapter:
    The class implementing the *Target* interface, thereby acting as an Adapter for *Client*
    by calling the *Adaptee* upon being called by the *Client*

:Adaptee:
    The class being adapted by an *Adaptor* and is executing its internal request method
    (e.g. *specific_request()*) which is triggered by the *Adapter*. It might be an external class.

.. mermaid::
    :align: center

    classDiagram
        Target <-- Client : HAS-A
        Target <|-- Adapter : implements
        Adapter <-- Adaptee : HAS-A
        class Target {
            <<Interface>>
            +request()
        }
        class Adapter {
            +request()
        }
        class Adaptee {
            specific_request()
        }

Example
```````
Find a template example for Python at https://refactoring.guru/design-patterns/adapter/python/example

.. literalinclude:: _code/adapter.py
    :language: python
