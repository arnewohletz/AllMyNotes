Moving components into separate files
=====================================
Usually, each component should be put into a separate file.

#. Each component must be exported, commonly a *default* export. For example:

    .. code-block:: jsx

        export default function Logo() {
          return <h1>Far Away</h1>;
        }

#. Each component, which uses that separate component needs to import it. When
   using a default export, the component can be imported by any name, but it is
   recommended to use the exact component name. For example:

    .. code-block:: jsx

        import Logo from "./Logo.js";

.. hint::

    In VS Code, this process can also be done by selecting a component, then right-click
    and select :menuselection:`Refactor --> Move to new file`, which automatically
    creates a new file in the same directory with the name of the component.

.. hint::

    All components could also be put into a separate directory, e.g. ``src/components``.