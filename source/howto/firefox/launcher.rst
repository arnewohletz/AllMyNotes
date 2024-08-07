Run multiple instances with separate profile
--------------------------------------------
Commonly, only one Firefox instance can run at a time. Opening two or more
instances, each instance featuring a different profile can be done using a trick.

macOS
`````
#. Create a new file within ``/usr/local/bin``:

    .. code-block:: bash

        $ sudo touch /usr/local/bin/firefox

#. Open the file:

    .. code-block:: bash

        $ sudo nano /usr/local/bin/firefox

#. Add the following content and save the file:

    .. code-block:: none

        #!/bin/zsh

        /Applications/Firefox.app/Contents/MacOS/firefox-bin -no-remote -P $1

#. To open Firefox using a specific profile, type:

    .. code-block:: bash

        $ firefox <profile_name>

    .. hint::

        You can find out the profile name, open a Firefox window and enter ``about:profiles``
        into the address bar. The profile names are listed there (Profile: <profile_name>).

        Please note, that profile names are case-sensitive. If the profile name is entered
        incorrectly, the profile selection screen appears and the profile must be selected
        manually. It's still possible to open multiple instances with different profiles, though.

Linux
`````
coming soon

Windows
```````
coming soon
