46. Vererbung
=============
* Braucht man mehrere Klassen, die gleiche Teile besitzen, so lassen sich diese
  gemeinsamen Teile in einer übergeordneten Klasse beschreiben und für alle
  abhängigen Klassen übernehmen
* Eine Klasse, welche von einer anderen erbt wird mit dem keyword extends
  eingeleitet:

    .. code-block:: java

        public class PKW extends Fahrzeug
        {

        }

* Es werden nur nicht-statische Variablen und Methoden vererbt (Instanz-Methoden
  + Instanz-Variablen)
* Statische Variablen und Methoden werden nicht vererbt, sondern werden in der
  Superklasse nachgeschlagen, sofern Java diese in der Klasse nicht findet
* Konstruktoren und lokale Variablen werden nie vererbt
* Methoden und Klassen werden nur nach unten vererbt, nicht nach oben
* Eine Klasse ist nicht vererbbar, wenn sie als **final** deklariert wird
