Rest-Parameter
==============
Der Rest-Parameter umfasst alle Argumente innerhalb einer Funktion, die NICHT als
Parameter in der Funktionsdeklaration erfasst wurden (sogenannte *überzählige*
Argumente).

.. important::

    **Übergabe von Argumenten an eine Funktion**

    Was passiert mit *überzähligen* Argumenten?

    .. code-block:: javascript

        // Übergabe von Argumenten an Funktion
        // was passiert mit überzähligen Argumenten

        function jessyDatas (name, age, address) {
            console.log(name, age, address);
            console.log(arguments);   // arguments = Arguments Objekt -> enthält alle übergebenen Argumente
            for (let arg of arguments) {
                console.log(arg);
            }
            console.log(arguments.length);
            console.log(arguments[3]);
        }

        jessyDatas("Jessica", 36, "Dragonroad 66", 165, 65);

Seit ES6 verfügbar. Enthält **nur** die *überzähligen* Parameter.

.. code-block:: javascript

    /*
        Rest-Parameter seit ES6
        ...params - Syntax fasst zusammen
        nimmt überzählige Argumente auf (die nicht von Parametern aufgefangen wurden)
        liefert Array mit überzähligen Argumenten
    */

    function jessyDatas2 (name, age, address, ...params) {
        console.log(name, age, address);
        console.log(params);   // params = Arguments Objekt -> enthält nur überzählige Argumente
        console.log(params.length);
        params.forEach( arg => console.log(arg));
    }

    jessyDatas2("Jessica", 36, "Dragonroad 66", 165, 65);

    let add = (...params) => params.reduce( (a,b) => a + b, 0);  // '0' ist Initialwert
    console.log(add(2,3));  // 5
    console.log(add(1,2,3,4,5,6,7,8,9));  // 45

    let greeting = (floskel, ...heroes) =>
        heroes.forEach(hero => console.log(`${floskel} ${hero}`));
    greeting("Heyho", "Jessy", "Luke", "Thor", "Odin");     // Heyho Jessy -> Heyho Luke -> ...

    let heroArr = ["Jessy", "Luke", "Thor", "Odin", "Elektra"];
    greeting("Hi", ...heroArr);   // Hi Jessy -> Hi Luke -> ...

Events und Event-Object
=======================
Events durchlaufen drei Phasen:

#. Capturing-Phase (Window --> Target / "from top down to target")
#. Target-Phase
#. Bubbling-Phase (Target --> Document / "from bottom up to document"):
   Standardmäßig wird hier auf Event reagiert

.. code-block:: none

    [element].addEventListener(
        event,          Event-Type
        function,       aufzurufende Funktion
        useCapture      Phase der Aktivierung bei Elementen welche höher in DOM sind als Target
                        true: Event wird bereits in Capturing-Phase ausgelöst
                        false: Event wird erst in Bubbling-Phase ausgelöst
                        (Default: false)
    )

Beispiel:

.. code-block:: none

                     | |  / \
    -----------------| |--| |-----------------
    | element1       | |  | |                |
    |   -------------| |--| |-----------     |
    |   |element2    \ /  | |          |     |
    |   --------------------------------     |
    |        W3C event model                 |
    ------------------------------------------

Bei Klick auf ``element2`` wird bei

.. code-block:: javascript

    element1.addEventListener('click',doSomething2,true)
    element2.addEventListener('click',doSomething,false)

das Event auf ``element1`` bereits in der Capturing-Phase, also **vor** ``element2``
ausgeführt, sprich, ``doSomething2`` erfolgt vor ``doSomething``.

Bei

.. code-block:: javascript

    element1.addEventListener('click',doSomething2,false)
    element2.addEventListener('click',doSomething,false)

hingegen durchläuft das Event ``element1`` ohne das der Handler reagiert, es wird
daraufhin zuerst ``doSomething`` ausgeführt, dann beginnt die Bubbling-Phase, erst
dann wird bei Wieder-Hochlaufen ``doSomething2`` ausgeführt.

.. code-block:: javascript

    let bodyTag = document.body;
    bodyTag.addEventListener("click", () => console.log("Body hat in Bubbling-Phase reagiert"), false);
    bodyTag.addEventListener("click", () => console.log("Body hat in Target-Phase reagiert"), true);

    let link_1 = document.querySelector("nav li:first-of-type a");
    let link_2 = document.querySelector("nav li:last-of-type a");
    let item_1 = link_1.parentNode;
    let item_2 = link_2.parentNode;

    /*
        event.preventDefault()
        unterdrückt Standardverhalten von Links, Formularen etc.

        event.stopPropagation()
        unterbindet Weitergabe des Events - Eventfluss wird unterbrochen
    */

    link_1.addEventListener("click", (event) => {
        event.preventDefault();
        console.log("Event hat Link 1 in Target-Phase erreicht");
    });
    item_1.addEventListener("click", () => console.log("Event hat Item 1 erreicht"));

    link_2.addEventListener("click", (event) => {
        event.stopPropagation();
        console.log("Event hat Link 2 in Target-Phase erreicht");
    });
    item_2.addEventListener("click", () => console.log("Event hat Item 2 erreicht"), true);

    /*
        generelle Eigenschaften des Event-Objektes
        [event].type            - Event-Typ
        [event].target          - Element, auf dem Event ausgeführt werden (alternativ zu 'this')
        [event].currentTarget   - Element, auf dem Handler registriert wurde
        [event].timeStamp       - Zeitpunkt des Ereignisses
        [event].eventPhase      - Ereignisphasen (1,2,3)

        [event].cancelable      - true / false
        Abfrage geeignet, um herauszufinden, ob ein Ereignis, das mit Standardaktion
        verbunden, dieses durch Aufruf von preventDefault() unterbrochen werden kann
    */

    let liste = document.querySelector("#liste");

    // "click" reagiert NUR auf die linke Maustaste
    liste.addEventListener("mousedown", (event) => {

        // Event-Objekt
        console.log(event);     //  mousedown { target: li, buttons: 1, ... }

        // Event, das direkt vom Ereignis betroffen
        console.log(event.target);  // li-Element

        // Element, auf dem Event registriert wurde
        console.log(event.currentTarget);   // ul (Parent)

        // Event-Phase ermitteln
        console.log(event.eventPhase);  // 3 --> Bubbling-Phase

        let phaseObj = {
            1: "Capturing -Phase",
            2: "Target-Phase",
            3: "Bubbling-Phase"
        }
        console.log(phaseObj[event.eventPhase]);

        //  Maustaste, die gedrückt wurde
        console.log(event.button);

        let mouseObj = {
            0: "Linke Maustaste",
            1: "Mittlere Maustaste",
            2: "Rechte Maustaste"
        };
        console.log(mouseObj[event.button]);  // z.B. 0 --> Linke Maustaste

        // Kontextmenü unterdrücken (Bei Klick mit rechter Maustaste)
        liste.oncontextmenu = function(event) {
            event.preventDefault();
            // return false;    // hier auch möglich
        };
    });

    // Tastatur-Ereignisse
    let field = document.querySelector("#field");

    let keyPressFunc = function(event) {
        console.log(event.key);
        console.log(event.which);  // Tastatur-Code der Taste
        if (event.shiftKey) console.log(event.which, "mit Umschalttaste");
    };
    field.addEventListener("keypress", keyPressFunc);

    let klicker = function(event) {
        console.log("Bildschirm-X-Position", event.screenX);
        console.log("Bildschirm-Y-Position", event.screenY);
        console.log("Browser-X-Position", event.clientX);
        console.log("Browser-Y-Position", event.clientY);
    }
    document.onclick = klicker;

    // window-scroll-Ereignis
    window.addEventListener("scroll", () => {
        console.log(scrollX, scrollY);
    });

    /*
        EventListener und once
        EventListener hat zusätzliche Option 'once' - diese entfernt Event-Listener
        automatisch nach 1. Auftreten des Events

                [elem].addEventListener(event, function,  {once: true});

        Aufräumen und Ausschalten des Listeners erfolgt automatische
        das hält Code übersichtlicher und Speicherverwaltung effizienter
        -> alle Variablen die zum callback gehören werden vom garbage collector gelöscht

        Event-Listener wird automatisch gelöscht, sofern dieser nicht mehr gebraucht wird.
    */

    liste.addEventListener("mousedown", function(event) {
        console.log("einmaliges Ereignis", event.eventPhase);
    }, {once: true, capture: true})

Destructuring
=============
Werte aus Arrays und Objekten extrahieren und in passende Variablen / Konstanten
überführen. Prinzip des Destructuring (destrukturierende Anweisung) ermöglicht es,
Werte, die in Objekten oder Arrays hinterlegt sind, relative einfach an
Variablen / Konstanten zuzuweisen.

Array-Destructuring
-------------------
.. code-block:: javascript

    let heroes = ["Jessy", "Luke", "Odin", "Elektra"];

    // ohne Destructuring
    let hero_1 = heroes[0];
    let hero_2 = heroes[1];
    let hero_3 = heroes[2];
    let hero_4 = heroes[3];

    // Array auf Grundlage von Variablen erstellen
    let heroArr = [hero_1, hero_2, hero_3, hero_4];

    // mit Destructuring
    let [one, two, three, four, five] = heroes;
    console.log(one, two);
    console.log(five);  // undefined, da überzählig

    // Destructuring für Funktions-Parameter nutzen
    function getNames ([one, two, three, four]) {
        console.log(three, four);
    };
    getNames(heroes);

    // bei existierenden Variablen entfällt 'let'
    // Arbeit mit default-Werten ist möglich
    [one, two, three, four = "a hero", five = "no hero"] = heroArr;
    console.log(four);  // Elektra
    console.log(five);  // no hero

    // nur bestimmte Werte extrahieren
    let [myHero1,,,myHero4] = heroes;
    console.log(myHero1, myHero4);

    // Werte aus mehrdimensionalen Arrays überführen
    let coords = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ];

    let [
        [a,b,c],
        [d,e,f],
        [g,h,i]
    ] = coords;

    console.log(a,e,i);  // 1 5 9

Objekt-Destructuring
--------------------
.. code-block:: javascript

    let favHero = {
        firstName: "Jessica",
        lastName: "Jones"
    };

    let {
        firstName:  firstFromObj,
        lastName:   lastFromObj
    } = favHero;
    console.log(firstFromObj, lastFromObj);     // Jessica Jones

    // einfacher, wenn key-Bezeichner = Variablen-Bezeichner
    let {
        firstName,
        lastName
    } = favHero;
    console.log(firstName, lastName);      // Jessica Jones

    // Werte aus geschachtelten Objekten
    let jessyData = {
        firstName:  "Jessica",
        age:        36,
        address: {
            postCode:   111,
            street:     "Dragonroad 66",
            city:       "Hells Kitchen"
        }
    }
    let {
        firstName: heroFirst,
        age,
        address: {
            postCode:   zip,
            street,
            number,
            city
        }
    } = jessyData;
    console.log(heroFirst, age, zip, street, city);     // Jessica 36 111 Dragonroad 66 Hells Kitchen
    console.log(number);    // undefined, da keine Entsprechung im Objekt

    // 'let' entfällt, wenn Variable bereits vorhanden
    ({firstName} = jessyData);  // runde Klammern notwendig, damit Destructuring erkannt wird
    console.log(firstName);

Kombination Array- und Object-Destructuring
-------------------------------------------
.. code-block:: javascript

    let jessyData = {
        firstName:  "Jessica",
        age:        36,
        address: {
            postCode:   111,
            street:     "Dragonroad 66",
            city:       "Hells Kitchen"
        },
        phone: [
            "0172-567894321",
            "999-66339955"
        ]
    };

    let {
        firstName,
        address: { city },
        phone:  [mobile, office]
    } = jessyData;

    console.log(firstName, city, mobile, office);  // Jessica Hells Kitchen 0172-567894321 999-66339955

    let marvelHeroes = [
        {
            name:       "Odin",
            contact:    {
                mail:   "odin@valhalla.org",
                phone:  "534698721"
            }
        },
        {
            name:       "Thor",
            contact:    {
                mail:   "thor@valhalla.org",
                phone:  "534698721"
            }
        },
        {
            name:       "Luki",
            contact:    {
                mail:   "loki@valhalla.org",
                phone:  "534698721"
            }
        },
    ];

    // Destructuring in for-Schleife nutzen
    for (let { name, contact: { mail, phone } } of marvelHeroes) {
        console.log(name, mail, phone);   //  Odin odin@valhalla.org 534698721 -> ...
    }

    // Destructuring für Parameter einer Funktion nutzen
    let chefchen = {
        name:       "Odin",
        contact:    {
            mail:   "odin@valhalla.org",
            phone:  "534698721"
        }
    };

    function heroMail( { contact: { mail } } ) {
        console.log(mail);  // odin@valhalla.org
    }
    heroMail(chefchen);

Factory-Function
================
Über eine Factory-Funktion kann ein Objekt als Rückgabewert einer Funktion
definiert werden. Dazu muss das Objekt in runde Klammern ``()`` geschrieben
werden, damit die Objektklammern (``{}``) nicht als Funktions-Klammern
fehlinterpretiert werden bzw. der Interpreter diese eindeutig als Objekt-Klammern
erfassen kann:

.. hint::

    Die Factory-Funktion definiert, wie ein Objekt aussehen soll. Sie gibt das
    Objekt beim Aufruf mit den definierten Argumenten aufgerufen wird, zurück.

.. code-block:: javascript

    // runde Klammern nötig, damit {} als Objekt-Klammern und nicht als Funktions-Klammern
    // interpretiert werden
    // hier: implizit wird erstelltes Objekt zurückgegeben
    const createUserObj = (user, avatar) => ({
        user,
        avatar,
        setName(newName) {
            this.user = newName;
            return this;
        }
    });

    let user1 = createUserObj("Jessy", "jessy_avatar.png");
    let user2 = createUserObj("Luke", "luke_face.jpg");

    console.log(user1);
    console.log(user2);
    console.log(user1.setName("Pinky"));    // überschreibt Namen

Constructor-Function
====================
Sollten IMMER mit Großbuchstaben beginnen. Muss mit ``new`` aufgerufen werden: erstellt
ein neues Objekt und gibt es zurück.

.. code-block:: javascript

    function Item (prodName, prodPrice, prodCat, prodQty) {
        this.name = prodName;
        this.price = prodPrice;
        this.cat = prodCat;
        this.qty = prodQty;
        this.shortPrint = function() {
            return  `${this.name} - ${this.price} EUR`;
        };
    };
    // Instanziieren
    let prod_1 = new Item("Talisker", 49.99, "Whiskey", 500);
    let prod_2 = new Item("Chivas Regal", 29.99, "Office Drinks", 1000);

    console.log(prod_1);
    console.log(prod_2);
    console.log(prod_1.shortPrint());

    let prod_3 = new Item("Talisker Limited Edition", 359.99, "HomeDrinks", 250);
    prod_3.slogan = function(msg) {
        return `${this.name} ${msg}`;
    };

    console.log(prod_3.slogan("in der limitierten Sonderauflage"));
    // console.log(prod_2.slogan("in der limitierten Sonderauflage"));   // geht nicht!

Über ``.prototype`` lassen sich Attribute, also Funktionen oder Variablen an
Objekte hinzufügen, welche auf alle, auch bereits instantiierten, Instanzen
eines Objekt angewendet werden:

.. code-block:: javascript

    // Nachträgliche Funktion für alle Objekt-Instanzen definieren (auch wenn Objekte schon
    // instantiiert)
    Item.prototype.slogan = function(msg) {
        return `${this.name} ${msg}`;
    }
    console.log(prod_2.slogan("in der limitierten Sonderauflage"));   // das geht!

    // prototype war lange Zeit wichtig, um Browser neue Methoden beizubringen
    // mittlerweile nicht mehr so bedeutend, da alle Browser auf ähnlichem Stand sind

Über ``instanceof`` kann geprüft werden ob ein Objekt sich von einem anderen Objekt
ableitet, d.h. ob sich die Prototypenkette des einen Objekts in dem zweiten wiederfindet.

.. code-block:: javascript

    // instanceof-Operator  (in gleicher Prototypenkette wie ...)
    // prüfen ob ein Objekt von einem anderen ableitet - diesen als Prototypen haben
    console.log(prod_2 instanceof Item);    // true
    console.log(prod_2 instanceof Object);  // true
    console.log(prod_2 instanceof Array);   // false
