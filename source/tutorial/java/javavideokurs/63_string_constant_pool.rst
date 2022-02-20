63. String Constant Pool
========================
Strings lassen sich mit und ohne Konstruktion erzeugen:

.. code-block:: java

    String hersteller = "BMW";
    String hersteller2 = new String("Audi");

Was ist der Unterschied?

.. code-block:: java

    String hersteller = new String("Audi");
    String hersteller2 = new String("Audi");

erzeugt zwei String Objekte mit dem gleichen Inhalt aber jeweils eigener
Referenzvariablen, :java:`hersteller == hersteller2` ist also *false*. Für

.. code-block:: java

    String hersteller = "Audi";
    String hersteller2 = "Audi";

hingegen ist :java:`hersteller == hersteller2` *true*, weil die Objekte nicht
separat im Heap, sondern im String Constant Pool (String Literal Pool) gespeichert
werden (abgetrennter Bereich im Heap). Anstelle stets ein neues Objekt zu erzeugen,
wird nachgeschaut, ob ein gleichnamiger String nicht bereits vorhanden ist und
dieser String erneut zugewiesen. Diesen Constant Pool gibt es **nur bei Strings**,
und existiert rein aus Performancegründen.

**Faustregel 1:** Ein neues String Objekt (new-Operator) sollte nur erzeugt werden,
wenn es sein muss, ansonsten sollten neue Strings im String Constant Pool erzeugt
werden.Ein neues String Objekt (new-Operator) sollte nur erzeugt werden, wenn es
sein muss, ansonsten sollten neue Strings im String Constant Pool erzeugt werden.

**Faustregel 2:** Zur Überprüfung, ob zwei Strings identisch sind sollte stets
der equals Operator verwendet werden (nicht ==), damit auch 'new String' Objekte
erfasst werden.

Eine mehrfache Referenzierung eines String Objekt ist möglich, da sich der Wert
eines String nicht verändern lässt (eine Variable lässt sich nur auf ein neues
String Objekt referenzieren).

Zeichen von String-Objekt ändern:

.. code-block:: java

    String s = "Test";
    s = s.replace("s", "x");

Die Funktion replace gibt ein neues String-Objekt zurück, dass erneut zugewiesen
werden muss (daher :java:`s = s.replace`, nicht :java:`s.replace`) - dies gilt
für alle Methoden, die den Inhalt eines String Objekts verändern.
