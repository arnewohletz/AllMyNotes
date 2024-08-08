SSL
===
Resolve SSL issues
------------------

:Problem:

    Interacting with the remote repository (for example ``git pull``) using
    a secure HTTP connection (for example ``https://github.com``) on a
    Windows machine using `Git for Windows`_ leads to this error message:

    .. code-block:: none

        Git on Windows: unable to get local issuer certificate

:Cause:

    The defined SSL backend to validate the remote's SSL
    certificate is not able to find the local trusted root CA certificate.

    Either no or an improper tool is specified, or the certificate is missing.

:Solution:

    Check the git config for the specified tool:

    .. code-block:: bash

        C:\> git config --global --get http.sslbackend

    which should print **schannel** (refers to `Secured Channel`_). If not, run

    .. code-block:: bash

        C:\> git config --global http.sslbackend schannel

    If that does not resolve the issue, check the root CA certificate:

    #. Open the webpage of the remote git service (for example
       ``https://github.com``).
    #. `Find out the ROOT CA certificate`_ used by the website.
    #. Open the certificate manager (:kbd:`Win + R`, type ``certmgr.msc`` and
       confirm).
    #. Under *Trusted Root Certification Authorities / Certificates*, check if
       if the certificate of the website is listed (it shouldn't).
    #. Search the web for a download to the root CA certificate in ``*.crt`` or
       ``*.cer`` format.
    #. Right-click :guilabel:`Trusted Root Certification Authorities --> Certificate`
       and select :guilabel:`All Tasks --> Import...` and follow the instructions
       to add the certificate.

.. _Git for Windows: https://gitforwindows.org/
.. _Secured Channel: https://learn.microsoft.com/en-us/windows/win32/secauthn/secure-channel
.. _Find out the ROOT CA certificate: https://support.mozilla.org/en-US/kb/secure-website-certificate#w_viewing-a-certificate
