State Pattern
-------------
* Object change their behavior depending on the status they are currently in
* It does not matter, how the object got into a particular state, only the state itself

**Example**: Flywheel at subway station which requires card swipe to open

.. mermaid::
    :caption: Flywheel (e.g. subway example)

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

continue at 37:54
