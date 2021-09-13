State Pattern
-------------
* Object change their behavior depending on the status they are currently in
* It does not matter, how the object got into a particular state, only the state itself

**Example**: Turnstile at subway station which requires card swipe to open

.. mermaid::
    :caption: Turnstile (e.g. subway example)

    stateDiagram
        Closed --> Process : pay
        Closed --> Closed : pay_failed
        Closed --> Closed : pay_ok (Timeout)
        Closed --> Closed : enter
        Process --> Open : pay_ok
        Process --> Closed : pay_failed
        Process --> Process : enter
        Open --> Closed : enter
        Open --> Open : pay_ok
        Open --> Open : pay_failed

.. table:: Transitioning table (current state + action -> new state)

    +------------+-----------------------------------+---------+
    | **States** | **Actions**                                 |
    |            +---------+----------+--------------+---------+
    |            | *enter* | *pay_ok* | *pay_failed* | *pay*   |
    +------------+---------+----------+--------------+---------+
    | *closed*   | closed  | closed   | closed       | process |
    +------------+---------+----------+--------------+---------+
    | *open*     | closed  | open     | open         | open    |
    +------------+---------+----------+--------------+---------+
    | *process*  | process | open     | closed       | process |
    +------------+---------+----------+--------------+---------+

* An object must have a state variable, which contains a *state object* (conditionals are
  replaced by polymorphism)
* The state object will implements all action methods

Issue
`````
* Each action method has to be implemented for each current state
* Having more states and actions increases number of implementation significantly (each is a
  combination of a state and an action, so *implementations = amount of states x amount of actions*)
* Keeping track of state-action combinations hard for complex scenarios
* Each action method had to check the current status (is_closed(), is_processing(), ...)
* Solving it using a lot of *if*-statements or *switch*-cases is possible, but probably
  much harder as using the *State Pattern*

Solution
````````
.. admonition:: Definition
    :class: pattern_definition

    The **State Pattern** allows an object to alter its behavior when its internal state changes.
    The object will appear to change its class.

As seen from the diagram above, if the state of the object changes, the implementation of its
action methods may change.

.. mermaid::
    :align: center
    :caption: General class diagram

    classDiagram
        State "1..*" <-- Context : HAS-A
        State <|-- ConcreteStateA
        State <|-- ConcreteStateB
        class Context {
            +request()
        }
        class State {
            <<interface>>
            +handle()
        }
        class ConcreteStateA {
            +handle()
        }
        class ConcreteStateB {
            +handle()
        }

* When calling *request()* method from the *Context* class, it will delegate to *state.handle()*
  to handle the state.
* THe *Context* class does not know, which state it currently has, but calls the *handle()* method
  of the *State* class (actually, it's implementation in the currently active *ConcreteState* class)
  to handle the state

.. mermaid::
    :align: center
    :caption: Applied to upper example

    classDiagram
        GateState "1..*" <-- Gate : HAS-A
        GateState <|-- OpenGateState
        GateState <|-- ClosedGateState
        GateState <|-- ProcessingPaymentGateState
        class Gate {
            +request()
        }
        class GateState {
            <<interface>>
            +handle()
        }
        class OpenGateState {
            +handle()
        }
        class ClosedGateState {
            +handle()
        }
        class ProcessingPaymentGateState {
            +handle()
        }

continue at 45:06