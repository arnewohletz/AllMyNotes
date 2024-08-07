Commands
========
A full reference can be viewed at https://docs.docker.com/reference/cli/docker/

Images
------
List all available image tags

.. code-block:: bash

    $ docker images

Logs
----
Display log messages (follow latest):

.. code-block:: bash

    $ docker logs --follow <CONTAINER_NAME>

Follow incoming log messages (but don't show previous):

.. code-block:: bash

    $ docker logs --tail=0 --follow <CONTAINER_NAME>

Save all previous logs to file (no file `logging driver`_ configured,
container must still run):

.. code-block:: bash

    $ docker logs <CONTAINER_NAME> 2> file.log

.. important::

    The command does not catch logs arriving after executing the command.

Log saving location
```````````````````
(default logging driver is JSON)

* Docker: ``/var/lib/docker/containers/<container_id>/<CONTAINER_ID>-json.log``
* Rootless Docker: ``~/.local/share/docker/containers/<CONTAINER_ID>/<CONTAINER_ID>-json.log``

The beginning of the container ID can be retrieved via ``docker container ls``.

You may also retrieve the filepath by running:

.. code-block:: bash

    $ docker inspect <CONTAINER_NAME> | jq -r .[].LogPath

.. _logging driver: https://docs.docker.com/config/containers/logging/configure/