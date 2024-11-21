Konstanten
==========
* ``const`` ist eine Neuerung von ES6 für die Initialisierung von Konstante
* Konstanten brauchen immer sofort eine Zuweisung
* Konstanten können nicht überschrieben oder neu zugewiesen werden
* Konstanten sind ideal für Konfigurationswerten oder Werte, die sich nicht ändern
* gleiches Scope-Verhalten wie Variablen (``let``)

.. code-block:: javascript

    // Konstanten
    {
        const TAX_RATE = 1.19;
        // const TAX_RATE = 1.19;  // error: Redeklaration von Konstanten
        // TAX_RATE = 6; // error: keine neue Zuweisung möglich

        let nettoPrice = 100;
        // let total = nettoPrice * 1.19; // 1.19 - was ist 1.19?
        let total = nettoPrice * TAX_RATE;
    }

Datentypen
==========
Primitive data types (Wert wird übergeben):

* number -> Zahlen (Integer und Float)
* string -> Zeichenketten
* boolean -> true/false
* bigint -> große Zahlen
* symbol -> ES6: unique
* undefined -> nicht belegte Variable
* null -> leerer Objektzeiger  (wird als Typ 'object' ausgegeben -> Known Bug)

Reference data types (Referenz auf Objekt im Speicher wird übergeben):

gilt für alle Objekte

* array -> vordefiniertes Objekt
* object literals
* function -> gehört zu Objekten
* date object -> Objekt zur Ermittlung des aktuellen Datums (speichert Zeit seit 1.1.1970)

.. important::

    JavaScript erlaubt das erneutes Zuweisen eines anderen Datentypen zu einer
    Variablen (dynamische Typenkonvertierung).

number
------
.. code-block:: javascript

    {
        // primitive data types

        // Zahlen (number) - Integer und Float
        console.log(Number.MIN_VALUE)
        console.log(Number.MAX_VALUE)

        // Unter bzw. überschreiten wir den Wertebereich
        // bekommt man ein -Infinity oder 'Infinity' zurück
        // (beides Datentyp number)
        // Hint: Führt nicht zum Fehler, darauf ließe sich noch reagieren
        console.log(1/0); // Infinity
        console.log(-1/0); // -Infinity
        console.log(0/0); // NaN (number)

        // NaN = Ergebnis einer fehlgeschlagenen mathematischen Operation
        // oder einer fehlgeschlagenen Typenkonvertierung

        // Vergleich von zwei NaN Objekten ist stets 'false' (-> daher Prüffunktion nötig)
    }

string
------
Gekennzeichnet durch ``""``, ``''`` oder ``\`\```.

.. code-block:: javascript

    // Zeichenketten (string)
    let output;

    output = '<p class="texte">Content</p>';  // DOM String (nutzt "" und '')
    output = "<p class=\"texte\">Content</p>";  // Escape " mit \
    output = "Mein Text mit \nZeilenumbruch";  // mit Zeilenumbruch
    output = "c:\\neuer_order"  // Prevent Escape

    console.log(output);

Wahrheitswerte (boolean)
------------------------
Es gibt nur ``true``und ``false``.

Ansonsten ``undefined``für nicht zugewiesene Variable oder ``null`` für ein nicht
vorhandenes Objekt.

.. warning::

    ``null`` ist kein 'object' Typ, obwohl so vom Interpreter behauptet, sondern
    ein eigener Objekttyp. Nicht mehr zu behebender Fehler in JavaSript.

BigInt
------
Nur für Genauigkeiten von über 15 Stellen hinaus, für das Web selten bis
nie notwendig.

BigInt Nummern müssen als solche generiert werden, bevor sie außerhalb des
15 Stellen Bereichs kommen (enden mit ``n``).

.. code-block:: javascript

    const bigNumber = 333444555666777888999;
    const bigIntNumber = 333444555666777888999n;

    // Zur Umwandlung in BigInt während der Laufzeit -> Konstruktorfunktion BigInt()
    const bigIntClass = BigInt(333444555666777);  // muss weniger als 15 Stellen haben
    const bigIntClass2 = BigInt(333444555666777888999);  // wird bereits gerundet übergeben

    console.log(bigNumber);  // wird in Ausgabe gerundet
    console.log(bigIntNumber);  // korrekte Ausgabe
    console.log(bigIntClass);

    console.log(333444555666777888999 == 333444555666777888111); // true, obwohl ungleich, da Rundung
    console.log(333444555666777888999n == 333444555666777888111n); // false -> OK

Operatoren
==========
Numerische Operatoren
---------------------
* ``+``  Addition
* ``-``  Subtraktion
* ``*``  Multiplikation
* ``/``  Division
* ``%``  Modulo / Rest einer **ganzzahligen** Division
* ``**`` Potenz (seit ES7)

.. code-block:: javascript

    console.log(12 / 6); // 2
    console.log(12 % 6); // 0
    console.log(12 % 7); // 5

    console.log(2 * 40 + 8 / 2); // 84 (Punkt vor Strich)
    console.log(2 * (40 + 8) / 2); // 48 (Klammern zuerst)

    let a = 2, b = 3, c;

    a += b; // identisch zu a = a + b;

    // Mehrfachzuweisung
    a = b = c = 42;

    console.log(a);

Inkrement / Dekrement Operator
------------------------------
``++``  um 1 erhöhen
``--``  um 1 verringern

.. code-block:: javascript

    /*
        Inkrement- / Dekrement-Operator

        Operator    Beispiel    Interpretation
        ++          a = ++b     a = b + 1; a = b
        ++          a = b++     a = b; b = b + 1
        --          a = --b     b = b - 1; a = b
        --          a = b--     a = b; b = b - 1
    */

    let a = 1;
    console.log(a++); // 1
    console.log(a); // 2

    a = 1;
    console.log(++a); // 2
    console.log(a); // 2

Verkettungs-Operator (+)
------------------------
Verkettung von Strings:

.. important::

    Mindestens ein Wert muss ein String sein, der/die andere(n) werden zum String
    konvertiert (implizite Typenumwandlung).

.. code-block:: javascript

    let userName = "Jessica";
    console.log("Hey " + userName + ". Schön, dass du da bist.");

    let a = "1";  // string
    let b = 2, c = 3;  // number

    console.log(b + c); // 5 (number)
    console.log(a + b + c); // "123" (string) -> keine Verkettung
    console.log(a + (b + c)); // "15" (string)
    // --> implizite Typ-Konvertierung (string wird bevorzugt)

Relationale Operatoren
----------------------
``<``  kleiner als
``>``  größer als
``<=`` kleiner gleich
``>=`` größer gleich
``==`` gleich (Datentyp wird implizit konvertiert)
``===`` gleich (Datentyp wird **nicht** verändert, daher wird Typengleichheit mit geprüft)
``!=``  ungleich (Datentyp wird implizit konvertiert)
``!==`` ungleich (Datentyp wird **nicht** verändert, daher wird Typengleichheit mit geprüft)

Rückgabe ist stets ein boolean (true/false).

.. code-block:: javascript

    console.log(3 < 42); // true
    console.log("3" < 42);  // true (string wird implizit konvertiert)
    console.log("42" == 42); // true (string wird implizit konvertiert)
    console.log("42" === 42); // false (unterschiedlicher Datentyp)
    console.log(100 < 42);  // false
    console.log("100" < 42); // false (string wird implizit konvertiert)
    console.log("100" < "42");  // true (ASCII Nummer werden zeichenweise verglichen, hier: 1 < 4 -> true)
    console.log("3 Autos" > 2);  // false (da "3 Autos -> NaN", NaN-Vergleiche sind stets false)

    // NaN Vergleiche (immer false) -> stattdessen isFinite() oder isNaN() nutzen
    console.log(NaN == NaN);   // false
    console.log(Number("3 Autos") == NaN);  // false

Typenkonvertierung
==================
In JavaScript können Datentypen explizit über einen Ausdruck konvertiert werden,
werden allerdings auch bei bestimmten Operation (z.B. Addition) implizit nur
für diese Operation konvertiert.

Implizierte Typenkonvertierung
------------------------------
.. code-block:: javascript

    let a = "2", b = 4;

    console.log(a * b); // 8 (number)
    console.log(a / b); // 0.5 (number)
    // --> bei '-', '*' und '/' werden Operanden in Number konvertiert

    console.log("15" - "8"); // 7 (number)
    console.log("Jessy" - 3); // NaN (number) => NaN - 3 = NaN

Explizite Typenkonvertierung
----------------------------
.. code-block:: javascript

    let a = "3", b = 4, c = 2;

    console.log(a + b);  // "34"
    console.log((a * 1) + b); // 7 (number) - implizite Typenkonvertierung nutzen
    console.log(+a + b);  // 7 (number) - unary plus Operator wird genutzt

    console.log(Number(a) + b);  // 7 (number)

    console.log(Number("-20.123")); // -20.123 (number)
    console.log(Number("Elektra"));  // NaN
    console.log(Number(" 45 ")); // 45  --> Leerzeichen werden entfernt
    console.log(Number("45 34")); // NaN  --> Innenliegende Leerzeichen
    console.log(Number("10px")); // NaN
    console.log(Number("10,20")); // NaN

    console.log(Number("")); // 0
    console.log(Number(null)); // 0
    console.log(Number(false)); // 0
    console.log(Number(true)); // 1

    console.log(Number(undefined)); // NaN

    /* commented out to prevent prompt

    let price_1 = prompt("Preis Artikel 1:", (10));  // 10 wird als Ausdruck übergeben, daher Klammern
    let price_2 = prompt("Preis Artikel 2:", (10));

    console.log(price_1 + price_2);  // 1010  -> NOK
    console.log(Number(price_1) + Number(price_2)); // 20 -> OK

    */

Über ``parseInt()`` wird versucht, einen Ausdruck in einen Integer zu konvertieren.
Ausdruck kann alles mögliche sein (muss in Klammern übergeben wird)

.. code-block:: javascript

    console.log(parseInt("42"));  // 42 (number)
    console.log(parseInt("42.42")); // 42, da nur ganzzahlig abgerundet
    console.log(parseInt("Elektra"));   // NaN
    console.log(parseInt(" 4256 "));  // 4256
    console.log(parseInt("42 56"));  // 42 -> nur erste Zahl wird geparst
    console.log(parseInt("16px"));  // 16 -> px wird ignoriert, gut zum Verändern von Web-Elementen
    console.log(parseInt(null)); // NaN
    console.log(parseInt(true)); // NaN

    // parseFloat()     versucht übergebenen Ausdruck in Dezimalzahl zu überführen

    console.log(parseInt("42.42")); // 42.42

Datentyp ermitteln
==================
Durch den ``typeof`` Operator. Gibt stets den Datentyp als **String** zurück.

.. code-block:: javascript

    // Datentyp ermitteln durch typeof-Operator

    // Syntax: typeof Operand
    // Rückgabe = Datentype als String

    let output;  // 'undefined' ist ein eigener Datentype
    output = 42;
    output = "42";
    output = true;
    output = null;  // 'null' ist ein eigener Objekttype obwohl 'object' angegeben ist
    output = NaN;

    let dataType = typeof output;
    let dataType2 = typeof typeof output;  // type 'string' da das rechte typeof einen String zurückgibt

    console.log(output, dataType);

Test auf NaN
------------
Zur Prüfung ob eine Variable eine Number ist oder nicht (``isNaN()``).

.. code-block:: javascript

    /*
        isNaN() liefert true, wenn Konvertierung gescheitert (wenn NaN)
        isNaN() liefert false, wenn Konvertierung in nubmer erfolgreich
    */

    console.log(isNaN("42"));        // false
    console.log(isNaN("42 Jahre"));  // true (da NaN)
    console.log(isNaN(NaN));         // true

Test auf Infinite oder Finite (``isFinite()``).

.. code-block:: javascript

    /*
        isFinite() prüft ob n endlich ist (im Wertebereich liegt)
        liefert false, wenn n = Infinity || -Infinity || NaN
        ansonsten true
    */

    console.log(isFinite(42 / 4)); // true
    console.log(isFinite(42 / 0)); // false (Infinite)
    console.log(isFinite(0 / 0)); // false (NaN)

Beispielobjekt: Math
====================
Sammlung von mathematischen Konstanten und Funktionen.

.. code-block:: javascript

    console.log(Math)       // Überblick über Objekt

    // Konstante PI
    console.log(Math.PI);

    // Quadratwurzel ziehen
    console.log(Math.sqrt(16)); // 4

    // Potenz ermitteln
    console.log(Math.pow(10, 2)); // 10^2 = 100

    // maximaler/minimaler Wert ermitteln
    console.log(Math.max(2,11,6,99,43,56,23));  // 99
    console.log(Math.min(2,11,6,99,43,56,23));  // 2

    // absolute Zahl ermitteln
    console.log(Math.abs(-42.234)) // 42.234

    // Zufallszahl
    console.log(Math.random()) // 0 ... 1 (exclusive 1)

    // Runden
    // Immer abrunden
    console.log(Math.floor(2.99)); // 2
    // Immer aufrunden
    console.log(Math.ceil(2.1)); // 3
    // kaufmännisches Runden
    console.log(Math.round(1.4999));  // 1
    console.log(Math.round(1.5));  // 2

    // Runden auf Nachkommastellen
    // Syntax: (number).toFixed(anzahl_nachkommastellen)
    // Rückgabe = string
    let number = 10.12345;
    console.log((number).toFixed()); // 10
    console.log((number).toFixed(2)); // 10.12
    console.log((number).toFixed(4)); // 10.1235

