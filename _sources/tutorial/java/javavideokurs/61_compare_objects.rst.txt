61. Objekte vergleichen (equals)
================================
Operator wird für den Vergleich von zwei komplexen Datentypen (Object, String, ...)
verwendet (entspricht dem '==' bei primitiven Datentypen).

Das '==' vergleicht die Werte der beiden Variablen, jedoch enthalten
Objektvariablen lediglich Referenzen. Verweisen zwei Objekvariablen auf das
gleiche Objekt so sind diese Variablen identisch ( per ==) Besitzen zwei Objekte
die gleichen Inhalte, so sind sie identisch (per equals):

<Object1>.equals(<Object2>)

Soll die Methode bei Objekten eigener Klassen angewendet werden muss die von Object
vererbte equals-Methode überschrieben werden, um zu definieren, was man selbst
unter Gleichheit versteht. Hier interessieren z.B. nur die Eigenschaften des
Fahrzeugs (Leistung, Hersteller, Anzahl der Türen - somit nicht der Preis)

.. hint::

    Eine Vergleich mit einem Null-Objekt ist stets false

**Vergleich von zwei primitiven Datentypen:**

.. code-block:: java

    @Override
    public boolean equals(Object obj)
    {
        //Der Teil ist Standard (auswendig lernen)
        if (!(obj instanceof PKW))
        { //prüfe ob Objekt vom Typ PKW ist
            return false;
        }
        PKW o = (PKW) obj; //Objekt wird auf PKW gecastet

        //Dieser Teil ist anwendungsspezifisch
        //Vergleich primitiver Datentypen
        if (this .getLeistung() != o.leistung)
        {
            return false;
        }
        if (this .anzahlTueren != o .anzahlTueren )
        {
            return false;
        }
        // Vergleich komplexer Datentypen
        // Da es sich um einen String handelt muss für den Vergleich abermals die equals-Methode aufgerufen werden
        //Merke : Es handelt sich nicht um die gerade definierte equals-Methode (Rekursion) sondern um die equals-Methode der String-Klasse
        if (!this .getHersteller().equalsIgnoreCase(o.getHersteller()))
        {
            return false;
        }
        return true;
    }

.. important::

    Wird bei dem Aufruf der equals-Funktion komplexe Datentypen (z.B. String)
    miteinander verglichen, muss für diese die equals-Methode zuvor ebenso
    angepasst werden (wie bei clone()) (hier nicht nötig, da String.equals die
    korrekte Methode ist).

*equalsIgnoreCase* ... nur bei String-Vergleich: Groß- und Kleinschreibung
interessiert nicht
