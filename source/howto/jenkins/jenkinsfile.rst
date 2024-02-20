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


Check current status of the pipeline
------------------------------------
In order to check the current status of the pipeline within or in-between stages,
use the following statement:

.. code-block:: groovy

    stage("Do something") {
        steps {
            echo "currentBuild.currentResult: ${currentBuild.currentResult}"
        }
    }

You can also use the status as a conditional for execution of a stage:

.. code-block:: groovy

    stage('Do something if pipeline so far OK') {
        when {
            expression { currentBuild.currentResult == 'SUCCESS' }
        }
        steps {
            // do something
        }
    }

.. note::

    ``currentBuild.result`` returns ``null`` if used inside the `stages <jenkins_sections_stages>`_
    section, but returns the status if used inside the `post <jenkins_sections_post>`_ section.

.. _jenkins_sections_stages: https://www.jenkins.io/doc/book/pipeline/syntax/#stages
.. _jenkins_sections_post: https://www.jenkins.io/doc/book/pipeline/syntax/#post


Print all currently set environmental variables
-----------------------------------------------
In order to see all currently available environmental variables, add this line to the
respective Jenkinsfile position:

.. code-block:: groovy

    script {
        sh 'printenv'
    }

which will output them in the following manner:

.. code-block:: none

    10:19:18  GIT_USERNAME=****
    10:19:18  JENKINS_HOME=/var/jenkins_home
    10:19:18  GIT_COMMITTER_NAME=tts jenkins
    10:19:18  GIT_PREVIOUS_SUCCESSFUL_COMMIT=de8bcce7ba3662eb36dc36d2d822cb3aa9adf3fb
    10:19:18  MAIL=/var/mail/jenkins
    10:19:18  LC_TIME=de_DE.UTF-8
    ...

Each of these variables can be accessed via ${ENVIRONMENT_NAME}, for example:

.. code-block:: groovy

    script {
        echo $GIT_COMMITTER_NAME
    }

Use time trigger as conditional
-------------------------------
In case a certain step is only supposed to happen if a build was started via a
time trigger, there is a conditional step, you can use:

.. code-block:: groovy

    if (env.BUILD_USER == "Timer Trigger") {
        // do something
    }
