Installation
============
Source: https://mkyong.com/java/how-to-install-java-on-mac-osx/

Installing OpenJDK on macOS
---------------------------
#. Install `Homebrew`_.
#. Run ``brew search java`` to find all Java related formulas, e.g.::

    ==> Formulae
    app-engine-java               java11                        jslint4java
    google-java-format            javacc                        libreadline-java
    java                          javarepl                      pdftk-java
    ==> Casks
    eclipse-java                                 oracle-jdk-javadoc
    eclipse-javascript                           homebrew/cask-versions/java-beta

#. Check the ``java`` formula via ``brew info java``, e.g.::

    openjdk: stable 16.0.1 (bottled) [keg-only]
    Development kit for the Java programming language
    https://openjdk.java.net/
    Not installed
    From: https://github.com/Homebrew/homebrew-core/blob/HEAD/Formula/openjdk.rb
    License: GPL-2.0-only with Classpath-exception-2.0
    ==> Dependencies
    Build: autoconf ✔
    ==> Caveats
    For the system Java wrappers to find this JDK, symlink it with
      sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

    openjdk is keg-only, which means it was not symlinked into /usr/local,
    because macOS provides similar software and installing this software in
    parallel can cause all kinds of trouble.

#. Install the latest OpenJDK by running ``brew install java``.

    .. note::

        Homebrew does install OpenJDK as a *keg*, which means the default Java installation
        at ``/usr/bin/java`` is **not** overwritten, but installed into ``/usr/local/Cellar/``.
        As mentioned in the ``brew info java`` output, it is not recommended to do
        overwrite the default Java, as it might create lots of issues.

#. Add installation to ``/Library/Java/JavaVirtualMachines/`` create a symbolic link:

    .. code-block:: bash

        $ sudo ln -sfn /usr/local/opt/openjdk/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk.jdk

#. Check, if the correct installation is now referenced by running ``java --version``, e.g.::

    openjdk 16.0.1 2021-04-20
    OpenJDK Runtime Environment Homebrew (build 16.0.1+0)
    OpenJDK 64-Bit Server VM Homebrew (build 16.0.1+0, mixed mode, sharing)

Switch between installed Java versions
--------------------------------------
When installing Java over Homebrew, you should have at least two Java versions installed on your system.
All versions can printed out by running ``/usr/libexec/java_home -V``, e.g.::

    Matching Java Virtual Machines (2):
        16.0.1 (x86_64) "Homebrew" - "OpenJDK 16.0.1" /usr/local/Cellar/openjdk/16.0.1/libexec/openjdk.jdk/Contents/Home
        14.0.1 (x86_64) "Oracle Corporation" - "Java SE 14.0.1" /Library/Java/JavaVirtualMachines/jdk-14.0.1.jdk/Contents/Home
    /usr/local/Cellar/openjdk/16.0.1/libexec/openjdk.jdk/Contents/Home

They are also located in ``/Library/Java/JavaVirtualMachines`` and can be called like this:

    .. code-block:: bash

        $ ls -ls /Library/Java/JavaVirtualMachines

    .. code-block:: none

        0 drwxr-xr-x  3 root  wheel  96 Jun  1  2020 jdk-14.0.1.jdk
        0 lrwxr-xr-x  1 root  wheel  42 Aug  9 09:24 openjdk.jdk -> /usr/local/opt/openjdk/libexec/openjdk.jdk

To enable a simple switch, add this content to your ``~/.zshrc`` file (create it, if it does not yet exist)::

    jdk() {
        version=$1
        unset JAVA_HOME;
        export JAVA_HOME=$(/usr/libexec/java_home -v"$version");
        java -version
    }

Save and close the file and source it to become active:

    .. code-block:: bash

        $ source ~/.zhsrc

Now you are able to switch to any installed version by running ``java <version>`` e.g.:

    .. code-block:: bash

        $ jdk 14

    .. code-block:: none

        java version "14.0.1" 2020-04-14
        Java(TM) SE Runtime Environment (build 14.0.1+7)
        Java HotSpot(TM) 64-Bit Server VM (build 14.0.1+7, mixed mode, sharing)

    .. code-block:: bash

        $ jdk 16

    .. code-block:: none

        openjdk version "16.0.1" 2021-04-20
        OpenJDK Runtime Environment Homebrew (build 16.0.1+0)
        OpenJDK 64-Bit Server VM Homebrew (build 16.0.1+0, mixed mode, sharing)

.. _Homebrew: https://brew.sh/