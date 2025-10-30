Datenübertragung an Server
==========================
.. attention::

    Die Informationen sind etwas löchrig und es fehlt auch etwas von den
    erzeugten Dateien. Falls nötig, besser noch anderswo nachschlagen.

.. hint::

    Die Beispielaufgaben hier werden über den XAMPP Apache Server gehostet.
    Dazu müssen die Ordner in ``/Applications/XAMPP/xamppfiles/htdocs/``
    verschoben werden.

Datenübertragung mit GET (per queryString)
------------------------------------------
Daten, welche per queryString an den Server übertragen werden, können mitgelesen
werden, daher dürfen keine sensiblen Daten darüber übertragen werden.

.. hint::

    ``pw-check/pw_check.php`` prüft, ob eine Query Parameter (``pw=...``)
    Sicherheitskriterien erfüllt.

Der Query String wird über ein Fragezeichen ``?`` an die URL angehängt werden:

.. code-block:: none

    URL?queryString

Der queryString selbst besteht aus key=value Paaren, welche mit ``&`` voneinander
getrennt werden:

.. code-block:: none

    URL?key=value&key2=value2

.. hint::

    **Starten des Apache Servers**

    Über XAMPP starten + auf ``localhost:80/server`` im Browser navigieren.

.. important::

    Bestimmte Sonderzeichen, wie ``#`` haben eine besondere Bedeutung in der URL.
    Daher müssen diese bei Übergabe in einem queryString über ``encodeURIComponent()``
    encodieren:

    .. code-block:: javascript

        let encodedKeyword = encodeURIComponent(kennwort);

    PHP decodiert diese Eingabe wieder, bevor der Wert verwendet wird.

Datenübertragung mit POST (per JSON)
------------------------------------
Siehe ``server/JSON-schreiben``.

.. important::

    Bei ``POST`` werden die Daten über den *request body* versendet, bei ``GET``
    können diese nur über URL Parameter (queryString) übermitteln und eignet
    sich daher nur für wenige Daten.

.. hint::

    ``/JSON-schreiben/script.php``: JSON wird erstellt, falls nicht vorhanden,
    ansonsten wird JSON wird geöffnet, die Werte verändert und geschlossen.

.. hint::

    Wird ein Formular über den Submit-Button übertragen, werden die Daten im
    Formular validiert und versendet. Dies wollen wir hier unterbinden, um
    zunächst die Eingaben zu prüfen, ob diese nicht bereits im JSON vorhanden sind.

    .. code-block:: javascript

        myForm.onsubmit = function() {
            submitFunc();
            // Absenden des Formulars unterbinden -> führt sonst zu Browser Refresh
            return false;
        };

    Das ``submit`` Ereignis wird am Formular ausgeführt, nicht am Button selbst
    (dieser hat lediglich das ``onclick`` Ereignis).

Aus Beispiel:

.. code-block:: javascript

    sendData(JSON.stringify(data));

    // Daten an JSON übertragen
    const sendData = function(data) {
        const xhr = new XMLHttpRequest();
        xhr.onload = function () {
            if (xhr.status != 200) return;
            console.log("Gesendete Daten:", xhr.responseText);
        };
        xhr.open("POST", "./script.php");
        xhr.responseType = "";
        xhr.send(data);
    }

.. important::

    Werden Daten wiederholt vom Server angefragt sollte verhindert werden, dass
    diese Daten aus dem Browser-Cache kommen. Zum **Deaktivieren des Caches** für
    eine Server-Anfrage, kann über ``.setRequestHeader()`` eine entsprechende
    Option im Request-Header übergeben werden:

    .. code-block:: javascript
        :emphasize-lines: 14

        const submitFunc = function() {
            // console.log("Hallo Welt");

            // JSON Datei mit AJAX laden
            const xhr = new XMLHttpRequest();
            xhr.onload = function() {
                if (xhr.status != 200) return;
                const jsonData = xhr.response;  // schon als Objekt geparst
                console.log("Daten-Empfang:" + jsonData);
                checkData(jsonData);
            };
            xhr.open("GET", "./artists.json");
            xhr.responseType = "json";
            xhr.setRequestHeader("Cache-Control", "no-cache");
            xhr.send();
        };



