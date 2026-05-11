.. _tutorial_react_ultimate_state_management_fundamentals:

Fundamentals of state management
================================
State Management:

    Deciding **when** to create pieces of state, what **types** of
    state are necessary, **where to place each piece of state and how data **flows**
    through the app.

    --> giving each piece of state a **home**

As applications grow, state cannot be generally kept inside each component.

Local vs. Global State
----------------------
Inside React, a piece of state is either local or global.

**Local state**:

* state needed **only by one or few components**
* state is defined inside the component, **only this component and its child**
  **components** have access to it (by passing via props)

**Global state**:

* state that **many components** might need
* **shared** state that is accessible to **every component** in the entire application

.. hint::

    Global state can be defined via React API or external state management tools
    such as `Redux`_.

.. _Redux: https://react-redux.js.org/

.. hint::

    We should always start with local state and only use global state, if it is needed.

.. _tutorial_react_ultimate_state_management_fundamentals_when_and_where:

State: When and where?
----------------------

.. thumbnail:: _file/state_where_and_when_no_global.jpg

    When and where use state (without global state)

