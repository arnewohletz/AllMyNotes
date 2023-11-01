GPG - GNU Privacy Guard
=======================
Setup
-----
Installation
````````````
Visit https://www.gnupg.org/download/ and download the latest binary for your
operating system.

**For macOS**

Using Homebrew:

.. prompt:: bash

    brew install gnupg

Add this to your ``~/.zshrc``:

    .. code-block:: none

        # Fixing "gpg: signing failed: Inappropriate ioctl for device"
        GPG_TTY=$(tty)
        export GPG_TTY

Make sure the ``gpg`` command is available on the command line.

Generate a key pair
```````````````````

.. hint::

    Have a sufficiently strong passphrase ready before starting the generation.

To generate a key pair run

.. prompt:: bash

    gpg --full-generate-key

Follow the `instructions provided on Github`_.

.. _instructions provided on Github: https://docs.github.com/en/authentication/managing-commit-signature-verification/generating-a-new-gpg-key#generating-a-gpg-key

Add PGP verification
--------------------
For GPG to work the sender (local git repository) must have access to the public
and private key. The corresponding server (for example Github or Bitbucket)
must be aware of your public key.

Client
``````
.. note::

    Not each client supports GPG signing of your commits.

Pycharm
'''''''
Pycharm lets you add GPG keys for each individual local git repository.

#. Open :menuselection:`Preferences --> Version Control --> Git`.
#. In the *Commit* section select :guilabel:`Configure GPG keys`.
#. Select *Sign commit s with GPG key* and select your generated key from the
   dropdown menu.
#. Confirm with :guilabel:`OK`.

Server
``````
Github
''''''
Multiple GPG keys can be added to your account, valid for any for your
repositories.

Follow the `latest instructions on Github to add a new GPG key`_.

.. _latest instructions on Github to add a new GPG key: https://docs.github.com/en/authentication/managing-commit-signature-verification/adding-a-gpg-key-to-your-github-account#adding-a-gpg-key

