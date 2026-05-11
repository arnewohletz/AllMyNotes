How to split a UI into components
=================================
When do we actually need to create another component?

Component Size
--------------
Too **large** components:

    * have too many **responsibilities** (a component should only **do one thing**,
      just like functions)
    * might need too many **props**
    * hard to **reuse**
    * **complex** code, hard to understand

Too **small** components:

    * will lead to too many components
    * confusing codebase
    * too **abstracted** (each component is an abstraction)

Generally, we need to find the **right balance** between too specific and too broad.

**4 criteria** on splitting a UI into components:

    #. Logical separation of content/layout (single responsibility)
    #. Reusability: make them reusable, if possible
    #. Responsibilities / complexity ???
    #. Personal preference

Framework: When to create a new component?
------------------------------------------
If answering any of the below questions with yes, you might need a new component.

.. hint::

    When in doubt, start with a relatively big component, then split it into smaller
    components as it becomes necessary.

    When already sure, it will be reused, put that reused part into its own component.

#. Logical separation of content/layout (single responsibility)

    * Does the component contain pieces of content or layout that don't belong together?

#. #. Reusability: make them reusable, if possible

    * Is it possible to reuse part of the component?
    * Do you want or need to reuse it?

#. Responsibilities / complexity

    * Is the component doing too many different things?
    * Does the component rely on too many props
    * Does the component have too many pieces of state and/or effects?
    * Is the code, including JSX, too complex/confusing?

#. Personal preference

    * Do you prefer smaller functions/components?

.. hint::

    **General hints**

    * creating a new component **creates new abstraction**. More abstractions require
      more mental energy to switch back and forth between components. Try not to
      create new components too early.
    * name a component according to **what it does** or **what it displays**. Don't
      be afraid to use long component names
    * Never declare a new component **inside another component**!
    * **Co-locate related components inside the same file**. Don't separate components
      into different files too early.
    * It's normal that an application has components of **many different sizes**,
      including very small and huge ones:

        * some very small components are necessary
        * most apps will have a few huge components (not meant to be reused)