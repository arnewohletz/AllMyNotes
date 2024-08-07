03 - Installing Docker
======================

Docker editions
---------------
#. Docker Community Editions (CE)

    * free and open source
    * aimed at developers and do-it-yourself operating teams to docker-ize their applications

#. Docker Enterprise Editions (EE)

    * suited for running mission critical applications
    * costs: 750 to 2000 $ per year
    * Some extras:

        - certified images and plugins
        - Docker DataCenter
        - vulnerability scans
        - official support

    * Release cycles

        - Edge: new version each months, trying out new features, patches for one month
        - Stable: every 3 months, get patches for 4 months
        - Enterprise Edition: every 3 months, get patches for 1 year

Option 1: Installing Docker Toolbox (OSX and Windows)
-----------------------------------------------------
* Designed to run Docker on OSX and Windows
* Installs these tools:

    - Docker CE/EE (includes daemon and CLI)
    - Docker Compose
    - Docker Machine

* creates a VM (using VirtualBox) with a lightweight Linux and installs the Docker server on it
* can also create Docker servers on Cloud Hosting providers
* VirtualBox
* Supply VM to run Docker
* Docker QuickStart Terminal
* Also able to create a docker server
* Kitematic
* Graphical tool to manage docker images and containers
* Optional (CLI already covers all functionality)

Option 2: Installing Docker for Mac / Windows
---------------------------------------------
* No VirtualBox required, since it uses HyperKit (OSX) or Hyper-V (Windows), which are built
  in already
* Install these tools:

    - Docker CE/EE
    - Docker Compose
    - Docker Machine

Which one to install?
---------------------
* Docker Toolbox (use it only if Docker for Mac / Windows gives you performance issues)

    - need a type 2 hypervisor: Hyper-V or HyperKit cannot be used
    - requires Mountain Lion 10.8+ or Windows 7+ (Home is OK)
    - docker daemon is running on a remote host (not localhost, e.g. 192.168.99.100)
    - docker QuickStart Terminal required to run docker commands

* Docker for Mac / Win (rather use this, unless running into performance issues)

    - need a type 1 hypervisor: VirtualBox or VMWare cannot be installed on the system
      (at least on Windows)
    - Requires Yosemite 10.10.3+ or Windows 10 (Pro, Ent, Stu, but not Home)
    - docker daemon runs on localhost (as if run natively)
    - any terminal works for running docker commands

    | https://docs.docker.com/desktop/install/mac-install/
    | https://docs.docker.com/desktop/install/windows-install/

    Maybe follow this for OSX:
    https://pilsniak.com/how-to-install-docker-on-mac-os-using-brew/

Check installation
------------------
Check docker

.. code-block:: bash

    $ sudo docker info

which should return docker system info

Check compose

.. code-block:: bash

    $ sudo docker-compose --version
