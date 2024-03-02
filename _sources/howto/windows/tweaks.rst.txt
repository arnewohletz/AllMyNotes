Overwrite domain enforced background image
------------------------------------------
If your Windows PC belongs to a domain, it may be that the domain enforces
a specific background image. In the background image settings menu, the hint
"Some settings are hidden or managed by your organization" shows on top and
the background image settings cannot be changed.

Follow these steps to set a different background image, bypassing this restriction:

#. Open the Registry.
#. Navigate to ``Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System``
#. There should be a **String** value set, which is named **Wallpaper**. If not present, create it.
#. Enter the full path of the desired wallpaper image file as value data.
#. Close the registry, log out and log back into your account. The new wallpaper
   should now be set.

.. hint::

    Occasionally, this value may be overwritten by the domain and a domain-predefined
    wallpaper will be set yet again. Repeat the above steps to revert this process.
