49. Casting von komplexen Dateitypen
====================================
Im Gegensatz zum Casting von primitiven Datentypen wird bei komplexen Datentypen nur
der Datentyp verändert, aber nicht die in ihm gespeicherten Werte (z.B. Instanzvariablen).


Prüfung eines expliziten Cast durch *instanceof*:

.. code-block:: java

    String s = ".....";
    Object o2 = new PKW();
    if (o2 instanceof String) {
        System.out.println("o2 ist ein String");
    } else {
        System.out.println("o2 ist kein String");
    }

Zu viele instanceof-Prüfungen in einem Programm weisen auf einen Designfehler hin:
Sofern die einzelnen erbenden Klassen sich zu sehr von ihrer Superklasse
unterscheiden, sollte man nicht lauter Objekte der Superklasse erstellen und
anschließend jedes Objekt auf die gewünschte Unterklasse casten wenn eine
Methoden und Variablen dieser Klasse aufgerufen werden soll, sondern direkt
Objekte dieser Klasse nutzen.

**Faustregel**:

Je mehr sich die Unterklassen seiner Superklasse unterscheiden, desto eher
sollte man Objekte dieser Klassen erstellen und nicht der Superklasse und diese
bei Bedarf casten (Abwägung, da üblicherweise die meist abstrakte Klasse
verwendet werden sollte, da hier durch Polymorphie alle Methoden und Variablen
an die Unterklasse übertragen werden).

-> So abstrakt wie möglich, aber so wenig komplexe Casts und instanceof Prüfungen
wie möglich
