tree - Troubleshooting
======================
.. |nbsp|  replace:: :raw-html:`<nobr><span style="border: 1px solid black; padding: 0px; max-width: fit-content;">NBSP</nobr>`

:Problem:

    When copying the result of a ``tree`` command into a text editor, it may happen
    that artifacts appear instead of space character. For instance, in Pycharm,
    copying this output from the Terminal

    .. code-block:: none

        .
        └── mychart
            ├── Chart.yaml
            ├── charts
            │   └── mysubchart
            │       ├── Chart.yaml
            │       ├── charts
            │       ├── templates
            │       │   └── configmap.yaml
            │       └── values.yaml
            ├── templates
            │   ├── _helpers.tpl
            │   └── configmap.yaml
            └── values.yaml

    into Pycharm, it looks like this

        | .
        | └── mychart
        |     ├── Chart.yaml
        |     ├── charts
        |     │ |nbsp| |nbsp| └── mysubchart
        |     │ |nbsp| |nbsp|     ├── Chart.yaml
        |     │ |nbsp| |nbsp|     ├── charts
        |     │ |nbsp| |nbsp|     ├── templates
        |     │ |nbsp| |nbsp|     │ |nbsp| |nbsp| └── configmap.yaml
        |     │ |nbsp| |nbsp|     └── values.yaml
        |     ├── templates
        |     │ |nbsp| |nbsp| ├── _helpers.tpl
        |     │ |nbsp| |nbsp| └── configmap.yaml
        |     └── values.yaml

:Cause:

    The artifact is a `non-breaking space`_ character, a specialized version of
    a regular space, which prevents line breaks. Apparently, ``tree`` has been
    using it since very early on and the problem only now arises due to some editors
    printing them. In Unicode they are defined as ``U+00a0``, whereas the regular
    space is defined as ``U+0020``. In the editor, there is no mechanism to replace
    those characters and most fonts have display character associated to it, which
    leads the the obscure output (NSBP actually stands for, non-breaking space).

:Solution:

    Search for ``[\u00A0]`` characters in the document (regex search must be active)
    and replace each match with a single space character.

.. _non-breaking space: https://en.wikipedia.org/wiki/Non-breaking_space
