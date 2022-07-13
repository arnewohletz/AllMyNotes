66. Generics
============
* es gibt generische :ulined:`Klassen` und :ulined:`Interfaces` (keine Enums)
* diese erweitern existierende Klassen zur Laufzeit (bis dahin existiert nur ein Platzhalter)

**Anforderung**

Es sollen identische Methoden auf mehrere verschiedene Klassen
angewandt werden. Diese sollen in einer Klasse definiert werden, welche mehrere
bestimmte (nicht nur einen!) :ulined:`komplexen Datentypen` akzeptieren (z.B. soll
die Klasse Objekte von diesen Typen in ein Object-Array speichern) und diese im
gleichen Typ zurück gibt.

**Vermeintliche Lösung**

Erstellung einer Klasse, die alle Instanzen vom Typ
*Object* und deren Kindklassen akzeptiert. Die Klasse akzeptiert das Objekt, muss
es jedoch auf Object umcasten, macht eine Verarbeitung und liefert das Objekt als
Typ *Object* zurück.

**Problem**

*Type-Safety* ist nicht gegeben

    #. Der Rückgabetyp ist stets Object, d.h. es muss auf den richtigen Typ geachtet
       werden, da das Objekt sonst nicht mehr mit den klassenspezifischen Methoden
       kompatibel ist. Sofern man nicht den Überblick hat ist jedoch nicht ersichtlich,
       in welchen Typ gecastet werden muss, weil lediglich die Liste der Object-Instanzen
       vorliegt.
    #. Da die Klasse alle Instanzen vom Typ *Object* und deren Kind-Klassen akzeptiert
       ist es möglich gemischte Listen zu erstellen. Es können also auch Objekte
       hinzugefügt werden, die eigentlich nicht in die Liste sollen.

Der Compiler prüft die Kompatibilität des aus der Object-Liste übergebenen Objekts
mit den Klassenmethoden nicht (was früher PKW war wurde zu Object und wird jetzt
aus Unwissenheit zu LKW gecastet). Diese Fehler treten erst zur Laufzeit auf.
Entweder muss jeder Typ akzeptiert werden (als Kind von *Object*) und dieser korrekt
zurückgecastet werden (d.h. es gibt keine Einschränkung) oder es wird für jeden
Typ, der die Methoden besitzen soll einen eigene Klasse geschrieben.

*Wenig elegante Lösung*

    #. Es wird für jeden Typ einen eigene Klasse mit den gleichen Methoden geschrieben,
       welche nur diesen Typen akzeptiert. Dies bedeutet viel redundanten Code
       und einen vergleichsweise hohen Aufwand.
    #. Object-Liste verwenden, Typ-Unsicherheit akzeptieren, mit Kommentaren arbeiten.

Der Datentyp sollte bereits zur Compiler-Zeit geprüft werden, ob der korrekte Typ
in die Klasse übergeben wird und was für Typen aus der Klasse herauskommen, so
dass nicht mehr gecastet werden muss.

**Lösung**

Generische Klassen (prüft schon zur Compile-Zeit, ob Typen kompatibel sind)

Am Beginn der Klasse wird ein Platzhalter-Typ vergeben (hier: T):

.. code-block:: java

    public class Liste<T> {

Dieser Typ T ist nicht-statisch, kann also nicht in einem statischen Kontext
(also für Instanzvariablen und Instanzmethoden) verwendet werden. Es wird statt
einem Object-Array ein T-Array erzeugt bzw. ein Object-Array erzeugt und auf T
gecastet:

.. code-block:: java

    public Liste (int capacity){
    array = (T[])new Object [capacity];
    }

Der Datentyp für T muss deklariert werden (sonst wird automatisch Object eingesetzt):

.. code-block:: java

    Liste<Fahrzeug> fahrzeugListe = new Liste<Fahrzeug>(100);

-> Hier wird für jedes T zur Laufzeit der Typ Fahrzeug eingesetzt. Das funktioniert
nicht mit primitiven Datentypen.

Das Gleiche bei Interfaces:

.. code-block:: java

    public interface Mapping<K, V> {

    public void put (K key, V value);
    public V get (K key);
    }

(-> Setzen mehrerer Datentypen durch Kommatrennung)

und implementieren in einer Klasse:

.. code-block:: java

    public class Map<K, V> implements Mapping<K, V> {

        @Override
        public void put (K key, V value){
        //TODO
        }
        public V get (K key){
        //TODO
        return null;
        }
    }

.. attention::

    Ein Überladen einer Methode, die Generics verwendet ist nicht möglich, da ansonsten
    nicht klar ist, welcher Datentyp erwartet wird, da der Generic ja unterschiedliche
    Datentypen bedeuten kann (z.B. :java:`public void get (K key)` und
    :java:`public void get (V value)` sind nicht beide parallel möglich)


Es lässt sich bereits bei der Implementierung eines Interfaces definieren, welche
Datentypen für die Generics verwendet werden sollen (kommt jedoch selten vor):

.. code-block:: java

    public class Map implements Mapping<String, String> {

        @Override
        public void put(String key, String value) {
        // TODO Auto-generated method stub
        }

        @Override
        public String get(String key) {
        // TODO Auto-generated method stub
        return null;
        }
    }

**Generische Methoden**

:ulined:`Beispiel`: Methode, welche ein Array mit komplexen Datentypen in eine Objekt vom
Typ Liste umwandelt.

.. code-block:: java

    public class ArrayUtils<X> {

        public static Liste<X> arrayToList (X[] array){
        return null;
        }
    }

funktioniert nicht, da Generic X nicht in statischen Methoden angewendet werden kann.

:ulined:`Lösung`: man macht die Methode selbst generisch:

.. code-block:: java

    public class ArrayUtils {

        public static <X> Liste<X> arrayToList(X[] array) {
            Liste<X> liste = new Liste<X>(array.length);
            for (X x : array) {
                liste.add(x);
            }
            return liste;
        }
    }

:ulined:`Erklärung`: Die statische Methode *arrayToList* vom Typ Liste<X>
( = Rückgabewert) mit dem Parameter X-Array *array* wird durch :java:`public static <X>`
als statische generische Methode mit dem Generic X deklariert. Die Methode erzeugt
eine neue generische Liste *liste* und weist ihr Länge des übergebenen X-Arrays zu.
Jedes Objekt innerhalb X-Array wird auf die gleiche Position im Liste-Array zugeordnet.

:ulined:`Aufruf der generischen Methode`

.. code-block:: java

    Liste<String> liste = ArrayUtils.<String>arrayToList(new String[] {"Hallo","Hi"});

:ulined:`Erklärung`: Die Variable *liste* vom Typ Liste mit dem Generic <String>
wird zugewiesen an den Rückgabewert der Methode arrayToString der Klasse *ArrayUtils*
mit dem Generic <String> und dem entsprechenden Übergabeparameter (hier: ein String-Array
mit zwei Strings).

**Faustregel**

Generics sollen dann verwendet werden, wenn identische Methoden auf mehrere definierte
komplexe Datentypen angewendet werden sollen, die zudem keine gemeinsame Super-Klasse
haben, in welcher man diesen definieren könnte.
