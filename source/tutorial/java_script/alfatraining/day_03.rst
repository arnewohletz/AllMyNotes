Kontroll- / Steuerstrukturen
============================
if-condition
------------
Erzeugt neuen Block-Kontext, welcher nur ausgeführt wird, wenn die vorgehende
Bedingung erfüllt ist.

.. code-block:: javascript

    // if-condition

    if (true) {
        console.log(true);
    }

    if (true) console.log(true); // Kurzschreibweise: wenn nur ein Statement

    if (false) {
        // wird nie erreicht
        console.log(false);
    } else {
        // wird immer erreicht
        console.log(false);
    }

    // Kurzschreibweise (wenn nur ein Statement)
    if (false) console.log(false);
    else console.log(false);

    let a = 2, b = 3;

    // Verschachtelte Prüfung --> nicht gut
    // if (a == b) {
    //     console.log("a == b");
    // } else {
    //     console.log("a != b");
    //     if (a < b) {
    //         console.log("a < b");
    //     } else {
    //         console.log("a > b");
    //     }
    // }

    // Weniger Verschachtelung durch 'if else'
    if (a==b) {
        console.log("a == b");
    } else if (a < b) {
        console.log("a < b");
    } else {
        console.log("a > b");
    }

    // Nochmal Kurzschreibweise
    if (a==b) console.log("a == b");
    else if (a < b) console.log("a < b");
    else console.log("a > b");


.. hint::

    Immer von Speziellen zum Allgemeinen prüfen. Beispiel:

    .. code-block:: javascript

        {
            let n = 14;

            if (n < 10) {
                console.log("n < 10");
            } else if (n < 100) {
                console.log("n < 100");
            } else if (n < 1000) {
                console.log("n < 1000");
            } else {
                console.log("n > 1000");
            }
        }

    Würde zuerst auf n < 1000 geprüft, wäre die Kondition erfüllt und die Prüfung
    ist beendet. Allerdings könnte die Antwort genauer sein.

**Einfache Prüfung** (Sonderfälle abfangen): gilt für ``null``, ``NaN``, ``0``,
``""``, ``undefined``:

.. code-block:: javascript

    // hier: undefined wird als 'false' interpretiert
    let inputVar;
    if (inputVar) console.log("Korrekt");
    else console.log("Inkorrekt");

    /*
        if (null)       => false
        if ("")         => false
        if (0)          => false
        if (undefined)  => false
        if (NaN)        => false

        aber:
        if (" ")        => true
        if (1)          => true
    */

    let userInput = prompt("Sag was:");

    if (userInput) console.log("Danke für " + userInput);
    else console.log("Oje");

Logische Operatoren
-------------------
* ``||`` Oder-Operator:

    Bedingung_1 || Bedingung_2

    - false || false => false
    - true || true => true
    - true || false => true
    - false || true => true

* ``&&`` Und-Operator:

    Bedingung_1 && Bedingung_2

    - false && false => false
    - true && true => true
    - true && false => false
    - false && true => false

* ``!`` Not-Operator: Verkehrt den Wahrheitswert

    !Bedingung

    - !true => false
    - !false => true

    .. code-block:: javascript

        let a = 10, b = 100;

        if (a < 1 || b > 20) console.log("wahr");
        else console.log("unwahr");

        if (a < 10 || a > 50) console.log("wahr");
        else console.log("unwahr");

        if (a > 0 && a < 11) console.log("wahr");
        else console.log("unwahr");

        if (a > 9 && b > 9) console.log("wahr");
        else console.log("unwahr");

        let userInput = "42";
        userInput = "Elektra";
        if (!isNaN(userInput)) console.log(Number(userInput) + 10);

* ``??`` Null-ish Operator

    Steht zwischen 2 Operanden; wenn 1. Operand **null || undefined**,
    wird 2. Operator genutzt.

    .. code-block:: javascript

        let number;  // undefined
        number = number ?? 42;
        number ??= 42;  // Kurzschreibweise für obige Zeile
        console.log(number); // 42

        number = 10;
        number = number ?? 42;
        console.log(number); // 10

switch Kontrollstruktur
-----------------------
Mehrfachverzweigung. Es wird lediglich das zutreffende "Fach" abgearbeitet.
Ohne ``break`` würden noch kommende Fächer ohne Prüfung abgearbeitet.

.. hint::

    Meistens ist eine if-else Kombination besser.

.. code-block:: javascript

    // Mehrfachverzweigung mit switch()

    let myDate = "2024-11-13", monthName;

    let separator = myDate.indexOf("-");
    let separator2 = myDate.lastIndexOf("-");
    let month = Number(myDate.slice(separator + 1, separator2));
    console.log(month);

    switch (month) {
        case 1:
            monthName = "Januar";
            break;
        case 4:
            monthName = "April";
            break;
        case 7:
            monthName = "Juli";
            break;
        case 11:
            monthName = "November";
            break;
        case 12:
            monthName = "Dezember";
            break;
        default:
            monthName = "Hammwer nicht";
    }

    // Ohne ``break`` würden noch kommende Fächer ohne Prüfung abgearbeitet.

    console.log(monthName);

    monthName = "";

    switch (month) {
        case 1:
            monthName += "Januar";
        case 4:
            monthName += "April";
        case 7:
            monthName += "Juli";
        case 11:
            monthName += "November";
        case 12:
            monthName += "Dezember";
    }

    console.log(monthName);  // "NovemberDezember"

    // Fach mit mehreren Werten, nur einer muss erfüllt sein
    let color = prompt("Wähle eine Farbe: rot (r), geld (g), blau (b)");
    if (color) {
        color = color.trim().toLocaleLowerCase();

        switch (color) {
            // Abarbeitung wenn 'rot' oder 'r'
            case "rot":
            case "r":
                console.log("Rot");
                break;
            case "geld":
            case "g":
                console.log("Gelb");
                break;
            case "blau":
            case "b":
                console.log("Blau");
                break;
            default:
                console.log("Ungültige Eingabe");
        }
    }

Strings
=======
Index-Suche
-----------
``.length`` gibt uns die Anzahl der Zeichens eines Strings zurück.

.. code-block:: javascript

    let user = "Jessica Jones"; // 13
    user = "Luke Cage";  // 9
    console.log(user.length);

``.ìndexOf()`` gibt uns die Indexposition einer (Sub-)Zeichenkette in einem String aus.
Durchsucht von links nach rechts, bricht nach erstem Fund ab. Sonst wird ``-1``
zurückgegeben ("nichts gefunden").

.. code-block:: javascript

    let user = "Jessica Lena Jones";

    console.log(user.indexOf(" ")); // 7
    console.log(user.indexOf("Lena")); // 8
    console.log(user.indexOf("lena")); // -1 (case-sensitive)

``.lastIndexOf()`` arbeitet von hinten nach vorne.

.. code-block:: javascript

    let user = "Jessica Lena Jones";
    console.log(user.lastIndexOf(" ")); // 12

Beide erlauben auch die Angabe des Start-Index, ab welchem gesucht wird:

.. code-block:: javascript

    let user = "Jessica Lena Jones";
    // mit Start-Index
    console.log(user.indexOf(" ", 8)) // 12, da Start bei 8
    console.log(user.lastIndexOf(" ", 11)) // 7, da Start bei 11

Umwandlung Klein-/Großkleinschreibung
-------------------------------------
``.toUpperCase()`` wandelt einen String in Großbuchstaben, ``.toLowerCase()``
entsprechend in Kleinbuchstaben.

.. code-block:: javascript

    let user = "Jessica Lena Jones";

    // .toUpperCase() - Umwandlung in Großbuchstaben
    console.log(user.toUpperCase()); // JESSICA LENA JONES
    user = user.toUpperCase();
    console.log(user); // JESSICA LENA JONES

    // .toLowerCase() - Umwandlung in Kleinbuchstaben
    console.log(user.toLowerCase()); // jessica lena jones
    console.log(user.toLowerCase().indexOf("lena"));  // 8

Teil-Strings
------------
``.slice(startIndex, endIndex)`` (``endIndex`` ist in Rückgabe **nicht** enthalten und
ist optional, kann auch höher sein als Länge des Strings -> String wird bis zum
Ende ausgegeben).

.. code-block:: javascript

    /*
        [string].slice(startIndex, endIndex)
    */

    let obst = "Apfel, Banane, Tomate"

    console.log(obst.slice());  // Apfel, Banane, Tomate  (gesamter String)
    console.log(obst.slice(7));  // Banane, Tomate
    console.log(obst.slice(7,13));  // Banane
    console.log(obst.slice(7,100));  // Banane, Tomate (Index höher als String lang -> OK)

    // negative Werte werden von hinten gezählt
    // und nach vorne fortgesetzt (geänderte Richtung)
    console.log(obst.slice(-14, -8)); // Banane
    console.log(obst.slice(-6)); // Tomate

    // endIndex muss auch in diese Richtung erfolgen,
    // sonst <emoty string>
    console.log(obst.slice(-14, -20)); // <empty string>

``.substring()`` funktioniert ähnlich wie ``slice``, erlaubt jedoch den Start- und
EndIndex zu vertauschen -> es kann keine versehentliche Verwechslung passieren
wie bei ``slice``.

.. code-block:: javascript

    let browser = "Mozilla"
    console.log(browser.substring());   // Mozilla
    console.log(browser.substring(0,3));  // Moz
    console.log(browser.substring(3,0));  // Moz  (vertauscht)
    console.log(browser.slice(3,0));  // <empty string>

    let picSource = "bild.png";
    console.log(picSource.substring(picSource.length - 3)); // png

    let myHero = "Jessica Jones";
    let spacePos = myHero.indexOf(" ");
    let firstName = myHero.substring(0, spacePos);
    let lastName = myHero.slice(spacePos + 1);

.. hint::

    Meistens ist ``slice`` vorzuziehen, da negative Indices erlaubt, es sei denn
    das Vertauschen der Indices ist gewünscht.

``.trim()`` entfernt alle Leerzeichen, die einen String umgeben (nur Anfang
und Ende, nicht dazwischenliegende).

.. code-block:: javascript

    let user = "            JEssiCa        LeNa  JoNEs      ";
    user = user.trim();
    console.log(user);  // "JEssiCa        LeNa  JoNEs"

    let firstName = user.substring(0, user.indexOf(" "));
    let lastName = user.slice(user.lastIndexOf(" ") + 1);
    console.log(firstName, lastName);  // Leerzeichen zwischen Werten

.. note::

    ``trimStart()``, ``trimEnd()`` usw. sind noch experimentell.

Prüfungen
---------
``.charAt()`` gibt das Zeichen an Indexposition zurück

.. code-block:: javascript

    // continue from above
    let firstLetter = firstName.charAt(0).toUpperCase();
    console.log(firstLetter);
    let restFirstName = firstName.slice(1).toLowerCase();
    console.log(restFirstName);
    firstName = firstLetter + restFirstName;
    console.log(firstName);  // Jessica

    lastName = lastName.charAt(0).toUpperCase() + lastName.slice(1).toLowerCase();
    console.log(lastName);

    user = firstName + " " + lastName;
    console.log(user);  // Jessica Jones

``.includes()`` prüft ob ein Ausdruck in Zeichenkette vorhanden ist
(gibt boolean zurück). Startposition kann als zweites Argument mitgegeben werden (optional).

.. code-block:: javascript

    let myStr = "Jessica und Luke sind Helden des MArvel-Universums";

    console.log(myStr.includes("Jessica"));  // true
    console.log(myStr.includes("Jessica", 2))  // false
    console.log(myStr.includes("Jones")) // false

``.startsWith()`` und ``.endsWith()`` prüft, ob ein String mit einem bestimmten
Ausdruck beginnt oder endet. ``.startsWith()`` akzeptiert einen optional Start-Index
als zweites Argument.

.. code-block:: javascript

    let myStr = "Jessica und Luke sind Helden des MArvel-Universums";

    console.log(myStr.endsWith("Sinn")); // false
    console.log(myStr.endsWith("ums")) ; // ture

Strings wiederholen
-------------------
``.repeat()`` wiederholt den String um die Anzahl der gegebenen Wiederholungen

.. code-block:: javascript

    console.log("Kohle ".repeat(1000));  // Kohle Kohle Kohle ... x 1000

Strings auffüllen
-----------------
``.padStart(Länge[, Füllzeichen])`` füllt Strings auf angegebene Länge. Das Leerzeichen ist das
Standard-Füllzeichen, kann angepasst werden, auch als Zeichenfolge, welche wiederholt
wird. Ein String wird nicht gekürzt, nur verlängert.
``padEnd(Länge[, Füllzeichen])`` funktioniert identisch, fügt die Füllzeichenn jedoch am
Ende des Strings an.

.. code-block:: javascript

    // padStart
    console.log("1234".padStart(10));  // "      1234"
    console.log("12345".padStart(10));
    console.log("1234".padStart(10, 0));  // "0000001234"
    console.log("1234".padStart(10, "*"));  // "******1234"
    console.log("1234".padStart(10, "+ +")); // "+ ++ +1234"

    // padEnd
    console.log("1234".padEnd(10, 0));  // "1234000000"
    console.log("1234".padEnd(10, "~"));

Ausdrücke in Strings konvertieren
---------------------------------
``.toString()`` existiert in fast allen Datentypen, jedoch nicht in ``undefined``
oder ``null``. Hier besser den String-Konstruktor verwenden, um Type Error zu
vermeiden.

.. code-block:: javascript

    //  Ausdrücke in String konvertieren

    // implizierte Typenkonvertierung - arbeitet mit String()
    console.log(42 + "");  // "42" (nicht 42 als Nummer)
    console.log(String(42)); // "42"
    console.log(String(42 + 69)); // "111"
    console.log(String(true)); // "true"

    console.log((42).toString());   // "42"
    console.log((42 + 69).toString())  // "111"
    console.log((true).toString()); // "true"

    /*
    ``.toString`` existiert in fast allen Datentypen, jedoch
    nicht in ``undefined`` oder ``null``.
    */
    let myVar;
    // console.log(myVar.toString()); // error
    // myVar = null;
    // console.log(myVar.toString()); // error

    console.log(String(myVar)); // "undefined"
