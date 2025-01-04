Event-Emitter
-------------
Event-Emitter sind Objekte vom Typ EventEmitter, welche ein Event auslösen.
Damit lassen sich eigene Events erstellen.

.. code-block:: javascript

    // Event-Emitter

    import event from "events";

    // Emitter erstellen
    let emitter = new event.EventEmitter();

    // Event mit on() registrieren
    // 1. Arg: Event-Name
    // 2. Arg: Callback (mit oder ohne Parameter)
    emitter.on("heroComesIn", (firstName, lastName) => {
        console.log(`Hallo ${firstName} ${lastName}. Schön, dass du da bist!`);
    });
    // mehrere Reaktionen auf Ereignis registrierbar (wird ebenfalls ausgeführt)
    emitter.on("heroComesIn", (firstName, lastName) => {
        console.log(`Hallo ${firstName} ${lastName}. Was willst du trinken?`);
    });

    // mit once() Ereignis registrieren, dass nach dem 1. Eintreten automatisch deregistriert wird
    // (nur bei ersten Mal ausgeführt wird)
    emitter.once("heroGoesOut", (firstName) => {
        console.log(`Bis bald, ${firstName}`);
    })

    // Ereignis auslösen mit emit()
    // emit(event, argumente für callback)
    emitter.emit("heroComesIn", "Jessica", "Jones");
    emitter.emit("heroComesIn", "Luke", "Cage");

    emitter.emit("heroGoesOut", "Jessica", "Jones");
    emitter.emit("heroGoesOut", "Luke", "Cage");

    /*
        Alternative zu on(): addListener
        addListener(event, callback)

        Deregistrieren mit removeListener(event, callback)
        alle Listener für Event entfernen mit removeAllListeners(event)
    */

Websockets
==========
Bislang war durch HTTP-Protokoll lediglich Anfrage des Clients und die Antwort des
Servers möglich. Mit Websockets ist eine bidirektionale Kommunikation möglich
z.B. über das TCP/IP Protokoll (nutzen Server untereinander).

.. hint::

    In manchen Netzwerken (z.B. Firmennetzwerk) sind Websockets geblockt.

Socket.io (https://socket.io/) hilft dabei, die

    *
    * Socketverbindung auf Server realisiert wird

Siehe ``Tag_23/NodeJS/10 Websockets``.

Canvas
======
Siehe ``Tag_23/canvas``.

Ein Canvas ist ein HTML-Element für eine Zeichenfläche.

.. code-block:: javascript

