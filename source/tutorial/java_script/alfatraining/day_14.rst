Durch DOM navigieren
--------------------
Traversal-Methoden
``````````````````
Über ``[object].children()`` wird ein Objekt mit allen Kindelementen geliefert:

.. code-block:: javascript

    console.log($("ul").children());        // alle Kind-Elemente
    console.log($("article").find("a"));    // 1. Link im Article

Über ``[object].parent()`` wird das direkte Elternelement **aller**
Kind-Elemente im *object* zurückgegeben:

.. code-block:: javascript

    console.log($("li").parent());          // direktes Elternelement

Über ``[object].parents()`` werden alle Elternelemente **aller**
Kind-Elemente im *object* zurückgegeben:

.. code-block:: javascript

    console.log($("li").parents());          // alle Elternelemente

Über ``[object].parentsUntil(selector)`` werden alle Elternelemente **aller**
Kind-Elemente bis zum *selector* (exclusive) im *object* zurückgegeben:

.. code-block:: javascript

    console.log($("li").parentsUntil("body"));  // alle Elternelemente bis excl. übergebenen Selektor

Über ``[object].closest(selector)`` wird das 1. Elternelemente welches die
Bedingung erfüllt im *object* zurückgegeben:

.. code-block:: javascript

    console.log($("li").closest("article"));    // 1. Elternelement, dass übergebenen Bedingung erfüllt

Für Geschisterelemente:

.. code-block:: javascript

    // Geschwisterelemente
    console.log($("ul").siblings());    // alle Geschwisterelemente
    console.log($("ul").next());        // direkt folgendes Geschwisterelement
    console.log($("ul").next("a"));     // direkt folgendes Geschwisterelement, welches Bedingung erfüllt
    console.log($("ul").nextAll());     // alle folgenden Geschwisterelemente
    console.log($("ul").nextAll("a"));  // alle folgenden Geschwisterelemente, welche Bedingung erfüllen
    console.log($("ul").nextUntil("a"));  // alle folgenden Geschwisterelemente bis excl. übergebenen Selektor

    console.log($("ul").prev());        // direkt vorhergehendes Geschwisterelement
    console.log($("ul").prevAll())      // alle vorhergehenden Geschwisterelemente

Beispiel:

.. code-block:: javascript

    // Beispiel: Event-Handler registrieren
    $("h2").on("click", function() {
        $(this).next().toggle("slow")
    }).next().hide();

**Beispiel**: Slideshow   --> siehe ``Tag_14/slide.js``.

jQuery mit AJAX
---------------
Siehe ``Tag_14/jQuery/script.js``.

GET Requests
````````````
**1. Möglichkeit**

``$.ajax()`` erwartet, dass ein Konfigurations-Objekt übergeben wird:

.. code-block:: javascript

    function loadContent(link) {
        $.ajax({
            type:       "GET",
            url:        link + ".html",
            dataType:   "html",
            success:    function(data) {
                            output.html(data);
                        },
            error:      function(xhrObj, error, errorMsg) {
                             console.log(xhrObj);
                             console.log(error, errorMsg);
                        }
        })

* ``type`` ist die Request-Methode
* ``url`` ist die aufzurufende URL
* ``dataType`` ist der zu erwartende Rückgabedatentyp
* ``success`` ist die Handlung, welche bei erfolgreicher Ausführung (200)
durchgeführt werden soll
* ``error`` ist die Handlung, welche bei nicht-erfolgreicher Ausführung
durchgeführt werden soll

**2. Möglichkeit**

``done()`` und ``fail()``

.. code-block:: javascript

        $.get({
            url:        link + ".html",
            dataType:   "html",
        }).done(function(data) {
                    output.html(data);
        }).fail(function(dxhrObj, error, errorMsg) {
                    console.log(xhrObj);
                    console.log(error, errorMsg);
        });

POST Request
````````````
Analog zu GET Requests, gibt es zwei Möglichkeiten:

.. code-block:: javascript

    function setData(data) {
        $.post({
            url:        "pfad zum verarbeiten",
            dataType:   "html" || "xml" || "json",
            data:       "zu sendende Daten",
            success:    function(data) {},
            error:      function() {}
        });
    }

Bonus: Lazy-Loading mit Hilfsmethoden-Bibliothek
================================================
Siehe ``Tag_14/libs/dom_helper.js`` (enthält Hilfsfunktionen) und
``Tag_14/libs/script-helpertest.js``.

Hier werden Bilder beim Herunterscrollen stets weiter geladen (man kann dadurch
endlos scrollen).

.. hint::

    **Zu ``dom_helper.js``**

    Über ``[elem.method].prototype`` lassen sich bereits definierte Elemente und
    deren Methoden überschreiben.

    Das prototyping kann zu Fehlern in Browsern führen, welche diese Funktion nicht
    unterstützt wird. Um dies zu vermeiden, kann über try-catch mit diesem Fehler
    umgegangen wird.
