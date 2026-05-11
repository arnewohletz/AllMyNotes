Component Lifecycle
===================
A component lifecycle only applied to **component instances**, not the component
itself. But most of time, when saying component, it is referred to a component
instance.

Phases of a component instance:

#. Mount / Initial Render
#. Re-Render
#. Unmount

.. figure:: _file/component_lifecycle.jpg

    Component instance lifecycle

.. important::

    We can define code to run at a specific phase / point in time.
