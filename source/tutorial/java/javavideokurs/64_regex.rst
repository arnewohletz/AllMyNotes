64. Reguläre Ausdrücke (RegEx)
==============================
Zwei Arten von besonderen Ausdrücken in Strings:

    * Reguläre Ausdrücke
    * Escape Sequenzen

**Reguläre Ausdrücke**

* RegEx’s bezeichnen ein bestimmtes Muster eines Strings
* RegEx’s sind für viele Programmiersprachen gleich


Die Methode *Pattern.matches(RegEx, Input)* prüft einen String, ob dieser sich
an ein definiertes Muster hält:

.. code-block:: java

    String regEx = "^[0-9][1-9]*,[0-9]{2}$";
    System.out.println(Pattern.matches(regEx, "12,90"));

* eine Zahl von 0-9
* gefolgt von einer beliebigen Anzahl von Ziffern von 0-9
* gefolgt von einem Komma
* gefolgt von zwei Ziffern von 0-9

Wichtig, wenn Strings auf korrekte Werte geprüft werden müssen.

.. hint::

    :^: Beginn der RegEx
    :$: Ende der RegEx

Alle regulären Ausdrücke lassen sich in der API unter *java.util.regex.Pattern*
nachlesen.

**Escape Sequenzen**

Für die Formatierung von Strings. Z.B.: :java:`System.out.println("Hallo\tCiao\nEnde");`
erzeugt die Ausgabe:

.. code-block:: none

        Hallo Ciao
        Ende

Nachzulesen unter `Oracle <https://docs.oracle.com/javase/tutorial/java/data/characters.html>`__.

.. hint::

    Soll tatsächlich \\t ausgegeben werden, so muss \\\\t geschrieben werden.
