73. Threading Anomalien (Beispiele)
===================================
.. attention::

    Lokale Variablen in der run() Methode besitzt jeder Thread für sich selbst.
    Greifen die Threads zeitgleich auf eine globale Klassenvariable zu, so
    verändern sie diese parallel.

Example 1
---------
.. literalinclude:: _file/72_threading_anomalies/CrazyThreads1.java
    :language: java

Example 2
---------
.. literalinclude:: _file/72_threading_anomalies/CrazyThreads2.java
    :language: java

Example 3
---------
.. literalinclude:: _file/72_threading_anomalies/CrazyThreads3.java
    :language: java