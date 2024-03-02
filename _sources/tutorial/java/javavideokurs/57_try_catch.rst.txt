57. Exceptions behandeln (try-catch)
====================================
#. Der eventuell eine Fehlermeldung erzeugende Codeblock wird in einen Codeblock
   gesteckt und dieser mit try bezeichnet.
#. Direkt danach erfolgt eine catch-Methode. Dabei wird eine Variable vom Typ
   *Throwable* (oder eine ihrer Kinnklassen) angegeben (wir verwenden
   NullPointerException)
#. Der anschließende Codeblock beinhaltet die Reaktion beim Eintreten dieses
   Fehlertyps.

* Tritt im try-Block ein Ausnahmefehler auf, so wird sofort der catch-Block
  ausgeführt
* Nachdem der catch-Block ausgeführt wurde geht das Program nicht zurück in den
  try-Block in die nächste Zeile nach dem Fehler sondern setzt das Programm nach
  dem catch-Block fort
* Ein try-catch Block kann nur die Fehlertypen anfangen, die in ihm definiert
  wurden -> sinnvolles Abfangen nötig
* Ein Programm stürzt ab, wenn eine Exception auch nicht in letzter Instanz
  abgefangen wird
* Wird eine Exception nicht direkt in der Methode behandelt, so sickert sie
  durch in die letzte Instanz, von der sie aufgerufen wurde

.. code-block:: java

    try{
        Object o = null;
        o.toString();
    }catch(NullPointerException e) {
        System.out.println("Fehler, aber ist nicht so schlimm");
    }

**Checked Exceptions:**

Methode muss eine Ausnahmebehandlung besitzen (bei unchecked exceptions ist
dies optional), z.B.:

    .. code-block:: java

        try{
            FileReader f = new FileReader(new File ("C:/xxx"));
        }catch(FileNotFoundException e){
        }


* Eine Ausnahme (exception) kann allgemein behandelt werden (:java:`catch (Exception e))`
  oder jeder einzelne Ausnahmetyp kann separat behandelt werden
* Catch-Blöcke werden der Reihe nach durchgegangen. Sobald ein korrekter Typ
  gefunden wurde, wird kein folgender catch-Block mehr ausgeführt
* Der *finally*-Block wird immer ausgeführt, auch wenn kein Ausnahmefehler auftritt


    .. code-block:: java

        try{
            FileReader f = new FileReader(new File ("C:/xxx"));
        }catch(FileNotFoundException e){
        }
        finally{
                System.out.println("FINALLY!");
        }

    Z.B. wir dieser verwendet um einen Stream wieder zu schließen, wenn während
    des Einlesevorgang ein Fehler aufgetreten ist. Dieser muss nämlich geschlossen
    werden, um für andere Daten verfügbar zu sein (sonst müsste dieser Code in
    try und jedes catch eingefügt werden).

    **Fazit**: Ein *finally* muss nur dann gesetzt werden, wenn der nach dem
    catch-Block vorhandene Code ansonsten nicht mehr ausgeführt wird. In den
    anderen Fällen ist es nicht nötig, jedoch auch nie falsch.
