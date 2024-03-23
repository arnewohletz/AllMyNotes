Bash shell
==========
Colorful for text output
------------------------
Same as for the :ref:`Windows terminal <windows_terminal_colorful_text>`,
bash is also able to display colorful text outputs.

Find this `reference`_ to determine the needed color code.

To define a text foreground color, apply the desired color **before** the
respective text. For convenience, you may want to define it as a variable:

.. code-block:: shell

    #!/bin/bash

    RED="\e[31m"
    DEFAULT="\e[39m"

    echo -e "${RED}This is in red${DEFAULT}"
    echo -e "This uses the default color"

which prints out the following:

    | :rfg:`This is in red`
    | This uses the default color

.. _reference: https://misc.flogisoft.com/bash/tip_colors_and_formatting
