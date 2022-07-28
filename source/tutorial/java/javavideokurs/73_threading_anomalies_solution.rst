73. Threading Anomalies (Explanation)
=====================================

:Problem:

    Alle drei (fehlerhaften) Programme verwenden teilweise die gleichen Daten
    (shared data). Bei Daten, die nur ein Thread nutzt (z.B lokale Variablen)
    gibt es keine Probleme.

:CrazyThread1.java:

    Beide Threads nutzen die Instanzvariablen alive und i (main + c (Namen der Threads))

:CrazyThread2.java:

    Alle drei Threads nutzen die Instanzvariable x  (main + c + c)

:CrazyThread3.java:

    Alle drei Threads nutzen die Instanzvariable x  (main + a + a)

:ulined:`Zwei Arten von Anomalien:`

* Race conditions (Wettlaufsituation)
* Sequential consistency

:ulined:`Sequential consistency`

* Regel: Eine Änderung, welche zum Zeitpunkt 0 stattgefunden hat (z.B.
  Inkrementierung eines Wertes) ist zu einem Zeitpunkt 1, welcher zeitlich
  hinter dem Zeitpunkt 0 liegt, erfolgt.
* Problem: Dies ist in Java nur innerhalb eines Threads garantiert
* Ursache: Speichermodell in Java

    * einen globalen Speicher
    * je einen lokalen Speicher je Thread
    * beim ersten Zugriff eines Threads einer im globalen Speicher vorhandenen
      Variable kopiert sich der Thread diese vom globalen in seinen lokalen Speicher
    * fortan arbeitet der Thread mit der Kopie (schottet sich quasi vom Rest
      des Programms ab): ändert er die Variable nicht, so geht er davon aus,
      dass diese sich nicht verändert
    * Sequential consistency gilt nicht für den globalen Speicher
    * jeder Thread kann selbst entscheiden, ob und wann er seine lokalen Daten
      mit dem globalen Speicher erneut abgleicht (refresh) oder den globalen
      mit seinem lokalen Wert überschreibt (flush)

* Wenn jeder Thread vor jeder Veränderung 'refreshed' und nach der Veränderung
  'flusht' arbeiten die Prozessen nicht miteinander (Zeitpunkt des Refresh +
  Flush ist vollkommen willkürlich)
* Ein Flush am Ende des Threads ist sicher


:CrazyThread1.java:

    * beide Threads nutzen die Instanzvariablen alive und i (main + c)
    * Entweder der Thread gleicht seine Daten (alive) nicht mit dem main()-Thread
      ab (macht kein refresh) oder der main()-Thread behandelt seine Daten lokal und verändert ihn nicht im globalen Speicher (macht kein flush) oder beides
    * Resultat: das Programm endet nie, da alive stets true ist (der thread
      kriegt das false des anderen nicht mit)

:CrazyThread3.java:

    * alle drei Threads nutzen die Instanzvariable x  (main + a + a)
    * Gleich wie bei CrazyThread1.java:  Die Threads schreiben ihre lokalen
      Daten nicht stetig in den globalen Speicher und oder refreshen nicht. Bsp:

        #. Thread 1 refreshed + flushed: x = 0 -> x = 4000 (+4000)
        #. Thread 2 refreshed + flushed: x = 4000 -> x = 7000 (+3000)
        #. Thread 1 refreshed + flushed: x = 7000 -> x = 11000 (+4000) -> Bedingung ist erfüllt, Thread 1 beendet (total loops = 8000)
        #. Thread 2 refreshed: x = 11000 -> Bedingung ist erfüllt, Thread 2 beendet (total loops = 3000)

    * Resultat: Thread 1 und 2 ergeben zusammen nicht 10000 (wie gefordert)

:ulined:`Anderes Problem`

:CrazyThread2.java:

    * die Variable x wird erst abgefragt nachdem beide Threads beendet (und
      damit sicherlich geflusht haben)
    * es kann nicht die lokale Variable des main() Threads sein, da diese 0
      sein müsste

:CrazyThread3.java:

    * Ausgabe von 10001 kann nicht mit einem Refresh-Flush Problem zusammenhängen,
      da dieser erst nach Abschluss der Threads abgerufen wird

-> :ulined:`Race conditions`

* durch Scheduling verursacht: ungünstiges Wechseln von einem Thread zum nächsten
* es wird davon ausgegangen, dass bei jedem Aufruf einer Variablen diese refreshed
  und bei jeder Veränderung direkt geflusht wird
* So kommt die 10001 (CrazyThread3.java) zustande:

.. thumbnail:: _file/73_threading_anomalies/race_condition.png
    :title: Race Condition

* :ulined:`Wichtig`: Auch bei Mehrkernprozessoren ist ein echtes paralleles
  Auslesen und Speichern von Variablen nicht möglich (nur echt parallele
  Verarbeitung) da nicht parallel auf die gleiche Adresse im Hauptspeicher
  zugegriffen werden kann
* Non-repeatable-read' (Race condition Typ): Zweimaliges Auslesen (hier:
  if-Bedingung + if-Methode), wobei die Variable beim zweiten Lesen nicht mehr
  den gleichen Wert hat
* Race condition Typ: 'Lost update' (CrazyThread2.java): Zuweisung einer
  Variablen wird von einem anderen Thread überschrieben:

    * Thread wird während einer Zuweisung gewechselt - Bsp:

        #. Thread 1: Zuweisung x = x + 1; Ein x = 1 wird also x = 1+1 ->
           Bevor x = 2 tatsächlich Zugeweiung erfolgt, wechselt der Thread
        #. Thread 2: Liest aktuellen Wert x = 1 (immer noch) Zuweisung
           x = x + 1 = 1 + 1 = 2 -> Flusht in den Hauptspeicher
        #. Thread 1: Refreshed x nicht erneut, da er sich bereits bei '='
           befindet, also weist zu: x = 1 + 1 = 2 -> x = 2 wird in den
           Hauptspeicher geflusht, das bereits vorhanden x = 2 wird überschrieben
        #. -> bei zwei x++ Zuweisungen wurde x nur ein Mal erhöht

    * Viele Inkrementierung gehen verloren daher ist x nie 4000, sondern immer weniger

* Lost update' kann auf im CrazyThread3.java passieren: Inkremente müssen wiederholt werden,
  da sie x nicht erhöht haben

:ulined:`Faustregel` beim Multi-Threading:

Arbeiten mehrere Threads auf den selben Daten? Nein -> Kein Problem; Ja -> Anomalien
treten unregelmäßig auf, sind schwer auszumachen (Kollege testet gleichen Code und
bekommt das Problem nicht)