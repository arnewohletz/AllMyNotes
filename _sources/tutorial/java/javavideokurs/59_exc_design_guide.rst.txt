59. Ausnahmebehandlung: Design Guide
====================================
:ulined:`Stets fragen`: **Bin ich schuld** (für das Auftreten eines möglichen
Ausnahmefehlers) bzw. muss ich das lösen?

| **Ja** -> Fehler direkt in der Methode beheben (try-catch)
| **Nein** :ulined:`oder` **Ja, aber Fehler hier nicht zu beheben** -> Exception
  werfen, damit der Fehler an anderer Stelle behandelt werden kann

* :ulined:`Unchecked Exception`: für Bug bzw. Programmierfehler (vermeidbar)
  -> Programm wird gezielt zum :ulined:`Absturz` gebracht um Bug zu identifizieren
  (durch Stacktrace). Typische unchecked exceptions: IllegalArgumentException,
  NullPointerException
* :ulined:`Checked Exception`: für nicht vermeidbare Fehler (z.B. Hardwareproblem
  oder User-Eingaben) (nicht zu erkennen beim Kompilieren) -> :ulined:`muss`
  behandelt werden, kann aber bis zur höchsten Instanz weitergereicht werden.
  Hier sollten möglichst :ulined:`eigene Exceptions` verwendet werden.

Wenn der Fehler weitergereicht wird abermals in der die Exception gefangene
Methode fragen: **Bin ich schuld?**

| Ja -> Exception abfangen (try-catch)
| Nein -> Exception weiterleiten (an höhere Instanz)

Bei :ulined:`Bugs` sollen stets :ulined:`unchecked exceptions` verwendet werden,
da diese nicht behandelt werden und somit zum Programmabsturz führen. Zur Laufzeit
sollen so Bugs erkannt werden.

**Vorteil** von unchecked exceptions im Vergleich zu Ausgaben auf der Konsole mit
Programmende: Durch den **Stacktrace** weiß ich stets, wo im Programm der Fehler
verursacht wurde.

Es sollte stets eine möglichst aussagekräftige Exception verwendet werden, damit
der Fehler schneller klar wird.

Erstellen einer eigenen Exception:

.. code-block:: java

    public class TunenException extends RuntimeException{

        public TunenException(){
        }

        public TunenException(String msg){
        super(msg);
        }

        public TunenException(Throwable t){
        super(t);
        }

        public TunenException(String msg, Throwable t){
        super(msg, t);
        }
    }

Die :ulined:`vier Standardkonstruktoren` definieren.

Stack trace:

.. code-block:: none

    Exception in thread "main" klassen.TunenException: Der Tunewert darf nichtnegativ sein
    at klassen.Fahrzeug.tunenMitEx(Fahrzeug.java:58)
    at programme.FahrzeugDemo.main(FahrzeugDemo.java:14)

Je weiter oben, desto weiter oben im Stack (neue Aufrufe werden auf den Stack gelegt).

Hier: FahrzeugDemo.java:14 -> ruft auf -> Fahrzeug.tunenMitEx -> erzeugt
TunenException (Der Tunewert darf nicht negativ sein).

**Faustregel**: Ein Stacktrace sollte stets gemacht werden, wenn eine (harmlose)
Exception nicht behandelt wird, sondern lediglich abgefangen wird, um einen
Softwareabsturz zu vermeiden.

:ulined:`Checked Exception` werden dann geworfen, wenn Fehler zur Laufzeit
auftreten, die nicht verhindert werden können (z.B. Hardwareproblem), d.h. es
muss ein *try-catch* Block erzeugt werden.
