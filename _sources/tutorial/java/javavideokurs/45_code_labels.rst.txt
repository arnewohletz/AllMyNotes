45. Code Labels
===============
* Bezeichnen einen bestimmte Menge an Code
* Einzig sinnvoller Nutzen ist das **Beenden von verschachtelten Schleifen**, die
  sonst nur über mehrfachen Aufruf von break bzw. continue beendet werden könnten
* Mehrere ineinander verschachtelte Schleifen können jeweils gelabelt werden
* Sollte nur für die **Bezeichnung verschachtelter Schleifen** verwendet werden -
  für sonst nichts!
* Viele halten Code Labels für überflüssig und gefährlich

.. code-block:: java

    meineGeschachtelteSchleife: for(int j = 0; j < 10; j++)
    {
        meineZweiteSchleife: for(int k = 0; k < 10; k++)
        {
            if (j == 5 && k == 5)
            {
                break meineGeschachtelteSchleife; // innere und äußere for-Schleife wird beendet
            }
            else if (k >=5)
            {
                continue meineZweiteSchleife; // beendet alle Schleifendurchgänge, bei denen k größer gleich 5 ist
            }
            System. out.println("j = " + j + ", k = " + k );
        }
    }
