Troubleshooting
===============

exec
----

:Problem:

    In a *Jenkinsfile*, when running a ``docker exec -it`` command, it returns
    the following error and fails:

    .. code-block:: none

        the input device is not a TTY

:Cause:

    A Jenkinsfile is run in a context which does not provide a TTY, which allows
    for immediate output from the shell to allow user interaction. By default,
    Jenkins uses non-TTY shells for the execution of Jenkinsfiles, in which case
    commands, which require and interactive shell (such as ``docker exec -it``),
    fail.

:Solution:

    Make the ``docker exec`` command non-interactive by removing the ``-it`` options:

        .. prompt:: bash

            docker exec CONTAINER_NAME COMMAND [ARGUMENTS...]
