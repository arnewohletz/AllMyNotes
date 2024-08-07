Code Reusability :footcite:p:`kruk22_scheibchenweise`
=====================================================
Source other modules
--------------------
The `Shell family`_ (to which Bash belongs) doesn't know library, classes or modules.
Dynamically loading code can be done via :bash:`source`, but using

* absolute paths aren't possible since the script location isn't fix
* relative paths aren't possible since those are relative by the current directory,
  not the location of the script file

This :bash:`try_include()` function is passed the module name, then attempts to find
its path and load it via :bash:`source`:

.. code-block:: bash
    :linenos:

    try_include() {
      local mod_name="$1"
      local mod_dir
      local mod_path
      if ! mod_dir=$(realpath "${BASH_SOURCE[0]}"); then
        echo "Cannot resolve ${BASH_SOURCE[0]}" 1>&2
        return 1
      fi
      mod_dir="${mod_dir%/*}"
      mod_path="$mod_dir/include/$mod_name.sh"
      if ! . "$mod_path"; then
        echo "Cannot load $mod_path" 1>&2
        return 1
      fi
      return 0
    }

:line 5:

    :bash:`${BASH_SOURCE[0]}` returns the relative path of the current script file
    towards the present working directory, whereas :bash:`realpath` returns its
    absolute path. If the resulting path cannot be resolved (throws an exit code
    other than 0), the conditional block is executed.

:line 9 + 10:

    The :bash:`mod_dir` is stripped by the final slash and the proceeding filename,
    resulting in the parent directory of the script, which is then expanded by
    :bash:`/include/$mod_name.sh` (where :bash:`$mod_name` is passed into the module).

:line 11:

    The :bash:`.` (`dot command`_) is a short writing for :bash:`source` and attempts
    to load the module file, entering the conditional block in case of an error
    (exit code differs from 0).

Initialize sourced modules
--------------------------
Without an initialization function, the loaded module is executed as if it were
directly written inside :bash:`try_include()`. Bugs in the loaded module will impact
the function. To prevent that, let's define that each module must contain a
constructor method, called :bash:`__init`, which returns 0 in case of success. This
method is then called by :bash:`try_include()`.

In addition, it must be prevented that a module is loaded more than once, since this
would reset any changes done to the module's state. A helper method called :bash:`have()`
is making sure of that.

.. code-block:: bash
    :linenos:

    have() {
      local module="$1"
      if [[ -n "${__BMS_INCLUDED[$module]}" ]]; then
        return 0
      fi
      return 1
    }

:line 3:

    The :bash:`-n` test operator evaluates if the succeeding string is empty
    (can be omitted, :bash:`if [[ "${__BMS_INCLUDED[$module]}" ]]` also suffices).
    :bash:`__BMS_INCLUDED` is a associative array (stores key-value pairs), which
    includes all successfully loaded modules (this will be added to the
    :bash:`try_include()` method)

.. hint::

    BMS stands for *Bash Module System*, the name of the framework.

.. hint::

    There is no rule or effect using double underscores ('__') preceding in
    method or variable names, but it is commonly used across languages to mark
    something as private (in case the language itself does not feature access
    modifiers, like bash).

:bash:`try_include()` is now updated to store successfully loaded modules into the
:bash:`__BMS_INCLUDED` associative array. Also a wrapper method :bash:`include()`,
which enables loading multiple modules in one call is added:

.. grid:: 2

    .. grid-item::

        .. code-block:: bash
            :linenos:

            try_include() {
              local module="$1"
              local mod_path
              local -i err
              if have "$module"; then
                return 0
              fi
              mod_path="$__BMS_PATH/$module.sh"
              if ! . "$mod_path" &>/dev/null; then
                echo "Cannot load $mod_path" 1>&2
                return 1
              fi
              if __init; then
                __BMS_INCLUDED["$module"]="$mod_path"
                err=0
              else
                echo "Cannot initialize $module" 1>&2

    .. grid-item::

        .. code-block:: bash
            :linenos:
            :lineno-start: 18

                err=1
              fi
              unset -f __init
              return "$err"
            }

            include() {
              local modules=("$@")
              local module
              for module in "${modules[@]}"; do
                if ! try_include "$module"; then
                  return 1
                fi
              done
              return 0
            }

:line 4:

    declares a local variables of type integer

:line 5:

    Calls the :bash:`have()` method to verifies if specified module has
    already been located.

:line 13:

    Calling the module's :bash:`__init()` method, on success adding the module
    to :bash:`__BMS_INCLUDED`.

:line 20:

    Remove variable :bash:`__init` (pointing to the module's initialization method)
    to clear reference for the next call on :bash:`try_included()`.

Naturally those global variables used by :bash:`try_included()` must be declared
as well:

.. code-block:: bash
    :linenos:

    __bms_init() {
      local mod_dir
      if ! mod_dir=$(realpath "${BASH_SOURCE[0]}"); then
        echo "Cannot resolve ${BASH_SOURCE[0]}" 1>&2
        return 1
      fi
      mod_dir="${mod_dir%/*}"
      declare -gxr __BMS_PATH="$mod_dir/include"
      declare -Axg __BMS_INCLUDED
      readonly -f have
      readonly -f try_include
      readonly -f include
      return 0
    }

:line 8:

    :bash:`declare -gxr` declares a global (:bash:`-g`) variable, which is
    `exported`_ after initialization (meaning it is available to every subsequent
    command / sub-shell in the environment) via the :bash:`-x` option and is
    read-only (:bash:`-r` option), so it cannot be accidentally overwritten.

:line 9:

    The :bash:`-A` option marks that the name is an associative array.

:line 10 - 12:

    Mark functions as read-only, securing them from subsequent changes.

All these functions are saved to a script (e.g. ``bms.sh``) and a new script is
created, which sources it:

.. code-block:: bash
    :linenos:

    #!/bin/bash

    main() {
      test_hello
      return 0
    }

    {
      if ! . bms.sh; then
        exit 1
      fi
      if ! include "test"; then
        exit 1
      fi
      main "$@"
      exit "$?"
    }

:line 4:

    Calling a function from a test module (included in line 12).

:line 9:

    Attempt to source ``bms.sh``.

:line 12:

    Attempt to source the *test* module using the :bash:`include()` function from
    ``bms.sh``.

Setting up a test module
------------------------
For convenience and general usability the ``bms.sh`` module, it should be placed
somewhere visible to all users, for example at ``/usr/local/share/bms/``, also
featuring an ``include/`` sub-folder.

In order to access the module from any bash script, this new directory needs to be
visible to the :bash:`source` command, hence it needs to be added to the PATH variable.
This can be done by placing a symbolic link:

.. code-block:: bash

    $ ln -s /usr/local/share/bms /usr/local/bin/bms.sh

The test module is now created in ``test.sh``. As previously defined, it must feature
a constructor method :bash:`__init()`:

.. code-block:: bash

    __init() {
      declare -gxr __test_name="$USER"
      return 0
    }

    test_hello() {
      echo "Hello $__test_name"
    }

Same namespace for all modules
------------------------------
In bash all sourced modules share the same namespace, which means that a variable
or method name must be unique across all sourced modules. To avoid such conflicts
when sourcing a new module.

This can be prevented when sticking to a set of rule within a module:

+-------------------+--------------------------------+----------------+
| Element           | Naming Convention              | Example        |
+===================+================================+================+
| module            | lowercase letters and digits   | mod            |
+-------------------+--------------------------------+----------------+
| function          | module_name + "_" + ...        | mod_functionA  |
+-------------------+--------------------------------+----------------+
| internal function | "_" + module_name + "_" + ...  | _mod_helper    |
+-------------------+--------------------------------+----------------+
| global variable   | "__" + module_name + "_" + ... | __mod_variable |
+-------------------+--------------------------------+----------------+

Because bash functions inherit the variables of its callee, by that being able
to change them. To prevent that all local variables must be declare using
:bash:`local` or :bash:`declare`.

Helper functions for arrays
---------------------------
Because arrays are used regularly a helper module to write, search and sort arrays
is useful and save it under ``/usr/local/share/bms/include/array.sh``.

Print array, one line per item
``````````````````````````````
.. code-block:: bash
    :linenos:

    array_to_lines() {
      local array=("$@")
      if (( ${array[@]} > 0 )); then
        printf "%s\n" "${array[@]}"
      fi
    }

:line 2:

    Define an array putting all passed in arguments (:bash:`$@`) into it.

:line 3 + 4:

    :bash:`${array[@]}` expands each member of the array into a separate word,
    separated with a space, for example ("one" "two" "three") -> "one" "two" "three".
    If the array has no members it expands to 0, so the conditional block is entered,
    if the array has any members. Each word is then printed via :bash:`printf`,
    by declaring each value as string followed by a new line (:bash:`"%s\n"`)
    and passing all array words as arguments.

Use :bash:`printf` over :bash:`echo`, because the ladder accepts options, so
something like :bash:`-o` in the array is interpreted as option and won't be printed.
It also saves the declaration of a loop, because :bash:`printf` is able to handle
arrays of various length in one call.

Sort array
``````````
To get the sorted elements of an array, the :bash:`array_to_lines()` function comes in
handy:

.. code-block:: bash
    :linenos:

    array_sort() {
      local array=("$@")
      array_to_lines "${array[@]}" | sort -V"
    }

:line 3:

    As :bash:`array_to_lines` returns a new-line separated list of values, we
    can pipe this directly into :bash:`sort` (the -V option is used to support
    version numbering within the text as well)

Search item in array
````````````````````
The function either returns an exit code 0, if the array contains a match or 1
if it doesn't. Using a :bash:`grep` on the array isn't as performant on longer
arrays as a regular loop is, so :bash:`array_to_lines()` will :ulined:`not` be
utilized here, but the array's elements are compared one by one:

.. code-block:: bash
    :linenos:

    array_contains() {
      local needle="$1"
      local haystack=("${@:2}")
      local cur
      for cur on "${haystack[@]}"; do
        if [[ "$needle" == "$cur" ]]; then
          return 0
        fi
      done
      return 1

:line 3:

    The function expects the first argument to be the term to search for and
    all following arguments to be the array content (:bash:`${@:2}`).

:line 4 + 5:

    Loop over all elements in the array (:bash:`$cur`) and compare it to the
    searched term (:bash:`$needle`).

Add a constructor
`````````````````
Because it is here defined that each module must implement a :bash:`__init()` function,
even though this function isn't used as nothing is required to be initialized by it,
so it only reports success:

.. code-block:: bash

    __init() {
      return 0
    }

Testing the functions
`````````````````````
In order to test each function created in this section, this test script is used:

.. grid:: 2

    .. grid-item::

        .. code-block:: bash
            :linenos:

            #!/bin/bash

            main() {
              local array
              local i
              array=()
              for (( i = 0; i < 5; i++ )); do
                local num
                num=$((RANDOM % 10))
                array+=("$num")
              done
              echo "Unsorted:"
              array_to_lines "${array[@]}"
              echo "Sorted:"
              array_sort "${array[@]}"
              for (( i = 0; i < 3; i++)); do
                local num
                num=$((RANDOM % 10))
                if array_contains "$num" "${array[@]}"; then

    .. grid-item::

        .. code-block:: bash
            :linenos:
            :lineno-start: 20

                  echo "array contains $num"
                else
                  echo "array does not contain $num"
                fi
              done
              return 0
            }

            {
              if ! bms.sh: then
                exit 1
              fi
              if ! include "array"; then
                exit 1
              fi
              main "$@"
              exit "$?"
            }

:line 7 - 11:

    Add five random numbers (integer between 0 and 32767): the double brackets
    in :bash:`num=$((RANDOM % 10))` enable the expression within to contain
    operators such as `%` (modulo) or other `arithmetic expressions`_ as opposed
    to single brackets. Same applies to square brackets as commonly used in
    if-statements (for example :bash:`if [[ i < 10 ]]; then`).

:line 29 - 34:

    Sourcing the two modules ``bms.sh`` and ``array``. The ladder uses the
    :bash:`include()` function from ``bms.sh`` so expects the module name as
    an argument.

Executing the test script produces an output similar to this:

.. code-block:: none

    Unsorted:
    2
    5
    3
    4
    9
    Sorted:
    2
    3
    4
    5
    9
    array contains 3
    array contains 9
    array does not contain 1

.. _Shell family: https://en.wikipedia.org/wiki/Comparison_of_command_shells
.. _dot command: https://en.wikipedia.org/wiki/Dot_(command)
.. _exported: https://www.delftstack.com/howto/linux/export-in-bash/
.. _arithmetic expressions: https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html
.. footbibliography::