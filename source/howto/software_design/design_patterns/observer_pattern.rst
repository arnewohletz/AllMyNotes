Observer Pattern
----------------
Issue
`````
* One or more objects needs to know. when a different objects (Subject) changes its state
* When all these objects need to ask the *Subject* object individually for potential changes (e.g. every 10 ms),
  there will be a lot of queries (Polling) -> lots of queries

Solution
````````
* The *Subject* pushes change information to its *Observers* (subscribers) objects
* all *Observer* objects need to register for a *Subject* object to receive changes
* when a change occurs in *Subject* the information is **pushed** to all registered *Oberserver* objects

.. note::

    *Subject* class will be referred to as *Observable* from here on for clearer naming.

.. admonition:: Definition
    :class: pattern_definition

    The **Observer Pattern** defines a one-to-many dependency between object so that when one
    object changes state, all of its dependencies are notified and updated automatically.

.. mermaid::
    :align: center

    classDiagram
        Observer "0..*" <-- Observable : HAS-A
        Observer <|-- ConcreteObserver : implements
        Observable <|-- ConcreteObservable : implements
        ConcreteObservable <-- ConcreteObserver : HAS-A
        class Observable {
            <<interface>>
            +add(Observer)
            +remove(Observer)
            +notify()
        }
        class Observer {
            <<interface>>
            +update()
        }
        class ConcreteObservable {
            +add(Observer)
            +remove(Observer)
            +notify()
            +get_state()
        }
        class ConcreteObserver {
            +update()
        }

* a *ConcreteObservable* updates its registered *ConcreteObservers* by calling their *update()* method
* a *ConcreteObservable* class has additional methods to do create or obtain the data, it is supposed to
  push towards its registered *ConcreteObservers*

.. warning::

    The *ConcreteObservable* class violates the :ref:`Open-Closed Principle <open_closed_principle>` since it
    handles the notification of its registered *ConcreteObservers* **and** has other logic of whatever it is
    the object is doing (e.g. pulling some data from a weather station), here bound to the method *get_state()*.

* a *ConcreteObservable* passes itself into the constructor of *ConcreteObserver*. This allows the *ConcreteObservable*
  to call the *update()* method without passing itself or the updated data, since the *ConcreteObserver* can reference
  it itself

Example
```````
Find a template example for Python at https://refactoring.guru/design-patterns/observer/python/example.

A weather station, which contains a sensor to measure the temperature (and other data) and multiple devices,
which each display the data.

.. mermaid::
    :align: center

    classDiagram
        Observer "0..*" <-- Observable : HAS-A
        Observer <|-- PhoneDisplay : implements
        Observer <|-- DeskDisplay : implements
        Observable <|-- WeatherStation : implements
        WeatherStation <-- PhoneDisplay : HAS-A
        WeatherStation <-- DeskDisplay : HAS-A
        class Observable {
            <<interface>>
            +add(Observer)
            +remove(Observer)
            +notify()
        }
        class Observer {
            <<interface>>
            +update()
        }
        class WeatherStation {
            +add(Observer)
            +remove(Observer)
            +notify()
        }
        class PhoneDisplay {
            +update()
        }
        class DeskDisplay {
            +update()
        }

.. literalinclude:: _code/observer.py
    :language: python

