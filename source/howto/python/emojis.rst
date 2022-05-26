How to print emojis natively
----------------------------
As all emoji characters are defined within the UTF-8 standard, you can print emojis
or any other UTF-8 character in Python natively.

For instance

.. code-block:: python

    >>> '\U0001F600'

will print the emoji character 1F600 (GRINNING FACE).
To get the unicode encoding for a specific emoji, refer to the `emoji list`_.

Alternatively, you may also refer to the emojis name, e.g.

.. code-block:: python

    >>> '\N{GRINNING FACE}'

which will also print the same emoji as above.

To get the name of an emoji as defined in Python, use the ``unicodedata`` module:

.. code-block:: python

    >>> import unicodedata
    >>> unicodedata.name(chr(0x1F600))
        'GRINNING FACE'
    >>> unicodedata.name('\U0001F600')
        'GRINNING FACE'

.. _emoji list: https://unicode.org/emoji/charts/full-emoji-list.html