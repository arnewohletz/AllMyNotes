Run Python scripts from anywhere
--------------------------------
Python scripts (single \*.py file programs) are especially handy, when those can
be executed

* from any current directory
* without prior activating any virtual environment

but simply like in this example:

.. prompt:: bash

    my_little_script.py

.. important::

    These steps only work on macOS and Linux.

These steps require to have :ref:`pyenv <install_pyenv>` (including pyenv-virtualenv)
installed on your system.

#. Create a directory, where you like to save your scripts (e.g. ``~/python_scripts``).
#. `Add this directory to your PATH variable <https://linuxways.net/centos/source-command-in-linux/>`__
   (add it to your shell's profile, e.g. ``~/.profile`` for *bash* or ``~/.zprofile`` for *zsh*), e.g.:

    .. code-block:: shell

        # Setting PATH to Python scripts directory
        export PATH="/your/scripts/directory:$PATH"

#. Open new Terminal window or `source <https://linuxways.net/centos/source-command-in-linux/>`__ your
   shell initialization script. Example:

        .. prompt:: bash

            source ~/.zprofile
#. Create a virtual environment using pyenv for your scripts:

    .. prompt:: bash

        pyenv virtualenv <PYTHON_VERSION> <VENV_NAME>

#. Select your virtual environment as interpreter for the scripts directory:

    .. prompt:: bash

        cd /your/scripts/directory
        pyenv local <VENV_NAME>

#. Create a new script file or copy your existing script(s) into your new scripts directory.
#. Add this content on the very top of any script file in your scripts directory
   (replace existing shebang line, if applicable):

    .. code-block:: python

        #!/bin/zsh
        "true" '''\'
        pushd $(dirname "${0}") > /dev/null
        "exec" "pyenv" "exec" "python" "$0" "$@"
        '''

    .. hint::

        Depending on your operating system, you may have to alter the shell path (line 1)
        (e.g. ``/usr/bin/bash``). Check your default shell by opening your Terminal
        and execute:

        .. prompt:: bash

            echo $SHELL

You should now be able to execute any \*.py script file within your scripts directory
from anywhere in the shell, without the need to activate the script's virtual environment
first.
