Copy files from or to remote with SCP
-------------------------------------
.. rubric:: Prerequisites

* SSH Client is installed on local machine
* SSH Server is installed on remote machine

.. hint::

    If the remote system name is unknown, you may also use its IP address.

.. rubric:: Copy files from remote server to local drive

.. prompt:: bash

    scp <remote_username>@<remote_machine_name>:</remote/source/file> </local/target/directory/>

Example:

.. prompt:: bash

    scp root@AECG111416:/tmp/test.txt /home/arnewohletz/docs/

.. rubric:: Copy files from local drive to remote server

.. prompt:: bash

    scp </local/source/file> <remote_username>@<remote_machine_name>:</remote/target/directory>

Example:

.. prompt:: bash

    scp /home/arnewohletz/docs/test_local.txt root@AECG111416:/tmp/

.. hint::

    Alternatively, you can use SFTP to copy files from and to a remote target. The basic copy
    command is analog to SCP. Simply exchange ``scp`` with ``sftp``.
