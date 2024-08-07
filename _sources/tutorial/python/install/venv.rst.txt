Using virtual environments
==========================
The Python Standard Library contains the module `venv`_, which creates virtual environments.
It uses the Python interpreter, whose *venv* module is called.

In comparison to the third-party library `virtualenv`_, the virtual environment is not
completely independent from its base interpreter. That means, the environment becomes
unusable, if the base interpreter is uninstalled, but also that the virtual environment
is updated to later versions, if the base interpreter is (for example, 3.9.2 -> 3.9.3).

Some commands below expect that your virtual environments are located in
``%USERPROFILE%/.venv`` (Windows) and ``$HOME/.venv`` (Linux / macOS). You may choose
any other directory, but make sure to adapt the commands.

Create a virtual environment
----------------------------

.. code-block:: bash

    $ python -m venv </path/to/target/env>

.. hint::

    On Windows, it has been observed, that if the interpreter is **not** referenced by
    ``python`` but something like ``python3.9``, the command fails. In that case,
    use the absolute path to your interpreter, for example:

    .. code-block:: bash batch

        C:\> C:\Users\my_username\AppData\Local\Programs\Python\Python39\python.exe -m venv </path/to/target/env>

You may choose something like ``~/.venv/my_project_venv``
(Windows: ``%USERPROFILE%\.venv\my_project_env``) as target path.

Activate the virtual environment
--------------------------------
**On Linux / macOS:**

.. code-block:: bash

    $ source </path/to/target/env>/bin/activate

**On Windows:**

.. code-block:: bash

    C:\> </path/to/target/env>/Scripts/activate.bat

Add activation script to your project
-------------------------------------
To easily activate the associated environment from inside a project, create a file called ``activate``
(Windows: ``activate.bat``) in your project's root directory.

**On Linux / macOS:**

.. code-block:: bash

    $ cd /my/project/root
    $ touch activate
    $ chmod a+x activate

Next, open the ``activate`` script and add the following content, then save exit:

.. code-block:: bash

    #!/usr/bin/env bash

    source ~/.venv/<ENV_NAME>/bin/activate

Make the script executable via ``chmod u+x activate``. To call the script, run:

.. code-block:: bash

    $ source activate

    # or alternatively
    $ . activate

.. hint::

    Starting the script without ``source`` will execute the command in a sub-shell, in which
    case the environment is activate only for the sub-shell, which is closed, once the script
    finished.

**On Windows:**

Create the file ``activate.bat`` inside the project's root directory. Open it and
add the following content:

.. code-block:: batch

    @echo off

    call %USERPROFILE%\.venv\<ENV_NAME>\Scripts\activate

Windows: Activate your environments from anywhere
-------------------------------------------------
It may be useful to activate an environment from anywhere and also
to get an overview over your virtual environments.

**On Windows:**

Save the following content into a file called ``activate.bat``.
The file must be saved in a directory, which is listed the **PATH** environmental
variable (for example, create a directory ``C:\bin``):

.. code-block:: batch

    @echo off

    set ENV=%1
    set AVAILABLE_ENV=dir %USERPROFILE%\.venv /A:D /B

    if [%ENV%]==[] (
        echo:
        echo Missing environment name.
        echo:
        echo Usage: activate ^<ENV_NAME^>
        GOTO INVALID_INPUT
    )

    %AVAILABLE_ENV%|find "%ENV%" > nul

    if errorlevel 1 (
        echo:
        echo Environment '%ENV%' was not found.
        GOTO INVALID_INPUT
    ) else (
        %USERPROFILE%\.venv\%ENV%\Scripts\activate.bat
        GOTO EOF
    )

    :INVALID_INPUT
    echo:
    echo Possible selections
    echo -------------------
    %AVAILABLE_ENV%

    :EOF
    exit /b 0

.. hint::

    The script expects all virtual environments to be available in
    ``C:\Users\<YOUR_USERNAME>\.venv``. If not, adapt the script accordingly.

To run the script, run ``activate <ENV_NAME>`` from anywhere. To see
all available environments only run ``activate``.

.. _venv: https://docs.python.org/3/library/venv.html
.. _virtualenv: https://virtualenv.pypa.io/en/latest/