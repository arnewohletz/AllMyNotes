Object.create()
===============
Seit ES6 ist ``Object.create()`` immer seltener im Einsatz (kommt von ES5):

.. code-block:: javascript

    // Object-Erstellung auf Grundlage eines Prototypen

    // Prototyp
    let whiskey = {
        name:       "",
        cat:        ["Whiskey"],
        price:      0,
        quantity:   500,
        shortPrint () {
            console.log(`${this.cat[0]}: ${this.name} - ${this.price}`);
        },
        slogan(msg) {
            console.log(`${this.name} - ${msg}`);
        }
    };

    console.log(whiskey);
    whiskey.shortPrint();

    // Objekt auf Grundlage des Prototypen erstellen
    let newProd = Object.create(whiskey);  // alle vererbten Eigenschaften unter 'prototype'
    console.log(newProd);
    console.log(newProd.price);
    // eigene Daten definieren
    //    wird direkt im Objekt hinzugefügt
    newProd.name = "Shivas Regal";
    newProd.price = 29.99;
    //    Referenz-Objekt, daher wird Wert unter 'prototype' verändert
    newProd.cat.unshift("Office Drinks");

    console.log(newProd);
    console.log(newProd.price);
    newProd.shortPrint();

    console.log(whiskey);   // Referenz-Objekt (cat) wurde AUCH HIER verändert, da Referenz-Objekt

Eigenschaftsattribute
=====================
Für Eigenschaften eines Objekts lassen sich Attribute definieren. Falls diese
nicht gesetzt werden, gilt der Default.

.. code-block:: javascript

    /*
        zur Konfiguration von Object-Properties

        Attribut        Nutzung

        value           Wert einer Eigenschaft

        writable        gibt an, ob Eigenschaft überschreibbar ist
                        (nachträgliche Änderung des values)
                        default: false

        enumerable      gibt an, ob Eigenschaft iterierbar ist
                        (ob sie in Iteration geliefert wird)
                        default: false

        configurable    gibt an, ob Eigenschaft konfigurierbar ist
                        (ob sie bspw. gelöscht werden kann)
                        default: false

        set             definiert Funktion, mit der schreibend auf Eigenschaft
                        zugegriffen werden kann (nur für Zugriffseigenschaften)

        get             definiert Funktion, mit der lesend auf Eigenschaft
                        zugegriffen werden kann (nur für Zugriffseigenschaften)
    */

    // Prototyp, der eine Methode beinhaltet

    let heroActions = {
        getHeroDatas () {
            return `${this.name} (${this.age} wohnt in ${this.address})`;
        }
    };

    // Objekt auf Grundlage des Prototypen erstellen
    let hero = Object.create(heroActions, {
        name:   {
            // initialer Wert der Eigenschaft
            value:          "Jessica",
            writable:       true,   // Eigenschaft ist überschreibbar
            enumerable:     true,   // Eigenschaft ist iterierbar
            configurable:   true    // Eigenschaft ist konfigurierbar
        },
        age:    {
            value:          36
        },
        address:    {
            value:          "Dragonroad",
            writable:       true
        }
    });

    hero.name = "Elektra";  // OK
    // hero.age = 29;   // TypeError: "age" is read-only
    // delete hero.age;   // TypeError: property "age" is non-configurable and can't be deleted
    // delete hero.address;  // TypeError: property "address" is non-configurable and can't be deleted
    hero.address = "Alexanderplatz 111, Berlin";  // OK
    console.log(hero);

    for (let key in hero) {
        console.log(key);  // nur 'name' und 'getHeroDatas' (Rest nicht iterierbar)
        // prototype-Einträge werden standardmäßig ebenfalls berücksichtigt

        // nur EIGENE Eigenschaften berücksichtigen
        if (hero.hasOwnProperty(key)) {
            console.log(key);   // nur 'name'
        }
    }

Neue Properties in Prototypen definieren
========================================
.. code-block:: javascript

    Object.prototype.print = function() {
        console.log("print-function", this);
    }

    // hero Objekt von oben
    hero.print();

    NodeList.prototype.giveBack = function() {
        console.log("giveBack hello");
    };

    document.querySelectorAll("li").giveBack();  // OK, da NodeList diese Methode hat
    // document.querySelector("li").giveBack();   // NOK, da Node diese Methode nicht hat

    // Event mit on() registrieren
    Node.prototype.on = function (event, fn) {
        this.addEventListener(event, fn);
        return this;
    };

    Node.prototype.off = function (event, fn) {
        this.removeEventListener(event, fn);
        return this;
    };

    let giveAlert = function() {
        alert("Es hat Klick gemacht");
    };
    document.querySelector("li").on("click", giveAlert);    // Event-Listener registrieren
    document.querySelector("li").off("click", giveAlert);   // Event-Listener de-registrieren

Prototype einem Objekt zuordnen
===============================
Mittlerweile über die ``Object.setPrototypeOf()`` um einen Prototypen für ein
Objekt zuzuweisen.

.. code-block:: javascript

    /*
        setzen / zuordnen eines Prototypen
        __proto__ (deprecated) || Object.setPrototypeOf()
    */

    // Prototyp, der Methode beinhaltet
    let heroActions = {
        getHeroDatas () {
            return `${this.name} (${this.age} wohnt in ${this.address})`;
        }
    };
    let heroDatas = {
        name:       "Jessica Jones",
        age:        36,
        address:    "Dragonraod 66"
    };

    // Object.setPrototypeOf(object, prototype);
    // Füge 'heroActions' unter Prototypenn von 'heroDatas' hinzu
    Object.setPrototypeOf(heroDatas, heroActions);

    console.log(heroDatas.getHeroDatas());

Klassensyntax
=============
JS macht kein "richtiges" OOP, es fühlt sich aber so an.

.. code-block:: javascript

    class Product {

        // constructor = Herzstück der Klasse
        // wird beim Instaniziieren zuerst ausgeführt
        constructor(prodName, prodPrice, prodCat, prodQty) {
            this.name = prodName;
            this._price = prodPrice;  // '_' um Property nicht mit Setter zu verwechseln
            this.cat = prodCat;
            this.qty = prodQty;
        }

        // über 'get' wird Funktion als Getter gekennzeichnet und ist nun eine Eigenschaft
        get shortPrint() {
            return `${this.name}: ${this._price} EUR (${this.qty} Stück auf Lager)`;
        }
        // hier kann arrow-function verwendet werden, da Objekt bereits erzeugt ist
        // Funktion wird im Objekt selbst verankert
        logThis = () => console.log(this);

        // über 'set' wird Funktion als Setter gekennzeichnet und ist nun eine Eigenschaft
        // Eigenschaft/Funktion wird im 'prototype' verankert
        set addQty(qty) {
            this.qty += qty;
        }

        set subQty(qty) {
            (this.checkQty(qty)) ? this.qty -= qty : console.log("unzureichender Lagerbestand");
        }

        checkQty(qty) {
            return (this.qty - qty > 1);
        }

        get price() {
            return this._price;
        }

        set price(newVal) {
            this._price = newVal;
        }

    };

    let newProd = new Product("Talisker", 49.99, "Whiskey", 500);
    console.log(newProd);
    newProd.logThis();

    // geht nicht mehr wegen 'set' Bezeichner ...
    // newProd.subQty(250);
    // newProd.addQty(100);
    // newProd.subQty(500);
    // ... muss nun als Eigenschaft verändert werden
    newProd.subItem = 250;
    newProd.addItem = 100;
    newProd.subItem = 500;
    console.log(newProd);
    console.log(newProd.shortPrint);

    /*
        Bezeichner für Getter und Setter müssen sich von Eigeschaften unterscheiden,
        damit es nicht zu Endlos-Rekursionen, Stack-Überlauf und letztlich
        Programmabsturz kommt

        oft werden Eigenschaften, auf die nicht direkt zugregriffen werden soll,
        mit '_' geprefixt - dannn sind Zugriffsmethoden vorhanden!

        Jede Klasse in eigenem Skript verorten!
    */

Eigenschaftsattribute für Properties setzen
-------------------------------------------
.. code-block:: javascript

    // Vorhandene Property
    // -------------------

    //     im Objekt sind alle schon vorhandenen Attribute standardmäßig überschreibbar,
    //     sofern die Eigenschaftattribute nicht anders gesetzt wurden
    Object.defineProperty(newProd, "name", {
            writable: false
        }
    );
    //    bei Erzeugung von Objekten werden Eigenschaftsattribute auf 'true' gesetzt,
    //    wenn sie ohne Konfiguration der Eigenschaftsattribute erzeugt wurden

    // newProd.name = "whatever";  // TypeError: "name" is read-only

    // Neue Property
    // -------------
    Object.defineProperty(newProd, "desc", {
        value: "Best Quality Whiskey",
        enumerable: true
    });

    // newProd.desc = "BliBlaBlub";  // TypeError: "desc" is read-only

    for (let key in newProd) {
        console.log(key);
    }

Arbeit mit Settern und Gettern der Eigenschaftsattribute
--------------------------------------------------------
Über ``Object.defineProperty()`` wird eine neue Property an ein bereits vorhandene
Instanz eines Objekts hinzugefügt:

.. code-block:: javascript

    let qualityVal = "Fine Best Strong...";
    Object.defineProperty(newProd, "quality", {
        get() {
            return qualityVal;
        },
        set(newVal) {
            qualityVal = newVal;
        },
        enumerable: true
    });

    console.log(newProd);
    newProd.quality = "Finest";
    console.log(newProd.quality);

Kind-Klasse erstellen (Klassen erweitern)
-----------------------------------------

.. code-block:: javascript

    class LtdProduct extends Product {
        constructor (name, cat, price, qty, limit) {
            // immer zuerst super() aufrufen! (sonst Fehler)
            // danach neue / spezielleren Eigenschaften hinzufügen
            super(name, price, cat, qty);
            this.limit = limit;
        }
        // Methoden der Elternklasse stehen zur Verfügung
        // könnt diese nutzen, ändern oder überschreiben

        set addQty(qty) {
            (this.checkLimit(qty)) ? super.addQty = qty : console.log("Limit überschritten");
        }

        checkLimit(qty) {
            return !(this.qty + qty > this.limit);
        }
    }

    let ltdProduct = new LtdProduct("Talisker Limited Edition",
        "Home Drinks", 399.50, 250, 500);
    console.log(ltdProduct);
    ltdProduct.subQty = 59;
    console.log(ltdProduct.shortPrint);
    ltdProduct.addQty = 50;

Statische Objekt-Eigenschaften (Methoden & Properties)
------------------------------------------------------
Statische Eigenschaften und Methoden können nur auf der **Klasse** angewandt
werden, nicht auf der Instanz dieser Klasse.

.. code-block:: javascript

    // Statische Methoden
    // -> Anwendung nur auf Klasse, nicht auf Instanzen

    class Product {

        constructor(prodName, prodPrice, prodCat, prodQty, prodArt) {
            this.name = prodName;
            this._price = prodPrice;
            this.cat = prodCat;
            this.qty = prodQty;
            this.art = prodArt;
        }

        get shortPrint() {
            return `${this.name}: ${this._price} EUR (${this.qty} Stück auf Lager)`;
        }

        logThis = () => console.log(this);

        set addQty(qty) {
            this.qty += qty;
        }

        set subQty(qty) {
            (this.checkQty(qty)) ? this.qty -= qty : console.log("unzureichender Lagerbestand");
        }

        checkQty(qty) {
            return (this.qty - qty > 1);
        }

        get price() {
            return this._price;
        }

        set price(newVal) {
            this._price = newVal;
        }

        // Statische Methode
        static getWhiskey() {
            return {
                SL:     "Scotch",
                BB:     "Bourbon",
                IRE:    "Irish"
            };
        };

        // Statische Eigenschaft innerhalb der Klasse definieren
        // Achtung: stets im SCREAMING_SNAKE_CASE schreiben
        static artObj = {
            SL:     "Scotch",
            BB:     "Bourbon",
            IRE:    "Irish"
        }

    };

    // Statische Eigenschaft außerhalb eines Objekts definieren  -> VERALTET!!
    Product.WHISKEY_ART = {
        SL:     "Scotch",
        BB:     "Bourbon",
        IRE:    "Irish"
    }

    let newProd = new Product("Glennfiddich", 39.99, "Whiskey", 500, Product.getWhiskey().IRE);
    let newProd2 = new Product("Glennfiddich", 39.99, "Whiskey", 500, Product.artObj.IRE);
    let newProd3 = new Product("Glennfiddich", 39.99, "Whiskey", 500, Product.WHISKEY_ART.IRE);

    console.log(newProd);
    console.log(newProd2);
    console.log(newProd3);

    /*
        statische Methoden und Eigenschaften:
            - werden direkt auf Klasse aufgerufen
            - werden nicht vererbt => sind also auf Instanzebene nicht verfügbar
    */

    console.log(newProd.artObj);        // undefined
    console.log(newProd.WHISKEY_ART)    // undefined

Symbole in Klassen
------------------
Über ``Object.getOwnPropertySymbols()`` lassen sich alle Symbole eines Objekts
zurückgeben:

.. code-block:: javascript

    const DOG_NAME = Symbol("dogname");

    class Dog {
        constructor (name) {
            this[DOG_NAME] = name;  // muss über Property-Access definiert werden
        }

        get name () {
            return this[DOG_NAME];
        }

        set name(newVal) {
            this[DOG_NAME] = newVal;
        }
    }

    let myDog = new Dog("Snoopy");
    myDog.name = "Leika";
    console.log(myDog.name);

    console.log(Object.getOwnPropertySymbols(myDog));
    myDog[Object.getOwnPropertySymbols(myDog)[0]] = "Moja";
    console.log(myDog.name);

Seit ES10 ist es möglich mit ``#`` eine private Eigenschaft zu definieren:

.. code-block:: javascript

    // private Eigenschaften (beginnt mit '#')
    // erst seit ES10 möglich
    // -> Zugriff nur innerhalb der Klasse, nicht von außerhalb
    class HomeAnimals {
        #anzahl;
        #initialCount;

        constructor(count = 0) {
            this.#initialCount = count;
            this.reset(count);
        }

        reset(value = this.#initialCount) {
            this.#anzahl = value;
        }

        addAnimal (count = 1) {
            this.#anzahl += count;
        }

        subAnimal (count = 1) {
            this.#anzahl -= count;
        }

        get actCount() {
            return this.#anzahl;
        }
    }

    let myAnimals = new HomeAnimals();
    console.log(myAnimals);

    myAnimals.addAnimal(3);
    myAnimals.addAnimal();
    myAnimals.reset(2);
    myAnimals.subAnimal();

    console.log(myAnimals.actCount);

    console.log(myAnimals["#anzahl"]);    // undefined --> da private Eigenschaft
    console.log(HomeAnimals["#anzahl"]);    // undefined --> da private Eigenschaft

