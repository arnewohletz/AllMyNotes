.. role:: java(code)
    :language: java
    :class: highlight

50. Scopes bei der Vererbung
============================
Es wird stets alles vererbt, auch die Methoden und Variablen die den
Access-Modifier private innehaben. Jedoch ist eine private Methode oder Variable
in der Kind-Klasse unsichtbar.

Enthält eine Superklasse die Variable :java:`int leistung`, wird diese vererbt.
Definiert die Kindklasse nun eine gleichnamige Variable so ersetzt diese die
vererbte Variable -> **Shadowing**
