Shell Scripting
===============

Script arguments
----------------
``$0``

    The shell script name.

``$1 $2 ...``

    The positional arguments passed into the shell script.

``$*``

    Prints all arguments passed into the script (except ``$0``), space separated.

    To change the separator (here: comma), define the ``IFS``:

    .. code-block:: bash

        IFS=,
        echo "$*"

``$#``

    The amount of arguments passed into a shell script (without ``$0``).

Variables
---------
``local``

    Define a variable as local. This will overwrite any equally named global variable.

    .. code-block:: bash

        var1="hello"

        function hi() {
            local var1
            var1="hi"
            echo "$var1"
        }

        hi()

    will print ``hi``, not ``hello``.

String Operators
----------------
``${varname:-word}``

    If ``${varname}`` exists and isn't ``null`` it returns its value, otherwise
    returns ``word``.

``${varname:=word}``

    If ``${varname}`` exists and isn't ``null`` it returns its value, otherwise
    it is set to ``word`` and then returned.

``${varname:?message}``

    If ``${varname}`` exists and isn't ``null`` it returns its value, otherwise
    print ``varname`` followed by ``message`` and abort the current command or
    script (non-interactive shells only).

    Used to catch errors from undefined variables.

``${varname:+word}``

    If ``${varname}`` exists and isn't ``null`` it returns its ``word``, otherwise
    return null.

``${varname:offset: length}``

    It returns the substring of $varname starting at offset and up to length characters.
    First character is at position 0. If length is omitted, string is returned until
    the end. If offset is less than 0, offset is taken from end of varname.

Continue at page 92 (Learning the Bash Shell)