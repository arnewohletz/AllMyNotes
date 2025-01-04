React
=====
JS Bibliothek für die Erstellung von Front-Ends. Komponentenbasiert.
Nutzt JSX Template-Sprache. Wenig Interaktion mit dem DOM. Nutzt einen virtuellen
DOM (V-DOM), welche eine abgespeckte Variante des HTML-DOM ist und vergleicht
diesen mit dem HTML-DOM, daher ist React schneller. Das optionale Parcel
(https://parceljs.org/) ermöglicht ein automatisches Reload der Seite bei Veränderung.

Eine Interaktion mit dem DOM ist kaum noch nötig, da die Anwendungen über Komponenten
zusammengebaut sind, welche über Funktionen definiert sind. Komponenten geben
JSX zurück, welches im Hintergrund zu HTML umgewandelt wird. Änderungen an
Komponenten wirken sich auf alle Instanzen aus.

https://react.dev/

Siehe ``Tag_24/react``.

.. hint::

    ``.parcel-cache``, ``dist`` und ``package-lock.json`` sollen nicht mit
    ausgeliefert werden.

Siehe ``Tag 25/react``.


Das Hauptprogramm enthält einen ``index.html`` und eine ``index.js``, welche das
Root-Element enthält.

Starten der React Applikation über Parcel:

.. code-block:: none

    npm i
    npx parcel index..html

Über den Befehl

.. code-block:: none

    npx create-react-app my-app

wird eine React Application in den Ordner ``my-app`` geschrieben und dort hinein
installiert. Dies ist hilfreich, falls das Zielsystem keine Node.js Installation
enthält. Weitere Infos: https://create-react-app.dev/docs/getting-started/.

Anschließend kann über

.. code-block:: none

    npm run build

ein Build-Script erstellt werden (erzeugt ``/build`` Ordner).
