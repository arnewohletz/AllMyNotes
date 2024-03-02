Proxy Pattern
-------------
Issue
`````
* You want to hide certain access points of a class to *Clients*, in other words, control the
  access of a particular class or system


Solution
````````
There are three types of proxies:
    * Remote proxy
        * Used when accessing a remote system or project
        * The proxy is then used to access this remote interface
    * Virtual proxy
        * Controls access to a resource that is expensive to create (in terms of CPU time)
        * The proxy then controls whether it is actually needed to interact with
          the resource it controls the access for
    * Protection proxy
        * Defines whether the caller its method is actually allowed to interact with
          the resource it controls (access management)
        * Controls access to resources based on access rights

* A proxy adds additional behavior to the resource it controls, but in terms of access control

.. admonition:: Definition
    :class: pattern_definition

    The **Proxy Pattern** provides a surrogate or placeholder for another object to
    control access to it.

Example
```````
Illustration of a *Virtual Proxy*.

Issue
'''''
* instantiating a **BookParser** will parse the entire *book* string (which contains
  the entire content of a book) and does some computations while doing it (like count verbs,
  words, chapters, pages, ...) -> it is expensive
* calling any of its methods (like number_of_pages(), which returns the amount of pages) is very
  cheap, because no further computation is required to get it
* the computation of these attributes during parsing is, on the other hand, only necessary, if
  any of the attribute-returning methods is actually called (which might not be the case for each
  instantiated *BookParser*)

.. code-block:: python

    str book = "....<entire book>..."
    book_parser = BookParser(book) # expensive instantiation
    print(book_parser.number_of_pages()) # cheap call

Solution
''''''''
* in order to increase performance, we only want to parse a string in the *BookParser* when
  any of its method (which require that computation) is called (make it lazy)
* we achieve this by not directly interacting with the *BookParser* but with a *BookParserProxy*,
  which interacts with the *BookParser*

:Subject:
    An interface class, which is implemented by both *RealSubject* and *Proxy*
    to ensure that both have the same interface

:RealSubject:
    The class that is the actual class we want to call

:Proxy:
    The class which is called by a *Client* instead of *RealSubject*. Since both implement
    the same interface, the *Client* can treat the *Proxy* equally to *RealSubject*.

.. mermaid::
    :align: center

    classDiagram
        Subject<|--RealSubject : implements
        Subject<|--Proxy : implements
        RealSubject<--Proxy : HAS-A
        class Subject {
            <<interface>>
            +request()
        }
        class RealSubject {
            +request()
        }
        class Proxy {
            +request()
        }

* the *Proxy* controls the access to *RealSubject*
* the *Proxy* follows the same interface as the thing it is proxying
* the *Proxy* does not have to instantiate *RealSubject* during its own creation,
  but may instantiate it in its method

Code Example
''''''''''''
Find a template example for Python at https://refactoring.guru/design-patterns/proxy/python/example

.. literalinclude:: _code/proxy.py
    :language: python