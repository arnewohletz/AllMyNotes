conda
=====

Manage environments
-------------------
Create new environment
''''''''''''''''''''''
.. code-block:: bash

    $ conda create -n <ENV_NAME>

Clone an existing environment
'''''''''''''''''''''''''''''
.. code-block:: bash

    $ conda create -n <NEW_ENV_NAME> --clone <EXISTING_ENV_NAME>

Rename an environment
'''''''''''''''''''''
.. code-block:: bash

    $ conda rename -n <CURRENT_NAME> <NEW_NAME>

Remove an environment
'''''''''''''''''''''
.. code-block:: bash

    $ conda env remove -n <ENV_NAME>

Packages
--------
Install Python interpreter into environment
'''''''''''''''''''''''''''''''''''''''''''
.. code-block:: bash

    (conda_env) $ conda install python=<X.X.X>

where ``<X.X.X>`` defines a valid Python version (for example 3.9.3).

List all available versions for package
'''''''''''''''''''''''''''''''''''''''
.. code-block:: bash

    $ conda search <package_name>

If the name is not entirely known, use wildcard characters:

.. code-block:: bash

    $ conda search '*<partial_package_name>*'
