jQuery
======
Bibliothek für JavaScript zur Vereinfachung (nutzt selbst JavaScript).
Mittlerweile durch Aufgreifen in ES6 immer weniger im Einsatz. Der Einsatz von
jQuery schafft viele Möglichkeiten, geht aber zu Lasten der Performance. Es
muss stets die gesamte Library geladen werden, obwohl meistens nur kleine Teile
der Bibliothek verwendet werden.

Es konnte sogar fertige Programme (Plugins) in ein JavaScript eingefügt werden.
Möglichkeit, diese ohne viel Aufwand einzusetzen. Es gab jedoch Inkompatibilitäten,
wenn mehrere Plugins gleichzeitig verwendet wurden.

jQuery besteht rein aus Funktionen welche Objekte zurückgeben. Die Aufrufe lassen
sich verketten.

``*.min.js`` ist eine minimierte Version der Bibliothek, die vom Browser schneller
zu Laden ist. jQuery arbeitet im **strikten Modus**, ``"use strict"`` muss also
beim Einsatz also nicht mehr selbst angegeben werden (gilt global).

jQuery ist **abwärtskompatibel**, man versucht also auch ältere JavaScript
Versionen zu unterstützen (man sieht daher oft ältere Syntax z.B. ``var`` im Code).

Integration von jQuery in HTML:

.. code-block:: html

    <head>
        <!-- ... -->
        <script src="./libs/jquery-3.7.1.min.js"></script>
    </head>

jQuery sollte **nicht** innerhalb des ``<body>`` geladen werden, sondern stets
im ``<head>``.

.. important::

    jQuery sollte stets auf dem eigenen Server liegen und nicht von einem
    externen Server geladen werden. Generell sollten alle externen Bibliotheken
    stets auf dem eigenen Server bereitgestellt werden, damit keine Zugriffe
    auf Bibliotheksseiten und Verletzung des Datenschutzes passieren (oder, falls
    dies nicht möglich ist, sollte der Nutzer zuerst um Erlaubnis gefragt werden).

Selektoren
----------
* ``$()``
* ``jQuery()``

Beide arbeiten gleich, jedoch ist das ``$`` häufig von anderen Frameworks bereits
in Verwendung und erzeugt einen Konflikt bei dem Versuch der Mehrfachverwendung.

Der **konfliktlose Modus** ermöglicht über

.. code-block:: javascript

    jQuery.noConflict();

dass das Dollarzeichen **nicht** mehr eingesetzt werden kann.

Aufruf von jQuery Funktionen
----------------------------
Wird jQuery eingesetzt, muss sich der JS-Code innerhalb einer jQuery Funktion
befinden.

**Alter Weg** (vor HTML 5): einleitender Handler, der darauf wartet, dass DOM fertig geladen

.. code-block:: javascript

    $(document).ready(function() { jQuery-Statements });

**Neuer Weg:**

.. code-block:: javascript

    jQuery( function() {} );

Beispiel (über ``$()``):

.. code-block:: javascript

    $( function() {
        console.log($("#url_llink"));
        console.log(document.querySelector("#url_link"));
    })

Elemente werden in einem "jQuery"-Objekt zurückgegeben.

Auf HTML-Attribute zugreifen
----------------------------
Über ``[elem].attr()`` lässt sich auf ein Attribut eines HTML Elements zugreifen.

.. hint::

    Der Rückgabewert eines Queries ist ein Object, welcher potentiell mehrere
    dem Query zutreffende HTML Elemente enthalten könnte. Die selektierten
    Elementen befinden mit nummerierten String Keys in ("0", "1", ... - das erste
    Match hat die "0"). Beim Zugriff über ``[0]`` wird die Zahl in einen String
    implizit umgewandelt und auf das Element zugegriffen.

.. code-block:: javascript

    console.log($("#url_llink"));  // das Objekt wird zurückgegeben
    console.log(document.querySelector("#url_link"));
    console.log($("#url_link")[0] == document.querySelector("#url_link"));  // true
    console.log($("#url_link")[0]);

.. code-block:: javascript

    // auf HTML-Attribute zugreifen
    let link = $("#url_link");
    console.log(link.attr("title"));  // Attribut ausgeben
    console.log(link.attr("title", "Ab jetzt mit jQuery"));  // Attribut setzen
    console.log(link.attr("title"));

    // mehrere Attribute gleichzeitig verändern
        link.attr({
            title: "jQuery",
            href: "https:/jquery.com"
        });

Über ``[elem].removeAttr()`` wird ein Attribut entfernt:

.. code-block:: javascript

    // Attribute entfernen
    console.log(link.removeAttr("title"));  // Selektion wird im Objekt zurückgegeben
    console.log(link.attr("title"));  // undefined

Über ``[elem].html()`` wird auf den HTML-Inhalt (inkl. Markups) eines Elements
zugegriffen:

.. code-block:: javascript

    // Zugriff auf Content
    let contentH1 = $("h2").html();
    console.log(contentH1);   // "Inhaltsverzeichnis"

    // lesend wird NUR Content des 1. selektierten Elements zurückgegeben
    // es hat sich erwiesen das mehr i.d.R. nicht gebraucht wird
    let contentP = $("p").html();
    console.log(contentP);  // "Hey"

    // Beim Schreiben werden ALLE selektierten Elemente überschrieben
    $("h1").html(contentP);  // --> Hey
    $("p").html(contentP);  // alle p-Elemente --> Hey

.. important::

    Die **jQuery-Methoden sind auf Ebene des Objekts**, nicht auf den Elementen
    innerhalb des Objekts. Sind mehrere Elemente im Objekt, werden diese in jQuery
    in einer Schleife durchlaufen --> es bedarf keiner Schleife in JavaScript
    um z.B. alle Elemente zu überschreiben.

Über ``[elem].text()`` wird auf den HTML-Text (ohne Markups) eines Elements
zugegriffen:

.. code-block:: javascript

    // Content ohne Markups
    // lesend werden ALLE selektierten Elements zurückgegeben (im Gegensatz zu .html())
    $("p").first().text("<b>Content ohne Markups<(p>");
    console.log($("p").text());  // "<b>Content ohne Markups<p>HeyHeyHeyHeyHey"

    // ebenso schreibend!

Selektion eingrenzen
--------------------
.. hint::

    **Ältere jQuery-Versionen**

    .. code-block:: none

        :first          1. Element
        :last           letztes Element
        :even           alle Elemente an geraden index-Positionen
        :odd            alle Element an ungerade index-Positionen
        :eq(index)      Element an übergebener index-Position
        :lt(index)      Elemente mit niedrigeren als übergebener index-Position
        :gt(index)      Elemente mit höherer als übergebener index-Position

        :nth-of-type(position)      Element an Position index + 1

    Über ``$("<tag>:<Eingrenzung>")`` lässt sich die Selektion eingrenzen.

    .. code-block:: javascript

        // Selektion eingrenzen
        $("p:first").html(contentH1);
        console.log($("p"));
        console.log($("p:first"));

Mittlerweile bietet jQuery Selektions-Methoden.

Über ``[object].first()`` lässt sich nur das erste Element im Objekt ausgeben:

.. code-block:: javascript

    $("p").first().html(contentH1);

Über ``[object].last()`` lässt sich nur das letzte Element im Objekt ausgeben:

.. code-block:: javascript

    $("p").last();

Über ``[object].eq(index)`` wird Element an index-Position zurückgegeben:

.. code-block:: javascript

    $("p").eq(2);

Über ``[object].even(index)`` werden alle Elemente an geraden index-Position zurückgegeben:

.. code-block:: javascript

    $("p").even();

Über ``[object].odd(index)`` werden alle Elemente an ungeraden index-Position zurückgegeben:

.. code-block:: javascript

    $("p").odd();

Über ``[object].<some_selector>.end()`` wird eine Unterselektion aufgehoben und
der vorherige Selektion von zutreffenden Elementen zurückgegeben:

.. code-block:: javascript

    $("p").first().end();   // gibt alle <p> Elemente zurück (hebt first() Selektion auf
    console.log($("p").first().end().is($("p")));  // true

    // Kann auch verkettet werden
    $("p").first().end().last();   // gibt letztes <p> Elemente zurück

.. hint::

    Die ``[match_result].is(selector)`` Methode vergleicht die Elemente von *match_result*
    zu denen eines *selector*.

Über ``[object].has(selector)`` werden nur die Elemente einer Selektion zurückgegeben,
welche einem weiteren Selektor entsprechen:

.. code-block:: javascript

    $("li").has("#");  // gibt li-Elemente zurück, welche ul-Kinder haben

Über ``[object].filter(selector)`` lassen sich die Elemente im Objekt filtern:

.. code-block:: javascript

    $("li").filter(".firstElement");

Über ``[elem].not(selector)`` lassen sich Elemente filtern, welche das Kriterium
**nicht** erfüllen:

.. code-block:: javascript

    $("li").not(".firstElement");

Über ``[elem].slice(startIndex, endIndex)`` wird ein Objekt zurückgegeben welches
nur ein Teil der ursprünglichen Menge an Elementen hat. Der ``endIndex`` ist
in der Rückgabe **nicht** enthalten:

.. code-block:: javascript

    $("p").slice(1,4);

Elemente oder DOM-Strings im DOM integrieren
--------------------------------------------
Über ``[object].<INTEGRATION_METHOD>`` wird ein weiteres HTML-Element an einer Stelle
in **allen** Elementen im Objekt angewandt:

* ``.before()``: Das Element wird außerhalb des Elements **vor** das selektierte Element gestellt
* ``.prepend()``: Das Element wird an den Anfang des selektierten Element gestellt
* ``.append()``: Das Element wird an das Ende des selektierten Element gestellt
* ``.after()``: Das Element wird außerhalb des Elements **nach** das selektierte Element gestellt

.. code-block:: javascript

    // Elemente || DOM-Strings im DOM integrieren
    // Hint: Methoden werden auf ALLE Elemente im Objekt angewandt!
    let elem = $(".element");
    elem.before("<p>before Text</p>");
    elem.prepend("<p>prepend Text</p>");
    elem.append("<p>append Text</p>");
    elem.after("<p>after Text</p>");

Inline-Styles setzen & auslesen
-------------------------------
Über ``[object].css("some-style")`` können Inline-Styles aus dem **ERSTEN** Element
im Objekt ausgelesen werden. Wenn ein expliziter Style dafür vorliegt, wird dieser
zurückgegeben, ansonsten der berechnete Style.

.. code-block:: javascript

    // Style des 1. Elementes wird ermittelt
    console.log($("p").css("font-size"));  // "16px"

Über ``[object].css("some-style", "some-value")`` wird ein Inline-Style an **ALLE**
Elemente im Objekts zugewiesen:

.. code-block:: javascript

    // Einen Style setzen
    $("p").css("background-color", "blue");
    console.log($("p").css("background-color"));  // rgb(0, 0, 255)"

    // Mehrere Styles setzen
    $("p").css({
        backgroundColor:    "orange",
        "font-size":        "20px",
        padding:            "10px 20px",
        border:             "1px solid green"
    })

Element-Klassen
---------------
Alle unten stehende Methoden (bis auf ``hasClass()``) geben das neue Objekt zurück.

Über ``[object].addClass()`` lassen sich auf **alle** Elemente im Objekt ein
weiterer Klassennamen anfügen (arbeitetet im Hintergrund mit ``classList.add()``).

.. code-block:: javascript

    $("p").addClass("fehler");

Über ``[object].removeClass()`` wird ein Klassennamen für **alle** Elemente im Objekt
entfernen:

.. code-block:: javascript

    $("p").removeClass("fehler");

Über ``[object].toggleClass()`` wird ein Klassennamen für **alle** Elemente im Objekt
falls nicht vorhanden, hinzugefügt, ansonsten entfernt:

.. code-block:: javascript

    $("p").toggleClass("fehler");

Über ``[object].hasClass()`` wird je Element im Objekt **ein Boolean** zurückgegeben,
welcher besagt ob dieses Element eine Klasse hat oder nicht (jQuery handelt die
Schleife):

.. code-block:: javascript

    if($("p").hasClass("fehler")) $("p").toggleClass("fehler");

Hier wird für alle p-Elemente ermittelt ob sie die Klasse ``"fehler"`` haben.
Falls ja, wird diese über ``toggleClass()`` entfernt.

Events
------
Über ``[object].on("event", function)`` wird ein Event-Listener registriert.

.. code-block:: javascript

    $("p").on("click", function() {
        alert("Da hat was geklickt!");
    });

    // Event-Handler werden NICHT überschreiben (wirkungslos)
    $("p").on("click", function() {
        alert("Da hat doch wirklich was geklickt!");
    });

.. hint::

    Früher gab es ``mouseover`` und ``mouseout``, statt der neueren ``on`` Funktion.

Über ``[object].off("event")`` werden **alle** Event-Listener, welche auf diesem
Event registrieren, entfernt (de-registriert).

.. code-block:: javascript

    $("p").off("click");

.. important::

    Bei JavaScript ist das nicht möglich, weil hier eine Referenz auf das Element
    mit übergeben werden muss. Bei jQuery verzichtet man auf diese Referenz und
    wendet die De-Registrierung auf alle Elemente im Objekt an.

Um auf ``this`` zuzugreifen, muss es zunächst in ein Objekt überführt werden
(über ``$(this)``), um mit jQuery-Methoden zu arbeiten:

.. code-block:: javascript

    $(".bild").on("mouseover", function() {
        $(this).attr("src", "./img/2.jpg");
    });
    $(".bild").on("mouseout", function() {
        $(this).attr("src", "./img/1.jpg");
    });

.. important::

    **Verkettung von jQuery-Methoden**

    Die ``on`` Methode liefert abermals das veränderte Objekt zurück, so dass direkt
    mit dieser Selektion weitergearbeitet werden kann:

    .. code-block:: javascript

        $(".bild").on("mouseover", function() {
            $(this).attr("src", "./img/2.jpg");
        }).on("mouseout", function() {
            $(this).attr("src", "./img/1.jpg");
        });

Effekte
-------
Effekte werden innerhalb einer Funktion eines Event-Listerners definiert.

Über ``[object].hide()`` Methode lässt sich ein Element ausblenden:

.. code-block:: javascript

    $("#bild-ausblenden").on("click", function() {
        $(".bild").hide();
        return false;  // deaktivieren des Standard-Verhaltens (springt zum Seitenstart)
    });

Es lässt sich ein Argument in ``hide()`` übergeben, welcher die Geschwindigkeit
des Ausblendens regelt (gleiches gilt für ``show()``):

.. code-block:: javascript

    $(".bild").hide();  // sofortiges Ausblenden ("kein Effekt")
    $(".bild").hide("fast");  // schnelles Ausblenden
    $(".bild").hide("slow");  // langsames Ausblenden
    $(".bild").hide(5000);  // 5000 ms

Über ``[object].show()`` Methode lässt sich ein Element ausblenden:

.. code-block:: javascript

    $("#bild-einblenden").on("click", function() {
        $(".bild").show();
        return false;  // deaktivieren des Standard-Verhaltens (springt zum Seitenstart)
    });

Weitere Effekte: fadeIn(), fadeOut(), slideUp(), slideDown()

Eigene Effekte erzeugen
```````````````````````
Über ``[object].animate(object, time)`` wird definiert, wie das Objekt am Ende des
Effekts aussehen soll. Vom derzeitigen Zustand wird der Übergang von jQuery berechnet.

.. code-block:: javascript

    $("#animate").on("click", function() {
        $("#container").animate({
            width:          "450px",
            fontSize:       "4em",
            opacity:        "50%"
        }, 2500)
    })

Dieser Effekt wendet mehrere CSS-Styles auf die Elemente an, innerhalb einer Zeit
von 2500 ms.

Über Style-Objekte lassen sich ebenfalls Animationen definieren. Hier wird das
Objekt aus dem sichtbaren Bereich entfernt und innerhalb von 5 Sekunden von links
in den sichtbaren Bereich verschoben.

.. code-block:: javascript

    const styleStart = {
        position:           "relative",
        left:               "-2000px",
        opacity:            0,
        backgroundColor:    "blue",
        color:              "#fff",
        padding:            "10px 20px"
    };

    const styleEnd = {
        left:               0,  // "0px"
        opacity:            1
    };

    // Start and End in one line
    $(".element").css(styleStart).animate(styleEnd, 5000);
