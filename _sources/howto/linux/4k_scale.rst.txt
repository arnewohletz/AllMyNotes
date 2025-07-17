Scale Java Applications for 4K displays
=======================================
Java applications often don't scale to higher resolutions (above Full-HD), making
them barely readable on 4k resolutions. Generally, running an application with the
additional ``JAVA-OPTS="-Dsun.java2d.uiScale=2"`` environment variable scales the
application (here: at a factor of 2). Depending on how the application is launched,
the steps on adding this variable are different.

On \*.desktop launcher files
----------------------------
#. Open the directory of the original ``*.desktop`` file.
#. Create a copy of it, naming it something like ``<original_name>_4k.desktop``.
#. Open it in an editor and adjust the ``Exec=`` statement adding the needed
   environment variable. For example, change

    .. code-block:: none

        Exec=/usr/bin/flatpak run --branch=stable --arch=x86_64 --command=soapui-launcher.sh. org.soapui.SoapUI

   into

    .. code-block:: none

        Exec=env JAVA-OPTS="-Dsun.java2d.uiScale=2" /usr/bin/flatpak run --branch=stable --arch=x86_64 --command=soapui-launcher.sh. org.soapui.SoapUI

#. Now run the new launcher file and the application should scale accordingly.
