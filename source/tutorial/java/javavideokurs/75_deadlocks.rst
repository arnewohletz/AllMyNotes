75. Deadlocks
=============
Synchronisierungen können sogenannte *Deadlocks* (Verklemmung) erzeugen:
Zwei oder mehr Threads können nicht fortsetzen, weil sie auf ein Ereignis warten, welches nur
ein Thread aus dieser Menge bewirken kann.

'Producer-Consumer' Problem:

* :download:`Pipeline.java <_file/75_deadlocks/Pipeline.java>`: Enthält put() und get() Methode
* :download:`Producer.java <_file/75_deadlocks/Producer.java>`: Legt etwas in die Pipeline -> put()
* :download:`Consumer.java <_file/75_deadlocks/Consumer.java>`: Holt etwas aus der Pipeline -> get()

Regel:

* Der Producer kann nur etwas in die Pipeline legen, wenn diese leer ist und wartet bis diese leer ist
* Der Consumer kann nur etwas aus der Pipeline holen, wenn diese etwas enthält und wartet
  bis diese etwas enthält

:Problem:

    Synchronisierte Threads beschlagnahmen das Lock der Methode put() oder lock() für sich
    und lassen einen Wechsel in einen anderen Thread nicht mehr zu z.B:

        #. die Pipeline ist leer
        #. Thread 0 möchte etwas herausholen -> wartet in der gelockten Methode get() bis
           etwas hineinkommt
        #. Thread 1 möchte etwas hineintun -> kommt nicht in die put(), da diese mit dem
           gleichen Lock auf get() synchronisiert ist

:ulined:`Lösung`:

.. continue