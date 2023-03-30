Drivers for Linux :footcite:p:`eggeling_linux_hardware`
=======================================================
Linux operating system include lots of drivers for present hardware, though it might
occur that certain (proprietary) drivers need to be installed manually. This guide
shows how to do so.

Screen stays black
------------------
After an installation of Linux on a system that previously ran Windows, it might happen
that the screen stays black on the start of the Linux installer. On Ubuntu-like
distribution the GRUB boot menu first shows after starting from an installer media device.

When continuing with the normal start and the screen stays black try:

A) Start Linux in safe-mode / compatibility-mode
B) Start with additional boot parameters

    #. Select a boot option in the GRUB boot menu, then hit :kbd:`E`.
    #. In the opened text list, navigate with the cursor buttons and add one
       or more option into the line starting with ``linux`` (add them **before** the
       ``--``). These options might help:

        * **xforcevesa**: kernel will only use the VESA-mode for display which runs
          on most graphic chips
        * **nomodeset**: prevents the system to switch into graphical mode (stays
          in text mode). Some Nvidia cards have troubles here.

       Linux Mint only (compatibility-mode)

        * **acpi=off** or **noacpi**: ACPI is ignored which causes the GPU & CPU to
          launch without power saving, hyperthreading or fan control.
        * **acpi=ht**: only hyperthreading and CPU are working, rest is ignored
        * **acpi=strict**: forces ACPI-support of the kernel to only consider ACPI
          attributes of hardware that follows the exact standard
        * **acpi_osi=linux**: skips the validation if ACPI of the computer is compatible
        * **noapic**: prevents APIC is used for the interrupt layer

        A useful combination is found to be: **acpi=off noapic nolapic**

After Linux has been successfully installed, in case of video errors persist,
try to boot with the same options as in the last step, then make the parameters
permanent (until a proper driver is installed).

Open

.. prompt:: bash

    sudo -H gedit /etc/default/grub

and edit this line with your parameters:

.. code-block:: none

    LINUX="[parameter_1]=[value_1] [parameter_2]=[value_2]"

To persist those in the GRUB, run

.. prompt:: bash

    sudo update-grub

After a restart, the changes are set.

Determine the hardware specifics & get driver
---------------------------------------------
Before getting the proper driver, the exact specifics of the hardware piece must
be determined. Each device owns a unique ID, which determines the device and its
manufacturer. Save all your hardware IDs into files:

.. prompt:: bash

    sudo lshw -numeric -html > lshw.html
    sudo lspci -nn > lspci.txt
    sudo lsusb -v > lsusb.txt

The ``lshw.html`` shows general machine information, while the ``lspci.txt`` and
``lsusb.txt`` list information about PCI and USB devices.

.. hint::

    An example ID for a PCI device might be `0bda:b812``, in which the ``0bda``
    determines the manufacturer and ``b812`` determines the device.

After determining the devices ID go to https://linux-hardware.org/?view=search
and enter the manufacturer ID (Vendor ID) and device ID into the respective fields.
The result entry should list the respective driver.
Another way is to probe your device

.. prompt:: bash

    sudo apt get hw-probe
    sudo -E hw-probe -all -upload

which reveals a URL to open in the browser.

In any way, the listed driver should state *works* or *detected* to work and must
be compatible with the kernel version your distribution uses. To determine that run

.. prompt:: bash

    uname -a

If there is no match, it's best to switch to matching Linux distribution.

Compile driver & install
------------------------
If the driver's source code is available, it can be compiled locally. It is crucial
that it is compatible with the kernel. The steps differ from driver to driver,
so an attached manual should be read carefully.

Example for a *Wifi stick RT88x2bu*:

#. Install binary packages needed:

    .. prompt:: bash

        sudo apt get git build-essential dkms linux-headers-$(uname -r)

#. Go to the drivers repository (here: https://github.com/morrownr/88x2bu-20210702)
#. Sync the repository

    .. prompt:: bash

        mkdir -p ~/src
        cd ~/src
        git clone [URL]
        cd 88x2bu-20210702

#. Execute these commands:

    .. prompt:: bash

        make clean
        make
        sudo insmod 88x2bu.ko

#. Check the kernel output on the loading of the driver for issues:

    .. prompt:: bash

        dmesg

#. For most driver, this command needs to be executed next:

    .. prompt:: bash

        sudo make install

   This puts the driver into ``/lib/modules/[kernel_version]``, which is loaded
   upon the next Linux build

Unsigned driver
---------------
For some drivers, they might not be loaded on startup due to secure boot,
which forbid loading of unsigned drivers. Either secure boot needs to be
deactivated or the driver must be signed.

To find out if the driver is signed run

.. prompt:: bash

    modinfo [module_name]

If the module cannot be installed via DKMS, execute these lines to sign it
manually (execute from directory where [MODULE] resides and adapt name):

.. prompt:: bash

    export KERNEL_BUILD=/lib/modules/$(uname -r)/build
    sudo -E $KERNEL_BUILD/scripts/sign-file sha256 /var/lib/shim-signed/mok/MOK.priv /var/lib/shim-signed/mok/MOK.der [Modul].ko

For more info visit https://github.com/Myria-de/kernel-modules.


.. footbibliography::