53. Keyword abstract
====================
#. Verwendung bei der Klassendefinition:

    .. code-block:: java

        public abstract class Fahrzeug {
        }

    bedeutet, dass es keine weitere Instanzen dieser Klasse erzeugt werden können.
    Konstruktoren einer abstrakten Klasse können nach wie vor über die
    Punktnotation super aufgerufen werden.

    -> Klassen, deren Begriff abstrakt ist (z.B Fahrzeug) und für das es keine
    Objekte geben soll, sollten als abstract definiert werden.

#. Definition einer Instanzmethode:

    Zwingt die Kind-Klasse diese Methode zu überschreiben

    .. code-block:: java

        public abstract void crashTest();

    Methode muss also gar nicht überschrieben, sondern in der Kind-Klasse erstmals
    definiert werden. Die Methode muss auch in der Kind-Klasse nicht zwingend
    definiert werden, sondern kann mit

    .. code-block:: java

        public abstract void crashTest();

    abermals an die folgende Kind-Klasse weitergereicht werden. Dann muss hier
    jedoch die Klasse ebenfalls als *abstract* definiert werden.

    -> Wenn auch nur eine Methode in der Klasse als abstrakt definiert wurde,
    so muss die Klasse als abstract definiert sein.

    Wird dann angewandt, wenn alle Kind-Klassen diese Methode benötigen, aber
    stets unterschiedlich implementiert werden müssen.
