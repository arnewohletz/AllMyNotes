47. Vererbungshierarchie
========================
* Es kann mehrere Vererbungsstufen geben
* Die unterste Stufe erbt von allen ihm überstehenden Klassen, die sich zwischen
  ihm und der Superklasse befinden
* Die Superklasse aller Superklassen heißt *Object*
* Mehrfachvererbung ist in Java nicht möglich, d.h. eine Klasse kann nicht von
  mehreren Klassen erben (-> `Deadly Diamond of Death <https://en.wikipedia.org/wiki/Multiple_inheritance>`__)
  -> Problematisch, wenn in diesen identische benannte Variablen oder Methoden
  existieren
