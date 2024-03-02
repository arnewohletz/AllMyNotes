62. Objekt-ID (hashCode)
========================
* Jedes Objekt besitzt eine Integer ID, genannt Hash-Code
* Abgeleitet von Speicheradresse des Objekts
* Zwei unterschiedliche Objekte besitzen unterschiedliche Hash-Codes
* hashCode Wert wird i.d.R. für keine Rechenoperation, sondern bei
  *HashCode-Verfahren* oder *Hashing-Methoden*

Konvention:

    * Wenn zwei Objekte per equals()-Methode identisch sind, müssen sie den
      gleichen Hash-Code haben
    * Wenn zwei Objekte per equals()-Methode nicht identisch sind, dürfen sie
      trotzdem den gleichen Hash-Code haben (aber es aber empfohlen zu
      unterscheiden, da sonst hashing-Methoden nicht möglich sind)

Wenn die equals-Methode überschrieben wird :ulined:`muss` gleichzeitig auch die
hashCode-Funktion überschrieben werden: **Ziel:** Es muss sichergestellt sein,
dass der return-Wert der hashCode()-Methode stets einen unterschiedlichen Wert
zurückgibt, wenn die equals()-Methode *false* ist und er identisch ist, wenn
diese *true* ist.

.. code-block:: java

    @Override
    public int hashCode() {
        return getLeistung() + anzahlTueren + getHersteller().hashCode();
    }

:ulined:`Hier`: Kombination aus Leistung, Anzahl der Türen und dem Hash-Code
des Strings hersteller.
