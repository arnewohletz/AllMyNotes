Modern-Unix - Alternatives for standard tools
=============================================
Source: https://github.com/ibraheemdev/modern-unix

|:+1:| |:+1:| bat
-----------------
https://github.com/sharkdp/bat

An alternative for ``cat``.

Install via

.. prompt:: bash

    brew install bat

Configure theme,

.. prompt:: bash

    bat --list-themes

Select a suitable theme, then add this line to your ``~/.zprofile`` or ``.bashrc``
(here using the *Coldark-Dark* theme, adjust to your theme):

    .. code-block:: none

        # bat
        export BAT_THEME="Coldark-Dark"

|:+1:| eza
----------
https://github.com/eza-community/eza

An alternative for ``ls``.

Install via

.. prompt:: bash

    brew install eza

Display the contents of a directory with extended details, groups column and icons:

.. prompt:: bash

    eza -lg --icons

|:+1:| |:+1:| lsd
-----------------
https://github.com/lsd-rs/lsd

An alternative for ``ls``

Install via

.. prompt:: bash

    brew install lsd

|:+1:| |:+1:|  duf
------------------
https://github.com/muesli/duf

An alternative for ``du``

Install via

.. prompt:: bash

    brew install duf

df
--
https://github.com/sharkdp/fd

An alternative for ``find``

Install via

.. prompt:: bash

    brew install fd
