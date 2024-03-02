60. Objekte kopieren (clone)
============================
* clone() erzeugt eine Kopie eines Objekts
* wird einer Variablen der Klon eines Objekts zugewiesen, so referenziert diese
  auf ein Objekt, was den Status zum Zeitpunkt des Klonens des ursprünglichen
  Objektes besitzt

**Problem**

    Die Klasse clone ist protected, d.h. man kann nicht von anderen Packages
    aus per Punktnotation die clone-Methode einer anderen Klasse aus aufrufen.

**Lösung**

    Die clone()-Methode der Superklasse in der Klasse des zu klonenden Objektes
    überschrieben und der Access Modifier dabei auf public gesetzt (offener ist
    stets möglich):

    .. code-block:: java

        @Override
        public Spielstand clone() throws CloneNotSupportedException{
            return (Spielstand) super.clone();
        }


    #. protected -> public
    #. Die Methode der Superklasse wird aufgerufen
    #. Beim Rückgabewert muss auf den Objekttyp gecastet werden, da dieser als
       Rückgabewert verlangt wird.

**Problem**

    Wird die clone() Methode nun aufgerufen gibt es einen Fehler:  Unhandled exception
    type CloneNotSupportedException.

**Lösung**

    Die Methode muss daher in in einen try-catch Block gefasst werden:

    .. code-block:: java

        try {
            aktuellerSpielstand.clone();
        } catch (CloneNotSupportedException e) {
            e.printStackTrace();
        }

* Eine Klasse, welche clone()-Methode unterstützen soll muss das Interface Cloneable
  implementieren:

    .. code-block:: java

        public class Spielstand implements Cloneable

  **Faustregel**: Wird in einer Klasse die clone()-Methode überschrieben, muss
  sie das Interface *Cloneable* implementieren. Die CloneNotSupportedException
  wird dann geworfen, wenn das Interface Cloneable nicht implementiert ist.
* Das Interface *Cloneable* ist leer, daher müssen keine Methoden implementiert
  werden (Marker-Interface), was eine reine Kennzeichnung darstellt
* Durch Prüfen mit *instanceof* wird geprüft, ob ein Interface implementiert
* :ulined:`Designkorrektur`: Da das Interface Cloneable mit 100 %-iger
  Sicherheit in die Klasse Spielstand implementiert ist, kann ausgeschlossen
  werden, dass die CloneNotSupportedException in der main-Methode geworfen wird.
  Um den Code daher zu verringern, sollte der try-catch Block daher bereits in
  der Spielstand.clone()-Methode erfolgen:

    .. code-block:: java

        @Override
        public Spielstand clone(){
            Spielstand klon = null;
            try{
                klon = (Spielstand) super.clone();
            }catch (CloneNotSupportedException e){
                e.printStackTrace();
            }
            return klon;
        }

    #. Die geworfene Exception der Super-Klasse wird direkt in der clone()-Methode
       behandelt (durch printStackTrace()).
    #. Die Methode selbst wirft die Exception nicht weiter (throws
       *CloneNotSupportedException* wird gelöscht).
    #. Die lokale Variable klon wird zurückgegeben, damit die Methode stets etwas
       zurück gibt, auch wenn der Ausnahmefehler auftritt (:java:`return (Spielstand)`
       & :java:`super.clone();` wird zu :java:`klon = (Spielstand) super.clone();`
       & :java:`return klon;` am Ende der Methode.
    #. Somit Rückgabewert = null bei Exception; Rückgabewert ist die Objektkopie
       sofern keine Exception.

    Gleichzeitig kann der try-catch Block in der main-Methode entfernt werden:

    .. code-block:: java

        static void sichereSpielstand() {
            // TODO: aktuellen Spielstand klonen und als gesicherten Spielstand
            // speichern
            aktuellerSpielstand.clone();
        }

**Problem**

    Die super.clone()-Methode erzeugt keine ‘tiefe’ Kopie, sondern eine ‘flache’
    Kopie, d.h. es wird nur die 'obere Ebene' des Objekts kopiert. D.h. befindet
    sich unter den Instanzvariablen ein komplexer Datentyp (hier, Fahrzeug Objekt)
    so wird nur die Referenzvariable geklont und nicht das Objekt selbst (bei
    primitiven Datentypen ist alles OK).

    Daher zeigen die Referenzvariable der Original-Instanz und die der kopierten
    Instanz auf das gleiche Objekt:

    .. code-block:: java

        public class Spielstand implements Cloneable{

            public int punkte;
            public Fahrzeug fahrzeug;
        }

**Lösung**

    Das Objekt selbst muss geklont werden, nicht nur dessen Referenzvariable.

    #. Die clone()-Methode muss auch in der jeweiligen Klasse (hier: Fahrzeug)
       definiert werden (daher auch hier: Cloneable implementieren):

        .. code-block:: java

            @Override
            public Fahrzeug clone() {
                Fahrzeug f = null;

                try {
                    f = (Fahrzeug) super.clone();
                } catch (CloneNotSupportedException e) {
                    e.printStackTrace();
                }
                return f;
            }

    #. Innerhalb der clone()-Methode der ursprünglich zu klonenden Klasse
       (hier: Spielstand) die clone()-Methode der Klasse der in ihr befindlichen
       Objekts aufrufen:

        .. code-block:: java

            @Override
            public Spielstand clone(){
                Spielstand klon = null;
                try{
                    klon = (Spielstand) super.clone();
                    klon.fahrzeug = fahrzeug.clone(); //-> weißt dem Fahrzeug-Objekt der Referenzvariable klon den Rückgabewert der clone()-Methode aus der Fahrzeug-Klasse zu
                }catch (CloneNotSupportedException e){
                    e.printStackTrace();
                }
                return klon;
            }

        :ulined:`Strings` sind kein Problem und haben dieses Problem nicht, da
        sie unveränderlich sind (immutables). Diese Kette geht solange, bis
        keine Objekte mehr in den tiefergehenden Klasse vorhanden sind.

    .. warning::

        Object.clone() benutzt nicht den Konstruktor einer Klasse um eine neue
        Instanz zu erzeugen. Ebenso werden keine Initialisierungsblöcke ausgeführt.
        Sofern wichtiger Code in einem Initialisierungsblock oder im Konstruktor
        vorhanden ist (z.B. Methodenaufrufe oder Instanzvariablen initialisieren),
        muss dieser nach dem klonen nochmal :ulined:`händisch eingetragen` werden.

**Zusammenfassung - Vorgehensweise:**

#. Cloneable interface für zu klonende Klasse implementieren.
#. clone()-Methode in der Klasse definieren.
#. super.clone() - Methode auf aufrufen + Signatur auf public + Klassentyp
   setzten (damit in der main()-Methode nicht geachtet werden muss).
#. Sofern in der Klasse Objekte enthält, muss die clone()-Methode auch in dieser
   Klasse implementiert werden und diese in der ursprünglich zu klonenden Klasse
   aufgerufen werden (manche Java-Klassen bieten bereits eine clone()-Methode).
