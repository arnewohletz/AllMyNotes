HTTPS - How does it work? :footcite:p:`https_explained`
=======================================================
#. The client sends a *HelloMessage* to the server. It contains all information
   the server needs to establish a connection via SSL, like the cipher suites and
   maximum supported SSL version.
#. The server answers with a *HelloClient* message, which contains similar information
   including the decision about the used cipher suite and SSL version.
#. The server authenticates itself by send its SSL certificate to the client, which
   includes a public key and a digital signature.
#. The client verifies the certificate, see if it is backed by a trusted Certificate Authority (CA).
#. A common key is agreed upon (session key), which will be used for both encryption
   and decryption (symmetric algorithm) of the data sent between client and server.
   This communication is also encrypted using asymmetric encryption with the servers
   public and private key. The client creates the symmetric key, encrypts it using the
   server's public key, then the server decrypts it using its private key.

.. footbibliography::
