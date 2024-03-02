58. Exceptions werfen (throw)
=============================
Objekte vom Typ Throwable (genauer: Exception) können ‘geworfen’ werden.

**Unchecked Exceptions**

.. code-block:: java

    throw new NullPointException();

Die Ausnahmebehandlung erfolgt in der Methode, welche diese aufgerufen hat (oder
wird noch weiter gereicht).

**Checked Exceptions**

Da die Ausnahme zwingend behandelt werden muss, muss die Methode angeben, ob und was
sie ‘wirft’, damit in der aufrufenden Methode entsprechend reagiert werden kann.

.. code-block:: java

    static void checked() throws FileNotFoundException{
        try {
            FileReader f = new FileReader(new File("C:/xxx"));
        } catch (FileNotFoundException e) {
            throw e;
    }

Der Typ der geworfenen Ausnahme sollte möglichst genau bezeichnet werden, damit
korrekt reagiert werden kann. Kürzer:

.. code-block:: java

    static void checked() throws FileNotFoundException{
        FileReader f = new FileReader(new File("C:/xxx"));
        throw new FileNotFoundException();
    }

Mehrere Exceptions werfen:

    .. code-block:: java

        static void checked() throws FileNotFoundException, SomeOtherException {}

Möglichkeiten:

    #. Nichts tun (nur bei unchecked exceptions) -> exception wird an überstehende
       Methode geleitet.
    #. Weiterwerfen (unchecked & checked) -> exception muss in der überstehenden
       Methode abgefangen oder weitergeleitet werden.
    #. Abfangen mit try-catch.

Es können :ulined:`eigene Exceptions` erzeugt werden, die über die vorhandene
Bibliothek hinaus gehen Konstruktoren, welche Exceptions erzeugen sollten dazu
implementiert werden:

    * Exception()
    * Exception(String message) (-> Zugriff mit getMessage)
    * Exception(String message, Throwable cause)

Überlegen, welche Kategorie: checked (kein Programmierfehler, sondern erwarteter
Fehler z.B. Nutzereingabe) oder unchecked (erbt von RuntimeException).
