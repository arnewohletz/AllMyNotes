Objekte
=======
Objekte besitzen

    * Eigenschaften: objektgebundene Variablen oder Konstanten
    * Methoden: objektgebundene Funktionen

Erstellung
----------
Über Literal-Schreibweise (üblicher)

.. code-block:: javascript

    let myObj = {};  // leeres Objekt
    console.log(myObj);

Über Constructor-Funktion

.. code-block:: javascript

    let myNewObj = new Object();  // leeres Objekt
    console.log(myNewObj);

Eigenschaften definieren
------------------------
Über Komma-separierte, key-value Paare. Das Kontext- Schlüsselwort ``this``
erlaubt den Zugriff auf das derzeitige Objekt.

.. code-block:: javascript

    let book = {
        mainTitle:          "JavaScript",
        subTitle:           "kurz und gut",
        target:             "Anfänger und Fortgeschrittene",
        price:              49.99,
        "Händler Preis":    19.99,  // key als String angelegt
        showTitle:          function() {
                                // console.log(book.mainTitle);  // nicht so
                                console.log(this.mainTitle, this.subTitle);  // nutze 'this'
                            }
    };

    console.log(book);  // Eigenschaften haben keine definierte Reihenfolge

Property-Keys (Eigenschaft) mit Sonderzeichen lassen sich per String definieren
(hier: "Händler Preis"), müssen dann über Property Access ausgelesen werden
(siehe unten).

Eigenschaft auslesen
--------------------
Über die Punkt-Notation des Objekts:

.. code-block:: javascript

    console.log(book.mainTitle);
    console.log(book.price);

Über den Property Access:

Wenn der Bezeichner als String vorliegt oder als String angelegt wurde, ist
der Zugriff über die Punktnotation nicht möglich. Hier muss über den
*Property Access* erfolgen

.. code-block:: javascript

    console.log(book."Händler Preis"); // geht nicht!!
    console.log(book["Händler Preis"]); // OK! Über Property Access

Eigenschaft ändern
------------------
Genauso wie auslesen über Punktnotation oder Property Access.

.. code-block:: javascript

    book.mainTitle = "Python";
    console.log(book.mainTitle); // "Python"
    book["Händler Preis"] = 30.00
    console.log(book["Händler Preis"]); // 30.00

Eigenschaft hinzufügen und löschen
----------------------------------
Über ``delete`` löschen.

.. code-block:: javascript

    // neue Eigenschaft
    book.inStock = true;
    delete book.inStock;
    console.log(book.inStock); // undefined

Methoden aufrufen
-----------------
Über die Punktnotation.

.. code-block:: javascript

    book.showTitle();  // Python kurz und gut

Objektdefinition in ES6
-----------------------
In ES6 können Variablen als gleichnamige Eigenschaften in Objekte eingefügt werden.

.. code-block:: javascript

    let price = 42.99, cat = "Office Drinks";

    // ES5
    let product_1 = {
        name:       "Talisker",
        prince:     price,
        cat:        cat
    }
    console.log(product_1);

    // ES6
    let  product_2 = {
        name: "Glenfiddich",
        price,
        cat,
        sellerPrice: (price -15)
    }
    console.log(product_2);

Beispiel: Date Objekt
---------------------
Allerhand Möglichkeiten zum Erhalten, Manipulieren und Ausgeben von Datum und Uhrzeit.

.. code-block:: javascript

    // erzeugen
    let today = new Date();
    console.log(today);

    // getter
    console.log(today.getDate()); // Tag im Monat (1 ... 31)
    console.log(today.getMonth()); // Monat (0 - 11)
    console.log(today.getDay()); // Wochentag (0 - 6, 0 = Sonntag)
    console.log(today.getFullYear()); // Jahr
    console.log(today.getHours()); // Uhrzeit Stunde
    console.log(today.getMinutes()); // Uhrzeit Minute
    console.log(today.getSeconds()); // Uhrzeit Sekunde
    console.log(today.getMilliseconds()); // Uhrzeit Millisekunde

    // JS-TimeStamp (Millisekunden seit 1.1.1970, Unix Timestamp * 1000)
    console.log(today.getTime());
    console.log(Date.now());

    // setter
    // Bestandteile Datum ändern
    let newDate = new Date();
    newDate.setFullYear(2224); // Jahr
    newDate.setMonth(11); // Monat (April)
    newDate.setDate(24); // Tag im Monat
    newDate.setHours(20);
    newDate.setMinutes(30);
    newDate.setSeconds(0);

    console.log(newDate);

    // mit Datum rechnen
    today.setDate(today.getDate() - 1);
    today.setDate(today.getDate() + 42);

    console.log(today);

    // Datum mit Date-String erzeugen
    console.log(new Date("Dec 24 2024 20:30:00"));
    console.log(new Date(2024,11));
    console.log(new Date(2024,11,6,19,23,15));

    let myDate = new Date(1111111111111111); // timestamp (epoch time)
    myDate.setTime(1111111111111);
    console.log(myDate);

    // UTC - Weltzeit
    let worldTime = new Date();
    worldTime.setUTCFullYear(2025);
    worldTime.setUTCMonth(5);
    worldTime.setUTCHours(15);

    console.log(worldTime); // Angabe der UTC Zeit -> wird in lokaler Zeit ausgegeben (e.g. CEST)
    console.log(worldTime.getUTCHours()); // 15

    // in UTC Zeit umwandeln
    let utcDate = new Date(Date.UTC(2024, 7, 31, 14, 42, 11));
    console.log(utcDate);

    // Zeitstring erzeugen
    console.log(utcDate.toUTCString());  // UTC Zeit: Sat, 31 Aug 2024 14:42:11 GMT
    console.log(utcDate.toString());  // lokale Zeitrechnung: Sat Aug 31 2024 16:42:11 GMT+0200 (Central European Summer Time)

    // Formatierte Ausgabe
    let now = new Date();

    let formatedDate = now.toLocaleString();  // formatierte Zeitausgabe
    formatedDate = now.toLocaleString("de-DE");  // deutsche Schreibweise
    formatedDate = now.toLocaleString("ko-KR");  //koreanische Scrheibweise

    formatedDate = now.toLocaleString("de-DE", { weekday: "long"});  // nur Wochentag in Langform (z.B. Freitag)

    // Datumsausgabe parametrisieren
    const OPTIONS =  {
        weekday: "long",
        month: "long",
        day: "numeric",
        year: "numeric",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit"
    }
    formatedDate = now.toLocaleString("de-DE", OPTIONS); // z.B. Freitag, 15. November 2024 um 12:19:51

    // nur Datum-Strings erhalten
    formatedDate = now.toLocaleDateString();
    // nur Uhrzeit erhalten
    formatedDate = now.toLocaleTimeString();
    // nur Stunde erhalten
    formatedDate = now.toLocaleTimeString("de-DE", {hour: "2-digit"}); // z.B. 12 Uhr

    console.log(formatedDate);
