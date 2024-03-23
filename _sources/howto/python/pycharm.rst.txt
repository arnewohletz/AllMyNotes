Pycharm
=======
Remove invisible interpreters
-----------------------------
It may happen, that a previously added Python interpreter is not displayed
on the *Show All* interpreter list
(:menuselection:`Settings --> Project --> Project Interpreter --> Show All...`)
though the interpreter still exists in the configuration. The effect is
that naming an interpreter the same as such a invisible one, leads to an error:

    .. code-block:: none

        Cannot Save Settings
        Please specify a different SDK name

The solution is to remove the entry from the SDK configuration file:

.. tabs::

    .. group-tab:: macOS

        ``~/Library/Application Support/JetBrains/PyCharm<VERSION>/options/jdk.table.xml``

    .. group-tab:: Linux

        ``~/.config/JetBrains/PyCharm<VERSION>/options/jdk.table.xml``

    .. group-tab:: Windows

        ``%APPDATA%\JetBrains\PyCharm<VERSION>\options\jdk.table.xml``

Open the file in a text editor. Remove the entire XML node which starts with

.. code-block:: xml

    <jdk version="2">
        <name value="YOUR_UNWANTED_PYTHON_INTERPRETER_NAME" />
        ...
    </jdk>

and save the file.

Restart Pycharm to apply the changes.
