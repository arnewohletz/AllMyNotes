.. _java_call_by_reference:

28. Referenzen (Call by Reference)
==================================
Werden Objekte an eine Methode (oder Konstruktor) übergeben wird stets eine Kopie
der Referenzvariable auf das Objekt übergeben (Call by Reference).

Diese kopierte Variable wird nach dem Ende der Methode wieder gelöscht.

Variable, die Objekte referenzieren besitzen keine eigene Werte sondern lesen
die Werte aus dem referenzierten Objekt heraus.

Gibt die Methode ein Objekt zurück und wird dieses dem ursprünglichen Objekt
zugewiesen, so wird die Referenz auf das ursprüngliche Objekt gelöscht, die
Neue besteht.

Eine Variable kann niemals mehrere Objekte referenzieren, aber mehrere Variablen
können das gleiche Objekt referenzieren (sollte aber nicht sein)

Wird eine Methode auf das referenzierte Objekt einer Variablen angewendet, so
verändert sich das Objekt selbst, nicht die Referenzierung (hier gilt:
:ref:`Call by Value <java_call_by_value>`)

Gibt die Methode, welche das Objekt verändert, dieses nicht zurück, so
referenziert die Variable nach wie vor das unveränderte Objekt -> 180

Gibt die Methode, welche das Objekt verändert, es zurück, so referenziert die
Variable das durch die Methode veränderte Objekt -> 220

**Dereferenzierung**

    Aufruf eines Objekts über eine auf es referenzierende Variable

**Beispiel**

.. code-block:: java

    public static void main(String[] args) {
        Auto b = new Auto(180, "Audi");
        doStuff(b)
        System.out.println(b.getLeistung());
        b = doStuffWithReturn(b);
        System.out.println(b.getLeistung());
        doOtherStuff(b);
        System.out.println(b.getLeistung());
    }

    static void doStuff(Auto auto) {
        auto = new Auto(220, "BMW");
    }

    static Auto doStuffWithReturn(Auto auto) {
        auto = new Auto(220, "BMW");
        return auto;
    }
    static void doOtherStuff(Auto auto) {
        auto.tunen(500);
    }

**Output**

.. code-block:: none

    180 //Variable deutet auf das ursprüngliche Objekt
    220 //Variable deutet auf das in der Methode erstellte Objekt

Null Pointer
------------
**null**

    Diesen Wert nimmt eine Referenzvariable automatisch an, so lange sie auf
    kein Objekt referenziert. Sie wird z.B verwendet, um gleich zu Beginn
    einer Klasse zu prüfen, ob die in eine Klasse hineingereichte Variablen
    auch auf ein Objekt referenzieren

**NullPointerException**

    Einer Variablen wurde kein Objekt zugewiesen, aber diese soll anzeigen,
    auf was sie referenziert

    .. code-block:: java

        Auto.nix = null;
        nix.tunen(50)

    -> eine NullPointerException wird geworfen.
