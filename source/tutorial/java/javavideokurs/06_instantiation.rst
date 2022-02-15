6. Instanz-Initialisierung
==========================

#. Die Vater-Klasse(n) werden initialisiert, d.h. deren Methoden und
   Instanzvariablen werden an die jeweiligen Kind-Klassen übergeben.
#. durchsucht Klasse zeilenweise nach Instanzvariablen initialisiert diese
   (legt sie im Speicher an), weißt aber noch keinen Wert zu.
#. Instanzvariablen werden Werte zugewiesen.
#. Konstruktor-Rumpf wird durchgeführt.

.. admonition:: Design Tips

    * Instanzvariablen, die für alle Objekte dieser Klasse gelten sollen, nicht
      in den Konstruktor-Parametern sondern in der Klasse zuweisen (ginge zwar
      auch im Konstruktor-Rumpf, allerdings ist die Zuweisung zu Beginn der
      Klasse leichter für andere ersichtlich)
    * Auch wenn Default-Werte benötigt werden sollten Variablen trotzdem explizit
      deklariert werden (auch mit default-Werten)
