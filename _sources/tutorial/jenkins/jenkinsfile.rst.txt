Learn to write Jenkinsfile
==========================
A Jenkinsfile defines all steps of a pipeline, while also handling variables and
defining functions to be called from within step definitions. It is written in
`Groovy`_ syntax.

.. _Groovy: https://www.groovy-lang.org/documentation.html

A basic pipeline
----------------
A basic structure of a Jenkinsfile using a *declarative pipeline* may look like this:

.. code-block:: groovy

    final String PRODUCT_CHOICES = [
        "CNTTS",
        "CNTTS-VVT"
    ].join("\n")

    final def PRODUCT_CHOICES_TO_SUFFIX_MAP = [
        "CNTTS": "cntts",
        "CNTTS-VVT": "vvt"
    ]

    pipeline {
        agent {
            label 'linux-jenkins'
        }

        options {
            timeout(time: 10, unit 'MINUTES')
            timestamps()
        }

        parameters {
            choice(
                name: 'PRODUCT',
                choices: "${PRODUCT_CHOICES}",
                description: "Product to be built."
            )
        }

        environment {
            ...
        }

        stages {
            ...
        }
    }

The ``agent`` section defines a node, a machine running a Jenkins agent, which in
this case must carry the *label* ``linux-jenkins``. If there are multiple matching
agents available, any of them is chosen.

The `options`_ section defines job options, such as the timeout.

The `parameters`_ section define job parameters that are defined before running the job.
Parameters defined here, are automatically moved into the *parameter* screen (where
the values can be adjusted before starting the build), after running the job at least once
(and not failing before the first stage, that is).
As shown above, variables can be defined and used as default values or choices for
build parameters.

The `environment`_ section allows for defining environment variables, only existing
within the scope of the file. Example:

.. code-block:: groovy

    environment {
        REPO_URL = "https://aac-srv-bitbucket-coretech.cerence.net/scm/trng21/cerence_neural_tts.git"
        NTTS_PRODUCT_PREFIX_SUFFIX = PRODUCT_CHOICES_TO_SUFFIX_MAP.get(params.PRODUCT_CHOICES)
    }

The `stages`_ section expects one or more ``stage`` sections. Those are made up of
one or more``steps`` sections. Example:

.. code-block:: groovy

    stages {
        stage('Do something meaningful') {
            steps {
                ...
            }
        }
    }

The `steps`_ section contains any allowed type of steps (see https://www.jenkins.io/doc/pipeline/steps/).
To point out a few:

* ``script``: allows to define scripted pipeline, which is Groovy code. It allows for
  running shell scripts via the `sh`_ (via the Pipeline Plugin). Example:

    .. code-block:: groovy

        steps {
            script {
                sh '''
                    ls -l | grep foo
                    echo "All done"
                '''
            }
        }

.. _options: https://www.jenkins.io/doc/book/pipeline/syntax/#options
.. _parameters: https://www.jenkins.io/doc/book/pipeline/syntax/#parameters
.. _stages: https://www.jenkins.io/doc/book/pipeline/syntax/#matrix-stages
.. _steps: https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-steps
.. _sh: https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#sh-shell-script

Managing & referencing variables
--------------------------------
One of the biggest problems when starting to write Jenkinsfile pipelines is the
handling of variables. To keep things flexible, variables are defined and referenced
to avoid having to change them at multiple places.

Global variables
````````````````
Globally available variables are accessible via the ``env`` global variable.
Some are already available (check <JENKINS_URL>/pipeline-syntax/globals#env for details),
the *env* variable is recommended to clearly see that it is a global variable, but
can also be omitted:

.. code-block:: groovy

    steps {
        script {
            echo ${env.BUILD_NUMBER}
            echo ${BUILD_NUMBER}
        }
    }

They also can be added to each individual Jenkins node, via
:menuselection:`Dashboard --> Computers --> <NODE> --> Configure` and checking
the *Node properties* to have **Environment variables** checked and added as
key-value pairs.

Local variables
```````````````
Local variables are those declared within the Jenkinsfile. This can happen in
the `environment`_ section as a simple declaration:

.. code-block:: groovy

    environment {
        FOO="bar"
    }

or within the `script`_ section:

.. code-block:: groovy

    steps {
        scripts {
            env.FOO = "bar"
        }
    }

Another way is to define local variables at the top of the file. Those can then
be accessed in any pipeline step:

.. code-block:: groovy

    final String CREDENTIAL_KEY = 'tts_rd_jenkins'

    pipeline {
    ...
        steps {
            script {
                checkout(some_url, some_branch, user: "${CREDENTIAL_KEY}")
            }
        }
    }

Referencing variables
`````````````````````
Depending on where and how variables are declared and from where in the Jenkinsfile
they are referenced, the syntax is slightly varying, but can cause a lot of confusion.
This reference is supposed to make it simple (this applies to string values):

.. csv-table::
    :file: _file/reference_variables_matrix.csv
    :widths: 10, 10, 10, 10, 10
    :header-rows: 1

Deviating from this syntax often lead to empty value (''), ``null`` values or
a *bad substitution* error report by the shell.

.. _environment: https://www.jenkins.io/doc/book/pipeline/syntax/#environment
.. _script: https://www.jenkins.io/doc/book/pipeline/syntax/#script

Further documentation
---------------------
* https://www.jenkins.io/doc/book/pipeline/syntax/
* https://phoenixnap.com/kb/jenkins-environment-variables