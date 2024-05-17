Writing any Unicode (UTF-8) character in HTML
=============================================
The browser interprets given HTML Codes for Unicode characters and displays them.
You may use either the

* entity name
* hex code
* decimal code

.. note::

    Emojis have an CLDR short name. This **does not** serve as entity name for
    HTML. It is used by applications (e.g. messenger) as a way to enter emojis,
    but cannot be interpreted by browser:

    You need to use either the hex or the decimal code for emojis.

| Entity names for Unicode characters: https://html.spec.whatwg.org/multipage/named-characters.html.
| Unicode hex & decimal codes (incl. emojis): https://symbl.cc/en/unicode-table/

**HTML Syntax**

+--------------+------------+
| Type         | Form       |
+==============+============+
| Entity name  | &<NAME>;   |
+--------------+------------+
| Decimal code | &#<CODE>;  |
+--------------+------------+
| Hex code     | &#x<CODE>; |
+--------------+------------+

**Example**

.. code-block:: html

    <p>Using entity name:</p>
    <p>&times;</p>
    <p>Using decimal code:</p>
    <p>&#128512;</p>
    <p>Using hex code:</p>
    <p>&#x1F600;</p>

is interpreted as:

    .. raw:: html

        <p>Using entity name:
        &times;</p>
        <p>Using decimal code:
        &#128512;</p>
        <p>Using hex code:
        &#x1F600</p>
