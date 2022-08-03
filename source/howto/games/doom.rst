Play multiplayer Doom on macOS
------------------------------
`Doom`_ and other games running on the Doom engine can be run on macOS using one
of the various source ports like `gzdoom`_. Some of these ports also support
multiplayer and are available on macOS. For online multiplayer you will also need
a server browser to find and join Doom sessions. This How-To shows how to install
and set up such an environment using the source port `Zandronum`_ and the server
browser `Doomseeker`_, which also comes packed with `Wadseeker`_, a tool which
auto-downloads missing resources required to join a particular session.

Installation
````````````
#. Install Zandronum via Homebrew:

    .. prompt:: bash

        brew install zandronum

#. Create a new directory ``~/Library/Application Support/zandronum`` and put in your
   ``doom.wad`` and ``doom2.wad`` file (from an existing Doom or Doom2 installation).
#. Try launching Zandronum selecting either of the WAD files.
#. Go to https://doomseeker.drdteam.org/download.php#.
#. Select the *Operating System* :guilabel:`Other (Source Code)` and click on the
   download link under *Doomseeker Source* (not the Bitbucket Snapshot). Extract the
   archive at a suitable location (e.g. ``~/Downloads/``)

    .. important::

        There is a binary download for macOS available, though that installation
        cannot be started due to a `signature error`_, which occurs on any macOS version
        10.14 (Mojave) or newer, preventing libraries to be loaded due to fails in
        verifying the application's signature. The current way of overcoming this
        issue is to build the binaries locally.

#. Install the required dependencies to build Doomseeker (Qt5 and CMake):

    .. prompt:: bash

        brew install cmake qt5

#. Set the variable Qt5_DIR in order for CMake to find your Qt5 installation:

    .. prompt:: bash

        export Qt5_DIR="/usr/local/opt/qt@5/"

#. Enter the extracted *doomseeker* directory and execute the build:

    .. prompt:: bash

        mkdir build
        cd build
        cmake ..
        make
        sudo make install

#. After the installation finished you may copy the ``build`` directory to a
   more suitable location (you may also want to rename it to ``doomseeker`` or
   something like that).
#. Create a link to your ``doomseeker`` executable:

    .. prompt:: bash

        ln -s /path/to/my/doomseeker/dir/doomseeker /usr/local/bin/doomseeker

#. Launch Doomseeker via:

    .. prompt:: bash

        doomseeker

.. hint::

    Auto-downloaded resources (usually in \*.ipk3 format) are copied to
    ``~/Library/Preferences/doomseeker/`` by default. You may change that
    under :menuselection:`Settings --> File paths`.

.. _Doom: https://www.pcgamingwiki.com/wiki/Doom_(1993)
.. _gzdoom: https://zdoom.org/downloads
.. _Zandronum: https://zandronum.com/
.. _Doomseeker: https://doomseeker.drdteam.org/
.. _Wadseeker: https://doomseeker.drdteam.org/wadseeker.php
.. _signature error: https://zandronum.com/tracker/view.php?id=4018

Set up a multiplayer game
`````````````````````````
coming later

GZDoom: Create and join a multiplayer game :footcite:p:`gzdoom_multiplayer`
```````````````````````````````````````````````````````````````````````````
GZDoom also features multiplayer capabilities, but is limited to certain game modes,
which is Deathmatch, Team Deathmatch and Cooperative. On the other hand, there are
some Doom mods, which are specifically built with the GZDoom engine (e.g. `Blade of Agony`_)
and fail to load using a different Source Port such as Zandronum.

To **create** aka host a multiplayer game using GZDoom, you need to launch it via the command
line using specific options, which are

.. option:: -host <min_players>

    ``<min_players>`` the minimum amount of participants (including the host) before the
    game is started

.. option:: -useip <IP_ADDRESS>

    This defines the IP address, which other players can connect to in order to join the
    game session. For LAN matches, use your local IP address (e.g. 192.168.178.50) and for
    Internet games, specify your global IP address (e.g. determine it on https://www.ipchicken.com/).

    .. important::

        For internet games, you may have to enable port forwarding for your machine in your
        router configuration. GZDoom uses port 5029 as default (you may define a different
        port via the :option:`-port` option) for which it needs forwarding on **UDP**
        traffic. For security reasons, you should disable the forward again after the game session.

.. option:: -netmode <num>

    Defines the network mode: ``0`` for *Peer-to-Peer*, which is recommended when having
    a slower internet connection or when only two people are playing, and ``1`` which should
    only be used when having a faster internet connection (10 Gb/s or more) or when
    creating a game with three or more people (people other than the host may leave the
    session without aborting it). Find more info `here <network_modes>`_.

A basic host command might be:

.. prompt:: bash

    gzdoom -host 2 -useip 192.168.178.50 -netmode 0

Additional options may be:

.. option:: -deathmatch

    Defines that this game session is of type **Deathmatch**. If this option is not passed, the game mode
    will be *Cooperative*.

.. option:: -warp <m>

    Directly launch a specific map. Depending on the launched game the style is ``ExMx``
    (e.g. E1M1 for first map of episode 1) or simply ``xx`` (e.g. 24 for map 24). See more
    at https://zdoom.org/wiki/Command_line_parameters#Multiplayer_options. Alternatively,
    you may use the :option:`+map` option.

Documentation on all multiplayer command line options: https://zdoom.org/wiki/Command_line_parameters#Multiplayer_options

To **join** a running multiplayer game, simply launch GZDoom also over the command line, stating
the IP address (and port, if it differs from the default), either the local IP address when
you are in the same LAN or the global IP address for internet connection:

.. prompt::

    gzdoom -join <HOST_IP_ADDRESS>

.. important::

    For both creating and joining a multiplayer game, the used WAD and IPK3 files must be
    specified in addition to the network option via :option:`-file` (for \*.ipk3 files) and
    :option:`-iwad` (for \*.wad files).

.. _Blade of Agony: https://boa.realm667.com/
.. _network_modes: https://zdoom.org/wiki/Multiplayer#Network_modes

.. footbibliography::