Set up iTerm2
=============
iTerm2 is a Terminal alternative for macOS.

Installation
------------
Install `iTerm2`_ via Homebrew:

.. prompt:: bash

    brew install --cask iterm2

Install `oh-my-zsh`_ via

.. prompt:: bash

    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

Set up movement & delete shortcuts
----------------------------------
iTerm does not feature shortcuts for moving word-by-word or to the end or beginning of a line.

#. Go to :menuselection:`Settings --> Profiles --> Keys --> Key Mapping`.
#. Add these new key mapping, for each selection `Send Escape Sequence` as Action:

    +-----------------------+----------------------+-----------+--------------------------------+
    | Key Mapping           | Action               | Value     | Does what?                     |
    +=======================+======================+===========+================================+
    | :kbd:`Alt + Left`     | Send Escape Sequence | b         | Jump one word to the left      |
    +-----------------------+----------------------+-----------+--------------------------------+
    | :kbd:`Alt + Right`    | Send Escape Sequence | f         | Jump one word to the right     |
    +-----------------------+----------------------+-----------+--------------------------------+
    | :kbd:`Alt + Del<-`    | Send Hex Code        | 0x17      | Delete left standing word      |
    +-----------------------+----------------------+-----------+--------------------------------+
    | :kbd:`Alt + Del->`    | Send Escape Sequence | d         | Delete right standing word     |
    +-----------------------+----------------------+-----------+--------------------------------+
    | :kbd:`Cmd + Left`     | Send Escape Sequence | OH        | Move to beginning of the row   |
    +-----------------------+----------------------+-----------+--------------------------------+
    | :kbd:`Cmd + Right`    | Send Escape Sequence | OF        | Move to end of the row         |
    +-----------------------+----------------------+-----------+--------------------------------+
    | :kbd:`Cmd + Del<-` \* | Send Hex Code        | 0x18 0x7f | Delete current row             |
    +-----------------------+----------------------+-----------+--------------------------------+
    | :kbd:`Cmd + Del->`    | Send Hex Code        | 0x0b      | Delete everything after cursor |
    +-----------------------+----------------------+-----------+--------------------------------+

    \* need to add this to your `~/.zshrc` or `~/.zprofile` to make it work:

        .. code-block:: none

            # iTerm2 support for 'Delete current row' keymap
            bindkey "^X\\x7f" backward-kill-line

A quicker solution, but which does not feature all above key mappings is to change the presets to
*Natural Text Editing*.

.. _iTerm2: https://iterm2.com/index.html
.. _oh-my-zsh: https://ohmyz.sh/

Set custom color theme
----------------------
There `a lot of color themes`_ to choose from.

#. Open the XML files for the respective theme and save it as *\*.itermcolors* file.
#. In iTerm go to :menuselection:`Settings --> Profiles --> Colors`.
#. Select :menuselection:`Color Preset... -> Import...` and select the *\*.itermcolors* file.
#. Again chose :guilabel:`Color Presets...`, and select the imported theme. They are
   immediately applied to the current shell.

.. _a lot of color themes: https://iterm2colorschemes.com/

Set custom oh-my-zsh theme
--------------------------
There are a `variety of themes`_ available for iTerm (all compatible with oh-my-zsh).

In this guide, the `powerlevel10k`_ theme is used for demonstration.

#. Install the theme via homebrew:

    .. prompt:: bash

        brew install powerlevel10k

#. Add it to your ``~/.zshrc`` file to be launched for each new shell window:

    .. prompt:: bash

        echo "source $(brew --prefix)/share/powerlevel10k/powerlevel10k.zsh-theme" >>~/.zshrc

#. Open a new shell window to start the setup wizard.
#. Confirm installing the new font, afterwards restart iTerm2.
#. The setup resumes. Follow the instructions and make your choices

.. _variety of themes: https://github.com/ohmyzsh/ohmyzsh/wiki/External-themes
.. _powerlevel10k: https://github.com/romkatv/powerlevel10k

Add custom plugins
------------------
Oh-my-zsh features a lot of optional plugins for various purposes. A list is available in the
`Plugins wiki page`_. The only plugin already pre-enabled is the `git plugin`_.

To add a plugin, open the ``~.zshrc`` file and add the plugin name to the *plugins* variable,
for example:

    .. code-block:: none

        plugins=(git pyenv)

.. _Plugins wiki page: https://github.com/ohmyzsh/ohmyzsh/wiki/Plugins
.. _git plugin: https://github.com/ohmyzsh/ohmyzsh/tree/master/plugins/git

Other tweaks
------------
* Change cursor to blinking, vertical bar:

    :menuselection:`Settings --> Profiles --> Text --> Cursor`:

        * select *Vertical bar*
        * check *Blinking cursor*

* Add command syntax highlighting:

    #. Install `zsh-syntax-highlighting`_:

        .. prompt:: bash

            brew install zsh-syntax-highlighting

    #. Enable it by adding a source line to your ``~/.zshrc`` file:

        .. prompt:: bash

            echo "source $(brew --prefix)/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc

.. _zsh-syntax-highlighting: https://github.com/zsh-users/zsh-syntax-highlighting
