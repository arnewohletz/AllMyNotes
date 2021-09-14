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

.. _transitioning_table:

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
  to handle the *State*.
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
        Gate <-- OpenGateState : HAS-A
        Gate <-- ClosedGateState : HAS-A
        Gate <-- ProcessingPaymentGateState : HAS-A
        class Gate {
            +enter()
            +pay()
            +pay_OK()
            +pay_failed()
            +transition_to(state: State)
        }
        class GateState {
            <<interface>>
            +enter()
            +pay()
            +pay_OK()
            +pay_failed()
        }
        class OpenGateState {
            +enter()
            +pay()
            +pay_OK()
            +pay_failed()
        }
        class ClosedGateState {
            +enter()
            +pay()
            +pay_OK()
            +pay_failed()
        }
        class ProcessingPaymentGateState {
            +enter()
            +pay()
            +pay_OK()
            +pay_failed()
        }

* the methods of *Gate* blindly delegate to the *GateState*, which the logic about the gate's state
  (here, the *Gate* class doesn't do anything but calling the respective method on the *GateState*
  implementing class, though it also could do something before or after calling it)
* each concrete State class implements all Context methods to have all combinations from the
  :ref:`transitioning table <transitioning_table>` and implements the behavior expected from that state
* there are various ways of changing the state of the *Gate* class:

    * The simplest way is to give then *ConcreteState* classes a reference to the *Gate* class in
      order to call a *Gate*'s *transition_to(state: State)* method which changes the *Gate*
      classes state. This is the approach **used in the Gate example**

        .. warning::
            This approach violates the :ref:`Open-Closed Principle <open_closed_principle>`
            since the original *Gate* class is mutated

    * To **avoid mutation** make the *ConcreteState* classes changing-state methods return a
      *ConcreteState* object, which the *Gate* class will use the return a new *Gate* class to
      the *Client* (original caller) with the proper state set

.. literalinclude:: _code/state.py
    :language: python
