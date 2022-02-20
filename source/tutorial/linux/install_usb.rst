Install Linux on USB flash drive
================================
Having an entire Linux distribution installed on a USB flash drive enables you to
boot it on various computer, using it as a portable environment.

This tutorial follows the process of creating and using a portable distribution of
`Pop!_OS <https://pop.system76.com/>`__ on a MacBook Air (Mid 2014).

Prerequisites
-------------
* Two USB flash drives (one used as the Installer (at least 4 to 8 GB) , the
  other one as the installation and your future portable Linux distribution target
  (128 GB or more recommended)
* Download the Linux distribution as \*.iso (check their official website). Stick to the
  latest LTS version, if available.
* `Etcher <https://www.balena.io/etcher/>`__ is installed

.. admonition:: MacBook Air Only

    **Get your network device driver**

    As of now, Mac computers use a Broadcom network device, for which drivers
    are commonly not included in Linux distributions. We'll need the driver to be
    available to use offline (except, if you have a wired internet connection available).

    #. Find out your network device name:

       .. prompt:: bash

            ioreg -r -n ARPT

        Find the IOName (e.g. "IOName" = "pci14e4,43ba").

        Go to https://devicehunt.com/ and select *PCI* as type and type in the IDs
        of your device. For the upper example:

            +------+-----------+-----------+
            | Type | Vendor ID | Device ID |
            +======+===========+===========+
            | PCI  | 14e4      | 43ba      |
            +------+-----------+-----------+

        This will print the details. Under *Device Details* you will see a BCM entry
        (e.g. BCM43602), which is the hardware model of your wireless network device.

    #. Many devices are supported by the `bcmwl-kernel-source` , including:

        * BCM4321
        * BCM4322
        * BCM4331
        * BCM4352
        * BCM43224
        * BCM43225
        * BCM43227
        * BCM43228
        * BCM4352
        * BCM4360

    #. As Pop!_OS is Ubunutu based, go the official `Ubuntu packages <https://packages.ubuntu.com/source/>`__
       website. In the search area, select your Ubuntu version (the LTS version of
       both OS's are the same) and search for *bcmwl-kernel-source*.
    #. Download the package (you might need to approve the download for the browser).

Steps
-----
.. warning::

    **Create a backup** of your native system on the device, which you will use to create the
    portable USB. If you select the wrong target during installation (local disk instead of
    USB flash device) you will erase your entire internal hard disk.

#. Connect the USB which you will use as the installer (not the installation target USB).
#. Open Etcher, select the image, your USB as target and start the flash.
#. Restart the system and boot from the USB.
#. Once the OS has started, plug in your installation target USB as well.
#. Start the installation, ***selecting the installation target USB as target**.
#. Once the installation is done, shut down the computer and remove the installer USB.
#. Restart the PC, booting from the portable Linux distribution USB device.

    .. admonition:: MacBook Air Only

        You will probably experience, that the Wi-Fi connection isn't available.
        Follow these steps to install the required driver:

        #. Copy the downloaded Broadcom driver onto the system (e.g. to ~/Downloads)
        #. Extract the archive (in case its not already a \*.deb file):

            .. prompt:: bash

                cd ~/Downloads
                tar xzvf ./bcmwl-kernel-source*.deb

        #. Install the driver (might a minute or two):

            .. prompt:: bash

                sudo apt install ./bcmwl-kernel-source*.deb

        #. Load the Broadcom Wi-Fi driver (here: Broadcom Model 43xx):

            .. prompt:: bash

                sudo modprobe -r b43 ssb wl brcmfmac brcmsmac bcma
                sudo modprobe wl

        You should now be able to connect to a Wi-Fi.

