Task scheduling using launchd
=============================
Similar to Linux' `crontab`_ and Windows' `Task Scheduler`_, macOS features a tool
to schedule automatic executions of scripts or other commands, `launchd`_.

Launchd manages agents and daemons which are defined in so called *job definition* files.
These files use the `Property list`_ format, an XML based format. There are tools
available for creating \*.plist files, such as `LaunchControl`_ (proprietary tool) or
`launched`_ (free web application).

Let's create a user agent for a shell script (here `example.sh`, which does a task we
like to execute every hour):

#. Open `launched`_ and enter

    * Name: ``example``
    * Command: ``/path/to/example.sh``
    * Start Interval: ``3600`` (3600 seconds = 1 hour)

    .. hint::

        You may also define the *Standard out path* and *Standard error path* to
        save ``stout`` and ``sterr`` into specific files for debugging purposes,
        for example:

        * Standard out path: ``~/tmp/example_sh_stout.log``
        * Standard error path: ``~/tmp/example_sh_sterr.log``

        Now you don't need to redirect ``stdout`` or ``stderr`` in the script itself.

#. Select :guilabel:`Create Plist`, on the following page select :guilabel:`download`.
#. Save the resulting file as **plist** (not xml) into ``~/Library/LaunchAgents/``
   (you may change the filename).
#. Add the \*.plist file to the list of loaded launch agents:

    .. prompt:: bash

        launchctl load -w ~/Library/LaunchAgents/launched.example.plist

    The script is now executed every hour.

.. important::

    If you change your \*.plist file, you need to re-load it to apply the changes:

    .. prompt:: bash

        launchctl unload -w ~/Library/LaunchAgents/launched.example.plist
        launchctl load -w ~/Library/LaunchAgents/launched.example.plist

    Doing changes to the shell script file does :ulined:`not` require a re-load of the
    launch agent.

.. _crontab: https://man7.org/linux/man-pages/man5/crontab.5.html
.. _Task Scheduler: https://en.wikipedia.org/wiki/Windows_Task_Scheduler
.. _launchd: https://www.launchd.info/
.. _LaunchControl: https://www.soma-zone.com/LaunchControl/
.. _launched: https://zerolaunched.herokuapp.com/