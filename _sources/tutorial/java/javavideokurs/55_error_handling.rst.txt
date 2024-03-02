55. Error Handling (Theorie)
============================
#. Fehler bei Verwendung von externen Dateien: z.B. Lese- oder Schreibzugriff wird
   verweigert, Festplatte kaputt (Hardwaredefekt).
#. Ungültige Eingabe (Fehlbedienung).
#. Bugs (selbst verschuldet).

**Problem:** Häufig wissen wir gar nicht, wozu das Objekt später verwendet wird,
d.h. wir können bei der Programmierung eines Objekts gar nicht abschätzen, auf
welche Fehler wird reagieren müssen.

**Beispiel:** Die Klasse ‘File’ besitzt Methoden die einen String erwarten
(z.B. Pfad der externen Datei). Diese Klasse wurde von Sun entwickelt. Den
Einsatz der Entwickler für die Klasse kann vielfältig sein. Also muss versucht
werden, auf möglichst viele Fehlbenutzung eine Fehlerbehandlung zu implementieren
(z.B. Pfad enthält nicht die benötigte Datei).

Da je nach Anforderung unterschiedlich auf den Fehler reagiert werden muss ist
es nicht sinnvoll bereits in der Klasse eine allgemein gültige Fehlerbehandlung
zu implementieren, sondern die Verantwortung dafür an den Entwickler zu geben.
Dieser muss den Fehler durch den Code reichen bis eine Methode gefunden wurde,
die alle nötigen Parameter hat, um korrekt auf den Fehler reagieren zu können.
Dies ist resultiert in der Regel jedoch in jeder Menge Daten (wenig effizient).

**Lösung:** Ausnahmebehandlung
