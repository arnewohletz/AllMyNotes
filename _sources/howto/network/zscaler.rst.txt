Zscaler
=======
To resolve any of those issue, you need to first download the Zscaler CA Root
certificate. Ask you IT department to provide it. It should be in either \*.pem or
\*.crt format - opening it should show content similar to this:

.. code-block:: none

    -----BEGIN CERTIFICATE-----
    ...
    -----END CERTIFICATE-----

Homebrew
--------
Homebrew internally uses cURL to download artifacts during installation. If the
ZScaler CA root certificate isn't found, you'll see a similar error:

.. code-block:: none

    curl: (60) SSL certificate problem: unable to get local issuer certificate
    ...
    Error: <PACKAGE_NAME>: Failed to download resource "..."

To resolve, make sure the ZScaler CA Root certificate is in \*.crt format (can
be simply renamed, if its \*.pem) and copy the certificate file:

.. code-block:: bash

    $ sudo mkdir /usr/local/share/ca-certificates/zscaler
    $ sudo mv /path/of/ZscalerRootCA.crt /usr/local/share/ca-certificates/zscaler/
    $ sudo chmod 755 /usr/local/share/ca-certificates/zscaler
    $ sudo chmod 644 /usr/local/share/ca-certificates/zscaler/ZscalerRootCA.crt

Create a ``.curlrc`` file inside your $HOME directory and add some content:

.. code-block:: bash

    $ touch ~/.curlrc
    $ echo "cacert=/usr/local/share/ca-certificates/zscaler/ZscalerRootCA.crt" >> ~/.curlrc

Also, Homebrew must be told to trust ``.curlrc``:

.. code-block:: bash

    $ echo insecure >> ~/.curlrc
    HOMEBREW_CURLRC=1
    $ export HOMEBREW_CURLRC

Now the installation should run without errors.
