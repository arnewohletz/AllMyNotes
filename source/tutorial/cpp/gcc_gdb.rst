GCC Compiler
============
`gcc <https://gcc.gnu.org/>` is a popular compiler compilation for C/C++ on Linux.
It is also available on Windows either via `minGW <http://mingw-w64.org/doku.php>`
or `Cygwin <https://sourceware.org/cygwin/>`.

Install GCC on Linux (Ubuntu)
-----------------------------
GCC may come preinstalled on Linux. Check your installed version, if any:

    .. code-block:: bash

        $ gcc -v

#. Update or install your GCC compiler:

    .. code-block:: bash

        $ sudo apt-get update
        $ sudo apt-get install build-essential gdb

Install GCC on Windows
----------------------
GCC comes bundled in mingw-w64, which is a still maintained, advanced version of the
original MinGW project. For convenience, we will use `MYSYS2 <https://www.msys2.org/>`
to install mingw-w64.

#. Go to https://www.msys2.org/ and download the installer and follow the installation steps.
#. Open a ``C:\mysys64\mysys2.exe`` to open a MYSYS2 shell.
#. Run these commands to install the base packages:

    .. code-block:: bash

        $ pacman -Syu

    .. code-block:: bash

        $ pacman -Su

#. Run this command to install the build tools including GCC:

    .. code-block:: bash

        $ pacman -S --needed base-devel mingw-w64-x86_64-toolchain

#. Next, add the .\mingw64\bin directory within you MYSYS2 installation to your PATH variable.
#. Open a new command window and try to run:

    .. code-block:: bash

        $ g++ --version
        $ gdb --version

    .. hint::

        G++ is the compiler of GCC used for C++ source code and GDB is a debugger,
        capable of debugging C++ code.

Build & Debug C++ in Visual Studio Code
---------------------------------------
Visual Studio Code supports `GDB <https://www.gnu.org/software/gdb/>` for debugging
C++ code.

Make sure, the `C/C++ extension`_ is installed.

In a new folder, create a \*.cpp file and add some content.

Open *Terminal / Configure Default Build Task* and choose **g++.exe** as compiler
(e.g. ``C:\mysys64\mingw64\bin\g++.exe`` on Windows or ``/usr/bin/g++``on Linux),
which will create the file ``.\.vscode\tasks.json``, defining your build parameters.

To **build** a file, select it, the choose *Terminal / Run Build Task...*, which will trigger
the build, which eventually puts an \*.exe file of the same name into the same directory.
You can execute the file by running:

    .. code-block:: bash

        $ my_file.exe

from the output directory.

In order to **debug** a file, first we create a configuration for it. Select *Run / Add Configuration*
and select **GDB/LLDB** and next up again **g++** as the compiler (pointing towards the MinGW G++ compiler
e.g.``C:\mysys64\mingw64\bin\g++.exe``).

This will create the new file ``.\.vcode\launch.json`` and start the debugging in a new Terminal window.

Further details:
https://code.visualstudio.com/docs/cpp/cpp-debug
https://code.visualstudio.com/docs/cpp/config-mingw

.. _C/C++ extension: https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools