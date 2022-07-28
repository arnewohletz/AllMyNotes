74. Synchronisation
===================

:Problem:

    * Threads müssen dazu gezwungen werden stets zu refreshen (vor einer Änderung) und zu flushen
      (nach einer Änderung) -> sequential consistency
    * Switchen des Schedulers an kritischen Stellen im Code muss verhindert werden (race conditions)

:Lösung:

    Synchronisierung der Threads

:ulined:`CrazyThread2.java -> SynchedThread2.java`

.. literalinclude:: _file/74_synchronization/SynchedThreads2.java
    :language: java
    :caption: SynchedThreads2.java

.. code-block:: java

    static Object lock = new Object();
        for ( i = 0; i < 2000; i++){
            synchronized(lock ){
                x++;
            }
        }

Änderungen:

    #. Es wird ein referenziertes Objekt initialisiert
    #. Das Inkrement x++ wird in einem synchronized-Codeblock ausgeführt:
       synchronized(<Verweis auf Object>){ Codeblock }

    -> Der Verweis darf nicht den Wert null enthalten, daher darf kein
    nicht-referenzierte leeres Objekt verwendet werden

Folgende Schritte werden beim synchronized-Block abgearbeitet:

#. Lock des referenzierten Object wird erlangt

    * jedes Objekt besitzt ein Lock (auch Monitor genannt)
    * sofern ein anderer Thread bereits den Lock hat wird gewartet bis er wieder frei ist

#. Refresh vom globalen auf den lokalen Speicher wird ausgeführt
#. Synchronisationsrumpf wird abgearbeitet
#. Flush vom lokalen Speicher auf den globalen Speicher
#. Lock wird wieder freigegeben

- sequential consistency ist gewährleistet da sicheres refreshen und flushen vor und nach der Veränderung
- race conditions Fehler passieren nicht, da ein Thread so lange pausieren muss, solange
  der das Lock nicht hat (nur ein Thread kann zeitgleich seinen Synchronsationsrumpf ausführen)

:ulined:`Wichtig:`

* Alle betroffenen Threads müssen auf das gleiche Objekt synchronisieren
* Welches Objekt verwendet wird, ist nicht wichtig
* Der main-Thread muss ebenfalls synchronisiert werden

z.B. SynchedThreads2.java

main-Thread -> verwendet Object c: :java:`synchronized (c)`

Thread 1 -> verwendet ebenfalls Object c, also muss auf this gelockt werden: :java:`synchronized (this)`

:ulined:`SynchedThread3.java`:

.. literalinclude:: _file/74_synchronization/SynchedThreads3.java
    :language: java
    :caption: SynchedThreads3.java

.. code-block:: java

    while (true )
        {
            synchronized (this )
            {
                if (x < 10000)
                {
                    x++;
                    loops++;
                }
                else
                {
                    break;
                }
            }
        }

:ulined:`Hinweis`:

* Der Synchronized Codeblock darf nicht innerhalb der if-Bedingung gesetzt werden,
  da dann noch immer nach der Prüfung x < 10000 der Thread gewechselt werden kann und
  somit das Ergebnis 10001 möglich ist
* Wäre die while-Schleife nicht in if-else getrennt, würde der erste Thread die
  Inkrementierung vollständig abschließen (erst bei 10000 wird der Block verlasssen).
  Der zweite käme nicht zum Zug:

    .. code-block:: java

        synchronized(this ){
            while(x <10000) {
                x++;
                loops++;
            }
        }

    Ergebnis:

        * Thread-1 has finished after 0 loops
        * Thread-0 has finished after 10000 loops
        * x is: 10000

:ulined:`SynchedThread1.java:`

.. literalinclude:: _file/74_synchronization/SynchedThreads1.java
    :language: java
    :caption: SynchedThreads1.java

* Ebenfalls den Rumpf der while-Schleife synchronisieren
* Im main-Thread muss nicht der ganze Rumpf, sondern nur die einzelnen Zugriffe synchronisiert werden

Hinweise:

* Flushen und Refreshen kostet Zeit
* Optimierung von Synchronisationsmomenten ist eine eigene Disziplin
* Je mehr synchronisiert wird, desto geringer wird der Geschwindigkeitsvorteil von Multi-Thread
* Wiederholung: die stop() Methode sollte nicht zum Beenden eines Threads verwendet werden,
  weil dieser beendete Thread sein lock dadurch frei gibt. Die Synchronized-Blocks der anderen
  Threads die das gleiche Lock verwenden werden dadurch frei zum Start. Falls eine Veränderung
  zu diesem Zeitpunkt nicht wie gewünscht abgeschlossen war, führt dies womöglich zu beliebigem
  Verhalten des Objekts, sofern andere Threads eingreifen

:ulined:`MultiThreadingDemo.java`:

.. literalinclude:: _file/74_synchronization/MultiThreadingDemo.java
    :language: java
    :caption: MultiThreadingDemo.java

* Das Programm funktioniert scheinbar auch ohne Synchronisation (vermutlich führen bestimmte
  Anweisungen in der MyTask.java zum Refresh und Flushen)
* man sollte sich jedoch auf so etwas nie verlassen und stets Synchronisationsblöcke verwenden

Die alive-Abfrage in der MyTask Methode:

.. code-block:: java

    synchronized (this )
        {
            if (!alive )
            {
                 System. out.println("Stopping!" );
                 return;
            }
        }

und den Aufruf der cancel()-Methode in der main-Methode:

.. code-block:: java

    synchronized(t){
        t.cancel();
    }

:ulined:`oder` in der alive-Abfrage der cancel() Methode selbst:

.. code-block:: java

    public void cancel()
        {
            synchronized(this ){
                alive = false;
            }
        }

:ulined:`Tip`: Synchronisieren einer kompletten Methode (z.B. cancel())

.. code-block:: java

    public synchronized void cancel()
    {
        alive = false;
    }

Es ist auch möglich statische Methoden zu synchronisieren:

.. code-block:: java

    public static synchronized void x() {
        synchronized(MyTask.class ){

        }
    }

Hier wird direkt auf die Objekt MyTask.class synchronisiert (wie das genau abläuft ist hier egal).
