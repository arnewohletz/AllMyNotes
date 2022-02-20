56. Ausnahmebehandlung (exceptions)
===================================
* Informationen über eine Fehlermeldung werden in einem Objekt gekapselt
* Die Klasse ist *Throwable*:

        :java:`printStackTrace()`: Die zuletzt aufgerufenen Klassen und Methoden
        werden wiedergegeben.

* Es werden nicht Objekte der Klasse Throwable, sondern dessen Kindklasse
  *Exception* erzeugt
* Error werden nur bei schwerwiegende Fehler verwendet häufig kann hier gar
  nicht reagiert werde (z.B. JVM stürzt ab)
* Die Klasse Exception besitzt zahlreiche Kindklassen, die sich hauptsächlich
  nur im Namen unterscheiden, um die Fehler besser zu kategorisieren
* Zwei Gruppen: Checked Exceptions + Unchecked Exceptions
* Unchecked Exceptions: RuntimeException und alle ihre Kindklassen
* Checked Exceptions: alle anderen Klassen in Exceptions
* Checked Exceptions: ein Exception-Objekt wird erstellt und weitergereicht
  (*throw*). Der Empfänger bearbeitet dann den Fehler oder reicht es weiter
  (eins muss passieren, sonst wird nicht kompiliert)
* Unchecked Exceptions: Behandlung ist komplett optional (-> hauptsächlich
  Bug-Handling)
