Pyreverse
=========
Pyreverse is a module inside `Pylint`_, which generates UML diagrams out of Python code.

Create a PlantUML class diagram
-------------------------------
.. code-block:: bash

    $ pyreverse -o plantuml --module-names yes -s 1 -d my/output/dir \
    path/to/module_A.py path/to/module_B.py ... && \
    sed -i "" "s/set namespaceSeparator none/set namespaceSeparator ./g" my/output/dir/classes.plantuml

``-o plantuml``
    Generate the UML diagram in PlantUML format (\*.plantuml)

``--module-names yes``
    Embed classes inside the module, they are located in

``-s 1``
    Show associations up to level 1 (direct associations)

``-d my/output/dir``
    The output path for the diagram files

``sed -i "" "s/set namespaceSeparator none/set namespaceSeparator ./g" my/output/dir/classes.plantuml``
    Replace te namespace separator from ``none`` to ``.``, which effectively
    uses the modules as namespaces, which puts classes of the same module
    inside a frame

.. _Pylint: https://www.pylint.org
