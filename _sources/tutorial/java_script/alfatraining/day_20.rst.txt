Datenstrukturen Map und Set
===========================
Seit ES6 verfügbar. Im Vergleich zu Objekten, sind die Key-Value Paare in einer Map
in einer **festen Reihenfolge**. Ein Set kann nur **einmalige** Werte enthalten.

Map
---
Geordnete Sammlung von Schlüssel-Wert Paaren.

.. code-block:: javascript

    // Erzeugung über Konstruktor-Funktion
    let myMap = new Map();  // leere Map
    console.log(myMap);

    // Eintrag hinzufügen
    myMap.set("firstName", "Jessica");      // Index-Position 0
    myMap.set("lastName", "Jones");
    myMap.set("age", 36);

    // Anzahl der Einträge ermitteln mit .size
    console.log(myMap.size);   // 3

    /*
        Map mit Werten erzeugen

        new Map([
            [key, value],
            [key, value]
        ])
    */

    let heldenStaerke = new Map([
            ["Jessica", 42],
            ["Luke", 63],
            ["Daredevil", 36],
            ["Odin", 1]
    ])

    console.log(heldenStaerke);
    console.log(heldenStaerke.size);   // 4

Konvertierungen
```````````````
.. code-block:: javascript

    // I) Object -> Map
    let user = {
        firstName:  "Jessica",
        lastName:   "Jones",
        age:        36
    };

    // Grundlage = Object-Function entries()
    console.log(Object.entries(user));

    let userMap = new Map(Object.entries(user));
    console.log(userMap);   // Map(3) { firstName → "Jessica", lastName → "Jones", age → 36 }

    // II) Map -> Object  (über Object.fromEntries())
    let userObj = Object.fromEntries(userMap);
    console.log(userObj);   // Object { firstName: "Jessica", lastName: "Jones", age: 36 }

    // III) Map -> Array
    let userArr = Array.from(userMap);
    console.log(userArr);   // Array(3) [ 0 : Array [ "firstName", "Jessica" ], 1: ... ]

Vorteil: Map-keys
`````````````````
Als Key wird jeder beliebige Datentyp akzeptiert (im Unterschied zu Objekten,
welche nur String & Symbol akzeptieren). Die einzige Bedingung ist, dass
Schlüsselwerte einzigartig sein müssen.

.. code-block:: javascript

    userMap.set("1", "String-Schlüssel");
    userMap.set(2, "Number-Schlüssel");
    userMap.set(2, "überschreibender Number-Schlüssel");
    userMap.set("2", "2. String Schlüssel");
    userMap.set(true, "Boolean-Schlüssel");
    console.log(userMap);

    // Limits in Objekten
    // --> im Objekt werden Number-Schlüssel zu Strings konvertiert
    let keyObj = {1: "Eins", true: "wahr"};
    console.log(keyObj);
    console.log(keyObj[1] === keyObj["1"]);   // true

    // --> im Objekt werden Objekt-Schlüssel als Typen-String konvertiert
    //      --> nicht möglich einzigartige Objekte abzulegen!!
    keyObj[user] = "Object-Key";
    console.log(keyObj);

    // bei Map ist das möglich
    let jessyMap = new Map();
    jessyMap.set(user, "Jessy datas");
    console.log(jessyMap);

    jessyMap.set({}, "Jessy");      // Neues Objekt wird erzeugt und referenziert
    jessyMap.set({}, "Elektra");    // Neues Objekt wird erzeugt und referenziert
    // zweites Objekt überschreibt das erste NICHT, da es Referenzen zu zwei
    // UNTERSCHIEDLICHEN (leeren) Objekten sind:
    console.log({} == {}); // false

    // Konstruktor Map() gibt Maß zurück, Methoden lassen sich direkt aufrufen
    // --> Verkettung
    // gleiches gilt für die set() Methode
    let heroStrongness = new Map()
        .set("Jessica", 42)
        .set("Luke", 63)
        .set("Odin", 1)

Methoden
````````
Struktur bietet eine Menge an Methoden und integrierte Iteratoren, so dass wir
direkt mit Entries arbeiten können.

.. code-block:: javascript

    let creatures = new Map([
        ["Hero", "Jesscia Jones"],
        ["Human", "Lutz Maier"],
        ["Tiere", "Lucy, the cat"],
        ["Ghost", "Michael Jackson"]
    ]);

    // [Map].get(key)  - gibt value-Wert zurück
    console.log(creatures.get("Hero"));     // "Jessica Jones"
    console.log(creatures.get("Inhuman"));  // undefined

    // [Map].has(key)  - gibt boolean zurück, ob key-Eintrag vorhanden ist
    console.log(creatures.has("Human"));    // true
    console.log(creatures.has("Inhuman"));    // false

    // [Map].delete(key) - prüft ob Eintrag vorhanden, falls ja, löscht Eintrag
    // gibt boolean zurück, ob Eintrag vorhanden
    console.log(creatures.delete("Inhuman"));   // false (nicht vorhanden)
    console.log(creatures.delete("Human"));   // true
    console.log(creatures.delete("Human"));   // false (bereits gelöscht)

    // [Map].clear() - Map leeren (alle Einträge löschen)
    // creatures.clear();
    console.log(creatures.size);   // 0

    // Maps besitzen integrierte Iteratoren
    // Methoden geben Map-Iterator zurück
    console.log(creatures.keys());

    // über keys iterieren
    for ( let key of creatures.keys()) {
        console.log(key);
    }
    // über values iterieren
    for ( let value of creatures.values()) {
        console.log(value);
    }
    // entries -> Standard-Iterator
    for (let [key, value] of creatures) {
        console.log(key, value);
    }

    // integriertes forEach
    // [Map].forEach( (value, key, map) => {} )
    creatures.forEach( (value, key, map) => {
        console.log(key, value);
        console.log(map);
    });

.. hint::

    Loops durch eine Map sind performanter als durch Objekte.
    Eine Umwandlung eines Objekts in eine Map.

Set
---
Sammlung von eindeutigen Werten.

.. code-block:: javascript

    // Erzeugung über Konstruktor-Funktion Set()
    let mySet = new Set();  // leeres Set
    console.log(mySet);

    // Einträge hinzufügen
    mySet.add("Jessy");
    mySet.add("Luke");
    mySet.add("Thor");
    mySet.add("Elektra");
    mySet.add("Thor");  // doppelte Einträge werden nicht akzeptiert
    console.log(mySet);

    // Ermittlung der Anzahl der Einträge über .size
    console.log(mySet.size);

    // Set mit Werten erstellen
    let heroSet = new Set(["Jessica", "Luke", "Daredevil", "Elektra", "Thor", "Odin", "Thor"]);
    console.log(heroSet);
    console.log(heroSet[1]);    // undefined, Einträge werden als key = value gespeichert, nicht über Index

Konvertierungen
```````````````
.. code-block:: javascript

    // Set -> Array
    let heroArr = [...heroSet];
    console.log(heroArr)

    // Array -> Set - durch Übergabe des Arrays an Konstruktor-Funktion

Methoden
````````
.. code-block:: javascript

    // Set-Methoden

    // [Set].has(key) - prüft, ob Eintrag im Set vorhanden
    // Rückgabe: boolean
    console.log(heroSet.has("Thor"));   // true
    console.log(heroSet.has("Loki"));   // false

    // [Set].delete(key) - prüft ob Eintrag vorhanden, falls ja, löscht diesen
    // Rückgabe: boolean (ob Key vor dem Löschen vorhanden war)
    console.log(heroSet.delete("Loki"));        // false
    console.log(heroSet.delete("Thor"));        // true

    // [Set].clear()  - löscht alle Einträge aus dem Set
    // heroSet.clear();
    console.log(heroSet.size);  // 0
    console.log(heroSet);   // leeres Set

    // keys(), values() und entries() sind vorhanden
    // zur Erstellung von Set-Iteratoren
    // values() = Default-Iterator
    console.log(heroSet.values());      // Set Iterator

    for (let value of heroSet) console.log(value);

    // integriertes forEach()
    // [Set].forEach( (value, key, set) ) = {} )
    heroSet.forEach( (value, key, set) => {
        console.log(value, key);    // Jessica Jessica -> Luke Luke -> ...
        console.log(set);   //  [ "Jessica", "Luke", ... ] -> [ "Jessica", "Luke", ... ] -> ...
    });

    // Rückgabe von Set() und add() = Set
    // so ist Verkettung möglich
    let heroesSet = new Set()
        .add("Nebula")
        .add("Elektra")
        .add("Jessica");

Beispiel: Duplikate aus Array entfernen
```````````````````````````````````````
.. code-block:: javascript

    // Beispiel: Duplikate aus Array entfernen

    let numberArr = [11,42,53,62,42,1,53,99,62,42,1,9];

    let numberSet = new Set(numberArr);
    console.log(numberSet);     // Duplikate wurden entfernt

    // Set in Array umwandeln
    let uniqueArr = [...numberSet];
    console.log(uniqueArr);

    // Zusammengefasst und kürzer
    let uniqueNumberArr = [...new Set(numberArr)];

Iteratoren
==========
Iteratoren sind Objekte, welche Methoden implementieren, die den "nächsten" Eintrag
einer iterablen Datenstruktur (z.B. ein Array) als Objekt mit den Attributen ``value``
(Wert) und ``done`` (boolean, Kette am Ende?) zurückgibt.

.. code-block:: javascript

    let heroes = ["Jessica", "Luke", "Daredevil", "Elektra", "Thor", "Odin"];

    let iterator = heroes.values();
    console.log(iterator);      // Array Iterator

    let iteratorReturnObj = iterator.next();
    console.log(iteratorReturnObj);     // Object { value: "Jessica",  done: false (Ende noch nicht erreicht) }
    iteratorReturnObj = iterator.next();
    console.log(iteratorReturnObj);     // "Luke"
    iteratorReturnObj = iterator.next();
    console.log(iteratorReturnObj);     // "Daredevil"
    iteratorReturnObj = iterator.next();
    console.log(iteratorReturnObj);     // "Elektra"
    iteratorReturnObj = iterator.next();
    console.log(iteratorReturnObj);     // "Thor"
    iteratorReturnObj = iterator.next();
    console.log(iteratorReturnObj);     // "Thor"
    iteratorReturnObj = iterator.next();
    console.log(iteratorReturnObj);     // value : undefined, done: true ---> heroes Array am Ende

    // eigenen Iterator erstellen
    // um eigenes Iterationsverhalten zu erzeugen

    // Aufgabe: Array in umgekehrter Reihenfolge durchlaufen (statt mit for-loop)
    function createIterator (array) {
        let counter = array.length - 1;
        return {
            next:   function() {
                if (counter < 0) {
                    return {
                        value: undefined,
                        done: true
                    }
                } else {
                    return {
                        value: array[counter--],
                        done: false
                    }
                }
            }
        };
    }

    // Iterator erzeugen
    let ownIterator = createIterator(heroes);
    let heroInObject = ownIterator.next();
    console.log(heroInObject);      // "Odin"
    heroInObject = ownIterator.next();
    console.log(heroInObject);      // "Thor"
    heroInObject = ownIterator.next();
    console.log(heroInObject);      // "Elektra"
    heroInObject = ownIterator.next();
    console.log(heroInObject);      // "Daredevil"
    heroInObject = ownIterator.next();
    console.log(heroInObject);      // "Luke"
    heroInObject = ownIterator.next();
    console.log(heroInObject);      // "Jessica"
    heroInObject = ownIterator.next();
    console.log(heroInObject);      // value: undefined, done: true

Generatoren
===========
Generatoren erlauben es, im Gegensatz zu Iteratoren, über for-Schleifen zu
iterieren.

.. code-block:: javascript

    // Generator-Function erstellen
    function* myGeneratorFunc() {
        console.log("Step 1");
        yield "Schritt 1";
        console.log("Step 2");
        yield "Schritt 2";
        console.log("Step 3");
    }

    // beim Aufruf der Generator-Function wird das Generator-Objekt erzeugt
    // Generator wird zurückgegeben - Funktion selbst nicht abgearbeitet
    let myGenerator = myGeneratorFunc();
    console.log(myGenerator);      // Generator { constructor: Iterator() }

    // ermöglicht, mehrere Generatoren auf Grundlage einer Generator-Function zu erzeugen
    // Generatoren zeigen alle das gleichen Iterations-Verhalten

    let aufruf = myGenerator.next();
    console.log(aufruf);        // Object { value: "Schritt 1", done: false }
    aufruf = myGenerator.next();
    console.log(aufruf);        // Object { value: "Schritt 2", done: false }
    aufruf = myGenerator.next();
    console.log(aufruf);        // Object { value: undefined, done: true }
    // weitere Aufrufe von next() können zu TypeError führen

    /*
        next()  - ähnlich wie bei Iteratoren
                - liefert Object mit Properties:
                    - value:    Rückgabe von yield
                    - done:     boolean, ob Ende der Generator-Funktion erreicht ist
        durch Aufruf von next() am Generator wird Generator-Funktion abgearbeitet
        bis zur Unterbrechung durch ein 'yield'. Dort wird beim nächsten Aufruf
        wieder eingesetzt und weiter abgearbeitet.
    */

    // über Generatoren iterieren
    // möglich, da Generator = Spezialfall eines Iterators
    let mySecondGenerator = myGeneratorFunc();

    for (let value of mySecondGenerator) {
        console.log("aus for-Schleife", value);
    }

    // unendlichen Generator erstellen
    function* counter() {
        let count = 0;
        while(true) {
            count++;
            let restart = yield count;
            if (restart) count = 0;
        }
    }

    let myCounter = counter();
    console.log(myCounter.next());      // Object { value: 1, done: false }
    console.log(myCounter.next());      // Object { value: 2, done: false }
    console.log(myCounter.next());      // ...
    console.log(myCounter.next());
    console.log(myCounter.next());
    console.log(myCounter.next());
    console.log(myCounter.next());
    console.log(myCounter.next());
    console.log(myCounter.next());
    console.log(myCounter.next());
    console.log(myCounter.next());      // Object { value: 11, done: false }
    console.log(myCounter.next(true));  // (XXX): Object { value: 1, done: false }
    console.log(myCounter.next());      // Object { value: 2, done: false }

    // (XXX): Das 'true' wird als Ausgabe für 'yield count' des VORHERIGEN next()
    // Aufrufs gesetzt. Dadurch wird beim Aufruf 'restart' der Wert 'true' zugewiesen
    // und dadurch der count auf '0' gesetzt.
    // 'yield' ist ebenso der EINSTIEGSPUNKT für den nächsten Aufruf von 'next()'
    // ein Wert, der über 'next(einWert)' übergeben wird, wird als der Rückgabewert
    // des yield-statements gesetzt


    // Generatoren als Iterator nutzen
    const counting = (start, end) => ({
        *[Symbol.iterator] () {
            while (start % end) {
                yield start++;
            }
        }
    });

    // the *[Symbol.iterator]

    for (let count of counting(1,25)) console.log(count);

Module
======
Seit ES6 verfügbar. Alles JS-Module laufen im strikten Modus (``"use strict";``
ist nicht mehr nötig).

Vor ES6: ``common.js`` war eine Bestrebung, Modulunterstützung zu integrieren.
Wird nicht mehr oft verwendet.

Siehe Anwendung in ``Tag_20/module/`` Dateien.
