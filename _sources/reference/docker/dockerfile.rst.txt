Dockerfile
----------
Example Dockerfile (contains various incoherent statements only, cannot be run):

.. literalinclude:: _file/Dockerfile_example
    :linenos:

:line 1:

    `Parser directive`_ for `Dockerfile frontend`_. This must be defined on top of
    the Dockerfile, because after the first *comment*, *empty line* or *builder instruction*
    has been processed, any following *parser directives* are treated as regular comments.

    The *Dockerfile frontend* entry allows to dynamically load a custom Dockerfile syntax,
    whereas ``syntax=docker/dockerfile:1`` points to the latest stable version 1 syntax.

:line 3:

    The ``ARG <NAME>`` instructions defines a variable that the user pass in at build-time.
    For example:

    .. code-block:: bash

        $ docker build --build-arg NVIDIA_TRITON_IMAGE_FQN="some_value"

:line 6:

    The ``ARG <NAME>=<VALUE>`` instruction defines a variable with a default value,
    so it is not mandatory to pass it in at build-time.

:line 7:

    The ``ARG <NAME>=${<VARIABLE>:-<DEFAULT>}`` instruction defines a variable <NAME>
    to the value of the variable <VARIABLE>. In case, <VARIABLE> is not passed in,
    the value assigned to <NAME> will be <DEFAULT>.

:line 9:

    From here onwards, all commands will be executed as user *root*.

:line 11 - 15:

    This section defines a `Here-Document`_, which allows any lines after the
    opening (line 11) until the closing (line 15) to be part of the same command.
    This allows for multi-line scripts without chaining these lines together with
    ``&& \`` statements at the end of each of those lines.
    The delimiter (here: ``EOF``) can be any single word string.

    This were the substitute without the *here-document*:

    .. code-block:: bash

        RUN apt-get update && \
            apt-get install -y --no-install-recommends gnupg2 curl ca-certificates

:line 18:

    Copies a local file into the built Docker image using the ``--chown`` option to
    define the ownership of the copied file.

:line 20:

    Set an `environment variable`_, here append ``:/usr/local/cuda-10.2/lib64`` to the
    predefined environment variable ``LD_LIBRARY_PATH`` (the variable contains directories,
    which contain shared libraries, to be searched before using the default directories)

.. _Parser directive: https://docs.docker.com/reference/dockerfile/#parser-directives
.. _Dockerfile frontend: https://docs.docker.com/build/dockerfile/frontend/#dockerfile-frontend
.. _Here-Document: https://docs.docker.com/reference/dockerfile/#here-documents
.. _environment variable: https://docs.docker.com/reference/dockerfile/#env