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

    To change the separator (here: comma), define the ``IFS`` (Internal Field Separator):

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

Patterns
''''''''
Example: ``some_path=/home/cam/book/long.file.name``

Pattern matching operator:

    | ``#`` matches the front ("number signs precede numbers")
    | ``%`` matches the rear ("percent signs follow numbers")

``${variable#pattern}``

    If the ``pattern`` matches the beginning of the variable's value, delete the shortest
    path that matches and return the rest.

    .. prompt:: bash

        echo ${some_path#/*/}
        # cam/book/long.file.name

    ``/*/`` matches everything between two slashes. The *shortest* pattern match
    on the front is ``/home/``, which is deleted.

``${variable##pattern}``

    If the ``pattern`` matches the beginning of the variable’s value, delete the longest
    part that matches and return the rest.

    .. prompt:: bash

        echo ${some_path##/*/}
        # long.file.name

    ``/*/`` matches everything between two slashes. The *longest* pattern match
    on the front is ``/home/cam/book``, which is deleted.

``${variable%pattern}``

    If the ``pattern`` matches the end of the variable’s value, delete the shortest
    part that matches and return the rest.

    .. prompt:: bash

        echo ${some_path%.*}
        # /home/cam/book/long.file

    ``.*`` matches a dot and everything that follows it. The shortest pattern match
    on the rear is ``.name``, which is deleted.

``${variable%%pattern}``

    If the ``pattern`` matches the end of the variable’s value, delete the longest
    part that matches and return the rest.

    .. prompt:: bash

        echo ${some_path%%.*}
        # /home/cam/book/long

    ``.*`` matches a dot and everything that follows it. The longest pattern match
    on the rear is ``long.file.name``, which is deleted.

    .. hint::

        If *exact* matches are found, only the *first* match is deleted:

        .. prompt:: bash

            export name=alicece
            echo ${name%%ce}
            # alice

        But if using the wildcard ``*``, then the longest occurrence will contain
        everything that follows it:

        .. prompt:: bash

            export name=alicece
            echo ${name%%ce*}
            # ali

``${variable/pattern/string}``

    The longest match to ``pattern`` in variable is replaced by ``string``.
    Only the first match is replaced.

    | If ``pattern`` starts with a ``#`` it must match with the start of the variable.
    | If ``pattern`` starts with a ``%`` it must match with the end of the variable.
    | If ``string`` is null, the matches are deleted.

``${variable//pattern/string}``

    The longest match to ``pattern`` in variable is replaced by ``string``.
    All matches are replaced.

    **Example:** Replace all colons with LINEFEED in PATH variable (print each
    entry in new line)

    .. prompt:: bash

        echo -e ${PATH//:/'\n'}

``${#varname}``

    Returns the length of the value of the variable as a character string

    .. prompt:: bash

        export SOME_VAR=123456789
        echo ${#SOME_VAR}
        # 9

Command substitution
--------------------
``command_A $(command_B)`` means, to use the return value of a ``command_B``
as a variable for ``command_A``. For example:

.. prompt:: bash

    # open all txt files in the current directory which contain 'hello'
    vi $(grep -l 'hello' *.txt)

Directory stack
---------------
The directory stack is known as a “last-in, first-out” or LIFO structure. Putting
something on the stack is referred to as *pushing*, taking something off the stack
is called *popping*.

*Pushing* and *popping* allows to move back to previous directories along the
directory stack.

``pushd <some/path>``

    Puts the current directory onto the directory stack and ``cd`` into the directory.
    The first time, ``pushd`` is called in a script or shell session, the current
    directory is pushed onto the directory stack first.

    Example:

    .. prompt:: bash

        pushd /some/path       # cd into /some/path

    .. code-block:: none

        # Directory stack
        /some/path   # top of the stack
        $(pwd)      # directory where pushd was initially called from

``popd``

    Remove the directory at the top of the directory stack, which then reveals
    a new top, then ``cd`` into that.

    Example:

    .. prompt:: bash

        popd                # cd into $(pwd)

    .. code-block:: none

        # Directory stack
        $(pwd)      # directory where pushd was initially called from

Flow controls
-------------
if/else
'''''''

.. code-block:: bash

    if condition
    then
        statements
    [elif condition
        then statements...]
    [else
     statements]
    fi

Condition Tests
'''''''''''''''
Square brackets ([]) surround expressions that include various types of operators:

.. code-block:: bash

    if [ condition_a ]; then
        ...
    elif [ condition_b ]; then
        ...
    else
        ...
    fi

**Multiple conditions**

.. code-block:: bash

    # all conditions must be True (AND)
    if [ condition ] && [ condition ] ...; then
    ...
    # using the -a operator (AND)
    if  [ condition_a -a condition_b ... ]; then
    ...

    # at least one codition must be True (OR)
    if [ condition ] || [condition ] ...; then
    ...
    # using the -o operator (OR)
    if [ condition_a -o condition_b ...]; then
    ...

**Combine condition and command**

.. code-block:: bash

    # Combine command and condition (command must exit with 0)
    if command && [ condition ]; then

**Negate condition**

.. code-block:: bash

    # condition is not True
    if [ ! condition ]; then
    ...

All conditions must be matches

.. _bash_string_comparisons:

String Comparisons
``````````````````
+--------------+----------------------------------------------+
| Operator     | True if ...                                  |
+==============+==============================================+
| str1 = str2  | str1 matches str2                            |
+--------------+----------------------------------------------+
| str1 != str2 | str1 does not match str2                     |
+--------------+----------------------------------------------+
| str1 < str2  | str1 is less than str2                       |
+--------------+----------------------------------------------+
| str1 > str2  | str1 is greater than str2                    |
+--------------+----------------------------------------------+
| -n str1      | str1 is not null (has length greater than 0) |
+--------------+----------------------------------------------+
| -z str1      | str1 is not null (has length 0)              |
+--------------+----------------------------------------------+

File attribute checking
```````````````````````
+---------------------+--------------------------------------------+
| Operator            | True if ...                                |
+=====================+============================================+
| -a *file*           | *file* exists                              |
+---------------------+--------------------------------------------+
| -d *file*           | *file* exists and is a directory           |
+---------------------+--------------------------------------------+
| -e *file*           | *file* exists; same as -a                  |
+---------------------+--------------------------------------------+
| -f *file*           | *file* exists and is a regular *file* \*   |
+---------------------+--------------------------------------------+
| -r *file*           | you have read permission on *file*         |
+---------------------+--------------------------------------------+
| -s *file*           | *file* exists and is not empty             |
+---------------------+--------------------------------------------+
| -w *file*           | you have write permissions on *file*       |
+---------------------+--------------------------------------------+
| -x *file*           | you have execution permission on *file*    |
+---------------------+--------------------------------------------+
| -N *file*           | *file* was modified since it was last read |
+---------------------+--------------------------------------------+
| -O *file*           | you own *file*                             |
+---------------------+--------------------------------------------+
| -G *file*           | *file*'s group IP matches yours \*\*       |
+---------------------+--------------------------------------------+
| *file1* -nt *file2* | *file1* is newer than *file2*              |
+---------------------+--------------------------------------------+
| *file1* -ot *file2* | *file1* is older than *file2*              |
+---------------------+--------------------------------------------+

| \* no directory or other special type of file
| \*\* or one of yours, if you are in multiple groups

Integer Conditionals
````````````````````
Comparison of two integer values

+------+-----------------------+
| Test | Comparison            |
+======+=======================+
| -lt  | Less than             |
+------+-----------------------+
| -le  | Less than or equal    |
+------+-----------------------+
| -eq  | Equal                 |
+------+-----------------------+
| -ge  | Greater than or equal |
+------+-----------------------+
| -gt  | Greater than          |
+------+-----------------------+
| -ne  | Not equal             |
+------+-----------------------+

Usage:

.. code-block:: bash

    # greater_10.sh
    if [ $1 -gt  10 ]; then
        echo "Your input is greater than 10"
    else
        echo "Your input is smaller than or equals 10"
    fi

    # Running...
    ./greater_10.sh 20
    # Your input is greater than 10
    ./greater_10.sh 2
    # Your input is smaller than or equals 10

for
'''
The *for* loop is **not** suited to execute a command for a fixed amount of times,
but rather execute over a list a arguments (like a set of files):

.. code-block:: bash

    # execute for each member of list -> $name
    for name [in list]
    do
        statements tha can use $name
    done

If ``[in list]`` is omitted, the list defaults to ``$@`` (all command line arguments),
but for readability, it should always be provided.

**Example:** Print info of all directories in the *PATH* variable

.. code-block:: bash

    # Set the IFS (Internal Field Separator) to colon (as used by PATH)
    IFS=:

    for dir in $PATH
    do
        ls -ld $dir
    done

**Example**: Print all positional arguments

.. code-block:: bash

    for filename in "$@"; do
        echo "$filename"
    done

case
''''
Used to test a variable's value and execute specific statements depending on the value.

.. code-block:: bash

    case expression in
        pattern1 )
            statements ;;
        pattern2 )
            statements ;;
        ...
        esac

The ``esac`` statement end a *case* block (it actually *case* backwards).

**Example:** Case differentiates file suffix

.. code-block:: bash

    for filename in "$@"; do
        pnmfile=${filename%.*}.ppm

        case $filename in
            *.jpg ) exit 0 ;;
            *.tga ) tgatoppm $filename > $pnmfile ;;
            *.gif ) giftopnm $filename > $pnmfile ;;
                * ) echo "procfile: $filename is an unknown graphic file."
                    exit 1 ;;
        esac
        outfile=${pnmfile%.ppm}.new.jpg
        pnmtojpeg $pnmfile > $outfile
        rm $pnmfile
    done

The ``* )`` case matches everything, but is only executed, if no other case
matched before.

**Example:** Checking the amount of arguments

.. code-block:: bash

    case "$#" in
        0 | 1)  echo "Zero or one argument ;;
        2    )  echo "Two arguments" ;;
        *    )  echo "More than two arguments" ;;
    esac

Multiple values can be combined via ``|``.

While & until
'''''''''''''
Allow code to run repetitively until a condition becomes True.

The *while* syntax:

.. code-block:: bash

    while [ condition ]; do
        statements
    done

The ``condition`` is actually a *list of statements* of which the last statement's
return value is used as the value of the condition.

These are the same:

.. code-block:: bash

    # loop while condition is True
    while [ condition ]; do

    # loop until condition becomes False, behavior as with upper while example
    until [ ! condition ]; do

So ``until`` is not used a lot. A use case for ``until`` can be to execute a
failing command until it succeeds:

.. code-block:: bash

    until commmand; do
        statements
    done


**Example**: Loop through all *PATH* variable entries

.. code-block:: bash

    path=$PATH  # make copy of PATH and append colon at the end
                # all entries are separated by colon

    while [ $path ]; do        # loop until path is empty ("")
        ls -ld ${path%%:*}     # remove colon at the end of $path
        path=${path#*:}        # remove current $path from path (colon-separated)
    done

**Example**: Copy file until succeeds

.. code-block:: bash

    until cp $1 $2; do
        echo 'Attempt to copy failed. waiting...'
        sleep 5
    done

Command Line Options & Typed Variables
--------------------------------------
Command Line Options
--------------------
shift
'''''
The ``shift`` command shifts the argument index by as many times as defined.
For example, ``shift 3`` leads to ``1=$4, 2=$5, ...``, meaning $1 references the
fourth positional argument, $2 the fifth and so on. The original first three
arguments are shifted out of scope.

This allows for putting command line options **before** the positional arguments.
It only allows for separate, uniform arguments (e.g. single dash).

**Example:** Single option (-o) script

.. code-block:: bash

    # my_script.sh
    if [ $1 = -o ]; then
        shift
        echo "We have an option: $1"
        # process the -o option
    fi
    echo "First positional argument: $2"
    # normal processing of arguments

    # ./my_script.sh -o "foo" "bar"
    # We have an option: foo
    # First positional argument: bar

``shift`` without any integer number is a shift of 1 index position.

**Example:** Multiple options

.. code-block:: bash

    while [ -n "$(echo $1 | grep '-')" ]; do
        case $1 in
            -a) process option -a ;;
            -b) process option -b ;;
            -c) process option -c ;;
            * ) echo 'Usage: alice [-a] [-b] [-c] args...'
                exit 1
        esac
        shift
    done
    # normal processing of arguments

**Example**: Multiple options + options with arguments

.. code-block:: bash

    while [ -n "$(echo $1 | grep '-')" ]; do
        case $1 in
            -a) process option -a ;;
            -b) process option -b ;;
                # $2 is the option's argument
                shift ;;
            -c) process option -c ;;
            * ) echo 'Usage: alice [-a] [-b] [-c] args...'
                exit 1
        esac
        shift
    done
    # normal processing of arguments

As the ``-b`` option has a argument, like ``-b debug``, before proceeding to the
next option (-c), another shift must happen.

getopts
'''''''
The ``getopts`` command allows for

* combined options (e.g. ``-abc``, instead of ``-a -b -c``)
* option without space in between its argument (e.g. ``-barg`` instead of ``-b arg``)

``getopts`` takes two arguments:

* the first is a string which can contain letters and colon. A letter is a valid option,
  a colon means, the preceding option requires an argument.
* the second is a variable name to which each option letter is assigned to (without the dash)

.. code-block:: bash
    :linenos:

        # getopts_simple.sh
        while getopts ":ab:c" opt; do
            case $opt in
                a  ) echo "processing -a" ;;
                b  ) echo "processing -b"
                     echo "$OPTIND is the option index"
                     echo "$opt is the option"
                     echo "$OPTARG is the option's argument" ;;
                c  ) echo "processing -c" ;;
                \? ) echo "usage: getopts_simple.sh [-a] [-b barg] [-c] args..."
                     exit 1
            esac
        done
        shift $(($OPTIND - 1))
        # normal processing of arguments...

        # ./getopts_simple.sh -a -b "foo" -c
        # 2: processing -a
        # 4: processing -b
        # 4 is the option index
        # b is the option
        # foo is the option's argument
        # 5: processing -c

:Line 2:    The first colon (``:``) in ``":ab:c"`` prevents getopts to print errors
            in case an illegal option is provided. The ``-a``, ``-b`` and ``-c``
            options are accepted, while ``-b`` takes an argument (``b:``)
:Line 8:    ``$OPTARG`` ... The argument value of the currently selected option
:Line 14:   ``$OPTIND`` ... The index of the **next** command-line argument to be
            processed. After ``getopts`` is done, it equals the number of the first
            "real" argument. It is initialized with **1** and *getopts* increments
            it by 1 at the start of processing the next option.
:Line 15:   The expression ``shift $(($OPTIND - 1))`` shifts the index to the
            regular arguments (like ``$1`` or ``$2``) ->
            :ref:`arithmetic operations <bash_arithmetic_operations>`

* ``getopts`` does not rely on ``shift`` statements to know where it is


Typed Variables
---------------
The built-in ``declare`` command defines variables for this session or script.
It features the following options:

+--------+---------------------------------------------------+
| Option | Meaning                                           |
+========+===================================================+
| -a     | The variables are treated as arrays               |
+--------+---------------------------------------------------+
| -f     | Use function names only                           |
+--------+---------------------------------------------------+
| -F     | Display function names without definitions        |
+--------+---------------------------------------------------+
| -i     | The variables are treated as integers             |
+--------+---------------------------------------------------+
| -f     | Make the variables as read-only                   |
+--------+---------------------------------------------------+
| -x     | Mark the variables for export via the environment |
+--------+---------------------------------------------------+

Running ``declare`` without any options prints all variables within this environment.
The command syntax:

.. code-block:: bash

    declare <option> <variableA=valueA> <variableB=valueB> ...

.. _bash_arithmetic_operations:

Integer Variables and Arithmetic
--------------------------------
* Arithmetic operations are enclosed in ``$((...))``
* Variables within arithmetic operations don't require but can have a preceding dollar sign
* Inside double-quotes arithmetic operations are evaluated

Arithmetic operators:

+----------+---------------------------------------+
| Operator | Meaning                               |
+==========+=======================================+
| ++       | Increment by one (prefix and postfix) |
+----------+---------------------------------------+
| --       | Decrement by one (prefix and postfix) |
+----------+---------------------------------------+
| \+       | Plus                                  |
+----------+---------------------------------------+
| \-       | Minus                                 |
+----------+---------------------------------------+
| \*       | Multiplication                        |
+----------+---------------------------------------+
| /        | Division (with truncation)            |
+----------+---------------------------------------+
| %        | Remainder                             |
+----------+---------------------------------------+
| \*\*     | Exponentiation                        |
+----------+---------------------------------------+
| <<       | Bit-shift left                        |
+----------+---------------------------------------+
| >>       | Bit-shift right                       |
+----------+---------------------------------------+
| &        | Bitwise and                           |
+----------+---------------------------------------+
| \|       | Bitwise or                            |
+----------+---------------------------------------+
| ~        | Bitwise not                           |
+----------+---------------------------------------+
| !        | Logical not                           |
+----------+---------------------------------------+
| ^        | Bitwise exclusive or                  |
+----------+---------------------------------------+
| ,        | Sequential evaluation                 |
+----------+---------------------------------------+

Relational operators:

+----------+--------------------------+
| Operator | Meaning                  |
+==========+==========================+
| <        | Less than                |
+----------+--------------------------+
| >        | Greater than             |
+----------+--------------------------+
| <=       | Less than or equal to    |
+----------+--------------------------+
| >=       | Greater than or equal to |
+----------+--------------------------+
| ==       | Equal to                 |
+----------+--------------------------+
| !=       | Not equal to             |
+----------+--------------------------+
| &&       | Logical and              |
+----------+--------------------------+
| \|\|     | Logical or               |
+----------+--------------------------+

Arithmetic Conditional
''''''''''''''''''''''
Testing of numerical values via operators (similar to
:ref:`string comparisons <bash_string_comparisons>`):

+----------+--------------------------+
| Operator | Meaning                  |
+==========+==========================+
| -lt      | Less than                |
+----------+--------------------------+
| -gt      | Greater than             |
+----------+--------------------------+
| -le      | Less than or equal to    |
+----------+--------------------------+
| -ge      | Greater than or equal to |
+----------+--------------------------+
| -eq      | Equal to                 |
+----------+--------------------------+
| -ne      | Not equal to             |
+----------+--------------------------+

Example:

.. code-block:: bash

    if [ 3 -gt 2 ]; then ...
    [ \( 3 -gt 2 \) || \( 4 -le 1 \) ]

Arithmetic Variables and Assignment
'''''''''''''''''''''''''''''''''''

continue learning the bash shell page 150

