Install zsh (without WSL)
=========================
Follow these steps to have a native zsh shell on Windows without creating a WSL,
including:

* oh-my-zsh
* Starship
* zsh-autosuggestions
* zsh-syntax-highlighting

#. Install Git for Windows (https://git-scm.com/install/windows), which will include
   the *git bash*.
#. Set up new profile in Terminal and use as default. In ``settings.json``, for example:

    .. code-block:: json

        {
            "commandline": "C:\\Program Files\\Git\\bin\\bash.exe",
            "guid": "{648d1200-3839-452b-81d5-a7d238447a6c}",
            "hidden": false,
            "icon": "C:\\Program Files\\Git\\mingw64\\share\\git\\git-for-windows.ico",
            "name": "git bash",
            "startingDirectory": "%USERPROFILE%"
        },

#. Install zsh (see https://dev.to/pavlosisaris/windows-command-line-revolution-unleash-zsh-and-oh-my-zsh-a-simple-guide-for-developers-271o)
#. Create ``C:\Users\<USERNAME>\.bashrc`` and insert this into it:

    .. code-block:: sh

        if [ -t 1 ]; then
          exec zsh
        fi

   This launches *zsh* on every start of the *git bash*.

#. Install oh-my-zsh: https://github.com/ohmyzsh/ohmyzsh/wiki
#. Download *FiraCode Nerd Font* from https://www.nerdfonts.com/font-downloads and install it.
#. Install *Starship.rs* (see https://starship.rs/) and append

    .. code-block:: none

        # Enable starship.rs
        # ------------------
        eval "$(starship init zsh | sed 's|/c/Program Files/starship/bin/starship.exe|starship|g')"

    to your ``C:\Users\<USERNAME>\.zshrc`` (create it, if not already existing)

#. Add ``starship.exe`` to your PATH variable e.g. ``C:\Program Files\starship\bin\starship.exe``
#. Create directory and config file for Starship:

    .. code-block:: bash

        $ mkdir -p ~/.config && touch ~/.config/starship.toml

#. Copy config from https://starship.rs/presets/nerd-font into your ``starship.toml``.
#. Install *zsh-syntax-highlighting*:

    .. code-block:: bash

        $ git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting

   and add it to your oh-my-zsh plugins (found inside ``C:\Users\<USERNAME>\.zshrc``):

    .. code-block:: none

        plugins=( [plugins...] zsh-syntax-highlighting)

   Restart shell to see effects. See also: https://github.com/zsh-users/zsh-syntax-highlighting/blob/master/INSTALL.md#with-a-plugin-manager

#. Install zsh autosuggestions:

    .. code-block:: bash

        $ git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions

   and add it to your oh-my-zsh plugins:

    .. code-block:: none

        plugins=( [other plugins...] zsh-autosuggestions )

   Restart terminal to see effects.

Everything is now set up.

Install zsh without admin rights
================================
I followed those steps when setting up laptop at Hensoldt, facing the following
limitations:

    * no admin rights
    * no WSL
    * not very powerful PC

which lead me to the following target:

* zsh (initialize via git-bash)
* zsh-autosuggestions (w/o oh-my-zsh)

as I found *oh-my-zsh* severy impacted my shell startup time (took at least 3 seconds)
and *zsh-syntax-highlighting* severy impacted input speed(took roughly half a second
until a pressed character appeared on the terminal.

#. Install Git for Windows (https://git-scm.com/install/windows), which will include
   the *git bash*.

   .. hint::

        This action requires admin rights, though IT provided the installation
        via the internal tool.

#. Set up new profile in Terminal and use as default. In ``settings.json``, for example:

    .. code-block:: json

        {
            "commandline": "C:\\Program Files\\Git\\bin\\bash.exe",
            "guid": "{648d1200-3839-452b-81d5-a7d238447a6c}",
            "hidden": false,
            "icon": "C:\\Program Files\\Git\\mingw64\\share\\git\\git-for-windows.ico",
            "name": "git bash",
            "startingDirectory": "%USERPROFILE%"
        },

#. Download the `cygwin`_ installer and run it via

    .. code-block:: none

        $ setup-x86_64.exe --no-admin

   to allow installation without admin rights. Install any additional packages that
   you feel necessary (probably most listed in *Basic*). For the following steps,
   you also need to install ``zsh`` (Z-Shell).

   Add the directory, where you installed all packages to your PATH variable.

    .. important::

        I eventually reverted all the next steps, as I found the *zsh* installation
        and initialization via ``.bashrc`` has its shortcomings, despite the efforts.
        Some steps may still be interesting when using the *git-bash*.

        The *git-bash* of course has no support for zsh extensions, though it
        turned out to be better choice nonetheless. Windows, especially when not
        having admin rights just sucks and is a waste of time to set up properly
        for serious software development.

#. Create ``C:\Users\<USERNAME>\.bashrc`` and insert this into it:

    .. code-block:: sh

        if [ -t 1 ]; then
          exec zsh
        fi

   This launches *zsh* on every start of the *git bash*.

#. Create the ``~/.zshrc`` file and insert the following content:

    .. code-block:: none

        # replace bash prompt with zsh-compatible version
        setopt prompt_subst
        PROMPT=$'%{\e]0;%n@%m:%~\a%}%F{green}%n%F{red}@%F{yellow}%m %F{magenta}${MSYSTEM} %F{yellow}%~%F{cyan} %f%{%}'

   This will create a similar line prompt as in *git-bash*. Without it, zsh displays
   the original prompt, which causes encoding problems.

#. When not using *oh-my-zsh* and its *git* plugin, we have to manually add a
   git prompt which is shown whenever the current directory is within a git repository.
   The article https://git-scm.com/book/en/v2/Appendix-A%3A-Git-in-Other-Environments-Git-in-Zsh
   suggests to add this to your ``.zshrc`` file:

    .. code-block:: none

        autoload -Uz vcs_info
        precmd_vcs_info() { vcs_info }
        precmd_functions+=( precmd_vcs_info )
        setopt prompt_subst
        RPROMPT='${vcs_info_msg_0_}'
        # PROMPT='${vcs_info_msg_0_}%# '
        zstyle ':vcs_info:git:*' formats '%b'

   Optionally, you may also add tab-completion for ``git commands``:

    .. code-block:: none

        autoload -Uz compinit && compinit

#. Sadly, `zsh-syntax-highlighting`_ decreased performance of zsh so much, that
   it became unusable. Luckily `zsh-autosuggestions`_ isn't quite as heavy on the
   shell. To install it run

    .. code-block:: none

        $ mkdir ~/.zsh && cd ~/.zsh
        $ git clone https://github.com/zsh-users/zsh-autosuggestions

   the open ``.zshrc`` and add this line:

    .. code-block:: none

        # zsh-autosuggestions
        source ~/.zsh/zsh-autosuggestions/zsh-autosuggestions.zsh

#. If you start the *git-bash* now, you will notice that :kbd:`Ctrl+Left` or
   :kbd:`Ctrl+Right` no longer jump back and forth to the next or previous
   entered word in the current line. To fix that, we create a new file ``~/.bindings``
   and put in this content:

    .. code-block:: none

        set enable-bracketed-paste Off

        bindkey '^[[1;5C' forward-word
        bindkey '^[[1;5D' backward-word
        bindkey '^[[1;3D' beginning-of-line
        bindkey '^[[1;3C' end-of-line

   This will enable the following shortcuts:

    * :kbd:`Ctrl+Left`: Jump to beginning of previous word
    * :kbd:`Ctrl+Right`: Jump to beginning of next word
    * :kbd:`Alt+Left`: Jump to beginning of the line
    * :kbd:`Alt+Right`: Jump to end of the line

   Open ``.zshrc`` and add this line:

    .. code-block:: none

        # source custom key bindings
        source ~/.bindings

#. For *git-bash* to support the ``.bindings`` file, open the :guilabel:`Options...`
   in *git-bash.exe*, navigate to *Keys* and uncheck the option
   *Esc/Enter reset IME to alphanumeric*.
#. Optionally, attach this function to ``.zshrc`` to automatically activate a
   Python virtual environment when entering a directory, which contains a ``.venv``
   directory:

    .. code-block:: sh

        # Auto-activate Python venv if .venv directory exists
        function cd() {
          builtin cd "$@"

          if [[ -z "$VIRTUAL_ENV" ]] ; then
            ## If env folder is found then activate the vitualenv
              if [[ -d ./.venv ]] ; then
                source ./.venv/Scripts/activate
              fi
          else
            ## check the current folder belong to earlier VIRTUAL_ENV folder
            # if yes then do nothing
            # else deactivate
              parentdir="$(dirname "$VIRTUAL_ENV")"
              if [[ "$PWD"/ != "$parentdir"/* ]] ; then
                deactivate
              fi
          fi
        }

#. Also optionally, provide additional environment variables, which are not present
   in this setup otherwise, such as ``$HOSTNAME``:

    .. code-block:: none

        # Manually defining env variables
        export SHELL="/usr/bin/zsh"
        export HOSTNAME=$(/usr/bin/hostname)
        export USER=$USERNAME

   Add other variables as needed.

.. _zsh-syntax-highlighting: https://github.com/zsh-users/zsh-syntax-highlighting
.. _zsh-autosuggestions: https://github.com/zsh-users/zsh-autosuggestions
.. _cygwin: https://cygwin.com/install.html
