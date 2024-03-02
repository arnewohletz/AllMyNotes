29. Garbage Collector
=====================
Durchsucht den *heap* nach nicht benötigten Objekten, d.h. nicht mehr referenzierte
Objekte. Der *stack* zerstört sich selbst -> nicht Aufgabe des GC

.. admonition:: Definition

    Der *Stack* (Stapel) ist der Teil des Arbeitsspeichers, welcher zur Laufzeit
    des Programms die Informationen zum Programmablauf und lokale Variablen
    speichert. Jeder Thread erhält einen eigenen Stack. Die Größe des Stacks ist
    recht klein und strikt limitiert (maximal einige MB groß). Objekte im Stack
    werden automatisch zerstört, wenn der Aufruf beendet ist (LIFO-Prinzip).


.. admonition:: Definition

    Der *Heap* (Haufen) ist der Teil des Arbeitsspeichers, welcher zur Laufzeit
    des Programms die meisten Objekte speichert. Seine Größe ist variabel und kann
    den sogar den gesamten verfügbaren Arbeitsspeicher einnehmen. Aufrufe sind
    deutlich langsamer als beim Stack und Speicher muss explizit wieder freigegeben
    werden (bei Java erledigt dies zumeist der Garbage Collector).


.. code-block:: java

    new String("Ich bin gleich weg...:-(");

-> das Objekt kann nach der Erstellung nicht mehr referenziert werden und wird somit
direkt gelöscht

.. code-block:: java

    System.gc();

Methode bittet den Garbage Collector zu arbeiten (er kann dies auch verweigern)
-> keine Optimierungsmethode

**Tips**

* Man sollte darauf achten, dass Objekte, die nicht mehr benötigt werden auch
  nicht mehr referenziert werden, damit sie gelöscht werden
* Vorhandene Variablen, welche auf ein nicht mehr vorhandenes Objekt referenzierten,
  sollten für neue Objekte wiederverwendet werden und nicht stets für neue Objekte
  neue Variablen erzeugen (insbesondere Instanzvariablen, die stets in der Klasse
  existieren; Lokale Variablen sind im Stack, werden automatisch gelöscht))
