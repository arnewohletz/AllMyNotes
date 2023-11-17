conda
=====

Manage environments
-------------------
Create new environment
''''''''''''''''''''''
.. prompt:: bash

    conda create -n <ENV_NAME>

Clone an existing environment
'''''''''''''''''''''''''''''
.. prompt:: bash

    conda create -n <NEW_ENV_NAME> --clone <EXISTING_ENV_NAME>

Rename an environment
'''''''''''''''''''''
.. prompt:: bash

    conda rename -n <CURRENT_NAME> <NEW_NAME>

Remove an environment
'''''''''''''''''''''
.. prompt:: bash

    conda env remove -n <ENV_NAME>

Packages
--------
Install Python interpreter into environment
'''''''''''''''''''''''''''''''''''''''''''
.. prompt:: bash, (conda_env)

    conda install python=<X.X.X>

where ``<X.X.X>`` defines a valid Python version (for example 3.9.3).

List all available versions for package
'''''''''''''''''''''''''''''''''''''''
.. prompt:: bash

    conda search <package_name>

If the name is not entirely known, use wildcard characters:

.. prompt:: bash

    conda search '*<partial_package_name>*'
