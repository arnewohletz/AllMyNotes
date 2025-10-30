.gitconfig
==========
The ``.gitconfig`` contains the user configuration for git. It applies to any
local repository of the current user. It can be overwritten for individual local
repositories by defining it in the repository's ``.git/config`` file.

The global ``.gitconfig`` is located at

    * macOS/Linux: ``~/.gitconfig``
    * Windows: ``%USERPROFILE%/.gitconfig``

whereas a repositories git config is located at ``.git/config``.

The system-wide ``gitconfig`` defines config variable at a system level, but may
be overwritten by the global and repository config. It is located at

    * macOS (git installed via *homebrew*): ``/opt/homebrew/etc/gitconfig``
    * Linux: ``/etc/gitconfig``
    * Windows (for `Git for Windows`_): ``C:\Program Files\Git\etc\gitconfig``

The full reference for git config value is `provided here <git_config_values_>`_.
This reference contains a selection.

To edit the respective files, run

.. code-block:: none

    git config --system --edit
    git config --global --edit
    git config --local --edit

which opens the file with the default editor (set as ``EDITOR`` environment variable).

.. _Git for Windows: https://git-scm.com/download/win
.. _git_config_values: https://git-scm.com/docs/git-config#_variables


[alias]
-------
Contains custom git alias commands in this form:

.. code-block:: ini

    my-simple-alias = !echo "Hello there!"

The ``!`` is needed upfront to run an external (non-git) command. It is called via

.. code-block:: bash

    $ git my-simple-alias

To create a more complex, multiline script, the script is put into a function
(here: ``f()``), which is eventually called. Inside the function, lines have to
end with a ``\`` to be continued in the next line. Commands are separated with ``;``:

.. code-block:: ini

    my-more-complex-alias = "!f(){\
        echo 'Hello there';\
        echo 'Have a nice day';\
    }; f"


[core]
------
**autocrlf**

For Windows users, the variable should be set to ``true``, which changes the line
endings to *CRLF* for all files of a repository. If users using macOS or Linux
also contribute to the repository, they submit *LF* line endings, which need to
be transformed.

For macOS/Linux users, the variable should be set to ``input`` which omits any
line ending conversions.

**editor**

Defines the editor to be used to edit messages on ``commit`` or ``tag``.

[credential]
------------
**helper**

Defines the credential management helper tool, which is called if username and
password is needed.

Common values:

* macOS: ``osxkeychain`` (macOS internal Keychain)
* Linux: *not sure*
* Windows: ``manager`` (the cross-platform `git-credential-manager`_, included in
  `Git for Windows`_)

[pull]
------
**rebase**

When set ``true``, rebase branches on top of the fetched branch, instead of
merging the default branch from the default remote when "git pull" is run.

[user]
------
**name**
The name of the author set to the ``author`` and ``committer`` field of
commit objects.

**email**
The email of the author set to the ``author`` and ``committer`` field of
commit objects.



.. _git-credential-manager: https://github.com/git-ecosystem/git-credential-manager