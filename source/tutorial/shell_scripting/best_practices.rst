Best practices :footcite:p:`kruk22_muschelperlen`
=================================================
Prevent code injection
----------------------
In comparison to Python, Bash scripts are already executed while reading them.
This makes it impossible to change them at runtime. This example demonstrates
a resulting problem:

.. code-block:: bash
    :linenos:

    #!/bin/bash
    echo "This row is only printed once"
    padded=$(printf '%*s' 256 ' ' | cat - "$0")
    echo "$padded" > "$0"

:line 3:

    printf defines a minimum amount of characters to print (256), in this case
    using a wildcard (``%*s``) and passing in spaces (' '). The result is then piped
    into ``cat``, which concatenates the result AKA standard input (meaning of ``-``,
    and the contents of the file (``"$0"``). The result is assigned to the ``padded``
    variable.

:line 4:

    Output of padded content (line 3) is overwrites the script file

Bash scripts are read character by character, bash remembers the current position via
an index. When everything is pushed to a higher index position because of the
proceeding spaces, the current position which bash remembers to be is then not
the same position in the actual script. Because of that, the
bash executes the remaining lines over and over again, resulting in an endless script.

This is a security issue, known as *code injection*, which attackers can use the manipulate
important scripts, for instance in order to gain access rights.

To prevent code injection, put the entire script into a *command group*, which is
then read into the memory all at once:

.. code-block:: bash
    :linenos:

    #!/bin/bash
    {
      echo "This row is only printed once"
      padded=$(printf '%*s' 256 ' ' | cat - "$0")
      echo "$padded" > "$0"
      exit 0
    }

The :bash:`exit 0` at the end guarantees that the script is ended at the end of the
group. Otherwise an attacker could still append content, which is then executed after
the group finishes.

Running script instances cannot be altered, but to prevent any changes to the script
on the files system, prevent other users from editing the file:

.. prompt:: bash

    chmod 755 /path/to/script.sh

Use functions
-------------
Functions are also read in one go, so another possibility is to use a *main* function,
which is called by a short command group. A basic structure:

.. code-block:: bash
    :linenos:

    #!/bin/bash
    main() {
      return 0
    }
    {
      main "$@"
      exit "$?"
    }

:line 6:

    The *main* function is called passing all script arguments (:bash:`"$@"`
    stands for "$1" "$2" ... and so on). See `bash manual`_ for more.

:line 7:

    Script exits with the exit status of the most recently executed foreground
    pipeline (here: 0 from main()).

Mind variable scopes
--------------------
Functions have the advantage of being able to declare local variables.

.. important::

    All variables that are not declared via :bash:`local` or :bash:`declare`
    (without :option:`-g` option) function as global variables.

* Variables passed into functions inherit the scope of the callee
* Global variables can be replaced by equally named local variable
* If a local variable, declared by the callee, is changed within the function, it
  was passed into, the variable of the callee is changed as well

Demonstration:

.. grid:: 2

    .. grid-item::

        .. code-block:: bash
            :linenos:

            #!/bin/bash
            servus_local() {
              local_gruss="Servus"
              moin_local
              echo "[$FUNCNAME] $gruss $USER"
            }
            moin_local() {
              local_gruss="Moin"
              echo "[$FUNCNAME] $gruss $USER"
            }
            servus_dynamic() {
              local_gruss="Servus"
              moin_dynamic
              echo "[$FUNCNAME] $gruss $USER"
            }
            moin_dynamic() {
              gruss="Moin"
              echo "[$FUNCNAME] $gruss $USER"
            }

    .. grid-item::

        .. code-block:: bash
            :linenos:
            :lineno-start: 20

            servus_global() {
              gruss="Servus"
              moin_global
              echo "[$FUNCNAME] $gruss $USER"
            }
            moin_global() {
              gruss="Moin"
              echo "[$FUNCNAME] $gruss $USER"
            }
            main() {
              servus_local
              echo "[$FUNCNAME] $gruss $USER"
              servus_dynamic
              echo "[$FUNCNAME] $gruss $USER"
              servus_global
              echo "[$FUNCNAME] $gruss $USER"
            }
            {
              main "$@"
              exit "$?"
            }

which outputs ($USER = "arnewohletz"):

.. code-block:: none

    [moin_local] Moin arnewohletz
    [servus_local] Servus arnewohletz
    [main]  arnewohletz
    [moin_dynamic] Moin arnewohletz
    [servus_dynamic] Moin arnewohletz
    [main]  arnewohletz
    [moin_global] Moin arnewohletz
    [servus_global] Moin arnewohletz
    [main] Moin arnewohletz

Always declare your variables with :bash:`local` and :bash:`declare` (see
`built-in commands`_).

To enable warning messages for undeclared variables, run your script via the
:option:`-u` option. You may also check your script using the `ShellCheck`_.

Properly name function arguments
--------------------------------
In Bash, function don't have arguments but positional parameters, which are numbered,
but don't have names. When a method uses more than five or more arguments, it is hard
to keep track of the position for each of them.

To overcome this issue, declare all positional parameter as local variable at the
beginnning of each function:

.. code-block:: bash

    send_email() {
      local address="$1"
      local title="$2"
      local message="$3"
    }

Always separate declaration and assignment of variables
-------------------------------------------------------
Be careful not to declare and assign a variable in one line: both actions are
executed sequentially and not in a defined order. For direct assignments, this is
not critical, but it is when the assigned value comes from a subshell:

.. code-block:: bash
    :lineos:

    file_contains() {
      local file="$1"
      local search_pattern="$2"
      local result=$(grep -F "$search_patern" "$file")
      if (( $? != 0 )); then
        # nothing found
        return 1
      fi
      return 0
    }

In line 5, the *$?* variable, the return value of tha previous command (line 4)
does not receive the *grep* return value, but the one from *local*, which is
always 0 except if the command received illegal parameters.

.. _bash manual: https://tiswww.case.edu/php/chet/bash/bashref.html#Special-Parameters
.. _built-in commands: https://www.gnu.org/software/bash/manual/html_node/Bash-Builtins.html
.. _ShellCheck: https://www.shellcheck.net/

.. footbibliography::
