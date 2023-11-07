Jenkinsfile
===========
Disable trace messages ("+ some_command") on console output
-----------------------------------------------------------
:Issue:

    When adding *echo* shell commands in a Jenkinsfile, like

    .. code-block:: groovy

        script {
            sh '''
                echo "Hello world"
            '''
        }

    it causes the line to be printed twice, once as a execution trace messages,
    and once as the original *echo* command:

    .. code-block:: none

        + echo Hello world
        Hello world

    whereas we only want to second line to be shown.

:Cause:

    `By default <sh_shell_command_>`_, Jenkins launches shell commands with the ``set -x`` option (see
    `here <set_builtin_>`_ for more info), which causes all commands to be echoed.
    For most commands defined inside the Jenkinsfile, that selection makes sense
    in order to know which command triggered the proceeding console output, but
    for echo it's merely a repetition.

:Solution:

    Deactivate the trace printing by setting ``set +x`` (the "+" switches off
    the option), before executing the *echo* command. In case different commands
    follow in the same shell code block, re-activate it:

    .. code-block:: groovy

        script {
            sh '''
                # ### Deactivate tracing
                { set +x; } 2>/dev/null
                echo "Hello world"
                # ### Re-activate tracing
                { set -x; } 2>/dev/null
                cp some_file /some/dir/
            '''
        }

    This shows the following console output:

    .. code-block:: none

        Hello world
        + cp some_file /some/dir

    In order to not show the *set* commands in the output, put them into curly
    braces assigning their *stderr* output to ``/dev/null``:

    .. code-block::

        { set +x; } 2>/dev/null


.. _set_builtin: https://www.gnu.org/software/bash/manual/html_node/The-Set-Builtin.html
.. _sh_shell_command: https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#sh-shell-script