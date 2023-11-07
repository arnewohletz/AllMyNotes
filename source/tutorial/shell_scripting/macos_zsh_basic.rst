macOS: zsh and launchd
======================
As of version 10.15 (Catalina) macOS changed the default shell to zsh_ (Z Shell), prior
using bash_ (Bourne again Shell). While *bash* is still available in macOS as of now, it
is recommended to zsh, including for shell scripts.

.. _zsh: https://www.zsh.org/
.. _bash: https://www.gnu.org/software/bash/

A basic shell script
--------------------
Shell scripts use the \*.sh suffix. In order to execute shell scripts directly, like

.. prompt:: bash

    my_first_script.sh

instead of requiring to pass it as an argument to a shell call like

.. prompt:: bash

    zsh ./my_first_script.sh

a so called shebang_ line is required in your script as the first line. This declares
which type of shell is used when the script is called directly. It is recommended to
use this shebang line on macOS:

.. code-block:: shell
    :linenos:

    #!/usr/bin/env zsh -l

.. hint::

    The ``env`` tool acts as a pointer towards the shell binary file.
    Using it makes the script less system dependent. Passing in the ``zsh`` argument
    defines, that we want the path to the zsh shell (here ``/bin/zsh``).

    The ``-l`` option defines, that we want a shell with the current user being logged
    into it. This executes the user specific profile files like ``/etc/zprofile`` or
    ``~/.zshrc`` (`more info`_), which feed to the PATH variable, which otherwise contains
    no paths to user-specific executable directories, such as ``/usr/local/bin``. In the
    shell script this enables us to use commands directly, without having to use their
    absolute paths:

    .. code-block:: shell

        # use binary commands directly
        match=$(pcregrep -o1 $update_version_regex $tmp_file)
        say "This worked just fine"

        # instead of requiring its absolute path
        match=$(/usr/local/bin/pcregrep -o1 $update_version_regex $tmp_file)
        /usr/bin/say "This worked as well, but is longer and system dependent"

    macOS uses a tool called *path_helper* to feed some entries to the PATH variable.
    It is called from ``/etc/zprofile`` by default.

Next up you may define your shell script. Here are some useful resources:

* https://scriptingosx.com/
* https://www.gnu.org/software/bash/manual/bash.html
* https://zsh.sourceforge.io/Doc/Release/zsh_toc.html

Make sure to make your script executable (for security reasons this is not done by default):

.. prompt:: bash

    chmod 755 my_first_script.sh

.. _shebang: https://en.wikipedia.org/wiki/Shebang_(Unix)
.. _more info: https://scriptingosx.com/2019/06/moving-to-zsh-part-2-configuration-files/

launchd: Script management
--------------------------
If you created a script and wish to execute regularly or on specific occasion (e.g.
after each log-in), macOS provides the `launchd`_ tool, which manages services and daemons,
similar to Linux' *systemd*. Similar to *cron* on Linux (or the *Task Scheduler* on Windows)
it offers the possibility to schedule executions of shell scripts.

.. hint::

    There are tools which help generating \*.plist files (although you might still
    need to do some manual tweaking afterwards), such as:

    * `LaunchControl`_ (proprietary, needs license)
    * https://launched.zerowidth.com/ (web form -> save as \*.plist, not \*.xml)

Launchd tasks (agents and daemons) are defined in \*.plist config files, which follows the
XML syntax. For our script we create a new file in ``~/Library/LaunchAgents`` (the user
agent directory):

.. prompt:: bash

    touch ~/Library/LaunchAgents/my_first_script.plist

Add in the following content:

.. code-block:: xml
    :linenos:

    <?xml version="1.0" encoding="UTF-8"?>
    <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
    <plist version="1.0">
        <dict>
            <key>Label</key>
            <string>MY_SCRIPT_NAME</string>
            <key>ProgramArguments</key>
            <array>
                <string>/bin/zsh</string>
                <string>-c</string>
                <string>/PATH/TO/MY/SCRIPT.sh</string>
            </array>
            <key>StartInterval</key>
            <integer>3600</integer>
            <key>StandardOutPath</key>
            <string>~/tmp/MY_SCRIPT_NAME.stdout.log</string>
            <key>StandardErrorPath</key>
            <string>~/tmp/MY_SCRIPT_NAME.stderr.log</string>
            <key>AbandonProcessGroup</key>
            <true/>
        </dict>
    </plist>

Now go ahead and replace MY_SCRIPT_NAME and PATH/TO/MY/SCRIPT.sh to match your script. Also edit the
*StartInterval* time if needed (above set to 3600 seconds, which is one execution per hour).
To run the script only once on login replace

.. code-block:: xml
    :linenos:
    :lineno-start: 13

    <key>StartInterval</key>
    <integer>3600</integer>

with

.. code-block:: xml
    :linenos:
    :lineno-start: 13

    <key>RunAtLoad</key>
    <true/>

For more information on the plist options, check https://www.launchd.info/.

After you finished configuration file, add it to the *launchd* controller:

.. prompt:: bash

    launchctl load ~/Library/LaunchAgents/my_first_script.plist

To check the status of the last execution run (replace MY_SCRIPT_NAME with the label
you defined in your \*.plist file)

.. prompt:: bash

    launchctl list | grep MY_SCRIPT_NAME

which lists the return code of your script from the last execution, which should be 0,
if the script ran successfully. Check the *stderr.log* and *stdout.log* files which
you defined in the \*.plist config file for clues.

.. hint::

    The return code is always 0 before the script was executed once after loading it.
    For debugging, change to a low *StartInterval* value to trigger an execution.

To remove the script from the launcher run

.. prompt:: bash

    launchctl unload ~/Library/LaunchAgents/my_first_script.plist

.. hint::

    Changes to the shell script are adapted and used at the next execution, but changes
    to the \*.plist require a reload (*unload* then again *load*) to the launch controller.

.. _launchd: https://www.launchd.info/
.. _LaunchControl: https://www.soma-zone.com/LaunchControl/
