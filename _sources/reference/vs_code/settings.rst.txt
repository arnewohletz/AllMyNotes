Customize via settings.json
===========================
VS-Code puts every change to the default configuration in a ``settings.json`` file.
Multiple configurations may exists, which which override each other. The order
is defined in the `VS settings precendence`_. The order, from most general to
most specific, where more general settings get overwritten by more specifics settings,
is:

#. Default settings  --> not configured (has no ``settings.json`` file)
#. User settings --> defined in each profile (``Code/User/profiles/<profile ID>/settings.json``)
#. Remote settings --> applied to a remote machine
#. Workspace settings --> applied to opened folder or workspace (``<workspace>/.vscode/settings.json``)

Language specific settings follow in the same order:

#. Language default settings
#. Language user settings
#. Language remote settings
#. Language workspace settings

Define settings for all profiles
--------------------------------
The *default* profiles can hand over settings to all other profiles by adding the
setting name to the ``"workbench.settings.applyToAllProfiles": [...]`` list.

.. code-block:: json

    {
        // Common settings (for all profiles)
        "workbench.settings.applyToAllProfiles": [
            "editor.insertSpaces",
            "editor.accessibilitySupport",
            "editor.autoIndent",
            "editor.fontFamily",
            "editor.fontSize",
            "editor.indentSize",
            "editor.minimap.enabled",
            "editor.renderWhitespace",
            "editor.tokenColorCustomizations"
        ]
        // more common settings ...
    }

In the example above, for instance ``"editor.fontSize"`` is applied to all profiles,
even if they specify their own ``settings.json`` as their settings source. To apply
a profiles own value for a setting, it must be remove from that list in the default
profile.

.. hint::

    Alternatively, while being in the default profile, a settings can be applied
    to all profiles from the settings menu. Click the gear button and select
    ``Apply Settings to all Profiles``.

.. _VS settings precendence: https://code.visualstudio.com/docs/getstarted/settings#_settings-precedence