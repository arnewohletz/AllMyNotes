.. role:: rfg

05 - Docker Workshop
====================
Creating a dockerfile
---------------------
#. Adding python

    .. raw:: html

        <div class="highlight">
        <pre>
        <span style="color:red;">FROM</span> python:3.7-alpine
        </pre>
        </div>

    Different Linux distributions (here for Python images):

        * Stretch (Debian distribution Version 9.8)
        * Slim-Stretched (based on Debian:Stretch, uses a light desktop environment
          -> suitable when remote access is not required)
        * Alpine (smallest space amount needed -> therefor especially used in containers)
        * Windows Server Core -> WON'T COVER
        * OnBuild -> WON'T COVER

    Python's dockerfile specifies the installation of an Operating System for the image to run on:

    .. code-block:: none

        FROM alpine:3.9

    Adding Alpine Linux in Version 3.9 (Alpine's dockerfile itself states 'FROM scratch', which
    means, that no OS is installed here)

#. Create a folder for the flask application (RUN executes any shell command)

    .. raw:: html

        <div class="highlight">
        <pre>
        <span style="color:red;">RUN</span> mkdir /app
        </pre>
        </div>

#. Specify a working directory (all commands from here use it as the relative root dir)

    .. raw:: html

        <div class="highlight">
        <pre>
        <span style="color:red;">WORKDIR</span> /app
        </pre>
        </div>

#. Copy files to application directory (COPY <src> <dest>)

    .. raw:: html

        <div class="highlight">
        <pre>
        <span style="color:red;">COPY</span> requirements.txt requirements.txt
        </pre>
        </div>

    or using the absolute path (not needed as working directory has been set before):


    .. code-block:: none

        COPY requirements.txt /app/requirements.txt

    You cannot copy any files or directories that are above the working directory.

#. Install Python packages from requirements.txt

    .. code-block:: none

        RUN pip install -r requirements.txt

    * packages installation should be done before the deployment of the app (next step) as
      when any change to the application code occurs, all packages will be installed again,
      even though there are no changes
    * this happens since all steps are repeated after the first step with a change is detected

#. Copy all application files to working directory (using relative '.')

    .. code-block:: none

        COPY . .

    When the source code has changed all steps after this step are executed -> that’s why the
    dependencies installation steps should be put before this one.

#. Add metadata to your docker image (optional, but useful)

    .. raw:: html

        <div class="highlight">
        <pre>
        <span style="color:red;">LABEL</span> maintainer="Arne Wohletz &lt;arnewohletz@gmx.de&gt;"
        </pre>
        </div>

    * You should try to keep the amount of layers in your docker images as low as possible
    * Each additional layer increases filesize and built time of your docker image
    * Each label creates a new layer, so it is wise to chain multiple labels together to form a single layer
    * The image (FROM) used in one image can be cached to be used in other images, e.g.


    .. code-block:: none

        FROM python:2.7-alpine

    can be used in multiple images without saving a copy for each image on the Docker Host system
    (decreases file size).

    Here, two metadata key-value pairs are added to the same label and layer:

    .. code-block:: none

        LABEL maintainer="Arne Wohletz <arnewohletz@gmx.de>" \
              version="1.0"

    Indentation isn't required, but looks better.

#. Define the application start command

    .. raw:: html

        <div class="highlight">
        <pre>
        <span style="color:red;">CMD</span> flask run --host=0.0.0.0 --port=5000
        </pre>
        </div>

    * The CMD command is run when the application is run (whereas the RUN command is run,
      when the application is built)
    * This command defines what it supposed to be executed, when the image is executed
    * The CMD command can be overridden from users via the command line (if they want to)
    * The CMD command should always be the last entry in the dockerfile

Building a docker image
-----------------------
After the dockerfile is complete, run this command from inside the projects working directory.

    .. raw:: html

        <div class="highlight">
        <pre>
        docker <span style="color:red;">image build -t</span> web1 .
        </pre>
        </div>

    -> builds the docker image with the tag ‘web1' of the current directory (‘.’)

    **-t** defines a tag name

    * The build process creates different layers for
    * Running the command again without any changes to the dockerfile lets the image build
      finish almost instantly

Inspect the docker image
------------------------

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">image inspect</span> web1
    </pre>
    </div>

see the output:

    * version is set to latest, since no version was supplied during build
    * Cmd shows the exact command being executed on the image
    * Created layers are displayed at the bottom

Specify a version

.. code-block:: none

    docker image build -t web1:1.0 .

List all docker image on the host system

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">image ls</span>
    </pre>
    </div>

Delete a docker image
---------------------
.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">image rm</span> web1:1.0
    </pre>
    </div>

Delete via image id

.. raw:: html

    <div class="highlight">
    <pre>
    docker image rm <span style="color:red;">-f</span> &lt;image_id&gt;
    </pre>
    </div>

You may only use the first few digits of the id to delete all tags referencing an image
with the same id (as done when adding additional tags to an existing image)

**-f** option enforces the removal

Push docker image to docker hub (and pull it again)
---------------------------------------------------
First you need to authenticate your Docker CLI to Docker Hub in order to push images to it

.. code-block:: none

    docker login

-> Enter your username and password

.. hint::

    This step does not required to be repeated as your authentication data is written to
    a config file located at ~/.docker/config.json (OSX, Linux) or
    %USERPROFILE%/.docker/config.json (Windows)

Tag your image with your Docker Hub username -> image copy with new name on host system
is created (uses same image id as original)

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">image tag</span> web1 &lt;dockerhub_username&gt;/web1:latest
    </pre>
    </div>

Push the image to docker hub

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">image push</span> web1 &lt;dockerhub_username&gt;/web1:latest
    </pre>
    </div>

You can find the image under your account / Repositories

When deleting the image from the host sytem (see last chapter), the image from the docker
hub repo can be pulled via

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">pull</span> web1 &lt;dockerhub_username&gt;/web1:latest
    </pre>
    </div>

Running docker containers
-------------------------
Get all currently running containers

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">container ls</span>
    </pre>
    </div>

Get all containers including stopped ones

.. raw:: html

    <div class="highlight">
    <pre>
    docker container ls <span style="color:red;">-a</span>
    </pre>
    </div>

Remove a (stopped) container

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">container rm</span> &lt;four_first_digits_of_container_id&gt;
    </pre>
    </div>

Start your app image inside a container (here: web1)

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">container run</span> -it -p 5000:5000 -e FLASK_APP=app.py web1
    </pre>
    </div>

**-it** sets the container up to be interactive:

    * allows for interrupting the app via ctrl+c
    * provide real-time input (e.g. navigating the filesystem)

**-p** specifies ports used by docker container an the application:
``-p <bind_port_of_docker_host>:<bind_port_of_docker_container>`` (here the application uses
5000 internally and is supposed to be accessible via 5000: CMD flask run --host=0.0.0.0 --port=5000)

**-e** sets an environmental variable. Flask expects the FLASK_APP variable being set to
the file that launches the flask server (so contains the flask app), which is in app.py

.. hint::

    Get overview of all containers (including stopped containers)

    .. code-block:: none

        docker container ls -a

Start it with a given name (instead of letting docker choose one) + remove it once it is
stopped (otherwise stopped containers will stay):

.. raw:: html

    <div class="highlight">
    <pre>
    docker container run -it <span style="color:red;">--rm --name</span> web1 -p 5000:5000 -e FLASK_APP=app.py web1
    </pre>
    </div>

**--rm** automatically removes container, after it is killed

**--name** adds a name to the container (if none is given, a random one is assigned to it
-> name must be unique)

Run a container in detached mode (in the background) -> the only output is the container id:

.. raw:: html

    <div class="highlight">
    <pre>
    docker container run -it --rm --name web1 -p 5000:5000 -e FLASK_APP=app.py <span style="color:red;">-d</span> web1
    </pre>
    </div>

**-d** launches app in detached mode, which means the container is run in the background

To check logs from running or closed containers run

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">container logs</span> &lt;container_name&gt;
    </pre>
    </div>

* Container name can be defined via **-d**)
* Prints out all log content

To print current logs to the command line type

.. raw:: html

    <div class="highlight">
    <pre>
    docker container logs <span style="color:red;">-f</span> &lt;container_name&gt;
    </pre>
    </div>

**-f** stands for foreground

Checking the current resource usage of running docker containers

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">container stats</span>
    </pre>
    </div>

showing disk usage, cpu usage, memory usage, network i/o

**Running multiple instances of the same container in parallel** requires

    * unique name
    * unused internal host port

so

.. code-block:: none

    docker container run -it --name othername -p 5000 -e FLASK_APP=app.py -d web1

-> leaving the first port out (host port) assigns a random port on the docker host

Automatically restart a docker container, if it crashed or docker daemon is restarted

.. raw:: html

    <div class="highlight">
    <pre>
    docker container run -it —name another name -p 5000 -e FLASK_APP=app.py -d <span style="color:red;">-—restart-on-failure</span> web1
    </pre>
    </div>

**--restart on-failure** enables the automatic restart of the container when it crashes
(cannot be combined with --rm). You can test it by running 'sudo service docker restart' on
Linux and see if the container is restarted once Docker is back. If stopped manually, it does
not restart.

Stop a running container (command takes a few seconds)

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">container stop</span> <container_name>
    </pre>
    </div>

Making Code Changes with Volumes
--------------------------------
Activate the debugger in flask

.. raw:: html

    <div class="highlight">
    <pre>
    docker container run -it --name withDebug -p 5000:5000 --rm -e FLASK_APP=app.py -e <span style="color:red;">FLASK_DEBUG=1</span> web1
    </pre>
    </div>

Make some changes in the code (app.py) -> restarting the container won't apply the code changes

**Manual approach**

    #. The manual approach is to rebuilt the image

        .. code-block:: none

            docker image build -t web1 .

    #. Starting the new container applies the code changes

**Approach with volumes**

Mounting the application code into the running container

Starting the container with the volume flag (-v)

.. raw:: html

    <div class="highlight">
    <pre>
    docker container run -it --name withDebug -p 5000:5000 --rm -e FLASK_APP=app.py -e FLASK_DEBUG=1 <span style="color:red;">-v $PWD:/app</span> web1
    </pre>
    </div>

| **-v** <source_dir>:<destination_dir>
| **$PWD** is a variable that stands for present working directory

-> Multiple volumes flags can be supplied

You can inspect the mounted volumes by running (providingthe container name)

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">container inspect</span> web1
    </pre>
    </div>

and checking the "Mounts” section content

.. important::

    * Changes applied within the mapped source directory are applied to the docker container's mounted copy
    * CAREFUL: Changes made to the container's mounted volume are also made to the source directory
    * Changes made outside a mapped directory are not applied to running containers (out of scope)

Debugging Tips and Tricks
-------------------------

.. hint::

    Problem

        Cannot interact with alpine filesystem of a running container using VirtualBox (Docker
        Toolbox, Windows issue only)

    Cause

        inotify (notifies OS about file system changes) does behave differently on alpine.
        It seems no problem when alpine is used on a Linux docker installation, though.

    Solution

        Change alpine to slim in your dockerfile: python3.7-alpine -> python3.7-slim-stretch

Connecting to a running container's file system

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">container exec</span> -it &lt;container_name&gt; <span style="color:red;">sh</span>
    </pre>
    </div>

| -> Opens up the containers shell (using 'bash’ or ‘sh’ when running other Linux distributions)
| -> Navigates to the specified working directory (WORKDIR) from the dockerfile

Command is useful to make sure, you are really running what you think you're running

Exit the exec session by hitting Ctrl+D

You can use any other command instead of 'sh' e.g. flask --version which prints the
flask version info to the local terminal window

.. important::

    All commands docker executes on the containers host OS are executed as root user.
    If new files are created by docker, they are owned by root (Linux only).

    To prevent this use the --user flag

    .. code-block:: none

        docker container exec -it --user "$(id -u):$(id -g)" web1 touch hi.txt

Linking Containers with Docker Networks
---------------------------------------
Install redis container

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">pull</span> redis:5.0-alpine
    </pre>
    </div>

* Docker containers can run on multiple networks
* Same as computers in general, docker containers must be on the same network
* If they are scattered across multiple networks, a bridge must be created between the
  various docker container networks

Docker creates several networks on it own. Check them out

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">network ls</span>
    </pre>
    </div>

* bridge: stands for the outside docker network (listed in your networks when running ifconfig)
* 'host' and 'none' are required by the docker daemon
* if no other network is specified for a container, the **bridge** is used as default

Inspect bridge network

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">network inspect</span> bridge
    </pre>
    </div>

-> "Containers" entry lists all running containers on that network

Running containers on the same network can talk to each other via their local IP addresses
(here web2 and redis are launched to the bridge network)

Check out a running containers IP address (here: redis)

.. code-block:: none

    docker exec redis ifconfig

Check their communication by piing the other container

.. code-block:: none

    docker exec web2 ping 172.17.0.2

Check the hosts mapping file -> other container is added with ip and its container ID

.. code-block:: none

    docker exec redis cat /etc/hosts

Creating a new network for Docker is useful, as it automatically the containers names to
its current IP addresses, even if those change, due to their unique ID (automatic DNS)

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">network create</span> --driver bridge &lt;some_network_name&gt;
    </pre>
    </div>

    -> When inspecting the new network, it is visible that it uses the 172.18.0.0 subnet whereas
    the bridge used the 172.17.0.0

Launch a container on a specified network (created a network named 'firstnetwork')

.. raw:: html

    <div class="highlight">
    <pre>
    docker container run -itd --name web2 -p 5000:5000 --rm -e FLASK_APP=app.py -e FLASK_DEBUG=1 <span style="color:red;">--net firstnetwork</span> -v $PWD:/app web1
    </pre>
    </div>

Now we can access each container on firstnetwork with their name (not their IP addresses anymore)

.. code-block:: none

    docker exec web2 ping redis

Persisting data to your docker host
-----------------------------------
* Restoring data after the container has been stopped
* For storing data of redis we will use a named volume (web2_redis:/data)
* Perfect for databases

Create a named volume

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">volume create</span> web2_redis
    </pre>
    </div>

    web2_redis is the volume name here

List all volumes of docker host

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">volume ls</span>
    </pre>
    </div>

more details

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">volume inspect</span> web2_redis
    </pre>
    </div>

    will show, where the volume will be mounted on the docker image

.. important::

    The mount point is not accessible on the local system (at least on OSX it is not)
    -> this is a design concept, the path is a place on the “remote” machine filesystem
    (from: https://github.com/docker/for-win/issues/6875)

Add the data volume to redis container when starting it

.. raw:: html

    <div class="highlight">
    <pre>
    docker container run -itd --name redis -p 6379:6379 --rm -e --net firstnetwork<span style="color:red;">-v web2_redis:/data</span> redis:5.0-alpine
    </pre>
    </div>

.. hint::

    Redis specific stuff: Save current data

    Since redis is a in-memory storage, it must be manually saved to the file system.

    .. code-block:: none

        docker exec redis redis-cli save

    This will create a dump.rdb file within the /data directory (on local redis container mount point)
    and on root dir of the redis container.

When stopping the container and restarting it, previous data is still there

This method is applicable for all kind of database -> you must merely find out, where
such data needs to be stored inside the container (/data for redis)

.. note::

    There should be no data stored inside the docker container once the application is
    running in production, since the application is supposed to be easily installable on
    various systems (portable)

Sharing Data between Containers
-------------------------------
* link data between containers without touching the docker host
* most popular use case is a web application using static assets (CSS, Javascript)
* Those static files are supposed to be shared via a webserver like nginx

New setting in the dockerfile

.. raw:: html

    <div class="highlight">
    <pre>
    <span style="color:red;">VOLUME</span> ["app/public"]
    </pre>
    </div>

* means, that the app/public folder is supposed to be exposed as a volume when containers
  is running
* multiple volume instructions are possible

Re-build the docker image (since dockerfile has changed) and start the container

Restart the redis container with referencing the new exposed volume of web2

.. raw:: html

    <div class="highlight">
    <pre>
    docker container run -itd --name redis -p 6379:6379 --rm -e --net firstnetwork -v web2_redis:/data <span style="color:red;">--volumes-from web2</span> redis:5.0-alpine
    </pre>
    </div>

-> volumes-from <container_name_that_has_the_volume_we_need>

Changes to the shared volumes are immediately visible to the other containers that added it (and vice versa)

In order to share directories, those must reside on the same docker host system

.. important::

    **Not recommended method**

    Volumes can be shared without editing the docker file:

        * add a -v flag to the container that shares a directory (e.g. -v /app/public)
        * execute redis as above

     -> the shared volumes must be specified in the command, not the dockerfile

Optimizing your Docker images (decrease your docker images size)
----------------------------------------------------------------
Use a *.dockerignore* file to reduce image size and not publish secure files:

    * during container creation docker will evaluate the file when COPY or ADD commands
      are executed
    * WORKDIR is the default start path for all ignore paths

.. code-block:: none

    .dockerignore #ignore the file itself
    .git/ #ignore a directory
    .foo/\* #ignore all files within a directory (but not the dir itself)
    \**/*.txt #ignore all files with txt extension
    !special.txt #make exception to above rule for special.txt file

-> Check out the updated dockerfile run script in the repository

Make .dockerignore a whitelist (instead of a blacklist)

.. code-block:: none

    *
    !keepthisfile.txt

Running scripts when a container starts
---------------------------------------
* Usage: Same docker images is supposed to be used for several projects, but each
  project has a slightly different setup routine
* Usually separate dockerfiles are needed in which most commands will be the same for
  each application
* It technically works, but all these files need to be maintained if the image changes

**Scenario:** Adding a database to all these projects (e.g. PostgreSQL), setting a own user
login and table name for each project's dockerfile -> very tedious

| -> Postgres is able to setup a table with username and password via a shell command (if
     not existing already)
| -> This script can be referenced as an entry point for each project's dockerfile

#. Add the entry point script to your dockerfile (located in root dir, not working dir):

    .. code-block:: none

        COPY docker-entrypoint.sh /

#. Make entrypoint script executable

    .. code-block:: none

        RUN chmod +x /docker-entrypoint.sh

#. Add entrypoint pointing to the copied script

    .. raw:: html

        <div class="highlight">
        <pre>
        <span style="color:red;">ENTRYPOINT</span> ["/docker-entrypoint.sh"]
        </pre>
        </div>

| Rebuild the application docker image
| Restart the redis container and the start the new application container

The used shell script:

    * within your entrypoint script, you can print terminal message by using **echo** (shell) e.g.

    .. code-block:: none

        echo "The Dockerfile ENTRYPOINT has been executed!"

    * an environmental variable is set (with a default value)

    .. code-block:: none

        export WEB2_COUNTER_MSG="${WEB2_COUNTER_MSG:-some default value if not specified}

    * ${WEB2_COUNTER_MSG} is a shell variable, which can be overridden by passing it into
      the docker command using the -e flag


.. hint::

    Python is able to access environmental variables by using:

    .. code-block:: none

        os.getenv(<env_var_name>) e.g os.getenv('WEB2_COUNTER_MSG, '')

**Explaining exec "$@"**

    * Dockerfile's CMD instruction passes whatever comes after to a default entry point
      (if none is defined)
    * This default entry point is "/bin/sh -c" (run whatever I pass as a command (-c) in /bin/sh)
    * Since our entrypoint now overrides this default, the "CMD flask --host ..." command actually does this

    .. raw:: html

        <div class="highlight">
        <pre>
        bin/sh -c "<span style="color:red;">$</span> && flask --host=0.0.0.0 --port=5000"
        </pre>
        </div>

    where **$** stands for our docker-entrypoint.sh content

    * the last command

    .. code-block:: none

        exec "$@"

    then does take every command given by you on the command line (e.g. docker container run ...)
    and executes it ($@ stands for all command-line arguments)

    -> basically continues the docker command

    -> The ENTRYPOINT defines what to run when using CMD in a dockerfile

    Used for

        * database migration
        * nginx config modification

Cleaning up after yourself
--------------------------
**Get info**

Check out all containers (running and stopped)

.. code-block:: none

    docker container ls -a

Check docker's currently used disk space

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">system df</span>
    </pre>
    </div>

Check docker images

.. code-block:: none

    docker image ls

    * images with name <none> are not used by anything -> they're dangling
    * these may be failed builds or builds that were replaced by a new image using the
      same tag (or both using the 'latest' tag)
    * dangling images are declared as reclaimable

Get containers and images spaces usage together (verbose output)

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">system df -v</span>
    </pre>
    </div>

Get system info

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">system info</span>
    </pre>
    </div>

(also verifies that docker daemon runs well)

**Cleaning up**

Remove all stopped containers, unused volumes and networks and all dangling images

.. raw:: html

    <div class="highlight">
    <pre>
    docker <span style="color:red;">system prune</span>
    </pre>
    </div>

| **-f** ... force deleting (no confirmation needed)
| **-a** ... removes all unused images (not associated to a container) -> use with
  care, images associated with stopped containers are deleted (images must be rebuild
  to retrieve them)

Stop multiple containers

.. code-block:: none

    docker container stop <containerA_name> <containerB_name> ...

Stop all running containers (at least one must be running, otherwise reports error)

.. code-block:: none

    docker container stop $(container ls -a -q)

**-q** means quiet mode, and outputs the container id as string

Removing multiple images

.. code-block:: none

    docker image rm <imageA_name> <imageB_name>:<tag_name> ...
