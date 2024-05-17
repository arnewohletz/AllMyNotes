An real-life example Jenkinsfile
================================
This How-To shows an example of a Jenkinsfile used in an actual pipeline. It took me
days to finish it (including writing additional script files), so in order to decrease
the pain when writing the next one, I want to document the knowledge I gained while
writing it.

For this purpose, the file is split in smaller sections, which include the literal
content of the file and a detailed explanations of the meaning of each file.

Global variables
----------------
This section defines global variables, which are visible within the entire Jenkinsfile.

.. code-block:: groovy
    :linenos:
    :lineno-start: 1

    @Library('tts_shared') _

    // --------------------------------------------------------------------------------------------------------------------
    //
    // Constants
    //

    final String ARTIFACTORY_SOURCE_REPO = 'tts-release/com/cerence'
    final String CREDENTIAL_KEY = 'tts_rd_jenkins_writer'

    final String PRODUCT_METAPACKAGE_REPO = "cerence_neural_tts"
    final String PRODUCT_METAPACKAGE_REPO_URL = 'https://aac-srv-bitbucket.coretech.cerence.net/scm/trng21/cerence_neural_tts.git'

    final String PRODUCT_CHOICES = [
        "CNTTS",
        "CNTTS-VVT"
    ].join("\n")

    final def PRODUCT_CHOICES_TO_PREFIX_SUFFIX_MAP = [
        "CNTTS": "cntts",
        "CNTTS-VVT": "vvt"
    ]

    // separate multiple email recipients with ';'
    // use the empty string '' to avoid sending email notifications
    final String NOTIFY_ON_FAILURE = 'alberto.pettarin@cerence.com;stefaan.willems@cerence.com;rahul.ranjan@cerence.com'
    final String NOTIFY_ON_SUCCESS = ''

    // --------------------------------------------------------------------------------------------------------------------

:line 1:

    Defines the import of an external library. To be able to import such a library,
    it must be added to the Jenkins installation's configuration, where it can be
    retrieved from an SCM (such as a git repository, where it is kept) and a name
    is defined (here: *tts_shared*) under which is can be imported.

    See `External Libraries`_ for further information.

.. _External Libraries: https://www.jenkins.io/doc/book/pipeline/shared-libraries/

:line 8 - 12:

    Definition of constant values, which are available for the entire Jenkinsfile.
    As the Jenkinsfile follows the Groovy syntax (which itself derives from the Java syntax),
    variables at the top-level must be declared in the following manner:

    .. code-block:: groovy

        final String VARIABLE_NAME = "some_value"

    The ``final`` keyword defines, that this variable a constant.

    The ``String`` keyword defines the type as String. Using the ``def`` keyword
    defines a variable without a type, which is defined at runtime.

    All basic types: https://pledbrook.github.io/groovy-cheat-sheet/guide/index.html#_type_list

:line 14-17:

    This definition defines String which consists of an array of strings, which is
    joined into a single string with a new-line character as delimiter (``join("\n"``).
    This is a possible format needed to define the *choices* within the *choice*
    `parameter <jenkinsfile_parameters_>`_, where all values must be separated via a
    new line character.

.. _jenkinsfile_choice: https://www.jenkins.io/doc/book/pipeline/syntax/#available-parameters

:line 19-22:

    The definition of a `map <groovy_map_>`_, which contains two key-value pairs. The value
    of a key can be accessed via the get method (see https://docs.groovy-lang.org/latest/html/groovy-jdk/).

.. _groovy_map: https://docs.groovy-lang.org/latest/html/documentation/core-syntax.html#_maps

Agent, Parameters and Options
-----------------------------
The `agent <jenkinsfile_agent_>`_, `parameter <jenkinsfile_parameters_>`_ and
`options <jenkinsfile_options_>`_ sections are defined inside the
`pipeline <jenkinsfile_pipeline_>`_ section. They could also be defined in the
Jenkins job configuration itself, but defining them inside the Jenkinsfile is a
good practice, as changed are tracked and the Jenkinsfile can be applied to various
pipeline jobs more easily.

.. code-block:: groovy
    :linenos:
    :lineno-start: 31

    pipeline {

        agent {
            label 'ci-cntts-test'
        }

        parameters {
            choice(
                name: 'PRODUCT',
                choices: "${PRODUCT_CHOICES}",
                description: 'Product, whose product meta-package is promoted and uploaded to AF'
            )
            string(
                name: 'SUBTASK_ID',
                defaultValue: 'READER-XXXX',
                description: 'Jira sub-task, which covers this release\'s promotion of the product metapackage (e.g. READER-1234)'
            )
            gitParameter(
                branch: '',
                branchFilter: 'origin/release/.*',
                defaultValue: '',
                description: 'Release branch (in cerence_neural_tts repo) to get development metapackage version from (default: NONE).',
                name: 'PRODUCT_METAPACKAGE_REPO_CHECKOUT_SOURCE',
                quickFilterEnabled: true,
                selectedValue: 'DEFAULT',
                sortMode: 'ASCENDING',
                type: 'PT_BRANCH',
                useRepository: "${PRODUCT_METAPACKAGE_REPO_URL}",
                listSize: '10'
            )
        }

        options {
            timeout(time: 5, unit: 'MINUTES')
            timestamps()
        }

:line 31:

    The `pipeline <jenkinsfile_declarative_pipeline_>`_ section starts a *declarative pipeline*.
    Jenkins supports two types of pipelines:

        * declarative pipelines
        * `scripted pipelines <jenkins_scripted_pipelines_>`_

    A declarative pipeline may contain scripted sections, which are equal to *scripted pipelines*.
    Declarative pipelines, though, have additional features (like restarting a
    pipelines from stage), but have limits in terms of what can be declared at which point.

:line 33-35:

    An `agent <jenkinsfile_agent_>`_, running on a Jenkins node, is defined via it's label.
    During runtime, an agent, which has this label associated to it, is selected
    as the node, to run this pipeline on. If multiple agent have that same label,
    Jenkins selects one of them (preferably one, which currently does not execute any
    job, or which has the shorted queue).

:line 37-61:

    Declaration of the job's input `parameter <jenkinsfile_parameters_>`_. The *parameter*
    sections expect any available parameter, namely

        * *string*: a single line string
        * *text*: a single or multiline string
        * *booleanParam*: accepts ``true`` or ``false``

            It may be used to not run certain *stages*, if the parameter is set to *false*:

            .. code-block:: groovy

                parameters {
                    booleanParam(
                        name: 'DO_SOMETHING',
                        defaultValue: false,
                        description: 'Select me, if you want to do something'
                }

                stage('Do something if not skipped') {
                    when {
                        expression { params.DO_SOMETHING == true }
                    }
                    steps {
                        // ... do something

            In the Jenkins web UI's job configuration, the parameter is a checkbox,
            where unchecked translates to ``false`` and checked to ``true``.

        * *choice*: a drop-down list of predefined choices
        * *password*: a password string (designed for secrets, as it won't be
          printed in the log output)

    All parameter values can be accessed further down the Jenkinsfile via
    ``${params.PARAMETER_NAME}``.

    Alternatively, parameters can be defined in a *properties* section. For this example:

    .. code-block:: groovy

        properties([
            parameters([
                choice(
                    name: 'PRODUCT',
                    // ... other parameter settings
                ),
                string(
                    name: 'SUBTASK_ID',
                    // ... other parameter settings
                ),
                gitParameter(
                    branch: '',
                    // ... other parameter settings
                )
            ])
        ])

        pipeline {
            // all other pipeline sections
        }

    :line 48-60:

        The `Git Parameter <jenkins_gitparameter_>`_ plugin provides a *gitParameter* directive,
        which allows for assigning a git branch (used here), tag, pull request or a revision
        number as a build parameter.

        In this case, the user is asked to select a branch (only branches matching
        the *branchFilter* expression are available) from the ``"${PRODUCT_METAPACKAGE_REPO_URL}"``
        repository (defined as global variable in line 12) and assigns the selection
        to the *PRODUCT_METAPACKAGE_REPO_CHECKOUT_SOURCE* parameter variable.

:line 63-66:

    Pipeline options may be declared in the `options <jenkinsfile_options_>`_ section.
    A variety of options are available. Here, a ``timeout`` of five minutes is declared,
    which automatically fails the pipeline, if it hasn't completed within that timeframe.
    The ``timestamps()`` option prepends all console outputs with a timestamp.


.. _jenkins_gitparameter: https://plugins.jenkins.io/git-parameter/
.. _jenkins_scripted_pipelines: https://www.jenkins.io/doc/book/pipeline/syntax/#scripted-pipeline
.. _jenkinsfile_agent: https://www.jenkins.io/doc/book/pipeline/syntax/#agent
.. _jenkinsfile_declarative_pipeline: https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-pipeline
.. _jenkinsfile_options: https://www.jenkins.io/doc/book/pipeline/syntax/#options
.. _jenkinsfile_parameters: https://www.jenkins.io/doc/book/pipeline/syntax/#parameters
.. _jenkinsfile_pipeline: https://www.jenkins.io/doc/book/pipeline/syntax/#declarative-pipeline

Stage - Checkout a git branch
-----------------------------
Pipelines are divided into *stages*. Unless defined as `parallel <jenkinsfile_parallel_>`_,
all stages are executed in the specified order.

.. code-block:: groovy
    :linenos:
    :lineno-start: 68

    stages {
        stage('Checkout product repo release branch') {
            steps {
                script {
                    sh 'echo Checkout repository'
                    checkout([$class: 'GitSCM',
                        branches: [[name: "${params.PRODUCT_METAPACKAGE_REPO_CHECKOUT_SOURCE}" ]],
                        extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: "${PRODUCT_METAPACKAGE_REPO}"]],
                        userRemoteConfigs: [[
                            url: "${PRODUCT_METAPACKAGE_REPO_URL}",
                            credentialsId: "${CREDENTIAL_KEY}"
                        ]]
                    ])
                }
            }
        }

:line 68:

    Start the `stages <jenkinsfile_stages_>`_ section. It must contain at least one
    `stage <jenkinsfile_stage_>`_ directive.

:line 70-82:

    Definition of a `stage <jenkinsfile_stage_>`_. It contains a `steps <jenkinsfile_steps_>`_
    section, which contains additional step directives defined in the `Jenkins Steps Reference <jenkinsfile_steps_>`_.
    It may also contain a `script <jenkinsfile_script_>`_ section, which contains a block
    of `scripted pipeline <jenkins_scripted_pipelines_>`_, which allows for execution
    of a more complex series of steps.

    In this case, it contains a *script* section. It first executes a `sh <jenkinsfile_sh_>`_
    command, which opens executes the shell script, in this case ``echo Checkout repository``.
    The `checkout <jenkinsfile_checkout_>`_ checks out the sources of another git repository,
    specified via the URL ``${PRODUCT_METAPACKAGE_REPO_URL}``, wheras the specific branch
    ${params.PRODUCT_METAPACKAGE_REPO_CHECKOUT_SOURCE} is checked out (note that git
    checkout is done via the `Git plugin <jenkins_gitplugin_>`_).

.. _jenkinsfile_parallel: https://www.jenkins.io/doc/book/pipeline/syntax/#parallel
.. _jenkinsfile_stages: https://www.jenkins.io/doc/book/pipeline/syntax/#stages
.. _jenkinsfile_stage: https://www.jenkins.io/doc/book/pipeline/syntax/#stage
.. _jenkinsfile_steps: https://www.jenkins.io/doc/pipeline/steps/
.. _jenkinsfile_script: https://www.jenkins.io/doc/book/pipeline/syntax/#script
.. _jenkinsfile_sh: https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#sh-shell-script
.. _jenkinsfile_checkout: https://www.jenkins.io/doc/pipeline/steps/workflow-scm-step/#checkout-check-out-from-version-control
.. _jenkins_gitplugin: https://plugins.jenkins.io/git/


Step - Configure environment variables
--------------------------------------
Pipelines may require some job or run-specific environment variables to be defined.
If those are few and simple or already known at the very beginning of the pipeline,
those can also be defined inside a `environment <jenkinsfile_environment_>`_ directive,
either at the above of the *stages* section or individual *stage* section (in case, those
will only be needed for this single step).

As the definition becomes more complex or certain parameters are only known until
checking out additional sources (as in our case), an extra *stage*, which globally
defines those variables, becomes necessary. Note, that here, each environment variable
must be added to the `env <jenkinsfile_env_>`_ object. Variables defined in the
*environment* sections are automatically added to the *env* object.

    .. code-block:: groovy
        :linenos:
        :lineno-start: 84

        stage("Configure environment variables") {
            steps {
                script {
                    // Input validation
                    if (!(params.SUBTASK_ID =~ /READER-\d+/)) {
                        currentBuild.result = 'ABORTED'
                        error "The entered SUBTASK_ID must match READER-[0-9]+ (e.g. READER-1234)"
                    }

                    // Product variables
                    env.NTTS_PRODUCT_PREFIX_SUFFIX = PRODUCT_CHOICES_TO_PREFIX_SUFFIX_MAP.get(params.PRODUCT)

                    env.CURRENT_METAPACKAGE_VERSION = sh(script: """
                        cd ${WORKSPACE}/${PRODUCT_METAPACKAGE_REPO}/meta/${NTTS_PRODUCT_PREFIX_SUFFIX};
                        python3 -c "from src.neuraltts.products.${NTTS_PRODUCT_PREFIX_SUFFIX}.__version__ import __version__;print(__version__)"
                        """, returnStdout: true)

                    env.CURRENT_PRODUCT_VERSION = sh(script: """yq '.product.version' $WORKSPACE/$PRODUCT_METAPACKAGE_REPO/docker/"$NTTS_PRODUCT_PREFIX_SUFFIX"_build_deps.yaml""", returnStdout: true)
                    if (env.CURRENT_METAPACKAGE_VERSION != env.CURRENT_PRODUCT_VERSION) {
                        currentBuild.result = 'ABORTED'
                        error "The product version (${env.CURRENT_PRODUCT_VERSION}) and product metapackage version (${env.CURRENT_METAPACKAGE_VERSION}) are not identical. Make sure both versions match and then retry."""
                    }
                    if (!env.CURRENT_METAPACKAGE_VERSION.contains('dev')) {
                        currentBuild.result = 'ABORTED'
                        error "This release branch ($PRODUCT_METAPACKAGE_REPO_CHECKOUT_SOURCE) already uses a promoted (non-dev) metapackage version for ${env.PRODUCT}: ${env.CURRENT_METAPACKAGE_VERSION}. Pipeline run was aborted."
                    }

                    env.PROMOTED_METAPACKAGE_VERSION = "$CURRENT_METAPACKAGE_VERSION".replace('.dev', '').trim()

                    // Paths
                    env.MAKEFILE_DIR = "${WORKSPACE}/pipelines/common/promote_product_metapackage"
                    env.METAPACKAGE_SETUP_PY_FILE_PATH = "${WORKSPACE}/${PRODUCT_METAPACKAGE_REPO}/meta/${env.NTTS_PRODUCT_PREFIX_SUFFIX}/setup.py"
                    env.METAPACKAGE_VERSION_FILE_PATH ="${WORKSPACE}/${PRODUCT_METAPACKAGE_REPO}/meta/${env.NTTS_PRODUCT_PREFIX_SUFFIX}/src/neuraltts/products/${env.NTTS_PRODUCT_PREFIX_SUFFIX}/__version__.py"
                    env.PRODUCT_DESCRIPTORS_DIR_PATH = "${WORKSPACE}/${PRODUCT_METAPACKAGE_REPO}/docker"

                    // Git branches
                    env.PROMOTION_RELEASE_BRANCH_LOCAL = "$PRODUCT_METAPACKAGE_REPO_CHECKOUT_SOURCE".replaceFirst("origin/", "")
                    env.PROMOTION_PULL_REQUEST_BRANCH_LOCAL = "feature/${params.SUBTASK_ID}_promote_product_metapackage_${params.PRODUCT}_" + "$PROMOTED_METAPACKAGE_VERSION".replace('.', '-')
                }
            }
        }


:line 94:

    Defines the *PRODUCT* build parameter to the *NTTS_PRODUCT_PREFIX_SUFFIX* environment variables,
    by retrieving the associated value from the *PRODUCT_CHOICES_TO_PREFIX_SUFFIX_MAP*. The `get() <java_map_get_>`_
    method returns the value of the given key (*params.PRODUCT*). It is a method provided by the
    Java layer, which Groovy builds upon. The type of the *PRODUCT_CHOICES_TO_PREFIX_SUFFIX_MAP*
    variable was not declared (using the ``def`` type), but assigned to the Map interface
    implementation during runtime.

:line 96-99:

    Defines the output of a shell script (`sh <jenkinsfile_sh_>`_) as the value of environment variable.
    The script itself must a string value assigned to the ``script`` option. If the string starts
    with triple single quotes (``'''``), the script allows for multiple lines without using line continuation
    (this is a requirement from Groovy). The same applies to using triple double-quotes (``"""``).

    For both, global or environmental variables put inside ``${...}`` are interpolated by their value.

    The ``returnStdout: true`` ensure, that the standard output value is returned and, in this case,
    assigned to a variable.

    **General rules**

    Use ``'''`` specifically, if your script requires to use variables literally:

        .. code-block:: groovy

            environment {
                VAR="global_value"

                script {
                    sh '''
                        VAR=local_value
                        echo $VAR
                    '''

        which prints ``local_var``, as $VAR is not replaced by the environmental value.

    Use ``"""`` specifically, if your script requires variables to be interpolated by their actual value:

        .. code-block:: groovy

            environment {
                VAR="global_value"

                script {
                    sh """
                        VAR=local_value
                        echo $VAR
                    """

        which prints ``global_var``, as $VAR is replaced by the environmental value.

    This also applies for single quotes. Variables inside single quotes (``'$VAR'``)
    are used literally, whereas inside double quotes (``"$VAR"``) are replaced by their
    interpolated value.

    In both single and double quotes script blocks, variables can be accessed both via
    ``$VAR`` or ``${VAR}``.

:line 101-105:

    Within the script block (which are executed in the default shell on the node, which
    is either *bash* on Linux or *zsh* on macOS), the environment variables inside
    the `env <jenkinsfile_env_>`_ object can be accessed via ``${env.<VARIABLE_NAME>}``.
    The block assigns the *currentBuild* `global variable <jenkins_global_variable_reference_>`_,
    settings it to ``'ABORTED'`` and emitting and `error signal <jenkins_error_signal_>`_
    via ``error``, which uses variable interpolation in its error string, which
    requires it to use *double quotes*.

:line 106-109:

    The ``contains`` method checks whether the array contains the given value.

:line 111:

    The ``replace`` method replaces a given target string (here: ``'.dev'``)
    with a substitute (here: ``''`` (empty)) within a string.

:line 120:

    The ``replaceFirst`` method replaces the first match of a given target (here:
    ``'origin/'`` with a substitute (here: ``""`` (empty)) within a string.

.. _jenkins_error_signal: https://www.jenkins.io/doc/pipeline/steps/workflow-basic-steps/#error-error-signal
.. _jenkins_global_variable_reference: https://www.jenkins.io/doc/book/pipeline/getting-started/#global-variable-reference
.. _jenkinsfile_environment: https://www.jenkins.io/doc/book/pipeline/syntax/#environment
.. _jenkinsfile_env: https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#using-environment-variables
.. _java_map_get: https://docs.groovy-lang.org/latest/html/groovy-jdk/java/util/Map.html#get(java.lang.Object,%20java.lang.Object)


Stage - Execute Makefile target
-------------------------------
More complex logic is advised to be moved into shell script. Furthermore, such
shell script can be executed via a Makefile target.

.. code-block:: groovy
    :linenos:
    :lineno-start: 128

        stage("Get latest compatible metapackage dependencies from AF") {
            steps {
                dir("${MAKEFILE_DIR}") {
                    script {
                        sh """
                            CURRENT_METAPACKAGE_VERSION=${CURRENT_METAPACKAGE_VERSION} \
                            NTTS_PRODUCT_PREFIX_SUFFIX=${NTTS_PRODUCT_PREFIX_SUFFIX} \
                            ARTIFACTORY_SOURCE_REPO=${ARTIFACTORY_SOURCE_REPO} \
                            JFROG_HOME=${JFROG_HOME} \
                            make pull-python-dependencies
                        """
                    }
                }
            }
        }

:line 130:

    The `dir <jenkinsfile_dir_>`_ block defines the working directory of all processes
    within the block (so from line 131 until line 139).

:line 131 - 139:

    A `script <jenkinsfile_script_>`_ section, which includes a `sh <jenkinsfile_sh_>`_
    command. As mentioned above, the *script* block contains a block of
    `scripted pipeline <jenkins_scripted_pipelines_>`_. In this case, this includes
    the *sh* command, which opens executes the shell script. As the script opens with
    triple double-quotes (``"""``) it is a multi-line shell script, which supports
    variable interpolation. As this multi-line script is actually a single line command,
    just broken into several lines for better readability, each line but the last
    requires the `line continuation`_ character ``\``.


.. _jenkinsfile_dir: https://www.jenkins.io/doc/pipeline/steps/workflow-durable-task-step/#dir-change-current-directory
.. _line continuation: https://www.gnu.org/software/bash/manual/bash.html#Escape-Character

Stage - Run inline groovy script
--------------------------------
Jenkins recommends to `outsource more complex logic into separate Groovy script files <outsource_scripts_>`_,
to keep a Jenkinsfile simpler and to allow reuse but other pipeline. Simpler scripts
can still be defined within the Jenkinsfile itself.

It follows the `Groovy syntax`_, while also supporting `additional steps <jenkinsfile_steps_>`_
provided by Jenkins.

.. code-block:: groovy
    :linenos:
    :lineno-start: 183

        stage("Push promotion changes to remote and create pull request") {
            steps {
                dir("${WORKSPACE}/${PRODUCT_METAPACKAGE_REPO}") {
                    script {
                        withCredentials([gitUsernamePassword(credentialsId: "${CREDENTIAL_KEY}")]) {
                            def create_pull_request_log = sh(script: """
                                PROMOTED_METAPACKAGE_VERSION=${PROMOTED_METAPACKAGE_VERSION} \
                                NTTS_PRODUCT_PREFIX_SUFFIX=${NTTS_PRODUCT_PREFIX_SUFFIX} \
                                PROMOTION_PULL_REQUEST_BRANCH_LOCAL=${PROMOTION_PULL_REQUEST_BRANCH_LOCAL} \
                                PROMOTION_RELEASE_BRANCH_LOCAL=${PROMOTION_RELEASE_BRANCH_LOCAL} \
                                PRODUCT_METAPACKAGE_PULL_REQUEST_URL=${PRODUCT_METAPACKAGE_PULL_REQUEST_URL} \
                                SUBTASK_ID=${params.SUBTASK_ID} \
                                CURRENT_BUILD_URL=${currentBuild.getAbsoluteUrl()} \
                                MAKEFILE_DIR=${MAKEFILE_DIR} \
                                make -f ${MAKEFILE_DIR}/Makefile push-promotion-changes-to-remote-and-create-pull-request
                                """, returnStdout: true)

                            /* Determine pull request URL and use as job description
                            Note: an already existing PR is updated, if pipeline runs successfully
                            another time against the same product release branch */
                            def pull_request_url
                            def new_pull_request_url_regex = /NEW_PULL_REQUEST_URL ((?!.*null).*) EOL/
                            def existing_pull_request_url_regex = /EXISTING_PULL_REQUEST_URL ((?!.*null).*) EOL/

                            def new_match = create_pull_request_log =~ new_pull_request_url_regex
                            def existing_match = create_pull_request_log =~ existing_pull_request_url_regex

                            if (new_match) {
                                pull_request_url = new_match[0][1]
                                currentBuild.description =
                                """Pull request created: <a href="${pull_request_url}">${pull_request_url}</a>"""
                            } else if (existing_match) {
                                pull_request_url = existing_match[0][1]
                                currentBuild.description =
                                """Pull request updated: <a href="${pull_request_url}">${pull_request_url}</a>"""
                            } else {
                                currentBuild.description = "Cannot determine pull request URL - check logs"
                            }
                        }
                    }
                }
            }
        }

:line 187:

    Opens a `withCredentials <jenkinsfile_withcredentials_>`_ block, which binds credentials,
    stored as a credentials set in Jenkins, to variables within this block. In this case,
    it calls the ``gitUsernamePassword(...)`` method, passing in the ``"${CREDENTIAL_KEY}"``
    (defined in line 9) as *credentialsID*, referencing the credentials set predefined on
    the Jenkins instance under that same ID. Effectively, this sets the variables

    * $GIT_USERNAME
    * $GIT_PASSWORD
    * $GIT_ASKPASS

    for the duration of the block.

:line 188 - 198:

    Assigns the variables *create_pull_request_log* as the stdout (standard output)
    of the shells script in line 189 - 197. The ``returnStdout: true`` option is
    an optional option of the `sh <jenkinsfile_sh_>`_ command. If set to ``true``,
    the standard output of the command is returned as string (in this case, whatever
    the Makefile target returns).

:line 204 - 205:

    These two lines each define a regular expression. The regex's `syntax <groovy_regex_>`_
    follows the one for Java. They must start and end with a ``\``. For line 204,
    a match must start with the string ``NEW_PULL_REQUEST_URL``, followed with the
    matching group which must not contain *null*, the followed by the string ``EOL``.

:line 207 - 208:

    Here the pattern is applied to the output of the command in line 188 -198.
    The syntax is: ``def match_object = input_text =~ regex_pattern``.

:line 211 + 215:

    The match object contains the matching string, which accessed via
    ``match_string = match_object[0][1]`` in this case, as the entire matching
    text is accessed via ``match_object[0]`` and the ``[1]`` defines the match
    of the first capturing group, which is the wanted text.


.. _outsource_scripts: https://www.jenkins.io/doc/book/pipeline/syntax/#post
.. _jenkinsfile_withcredentials: https://www.jenkins.io/doc/pipeline/steps/credentials-binding/#withcredentials-bind-credentials-to-variables
.. _Groovy syntax: https://groovy-lang.org/syntax.html
.. _groovy_regex: https://docs.groovy-lang.org/latest/html/documentation/index.html#_regular_expression_operators

Post section
------------
The `post <jenkins_post_>`_ section contains all steps, which are executed after the
pipeline or it's steps are completed.

.. code-block:: groovy
    :linenos:
    :lineno-start: 228

    post {
        success {
            script {
                nttsMonitorEmail nttsMonitorEmail.SUCCESS()
            }
        }
        failure {
            script {
                nttsMonitorEmail nttsMonitorEmail.FAILURE()
            }
        }
    }

:line 229:

    This opens a *success* condition block, which is only executed, if the pipeline
    is marked as success.

:line 231 + 236:

    The *nttsMonitorEmail* is the name of an imported Groovy script (line 1).
    The ``nttsMonitorEmail.groovy`` file defines a *call()* method, which accepts
    a custom type ``MonitorTypes`` (an enum, which is either ``MonitorTypes.SUCCESS``
    or ``MonitorTypes.FAILURE``) which executes differently depending on the given
    argument. In this case, different recipients are contacted in case of a
    successful (none, as it uses the empty ``NOTIFY_ON_SUCCESS`` string defined in line 29)
    and a failing pipeline (uses ``NOTIFY_ON_FAILURE`` defined in line 28).

    More on shared libraries: https://www.jenkins.io/doc/book/pipeline/shared-libraries/

:line 234:

    This opens a *failure* condition block, which is only executed, if the pipeline
    is marked as failure.

.. _jenkins_post: https://www.jenkins.io/doc/book/pipeline/syntax/#post
