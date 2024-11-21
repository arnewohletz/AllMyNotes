DOM - Document Object Model
===========================
Browser analysiert HTML Datei und legt die Elemente als Objekte in einen
Speicher, das DOM, ab -> "rendern".

* Es besteht aus Knoten, den sogenannten Nodes
* Es gibt *Element-Knoten*, *Text-Knoten* und *Kommentar-Knoten*. Knoten können
  auch verschachtelt sein (z.B. Satz mit einzelnem Wort als Link)
* Das oberste Element ist der ``document`` Knoten: dieser enthält zahlreiche Infos
  zum Dokument und zahlreiche Methoden um das Dokument zu bearbeiten.

.. hint::

    Erreichbar über :menuselection:`Developer Tools --> DOM`.

Beispiele:

.. code-block:: javascript

    console.log(document); // gesamtes Dokument Element ausgeben
    console.log(document.body); // body Element des Dokuments

    // Zugriff auf beliebige Elemente (sind JS Objekte)
    document.getElementById("id");  // => Element
    document.getElementByTagName("tagname");  // => HTML-Collection
    document.getElementByClassName("classname");  // => HTML-Collection
    document.getElementsByName("name");  // => HTML-Collection

Die Methoden können auf alle Elemente angewendet werden und werden dann auf alle
innenliegenden Elemente zugreifen. Mit **JQuery** ist jedoch eine zielgerichtetere
Suche nach bestimmten Elementen möglich. Jedoch kamen mit ES6 zwei neue Selektoren
hinzu, die wiederum die Anwendung von JQuery nicht mehr nötig machen.

Query-Selector
--------------
Neu seit ES6 (von JQuery inspiriert):

.. code-block:: javascript

    document.querySelector("css-syntax");  // => Element
    document.querySelectorAll("css-syntax");  // => NodeList (moderne Version von HTML-Collection)

    console.log(document.querySelector("h1"));  // Element: erstes Match wird zurückgegeben
    console.log(document.querySelector("h2"));
    console.log(document.querySelectorAll("h2"));  // NodeList: alle Matches werden zurückgegeben
    console.log(document.querySelectorAll("h2")[1]);  // Element an index 1

Content-Zugriff
---------------
Zugriff auf Inhalt von Elementen, inklusive Unter-Elementen (wenn vorhanden).

.. hint::

    Zugriffe auf das DOM sind das Nadelöhr für eine Webseite. Daher sollten Zugriffe
    auf das DOM möglichst minimal gehalten werden, d.h.

    * vorhanden DOM Element als Variablen ablegen
    * neue Elemente vorab anfertigen, bevor sie ins DOM geschrieben werden

Mit ``.innerHTML`` wird der Content inklusive aller Markups (Element-Tags) geliefert.

.. code-block:: javascript

    let headLine = document.querySelector("h1");

    // [element].innerHTML => liefert den Content Text inklusive Markups
    console.log(headLine.innerHTML);

    // überschreiben vom Text Content
    headLine.innerHTML = "<em>Hallo</em> Welt";
    console.log(headLine.innerHTML);

.. hint::

    Die ursprüngliche HTML Seite wird durch Änderung **nicht** verändert. Die Änderung
    erfährt nur das DOM.

.. code-block:: javascript

    // hinzufügen von Text
    headLine.innerHTML = "Achtung: " + headLine.innerHTML;
    headLine.innerHTML += "!!!";  // hinten anfügen

    // gesamter Content wird geschrieben
    headLine.innerHTML +=  " mit             Zusatz <span style=\"display:none\">unsichtbar</span>";

Den gerenderten Content (so wie User es sieht -> Ohne Markups, ohne doppelte Leerzeichen
oder ausgeblendete Inhalte) wird über ``.innerText`` sichtbar:

.. code-block:: javascript

    headLine.innerHTML +=  " mit             Zusatz <span style=\"display:none\">unsichtbar</span>";
    console.log(headLine.innerHTML);
    // Achtung: <em>Hallo</em> Welt!!! mit             Zusatz <span style="display:none">unsichtbar</span>
    console.log(headLine.innerText); // "Achtung: Hallo Welt!!! mit Zusatz"

Über ``.textContent`` werden doppelte Leerzeichen ausgegeben, aber keine Markups
oder ausgeblendete Inhalte.

.. code-block:: javascript

    headLine.innerHTML +=  " mit             Zusatz <span style=\"display:none\">unsichtbar</span>";
    console.log(headLine.textContent); // Achtung: Hallo Welt!!! mit             Zusatz unsichtbar

.. TODO: // .innerText = gerenderter Content (keine ausgeblendeten Elemente, keine Markups -> Users)
// .textContent = AM PERFORMANTESTEN: so wie im Inspektor (mit doppelten Leerzeichen, mit ausgeblendeten Inhalte, aber keine Markups)


.. hint::

    ``.innerText`` und ``.textContent`` sind performanter, als ``.innerHTML``,
    aber enthalten weniger Informationen. Es kommt auf den Anwendungsfall an,
    welches Property ausgelesen werden soll.

NodeList
--------
Im Gegensatz zu JQuery, welche die Ergebnis-Elemente als Liste von Objekten zurückgibt,
sind auf eine NodeList diese Methoden nicht direkt verfügbar. Die NodeList enthält
wiederum diese Objekte.

.. code-block:: javascript

    let listItems = document.querySelectorAll("li");
    console.log(listItems);

    // Anzahl der selektierten Elemente
    console.log(listItems.length);

    console.log(listItems.innerHTML); // undefined -> nicht verfügbar

    for (let i = 0; i < listItems.length; i++) {
        console.log(listItems[i]);  // OK
        console.log(listItems[i]).innerHTML;
    }

Bei nicht vorhandenen Elementen wird ``null`` zurückgegeben bzw. ein leeres
``NodeList`` Element. Hier mit einer einfachen Prüfung arbeiten:

.. code-block:: javascript

    // Element nicht vorhanden
    let orderedList = document.querySelector("ol");
    console.log(orderedList);  // null
    console.log(orderedList.innerHTML);  // TypeError

    // prüfe ob Element im DOM vorhanden (Zugriffsfehler vermeiden)
    if (orderedList) {
        console.log(orderedList.innerHTML);
    }

    // Bei querySelectorAll
    let orderedLists = document.querySelectorAll("ol");
    console.log(orderedLists);  // empty NodeList

    if (orderedList.length) {
        // hier nur wenn NodeList nicht leer
    }

Globales vs lokales Selektieren
-------------------------------
* Global: über ``document`` Objekt
* Lokal: über ein *Element* (innerhalb aller eingeschlossenen Elemente)

.. code-block:: javascript

    // global selektieren (über document)
    let myList = document.querySelector("#secondList");
    let listItems = document.querySelectorAll("li");

    console.log(myList);
    console.log(listItems);

    // lokales selektieren (innerhalb eines Elements)
    listItems = myList.querySelectorAll("li");
    console.log(listItems);

DOM-Zugriff auf Class-Attribut
------------------------------
Das ``class`` Attribute von Elementen manipulieren. Die ``className`` Attribut
ist die performanteste Methode, es gibt auch die Möglichkeit über ``classList``
(``DOMTokenList``, ein Array-artiges Gebilde) Klassen zu verwalten, welches
weitere Methoden liefert.

.. code-block:: javascript

    /*
        Variante 1:
        [element].className => speichert Strings
        Manipulation über Zeichenkettenverarbeitung
    */
    let para = document.querySelector(".absatz");
    console.log(para.className);
    para.className = "wichtig";  // className überschreiben
    para.className += " absatz texte";  // Klassen hinzufügen

    /*
        Variante 2:
        [element].classList

    */
    console.log(para.classList);  // => DOMTokenList

    // Anzahl der am Element anliegeneden Klassen
    console.log(para.classList.length);

    // Zugriff über Property Access
    console.log(para.classList[1]);  // "absatz"
    }

``classList`` Methoden:

    * ``.add()`` fügt Klassen hinzu (keine doppelten erlaubt)
    * ``.remove()`` entfernt eine Klasse
    * ``.replace()`` ersetzt eine Klasse
    * ``.toggle()`` fügt eine Klasse hinzu wenn nicht vorhanden, sonst wird
      diese entfernt
    * ``.contains()`` prüft ob eine Klasse einem Element anhängt (alternativ auch
      über Property Access)

.. code-block:: javascript

    para.classList.add("hinweis");  // Klasse hinzufügen
    para.classList.add("hinweis");  // Versuch doppeltes Hinzufügen wird ignoriert

    para.classList.remove("texte");  // Klasse entfernen

    para.classList.replace("absatz", "new-absatz");  // Klasse ersetzen
    para.classList.replace("fehlt", "fehlt-immer-noch");

    /*
    toggle:
        wenn Klasse vorhanden -> wird entfernt
        wenn Klasse nicht vorhanden -> wird hinzugefügt
    */
    para.classList.toggle("wichtig");

    console.log(para.classList);

    // auf Klasse prüfen
    if (para.classList.contains("hinweis")) {
        console.log(para.classList.contains("hinweis"));  // true
    }

    // durch classList iterieren über Property Access
    for (let i = 0; i < para.classList.length; i++) {
        console.log(para.classList[i]);
    }

Zugriff auf Attribute von HTML-Elementen
----------------------------------------
Content-Zugriff
```````````````
Über ``.getAttribute()`` wird Inhalt eines Attributs geliefert (oder ``null``,
falls Attribut nicht existiert):

.. code-block:: javascript

    let myProgress = document.querySelector("progress");


    // Attribute auslesen
    // [element].getAttribute(attr_name);
    // Rückgabe ist immer ein String

    console.log(myProgress.getAttribute("max"));  // "10"
    console.log(myProgress.getAttribute("value"));  // "1"
    console.log(myProgress.getAttribute("title"));  // null

Über ``.setAttribute()`` den Wert eines Attributs ändern oder neue Attribute
hinzufügen:

.. code-block:: javascript

    // Attribute setzen
    myProgress.setAttribute("max", 100);
    myProgress.setAttribute("value", 8);
    myProgress.setAttribute("id", "progress-bar");   // neues Attribut

Über ``.removeAttribute()`` ein vorhandenes Attribut entfernen. Ist das Attribut
nicht vorhanden, wird der Befehl ignoriert (kein Fehler):

.. code-block:: javascript

    // Attribut entfernen
    myProgress.removeAttribute("id");
    console.log(myProgress.getAttribute("id")); // null

Über ``.hasAttribute()`` prüfen ob ein Element ein bestimmtes Attribut hat:

.. code-block:: javascript

    // prüfen ob eine Attribut anliegt
    console.log(myProgress.hasAttribute("id"));   // true
    console.log(myProgress.hasAttribute("max"));  // false

Über ``.attributes`` alle Attribute eines Elements in einer ``NamedNodeMap``
erhalten:

.. code-block:: javascript

    console.log(myProgress.attributes);   // NamedNodeMap

    // etwas umständlich, aber möglich
    console.log(myProgress.attributes.max);   // max="100"
    console.log(myProgress.attributes.max.nodeValue);   // "100"

IDL-Zugriff
```````````
IDL ... Interface Description Language

Einfacher als Content-Zugriff, allerdings ist der Zugriff nur möglich, wenn
das Element als Interface definiert ist.

Vorteile:

- einfachere Notation
- Der Rückgabewert erfolgt im exakten Datentyp, nicht stets als String

Nachteile:

- Funktioniert nur über ein Interface

.. code-block:: javascript

    // IDL-Zugriff
    let myProgress = document.querySelector("progress");

    // Attribut auslesen
    // (direkter Zugriff über Punktnotation anstelle Weg über Methoden)
    console.log(myProgress.max);   // 100 (number)
    console.log(myProgress.value);  // 8 (number)

    // Attribut setzen
    myProgress.max = 8;
    myProgress.value = 5;
    console.log(myProgress.max);   // 8 (number)
    console.log(myProgress.value);  // 5 (number)

Sonderfall: Boolesche Attribute
```````````````````````````````
Attribute, welche ohne Wert das Verhalten eines Elements beeinflussen

Beispiele: ``async``, ``defer``, ``disabled``, ``required``

Über Content-Zugriff:

.. code-block:: javascript

    let myBtn = document.querySelector("button");

    // mit Content-Zugriff

    // boolesches Attribut setzen
    // doppelte Übergabe nötig (Wert des 2. Arguments jedoch egal)
    myBtn.setAttribute("disabled", "disabled");

    // boolesches Attribut entfernen
    myBtn.removeAttribute("disabled");

    // boolesches Attribut toggeln
    myBtn.toggleAttribute("disabled");  // hinzufügen
    myBtn.toggleAttribute("disabled");  // entfernen

Über IDL-Zugriff (wieder einfacher):

.. code-block:: javascript

    let myBtn = document.querySelector("button");

    // mit IDL-Zugriff
    myBtn.disabled = true;
    myBtn.disabled = false;

Interface Zugriff
`````````````````
Der Content-Zugriff kann **nicht** auf Interfaces zugreifen, dies ist nur über
den IDL-Zugriff möglich.

.. code-block:: javascript

    let eingabeFeld = document.querySelector("#eingabe");

    console.log(eingabeFeld.getAttribute("value"));   // "Hey"
    console.log(eingabeFeld.value); // "Hey"

    // Änderung über Content
    eingabeFeld.setAttribute("value", "Hey, du da");
    console.log(eingabeFeld.getAttribute("value"));   // "Hey, du da"
    console.log(eingabeFeld.value); // "Hey, du da"

    // Änderung über IDL
    eingabeFeld.value = "Hoppla";
    console.log(eingabeFeld.getAttribute("value"));   // "Hey, du da"  (hat nicht geklappt)
    console.log(eingabeFeld.value); // "Hoppla"  (OK)

    // Änderung bei Nutzer-Eingabe
    eingabeFeld.onchange = function() {
        console.log(eingabeFeld.getAttribute("value"));   // NOK -> alter Wert
        console.log(eingabeFeld.value);   // OK -> neuer Wert
    };

**Fazit:**

* Bei Nutzereingaben muss immer über IDL gegangen werden  --> bei Dokument im DOM
* Vorherige Werte lassen sich auch über Content Zugriff geholt  --> bei Dokument im Speicher

Events
======
Auf Vorgänge, die während der Laufzeit auftreten können (z.B. Maus- & Tastatureingaben)
kann mit einem anderen Ereignis reagiert werden. Es gibt dafür zwei Möglichkeiten:

* Event-Listener
* Event-Handler

.. important::

    Um zu verhindern, dass Events mehrfach registriert werden, stets mit dem Event-Handler
    arbeiten, nicht mit dem Event-Listener.

Event-Listener
--------------
eine Funktion wird an das Element (z.B. Button), welches eine
Ereignis erfährt, registriert. Tritt das Ereignis ein, wird die Funktion ausgeführt.
Es können **mehrere Funktionen für das selbe Event** für ein Element definiert
werden, wobei die Funktionen **hintereinander ausgeführt** werden.

.. code-block:: javascript

    let inputField = document.querySelector("#eingabe");

    function log_msg (msg) {
        console.log(msg);
    }

    // anonyme Funktion als ersten Event-Listener für 'blur' event registrieren
    // NACHTEIL: Kann nicht de-registriert werden, da anonyme Funktion
    inputField.addEventListener("blur", function() {
        console.log("Ich bin nicht mehr selektiert");
    });
    // anonyme Funktion zweiter Event-Lister für 'blur' event registrieren
    // beide Funktionen werden nun ausgeführt beim Eintritt des Events
    // NACHTEIL: Kann nicht de-registriert werden, da anonyme Funktion
    inputField.addEventListener("blur", function() {
        log_msg("Selektiere mich bitte erneut");
    });

    function onBlurHandler() {
        console.log("Ich mach das ...");
    }

    function onBlurHandlerWithArgs(event) {
        console.log(event.type);
    }

    // benannte Funktion als dritten Event-Listener für 'blur' event registrieren
    inputField.addEventListener("blur", onBlurHandler);

    // de-registrieren von drittem Event-Listener
    // GEHT NUR BEI BENANNTEN FUNKTIONEN!
    inputField.removeEventListener("blur", onBlurHandler);

    // benannte Funktion mit Argument als Event-Listener für 'blur' registrieren
    inputField.addEventListener("blur", (event) => onBlurHandlerWithArgs(event));

    // de-registriere Funktion mit Argumenten als Event-Listener
    inputField.removeEventListener("blur", onBlurHandlerWithArgs);

.. note::

    The ``blur`` event is fired, when the element has lost focus (e.g. user selects
    a different element).

DOMContentLoaded Event Listener
```````````````````````````````
.. TODO: EventListener für DOMContentLoaded event dokumentieren

Feuert etwas früher, wie ``load``event. Siehe Dokumentation.

Event-Handler
-------------
Ist eine Eigenschaft eines Elements, welche direkt **einer** Funktion
zugewiesen werden kann. Diese wird ebenfalls beim Eintreten des Ereignisses
ausgeführt. Es gibt hier nur eine Funktion. Sobald die Eigenschaft einer anderen
Funktion zugewiesen wird, wird die bisherige Zuweisung überschrieben.

.. note::

    Jeder Event-Handler beginnt mit ``on`` plus dem *Event Namen* und kann in den
    Elementen nachgeschaut werden. Event-Handler Properties sind alle im lower-Case,
    ohne Trennzeichen, geschrieben (z.B. ``onclick``).

.. code-block:: javascript

    let inputField = document.querySelector("#eingabe");

    function log_msg (msg) {
        console.log(msg);
    }

    // Event-Handler für 'blur' event zuweisen
    inputField.onblur = function() {
        log_msg("Ich handle das allein");
    };

    // Event-Handler für 'blur' event wird überschrieben
    inputField.onblur = function() {
        log_msg("Denkste! Ich bin jetzt der Chef! Hinfort!");
    };

    function gibMeldungDazu() {
        console.log("Das Event ist wirklich eingetreten");
    }

    // Ausgelagerte Funktion als Event-Handler registrieren (OHNE Klammern übergeben)
    inputField.onfocus = gibMeldungDazu;
    console.log(gibMeldungDazu);  // function
    console.log(gibMeldungDazu());  // undefined (da kein Return-value)

    // Event-Handler de-registrieren (auf 'null' setzen)
    inputField.onfocus = null;

DOM-Event-Handler
`````````````````
Der ``onload`` Event-Handler wird erst nach abgeschlossenen Laden des DOMs und allen
verknüpften Resources (CSS, Bilder, usw.) aufgerufen.

.. code-block:: javascript

    let inputField = document.querySelector("#eingabe");

    // DOM-Event-Handler
    window.onload = function() {
        console.log("DOM und alle verknüpften Ressourcen fertig geladen");
    };
