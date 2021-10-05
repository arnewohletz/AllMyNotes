Firefox UserChrome.css
----------------------
.. hint::

    Steps must be executed for each profiles.

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
#. Within ./chrome, create a new file called **UserChrome.css** and open it
#. Copy the content of :ref:`UserChrome.css <user_chrome_css>`.
#. Save the file and restart Firefox to apply changes.

.. _user_chrome_css:
UserChrome.css
``````````````
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
