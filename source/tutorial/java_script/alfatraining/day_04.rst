Schleifen
=========
for-loop (Zählerschleife)
-------------------------
Zählerschleife mit for (Initialisierung; Bedingung; Befehlsfolge)

.. code-block:: javascript

    // Zählerschleife mit for (Initialisierung; Bedingung; Befehlsfolge)

    for (let i = 0; i < 11; i++) {
        console.log("Durchlauf " + i);
    }

    for (let i = 10; i < 101; i += 10) {
        console.log(i, i * i);
    }

    // Mehrere Variablen
    for (let i = 0, j = "0"; j.length < 11; i++, j += i) {
        console.log(i, j, j.length);
    }

    let user = "Elektra";

    for (let i = 0; i < user.length; i++) {
        console.log(user.charAt(i));
    }

.. hint::

    ``let`` kann für Zählvariable im Nicht-Strikten-Modus weggelassen werden,
    sollte man jedoch nicht.

do-while-loop
-------------
Die Schleife wird stets 1x durchgeführt, bevor eine Bedingung geprüft wird.
Eignet sich für Nutzerabfragen. Es muss sichergestellt sein, dass der erste
Durchlauf nicht bereits zu einem Fehler führt.

.. code-block:: javascript

    /*
        fußgesteuerte do...while Schleife

        do {
            Statements;
        } while (Bedingung)
    */

    const SOLUTION = 42;
    let answer;

    do {
    answer = prompt("Die Antwort auf alle Fragen des Universums: ");
    } while (answer != SOLUTION)

    console.log("Great!");

    // Erzeuge zufällig ermittelte ungerade Zahl
    let rand;

    do {
        rand = Math.ceil(Math.random() * 100);
        console.log("Ermittelte Zahl: ", rand);
    } while ( !(rand % 2) )

    console.log("ungerade Zahl: ", rand);

while-loop
----------
Zuerst wird geprüft und daraufhin die Schleife begonnen.

.. code-block:: javascript

    /*
        kopfgesteuerte while... Schleife

        while (Bedingung) {
            Statements;
        }
    */

    let user = "Jessica                Lena             Jones";

    // Solange zwei Leerzeichen in 'user'
    // entferne diese
    while (user.includes("  ")) {
        let doubleSpace = user.indexOf("  ");
        let partOne = user.slice(0, doubleSpace + 1);
        console.log(partOne);
        let partTwo = user.slice(doubleSpace).trim();
        console.log(partTwo);
        user = partOne + partTwo;
        console.log(user);
    }

Schleifensteuerung
==================
Vorzeitiger Abbruch einer Schleife (z.B. wenn Bedingung erfüllt ist).

* Beenden der Schleife mit ``break``

.. code-block:: javascript

    for (let i = 1; i < 101; i++) {
        let result = i * i + 42;
        if (result > 100) break;
        console.log(result);
    }

* Aktuellen Durchlauf der Schleife abbrechen mit ``continue``

.. code-block:: javascript

    for (let i = 1; i < 101; i++) {
        let result = i * i + 42;
        if (result % 2) continue;
        console.log(result);
    }

In for Schleif springt Interpreter zur Befehlsfolge (z.B. i++)
In while Schleife sprint Interpreter zur Bedingungsprüfung (was nach ``while`` steht)

Funktionen
==========
Funktionsdeklaration
--------------------

.. hint::

    Funktionen unterliegen dem Hoisting, d.h. eine Funktion kann bereits **vor**
    seiner Deklaration aufgerufen werden.

.. code-block:: javascript

    /*
    function bezeichner (parameter) {
            Statements;
            return Rückgabewert;
        }

        Aufruf:
        bezeichner (argumente);

        Argumente / Parameter / return = optional
        Parameter = funktionsgebundene Variablen
        return beendet Funktion und kann Wert aus Funktion heraus zurückgeben
        return ersetzt Funktionsaufruf

        kann vor Deklaration aufgerufen werden - unterliegt Hoisting
    */

    myFunc();

    function myFunc () {
        console.log("Guten Tag");
    }
    myFunc();

    console.log(myFunc);
    console.log(myFunc());

    // mit Parametern
    function logMsg (msg) {
        console.log(msg);
    }
    logMsg();       // undefined
    logMsg("Hey");
    logMsg(42);

    function MsgRepeater (msg, count) {
        console.log(msg.repeat(count));
    }
    MsgRepeater("Koks ", 1000);
    // MsgRepeater(1000, "Koks "); => Reihenfolge der Argumente beachten

    // mit return
    function product(a,b) {
        console.log("a", a);
        console.log("b", b);
        return a * b;
    }
    console.log("Ergebnis:", product(42,111));
    console.log("Ergebnis:", product(4,10));
    console.log("Ergebnis:", product(4));       // NaN, da 2. Parameter undefined

    console.log(product(product(2,3),product(4,5)));
    console.log(product(6,product(4,5)));
    console.log(product(6,20));
    console.log(120);

.. hint::

    Eine Funktion ohne ``return`` Statement liefert ``undefined`` zurück.

Funktionsausdruck
-----------------
.. important::

    Funktionsausdrücke unterliegen nicht dem Hoisting, d.h. die Deklaration muss
    **vor** dem ersten Aufruf im Skript erfolgen.

    Daher ist der Funktionsausdruck generell performanter.

.. code-block:: javascript

    /*
        let bezeichner = function (parameter) {
            Statements;
            return Rückgabewert;
        };

        bezeichner(argumente);

        unterliegen NICHT dem Hoisting
        ist performanter
    */

    // square(3);

    let square = function(a) {
        return (a * a);
    };

    console.log(square(3));
    console.log(square(333));
    console.log(square());      // NaN

Default-Werte für Parameter
---------------------------
Zur Vermeidung von ``undefined`` für beim Funktionsaufruf nicht übergebenen Argumente.

.. code-block:: javascript

    let wellcomeMsg = function(name = "Namenlos", anrede = "...") {
        console.log("Hey", anrede, name);
    }
    wellcomeMsg();
    wellcomeMsg("Jessica");
    wellcomeMsg("Jessica", "Heldin");

    function multiply (a = 0, b = 1, c = 1, d = 1, e = 1) {
        console.log(a,b,c,d,e);
        return a * b * c * d * e;
    }
    console.log(multiply());
    console.log(multiply(5));
    console.log(multiply(5,10));
    console.log(multiply(5,10,14,22,42));

IIFE (immediately invoked function expression)
----------------------------------------------
.. hint::

    Sind derzeit nicht mehr allzu verbreitet. Wurden früher verwendet, um Variablen
    nicht in den global Scope zu schreiben. Sie werden jedoch weiterhin als
    anonyme Funktionen verwendet.

Wird direkt bei Definition auch einmalig ausgeführt. Die Funktion kann daraufhin
nicht noch einmal ausgeführt werden, sofern sie nicht auf eine Variable zugewiesen
wird.

.. code-block:: javascript

    (function() {
        let innerVar = 42;
        console.log("IIFE", innerVar);
    })();
    // '(...)' um Funktionsdeklaration bedeutet: "das ist eine Funktion"
    // '()' zum Ende triggern den Aufruf (akzeptiert auch Argumente)
    // console.log(innerVar);  => ReferenceError (da innerVar im Funktions-Scope)

    (function testing() {
        console.log("Test-IIFE");
    })();
    // console.log(testing()); => ReferenceError (da Funktion nicht gespeichert wird)

    let result = (function (a,b) {
        return a * b;
    })(2,3);
    console.log(result);   // erneute Ausführen sofern Funktion einer Variable zugeordnet

    // Kurzschreibweise
    // unterstützt kein return & kann nicht an Variable übergeben werden
    !function() {
        console.log("Greetings");
    }();

Anwendungen findet es das Pattern z.B. bei der Abkapselung von Variablen aus dem
globalen Namespace.

See more: https://developer.mozilla.org/en-US/docs/Glossary/IIFE

Arrays
======
Arrays sind kein eigener Datentyp, sondern gehören zu den vordefinierten Objekten.
Sie enthalten eine Sammlung von Werten, die mit einer Variablen referenziert werden:

.. code-block:: none

    [a,b,c,d]

    Index   Element
    0       a
    1       b
    2       c
    3       d

Arrays erzeugen
---------------
.. code-block:: javascript

    // Array über Literal-Schreibweise erzeugen
    let myArr = [];     // leeres Array
    console.log(myArr);

    let myFilledArr = [1,2,3,4,5];
    console.log(myFilledArr);

    // Array über Constructor-function erzeugen
    let newArr = new Array(7);  // leeres Array mit Platz für 7 Elemente
    console.log(newArr);

    let newFilledArr = new Array(2,3,4,5,true, "Jessy");
    console.log(newFilledArr);

    let heroes = ["Jessica", "Luke", "Daredevil"];

Das Schlüsselwort ``new`` sorgt dafür, dass das ein neues Array erstellt und
zurückgegeben wird.

Arrays abfragen
---------------
* Über den Index

.. code-block:: javascript

    // [array].length um Anzahl der Elemente im Array zu ermitteln
    console.log(heroes.length);

    // Zugriff über Property Access
    console.log(heroes[2]);
    console.log(heroes[0]);

.. important::

    Mit JavaScript kann nicht per nativem Index auf einen Index, der von hinten
    in einem Array gezählt wird, zugegriffen wird.

    .. code-block:: javascript

        let abc = ["a", "b", "c"];
        console.log(abc[-1]);  // gibt 'undefined' zurück

        // Richtige Methode
        console.log(abc[abc.length - 1]);  // gibt letztes Element zurück

* Über ``.at()``

.. code-block:: javascript

    // Zugriff über [array].at(index)
    console.log(heroes.at(1));

Mehrere Arrays verbinden
------------------------
.. important::

    Die Struktur von verbundenen Arrays sollte es möglichst leicht machen, die
    gespeicherten Daten wieder zu bekommen.

.. code-block:: javascript

    let empty = [];
    let emptySlots = new Array(3);
    let primes = [2,3,5,7];
    let band = ["John","Paul","Mary"];
    let mixed = [42,"Jessica",true, {}];
    let sparceArr = [2,,4];  // leeres Element an zweiter Stelle

    let all = [empty, emptySlots, primes, band, mixed, sparceArr];

    // Auf innenliegende Arrays zugreifen
    for (let i = 0; i < all.length; i++) {
        console.log(i, all[i]);
        console.log("Array mit", all[i].length, "Elementen");

        for (let k = 0; k < all[i].length; k++) {
            console.log("Element an Position", k, ":", all[i][k]);
        }
    }

Arrays manipulieren
-------------------
* ``.push(<element>)`` fügt das Element an letzter Stelle eines Arrays ein und gibt
  die Länge des neuen Arrays zurück.

.. code-block:: javascript

    let heroes = ["Jessica Jones", "Luke Cage", "Daredevil", "Elektra", "Nebula"];

    // [array].push() => hinzufügen von 1+ Elementen am Ende des Arrays
    // Rückgabe = neue Länge des Arrays nach dem hinzufügen
    heroes.push("Odin");
    let newLength = heroes.push("Thor", "Loki");  // 8

* ``.pop()`` entfernt das letzte Element eines Arrays und gibt es zurück

.. code-block:: javascript

    // [array].pop() => entfernt letztes Element des arrays
    // Rückgabe = entferntes Element
    heroes.pop();  // 'Loki' wird entfernt
    let oneHero = heroes.pop();  // 'Thor' wird entfernt und zurückgegeben

* ``.unshift()`` fügt Elemente **am Anfang** des Arrays ein (bestehende Werte werden
  nach hinten verschoben) und gibt die neue Länge als Nummer zurück.

.. code-block:: javascript

    newLength = heroes.unshift("Thor","Loki");

* ``.shift()`` entfernt das erste Element eines Arrays und gibt es zurück.

.. code-block:: javascript

    heroes.shift();  // Thor
    oneHero = heroes.shift();  // Loki

* ``.splice(index, anzahl_elemente, 1+ elemente)`` verändert ein Array,
  ab Position mit ``index`` für die ab hier nächsten ``anzahl_elemente``. Fälle:

    - (index) --> Entferne alle Element ab ``index`` bis Ende
    - (index, anzahl_elemente) --> Entfernt ab ``index`` die nächsten
      ``anzahl_elemente``
    - (index, anzahl_elemente, 1+_element) --> Ersetzt (entfernt und fügt ein)
      ab ``index`` die nächsten ``anzahl_elemente`` mit ``1+element`` (item1,
      item2, ..., itemN)

    Die entfernten Elemente werden als Array zurückgegeben. Wurde kein Element
    entfernt wird ein leeres Array zurückgegeben.

.. code-block:: javascript

    let heroes = ["Jessica Jones", "Luke Cage", "Daredevil", "Elektra", "Nebula", "Odin"]

    // gibt Array ab index 1 (inklusive) die nächsten 3 Elemente zurück
    let cardRoom = heroes.splice(1,3);
    console.log(cardRoom); // ["Luke Cage", "Daredevil", "Elektra"]
    console.log(heroes); // ["Jessica Jones", "Nebula", "Odin"]

    // füge an Indexposition 1 diese Elemente ein, gibt leeres Array zurück
    heroes.splice(1,0,"Loki","Thor","Hulk");
    console.log(heroes); // [ "Jessica Jones", "Loki", "Thor", "Hulk", "Nebula", "Odin" ]

    // entfernt alle Elemente ab index 2
    let offline = heroes.splice(2);
    console.log(offline); // [ "Thor", "Hulk", "Nebula", "Odin" ]
    console.log(heroes); // [ "Jessica Jones", "Loki" ]

    // fügt Element an vorletzter Position ein
    heroes.splice(-1,0,"Elektra","Nebula"); // [ "Jessica Jones", "Loki", "Elektra", "Nebula" ]

    console.log(heroes);
    console.log(offline);

    console.log(typeof heroes);  // object

Array prüfen
------------
Über die ``Array.isArray()`` Methode.

.. code-block:: javascript

    console.log(Array.isArray(heroes));     // true
    console.log(Array.isArray(oneHero));    // false

Array kopieren
--------------
Die ``.slice()`` Methode gibt eine Kopie eines Arrays zurück. Das originale Array
wird bei Veränderungen der Kopie **nicht** verändert.

.. important::

    Ein Array kann **nicht** über Zuweisung einer zweiten Variablen kopiert werden,
    da dies als Referenz passiert, d.h. beides Variablen zeigen auf das gleiche
    Array. Eine Änderung über eine Variable wirkt sich daher auf beide Variablen aus.

    .. code-block:: javascript

        let abc_1 =  ["a", "b", "c"];
        let abc_2 = abc_1;
        abc_1.push("d");
        console.log(abc_2); // ["a", "b", "c", "d"]  Oops!

.. code-block:: javascript

    let heroes = ["Jessica Jones", "Luke Cage", "Daredevil", "Elektra", "Nebula"];

    // vollständige Kopie
    console.log(heroes.slice());

    // Kopie ab startIndex
    console.log(heroes.slice(2));

    // Kopie ab startIndex bis exclusive endIndex
    console.log(heroes.slice(2,4));

    // arbeit mit negat. Werten ist möglich
    // Ermittlung der index-Position durch Zählung vom Ende her
    console.log(heroes.slice(1,-1));

    console.log(heroes);

Element in Array Elemente teilen
--------------------------------
Über ``[string].split()`` wird ein String an einem Separator geteilt und in
Array abgelegt.

.. code-block:: javascript

    // [string]. split(separator)
    // konvertiert String in Array anhand des übergebenen Separators

    let headline = "Willkommen";

    // kein Separator -> packt Variable unverändert in eine Array
    console.log(headline.split()); // ["Willkommen"]
    // empty String separator -> jedes Zeichen wird separates Element
    console.log(headline.split("")); // [ "W", "i", "l", "l", "k", "o", "m", "m", "e", "n" ]

    let user = "Jessica Lena Maria Josepha Jones";
    // Leerzeichen Separator -> trennt jedes Wort (z.B. für CSV Daten)
    console.log(user.split(" ")); // [ "Jessica", "Lena", "Maria", "Josepha", "Jones" ]

    let obst = "Apfel, Banane, Tomate, Kirsche";
    console.log(obst.split(", ")); // [ "Apfel", "Banane", "Tomate", "Kirsche" ]

    // [string]. split(separator, anzahl_elemente)
    console.log(obst.split(", ", 2));  // [ "Apfel", "Banane" ]

Elemente in Array zu String verbinden
-------------------------------------
Über ``[array].join()`` werden die Elemente eines Array in einen String überführt
mit ein optional Separator zwischen den Elementen und dieser zurückgegeben. Das
Array bleibt unverändert.

.. code-block:: javascript

    let obst_array = [ "Apfel", "Banane", "Tomate", "Kirsche" ];
    console.log(obst_array.join("")); // ApfelBananeTomateKirsche

    console.log(obst_array.join(" ")); // Apfel Banane Tomate Kirsche

Performanter, aber weniger flexibel ist die ``.toString()`` Methode. Es wird
stets Komma als Separator verwendet.

.. code-block:: javascript

    console.log(obst_array.toString()); // Apfel,Banane,Tomate,Kirsche
    // Array selbst bleibt ebenfalls unverändert
    console.log(obst_array); // [ "Apfel", "Banane", "Tomate", "Kirsche" ]

Elemente sortieren
------------------
Über ``sort()`` werden Elemente **aufsteigend** sortiert.

.. code-block:: javascript

    let heroes = ["Jessica", "Luke", "Daredevil", "Elektra", "Udin", "Thor", "Nebula"];
    console.log(heroes);
    heroes.sort();  // sortiert aufsteigend
    console.log(heroes);  // sortiertes Array

.. important::

    ``sort()`` nutzt ASCII Zeichentabelle zur Sortierung:

    .. code-block:: javascript

        console.log([2,42,1,11,104,99,22,65,6,7,52,3].sort());  // Funktioniert nicht

Über ``reverse()`` werden Elemente **invertiert**.

.. code-block:: javascript

    let heroes = ["Jessica", "Luke", "Daredevil", "Elektra", "Udin", "Thor", "Nebula"];
    console.log(heroes);
    heroes.sort().reverse();  // sortiert aufsteigend + invertiert -> absteigende Sortierung
    console.log(heroes);  // sortiertes Array

Indexposition von Element abfragen
----------------------------------
``.indexOf()`` ermittelt die Indexposition eines Elements von links (Start) aus gezählt.
Ein Start-Index ist optional. Nach dem ersten Fund wird die Suche gestoppt.
``.lastIndexOf()`` tut dasselbe, beginnt jedoch von hinten an zu suchen.

.. code-block:: javascript

    /*
        [array].indexOf(elem [,startIndex])
        [array].lastIndexOf(elem [,startIndex])
    */
    let heroes = ["Jessica", "Luke", "Daredevil", "Elektra", "Udin", "Thor", "Nebula"];

    console.log(heroes.indexOf("Jessica"));  // 0
    console.log(heroes.indexOf("Jes")); // -1 (nicht gefunden)
    console.log(heroes.indexOf("Jessica", 2)); // -1 (an Indexpostion 0)
    console.log(heroes.lastIndexOf("Elektra"));   // 3

``includes()`` prüft, ob ein Element in Array enthalten ist. Gibt einen **boolean** zurück.
Ein Start-Index ist optional.

.. code-block:: javascript

    /*
        [array].incudes(elem [, startIndex])
        prüft ob element in Array enthalten
        Rückgabe: boolean
        Start-Index als optionales 2. Argument
    */
    let heroes = ["Jessica", "Luke", "Daredevil", "Elektra", "Udin", "Thor", "Nebula"];

    console.log(heroes.includes("Elektra"));  // true
    console.log(heroes.includes("or"));  // false
    console.log(heroes.includes("Luke", 3))  // false

Arrays kombinieren
------------------
Über ``.concat()`` lassen sich Elemente oder Arrays an ein Array anfügen.
Das Ursprungs-Array wird nicht verändert. Das neue Array wird zurückgegeben.

.. code-block:: javascript

    let array = [1,2,3,4],
        array2 = [5,6,7,8];

    let array3 = array.concat(array2);
    array3 = array.concat(5,array2,10);
    console.log(array3);  // [ 1, 2, 3, 4, 5, 5, 6, 7, 8, 10 ]
    console.log(array);  // [ 1, 2, 3, 4 ]

Arrays abflachen
----------------
Über ``.flat()`` werden innenliegende Arrays, in das äußere Array überführt.
Die *Tiefe* ist standardmäßig ``1``, kann jedoch erhöht werden, so das auch weiter
innenliegende Arrays mit abgeflacht werden.

.. code-block:: javascript

    let multiArr = [1,2,3,[4,5,6],7];
    console.log(multiArr.flat()); // [ 1, 2, 3, 4, 5, 6, 7 ]
    multiArr = [1,2,3,[4,[5,6]],7];
    console.log(multiArr.flat()); // [ 1, 2, 3, 4, [5, 6], 7 ]
    console.log(multiArr.flat(2)); // [ 1, 2, 3, 4, 5, 6, 7 ]
