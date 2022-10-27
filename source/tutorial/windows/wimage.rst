Set up Windows image backup with c't-WIMage :footcite:p:`vahldiek21_ersatzrad`
==============================================================================
`WIMage`_ is a backup solution provided by c't for the main disk partition (``C:\``).
The Windows Setup Tool, which installs Windows operating system images, accepts
such a backup and transfers them onto hard disk partitions. WIMage supports
Windows 8.1, 10 (from 1703) and 11 in both 32 and 64 Bit variants.

Prerequisites
-------------
* An empty, external USB drive having the size of the main disk partition or more.
  WIMage makes use of up to 2 TB of available storage (limitation of the `MBR-Partitioning`_).
  It supports larger drives, though doesn't use the extra space: **Saving partitions larger than 2 TB might fail**.
* The latest version of WIMage, downloadable from https://www.heise.de/ct/artikel/c-t-WIMage-3863074.html#nav_download_von__3
* The latest version of the Media Creation Tool (not available for Windows 8.1, which requires
  downloading the ISO image):

    * Windows 8.1: https://www.microsoft.com/en-us/software-download/windows8ISO
    * Windows 10: https://www.microsoft.com/en-us/software-download/windows10
    * Windows 11: https://www.microsoft.com/en-us/software-download/windows11

* Migrate any installed WSL-1 distributions to WSL-2 (`Migrate to WSL-2`_)

.. _MBR-Partitioning: https://en.wikipedia.org/wiki/Master_boot_record

Procedure
---------
Setup
`````
#. Connect the USB storage device.
#. Start the Media Creation Tool and step through the wizard to create an installation media.
#. Select the exact version, which the backup installation uses (for example, Windows 10 Pro 64-Bit).
#. Select the USB storage device as target and launch the creation. The wizard assigns
   ``ESD-USB`` as name for the installation media.

    .. warning::

        For Windows 8.1, use `Rufus`_ to create the installation media.

#. Unzip ``ct-WIMage.zip`` and copy both the ``ct-WIMage`` directory and ``ct-WIMage-maker.bat``
   to ``ESD-USB``'s root directory (which already contains the Windows install files).
#. On the storage device, run ``ct-WIMage-maker.bat`` as administrator.
#. Confirm the security question with "J" (*Ja/Yes*).
#. The script creates a new partition on the storage device. If the
   explorer appears in the forefront, ignore it. Don't abort the script.

After the setup is complete, the ``ESD-USB`` device name changed to
``CT-BOOT`` (keeping the same assigned to drive letter D, if not already occupied)
and created an additional drive, named ``CT-IMAGE`` (assigned to drive letter E, if
not already occupied).

Create backup
`````````````
.. important::

    The initial backup can take 5 hours and longer, though parallel work is
    still possible. Choose a suitable time slot for it.

#. Open the ``CT-IMAGE`` device and execute the ``ct-WIMage-x64.bat`` as administrator.

    .. hint::

        In case ``CT-BOOT`` uses a 32-Bit operating system the file is named ``ct-WIMage-x86.bat``.

#. The explorer might open a new window in the foreground, selecting another new partition
   (drive letter P, if not already occupied), which is a shadow copy of your system drive.
   Its content which is then saved onto ``CT-IMAGE``.
#. Wait until the backup is complete (might take several hours on first run,
   depending on the disk size and transfer speed).

    .. hint::

        In case of errors, check out the :ref:`troubleshooting <wimage_troubleshooting>` section.

    .. hint::

        Future backups are faster, depending on the amount of changes
        after the last backup, but may still take 3 hours or longer.

Restore from backup
```````````````````
Follow these steps to restore the hard disk from the backup. This may become necessary in case of

    * a hard disk defect
    * a serious error in your Windows installation (for example
      due to updates or some other erroneous actions)
    * transferring the present state to a new hard disk

#. Boot your PC from the external USB storage device.

    .. hint::

        How to do so depends on the hardware provider's BIOS. You might have to
        disable secure boot to enable booting from external devices).

#. After the Windows setup initialized, select your preferred keyboard layout
   and location.
#. Next up, select :guilabel:`Install now`.
#. After the setup has started (might take a minute to complete), accept the license
   terms and select :guilabel:`Next`.
#. Select the customized installation type.
#. Choose the install location. If you want to restore your broken Windows partition,
   select the one containing the existing main disk partition ``C:\``.
   If you are using a different hard disk, select a partition which has a size of
   not less than the original backed up drive.

    .. warning::

        The ``CT-BOOT`` and ``CT-IMAGE`` partitions should also be listed, but are
        not to be used!

    .. warning::

        When selecting a partition which already holds a Windows installation,
        WIMage moves that content to a sub-directory named ``Windows.old``.
        From there you may access earlier files. In this case, the hard disk requires
        space to store another instance. Logically, if the old files aren't needed
        or the backup partition uses more than 50 % of its available space,
        format the drive first.

#. Choose :guilabel:`Next` and wait until the installation is complete.
#. Restart the PC (in case, external disks have boot priority according to your BIOS
   settings, detach the hard disk after the shutdown).

.. _wimage_troubleshooting:

Troubleshooting
---------------
WIMage exits due to missing wimre.wim
`````````````````````````````````````
WIMage requires a copy of the Windows RE (Recovery Environment), which resides
on a separate partition. The RE partition is commonly used to repair a corrupted
Windows installation.
In case it isn't found, the script exits with a note ``Operation fehlgeschlagen`` after the
message ``Windows RE auf Windows-Partition verschieben``.

#. Check, if the recovery environment is active:

    .. prompt:: text C:\\>

        reagentc /info

    If it shows *enabled* under *Status*, it's already active. In this case,
    deactivate it temporarily by entering:

    .. prompt:: text C:\\>

        reagentc /deactivate

    You may check the status via ``/info`` again to verify.

#. Go to ``C:\Windows\System32\Recovery`` and check whether it contains a file
   named ``winre.wim``. In case it does, leave the rescue environment
   status as is and start another WIMage backup.
#. In case it doesn't, the rescue system is missing and must be
   retrieved by another Windows installation using the same Windows version. For instance,
   when using Windows 10 Pro, the file must come from the same edition, though
   the version may differ for example 21H2 also accepts the rescue system from 22H2.
#. Download the Media Creation Tool (in case of Windows 8.1, download the ISO image)
   for the respective Windows version (*Create <VERSION> installation media* entry):

    * Windows 8.1: https://www.microsoft.com/en-us/software-download/windows8ISO
    * Windows 10: https://www.microsoft.com/en-us/software-download/windows10
    * Windows 11: https://www.microsoft.com/en-us/software-download/windows11

#. Connect a USB storage device with at least 16 GB of disk space.
   **Careful**: Creating the startup disk formats the device, so save any important data
   from the device first, if needed.

    .. important::

        **For Windows 8.1**

        Download `Rufus`_ to create an installation media using the downloaded ISO.
        Ignore the next step.

#. Launch the Media Creation Tool / Rufus, follow the wizard and create the installation media.
#. Go to the ``sources`` directory on the installation media device and locate
   a file called ``install.esd`` and copy it to ``C:\``.
#. Open a command prompt as administrator, go to ``C:\`` and run

    .. prompt:: text C:\\>

        dism /Export-image /SourceImageFile:install.esd /SourceIndex:1 /DestinationImageFile:C:\install.wim /Compress:max /CheckIntegrity

   which converts the file to ``install.wim`` located at the same directory.

#. Mount the file by running

    .. prompt:: text C:\\>

        mkdir C:\wintemp
        dism /Mount-Wim /WimFile:"C:\install.wim" /index:1 /MountDir:"C:\wintemp"

#. Go to ``C:\wintemp\Windows\System32\Recovery`` and copy the ``Winre.wim``
   file to ``C:\Windows\System32\Recovery``.
#. Restart the WIMage script. If the error doesn't reoccur, delete ``C:\wintemp``,
   ``install.wim`` and ``install.esd``.

OneDrive syncs crashes WIMage
`````````````````````````````
Experiences show that synced directories or files in OneDrive from which you
aren't the owner are crashing WIMage. To prevent that, stop the sync on all
these directories or files and delete them from the hard disk. You may resync
them after the backup, if needed.

.. hint::

    Better quit OneDrive before creating the backup.

The scripts reports the following error at the first stage and exits:

.. code-block:: none

    -9 was unexpected at this time

To resolve it open ``ct-WIMage-x64.bat`` on the root of your ``CT-WIMAGE``
partition and find the following line (at around line 234):

.. code-block:: none

    for /f "tokens=3" %%a in ('dir %systemdrive% /-c ^| findstr /i "Verzeichnis(se)"') do set frei=%%a

and replace it with:

.. code-block:: none

    for /f "tokens=2" %%a in ('wmic volume get DriveLetter^,FreeSpace ^| findstr /i "%systemdrive%"') do set frei=%%a

Save and close the file and start a new run.

Damaged hard disk junctions due to OneDrive
```````````````````````````````````````````
Somewhere during the script operation, the script abort showing this error:

.. code-block:: none

    ERROR 4393

    The tag present in the reparse point buffer is invalid

It means, some mentioned junction files might be in a damaged state.
This may occur if OneDrive has crashed or terminated improperly at some point.

#. Open a command prompt as administrator
#. Enter (in case the system drive uses a different letter, replace ``c`` below):

    .. prompt:: text C:\\>

        chkdsk c: /r /f

#. Confirm with :kbd:`Y` when asked.
#. Restart the PC and wait for the disk check to complete (it may take two hours or longer).
#. Retry running the WIMage script.

.. footbibliography::

.. _WIMage: https://www.ct.de/wimage
.. _migrate to WSL-2: https://dev.to/adityakanekar/upgrading-from-wsl1-to-wsl2-1fl9
.. _Rufus: https://rufus.ie/en/