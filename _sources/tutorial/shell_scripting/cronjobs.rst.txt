Linux: Manage scripts via cron job
----------------------------------
The Cron daemon is a built-in Linux utility that runs processes on your system
at a scheduled time. Cron reads the crontab (cron tables) for predefined
commands and scripts.

Cron jobs run as the current user are define in your user's ``crontab`` file.
To open it run

.. code-block:: bash

    $ crontab -e

You may need to select an editor on first usage.

At the bottom, create a new, single line entry in the following manner:

    ``<SCHEDULE_EXPRESSION> [<PATH_TO_COMMAND>]<COMMAND> [<ARGUMENTS>] [OUTPUT]``

where the **SCHEDULED_EXPRESSION** defines how often crontab triggers a command.
Use the `crontab guru`_ to create such an expression.

If your command is only reachable from a specific directory, also specify the
**PATH_TO_COMMAND**

Finally, define the **COMMAND** you want crontab to run.

If your command requires further **ARGUMENTS**, enter them after the command,
like you would when running the command manually.

The **OUTPUT** is also optional, defining if where the executable defers the
output, for example into a file

Example:

.. code-block:: none

    # Print contents of a directory every 10 minutes and write to output.log
    */5 * * * * /usr/bin/make -f /some/directory/Makefile do_this > output.log

.. _crontab guru: https://crontab.guru
