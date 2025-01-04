JSON Requests
=============
Genauso wie mit XML Daten, können auch JSON Daten auf eine Anfrage zurückgegeben
werden. Wenn JSON möglich ist, sollte stets dieses Format gegenüber XML bevorzugt
werden.

Anfrage senden
--------------
Zum Senden einer Anfrage wird zunächst das XMLHttpRequest-Object (XHR) erstellt:

.. code-block:: javascript

    // 1. XHR-Object erstellen
    let xhr = new XMLHttpRequest();

Daraufhin wird ein Event-Handler erzeugt, welcher auf die Server-Antwort wartet:

.. code-block:: javascript

    // 2. Event-Handler
    xhr.onload = function() {
        if (xhr.status != 200) {
            output.textContent = "Allgemeiner Verarbeitungsfehler";
            return;
        }
    }

Bei modernen Browsers werden die Rückgabedaten automatisch geparst und in ein Objekt
überführt. In älteren Browsern muss dies manuell durchgeführt werden.

Eine Fallunterscheidung kann dafür sorgen, dass beide Varianten unterstützt werden:

.. code-block:: javascript

    // Fähigkeitenweiche (modern <-> alt)
    let jsonData;
    if (xhr.responseType == "json") jsonData = xhr.response;
    else (jsonData = JSON.parse(xhr.responseText));

Als nächstes muss über ``.open()`` die HTTP-Anfrage formuliert werden.

.. code-block:: javascript

    // 3. Anfrage formulieren
    xhr.open("GET", "./artists.json");

Die Anfrage lässt sich weiterhin konfigurieren. Hier wird über ``.responseType``
der Rückgabetyp der Daten definiert, in diesem Fall ``"json"``, was einem
JSON-Dokument entspricht.

.. code-block:: javascript

    // 4. Anfrage konfigurieren
    xhr.responseType = "json";

Die Anfrage wird zuletzt mit ``.send()`` ausgeführt.

.. code-block:: javascript

    // 5. Anfrage an Server übermitteln
    xhr.send();

Die Daten werden als Objekt zurückgegeben und können weiterverarbeiten werden
(siehe Tag_11/JSON-Daten_mit_Ajax_laden/js/script.js)

Übungen
=======
JSON Daten über AJAX laden
--------------------------
siehe Tag_11/browser-json

HTML Snippets über AJAX laden
-----------------------------
siehe Tag_11/login-register

Vollständige HTML Seiten über AJAX laden
----------------------------------------
siehe Tag_11/login-register-html-Seiten

Über ``[XNLHttpRequest].responseXML`` erhält man ein ``Document`` Objekt mit dem
geparsten HTML oder XML.

.. important::

    Eine Konstante (``const``) bedeutet nicht, dass das Objekt, auf welches die
    Konstante verweist, unveränderlich ist, sondern lediglich, dass diese
    Referenzvariable nicht später auf ein anderes Objekt verweisen darf.

.. important::

    Mit ``[old].replaceWith([new])`` wird das bisherige Objekt ``elem`` aus dem DOM
    genommen und das neue Objekt ``new`` eingefügt. Eine Referenz, welches bislang
    auf ``old`` verwiesen hat, weißt nun auf ``new``.

Verlaufshistorie
================
Über ``window.history`` oder ``History`` Objekt kann auf die Historie der anzeigten
Seiten im Browser zugegriffen werden.

.. hint::

    Beim Ausführen von AJAX-Operationen entstehen **keine** Einträge in der Historie
    erstellt. Oft soll dieser Komfort jedoch für den Nutzer möglich sein.
    Dann müssen diese manuell erstellt werden.

:``history.length``:
    Anzahl der History -Einträge

:``history.back()``:
    Eine Seite im Verlauf zurückgehen

:``history.forward()``:
    Eine Seite im Verlauf vorangehen

:``history.go()``:
    Lade Seite mit einer relativen Referenz zur aktuellen Seite:

    * ``history.go(-1)``: Eine Seite zurück gehen
    * ``history.go(-5)``: Fünf Seiten zurück gehen
    * ``history.go(1)``: Eine Seite voran gehen
    * ``history.go(3)``: Drei Seiten voran gehen

Verlaufseinträge erstellen
---------------------------
Über ``history.pushState( state-object, title, relative-URL)`` wird ein neuer
Verlaufseintrag erstellt.

.. hint::

    Der Browser verwendet für seinen Einträge keine state-Objekte.

.. code-block:: javascript

    // Verlaufseintrag erstellen
    history.pushState(
        { pageId: linkName },    // state-object
        linkContent,
        hyperRef
    )

Durch Verlaufseinträge navigieren
–--------------------------------
Über popstate-Ereignis

    * wird immer bei Navigation durch ``history`` ausgelöst
    * gibt state-object zurück, das mit ``pushState`` übergeben wurde

Der ``state`` Objekt ist Teil des ``event`` Objekts, welches in jeden Event-Handler
Funktion verfügbar ist.

.. code-block:: javascript

    window.onpopstate = function(event) {
        // Event-Objekt ist in jeder Event-Handler Funktion verfügbar

        // Das State-Objekt wird ebenfalls als Teil des Event-Objects übergeben
        // Muss ausgelesen werden
        console.log(event.state);  // gibt das

        // für ersten Aufruf einer Seite wird KEIN state Objekt in der History
        // gespeichert, da dies der erste Aufruf ist (das event.state Objekt ist 'null').
        // In diesem Fall wird die Hauptseite (index.html) geladen
        if (event.state) {
            loadContent(event.target.pageID + ".html");
        }
        else {
            loadContent("index.html");
        }
    }

.. hint::

    **Zweigleisig fahren**

    Es bietet sich an, beide Möglichkeiten für das Laden von neuen Inhalten zu
    implementieren (per AJAX UND per JavaScript):

    * Bei AJAX: nicht lesbar für Suchmaschinen
    * Bei JavaScript: geht nicht, wenn Nutzer JavaScript deaktiviert

    Die Performance-Einbußen sind in der Regel vertretbar.
