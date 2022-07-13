71. Thread & Runnable
=====================
Die main() Methode ist lediglich ein Thread.

**Möglichkeit 1: Klasse Thread (nicht so gut)**

* Ein neuer Thread wird in Java über Thread-Objekte erzeugt (Klasse Thread)
* Die :java:`Thread.run()` Methode erzeugt einen neuen Thread: leerer Rumpf
* run() Methode muss überschrieben werden

    .. code-block:: java

        public class MyTask extends Thread{

            @Override
            public void run(){
                //Code für den zusätzlichen Thread
            }
        }

* Die start() Methode erzeugt einen neuen Thread (asynchrone Methode)

    #. Ein neuer Systemthread wird erzeugt
    #. In diesem wird die run() Methode aufgerufen
    #. Direkt danach wir die start() Methode wieder verlassen und die main()
       Methode läuft parallel zur run() Methode

    .. code-block:: java

        MyTask t = new MyTask();
        t.start();

* Ein Thread kann in einer Instanz nur ein Mal gestartet werden
* Zum erneuten Aufrufen der run() Methode muss eine neue Instanz erzeugt werden

.. hint::

    Mit :java:`Thread.sleep(long millies)` wird der Prozess für x Millisekunden
    pausiert.

* Ein Multi-Thread Program stürzt erst dann ab wenn kein Thread mehr läuft
* Es stürzt nicht automatisch mit dem Absturz der main() Methode ab
* Wie die Threads eines Programm auf die CPU-Kerne verteilt werden liegt in der
  Hand des Schedulers (wir haben darauf keinen Einfluss)
* In der Praxis sollten nicht zu viele Threads parallel existieren
* Es ist nicht wichtig wo im Program neue Threads erzeugt werden

**Möglichkeit 2: Interface Runnable (Unbedingt vorzuziehen!!!)**

* Besitzt nur die run() Methode
* Die Klasse Thread implementiert diese run() Methode:

    .. code-block:: java

        public class MyTask implements Runnable{

* Um Methoden der Thread Klasse zuzugreifen wird die Instanzmethode Tead.currentThread()hr verwendet:

    .. code-block:: java

        Thread.currentThread().getName()

* Der Rest in the Klasse bleibt gleich
* In der main() Methode wird der Zugriff auf die start() Methode über das
  Erzeugen eines neuen Thread Objektes ermöglicht, welcher eine Runnable als
  Übergabeparameter akzeptiert:

    .. code-block:: java

        MyTask t = new MyTask();
        Thread thread = new Thread(t);
        thread.start();

* Es wird die start() Methode der übergebenen Runnable ausgeführt (nicht die
  Thread.start() Methode)
* :ulined:`Vorteil`: Die Implementierung von einem Interface ist stets
  möglich, jedoch gibt es keine Mehrfachvererbung in Java (deadly diamond of
  death). Somit kann eine Klasse die bereits eine Klasse beerbt nicht mehr von
  der Klasse Thread erben

:ulined:`Thread beenden` (bevor die run() Methode abgeschlossen ist)

Falscher Weg:

    * Thread.stop() Methode
    * Die Methode ist veraltet (deprecated)

Richtiger Weg:
Sauberes Beenden des Threads durch eine Bedingung in der Thread-Klasse, welche eine
Variable verändert und damit das Beenden des Threads hervorruft:

    #. Initialisierung eines boolean Wertes :java:`private boolean alive;`
    #. Bedingung in die run() Methode schreiben, welche die Methode durch
       return beendet sobald der boolean false ist:

        .. code-block:: java

            if(!alive ){
            System. out.println("Stopping!" );
              return;
            }

    #. Eine Methode definieren, welche die Variable verändert:

        .. code-block:: java

            public void cancel(){
                alive = false;
            }

    #. Die Abbrechmethode (hier: cancel()) wird vom den Thread aufrufenden
       Thread aufgerufen: :java:`t.cancel();`

Hinweise zum Verwenden von neuen Threads:

* keinen neuen Thread für kleine Berechnungen
* für Dinge, die im Hintergrund laufen sollen (z.B. regelmäßiges Abgleichen
  von Daten)
* zu viele Threads überlasten den Rechner wegen des Scheduling
  (Geschwindigkeitsgewinn geht zurück)
