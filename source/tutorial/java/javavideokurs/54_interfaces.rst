.. role:: ulined

54. Interfaces
==============
#. Interfaces sind rein abstrakte Klassen.
#. Enthält nur :ulined:`abstrakte Methoden` und :ulined:`Konstanten`. Interfaces
   bündeln einen Funktionsumfang.
#. Methoden und Konstanten müssen alle **public** sein.
#. Implementieren eines Interfaces in einer Klasse:

    .. code-block:: java

       import interfaces.Verkaeuflich;

        public abstract class Fahrzeug implements Verkaeuflich{
        }

    Nun müssen alle Methoden des Interfaces in dieser Klasse definiert werden.
    Wenn eine Methode nicht implementiert, so muss die Klasse abermals *abstract*
    sein.

#. Jede Klasse kann beliebig viele Interfaces implementieren (egal wo in der
   Vererbungshierarchie).
#. Interfaces sind komplexe Datentypen. Es lassen sich daher Variablen vom Typ
   dieses Interfaces in Klassen definieren.
#. Im Gegensatz zu abstrakten **Klassen** lassen sich Objekte eines Interface-Typs
   **erzeugen**

    .. image:: _file/54_interfaces/interface_inheritance.png

    Hier: Das Interface Verkaeuflich verbindet die aus unterschiedlichen
    Hierarchien stammenden Klasse Fahrzeug und Dackel. So lassen sich mit Hilfe
    eines Verkäuflich-Objektes bzw. Verkäuflich-Array Methoden gleiche Methoden
    auf alle dem Interface-Array angehörigen Objekte Methoden anwenden.

#. Implementieren mehrerer Interfaces pro Klasse mit Komma:

    .. code-block:: java

        public abstract class Fahrzeug implements Verkaeuflich, I2, I3, I4 {
        }

#. Implementiert eine Klasse zwei Interfaces welche beide eine Methode des
   gleichen Namens besitzen, so ist das kein Problem, da ja keine Implementierung
   stattgefunden hat. Das ist also nur die zweifache Aufforderung diese Methode
   in der Klasse zu implementieren.
#. Konstanten in Interfaces können auch ohne *public* und *final* angegeben werden

    .. code-block:: java

        static int i = 0;
        public static final int j = 0;

    bedeutet in einem Interface das Gleiche. Genauso bei Methoden:

    .. code-block:: java

        public abstract int getPreis();
        int getLeistung();

    sind identisch, da *public* und *abstract* implizit vergeben wird.

#. Interfaces können voneinander erben, im Sinne erweitern sie sich.

    .. code-block:: java

        public interface Verkaeuflich extends I2{
        }

    Klassen die ein “Kind-Interface” implementieren, müssen zugleich auch das
    “Vater-Interface” implementieren.

#. Konstanten in Interfaces sind implizit *public static final*.
