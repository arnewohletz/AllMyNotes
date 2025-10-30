Timing
======
timeout
-------
Über ``setTimeout()`` lässt sich ein Timeout setzen

.. code-block:: javascript

    document.querySelector("#alert-on").addEventListener("click", alertOn);
    document.querySelector("#alert-off").addEventListener("click", alertOff);

    let timeoutId;

    function alertOn() {
        timeoutId = setTimeout(function() {
            console.log(timeoutId);
            alert("Das hat 4 Sekunden gedauert");
        }, 4000);
    }

Über ``clearTimeout()`` wird ein Timeout abgebrochen:

.. code-block:: javascript

    function alertOff() {
        console.log(timeoutId);
        clearTimeout(timeoutId);
    }

Alle Timeouts werden beim Laden des Skripts registriert. Der Zeitpunkt des Timeout
wird also stets vom Laden des Skriptes gerechnet und **nicht** vom vorangegangenen
Timeout aus gerechnet. Funktionen kommen auf den Stack und werden beim Eintritt ihres
Timeouts ausgeführt, das Skript setzt derweil fort.

Interval
--------
Zyklisches, wiederholendes Ausführen einer Funktion.

Über ``setInterval()`` wird ein Intervall gesetzt. Hier wird die aktuelle Zeit
jede Sekunde aktualisiert:

.. code-block:: javascript

    let intervalId = setInterval(function() {
        console.log("2 Sekunden später");
    }, 2000);
    let timeFunc = function() {
        let datum = new Date();
        let time = datum.toLocaleTimeString();
        document.querySelector("#zeit").textContent = time;
    };

    let timeIntervalId = setInterval(timeFunc, 1000);

Über ``clearInterval()`` wird ein Intervall abgebrochen:

.. code-block:: javascript

    document.querySelector("#interval-off").addEventListener("click", function() {
        clearInterval(intervalId);
        clearInterval(timeIntervalId);
    });

RequestAnimationFrame
---------------------
Über ``requestAnimationFrame()`` wird einmalig eine Animation durchgeführt. Dabei
wird die Ausführung beim Render-Prozess getätigt.

.. code-block:: javascript

    let runCat = function() {
        let position = counter * counter / 8;
        counter++;
        cat.style.left = position + "px";
        if (counter < 100) {
            animationId = requestAnimationFrame(runCat)
        }
    };
    requestAnimationFrame(runCat);

.. hint::

    **Funktion beim Deklarieren sofort einmalig ausführen**

    Über :ref:`IIFE <javascript_iife_immediately_invoked_function_expression>`
    (Immediately Invoked Function Expression):

    .. code-block:: javascript

        (function runCat() {
            let position = counter * counter / 8;
            counter++;
            cat.style.left = position + "px";
            if (counter < 100) {
                animationId = requestAnimationFrame(runCat)
            }
        })();


Über ``cancelAnimationFrame()`` wird die Animation gestoppt:

.. code-block:: javascript

    mouse.addEventListener("click", function() {
        console.log("STOP");
        cancelAnimationFrame(animationId);
    });

Location-Objekt
===============
Das ``window.location`` Objekt beinhaltet zahlreiche Informationen zum
aktuellen Dokument.

.. code-block:: javascript

    // Hyperreferenz der Seite auslesen
    console.log(location.href);

    // queryString (<my_url>?param1=foo -> ?1=foo)
        // if current location is https://example.com
    console.log(location.search);  //<empty string>
        // if current location is https://example.com?q=123
    console.log(location.search);  // "?q=123"

    // hashTag (<my_url>#mytag -> #mytag)
    console.log(location.hash);

    // Dateienpfad -> relativer Pfad der HTML
    console.log(location.pathname);

    // Hostname / Domain
    console.log(location.hostname);

    // Protokoll (http, https, file)
    console.log(location.protocol);

    // Seite neu laden
    document.querySelector("#interval-off").addEventListener("click", function() {
        location.reload();  // evtl. mit Übergabe von true, um Cache zu leeren
    })

    let myBtn =document.querySelector("#alert-on");

    // JS Weiterleitung (auf eine andere Seite)
    myBtn.onclick = function() {
        location.assign("https://duckduckgo.com");
        // neuer History-Eintrag wird erstellt, dadurch kann Nutzer zurückkehren
    };
    myBtn.onclick = function() {
        location.replace("https://duckduckgo.com");
        // kein neuer History-Eintrag, daher keine Rücknavigation möglich
    }
    myBtn.onclick = function() {
        // location.href = "https://duckduckgo.com";
        // genauso wie 'assign', mit History-Eintrag
        location.href += "#alfa";
    }

Objekt-Funktionen
=================
Über Prototyping erhalten Kind-Objekte die Fähigkeiten des Eltern-Objekt. Das
oberste Objekt aller Objekte ist das ``Object`` Objekt. Folgendes Objekt:

.. code-block:: javascript

    let user = {
        lastName:       "Jones",
        firstName:      "Jessica",
        age:            36,
        address:        "Dragonroad 66, Hell's Kitchen",
        getFullName:    function() {
                            return this.firstName + " " + this.lastName;
                        }
    };

Über ``Object.keys()`` werden alle Keys aller Attribute eines gewünschten Objekts
als Array zurückgegeben:

.. code-block:: javascript

    console.log(Object.keys(user));

Über ``Object.values()`` werden die Werte aller Attribute eines gewünschten
Objekts als Array zurückgegeben:

.. code-block:: javascript

    console.log(Object.values(user));

Über ``Object.entries()`` werden die Keys und Werte aller Attribute eines
gewünschten Objekts als Array [key, value] zurückgegeben:

.. code-block:: javascript

    console.log(Object.entries(user));

for-in Schleife
---------------
Iteriert über **Keys** eines Objekts:

.. code-block:: javascript

    let heroes = ["Jessica", "Luke", "Daredevil", "Elektra", "Odin"];

    let user = {
        lastName:       "Jones",
        firstName:      "Jessica",
        age:            36,
        address:        "Dragonroad 66, Hell's Kitchen",
        getFullName:    function() {
                            return this.firstName + " " + this.lastName;
                        }
    };

    for (let index in heroes) {
        console.log(index, heroes[index]);    // 0 Jessica -> 1 Luke -> ...
    }
    for  (let key in user) {
        console.log(key, user[key]);   // OK: lastName Jones -> firstName Jessica -> ...
        console.log(user.key);      // NOK: undefined  --> es gibt kein Attribute 'key'
        console.log(typeof key);    // string
    }

for-of Schleife
---------------
Iteriert über **Values** eines Objekts. Hierfür benötigt das Objekt einen Iterator,
wie z.B. das Array-Objekt dies hat:

.. code-block:: javascript

    for (let value of heroes) {
        console.log(value, heroes.indexOf(value));  // Jessica 0 -> Luke 1 -> ...
    }
    for (let key of Object.keys(user)) {
        console.log(key);  // lastName -> firstName -> ...
    }
    for (let entry of Object.entries(user)) {
        console.log(entry);  // [ "lastName", "Jones" ] -> [ "firstName", "Jessica" ] -> ...
    }

Objekt einfrieren
-----------------
Über ``Object.freeze()`` lässt sich ein Objekt einfrieren.
Wenn ein Objekt eingefroren ist, lässt es sich nicht mehr verändern (wie andere
Programmiersprachen z.B. mit Enums arbeiten).

Wichtig ist, alle Referenzen zu dem eingefrorenen Objekt ebenfalls einzufrieren,
da ansonsten Änderung über diese weiterhin möglich sind.

.. code-block:: javascript

    const marvelHero = {
        name:   "Jessica Jones",
        age:    36,
        status: "angry"
    };

    Object.freeze(marvelHero);

    // marvelHero.name = "Luke Cage"; // TypeError: "name" is read-only
    // delete marvelHero.name; // TypeError: property "name" is non-configurable and can't be deleted
    // marvelHero.character = "ComicHero";  // TypeError: can't define property "character": Object is not extensible

.. warning::

    Ohne den Strikten Modus, sind diese Zuweisungen trotz Freezing möglich!

Objekt duplizieren
------------------
Neue Methode von 2022. Über ``structuredClone()`` wird ein Objekt vollständig,
jedoch ohne Methoden, dupliziert. Duplizierte Objekte sind nicht eingefroren:

.. code-block:: javascript

    const marvelHero = {
            name:   "Jessica Jones",
            age:    36,
            status: "angry"
        };

    let clonedHero = structuredClone(marvelHero);
    clonedHero.name = "Luke Cage"
    console.log(clonedHero);
    console.log(clonedHero.name);  // Luke Cage
    console.log(marvelHero.name);  // Jessica Jones

Andere Möglichkeiten: Prototyping oder JSON (Methoden werden hier ebenfalls ignoriert).

Objekte durch Variablen erzeugen
--------------------------------
Es gibt eine alte und neue Möglichkeit:

.. code-block:: javascript

    let cat = "Lucy",
        dog = "Momo",
        hero = "Jessica";

    // ES5 (alte Variante)
    let myObject = {
        cat: cat,
        dog: dog,
        hero: hero
    };

    let output = function(who) {
        // 'this' referenziert das Objekt auf dem die 'output'-Methode aufgerufen wird
        return who + " is " + this[who];
    }

    // ES6 (neue Variante)
    let myNewObject = {
        cat,
        katze: cat,   // alter Weg weiterhin möglich
        dog,
        hero,
        output  // auch mit Funktionen möglich
    };
    console.log(myNewObject);
    console.log(myNewObject.output("hero"));    // hero is Jessica
    console.log(myNewObject.output("katze"));   // katze is Lucy

FormData-Object
===============
Über ein FormData Objekt lässt sich ein Formular erzeugen

.. code-block:: javascript

    // leeres FormData-Object erstellen
    let myFormDatas = new FormData();

    // Hinzufügen von Einträgen
    myFormDatas.append("firstName", "Jessica");

    let myForm = document.querySelector("#myForm");

    // Event-Handler damit Formular nicht abgesendet wird
    myForm.onsubmit = function() {
        // Formulardaten übergeben
        let allFormDatas = new FormData(myForm);

        // Eintrag erweitern/ergänzen oder hinzufügen (falls nicht vorhanden)
        allFormDatas.append("Username", "jessica123");
        allFormDatas.append("firstName", "Jessica");

        // Eintrag ersetzen oder neu hinzufügen
        allFormDatas.set("password", "12345");

        // Eintrag prüfen
        if (allFormDatas.has("unsinn")) {
            // Eintrag löschen
            allFormDatas.delete("unsinn");
        }

        // löschen auch ohne vorherige Prüfung auf Vorhandenseins des Eintrags möglich
        // wenn nicht vorhanden, wird Aufruf ignoriert
        allFormDatas.delete("unsinn");

        // Iteratoren erstellen
        console.log(allFormDatas.keys());      // FormData-Iterator
        // Durch keys iterieren
        for (let key of allFormDatas.keys()) {
            console.log(key);
        }
        // Durch values iterieren
        for (let value of allFormDatas.values()) {
            console.log(value);
        }
        // Durch entries iterieren (default Iterator)
        for (let entry of allFormDatas) {
            console.log(entry);
        }
        // 1. Wert eines Keys ermitteln
        console.log(allFormDatas.get("username"));

        // alle value-Werte eines Eintrags ermitteln
        // Rückgabe = Array mit Werten einzelner Elemente
        console.log(allFormDatas.getAll("username"));

        // WICHTIG! Formular nicht absenden
        return false;

.. _javascript_datatype_symbol:

Datentyp: Symbol
================
Datentyp wird bei Webseiten-Programmierung kaum eingesetzt. Seit ES6 verfügbar.
Symbole sind **immer einzigartig** - gleichen sich nicht untereinander. Sie können
beim Erzeugen eine Beschreibung erhalten. Erzeugte Symbole werden im Symbolregister
gespeichert.

.. code-block:: javascript

    console.log(Symbol() == Symbol());      // false
    console.log(Symbol("test") == Symbol("test"));      // false

    // Methode Symbol.for()
    let sym1 = Symbol.for("hero.Jessy");
    let sym2 = Symbol.for("hero.Jessy");
    let sym3 = Symbol.for("hero.Jessica");

    console.log(sym1 == sym2); // true
    console.log(sym1 == sym3); // false

    let object = {};
    object.id = 99;

    let symbolId = Symbol("id");
    object[symbolId] = 111;     // Property-Access -> Variablenname als Key
    object.symbolId = 42;   // Punktnotation: -> Symbol-Objekt als Key

    console.log(object);
    console.log(object.id);  // 99
    console.log(object.symbolId);  // 42
    console.log(object["symbolId"]);  // 42  ---> property Name muss bekannt sein
    console.log(object[symbolId]);  // 111

    // Properties, die als Symbol angelegt sind, sind nicht iterierbar
    for (let key in object) {
        console.log(key);   // Symbol("id") wird NICHT ausgegeben
    }

    let symbol_2 = Symbol("id");
    object[symbol_2] = 222;
    console.log(object);  // --> Es gibt nun ZWEI Symbol("id") keys

    for (let entry of Object.entries(object)) {
        console.log(entry);   // Beide Symbol("id") entries werden NICHT ausgegeben
    }

Template String
===============
Neu in ES6. Innerhalb von Backticks-Strings können Ausdrücke innerhalb von ``${}``
Ausdrücke eingefügt werden.

.. code-block:: javascript

    let name = "Jessica";
    let inYears = 30;
    let age = 36;

    // Bei Konsolenausgabe müssen weitere Zeilen an den Zeilenanfang, da sonst
    // Einrück-Leerzeichen mit ausgeben werden
    let templateString = `Hallo ${name}!
    In ${inYears} wirst du ${age + inYears} Jahre alt sein!`;

    // ... dies gilt NICHT für Ausgabe in Elementen, aber berücksichtigt keine
    // Zeilenumbrüche (muss mit <br> Tags gemacht werden)
    document.querySelector("#templStr").textContent = templateString;

    console.log(templateString);
