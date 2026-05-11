Prop types
==========
.. important::

    Prop Types have been removed from React in version 19. See
    https://react.dev/blog/2024/04/25/react-19-upgrade-guide#removed-deprecated-react-apis.
    It is recommended to switch to Type Script.

If this is very important to you, rather use `TypeScript`_ instead of JavaScript.
Though React allows to specify it, but it is rarely used in React projects using
JavaScript.

First, import the ``PropTypes`` object

.. code-block:: jsx

    import PropTypes from "prop-types";

Define the ``PropTypes`` property on your component class. For example:

.. code-block:: jsx

    StarRating.propTypes = {
      maxRating: PropTypes.number,
    };

.. hint::

    Import uses upper-case ``PropTypes`` whereas the class property uses lower-case
    ``propTypes``.

If passing in a value into ``maxRating`` prop other than a number, the console
displays a **warning**.

.. _TypeScript: https://www.typescriptlang.org/
