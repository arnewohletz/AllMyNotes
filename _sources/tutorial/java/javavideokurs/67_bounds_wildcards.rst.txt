67. Bounds & Wildcards
======================
Bounded Type Parameter (Bounds)
-------------------------------
* Bounds schränken die Auswahl eines Typ-Parameters ein
* Funktioniert für Typ-Parameter von Klassen und Interfaces, sowie von Methoden
  und Konstruktoren

**Anforderung**

Dem Platzhalter Typ-Parameter soll zur Laufzeit nicht ein beliebiger Typ (bzw.
Typen) zugewiesen werden, sondern nur eine eingeschränkte Auswahl haben. Dadurch
lassen sich dann auf alle Objekte, die von der Klasse akzeptiert werden, bestimmte
typ-spezifische Methoden anwenden. Es soll nicht möglich sein, dass diese Methoden
bei Objekten aufgerufen werden, die diese Funktionalität gar nicht haben.

**Möglichkeiten**

#. Generic wird nicht genutzt. Stattdessen werden verschiedenen Listen erzeugt,
   welche jeweils nur die Methoden des akzeptierten Objekts besitzen. So verhindert
   man nicht kompatible Aufrufe -> Problematik vor der Anwendung von Generic wieder da
#. Es wird in der jeweiligen Methode entsprechend von Typ <T> (z.B.) auf den benötigten
   Typ gecastet. Dies führt dazu, dass oftmals auf Typen gecastet wird, die gar
   nicht im Array zur Verfügung stehen (CastClassException) (z.B. wird auf
   Fahrzeug gecastet, aber im Array stehen Strings) -> generisches Verhalten ist
   quasi vorgegaukelt.

**Lösung**

Mischung: Generisches Typ-Parameter für die Typsicherheit + Zugriff auf Methoden
eines konkreten Typs -> :ulined:`alles in einer Klasse!`, also ein Mittelweg
zwischen ‘freien’ Genetics und strikter Klassenzuweisung.

Zunächst muss der Typ-Parameter den entsprechenden Klassentyp erweitern:

.. code-block:: java

    public class FahrzeugListe<T extends Fahrzeug> {

nun kann auf Methode der Klasse Fahrzeug zugegriffen werden:

.. code-block:: java

    public int berechneEinnahmen(){
        int summe = 0;
        for (T t: array){
            summe += t.getPreis();
        }
        return summe;
    }

So kann anschließend nur ein entsprechendes Array des erlaubten Typs (oder dessen
Kind-Klassen) erzeugt werden:

.. code-block:: java

    FahrzeugListe<PKW> fahrzeuge = new FahrzeugListe <PKW> (100);
    FahrzeugListe<Fahrzeug> fahrzeuge = new FahrzeugListe <Fahrzeug> (100);

Andere Typen erzeugen einen Compiler-Fehler.

.. admonition:: Faustregel

    Möchte ich auf bestimmte gemeinsame Methoden zugreifen und trotzdem generisch
    bleiben, so dass alle gewünschten Objekte eines Typ in der Klasse akzeptiert sind,
    sollten Bounds verwendet werden.

Nicht nur Klassen, sondern :ulined:`auch Interfaces` können als Schranke angegeben
werden:

* auch hier wird extends verwendet und nicht implements
* :java:`extends` ist hier zu lesen wie ‘kompatibel'
* nun können nur die Klassentypen verwendet werden, welches dieses Interface
  implementieren (bzw. von einer Klasse erben, die dieses Interface bereits
  implementiert hat

Es lassen sich mehrere Interfaces und Klassen als Bereich angeben oder diese auch kombinieren:

.. code-block:: java

    public class FahrzeugListe<T extends Fahrzeug & Verkaeuflich> {

-> Es werden nun nur die Typen zugelassen, auf die :ulined:`alle Bedingungen zutreffen`

:ulined:`Merke`: Es müssen zuerst die Klassen und dann die Interfaces angegeben
werden. Nach der Deklaration eines Interfaces darf keine Klasse mehr kommen.

Wildcards
---------
**Problem**

Generische Klassen sind nicht polymorph wie normale Klassen (was bedeutet, statt
einen Typ X zu übergeben lässt sich auch ein Typ Y heranziehen, der selbst ein
Kind von X ist bzw. X implementiert), d.h. eine Methode, die den Typ Fahrzeug
erwartet kann keine Objekte vom Typ Object akzeptieren.

.. code-block:: java

    Object o = new String(); -> OK: Polymorphie
    Liste<Object> objListe = new Liste<String>(100);
    // -> Nicht OK: Type mismatch: cannot convert from Liste<String> to Liste<Object>

Bei Generics gilt: :ulined:`Eine Liste vom Subtyp einer anderen Klasse kann diese nicht ersetzen`
(eine Liste Object ist keine Liste String). Genauso kann eine Methode in einer
generischen Klasse, die ein Object als generischen Typ verwendet keinen Subtyp
akzeptieren:

.. code-block:: java

    public static int getRemainingSlots(Liste<Object> liste) {
        return liste.getCapacity() - liste.getElementCount();
    }

Der Aufruf :java:`int i = ArrayUtils.getRemainingSlots(strListe);` führt zu einem
Compile-Error (The method getRemainingSlots(Liste<Object>) in the type ArrayUtils
is not applicable for the arguments (Liste<String>))

Um dies zu verhindern müsste also für jeden Typ eine eigene Methode
:java:`getRemainingSlots(Liste<Typ> name)` geschrieben werden.

**Lösung**

Wildcards:

.. code-block:: java

    public static int getRemainingSlots(Liste<?> liste) {
        return liste.getCapacity() - liste.getElementCount();
    }

Das <Object> wird durch <?> ersetzt (Kurzschreibweise für: x extends Object)
-> Es ist alles erlaubt was innerhalb der bounds von Object ist (also alles)

* Man kann auch jeder andere bound setzten: z.B. x extends Fahrzeug. Dies muss
  dann aber explizit angegeben werden
* Auch Interfaces sind möglich (alle Datentypen die dieses Interface implementieren)
* Es gibt keine Möglichkeit mehrere Klassen oder Interfaces anzugeben (mit &)
  -> dies ist nur bei bounds möglich


Es lässt sich auch eine Untergrenze eingeben (statt einer Obergrenze mit extends):

.. attention::

    Wildcards sollten nicht dazu verwendet werden undefinierte Typ-Parameter zu ermöglichen.

    .. code-block:: java

        ArrayList<?> listTwo = new ArrayList<String>();

    Dadurch ist es nicht mehr möglich Methoden, die den Typ-Parameter nutzen
    (z.B. add(E e)) zu nutzen: add(?) ist nicht möglich, da diese Methode mit
    keinerlei Datentyp aufgerufen werden kann. Wildcards daher nur in Methoden
    verwenden, nicht beim Erzeugen neuer Listen.

**Unterscheidung von Bounds und Wildcards**

* Bounds werden in der Definition von Tipparameter festgelegt (also zu bereits
  in der Definition des Interfaces oder der Klasse in welcher die kompatiblen
  Datentypen angegeben werden müssen): :java:`public class Liste<T> {`
* Wildcards werden dort angegeben, wo der letztlich Typ eines Platzhalter zur
  Laufzeit definiert wird: :java:`public static int getRemainingSlots(Liste<?> liste) {`
