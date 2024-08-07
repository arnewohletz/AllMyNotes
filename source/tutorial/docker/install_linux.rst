Install Docker (CE) on Linux Mint (Ubuntu)
==========================================

#. Update apt package index.

    .. code-block:: bash

        $ sudo apt update

#. Install required packages.

    .. code-block:: bash

        $ sudo apt install apt-transport-https ca-certificates curl gnupg-agent
        $ software-properties-common

#. Add Dockers official GPG key.

    .. code-block:: bash

        $ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

    .. admonition:: Optional

        **Verify the key with fingerprint**

        .. code-block:: bash

            $ sudo apt-key fingerprint 0EBFCD88

        Output should display 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88
        (check the last 8 digits).

#. Add the Docker repository to your package index

    .. code-block:: bash

        $ echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(. /etc/os-release; echo "$UBUNTU_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

    .. hint::

        Other Linux distributions require a different repository url (see
        `here <https://docs.docker.com/engine/install/ubuntu/>`__)

#. Check, if the repository was added to your "additional repositories list"

    .. code-block:: bash

        $ cat /etc/apt/sources.list.d/docker.list

    The output should contain something like this:

    .. code-block:: none

        deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable

#. Install docker components

    .. code-block:: bash

        $ sudo apt update
        $ sudo apt install docker-ce docker-ce-cli docker-compose containerd.io

    .. admonition:: Optional

        **Access docker without using 'sudo'**

        In order to access docker without the 'sudo' command, your current user must
        be added to the docker group (was created during installation)

        .. code-block:: bash

            $ sudo usermod -aG docker $USER

        Then, log out and re-log in to apply the changes

#. Create an account on `Docker Hub <https://hub.docker.com/>`__.
#. Add your Docker Hub login to your docker installation

    .. code-block:: bash

        $ docker login

    .. admonition:: Optional

        A warning message may appear:

        .. code-block::

            WARNING! Your password will be stored unencrypted in /home/<USERNAME>/.docker/config.json.

        Install and setup `docker-credential-helper <https://github.com/docker/docker-credential-helpers>`__
        to not leave your credentials unencrypted.

            #. Install `pass <https://www.passwordstore.org/>`__ and `gnupg2 <https://gnupg.org/>`__:

                .. code-block:: bash

                    $ sudo apt install pass gnupg2

            #. Create a key pair which will be used to encrypt your password database:

                .. code-block:: bash

                    $ gpg2 --quick-gen-key <YOUR_USERNAME>

                .. important::

                    In case you define a passphrase, keep it somewhere save, you
                    will need it later.

                This will print out the public key ID (here: in red), e.g.:

                    .. raw:: html

                        <div class="highlight">
                        <pre>
                        pub   rsa3072 2022-02-09 [SC] [expires: 2024-02-09]
                              <span style="color:red;">ECDB0435E583258DF7687798042565C64AF26E7D</span>:
                        uid                      arne.wohletz
                        sub   rsa3072 2022-02-09 [E]
                        </pre>
                        </div>

                You can reprint it by running ``gpg2 --list-keys``.

            #. Ensure, that the primary key is trusted:

                .. code-block:: bash

                    $ gpg --edit-key <YOUR_PUBLIC_KEY_ID>

                .. code-block:: bash

                    gpg> trust
                    gpg> 5
                    gpg> quit

            #. Set up *pass*:

                .. code-block:: bash

                    $ pass init gpg2 <YOUR_PUBLIC_KEY_ID>
                    $ pass insert docker-credential-helpers/docker-pass-initialized-check

                You should be prompted twice to enter your Docker Hub password.

            #. Download latest release of **docker-credential-pass** (utilizes **pass**)
            #. Extract the binary into a directory listed in PATH.
            #. Open your docker config file:

                .. code-block:: bash

                    $ nano ~/.docker/config.json

            #. Erase all content (if any) and add:

                .. code-block:: none

                    {
                        "credsStore": "pass"
                    }

                Save and close the file.

            #. Log into Docker Hub:

                .. code-block:: bash

                    $ docker login --username="<YOUR_DOCKER_HUB_USERNAME" docker.io

                Enter your password (this should not be required once).

            #. Check if *docker-credential-pass* saved the login:

                .. code-block:: bash

                    $ docker-credentials-pass list

                which should print something like this:

                .. code-block:: none

                    {"https://index.docker.io/v1/":"<YOUR_DOCKER_HUB_USERNAME>"}

#. Check installation success

    .. code-block:: bash

        $ docker run --rm -it --name test alpine:latest /bin/sh

    * Output should be, that alpine:latest isn't found and is downloaded
    * Entering alpine shell after installation

    Enter this into the alpine shell:

    .. code-block:: bash

        $ cat /etc/os-release

    which should output the alpine distribution info.

    Type ``exit`` to close the connection.

**Sources**:

https://docs.docker.com/engine/install/ubuntu
https://computingforgeeks.com/install-docker-docker-compose-on-linux-mint
https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo
