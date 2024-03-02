44. Break & Continue
====================
* Beide Anweisungen sollte möglichst sparsam eingesetzt werden (auch nicht in
  komplexen Codeteilen, da sie dort untergehen und unerwarteterweise eine Schleife
  beenden)
* sollten deutlich gemacht werden (z.B. Kommentar)

**break**

    Beendet die aktuelle Schleife.

    Wozu? Verhindert, dass bestimmter Code ausgeführt wird, sofern dessen Ausführung
    sinnlos ist.

**continue**

    Beendet den aktuellen Schleifengang.

    Wozu? Das 'continue' befindet sich in einer Bedingung, im Anschluss der komplexe
    Code (viele Ebenen). Durch diese Anordung erspart man sich eine Ebene im komplexen
    Code.

.. code-block:: java

    for (Auto a : autos )
    {
        //Version ohne continue
        if (a .getLeistung () > 100)
        {
            //komplexer Code (viele Ebenen)
        }

        //Version mit continue
        if(a .getLeistung () <= 100) {
            continue; // beendet den aktuellen Schleifendurchgang (der for-Schleife)
        }
        // komplexer Code (viele Ebenen)
    }
