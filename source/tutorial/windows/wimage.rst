Set up Windows image backup with c't-WIMage :footcite:p:`vahldiek21_ersatzrad`
==============================================================================
`WIMage`_ is a backup solution provided by c't, which is a script, that saves a
Windows image of the system volume (usually ``C:\``). The backup media, an external USB
device, can be booted from and restore the complete drive using the Windows Setup Tool
(used for Windows installations). It supports Windows 8.1, 10 (from 1703) and 11 in
both 32 and 64 Bit variants.

Prerequisites
-------------
* An empty, external USB drive with a size of at least the size of your hard drive (WIMage supports
  up to 2 TB, larger drives are supported, but max. 2 TB can be used) formatted in FAT32
* Latest version of WIMage from https://www.heise.de/ct/artikel/c-t-WIMage-3863074.html#nav_download_von__3
* Latest version of the Media Creation Tool (not available for Windows 8.1, only ISO) for
  the Windows version that is used (see under *Create <VERSION> installation media*
  entry):

    * Windows 8.1: https://www.microsoft.com/en-us/software-download/windows8ISO
    * Windows 10: https://www.microsoft.com/en-us/software-download/windows10
    * Windows 11: https://www.microsoft.com/en-us/software-download/windows11

* No WSL-1 distribution is installed (`migrate to WSL-2`_)

Procedure
---------
Setup
`````
#. Connect the USB storage device.
#. Start the Media Creation Tool and step through the wizard to create a installation media
   for the specific Windows version, that is used (Home, Pro, 32/64-Bit). Don't select a
   re-installation of Windows. Select the USB storage device as target. The device
   is named **ESD-USB**.

    .. warning::

        For Windows 8.1 the installation media must be created via `Rufus`_.

#. Unzip ``ct-WIMage.zip`` and copy both the ``ct-WIMage`` directory and ``ct-WIMage-maker.bat``
   to the storage device's root directory (which already contains the Windows install files).
#. On the storage device, execute ``ct-WIMage-maker.bat`` as administrator.
#. Answer the security question with **J** for *Yes* (*Ja* in German).
#. As the script executes a new partition is created on the storage device. If the
   explorer appears in the forefront, ignore it. Do not abort the script.
#. After the setup is complete, the previous **ESD-USB** device is now named
   **CT-BOOT** (drive letter D:\ is not occupied) and an additional drive should
   be listed in the explorer, named **CT-IMAGE** (drive letter E:\ if not occupied).

Create backup
`````````````
#. Open the **CT-IMAGE** device and execute the ``ct-WIMage-x64.bat`` (*x86*, in case
   a 32-Bit system was created for **CT-BOOT**) as administrator.
#. The explorer might open a new window in the foreground, selecting another new partition
   (letter P:\ if not preoccupied), which contains a shadow copy of your system drive,
   which is then saved onto **CT-IMAGE**.
#. Wait until the backup is complete (might take several hours on first execution,
   depending on the disk size and transfer speed).

    .. hint::

        In case of errors, check out the subsequent troubleshooting section.

    .. hint::

        Subsequent backups are a lot faster, depending on the amount of changes
        since the last backup.

Restore from backup
```````````````````
In case of a hard disk defect, a serious error in your Windows installation (for example
due to updates or some other erroneous actions) or simply transferring the present
state to a new hard disk, follow these steps.

#. Boot your PC from the external USB storage device (how to do so depends on the
   hardware provider's BIOS. Also, you might have to disable secure boot to enable
   booting from external devices).
#. Once the Windows setup initialized, select your preferred keyboard layout and
   location.
#. Next up, select :guilabel:`Install now`.
#. After the setup has started (might take a minute to complete), accept the license
   terms and select :guilabel:`Next`.
#. As installation type, select *Customized:...*.
#. Choose the location, where the backup shall be installed to. Select a partition
   on the internal hard disk of sufficient size for example the one containing the
   existing Windows system drive ``C:\`` (the **CT-BOOT** and
   **CT-IMAGE** partitions should also be listed, but are not to be used). Partitions
   may need be formatted to an adequate format first (recommended: FAT32).

    .. warning::

        If the a partition already containing a Windows installation is selected,
        that content will be saved to sub-directory named ``Windows.old``, from where
        you may access previous files. The backup will be saved next to it. Beware,
        that this may double the required size of that partition. If old files
        are not needed or if the partition was occupying more than 50 % of the
        available hard disk space, better format the drive first.

#. Choose :guilabel:`Next` and wait until the installation is complete.
#. Restart the PC (in case, external disks are prioritized by default, detach
   the hard disk after the shutdown).

Troubleshooting
---------------
WIMage exits due to missing wimre.wim (cannot find Windows RE)
``````````````````````````````````````````````````````````````
WIMage requires a copy of the Windows RE (Recovery Environment) partition, which resides
usually in a separate partition (which is used to save a corrupted Windows installation).
In case it is not found, it exits with a note **Operation fehlgeschlagen** after the
message **Windows RE auf Windows-Partition verschieben**.

#. Check, if the recovery environment is active:

    .. prompt:: bash C:\\>

        reagentc /info

    If it shows *enabled* under *Status*, it is active

#. In case it is active, deactivate it temporarily by entering:

    .. prompt:: bash C:\\>

        reagentc /deactivate

    You may check the status via ``/info`` again to verify.

#. Navigate to ``C:\Windows\System32\Recovery``, in which a file named
   ``winre.wim`` should reside. In case, it does, leave the rescue environment
   status as is and start another WIMage backup.
#. In case, it does not, the rescue system is indeed missing and needs to be
   retrieved by a different but identical Windows installation (for instance, when
   using Windows 10 Pro, the file needs to come from the same edition, though
   the version may differ e.g. 21H2 or 22H2).
#. Download the Media Creation Tool (not available for Windows 8.1, only ISO) for
   the respective Windows version (*Create <VERSION> installation media* entry):

    * Windows 8.1: https://www.microsoft.com/en-us/software-download/windows8ISO
    * Windows 10: https://www.microsoft.com/en-us/software-download/windows10
    * Windows 11: https://www.microsoft.com/en-us/software-download/windows11

#. You will need a USB storage device (will be cleared) with at least 16 GB of disk
   space. Insert it into your PC.

    .. important::

        **Windows 8.1 only**

        Download `Rufus`_ to create an installation media using the downloaded ISO.
        Ignore the next step.

#. Launch the Media Creation Tool, follow the wizard and create the installation media.
#. Navigate to the ``sources``directory on the installation media device and locate
   a file called ``install.esd`` and copy it to ``C:\``.
#. Open a command prompt as administrator, navigate to ``C:\`` and execute

    .. prompt:: bash C:\\>

        dism /Export-image /SourceImageFile:install.esd /SourceIndex:1 /DestinationImageFile:C:\install.wim /Compress:max /CheckIntegrity

   which will convert the file to ``install.wim`` located at the same directory.

#. Mount the file by running

    .. prompt:: bash C:\\>

        mkdir C:\wintemp
        dism /Mount-Wim /WimFile:"C:\install.wim" /index:1 /MountDir:"C:\wintemp"

#. Navigate into ``C:\wintemp\Windows\System32\Recovery`` and copy the ``Winre.wim``
   file to ``C:\Windows\System32\Recovery``.
#. Restart the WIMage script. If the error is resolved, delete ``C:\wintemp``,
   ``install.wim`` and ``install.esd``.

OneDrive syncs crash WIMage
```````````````````````````
It was experienced that synced directories or files in OneDrive (from which you
are not the owner) are crashing WIMage. To prevent that, stop the sync on all
directories or files and delete them from the hard disk (resync them after the
backup, if needed).

.. hint::

    Generally, it is recommended to quit OneDrive during backup creation.

Early after starting the backup script, the following error occurs and the
script exits:

.. code-block:: none

    -9 was unexpected at this time

To resolve it open ``ct-WIMage-x64.bat`` on the root of your ``CT-WIMAGE``
partition and find the following line (at around line 234):

.. code-block:: none

    for /f "tokens=3" %%a in ('dir %systemdrive% /-c ^| findstr /i "Verzeichnis(se)"') do set frei=%%a

and replace it with:

.. code-block:: none

    for /f "tokens=2" %%a in ('wmic volume get DriveLetter^,FreeSpace ^| findstr /i "%systemdrive%"') do set frei=%%a

Save and close the file and start a new execution.

Damaged hard disk junctions due to OneDrive
```````````````````````````````````````````
Somewhere during the script execution, the script abort showing this error:

.. code-block:: none

    ERROR 4393

    The tag present in the reparse point buffer is invalid

The message says, some of the mentioned junction files might be in a damaged state,
which may occur if OneDrive has crashed or terminated improperly at some point.

#. Open a command prompt as administrator
#. Enter (in case the system drive uses a different letter, replace ``c`` below):

    .. prompt:: bash C:\\>

        chkdsk c: /r /f

#. Confirm with 'Y' when asked.
#. Restart the PC and allow disk check to run (it may take two hours or longer).
#. Retry running the WIMage script.

.. footbibliography::

.. _WIMage: https://www.ct.de/wimage
.. _migrate to WSL-2: https://dev.to/adityakanekar/upgrading-from-wsl1-to-wsl2-1fl9
.. _Rufus: https://rufus.ie/en/