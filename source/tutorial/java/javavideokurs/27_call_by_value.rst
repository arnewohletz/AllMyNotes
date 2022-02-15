.. _java_call_by_value:

27. Call by Value
=================
Wird Variable an eine Methode oder einen Konstruktor übergeben, so wird eine
neue Variable angelegt und der Wert der ursprünglichen in diese hinein kopiert
und die neue Variable an die Methode (oder den Konstruktor) übergeben.

Gibt die Methode keinen Wert zurück, wird der Wert der ursprüngliche Variable
nicht überschrieben und der ursprüngliche Wert gilt weiterhin (siehe Beispiel).

Gibt die Methode einen Wert zurück und die Variable wird dieser Rückgabewert
zugewiesen, wird der Wert der ursprünglichen Variable überschrieben (siehe Beispiel).

Gibt die Methode, welche den Wert der Variablen verändert, diese nicht zurück,
so ist der Variable nach kein neuer Wert zugewiesen -> 10

Gibt die Methode, welche den Wert der Variablen verändert, diese zurück, so
wird der Variable der veränderte Wert zugewiesen -> 20

Die Übergabe der ursprünglichen Variablen an die Methode heißt
:ref:`Call by Reference <java_call_by_reference>`.

**Beispiel**:

.. code-block:: java

    public static void main(String[] args) {
        int a = 10;
        doStuff(a);
        System.out.println("Nach der Methode ohne Rückgabe: " + a);
        a = doOtherStuff(a);
        System.out.println("Nach der Methode mit Rückgabe: " + a);
    }

    static void doStuff(int i) {
        i *= 2;
        System.out.println("In der Methode: " + i);
    }

    static int doOtherStuff(int i) {
        i *= 2;
        return i;
    }

**Output:**

.. code-block:: none

    In der Methode: 20
    Nach der Methode ohne Rückgabe: 10
    Nach der Methode mit Rückgabe: 20

