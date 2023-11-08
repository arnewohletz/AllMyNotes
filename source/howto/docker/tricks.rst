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