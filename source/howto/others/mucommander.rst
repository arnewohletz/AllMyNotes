Set up muCommander
==================
`muCommander`_ is a cross-platform file manager. These steps show how to configure and
alter the tool to make it a better experience on macOS. The following steps will change
the UI similar to the following:

.. list-table:: muCommander UI

    * - .. thumbnail:: _img/mucommander_vanilla.png
            :group: ui_change

            muCommander (Vanilla UI)

      - .. thumbnail:: _img/mucommander_improved.png
            :group: ui_change

            muCommander (Improved UI)

Add high-res icons
------------------
muCommander currently only has very low resolution icons, which look very pixelated, especially
when increasing the icon size in the preferences. A `fork`_ provides higher resolution icons, which
can replace the low-res icons:

#. Extract :download:`highres_icons.zip <_file/highres_icons.zip>` into ``~/Downloads``.
#. Execute this command (adapt the version number, here 1.0.1):

    .. prompt:: bash

        jar -uf /Applications/muCommander.app/Contents/app/app/mucommander-core-1.0.1.jar -C ~/Downloads/highres_icons images/action

#. (Re)start muCommander.

Add better dark theme
---------------------
muCommander features a few themes, but the dark themes might to appease everyone. Luckily, additional themes
can be imported.

#. Download latest version of *Flatlaf IntelliJ Themes* from https://search.maven.org/search?q=a:flatlaf-intellij-themes.
#. Open muCommander.
#. Go to :menuselection:`Preferences --> Appearance`.
#. Under *Look & Feel*, select :guilabel:`Import` and select ``flatlaf-intellij-themes-<SOME_VERSION>.jar``.
#. Select one of the newly added themes from the *Look & Feel* dropdown selection menu and apply it.

Custom theme settings
---------------------
The file systems panes can also be altered and those settings can both be exported and imported.
These steps apply a custom settings file via import which sets it to a dark tone.

#. Open muCommander.
#. Go to :menuselection:`Preferences --> Appearance`.
#. Under 'Theme', select 'Import' and select
   :download:`custom_dark_theme_settings.xml <_file/custom_dark_theme_settings.xml>`.
#. You may want to do adjustments manually.
#. Close preferences with :guilabel:`OK`.

Switch to dark window bar
-------------------------
To get a window bar, which matches the system theme, a new option must be passed when
muCommander is launched.

#. Open ``/Applications/muCommander.app/Contents/app/muCommander.cfg`` with a text editor.
#. Add this line into the ``[JavaOptions]`` section:

    .. code-block:: none

        java-options=-Dapple.awt.application.appearance=system

#. Save and close the file, then restart muCommander.

Change default text editor
--------------------------
muCommander comes with its own internal text editor, which offers little to none features,
but is only useful for simplest text editing. You might want to set a different editor
as default. Here, `Visual Studio Code`_ is set as the default, but any other editor can be
used (just make sure it can be launched over the command line).

#. Open ``~/Library/Preferences/muCommander/commands.xml``.
#. Change the value of the ``edit`` alias to

    .. code-block::

        <command alias="edit" value="/usr/local/bin/code $f" type="system"/>

#. Save and close the file, then restart muCommander. Try editing a text file (:kbd:`F4`).

.. _muCommander: https://www.mucommander.com/
.. _fork: https://github.com/trol73/mucommander
.. _Visual Studio Code: https://code.visualstudio.com/