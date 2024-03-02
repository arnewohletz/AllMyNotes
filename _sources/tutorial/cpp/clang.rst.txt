Clang++ Compiler
================
Clang_ is a popular compiler for the C language family (such as C/C++, Objective C/C++).
Clang++ is referred to as the C++ compiler within Clang. It is the default C++ compiler
on OSX, comes with XCode and the XCode command line tools.

.. _Clang: https://clang.llvm.org/

Installation
------------
Install the XCode command line tools:

.. prompt:: bash

    sudo xcode-select --install

This will trigger the download and installation.

If you already have those installed, but are unable to update them to a later version,
first remove them manually, then re-install:

.. prompt:: bash

    sudo rm -rf /Library/Developer/CommandLineTools
    sudo xcode-select --install

Usage
-----
Clang++ is a command line tool, which features a lot of optional parameters.

**Basic compilation**

.. prompt:: bash

    clang++ --std=c++20 -g <input_file> -o <output_file>

:``--std=<standard>``:
    Language standard to compile for. Possible: c++98, c++11, c++14, c++17, c++20

:``-o <file>``:
    Write output to <file>

:``-g``:
    Generate source-level debug information. Needed for debugging.