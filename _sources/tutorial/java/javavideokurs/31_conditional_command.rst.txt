31 Bedingte Anweisung
=====================

**Konditional-Operatoren**

<Variable> = <Bedingung> ? <Wert bei true> : <Wert bei false>

<Variable> = <Bedingung1> ? <Bedingung2> ? <Wert bei true,true> : <Wert bei true,
false> : <Wert bei false,false>

**Beispiel**

.. code-block:: java

    String s;
    int j = 10;
    if (j % 2 == 0){
    s = "Zahl gerade";
    }
    else{
    s = "Zahl ist ungerade";
    }

    //Konditionaloperator
    s = j % 2 == 0 ? "Zahl gerade" : "Zahl ungerade"; // das gleiche wie oben

    s = j % 2 == 0 ? j == 0 ? "Zahl gerade (null)": "Zahl gerade": "Zahl ungerade";
