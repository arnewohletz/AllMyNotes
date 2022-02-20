65. Enums
=========
Enums sind Klassen, die jedoch folgende Unterschiede aufweisen:

#. Während der Laufzeit lassen sich keine Instanzen eines Enums erzeugen

    * Es können jedoch (im Gegensatz zu Interfaces) Instanzen davon existieren,
      diese müssen jedoch bereits zur Compile-Zeit festgelegt werden
    * Instanzen eines Enums werden nie vom Garbage Collector zerstört, da sie
      immer intern referenziert werden
    * Eine Klasse die quasi intern festlegt, wie viele Instanzen es von ihr geben wird
    * Enums werden verwendet, wenn nur eine bestimmte Anzahl von Instanzen
      vorhanden sein dürfen (z.B. Wochentage)
    * Es ist auch möglich, die erlaubten Instanzen als Konstanten zu definieren
      und den Konstruktor auf private zu setzen: Jedoch lässt sich hier die
      Restriktion umgehen (von Programmierkollegen oder einem selbst) indem
      man z.B. die Main-Methode in diese restriktive Klasse schreibt
    * Enums werden vom Compiler überprüft und bieten die gleiche Funktionalität
      mit weniger Code:

        Enums schaffen Sicherheit, dass zur Laufzeit keine weiteren Instanzen
        einer Klasse erzeugt werden können, ohne dass der Konstruktor auf
        private gesetzt werden muss. Statt:

        .. code-block:: java

            public class Wochentag {

                public static final Wochentag MONTAG = new Wochentag ("MONTAG");
                public static final Wochentag DIENSTAG = new Wochentag ("DIENSTAG");
                public static final Wochentag MITTWOCH = new Wochentag ("MITTWOCH");
                public static final Wochentag DONNERSTAG = new Wochentag ("DONNERSTAG");
                public static final Wochentag FREITAG = new Wochentag ("FREITAG");
                public static final Wochentag SAMSTAG = new Wochentag ("SAMSTAG");
                public static final Wochentag SONNTAG = new Wochentag ("SONNTAG");

                private final String name;

                public Wochentag(String name) {
                    this.name = name;
                }

                @Override
                public String toString(){
                    return name;
                }

            }

        schreibe ich

        .. code-block:: java

            public enum Wochentag {
                MONTAG, DIENSTAG, MITTWOCH, DONNERSTAG, FREITAG, SAMSTAG, SONNTAG;
            }

        Konventionen: <Konstante1>, <Konstante2> , … ; (Konstante natürlich groß schreiben)

        * Enums sind komplexe Datentypen (Objekte) und erben von der Klasse Object
        * Eine Konstante in einem Enum, welche ein Objekt referenziert weist
          diesem Objekt stets die finale Variable name vom Typ String zu, die
          gleichzeitig ihr eigener Name ist (hier: MONTAG, …): :java:`MONTAG.name = “MONTAG"`
        * Die toString() Methode wird in einem Enum stets automatisch so
          überschrieben, dass sie den Namen einer Instanz als String zurückgibt:

            .. code-block:: java

                @Override
                public String toString(){
                    return name();
                }

#. Jede Instanz eines Enums besitzt (neben der Konstante name) automatisch
   eine ID-Konstante

    * diese wird aufgerufen über <Instanz-Name>.ordinal()
    * die ID ergibt sich aus der Position ihrer Deklaration (z.B. MONTAG ist 1,
      DIENSTAG ist 2, …)
    * :ulined:`Vorteil:` Instanzen eines Enums können in switch-case statements
      verwendet werden (geht sonst bei komplexen Datentypen nicht):

        .. code-block:: java

            switch (tag) {
            case MONTAG:
                System.out.println("Schlimm!");
                break;
            case FREITAG:
                System.out.println("TOLL!");
                break;
            case SAMSTAG:
                System.out.println("SUPER!");
                break;
            case SONNTAG:
                System.out.println("Ziemlich gut.");
                break;
            default:
                System.out.println("So la la");
            }

    * zwei Instanzen eines Enums könne per == verglichen werden, da sichergestellt
      ist, dass es jedes Objekt definitiv nur ein Mal gibt (bei Klassen-Instanzen
      muss man hingegen equals verwenden)

#. Konstruktoren

    * Konstruktoren sind bei Enums stets private (dies muss nicht extra
      deklariert werden)
    * private bedeutet hier jedoch, dass selbst das Enum selbst den Konstruktor
      nicht aufrufen kann, sondern nur vom Enum-Loader. Es können also nur zu
      Beginn des Enums Instanzen dieses erzeugt werden.
    * Vergeben von finalen Variablen im Konstruktor:

    .. code-block:: java

        public enum Wochentag {

            MONTAG("MONDAY"), DIENSTAG("TUESDAY");

            private final String inEnglish;

            Wochentag(String inEnglish){
            this.inEnglish = inEnglish;
            }

            public String getInEnglish(){
                return inEnglish;
            }

        }

:ulined:`oder`

.. code-block:: java

    public enum Wochentag {

        MONTAG("MONDAY"), DIENSTAG("TUESDAY");

    }
    private final String inEnglish;

    void Wochentag(String inEnglish){
        this.inEnglish = inEnglish;
    }

    public String getInEnglish(){
        return inEnglish;
    }


    | Überladen des Konstrukteurs mit Wochentag().
    | Hier werden die Variablen der Reihe nach definiert:
      this(Wert Variable 1, Wert Variable 2 ,…).

Bei Enums gibt es **keine Vererbung**.

**Faustregel:** Wenn bekannt und sichergestellt ist, dass nur eine ganz bestimmte
Anzahl von Objekte eines Typs im Programm nötig sind, sollte diese Klasse als
Enum definiert werden.
