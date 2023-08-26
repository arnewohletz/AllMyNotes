Conda commands
==============
Create new environment
----------------------
.. prompt:: bash

    conda create -n <ENV_NAME>

Install Python interpreter into environment
-------------------------------------------
.. prompt:: bash, (conda_env)

    conda install python=<X.X.X>

where ``<X.X.X>`` defines a valid Python version (for example 3.9.3).

Clone an existing environment
-----------------------------
.. prompt:: bash

    conda create -n <NEW_ENV_NAME> --clone <EXISTING_ENV_NAME>

Rename a environment
--------------------
.. prompt:: bash

    conda rename -n <CURRENT_NAME> <NEW_NAME>
