Unit testing :footcite:p:`kruk22_nachkontrolle`
===============================================

.. hint::

    **Update Bash on macOS** :footcite:p:`weibel_upgradebash`

    Make sure to use a recent version of bash (for example, the executable
    :bash:`readarray` is not available on older versions. Since **macOS** contains
    a very old version of bash (3.2 from 2007) due to a licensing change and
    might drop bash entirely in the future, install it manually:

    .. code-block:: bash

        $ brew install bash

    When calling bash, the new version is now called. Also add the new bash to your
    list of trusted shells. Run

    .. code-block:: bash

        $ sudo nano /etc/shells

    and add ``/usr/local/bin/bash`` to the list.

    **Important**: In case your bash scripts use a shebang line, change it to

    .. code-block:: bash

        #!/usr/local/bin/bash

Installation
------------
`Spell Check`_ is a Behavior-Driven Development unit testing framework designed
for dash, bash, ksh, zsh and all POSIX shells.

To install it, follow the instructions on https://github.com/shellspec/shellspec#installation.

On macOS, install it via *homebrew*:

.. code-block:: bash

    $ brew tap shellspec/shellspec
    $ brew install shellspec

On Linux, build the binaries from the sources:

.. code-block:: bash

    $ git clone https://github.com/shellspec/shellspec
    $ cd spellcheck
    $ sudo make install

.. _Spell Check: https://github.com/shellspec/shellspec

Define the tests
----------------
Tests are organized in Specfiles. It comprises of one or multiple test groups.
It is advised to use the name of the function a group is supposed to test.

Example:

.. code-block:: bash

    Describe "FunctionUnderTest"
      It "BehaviourUnderTest"
        # test code
      End
    End

Here are the functions, that need to be tested:

.. code-block:: bash

    array_to_lines() {
      local array=("$@")
      if (( ${#array[@]} > 0 )); then
        printf "%s\n" "${array[@]}"
      fi
    }

    array_sort() {
      local array=("$@")
      array_to_lines "${array[@]}" | sort -V
    }

    array_contains() {
      local needle="$1"
      local haystack=("${@:2}")
      local cur
      for cur in "${haystack[@]}"; do
        if [[ "$needle" == "$cur" ]]; then
          return 0
        fi
      done
      return 1
    }

The function :bash:`array_to_lines()` returns a array line by line. The criteria to
test are

* all input elements are also in the output
* the output features the same amount of elements as the input
* if the input array is empty, there must not be any standard output
* the order of the output elements match the ones in the input array

The function :bash:`array_sort()` sorts an array. The criteria are

* no standard output for empty input array
* output must be sorted (no digit-wise sorting, since 1,3,20 would become 1,20,3)
* all input elements are also in the output

The function :bash:`array_contains()` checks if an array contains a certain element.
The criteria are

* elements located at the very first, somewhere in the middle and very last position
  of an array must be found
* no success if reported if element is not found
* if the passed in array is empty, the return value must not be 0

This is the resulting ``.specfile``:

.. code-block:: bash

    Describe "array_to_lines()"
      Pending "Not implemented"

      It "output each element of the input array"
      End
      It "amount of output elements match input array element amount"
      End
      It "don't output anything if input array is empty"
      End
      It "order of elements is not changed"
      End
    End

    Describe "array_sort()"
      Pending "Not implemented"

      It "don't output anything if input array is empty"
      End
      It "each input element is output"
      End
      It "no digit-wise sorting"
      End
    End

    Describe "array_contains()"
      Pending "Not implemented"

      It "find element at the very beginning of array"
      End
      It "find element in the middle of the array"
      End
      It "find element at the very end of the array"
      End
      It "return 1 if element was not found"
      End
      It "return 1 if input array is empty"
      End
    End

:Describe:
    Defines the test group (closed via :bash:`End`)

:It:
    Defines a test case (closed via :bash:`End`)

:Pending:
    Defines that these tests are supposed to be skipped.

Implement the tests
-------------------
The first test case for :bash:`array_to_lines()` cannot be implemented with
*ShellSpec* alone, but requires an additional shell helper function, which is
then called by the framework:

.. code-block:: bash
    :linenos:

    It "output each element of the input array"
      _test_array_to_lines_output_complete() {
        local input
        local output
        local input_element
        input=(
          0 1 2 3 4 5 6 7
          "" " " "-" "--"
          "a" "b" "c" "d"
        )
        ausgabe=()
        readarray -t output < <(array_to_lines "${input[@]}")
        for input_element in "${input[@]}"; do
          local -i is_in_output
          local output_element
          is_in_output=0
            for output_element in "${output[@]}"; do
              if [[ "$input_element" == "$output_element" ]]; then
                is_in_output=1
                break
              fi
            done

            if (( is_in_output == 0 )); then
              return 1
            fi
        done
        return 0
    }
    When call _test_array_to_lines_output_complete
    The status should equal 0
    End

:line 2:
    Definition of helper function.

:line 12:
    Calling `readarray`_ which takes the result of :bash:`array_to_lines "${input[@]}"`
    as input and saves the result into :bash:`output`.

:line 13 - 28:
    Loop through all input elements and compare them with all output elements.
    If it is found return 0 otherwise 1.

:line 30:
    Calls the :bash:`_test_array_to_lines_output_complete` helper function.
    The :bash:`When` directive marks the evaluation procedure.

:line 31:
    The previous call status is checked (if it is not 0 the test fails).
    The :bash:`The` directive marks the expectation.

    .. hint::

        To compare the stdout with a string, use :bash:`stdout should equal "my_string"`.

The next test case, comparing the amount of outputted lines with the amount of
elements in the array, can be implemented without an additional helper method:

.. code-block:: bash

    It "amount of output elements match input array element amount"
      When call array_to_lines 1 2 3 4 5
      The lines of stdout should equal 5
    End

Checking for no output when passing an empty array. It suffices to check for the
return code and skip the check on the non-existing stdout:

.. code-block:: bash

    It "don't output anything if input array is empty"
      When call array_to_lines
      The status should equal 0
    End

To test the order of the output lines, you may use the :bash:`line` directive
of Spell Check:

.. code-block:: bash

    It "order of elements is not changed"
      When call array_to_lines 1 2 3
      The line 1 stdout should equal "1"
      The line 2 stdout should equal "2"
      The line 3 stdout should equal "3"
    End

The first two test cases for :bash:`array_sort()` are implemented similarly (the
'output complete' test requires another helper method like :bash:`_test_array_sort_output_complete`,
see below for implementation).
The third one, checking for non-digit sorting is implemented as follows:

.. code-block:: bash

    It "no digit-wise sorting"
      When call array_sort 20 1 3
      The line 1 of stdout should be equal "1"
      The line 2 of stdout should be equal "3"
      The line 2 of stdout should be equal "20"
    End

Also all test cases needed for :bash:`array_contains()` can be implemented
without helper methods:

.. code-block:: bash

    Describe "array_contains()"
      It "find element at the very beginning of array"
        When call array_contains "1" "1" "2" "3"
        The status should equal 0
      End
      It "find element in the middle of the array"
        When call array_contains "2" "1" "2" "3"
        The status should equal 0
      End
      It "find element at the very end of the array"
        When call array_contains "3" "1" "2" "3"
        The status should equal 0
      End
      It "return 1 if element was not found"
        When call array_contains "0" "1" "2" "3"
        The status should equal 1
      End
      It "return 1 if input array is empty"
        When call array_contains "0"
        The status should equal 1
      End
    End

.. _readarray: https://helpmanual.io/builtin/readarray/

Execute the tests
-----------------
As the methods under test are defined outside of the ``.specfile`` the module
framework including the array module must be loaded into it. As specfiles support
regular shell expressions, an :bash:`include` statement before the first
test group is sufficient. An error handling for that is not required as
Shell-Check will report to us in case of errors:

.. code-block:: bash

    . bms.sh
    include "array"

    Describe "array_to_lines()"
      It "output each element of the input array"
        It "output each element of the input array"
            local input
            local output
            local input_element

            input=(
                0 1 2 3 4 5 6 7
                "" " " "-" "--"
                "a" "b" "c" "d"
            )
            output=()

            readarray -t output < <(array_to_lines "${input[@]}")

            for input_element in "${input[@]}"; do
                local -i is_in_output
                local output_element

                is_in_output=0
                for output_element in "${output[@]}"; do
                    if [[ "$input_element" == "$output_element" ]]; then
                        is_in_output=1
                        break
                    fi
                done

                if (( is_in_output == 0 )); then
                    return 1
                fi
            done

            return 0
        }

        When call _test_array_to_lines_output_complete
        The status should equal 0
      End

      It "amount of output elements match input array element amount"
        When call array_to_lines 1 2 3 4 5
        The lines of stdout should equal 5
      End

      It "don't output anything if input array is empty"
        When call array_to_lines
        The status should equal 0
      End

      It "order of elements is not changed"
        When call array_to_lines 1 2 3
        The line 1 of stdout should equal "1"
        The line 2 of stdout should equal "2"
        The line 3 of stdout should equal "3"
      End
    End

    Describe "array_sort()"
      It "don't output anything if input array is empty"
        When call array_to_lines
        The status should equal 0
      End

      It "each input element is output"
        _test_array_sort_output_complete() {
            local input
            local output
            local input_element

            input=(
                0 1 2 3 4 5 6 7
                "" " " "-" "--"
                "a" "b" "c" "d"
            )
            output=()

            readarray -t output < <(array_sort "${input[@]}")

            for input_element in "${input[@]}"; do
                local -i is_in_output
                local output_element

                is_in_output=0
                for output_element in "${output[@]}"; do
                    if [[ "$input_element" == "$output_element" ]]; then
                        is_in_output=1
                        break
                    fi
                done

                if (( is_in_output == 0 )); then
                    return 1
                fi
            done

            return 0
        }

        When call _test_array_sort_output_complete
        The status should equal 0
      End

      It "no digit-wise sorting"
        When call array_sort 20 1 3
        The line 1 of stdout should equal "1"
        The line 2 of stdout should equal "3"
        The line 3 of stdout should equal "20"
      End
    End

    Describe "array_contains()"
      It "find element at the very beginning of array"
        When call array_contains "1" "1" "2" "3"
        The status should equal 0
      End

      It "find element in the middle of the array"
        When call array_contains "2" "1" "2" "3"
        The status should equal 0
      End

      It "find element at the very end of the array"
        When call array_contains "3" "1" "2" "3"
        The status should equal 0
      End

      It "return 1 if element was not found"
        When call array_contains "0" "1" "2" "3"
        The status should equal 1
      End

      It "return 1 if input array is empty"
        When call array_contains "0"
        The status should equal 1
      End
    End

You may save the upper code in ``array_spec.sh`` and execute it via:

.. code-block:: bash

    $ shellcheck --shell bash --format documentation array_spec.sh

This executes the tests and produces a test run documentation. Lastly, save
the ``array_spec.sh`` under ``/usr/local/share/bms/test/``.

Parameterized Tests
-------------------
Definition
``````````
One advantage of Spell-Check in comparison with other shell test framework (like
`BATS`_) is that is enables us to perform tests with a lot of different inputs.

For this purpose a new :bash:`is` module is created containing these methods:

* :bash:`is_digits()`: checks if string only contains digits
* :bash:`is_upper()`: checks if string only contains upper case characters
* :bash:`is_lower()`: checks if string only contains lower case characters
* :bash:`is_alnum()`: checks if string only contains letters and digits

Create a new file ``/usr/local/share/bms/include/is.sh`` and implements the methods:

.. code-block:: bash
    :linenos:

    is_digit() {
      local str="$1"
      if [[ "$str" =~ ^[0-9]+$ ]]; then
        return 0
      fi
      return 1
    }

    is_upper() {
      local str="$1"
      if [[ "$str" =~ ^[A-Z]+$ ]]; then
        return 0
      fi
      return 1
    }

    is_lower() {
      local str="$1"
      if [[ "$str" =~ ^[a-z]+$ ]]; then
        return 0
      fi
      return 1
    }

    is_alnum() {
      local str="$1"
      if [[ "$str" =~ ^[a-zA-Z0-9]+$ ]]; then
        return 0
      fi
      return 1
    }

:line 3 + 11 + 19 + 27:

    Compare string with a regular expression.
    :bash:`^` and :bash:`$` mark the begin and end of the expression.
    The :bash:`=~` operator defines a regex match operation between a string
    on the left side and a regex on the right side.

The **is** module also requires a constructor (same as array):

.. code-block:: bash

    __init() {
      return 0
    }

Execution
`````````
To create dynamic parameters for tests, the directive :bash:`Parameter:dynamic`
must be set. Before the next, concluding :bash:`End`, values can be defined
using the special method :bash:`%data`. Those

The tests are defined in ``/usr/local/share/bms/include/test/is_spec.sh``:

.. code-block:: bash
    :linenos:

    . bms.sh
    include "is"

    Describe "is_digits()"
      Parameters:dynamic
        for (( i = 32; i < 127; i++ )); do
            c=$(printf "\\x$(printf '%02x' "$i")")
            if (( i >= 48 )) && (( i <= 57 )); then
                %data "accepts '$c'" "$c" 0
            else
                %data "accepts '$c' not" "$c" 1
            fi
        done
      End
      It "$1"
        When call is_digits "$2"
        The status should equal "$3"
      End
    End

:line 7:

    Calculates the hexadecimal value of a decimal input (:bash:`printf '%02x' "$i"`)
    and get the associated ASCII character (:bash:`c=$(printf "\\x<HEX_CODE>"
    for example :bash:`c=$(printf "\\x21"))`).

:line 9 + 11:

    Definition of test positional parameters using the :bash:`%data` special
    function. Here, for either the good case ( 48 <= i <= 57, which are ASCII
    codes for the digits from 0 to 9) and the bad case (i within 32 and 127,
    which are the printable ASCII character and outside of 48 to 57) three
    positional values are passed to the test:

    #. The test case name (for example "accepts 'a'")
    #. The test data value (for example 'a')
    #. The return code to assert against (for example 0)

:line 15 - 18:

    The test which is supposed to use the upper defined values. The passed in
    parameter are called via their position, for example :bash:`$1` for the
    test case name (there is no $0).

The other tests are similar:

.. code-block:: bash

    Describe "is_upper()"
      Parameters:dynamic
        for (( i = 32; i < 127; i++ )); do
            c=$(printf "\\x$(printf '%02x' "$i")")
            if (( i >= 65 )) && (( i <= 90 )); then
                %data "akzeptiert '$c'" "$c" 0
            else
                %data "akzeptiert '$c' nicht" "$c" 1
            fi
        done
      End
      It "$1"
        When call is_upper "$2"
        The status should equal "$3"
      End
    End

    Describe "is_lower()"
      Parameters:dynamic
        for (( i = 32; i < 127; i++ )); do
            c=$(printf "\\x$(printf '%02x' "$i")")
            if (( i >= 97 )) && (( i <= 122 )); then
                %data "akzeptiert '$c'" "$c" 0
            else
                %data "akzeptiert '$c' nicht" "$c" 1
            fi
        done
      End
      It "$1"
        When call is_lower "$2"
        The status should equal "$3"
      End
    End

    Describe "is_alnum()"
      Parameters:dynamic
        for (( i = 32; i < 127; i++ )); do
            c=$(printf "\\x$(printf '%02x' "$i")")
            if (( i >= 48 && i <= 57 )) ||
               (( i >= 65 && i <= 90 )) ||
               (( i >= 97 && i <= 122 )); then
                %data "akzeptiert '$c'" "$c" 0
            else
                %data "akzeptiert '$c' nicht" "$c" 1
            fi
        done
      End
      It "$1"
        When call is_alnum "$2"
        The status should equal "$3"
      End
    End

To execute the tests, again call shellspec:

.. code-block:: bash

    $ shellcheck --shell bash --format documentation is_spec.sh

.. _BATS: https://github.com/bats-core/bats-core

.. footbibliography::
