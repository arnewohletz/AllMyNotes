Run multiple different profile instances
----------------------------------------
Commonly, only one firefox instance can be executed at a time. Opening two or more
instances, each instance featuring a different profile can be done using a trick.

macOS
`````
#. Create a new file within ``/usr/local/bin``:

    .. prompt:: bash

        sudo touch /usr/local/bin/firefox

#. Open the file:

    .. prompt:: bash

        sudo nano /usr/local/bin/firefox

#. Add the following content and save the file:

    .. code-block:: none

        #!/bin/zsh

        /Applications/Firefox.app/Contents/MacOS/firefox-bin -no-remote -P $1

#. To open Firefox using a specific profile, type:

    .. prompt:: bash

        firefox <profile_name>

    .. hint::

        You can find out the profile name, open a Firefox window and enter ``about:profiles``
        into the address bar. The profile names are listed there (Profile: <profile_name>).

        Please note, that profile names are case-sensitive. If the profile name is entered
        incorrectly, the profile selection screen appears and the profile must be selected
        manually. It is still possible to open multiple instances with different profiles, though.

Linux
`````
coming soon

Windows
```````
coming soon