Node.JS
=======
Datei ausführen:

.. code-block:: none

    node <dateiname>

Öffne Node.js REPL (read eval print loop):

.. code-block:: none

    node

* können hier JS-Code eingeben, der direkt ausgeführt wird, ähnlich wie
  in Entwicklerkonsolen der Webbrowser
* REPL verlassen durch Eingabe von .exit

.. hint::

    mit ``require(…)`` importiert Node.js Module

Gleichzeitige Ausführung
------------------------
Node.js versucht jede Anweisung so schnell wie möglich auszuführen.
Programm enthält aber auch viele Anweisungen, die langsam sind (bsw. Einlesen
einer Datei). Bei synchronen Methoden laufen im Hintergrund Anweisungen, die
warten müssen

    * d.h. Anweisung blockiert weitere Ausführung des Programms
    * Programm läuft nicht 100% effizient, wenn es dauernd warten muss
    * und wenn noch weitere Dateien eingelesen werden sollen...

Um möglichst effizient zu arbeiten, sollte Programm sofort damit beginnen.
In der Informatik zwei gibt Ansätze, die Problem lösen:

    * asynchrone Programmierung und
    * Multithreading

JavaScript bevorzugt asynchrone Programmierung
``````````````````````````````````````````````
Dabei wird einer Anweisung Code mitgegeben, der ausgeführt werden soll,
sobald Anweisung das gewünschte Ergebnis erhalten hat. Mitgegebener Code wird
also asynchron »irgendwann später« ausgeführt JavaScript-Programm läuft
immer in einem einzelnen Thread ab. Callbacks kommen in Reihenfolge ihres
Auftretens in Warteschlange -  werden erst ausgeführt, wenn nichts weiteres
zu tun ist.

Multithreading
``````````````
Alternative zu asynchroner Programmierung nutzt Tatsache, dass moderne
Betriebssysteme mehrere Dinge gleichzeitig machen können (Multitasking).
Programm startet einfach weiteren »Neben-Task«, der sich im Hintergrund um
möglicherweise langsame, blockierende Anweisung kümmert. Technisch wird dieser
»Neben-Task« meist als sogenannter Thread implementiert – man spricht von
Multithreading. Die Kunst besteht darin, Threads korrekt zu koordinieren
wenn mehrere Threads dieselben Variablen gleichzeitig (oder zeitlich
verschränkt) unkoordiniert verändern, führt das zu Fehlern, die sehr schwer zu
finden sind. Selbst dort, wo Einlesen der Datei unabhängig von Berechnung ist,
könnte Lösung mit Multithreading-Ansatz problematisch sein. Reihenfolge der
Ausgabe könnte sich willkürlich ändern, je nachdem, ob Haupt-Thread oder
Neben-Thread schneller war Programm reagiert nicht mehr vorhersehbar und kann
nicht zuverlässig getestet werden. Asynchroner Ansatz in dieser Hinsicht robuster!

Node-Standardbibliothek
-----------------------
Bibliothek definiert gut dokumentierte Schnittstelle (engl. interface) mit
Angaben zu Funktionsaufrufen. So eine Schnittstelle wird häufig API (engl.
application programming interface) genannt.

Standard-Module (Auswahl):

.. csv-table::
    :header-rows: 1

    Modul,Zweck
    buffer,Buffer
    console,Ausgabe/Debugging in die Eingabeaufforderung (z.B.console.log(…))
    crypto,Kryptographie
    fs,Dateisystemzugriff
    os,Interaktion mit dem Betriebssystem
    stream,Datenströme
    zlib,Datenkomprimierung

jedes Modul hat Stabilitätswert:

    * beschreibt Stabilität der Schnittstelle
    * Bereich geht von 0 (sehr instabil) zu 3 (sehr stabil)

Module mit Werten 2-3 ruhig verwenden ohne Angst zu haben, dass zukünftige
Version der Standardbibliothek die Schnittstelle so ändert, dass Code nicht
mehr funktioniert.

**Buffer** = beliebige Folge von Bytes
Unterschied zu Strings: Strings enthalten druckbare Bytes (also Zeichen), die
bestimmtem Encoding folgen (bsw. UTF8) Buffer enthalten beliebige Daten:
gzip-komprimierte Daten, Bilder, Messdaten eines Sensors oder ...

**Stream-API** ist sehr komfortabel

    * pipe(…)-Funktion erlaubt es, Streams zu verbinden (daher der Name
      »pipe«, englisch für Röhre)
    * Eingabestrom wird damit an Ausgabestrom angesteckt und pipe(…) kümmert
      sich darum, benötigte Callbacks zu erstellen

Beispiel: fs-Modul
``````````````````
https://nodejs.org/docs/latest/api/fs.html#file-system

* Beinhaltet etwa 100 Funktionen
* Name steht für Dateisystem (engl.filesystem)
* Modul enthält Funktionen zum Umgang mit Dateien - bsw. Funktion fs.readFileSync(…)

``fs.readFileSync(…)``

    * liest eine Datei ein (blockierende Variante)
    * Beispiel:  const data = fs.readFileSync("products.csv", "UTF8");

``fs.readFile(…)``

    * liest eine Datei ein (asynchrone Variante)
    * Beispiel:  const data = fs.readFile( "products.csv", "UTF8", (error, data) => console.log(data) );

``fs.writeFileSync(…)``

    * schreibt Daten in eine Datei (blockierende Variante)
    * bereits vorhandene Daten werden überschrieben

    Beispiel:

    .. code-block::javascript

        const data = "Hello World";
        fs.writeFileSync("hello.txt", data, "UTF8");

``fs.writeFile(…)``

    * schreibt Daten in eine Datei (asynchrone Variante)
    * bereits vorhandene Daten werden überschrieben

    Beispiel:

.. code-block:: javascript

    const data = "Hello World";
    fs.writeFile("hello.txt", data, "UTF8", error => { if (error) console.log("Error: " + error); } );

``fs.statSync(…)``

    * ermittelt Infos zur Datei (blockierende Variante)

    Beispiel:

.. code-block:: javascript

    const stats = fs.statSync("hello.txt");
    console.log(stats.size);  // => size in bytes

``fs.stat(…)``

    * ermittelt Infos zur Datei (asynchrone Variante)
    * Beispiel:  fs.stat("hello.txt",  (error, stats) => console.log(stats.size) ); // => size in bytes

``fs.unlinkSync(…)``

    * löscht eine Datei (blockierende Variante)
    * Beispiel:  fs.unlinkSync("hello.txt");

``fs.unlink(…)``

    * löscht eine Datei (asynchrone Variante)
    * Beispiel:  fs.unlink("hello.txt", error => { if (error) console.log("Error: " + error);});

npm
---
Sammlung von Modulen für node.js auf http://www.npmjs.com
Die meisten Module sind unter freizügigen Open Source-Lizenz verfügbar - dürfen
diese Module somit uneingeschränkt einsetzen.

Validator-Modul (https://www.npmjs.com/package/validator)
Kann Daten aller Art validieren (Zahlen in verschiedenen Formaten, komplexere Daten,
wie Datumsangaben, Kreditkartennummern oder ISBNs).

validator-Modul mit npm installieren:

.. code-block:: none

    npm install validator@12

Weist npm an, neueste Version des validator-Moduls mit Hauptversion 12 zu installieren.
Ohne Angabe ``@12`` würde npm einfach neueste Version installieren.
Meist besser an einer Hauptversion festzuhalten, da sich Teile eines Moduls in
zukünftigen Hauptversionen ändern können - evtl. gibt es bestimmte Modulfunktion
in Folgeversion nicht mehr.

Node.JS Module müssen mit Semantic Versioning benannt sein (http://semver.org/).

**Module für eigene Projekte**

Installierte Module sollten als Abhängigkeit im Projekt eingebracht werden.
Nicht besonders praktisch, Module vorzuinstallieren und zusammen mit Software zu
veröffentlichen wäre z.B. mühsam, Module aktuell zu halten. außerdem nicht
garantiert, dass npm beim Installieren nicht gewisse Schritte ausführt, die
vom Betriebssystem abhängen. besser, dem Programm Anweisungen beizulegen, welche
Module(in welchen Versionen) benötigt werden, um Programm zum Laufen zu bringen.

Abhängigkeiten in ``package.json`` Datei listen:

Wenn package.json im Verzeichnis liegt und im selben Verzeichnis Befehl
npm install ausgeführt wird, installiert npm automatisch abhängige Module
(in den richtigen Versionen).

**Anwendungsmöglichkeiten des npm-Befehls**

.. csv-table::

    ``npm install Modul@Version``,installiere Modul in der Version
    ``npm uninstall Modul@Version``,entferne Modul in der Version
    ``npm update Modul``,update Modul auf die neueste Version
    ``npm init``,erstelle package.json-Datei  (Befehl fragt Eigenschaften ab)
    ``npm init --yes``,erstellt eine package.json-Datei  (Befehl setzt Default-Werte)
    ``npm list``,listet alle installierten Module auf
    ``npm search Suchbegriff``,suche Module, deren Name Suchbegriff enthält

.. hint::

    ``npm install``, ``npm uninstall`` und ``npm update`` kennen Option --global
    (oder kurz: -g). Mit dieser Option handeln Befehle im Installationsverzeichnis
    von Node.js selbst - Module werden global installiert, entfernt oder aktualisiert
    diese Option mit Vorsicht verwenden - evtl. werden Module von anderen Programmen
    noch gebraucht?


Eigene Module schreiben
-----------------------
Sammlung an JavaScript-Funktionen lässt sich einfach in Node.js-Modul verwandeln.
Funktionen, die dem Aufrufer des Moduls zur Verfügung gestellt werden sollen,
müssen zu vordefiniertem Objekt mit treffendem Namen exports hinzugefügt werden.
Modul kann dann mit

.. code-block:: javascript

    ``require(./moduldatei.js)``

eingebunden werden.

Schreibweise ./moduldatei.js forciert Einbinden des Moduls aus aktuellem Verzeichnis
bei Zuweisung mit require(…) auch möglich, zu entscheiden, nur auf bestimmte
Funktion zuzugreifen:

.. code-block::javascript

    require(./moduldatei.js).function

Vom Modul zum npm-Paket
```````````````````````
Wenn Modul öfter verwendet oder auf npmjs.com veröffentlicht werden soll, npm-Paket erstellen.

Dazu Verzeichnis erstellen mit:

    * Namen des Moduls gefolgt von @-Zeichen und Versionsnummer bsw. ``namesmodule@0.0.1``
    * dort hinein kommt Code des Moduls sowie eine ``package.json``, die Modul beschreibt

Wichtige Eigenschaft ist "main" - hier wird Einsprungpunkt definiert, also Datei mit
exports-Definitionen. Modul darf auch aus mehreren Dateien bestehen, gibt aber immer
genau einen Einsprungpunkt. Die Felder ``keywords``, ``author`` und ``license``
ausfüllen, wenn Modul veröffentlicht werden soll wenn Modul weitere Module benötigt,
diese über dependencies-Eigenschaft deklarieren.

**Installation über**

.. code-block:: none

    npm install pfad/zum/Modul/modul

Darauf achten, dass im Projekt eine ``package.json`` liegt, um Abhängigkeiten
automatisch hinzugefügt zu bekommen

.. attention::

    Pfad in ``package.json`` muss angepasst werden, wenn Modul aus Ordner von
    Rechner installiert wurde - relative Pfade sind nicht erlaubt!

``npm`` muss am Argument erkennen können, dass es sich um Verzeichnis handelt.
``npm`` geht so vor, dass es im Zweifelsfall probiert, Argument als lokales
Verzeichnis zu öffnen. Dort sucht es nach ``package.json`` — falls das nicht
klappt, wird auf http://www.npmjs.com gesucht.

Deinstallieren über: ``npm uninstall name_des_moduls``

Wenn wir modul im Ordner ausgeliefert bekommen reicht Dank ``package.json``
 ein ``npm install``, um es zu installieren und Anwendung zum Laufen zu bringen.

**npm-Pakete veröffentlichen**

npm macht es leicht, Pakete direkt auf npmjs.com oder eigenem Webserver zu veröffentlichen.

Dazu npm-Modul-Verzeichnis als TGZ-Datei archivieren und auf npm oder Webserver laden.

Befehl unter OS X und Linux, um TGZ-Datei zu erstellen:

.. code-block:: none

    tar zcf namesmodule@0.0.1.tgz namesmodule@0.0.1

Unter Windows eines der bekannten Archivprogramme benutzen oder innerhalb des
Modul-Ordners ``npm pack`` nutzen => liest package.json aus und nutzt Name und Version.

Modul dann installieren mit:

.. code-block:: none

    npm i namesmodul (Hosting bei npm)

oder

.. code-block:: none

    npm i http://www.domain.de/namesmodule@0.0.1.tgz

Der eigene Server
-----------------
Express
```````
Mit http-Moduls einen Webserver programmieren = viel zu aufwändig, denn es gibt
zu viele Details des HTTP-Protokolls, die programmiert werden müssten. Das
Webserver-Framework Express (https://expressjs.com/) vereinfacht Arbeit wesentlich.
Open Source Software Express unterstützt uns bei Auslieferung von Dateien, dem
Routing, dem View-Rendering und ist modular erweiterbar Code ist wesentlich
flexibler und ausbaufähig:

eigentliche Arbeit des Verarbeitens einer Anfrage erfolgt mit get(…)-Methode
- weisen damit Express an, GET-Anfrage auf URL-Pfad / mit Callback im zweiten
Argument zu beantworten. Antwort-Objekt ``res`` besitzt hier eine send(…)-Methode,
die bereits passende Default-HTTP-Header setzt nur Seiteninhalt muss noch übergeben werden

Routing
```````
Zuordnen von Pfaden wie ``/`` oder ``/seite.html`` zu Callbacks nennt Express *Routing*.
Können mit ``app.get()`` mehrere Routen definieren. Ganze Seite so zu routen,
wäre nicht sehr wartungsfreundlicher Ansatz. Express hat eingebaute Funktion
``express.static(…)``, die automatisch alle Dateien aus Verzeichnis bereitstellt.
Mit Aufruf von ``express.static(…)`` wird Name des Verzeichnisses übergeben,
in dem Dateien liegen. Express stellt alle Dateien im angegebenen Verzeichnis,
inkl. Unterverzeichnissen, über HTTP bereit. Die Notwendigkeit, einzelne Routen
zu definieren, entfällt. ``express.static(…)`` und Routen lassen sich kombinieren.
Bei Konflikt - gerouteter Pfad identisch mit existierender Datei - ermittelt
Express Vorrang aus Reihenfolge der Aufrufe im JavaScript-Code, wobei erster Aufruf gewinnt.

Middleware
``````````
Funktionalität von Express lässt sich durch Middleware erweitern.

Middleware = wesentlicher Bestandteil von Express

Dies sind Funktionen, die für Verarbeitung von Anfragen hintereinandergeschaltet
werden können und dabei unterschiedliche Funktionalitäten wie beispielsweise
Parsen von Cookies oder auch komplexere Themen wie Sicherheit und Zugriffskontrolle
implementieren. Jede Middleware-Funktion hat Zugriff auf Anfrageobjekt (Request-Objekt),
Antwortobjekt (Response-Objekt) und auf jeweils nächste Middleware-Funktion wird
mit ``app.use(…)`` geladen mit Aufruf next() wird Abarbeitung weitergegeben hat
keinen einfluss auf app.get() -> wird davor ausgeführt.

**Beispiel für Verwendung:**

Nutzung des Middleware-Package body-parser : https://github.com/expressjs/body-parser
Um Inhalt einer HTTP-Anfrage zu parsen - beispielsweise um POST Inhalte abzufangen.
Geparster Inhalt ist innerhalb der Callback-Funktion über Eigenschaft ``body``
des Anfrageobjekts erreichbar. Um Middleware-Funktion zu verwenden, auch hier
Übergabe des entsprechenden Aufrufs an Methode ``use()`` am Anwendungsobjekt.
extended-Angabe in ``bodyParser.urlencoded`` erlaubt zu wählen, ob URL-codierte
Daten mit Querystring-Bibliothek (false) oder qs-Bibliothek (true) analysiert
werden sollen
"erweiterte" Syntax ermöglicht Codierung umfangreicher Objekte und Arrays ins
URL-codierte Format, wodurch JSON-ähnliche Erfahrung mit URL-Codierung ermöglicht
wird.

Liste der Middleware Module auf Express-Seite: http://expressjs.com/en/resources/middleware.html


