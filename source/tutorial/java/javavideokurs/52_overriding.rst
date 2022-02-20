.. role:: rfg
.. role:: gfg

52. Overriding
--------------
#. Überschreiben einer Instanzmethode in der Kind-Klasse, welche an eine Vater-Klasse
   definiert wurde. Eine Methode kann nur überschrieben werden, sofern diese für
   die Kind-Klasse sichtbar ist (darf also nicht private sein).
#. Die Annotation @Override lässt den Compiler überprüfen, ob eine Methode auch
   tatsächlich überschrieben wird (*Overriding*) oder ob diese lediglich überladen
   wird (Overloading) -> sollte zur Fehlervermeidung stets verwendet werden:

    .. code-block:: java

        @Override
        public String toString(){
            return "Die Leistung ist " + leistung + ", der Hersteller ist " + hersteller;
        }

#. Die Sichtbarkeit kann beim Overriding erhöht werden, aber nicht verringert:

    | protected -> public :gfg:`OK`
    | package private -> private :rfg:`NOK`

#. Bei primitiven Datentypen (int, ...) muss der Datentyp mit der ursprünglichen
   Methode übereinstimmen. Bei komplexen Datentypen (String, ...) kann der
   Datentyp auch ein kovarianter Datentyp sein, d.h. ein Typ der weiter unten in
   der Vererbungshierarchie liegt: z.B. wenn String einen Typ SubString beerbt,
   so kann der ursprüngliche Rückgabewert (String) in den Subtypen (SubString)
   verändert werden.
#. Es wird immer die Methode aufgerufen, von welcher das Objekt stammt: z.B. wird
   eine Objekt PKW erzeugt und durch eine Variable vom Typ Fahrzeug referenziert,
   so wird die Methode der PKW Klasse aufgerufen, nicht die der Klasse Fahrzeug
   (der deklarierte Datentyp ist nicht relevant).
#. Klassenmethoden (static) können nicht überschrieben werden, d.h. wenn es eine
   statische Methode sowohl in einer Kind-Klasse also auch in einer höheren
   Klassen mit dem gleichen Namens gibt, so wird stets die Methode der höher
   gestellten Klasse ausgeführt.
#. Klassenmethoden die als final deklariert wurden, können nicht überschrieben
   werden.
