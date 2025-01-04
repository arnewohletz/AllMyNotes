AJAX
====
Begriff Ajax wurde 2005 von Jesse James Garrett geprägt.

Ajax steht als Abkürzung für **Asynchronous JavaScript and XML** (asynchrones JavaScript
und XML) doch Ajax-Anwendungen nicht asynchron im Sinne, dass Kommunikation mit
Server völlig losgelöst von Benutzereingaben stattfindet. Auch XML nicht
zwangsläufig Übertragungsformat für Daten zwischen Client und Server.

„Ajax“ => JavaScript-gestützter Datenaustausch mit Webserver im Hintergrund.

* XML => ein mögliches, aber nicht zentrales Übertragungsformat
* asynchron => JavaScript-Ausführung blockiert beim Warten auf Server-Antwort
  nicht Browser, JavaScript-Ereignisse werden gefeuert, wenn Server-Antwort eingetroffen
* funktioniert also über selbsterzeugte HTTP-Anfragen, Server-Antwort steht Script
  zur Verfügung
* neu = asynchrone Kommunikation im Hintergrund

Interaktion im Web ohne Ajax
----------------------------
* Anwender aktiviert Link oder sendet Formular ab
* Browser sendet entsprechende HTTP-Anfrage an Webserver
* Webserver antwortet, indem er üblicherweise HTML-Dokument zurückliefert,
  das Browser verarbeitet und anstelle des alten anzeigt
* ohne Ajax muss immer neues, vollständiges HTML-Dokument vom Server geladen werden
* Ajax durchbricht Prinzip und ändert damit Bedienung von Webseiten und Aufbau
  von Webanwendungen grundlegend
* werden nur kleine Datenportionen mit Webserver ausgetauscht -gerade benötigte
  Daten nachgeladen, dem Server ausgewählte Änderungen mitgeteilt
* im Extremfall kommt Single Page Application heraus
* besteht nur aus einem ursprünglichen HTML-Dokument
* restlicher Datenaustausch mit Webserver läuft per JavaScript im Hintergrund:
  über DOM-Schnittstelle wird Dokument nach Belieben umgestaltet
* Dokument reagiert auf Benutzereingaben, übersendet diese gegebenenfalls an
  Server, lädt im Hintergrund Inhalte vom Server nach und montiert sie ins
  bestehende Dokument

Vor- und Nachteile von Ajax
===========================
Klassisches Modell mit eigenständigen, adressierbaren Dokumenten
----------------------------------------------------------------
Herkömmliches Modell funktioniert nach Grundsatz »Stop and Go«:

#. Anwender klickt auf Link oder Absende-Button eines Formulars und muss warten
#. Browser übermittelt Anfrage an den Webserver
#. Webserver speichert gegebenenfalls Änderungen ab und generiert neues, vollständiges Dokument
#. Wenn Dokument zum Client-Rechner übertragen wurde und Browser es vollständig
   dargestellt hat, kann Anwender in Webanwendung weiterarbeiten
#. Browser zeigt Reihe von eigenständigen HTML-Dokumenten (Ressourcen) an, die
   alle eindeutige, gleichbleibende Adresse (URL) besitzen

Dokumente sind unabhängig von JavaScript lesbar, verlinkbar, durch Suchmaschinen
indizierbar, problemlos abspeicherbar.

Besonderheiten bei Ajax
-----------------------
* Mit Ajax Server-Anfragen im Hintergrund, ohne dass Dokument ausgewechselt wird
* Warten auf Server-Antwort fällt ganz weg oder wird extrem verkürzt
* gibt keine vollständigen, adressierbaren Dokumente mehr, die in Webanwendungen
  bestimmten Punkt und Status markieren
* Zurück-Funktion des Browsers funktioniert bei Verwendung von Ajax nicht mehr wie gewohnt

Zugänglichkeit von Ajax-Anwendungen
-----------------------------------
* Großer Teil der Datenverarbeitung vom Server-Rechner auf Client-Rechner (Browser) verlagert
* Verlauf, den bisher Browser automatisch zur Verfügung stellte, müssen in
  Ajax-Anwendungen nachgebaut werden, z.B. indem jeder Status Adresse bekommt,
  damit Zurück-Navigation funktioniert

Einsatzgebiete
--------------
* Einsatz von Ajax als Zusatzfunktionalität
* Wenn JavaScript verfügbar, genießt Anwender gewissen Extra-Komfort in Bedienung
* Wenn JavaScript nicht aktiv oder Ajax nicht verfügbar, kann Website trotzdem
  ohne funktionale Einschränkungen benutzt werden
* Nachladen von Inhalten auf Benutzerwunsch (z.B. beim Klicken oder Überfahren mit Maus)
* Automatische Vervollständigung (Autocomplete und Suche bei der Eingabe)

Server-Aktionen ohne Antwort-Daten
----------------------------------
Einfache Formulare, die per Ajax automatisch abgesendet werden:

    * Kommentarfunktion
    * Bewertungen mit einfacher Skala (z.B. 1-5 Sterne)
    * Abstimmungen

* Listen-Funktionen wie Markieren, Ausblenden, Löschen usw.
* Blättern und Seitennavigation
* Wechsel zwischen Lese- und Editier-Modus bei Formularen
* Regelmäßige Aktualisierungen vom Server (Liveticker, E-Mail, Chats)
* verwendete Dateiformate für Übertragung: HTML, XML und JSON

XML
===
Das XML Format wird in JavaScript hauptsächlich für Ajax angewandt.

XML-Dokument hat strikte Regeln für Aufbau, dadurch sehr einfach, DOM (Document
Object Model) zu nutzen. Auch hier in Knoten denken und in Hierarchie navigieren.

.. code-block:: javascript

    let xmlString = '<?xml version="1.0" encoding="UTF-8"?>' +
        '<artists>' +
        '<artist name="Kyuss">' +
        '<albums>' +
        ' <album>' +
        ' <title>Wretch</title>' +
        ' <year>1991</year>' +
        ' </album>' +
        ' <album>' +
        '   <title>Blues for the Red Sun</title>' +
        '    <year>1992</year>' +
        '   </album>' +
        '   <album>' +
        '    <title>Welcome to Sky Valley</title>' +
        '    <year>1994</year>' +
        '  </album>' +
        '  <album>' +
        '   <title>...And the Circus Leaves Town</title>' +
        '  <year>1995</year>' +
        '  </album>' +
        '  </albums>' +
        '</artist>' +
        '</artists>';

    console.log(xmlString);

Der XML-String wird als ``XMLDocument`` Datentyp implizit umgewandelt, welcher
die gleichen Methoden wie ``Document`` bietet. Der Aufbau von XML ist sehr ähnlich
dem von HTML und die DOM-API für HTML lässt sich ebenfalls auf XML anwenden.

Umwandlung XML-String zu XML-DOM (XML-Dokument)
-----------------------------------------------
Über das ``DOMParser`` Objekt lässt sich mit der ``.parseFromString()`` Methode
ein XML-String in ein XML-DOM Objekt umwandeln.

.. code-block:: javascript

    let parserObj = new DOMParser();
    let xmlDoc = parserObj.parseFromString(xmlString, "text/xml");
    console.log(xmlDoc);

Hierauf lassen sich sämtliche DOM-Methoden des ``Documents`` (HTML-DOM) ebenfalls
nutzen:

.. code-block:: javascript

    // Methoden vom DOM-Zugriff integriert/nutzbar
    let myArtist = xmlDoc.querySelector("artist");
    console.log(myArtist);

.. important::

    Es ist kein Zugriff per IDL möglich, da sich das XML-Document nicht im
    (herkömmlichen) DOM befindet:

    .. code-block:: javascript

        // kein IDL-Zugriff, da document nicht im DOM
        console.log(myArtist.name);                 // undefined
        console.log(myArtist.getAttribute("name")); // Kyuss

Umwandlung XML-Dokument in XML-String
-------------------------------------
Über das ``XMLSerializer`` Objekt lässt sich über die ``.serializeToString()``
Methode ein XML-Dokument in einen XML-String umwandeln.

.. code-block:: javascript

    let serializerObj = new XMLSerializer();
    let myXMLStr = serializerObj.serializeToString(xmlDoc);
    console.log(myXMLStr);

XMLHttpRequest
==============
Über einen ``XMLHttpRequest`` wird verwendet, um Anfragen vom Client an den Server
zu schicken, bei welchem Daten angefordert werden. Diese Daten können im XML Format
zurückgegeben werden, müssen jedoch nicht.

Anfrage senden
--------------
Zum Senden einer Anfrage wird zunächst das XMLHttpRequest-Object (XHR) erstellt:

.. code-block:: javascript

    // 1. XHR-Object erstellen
    let xhr = new XMLHttpRequest();

Daraufhin wird ein Event-Handler erzeugt, welcher auf die Server-Antwort wartet:

.. code-block:: javascript

    // 2. Event-Handler erstellen
    xhr.onload = function() {
        // feuert, wenn Server-Antwort vollständig eingetroffen
        // response muss nicht zwingend angefragte Daten enthalten
        if (xhr.status != 200) return;
        // Server hat mit "OK" (Status 200) geantwortet
        // https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
        // https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
        // Daten wurden ordnungsgemäß übermittelt und können jetzt verarbeitet werden
        console.log(xhr);
    };

.. hint::

    Hier wird der ``onload`` Event Handler einer Funktion zugewiesen, welche den
    Status *200* (OK) setzt und das XMLHttpRequest Objekt in die Konsole geloggt.
    Die Funktion wird folglich nach Abschließen der Anfrage d.h. dem Erhalt der
    Server-Antwort ausgelöst.

Als nächstes muss über ``.open()`` die HTTP-Anfrage formuliert werden.

.. code-block:: javascript

    // 3. HTTP-Anfrage formulieren
    xhr.open("GET", "./artists.xml");
    // xhr.open("POST", "./script.php");

.. hint::

    Hier wird ein XML-Dokument über die GET-Methode angefordert.

Die Anfrage lässt sich weiterhin konfigurieren. Hier wird über ``.responseType``
der Rückgabetyp der Daten definiert, in diesem Fall ``"document"``, was entweder
einem HTML oder einem XML-Dokument entspricht.

Über ``.setRequestHeader()`` lässt sich ein Text an das Ende einer Headers anhängen.
In diesem Fall wird an den ``"Accept"`` Feld der Wert ``"text/xml"`` angehängt,
was dem Server mitteilt, dass der Client Antworten des Mimetypes ``text/xml``,
also einen XML String, akzeptiert. Wird er nicht definiert, werden die Antwortdaten
als String gespeichert.

.. code-block:: javascript

    // 4. Anfrage konfigurieren
    // Wie sollen Antwort-Daten vorliegen?
    // xhr.responseType = "";  // Antwort als String (default)
    xhr.responseType = "document";  // geparstes Document (HTML || XML)
    // xhr.responseType = "json";      // geparste JS-Daten, wenn Browser es kann

    // Request-Header konfigurieren
    xhr.setRequestHeader("Accept", "text/xml");

Die Anfrage wird zuletzt mit ``.send()`` ausgeführt.

.. code-block:: javascript

    // 5. Anfrage senden
    xhr.send();
    // xhr.send(data);

    console.log (xhr);  // Daten vom Server noch nicht da

Zusätzlich lassen sich weitere Event-Listener dem XMLHTTPRequest anhängen, z.B.
um wie hier, den aktuellen Status des Requests anzuzeigen:

.. code-block:: javascript

     xhr.addEventListener("load", function() {
        console.log("Laden der Daten vom Server abgeschlossen!");
    });

    xhr.addEventListener("progress", function() {
        console.log("Fortschritt beim Laden der Daten vom Server!");
    });

    xhr.addEventListener("error", function() {
        console.log("Fehler beim Laden der Daten vom Server!");
    });

    xhr.addEventListener("timeout", function() {
        console.log("Timeout beim Laden der Daten vom Server!");
    });

Antwort weiterverarbeiten
-------------------------
Hat man über einen ``XMLHTTPRequest`` ein Antwort-Objekt mit vom Server erhalten, lässt
sich der HTML oder XML Inhalt über das ``.responseXML`` Attribut auslesen.

.. code-block:: javascript

    const output = document.querySelector("#browser");

    const xhr = new XMLHttpRequest();
    xhr.onload = function() {
        if (xhr.status != 200) {
            output.textContent = "Ooops";
            return;
        }

        const xml = xhr.responseXML;
        const allBrowser = xml.querySelectorAll("browser");
        console.log(allBrowser);

        outputFunc(allBrowser);
    };

Beachte, dass der Rückgabewert von ``.responseXML`` ein Dokument ist. Damit lässt
sich weiterarbeiten, wie mit dem DOM.
