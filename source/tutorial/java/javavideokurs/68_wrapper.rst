68. Wrapper & Auto-(Un) Boxing
==============================
* Jeden primitiven Datentyp kann man ‘wrappen'
* Die Wrapper befinden sich in deren einzelnen Klassen (8 Stück): Integer,
  Character, Byte, Short, Long, Double, Float, Boolean
* Wrapper-Objekte besitzen Instanzvariable. einen Konstruktor, einen Getter aber
  keinen Setter -> Wrapper-Objekte sind Immutable

.. code-block:: java

    Integer integer = new Integer("100") ;

:Integer(String s):

    Es wird ein String abgegeben und der Integer-Wert wird daraus herausgezogen
    (z.B. “100”). Ist dies zur Laufzeit nicht möglich, so gibt es eine
    Exception oder es wird ein Standardwert verwendet (z.B. false bei Boolean)
    -> gilt für alle Wrapper-Klassen

Die Wrapper-Klassen bieten viele Methoden -> in API nachschauen

.. hint::

    :java:`.hashCode()` nützlich um den HashCode eines eigenen Objekts möglichst
    einzigartig zu machen:

    .. code-block:: java

        @Override
        public int hashCode(){
            return getLeistung() + new Integer (1*AnzahlTueren).hashCode() + getHersteller().hashCode();
        }

    * Wrapper packen einen primitiven Datentyp in ein Objekt
    * essentiell bei generischen Datenstrukturen

.. code-block:: java

    Liste<Integer>liste = new Liste<Integer>(100);
    liste.add(new Integer(25));

:Auto Boxing:

    der Compiler kann primitive Datentypen selbstständig in entsprechende Wrapper-Objekte umwandeln

:Auto Un-Boxing:

    der Compiler kann Wrapper-Objekte selbstständig in entsprechende primitive Datentypen umwandeln

Man kann also auch schreiben:

.. code-block:: java

    Liste<Integer>liste = new Liste<Integer>(100);
    liste.add(25);

Der Compiler erkennt automatisch, dass er den primitiven Datentyp in einen Wrapper
packen muss, um ihn der Liste hinzuzufügen, daher kann man schlicht den primitiven
Typ angeben.

Genauso kann ein Abruf eines Listeneintrags  wandelt der Compiler das Wrapper-Objekt
automatisch in den primitiven Datentyp um (ruft dazu die Integer.intValue()
Methode auf): :java:`i = liste.get(0);`

Es können auch Rechenoperationen auf Wrapper-Objekte angewandt werden:

.. code-block:: java

    Double d1 = new Double(1.4);
    Double d2 = new Double(2.4);
    Double d3 = d1 + d2;

Hier passiert ebenso automatischen Boxing und Un-Boxing.

.. attention::

    **Vergleich von Wrapper-Objekten**

    .. code-block:: java

        Integer i1 = new Integer(50);
        Integer i2 = new Integer(50);

        System.out.println(i1 >= i2); // -> TRUE
        // true, weil die Werte gleich sind

        System.out.println(i1 == i2); // -> FALSE
        // false, da bei Integer in unterschiedlichen Objekten abgelegt sind
        //(== bedeutet bei Objekten Identität, nicht Wert)

        Integer i1 = 50;
        Integer i2 = 50;

        System.out.println(i1 == i2);-> TRUE
        // true, weil Integer Objekte  ebenso einen Constant Pool haben, wodurch
        Objekte mit gleichem Inhalt nicht erneut abgelegt werden.

        Integer i1 = 200;
        Integer i2 = 200;

        System.out.println(i1 == i2); // -> FALSE
        //Jedoch umfasst dieser nur den Wertebereich von -128 bis +127 😉

.. admonition:: Faustregel

    Bei größeren Vergleichen und Berechnungen verhindern, dass Auto-Boxing und
    Un-Boxing verwendet wird, da man sehr genau aufpassen muss, wann dies geschieht
    und wann nicht.

**BigInteger & BigDecimal**

* nur vom Speicher begrenzte Höhe des Wertes (nicht die typischen Grenzen)
* möglich, da die Klasse Werte intern als String speichert
* wird z.B. für sehr große Zahlen und genaueste Berechnungen verwendet (Double
  hat “nur” 64-Bit Genauigkeit und muss irgendwann runden)

Fehler passieren, wenn mit bereits gerundeten Werten weitergerechnet wird:

.. code-block:: java

    for (double d = 0; d <= 1.0; d += 0.1){
         System.out.println(d);
    }

Ergebnis:

.. code-block:: none

    0.0
    0.1
    0.2
    0.30000000000000004
    0.4
    0.5
    0.6
    0.7
    0.7999999999999999
    0.8999999999999999
    0.9999999999999999

* Auch die Werte dieser Klassen sind **Immutables**
* Auto-Boxing und Un-Boxing sind hier nicht verfügbar
