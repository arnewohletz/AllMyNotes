.. role:: java(code)
    :language: java
    :class: highlight

48. Polymorphism
================

.. admonition:: Regel

    Verwende stets den abstraktesten Datentypen, sofern keine Methode bzw. Variablen
    von darunterlegenden Klassen benötigt werden.

Nur bei komplexen Datentypen (Objekte und Springs) möglich, nicht den primitiven
Datentypen (int, long, ….)

**Beispiel**:

:java:`class PKW extends Fahrzeuge {}`

Klasse *PKW* erbt die Klasse *Fahrzeuge* (diese wiederum von der Superklasse *Object*).

:java:`Fahrzeug pkw1 = new PKW();`

Da Fahrzeuge an PKW vererbt kann ich ein Fahrzeug-Objekt auch als PKW deklarieren,
weil sie *kompatibel* sind (-> alles was Fahrzeug hat, hat auch PKW -> **Substitutionsprinzip**).

*Wozu einen ein Objekt PKW mit einer Variablen vom Typ Fahrzeuge referenzieren?*
*Wieso nicht mit PKW?*

Um sicherzustellen, dass das auf bestimmte Funktionen oder Variablen des Objektes
nicht zugriffen werden kann um so Objekte zu vereinfachen und nur mit den nötigen
Funktionsumfang auszustatten (so abstrakt wie möglich, d.h. je höher in der
Baumhierarchie, desto besser)

    * nur den Datentyp, den wir benötigen um an eine bestimmt Information zu kommen, aber nicht mehr
    * macht Code einfacher und flexibler

**Beispiel:**

Benötigt wird die Information

    * wie viele Fahrzeuge vorhanden sind
    * was der Preis für ein bestimmtes Fahrzeug ist

Es interessiert nicht, was für eine Art Fahrzeug (PKW, LKW, …), da dies keine
Rolle spielt.

| **Einfacher**: Code wird kürzer, da nicht jede Klasse ihre eigene Zähl- und
  SetPreis-Methode braucht.
| **Flexibler**: Wenn eine weitere Klasse hinzukommt, die von Fahrzeuge erbt, so
  muss für diese Funktionalität kein neuer Code geschrieben werden, da dieser
  bereits in der Superklasse vorhanden ist.

**Faustregel** für Objektorientierte Programmierung: Immer den abstraktesten Datentyp
verwenden (Was interessiert mich, was nicht?).

**Zusatz:**

.. code-block:: java

    public static void hinzufuegen(Fahrzeug fahrzeug) {
        if (fCounter < fahrzeuge.length) {
            fahrzeuge[fCounter++] = fahrzeug;
        }
    }

    public static void hinzufuegen(PKW pkw) {
        if (pkwCounter < pkws.length) {
            pkws[pkwCounter++] = pkw;
        }
    }

*Welche Methode wird aufgerufen sofern sie über die Referenz zu einem PKW-Objekt*
*aufgerufen wird (pkw.hinzufuegen)?*

Stets die Methode, deren deklarierten Typ das referierte Objekt am genauesten
beschreibt, also ruft

.. code-block:: java

    private static PKW[] pkws = new PKW[];
    pkws.hinzufuegen(pkw1);

die Funktion :java:`hinzufuegen(PKW pkw)` auf.
