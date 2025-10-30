Arrow-Function
==============
Verkürzte Schreibweise einer Funktion. Seit ES6 verfügbar.

* Schlüsselwort function entfällt
* dafür wird fat arrow (``=>``) gesetzt
* wenn nur ein Parameter übergeben wird, können () entfallen

Syntax:

.. code-block:: javascript

    let bezeichner = () => {};
    let bezeichner = para => {};
    let bezeichner = (para1, para2) => {};

Bei kurzen Statements können ``{}`` weggelassen werden. Hier wird der Wert
des Statements implizit zurückgegeben:

.. code-block:: javascript

    let bezeichner = (p1,p2) => p1 * p2;

Bei mehreren Statements müssen ``{}`` hingegen gesetzt werden.

Das Schlüsselort ``this`` verhält sich in Arrow-Funktions anders, als in
regulärer definierten Funktionen:

.. code-block:: javascript

    /*
        Schlüsselwort 'this'

        mit 'this' spricht man innerhalb einer Objektmethode (oder Konstruktor)
        die jeweilige Objektinstanz an => das aktuelle Objekt / dieses Objekt (Kontext-Objekt)

        this = impliziter Parameter von Funktionen
        wird beim Aufruf der Funktion mit Kontext-Objekt belegt, auf dem Funktion aufgerufen wird
        this kann nicht geändert werden

        this referenziert immer Objekt, in dessen Kontext Funktion aufgerufen wird
        Ausnahme = arrow-Function
    */

    let person_1 = {
        firstName:  "Jessica",
        age:        36,
        myMethod () {
            console.log(this);  // Object {firstName: "Jessica", ...}
        }
    };

    person_1.myMethod();

    function myNewFunc() {
        console.log(this);  // undefined
    }
    myNewFunc(); // undefined


.. important::

    Arrow Funktionen haben **kein** eigenes Bindung für 'this' (ebenso 'arguments'
    und 'super') und sollten daher **nicht** für Methoden von Objekten verwendet werden.

    **Keine Arrow-Funktionen innerhalb von Objekten verwenden**

.. code-block:: javascript

    /*
        this befindet sich in Funktion außerhalb eines Objektes
        daher bezieht sich this auf umliegenden Raum und hat kein Kontext-Objekt => undefined
        ohne strikten Modus wird window-Object referenziert
    */

    function getName() {
        return this.firstName;
    }

    let getName2 = () => this.firstName;
    /*
        mit arrow-Function referenziert this das Objekt, in dem Funktion definiert wurde
        im strikten Modus -> this = undefined

        Kontext-Objekt von this = Objekt, in dem Funktion definiert ist
        nicht Kontext, in dem sie aufgerufen wird
    */

    let person_2 = {
        firstName:  "Jessica",
        age:        36,
        getName,
        getName2
    };
    console.log(person_2.getName());    // "Jessica"
    console.log(person_2.getName2());   // undefined
    // wenn Funktion in Objekt gezogen und auf diesem aufgerufen wird,
    // wird Bezug zum Kontext-Objekt hergestellt
    // arrow-Function nicht für ausgelagerte Funktionen mit Kontakt zu this erstellen!

    let person_3 = {
        firstName:  "Elektra",
        age:        28,
        myFunc() {
            let myInnerFunc = function() {
                console.log(this);
            };
            myInnerFunc();
        }
    };
    person_3.myFunc();  // undefined

    /*
        bei Nutzung von this in innerer Funktion fällt this aus Kontext heraus
        im stricten Modus => undefined
        sonst window-object
    */

    let person_4 = {
        firstName:  "Elektra",
        age:        28,
        myFunc() {
            let myInnerFunc = () => console.log(this);
            myInnerFunc();
        }
    };
    person_4.myFunc();  // Object { firstName: "Elektra", ... }

    /*
        um Bezug zum Objekt wieder herzustellen => arrow-Function nutzen
        this referenziert Kontext-Objekt, in dem innere Funktion definiert wird
         Objekt wird zurück gegeben
    */

    document.addEventListener("click", function() {
        console.log(this);
    }); // HTMLDocument
    document.body.addEventListener("click", function() {
        console.log(this);
    }); // <body>
    document.addEventListener("click", () => console.log(this));        // window
    document.body.addEventListener("click", () => console.log(this));   // window

    /*
        Zusammenfassung - Kontakt mit this

        wann normale Funktion - wann arrow-Function?
        - im Raum außerhalb von Objekten => funktionsdeklaration oder funktionsausdruck
        - in callback => arrow-function
        - innerhalb von objekt-Methoden => arrow-function
        - in Konstruktor-Funktionen => keine arrow Function zur Erzeugung von Objekten nutzbar

        Eigenschaften von arrow-Function:
        - referenzierter Wert von this ergibt sich aus Kontext, in dem Funktion definiert wirde!
          nicht aus Kontext, ion dem sie ausgeführt wird!
    */

Higher Order Functions
======================
Funktionen können als Argumente an andere Funktionen übergeben werden

.. code-block:: javascript

    function sayHello(nameFunc) {
        console.log(`Hallo ${nameFunc()}`);

    }

    function giveName () {
        return "Jessica";
    }
    sayHello(giveName);     // Hallo Jessica
    sayHello(function() {return "Luke";});    // Hallo Luke
    sayHello(() => "Odin");     // Hallo Odin

    let logHello = function (callbackfunction) {
        callbackfunction("Hallo Duda");
    };
    logHello(function(text) {console.log(text);});  // Hallo Duda

sort()
------
Sortiert anhand der UTF16-Zeichentabelle.

.. code-block:: javascript

    let heroes = ["Jessy", "Elektra", "Loki", "Thor"];
    console.log(heroes.sort());   // [ "Elektra", "Jessy", "Loki", "Thor" ]

``[Array].sort(compareFn)`` erlaubt eine Sortierfunktion, welche zwei Argumente (a und b)
benötigt. Rückgabewerte:

    * negativer Wert => a kommt vor b
    * positiver Wert => b kommt vor a
    * 0 oder NaN 0 => a und b sind identisch

.. code-block:: javascript

    let numbers = [1,5,99,11,22,20,3,10,62,63,6,600];

    let numberCheck = function(a,b) {
        console.log(`${a} - ${b} = ${a - b}`);
        return a - b;
    };
    console.log(numbers.sort(numberCheck)); //  [ 1, 3, 5, 6, 10, 11, ... ]

    /*
        sort() = higher order
        numberCheck() = callback

        callback wird an higher order übergeben
        wird von higher order eigenständig mit argumenten aufgerufen
        Verarbeitung in higher order erfolgt auf Grundlage des Rückgabewertes der callback
    */

    heroes = ["Jessica", "Luke", "Odin (Chef)", "Thor", "Elektra"];

    // Regel: Chef nach vorne, Rest alphabetisch
    let isChef = hero => hero.endsWith("(Chef)");
    let sortHeroes = (hero1, hero2) => {
        if (isChef(hero1)) return -1;  // Chef schon vorne --> nicht sortieren
        if (isChef(hero2)) return 1;    // Chef hinten --> nach vorne sortieren
        return (hero1 > hero2) ? 1 : -1;
        // ist hero1 hinter hero2 --> nicht sortieren, daher positiv
        // ansonsten --> sortiere, daher negativ
    };
    console.log(heroes.sort(sortHeroes));   // [ "Odin (Chef)", "Elektra", "Jessica", "Luke", "Thor" ]

forEach()
---------
Als Ersatz für eine for-Schleife für Arrays.

.. code-block:: javascript

    /*
        ersetzt for-Schleife für Arrays
        durchläuft Array Element für Element
        erwartet callback

        übergibt an callback:
            1. Array-Element
            2. index-Position   --> optional
            3. Ursprungsarray   --> optional

        erwartet keinen Rückgabewert von callback
        lässt sich auf NodeList anwenden - aber nicht auf HTMLCollection
    */

    let jahresZeiten = ["Frühling", "Sommer", "Herbst", "Winter", "Eiszeit"];

    // array element, index-position, ursprungsarray
    jahresZeiten.forEach( (elem, index, array) => {
        console.log(index, elem);   // 0 Frühling -> 1 Sommer -> ...
        console.log(array);  // [ "Frühling", "Sommer", "Herbst", "Winter", "Eiszeit" ]
    });

    // nur array element
    let numbers = [1,5,99,11,22,20,3,10,62,63,6,600], sum = 0;
    numbers.forEach( zahl => sum += zahl);
    console.log(sum);  // 902

    // array element, index position
    let paraList = document.querySelectorAll("p");
    console.log(paraList);
    paraList.forEach( (tag, i) => console.log(i, tag.textContent)); // 0 text -> 1 text -> ...

map()
-----
Durchläuft ein Array Element für Element und erstellt ein neues Array, wobei
jedes Element durch eine Callback-Funktion verändert werden kann.

.. code-block:: javascript

    /*
    durchläuft Array Element für Element
    erwartet callback

    übergibt an callback:
        1. Array-Element
        2. index-Position
        3. Ursprungsarray

    erwartet Rückgabewert von callback
    erstellt ZielArray (Kopie des Arrays)
    Rückgabewerte der Callback werden Zielarray geschrieben

    lässt sich nicht auf arrayartige Gebilde anwenden
    mit Array.from() kann arrayartiges Gebilde in Array konvertiert werden
    */

    let heroes = ["Jessica", "Luke", "Odin", "Thor", "Elektra", "Nebula"];

    let makePassword = (hero, i) => {
        let password = i;
        password += hero.split("").reverse().join("")  // Name spiegeln
        password += hero.length;
        return password;
    };

    let passwordArray = heroes.map(makePassword);
    console.log(passwordArray);     // [ "0acisseJ7", "1ekuL4", ... ]

    // oder... (mit Arrow-Function)

    let numbers = [1,5,99,11,22,20,3,10,62,63,6,600]
    let squares = numbers.map( zahl => Math.pow(zahl, 2) );
    console.log(squares);   // [ 1, 25, 9801, ... ]

filter()
--------
Mit ``.filter()`` lassen sich Einträge in einem Array filtern.

.. code-block:: javascript

    /*
    durchläuft Array Element für Element
    erwartet callback, in der Bedingungsprüfung stattfindet

    übergibt an callback:
        1. Array-Element
        2. index-Position
        3. Ursprungsarray

    erwartet Rückgabewert (boolean) von callback
    erstellt ZielArray mit Elementen, auf die callback mit true geantwortet hat
    Bedingungsprüfung findet in callback statt

    lässt sich nicht auf arrayartige Gebilde anwenden
    mit Array.from() kann arrayartiges Gebilde in Array konvertiert werden
    */

    let heroes = ["Jessica", "Luke", "Odin", "Thor", "Elektra", "Nebula"];
    let avengers = heroes.filter( hero => hero.length > 4 );
    console.log(avengers);      // [ "Jessica", "Elektra", "Nebula" ]

    let filtered = [1,42,52,53,62,99,111,7,9,3].filter( zahl => zahl > 9);
    console.log(filtered);  // [ 42, 52, 53, 62, 99, 111 ]

reduce()
--------
Reduziert Elemente eines Arrays auf einen einzelnen Wert.

.. code-block:: javascript

    /*
        reduziert Elemente eines Arrays auf einen einzelnen Wert
        benötigt callback, in der Reduktion definiert wird
        reduce() übergibt 2 Argumente an callback
        callback reduziert auf einzelnen Wert und gibt diesen zurück
        reduce() übergibt Rückgabewert mit nächstem Array-Element
        ...
        bis nur noch ein Wert vorhanden ist (= Rückgabewert von reduce)

        lässt sich nicht auf arrayartige Gebilde anwenden
        mit Array.from() kann arrayartiges Gebilde in Array konvertiert werden
    */

    let numbers = [1,5,99,42,53,62,11,9,73];

    let add = (a,b) => {
        console.log(`${a} + ${b} = ${a + b}`);
        return a + b;
    };
    let total = numbers.reduce(add);
    console.log(total);     // OK: 355

    let sum = array => array.reduce(add);
    console.log(sum([52,63,41,11]));    // OK: 167
    console.log(sum([52]));   // 52 wird zurückgegeben
    // console.log(sum([]));  // Uncaught TypeError: reduce of empty array with no initial value

    /*
        Initialwert kann als 2. Argument an reduce() übergeben werden
        Wert muss zur Reduktion passen
        dient der Vermeidung von TypeError bei Übergabe eines leeren Arrays
    */
    let sumWithInitial = array => array.reduce(add, 0);
    console.log(sumWithInitial([]));    // 0

    // reduceRight(cbf [, initial value])
    // arbeitet wie reduce(), jedoch von rechts nach links

Array prüfen
------------
.. code-block:: javascript

    /*
        every()     - prüft, ob ALLE Elemente einer Bedingung entsprechen
        some()      - prüft, ob MINDESTENS EIN Element einer Bedingung entspricht

        higher order übergibt ein Array-Element an callback function
        in callback function wird anhand definierter Bedingung geprüft und boolean
        als Ergebnis zurückgegeben
        Rückgabe der higher order = boolean
    */

    let numbers = [2,21,42,3,9];
    let even = zahl => {
        console.log(zahl, !(zahl % 2));
        return !(zahl % 2);
    };

    console.log(numbers.every(even));   // false
    console.log(numbers.some(even));    // true

Elemente finden
---------------
Über ``find()``, ``findIndex()`` sowie ``findLast()``, ``findLastIndex()``
lassen sich Elemente in einem Array finden.

.. code-block:: javascript

    let numbers = [21,42,3,10,9];
    let even = zahl => {
        console.log(zahl, !(zahl % 2));
        return !(zahl % 2);     // even: !0 --> true; odd: !1 --> false
    };

    /*
        find()
        liefert 1. Element eines Arrays, dass einer in callback function
        definierten Bedingung entspricht
        ohne Fund: undefined
    */
    console.log(numbers.find(even));    // 42

    /*
        findIndex()
        liefert die Indexposition eines Elements in einem Array,  dass einer
        in callback function definierten Bedingung entspricht
        ohne Fund: -1
    */
    console.log(numbers.findIndex(even));   // 1

    /*
        findLast() und findLastIndex() funktionieren genau so wie find() und
        findIndex(), arbeiten jedoch von rechts nach links
    */
    console.log(numbers.findLast(even));    // 10
    console.log(numbers.findLastIndex(even));   // 3

Spread-Syntax
=============
Werte aus Objekten oder Arrays werden aufgeteilt, als einzelne Werte übergeben.

.. code-block:: javascript

    /*
        ...bezeichner
        Syntax teilt Werte von Arrays und Objekten auf
    */

    let add = function(a = 0, b = 0, c = 0, d = 0) {
        console.log(a,b,c,d);
        console.log(a + b + c + d);
    };

    let numbers = [42,62,99,11];
    add(...numbers);    // Elemente von numbers werden einzeln übergeben

    console.log(Math.max(...numbers));  // 99
    console.log(Math.min(...numbers));  // 11

    // für Arrays
    let obst = ["Apfel", "Kirsche", "Pflaume", "Birne"];
    let mehr_obst = ["Banane", "Kiwi", "Orange", ...obst, "Mandarine"];
    console.log(mehr_obst);

    // für Objekte
    let user = {
        name:   "Jessica",
        age:    36,
        status: "angry"
    };
    let marvelHero = {
        subject:    "Comic Hero",
        ...user,
        vote:       42
    };
    console.log(marvelHero);

    // Beispiel: Date-Object

    let dateArr = [2024,11,11];
    let date = new Date(...dateArr);
    console.log(date);

Unterschiede beim Duplizieren von Objekten
------------------------------------------
Die Spread-Syntax sollte nicht für das Erstellen von Objekten verwendet werden,
da hier Referenzen übergeben werden.

.. code-block:: javascript

    const myUser = {
        name:       "Jessy",
        age:        36,
        address:    {
            street: "dragonroad",
            number: 66,
            city:   "Hells Kitchen"
        }
    };
    const myUser2 = {...myUser};       // Vorsicht: myUser2 referenziert Attribute von myUser (keine Kopie)!
    myUser2.name = "Luke"

    const myUser3 = JSON.parse(JSON.stringify(myUser));
    const myUser4 = structuredClone(myUser);

    myUser.address.number = 111;

    console.log(myUser);    // ok
    console.log(myUser2);   // ok   --> Hausnummer wird auch geändert!
    console.log(myUser3);   // ok
    console.log(myUser4);   // ok

    console.log(myUser.address.number);    // ok
    console.log(myUser2.address.number);   // ok   --> Hausnummer wird auch geändert!
    console.log(myUser3.address.number);   // ok
    console.log(myUser4.address.number);   // ok

    // Die Spread-Syntax übermittelt Werte als Referenzen. Wird das Ursprungs-Objekt
    // verändert, wird dies auch auf die Referenzen angewandt

    // => Besser keine Objekte mit Spread-Syntax duplizieren!

.. warning::

    Die Spread-Syntax erzeugt **flache** Kopien, d.h. nur Referenzen werden
    erzeugt.
