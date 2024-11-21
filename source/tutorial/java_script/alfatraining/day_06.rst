JSON - JavaScript Notation Object
=================================
Austauschformat von JavaScript als JSON String in andere Programmiersprachen,
z.B. Datenübergabe ans Backend oder als Cookies.

* JS-Daten in JSON String umwandeln = serialisieren
* Nutzen: JSON String Daten auffangen oder übertragen (z.B. Backend wie DB)

JSON Support in allen modernen Programmiersprachen vorhanden (auch plattformübergreifend)

Im JSON String müssen **Keys stets in doppelten Anführungszeichen** stehen (einfach
Anführungszeichen sind nicht erlaubt, da diese für die Übergabe des String benötigt
werden). Gleiches gilt für String Werte.

Serialisieren / Deserialisieren
-------------------------------
Über ``JSON.stringify()`` wird ein JS Object in ein JSON String überführt. Doppelte
Anführungszeichen werden bei definierten Objekten automatisch gesetzt. Dies muss bei
eigens geschriebenen JSON Strings jedoch selbst gemacht werden.

Über ``JSON.parse()`` wird ein JSON String in ein JS Objekt überführt.

.. code-block:: javascript

    // Daten serialisieren
    let jsonStr = JSON.stringify(product);
    console.log(jsonStr);
    console.log(typeof jsonStr); // string

    // Daten parsen
    console.log(JSON.parse('{"name": "SingleMalt", "category": ["Whiskey", "Office Drinks"], "price": 29.99, "inStock": 500}'));
    console.log(JSON.parse(jsonStr));  // same as above
    console.log(JSON.stringify(42)) // "42"

Cookies
-------
Beim Clientrechner als String gespeicherte Daten des Nutzer, wodurch der Server den
Client erkennen kann. Diese werden für jeden Browser einzeln gespeichert und verwaltet.
Werden bei einer Anfrage des Client mitgesendet und zurückgesendet -> können
abgefangen werden.

Es dürfen keine sensiblen und großen Daten als Cookies gespeichert werden.

.. hint::

    Im HTTP werden Daten in beide Richtungen als Text übertragen. Der Client sendet
    die Anfrage, der Server antwortet immer (notfalls mit Error).

Im Firefox unter :menuselection:`Web Tools --> Storage --> Cookies`.

.. code-block:: javascript

    // Cookie anlegen
    document.cookie = "user=Jessica";
    // Überschreibe Cookie
    document.cookie = "user=Elektra";
    // Neuer Cookies (hier: nur über admin path) -> wird im Browser nur im /admin Pfad angezeigt
    document.cookie = "user=Elektra; path=/admin";

Das ``sameSite=strict`` Cookie Attribut wird Cookie nur gesendet, wenn man sich auf der
gleichen Domain befindet (nicht, wenn Seite aus anderer Domain heraus angefordert wird).
Dies verhindert, dass korrumpierte Cookies, nicht ausgelesen wird.

.. note::

    **From ChatGPT on ``sameSite``**:

    ``Strict``:

        * Cookies are sent only with requests originating from the same site.
        * Cross-site requests (e.g., navigating to the site from an external
          link or an embedded iframe) do not include the cookie.
        * Best for highly sensitive cookies (e.g., authentication cookies) but
          can reduce usability, as legitimate cross-site requests might not
          work as expected.

    ``Lax``:

        * Cookies are sent with top-level navigation requests (e.g., when a
          user clicks a link to the site) but not with embedded resources
          (e.g., images or iframes).
        * Provides a balance between usability and security.
        * Default behavior in modern browsers if no SameSite value is specified.

    ``None``:

        * Cookies are sent with both same-site and cross-site requests.
        * Must be used with the ``Secure`` flag (i.e., only over HTTPS) in
          modern browsers to avoid being rejected.
        * Allows cookies to work with third-party integrations but may expose
          them to CSRF risks.

.. code-block:: javascript

    // auto-accept Cookie
    // secure: wird nur bei HTTPS gesendet
    // max-age: Speicherdauer des Cookie (86400 Sekunden = 1 Tag)
    document.cookie = "accept=1; max-age=86400; Secure; sameSite=lax"

.. important::

    Das ``sameSite`` Attribut muss derzeit noch nicht übergeben werden, aber bald.
    Mehr unter https://owasp.org/www-community/SameSite.

Cookies erstellen, auslesen und löschen über JS-Funktionen
----------------------------------------------------------
(aus ``cookies-utils.js``)

.. code-block:: javascript

    /* aus cookies-utils.js (Hilfsmethoden für Cookies)
    ####################### */

    // Cookie erstellen
    function createCookie(name, value, sameSite, days) {
        let expires = '', secure = '';
        if(sameSite) secure = "sameSite=" + sameSite + "; ";
        // if(sameSite == "None") secure += "Secure; ";
        if (days) {
            let date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = '; expires=' + date.toUTCString();
        }
        document.cookie = name + '=' + value + expires + '; ' + secure + 'Secure;  path=/';
        // document.cookie = name + '=' + value + expires + '; ' + secure + 'path=/';
    }

    // Cookie lesen
    function readCookie(name) {
    let nameEQ = name + '=';
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
    }

    // Cookie löschen
    function deleteCookie(name) {
        createCookie(name, '', "None", -1);
    }
    // ########################

    // Erstelle Cookie
    createCookie("hero", "Thor", "Lax", 30);

    // Cookie lesen (Cookie --> Array, if found, else Null)
    console.log(readCookie("hero"));  // "Thor"
    console.log(readCookie("userName")); // null

    // Cookie löschen (leeren Cookie mit gleichem Namen erstellen)
    deleteCookie("hero");
    console.log(readCookie("hero"));  // null

.. hint::

    Auch möglich: Cookie als Objekt erzeugen und an die ``createCookie()`` Funktion
    übergeben.

Prüfe ob Arbeit mit Cookies möglich / erlaubt ist
-------------------------------------------------
Möglicherweise hat Nutzer die Verwendung von Cookies untersagt. Manche Browser
unterstützen das ``navigator.cookiesEnabled`` object (boolean). Bei anderen Browsern
muss versucht werden einen leeren Cookie anzulegen und auszulesen.

.. hint::

    Mehr zum ``navigator`` Object: https://developer.mozilla.org/en-US/docs/Web/API/Navigator

.. code-block:: javascript

    function cookieCheck() {
        let canUseCookies = false;
        // check Browser has set navigator.cookieEnabled to true
        if (navigator.cookiesEnabled) canUseCookies = true;
        // Setze leeren Cookie und prüfe ob vorhanden
        if (!canUseCookies && typeof navigator.cookieEnabled == "undefined") {
            document.cookie = "testCookie";
            if (document.cookie.includes("testCookie")) canUseCookies = true;
        }
        return canUseCookies;
    }

    if (cookieCheck()) {
        console.log("can use cookies");
        console.log(navigator.cookieEnabled);
    } else {
        console.log("Nope");
    }

Web Storage
===========
Cookies werden ständig hin und hergeschickt und viele Nutzerdaten enthalten und
weitergegeben werden können. Viele Nutzer löschen Cookies regelmäßig oder blockieren
das Erstellen von Cookies generell. Auch ist die Datenmenge begrenzt (4 KB). Außerdem ist
das Lesen und Schreiben etwas umständlich. Daher bietet der *Web Storage* eine
moderne Alternative.

Daten werden in zwei verschiedenen Storage-Objekte (Datenbanken) abgelegt:

* Local Storage (``window.sessionStorage``) -> speichert Daten über aktuelle Sitzung
  hinaus (Daten auch von anderen Tabs heraus verfügbar)
* Session Storage (``window.localStorage``) -> Daten bleiben nur in aktueller Sitzung
  (nur innerhalb eines Tabs)

Beide verfügen über die gleichen Methoden und Eigenschaften.

.. hint::

    ``window`` ist das oberste Objekt des Browserfensters. Dazu muss aber auch ein
    Browserfenster vorhanden sein.

Vorteile:

* 4 - 8 MB Datenmenge
* Daten werden nicht hin- und hergeschickt, nur wenn explizit angefordert
* Unterscheidet zwischen Domains (e.g. localhost)
* Daten über Objektzugriff oder Methoden auslesbar und speicherbar

Web Storage wird von Nutzern selten bis nie gelöscht, sind daher in der Regel beim
nächsten Mal wahrscheinlich wieder da. Trotzdem muss man dies zuvor prüfen, wie bei
Cookies. Die Storages sind weiterhin in Domains gegliedert (wie bei Cookies).

Storage -Methoden
-----------------
Beide Storages unterstützen die gleichen Methoden.

Über ``.setItem()`` kann ein neuer Eintrag geschrieben oder vorhandener
überschrieben werden.

.. code-block:: javascript

    // Eintrag in Storage schreiben / ändern
    sessionStorage.setItem("firstName", "Jessica");
    sessionStorage.setItem("lastName", "Jones");
    sessionStorage.setItem("firstName", "Jessy");  // überschreiben
    sessionStorage.setItem("fullName", "Jessica Jones");

Über ``.length`` wird die Anzahl der Items ermittelt

.. code-block:: javascript

    // Anzahl Items ermitteln
    console.log(sessionStorage.length); // 2

Über ``.getItem()`` ein Element auslesen

.. code-block:: javascript

    // Eintrag auslesen
    console.log(sessionStorage.getItem("fullName"));

Über ``.removeItem()`` einen vorhanden Eintrag löschen

.. code-block:: javascript

    // Eintrag löschen
    sessionStorage.removeItem("fullName");
    console.log(sessionStorage.getItem("fullName"));  // null

Über ``.clear()`` alle Elemente im Storage löschen

.. code-block:: javascript

    // Storage clearen
    sessionStorage.clear();
    console.log(sessionStorage.length); // 0

Alternative Wege:

.. code-block:: javascript

    // alternative Wege
    sessionStorage.firstName = "Jessica";
    console.log(sessionStorage.firstName);
    sessionStorage["lastName"] = "Jones";
    console.log(sessionStorage["lastName"]); // über access modifier

Objekt in Storage speichern
---------------------------

.. code-block:: javascript

    let user = {
        name:       "Jessica",
        age:        35,
        address:    "Dragonroad"
    };

    localStorage.setItem("userData", user);  // Oh no!

Dies ist so **nicht möglich**, da nur der Datentyp (object) übergeben wird, nicht
jedoch die Daten des Objekts. Daher muss über JSON gegangen werden:

.. code-block:: javascript

    localStorage.setItem("userData", JSON.stringify(user));
    console.log(localStorage.getItem("userData")); // {"name":"Jessica","age":35,"address":"Dragonroad"}

Zum Auslesen, muss der Wert wieder in ein Objekt überführt werden

.. code-block:: javascript

    console.log(JSON.parse(localStorage.getItem("userData"))); // --> Object {...}

.. important::

    Auch Storage Dateien sind nicht sicher. Falls Daten auf keinen Falls verschwinden
    dürfen, sollte diese im Backend (z.B. einer Datenbank) gespeichert werden.

Prüfen ob Storage verfügbar
---------------------------
Bei Zugriff auf Storage ohne das dieser vorhanden ist, wirft Fehler.

.. code-block:: javascript

    // Prüfen ob Storage verfügbar
    if (typeof Storage != "undefined") {  // Storage Constructor Funktion verfügbar?
        console.log(window.Storage);  // umfasst beide Storages
        console.log(window.localStorage);
        console.log(window.sessionStorage);
    }

Errors
======
Typische Arten von Fehlern:

:Syntaxfehler:
    Verstöße gegen die JS-Syntax (werden meist in Entwicklungsumgebung
    bereits dargestellt.
:Laufzeitfehler:
    Treten erst während der Programmausführung auf, z.B.

    * (noch) nicht vorhandene Variable, Funktionen, etc.
    * falsche Nutzereingaben
    * falsche selektierte oder fehlende Element im DOM (oder DOM noch nicht fertig
      gerendert)
:Logische Fehler (Bugs):
    Falsch gedacht oder falsch umgesetzt.

Z.B. lassen sich Ausgaben über ``console.log()`` oder ``alert()`` prüfen, zur
Werteermittlung oder Fluss-Kontrolle.

Alle Fehler stammen von dem Basis-Typ ``Error`` ab:

* ReferenceError --> reference-object nicht vorhanden
* SyntaxError --> Syntax nicht korrekt
* RangeError --> Zugriff auf Wert außerhalb des gültigen Wertebereichs (z.B. Array)
* TypeError --> Nicht vorhandene Eigenschaften eines Typs aufrufen (z.B. Methode eines Objekts)

try-catch Block
---------------
Trifft Fehler innerhalb des Blocks auf, kann dieser behandelt werden.

.. code-block:: javascript

    try {
        console.log("begin try");
        Alert("Hallo");  // Syntax-Fehler -> ReferenceError
        console.log("end try");
    } catch (error) {
        console.log("begin catch");
        console.log(error);
        console.log("Error-Type:", error.name);  // Error-Type: ReferenceError
        console.log("Error-Msg:", error.message);  // Error-Msg: Alert is not defined
        Alert("Hallo");  // Syntax-Fehler -> bricht catch-Block ab, Fehler geht in console, Programm bricht ab
        console.log("end catch");
    } finally {
        // wird immer ausgeführt (z.B. etwas wichtiges Schließen)
        console.log("begin finally");
        console.log("end finally");
    }

    console.log("free again");

Mit ``throw`` kann ein eigener Fehler geworfen werden.

.. code-block:: javascript

    (function getInput() {
        let input = prompt("Zahl zwischen 5 und 10:");
        try {
            if (!input) throw "is empty";
            if (isNaN(input)) throw "is not a number";
            if (input < 5) throw "is too low";
            if (input > 10) throw "is too high";
            console.log("Thank you.");
        } catch (error) {
            console.log(input, error);
            getInput();  // erneuter Aufruf dieser Funktion
        }
    })();

Debugger
========
Über :menuselection:`Developer Tools --> Debugger` lässt sich ein Skript anhalten
und schrittweise durchlaufen.

Windows-Objekt
==============
Das Window ist das Haupt-Objekt des Browser-Fensters. Dessen Properties sind global
verfügbar.

Beispiel für globale Properties:

.. code-block:: javascript

    console.log(window);

    // Properties sind global verfügbar
    // alert(), confirm(), prompt()
    // print()
    // open() nicht mehr verwenden (Pop-ups, werden oft geblockt)

    // in px -> über ParseInt, ParseFloat umrechenbar

    console.log(innerWidth);  // innere Fensterbreite (in px, inkl. Scrollbars)
    console.log(innerHeight); // innere Fensterhöhe (in px, inkl. Scrollbars)
    console.log(outerWidth); // äußere Fensterbreite (in px, alles inklusive)
    console.log(outerHeight); // äußere Fensterhöhe (in px, alles inklusive)

    console.log(scrollX); // aktuelle Scroll-Höhe (in px)
    console.log(scrollY); // aktuelle Scroll-Breite (in px)
