Measures to clean up hard disk
==============================
Windows tends to fill the hard disk with various things over time. Those are some
recommendation to get disk space back.

* Clean up using `PC Manager`_ or `CCleaner`_.
* Run `TreeSize Free`_ to determine large directories and files.

Specific directories:

* ``C:\System Volume Information``: the directory contains disk snapshots done by
  the `Volume Shadow Copy`_. By default it uses up to 10 % of the disk space.

    Check the currently maximum storage space via command line as admin:

    .. code-block:: bash

        C:\> vssadmin list shadowstorage

    and see the ``Maximum Shadow Copy Storage space`` value on the respective volume.

    To reduce the size (here, set to *10 GB* for ``C:\``), execute:

    .. code-block:: bash

        C:\> vssadmin resize shadowstorage /on=c: /for=c: /maxsize=10GB

    This will prevent the directory from saving more than 10 GB of shadow copies.


.. _PC Manager: https://pcmanager.microsoft.com/en-us
.. _CCleaner: https://www.ccleaner.com/ccleaner
.. _TreeSize Free: https://www.jam-software.com/treesize_free
.. _Volume Shadow Copy: https://learn.microsoft.com/en-us/windows-server/storage/file-server/volume-shadow-copy-service
