70. (Multi-) Threading
======================

:Tread:

    Menge an nacheinander aufzurufenden Befehlen (kompilierter Quellcode)

* Vor den Mehrkern-Prozessoren: Es gab keine echte zeitgleichen Threads - Threads
  wurden nur unterbrochen zugunsten von anderen Threads. Diese Wechsel zwischen
  den Threads passiert in so schneller Abfolge, dass diese zeitgleich :ulined:`erscheinen`
* Mehrkern-Prozessoren ermöglichen echte parallele Verarbeitung von Threads
* Multi-Threading bringt nur dann eine Performance-Steigerung, wenn die Kerne nicht
  bereits von anderen Threads belegt sind
* Ohne mehrere Threads in ein Programm einzubauen lässt sich die mögliche
  Performance-Steigerung von Mehrkernprozessoren nicht nutzen
* Theoretische Performance-Steigerung: +100 % pro Kern sofern ein (weiterer) Thread
  des Programms auf diesem läuft
* Multi-Thread Programme sind auch auf 1-Kern-Prozessoren ausführbar (laufen nur
  langsamer)
* Task Management: Scheduler (vom Betriebssystem) verwalten die Threads, an Stelle
  des Programms -> wird ein Code zu kompliziert kann ich den Code im Threads packen
  und dem Scheduler die zeitliche Steuerung überlassen

