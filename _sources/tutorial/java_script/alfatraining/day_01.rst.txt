Introduction
============
* 3 Schichten; HTML (semantisch), CSS (Layout), JavaScript (funktional)
* Über Konsole ist alles erreichbar -> sensible Daten gehören nicht ins Front-End
* Front-End JavaScript hat keinen Zugang zum Dateisystem, nur zur DOM

Geschichte von JavaScript
-------------------------
* 1995: Sprache schaffen zum Einbinden von JavaApplets in Netscape Navigator
  Mocca -> LiveScript -> JavaScript
* 1996 Internet Explorer: JScript -> doppelter Aufwand für Programmierer
* ECMA wollte einheitlichen Standard schaffen -> Wie soll was funktionieren? -> ECMA Script -> ES (derzeit ES6)
* Macromedia half bei Einführung von ES4 (ActionScript) -> wurde zu ES5
* 2015: ES5 -> ES6 war großer Schritt (Vereinfachung) -> "bestes ES seit ES3"
* erst seit IE tot war, war der Weg frei für ES6
  (keine "Polyfills" mehr -> dem Browser Funktionalität beibringen, die es noch nicht kann)
  ES5 noch immer stark verbreitet (oft gemischt mit ES6)
* seitdem jährlicher ECMA Release, aber Änderungen nicht in jedem Browser verfügbar (nur Kern ist garantiert)
  -> JS stets auf unterschiedlichen Browsern testen: Chrome, Firefox, Safari, Opera, Edge

JavaScript mit VS Code
----------------------
.. note::

    VS Code ist in JavaScript mit Hilfe von Node.JS geschrieben (daher Einstellungen in JSON Format)

**Empfohlene Extensions**

* `Auto Rename Tag`_
* `ESLint`_
* `German Language Pack for Visual Studio Code`_
* `Live Server`_ -> Ansicht im Browser (NodeJS Express Server), Änderungen im Browser ohne Reload, Ajax

.. attention::

    *Live Server* benötigt für jedes Projekt einen eigenen Ordner

Jeden Tag
* ein neues Projekt
* Unterlagen werden vom Dozenten hochgeladen

.. _Auto Rename Tag: https://marketplace.visualstudio.com/items?itemName=formulahendry.auto-rename-tag
.. _ESLint: https://marketplace.visualstudio.com/items?itemName=dbaeumer.vscode-eslint
.. _German Language Pack for Visual Studio Code: https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-de
.. _Live Server: https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer

Einbinden von JavaScript
------------------------
HTML Grundgerüst über *emets* (bei VS Code):
>>> html
>>> !

JavaScript direkt ins HTML
``````````````````````````
-> gilt nur für diese eine Seite

.. code-block:: html

    <script>
        alert("Hi");
    </script>

Verweis auf externe JS Datei in HTML
````````````````````````````````````
.. code-block:: html

    <script src="script.js">
        alert("Hi");
    </script>

--> ``script.js`` wird hier eingelesen
--> Datei überschreibt explizites JS falls hier zusätzlich (hier: alert) definiert
--> Pfad stets relativ zur HTML Datei

Asynchrones Laden
`````````````````
Interpreter wartet nicht auf vollständiges Laden des Skripts

.. code-block:: html

    <script src="script.js" async></script>

``defer`` Skripte dürfen erst ausgeführt wenn DOM fertig geladen ist:

.. code-block:: html

    <script src="script.js" async defer></script>

* ``async`` bedeutet, dass das Skript parallel zum Parsen des Dokuments geladen wird
* ``defer`` bedeutet, dass das Script erst nachdem das Dokument geparst wurde, geladen wird

Beste Möglichkeit: Skript ans Ende des HTML packen

So erspart man sich ``async`` und ``defer`` oder es macht nichts, wenn man diese
aus Versehen vergisst.

.. code-block:: html

    <html>
    <body>
        // the entire body
        <script src="script.js"></script>
    </body>
    </html>

Dadurch sollten alle Elemente im DOM sein.

Mehrere Skript-Tags mit Dateien in ein HTML Seite einfügen:

.. code-block:: html

    <html>
    <body>
        // the entire body
        <script src="script_1.js"></script>
        <script src="script_2.js"></script>
        <script src="script_3.js"></script>
    </body>
    </html>

Dabei werden in dieser Reihenfolge abgearbeitet -> darauf achten

Strict-Mode
===========
Generell eine gute Idee, besonders zum Lernen.

- Teilmenge von JS
- performanter
- **jeder** (Syntax-)Fehler wird angezeigt
- wird z.B. bei JQuery immer angewandt (automatisch)
- jeder moderne Browser unterstützt diesem Modus

über

.. code-block:: javascript

    'use strict';

zu Beginn eines Dokuments.

Kommentare
==========
.. code-block:: javascript

    // einzeiliger Kommentar
    /*
        mehrzeiliger
        Kommentar
    */

Schreibregeln & Konventionen
============================
Bei JavaScript

- gilt case sensitive (username != USERNAME)
- beginnt Zählung bei 0
- gilt englische Schreibweise (Dezimaltrennzeichen = ``.`` nicht ``,``)

Nicht relevant für Interpreter, aber Programmierer, dient der Lesbarkeit von Code

- ein Statement pro Zeile
- jede Zeile mit Semikolon beenden (obwohl nicht notwendig)
- Bezeichner sollten sprechend sein (keine Chiffren)

**Regeln für Bezeichner**

- beginnt mit einem Buchstaben, Underscore, Dollar-Zeichen oder Hashtag (jedoch haben
  diese oft andere Konventionen)
- danach sind auch Ziffern erlaubt
- sonst keine Sonderzeichen und Umlaute
- keine Leerzeichen
- keine reservierten Wörter verwenden (https://www.w3schools.com/Js/js_reserved.asp)
- keine Bezeichner von vordefinierten Funktionen oder Objekten verwenden

**Konventionen für Bezeichner**

- für Variablen, Konstanten und Funktionen: lower camel case (lowerCamelCase)
- für Konstruktor-Funktionen: upper camel case (UpperCamelCase)
- für Konstanten zur Konfiguration: screaming snake case (SCREAMING_SNAKE_CASE)

Anweisungsblöcke {} zum Gruppieren mehrerer Anweisungen:

.. code-block:: javascript

    if (true) {
      var x = 2;
      let y = 2;
    }

-> Interpreter weiß, dass alle Anweisungen gemeinsam ausgeführt werden müssen

Vordefinierte Funktionen
========================
.. code-block:: javascript

    // Basics
    alert("Hi"); // pausiert das Skript, User muss Alert-Dialog bestätigen, um fortzusetzen
    confirm("Bist du sicher?"); // pausiert das Skript, User kann mit 'OK' True zurückgeben oder mit 'Cancel' False
    prompt("Wer bist du?", "Niemand"); // Zeigt Eingabefenster (mit Standardwert) -> gibt 'null' (Cancel) oder String mit Eingabe zurück (OK, falls leere Eingabe -> <empty string>)

    console.log("Hello World!", "Wie geht's?"); // String auf der Konsole darstellen
    console.log(42); // Logge Zahl -> grün
    console.log({}); // Logge Objekt -> blau
    console.warn("Warnung"); // Logge Warnung -> Symbol + gelber Hintergrund
    Alert("Hilfe");  // Fehler, da 'Alert' Funktion nicht verfügbar -> Symbol + roter Hintergrund
    console.table(["a", "b", "c", "d"]);  // Zeigt Array tabellarisch an

    // Zeitmessung
    console.time("Messung");
    // ... do some other stuff
    console.timeEnd("Messung");

    // Konsolenausgaben löschen
    console.clear();

Variablen
=========
1) Deklaration -> Variable wird erzeugt
2) Initialisierung -> erfolgt durch Interpreter (erzeugt sie im Speicher)
3) Zuweisung -> Wert wird an Variable übergeben

Generell sollten möglichst wenig Variablen im globalen Scope definiert werden.

.. hint::

    "Hoisting" bedeutet, dass in der Funktion alle Variablen im lokalen Gültigkeitsbereich
    der Funktion bereits **alle Deklarationen** zu Beginn der Funktion stattfinden (Variable
    ist ``undefined``), jedoch die Initialisierung erst in der entsprechenden Zeile.

Alter Weg (ES5): mit ``var``

.. code-block:: javascript

    // Variablen unterliegen dem "Hoisting"
    // https://de.wikipedia.org/wiki/Hoisting
    console.log(myVar); // undefined, da noch keine Zuweisung -> Fehlerquelle!

    var myVar; // noch keine Zuweisung
    var myNumber = 42;  // mit Zuweisung

Neuer Weg (ES6): mit ``let``

.. code-block:: javascript

    // kein Hoisting (weil es häufig zu Fehlern führt)

    // console.log(myLetVar); // Fehler: Variable hier noch nicht definiert

    // global Scope
    let myLetVar = 999;

    // früher wurden viele Funktionen nur zum Kapseln von Variablen geschrieben
    // (zu viele Variablen waren im globalen Scope)

    // Neu: Block Scope (z.B. in Funktionen, If/Else Schleifen oder Blöcken)
    {
        let blockScopedVar = 100;
        console.log(blockScopedVar);
        let myLetVar = 111;
    }

    // console.log(blockScopedVar); // error: not defined
    console.log(myLetVar); // 999

    // mehrere Variablen gleichzeitig erzeugen
    // myCat hat Zuweisung, andere undefined
    let myCat = "Fussel", myDog, myHome, myHero, myGhost;

    myDog = "Moja";
    console.log(myCat, myDog);

    // Rückgabewerte in Variable speichern
    // let confirmReturn = confirm("Korrekt?");

    // Nutzerinput als Variable speichern
    // let userName = prompt("Dein Name:");
