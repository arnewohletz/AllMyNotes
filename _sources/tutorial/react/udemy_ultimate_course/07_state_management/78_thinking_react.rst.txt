What is "Thinking in React"?
============================
Thinking in **state transitions** , not element mutations.

Process (not rigid, often not as linear):

#. Break desired UI into **components** and establish a **component tree**
#. Build a **static** version of React (without state and interactivity)
#. Think about state:

    * When to use state
    * Types of state: local vs. global
    * Where to place each piece of state

#. Establish **data flow**:

    * one-way data flow
    * child-to-parent communication
    * accessing global state

Step 3 and 4 are about **stage management**.
