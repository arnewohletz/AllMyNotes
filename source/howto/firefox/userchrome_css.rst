Custom style with UserChrome.css
--------------------------------
.. hint::

    Steps must be executed for each profile.

Prerequisites
`````````````
Profile customization style sheet support must be enabled:

    #. Type `about:config` into address bar and confirm (accept risk, when asked)
    #. Type `toolkit.legacyUserProfileCustomizations.stylesheet` into search field
    #. Set the resulting entry value to **true** and restart the browser

Steps
`````
#. Open Firefox.
#. Type `about:profiles` into search bar and confirm.
#. For each profile open the *Root directory*.
#. Within there, create a new directory called **chrome**.
#. Within *./chrome*, create a new file called **UserChrome.css** and open it.
#. Add or change the content of :ref:`UserChrome.css <user_chrome_css>`.
#. Save the file and restart Firefox to apply changes.

Get Firefox style elements
``````````````````````````
.. important::

    Use a **clean profile** without extensions as those (e.g. uBlock) may break
    functions of the browser toolbox.

#. `Enable Browser Toolbox`_.
#. `Open the Browser Toolbox`_.
#. In case you need to inspect elements from pop-up elements (e.g. app menu),
   open the setting (three dots button in the top right) and check
   **Disable Popup Auto-Hide**.
#. Get your browser into the state in which you have access your desired element.
#. Select the element picker (top left button) and select the browser element.
#. On the right side, select the *Rules* tab to the see all CSS rules applicable
   to your element.
#. Edit the rules freely to your needs.
#. Save the changed or new rules to your ``userChrome.css`` file. Make sure to
   mark them all as ``!important`` to prevent the rules from being overwritten
   by the browser.
#. Restart the browser using the respective profile to check the result.

.. _Enable Browser Toolbox: https://developer.mozilla.org/en-US/docs/Tools/Browser_Toolbox#enabling_the_browser_toolbox
.. _Open the Browser Toolbox: https://developer.mozilla.org/en-US/docs/Tools/Browser_Toolbox#opening_the_browser_toolbox

.. _user_chrome_css:

UserChrome.css Snippets
```````````````````````
Save Bookmarks menu
'''''''''''''''''''
Windows (1920 x 1080):

.. code-block:: css

    /* Removes pointless bookmark thumbnail image*/
    #editBookmarkPanelImage, #editBookmarkPanelFaviconContainer {
      display: none !important;
    }

    @namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");

    /*Define size of folder tree window*/
    #editBMPanel_folderTree {
        min-height: 600px !important;
        min-width: 40em !important;
    }

    /*Define edit bookmark panel size*/
    #editBookmarkPanel {
      min-width: 44em !important;
      font-size: 13px;
    }

    #editBMPanel_tagsSelector[collapsed="true"] {
        display:none !important;
    }

    /* Remove tag definition*/
    #editBMPanel_tagsRow {
        display:none !important;
    }

    /*Auto-expand folder tree view*/
    #editBMPanel_folderTreeRow {
        visibility:visible !important;
        -moz-box-align:stretch !important;
    }

    /* reduces vertical size of bookmark menu items */
    menupopup:not(.in-menulist) > menuitem,
    menupopup:not(.in-menulist) > menu {
      padding-block: 2px !important;
      min-height: unset !important; /* v92.0 - for padding below 4px */
    }


iMac (5120 x 2880):

.. code-block:: css

    coming later


MacBook Air (1440 × 900):

.. code-block:: css

    /* Hide Giant Thumbnail on Edit Bookmark Panel */
    #editBookmarkPanelImage {
      display: none !important;
    }

    @namespace url("http://www.mozilla.org/keymaster/gatekeeper/there.is.only.xul");

    /*Define size of folder tree window*/
    #editBMPanel_folderTree {
        min-height: 400px !important;
        min-width: 40em !important;
    }

    /*Define edit bookmark panel size*/
    #editBookmarkPanel {
      min-width: 44em !important;
      font-size: 13px;
    }

    #editBMPanel_tagsSelector[collapsed="true"] {
        display:none !important;
    }

    /* Remove tag definition*/
    #editBMPanel_tagsRow {
        display:none !important;
    }

    /*Auto-expand folder tree view*/
    #editBMPanel_folderTreeRow {
        visibility:visible !important;
        -moz-box-align:stretch !important;
    }

    /* reduces vertical size of bookmark menu items */
    menupopup:not(.in-menulist) > menuitem,
    menupopup:not(.in-menulist) > menu {
      padding-block: 2px !important;
      min-height: unset !important; /* v92.0 - for padding below 4px */
    }

Application Menu
''''''''''''''''

.. code-block:: css

    /*Decrease app menu size*/
    :root {
        --arrowpanel-menuitem-padding-block: 2px !important;
        --arrowpanel-menutiem-padding-inline: 2px !important;
    }

Toolbar bookmark popup menu
```````````````````````````

.. code-block:: css

    /* Increase bookmark popup window max-width (default: 41em)*/
    menupopup > menuitem {
        max-width: 100em !important;
    }


Links
`````
https://www.userchrome.org