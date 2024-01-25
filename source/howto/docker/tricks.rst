Docker Cheatsheet
=================
Images
------

Inspect image content (with or without starting container)
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#. If no container of the image exists (running or stopped), create it from the image
   (here: *my_image*). It won't be started. Run:

    .. prompt:: bash

        docker create --name my_container my_image

    .. hint::

        You may also reference the image ID, instead of the name.

#. Export the container contents into a tar archive:

    .. prompt:: bash

        docker export my_container > my_container.tar

    .. hint::

        This also works for running or stopped containers.

#. Extract the image archive:

    .. prompt:: bash

        mkdir my_container
        tar -xf my_container.tar -C ./my_container

You may now inspect all the content inside the ``./my_container`` directory.

exec
----
Make ``docker exec`` return same exit code as executed command
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
:Problem:

    When a command, being executed on a running container, returns a exit code
    other than zero (0), the ``docker exec`` command itself still returns the
    exit code 0.

:Cause:

    The ``docker exec`` command ran successfully, as the container was reachable
    and the command could be triggered. When running``docker exec`` like this:

    .. prompt:: bash

        docker exec -it CONTAINER_NAME COMMAND [ARGUMENTS...]
        # for example
        docker exec -it some_container ls -l /not/here
        # output:
        # ls: cannot access '/not/here': No such file or directory
        echo $?
        # 0 -> shows exit code 0 (OK)

:Solution:

    The command itself must call another ``bash`` instance to execute the command.
    If that instance returns a non-zero exit code, the ``docker exec`` command
    will also return a non-zero exit code:

    .. prompt:: bash

        docker exec -it CONTAINER_NAME /bin/bash -c 'COMMAND [ARGUMENTS...]'
        # for example
        docker exec -it some_container /bin/bash 'ls -l /not/here'
        # output:
        # ls: cannot access '/not/here': No such file or directory
        echo $?
        # 2 -> shows exit code 2 (NOK)

    .. attention::

        The command argument for the ``-c`` option must be put in single quotes,
        not double quotes.

    .. hint::

        You may need to replace ``/bin/bash`` by another shell executable, like
        ``sh``, ``/bin/sh`` or ``/bin/zsh`` - whatever shell is available on
        the Docker container. Make sure, that shell supports the ``-c`` option.
