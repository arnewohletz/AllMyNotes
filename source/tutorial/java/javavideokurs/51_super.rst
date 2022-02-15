51. Keyword super
=================
1)
--
**Problem:**

    Konstruktoren werden nicht an Kind-Klassen vererbt, d.h. die Instanzvariablen
    eines Konstruktors der Vater-Klasse werden nicht vererbt, also wird für die
    Kind-Klasse der default-Konstruktor verwendet (leerer Rumpf, keine
    Instanzvariablen). Möchte man nun eine nun ein neues Instanz Kind-Klasse
    erzeugen so ist und lässt sich nicht auf diese Instanzvariablen zugreifen,
    welche die Vater-Klasse für bestimmte Funktionen vorsieht (z.B. muss wird
    für jedes Fahrzeug bei der Initialisierung eine Leistung definiert, die in
    einer Methode verändert werden kann).

**Lösung:**

    Man erzeugt einen neuen Konstruktor in der Kind-Klasse und ruft in diesem
    den Konstruktor der Vater-Klasse auf:

    .. code-block:: java

        public class LKW extends Fahrzeug
        {
            public LKW(int leistung, String hersteller, int preis) {
                super(leistung, hersteller, preis);
            }
        }

Man kann außerdem weitere Parameter übergeben, die nicht als Instanzvariable
herangezogen werden:

.. code-block:: java

    public PKW(int leistung, String hersteller, int preis, int anzahlTueren) {

        super(leistung, hersteller, preis);
        setAnzahlTueren(anzahlTueren);
    }

aber *super* muss der erste Aufruf im Konstruktiv sein.

Sofern der Konstruktor der Vater-Klasse keine Werte verlangt, lässt sich auch der
default-Konstruktor der Kind-Klasse verwenden:

.. code-block:: java

    public PKW(){
        super();
    }

Dieser Ausdruck wird jedoch nicht explizit angegeben (ist implizit vorhanden).

Bevor eine Instanz der Kind-Klasse initialisiert wird, wird zuerst die Vater-Klasse
initialisiert (siehe UPDATE bei :doc:`06_instantiation`), d.h. der Methoden
und Instanzvariablen werden übergeben.

2)
--
* Mit *super* kann man auf Methoden und Variablen der Vater-Klasse(n) zugreifen
* Im Gegensatz dazu kann mit this sowohl auf die Methoden und Variablen der Vater-Klassen
  als auch der eigenen Klasse zugegriffen werden

Shadowing lässt sich mit *super* vermeiden:

.. code-block:: java

    public class Fahrzeug {
        int leistung;
    }
    public class PKW extends Fahrzeug
    {
        {
        super.leistung = 100;  -> Hier wird auf die Vater-Klasse zugegriffen
        }
    private int leistung;
    }

Jedoch ist diese Praktik sehr selten, denn üblicherweise wird eine Instanzvariable
nicht erneut in einer Kind-Klasse initialisiert.
