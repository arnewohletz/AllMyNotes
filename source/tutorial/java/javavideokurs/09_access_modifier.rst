9. Access Modifiers
===================
Definieren Sichtbarkeit für andere Klassen. Vier verschiedene:

**package private**

    Nur verfügbar für alle Klassen im gleichen Package (wird verwendet,
    sofern kein anderer angeben ist).

**protected**

    (Derzeit) wie *package private* (später mehr).

    .. admonition:: Update

        Wie *package private*, aber auch für Kind-Klassen verfügbar die nicht
        im gleichen Package liegen.

**public**

    Verfügbar im gesamten Projekt, auch von Klassen in anderen Packages.

**private**

    Nur in dieser Klasse verfügbar.


Richtlinien
-----------
#. Alle Instanz-Variablen müssen private gemacht werden (Zugriff nur über getter und setter)
#. Alle anderen Elemente in der Regel public