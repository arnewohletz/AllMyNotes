Break: Übungsaufgaben
=====================
Die folgenden Übungen wurden gemeinsam im Kurs gelöst und greifen hauptsächlich
bereits besprochene Themen auf, um diese zu üben. Wenige neue Dinge, werden hier
jedoch ebenfalls erläutert.

Übung 1: Zutreffende Listeneinträge highlighten
-----------------------------------------------
Ein Eingabefeld führt zum Highlighten von Listeneinträgen die diese Eingabe-String
mit enthalten.

.. literalinclude:: _file/day_08/01_index.html
    :language: html

.. literalinclude:: _file/day_08/01_index.js
    :language: javascript

Übung 2: E-Book Darstellung
---------------------------
Ein Darstellung für ein E-Book, mit Sprung-Buttons.

.. literalinclude:: _file/day_08/02_index.html
    :language: html

.. literalinclude:: _file/day_08/02_index.js
    :language: javascript

Übung 3: Font-Size ändern
-------------------------
Aufgabe A: Über vier verschiedene Button soll ein Text in einer dem Button
zugehörigen Schriftgröße auf einen Text angewandt werden.

.. literalinclude:: _file/day_08/03_a_index.html
    :language: html

.. literalinclude:: _file/day_08/03_a_index.js
    :language: javascript

Aufgabe B: Über zwei Button (Plus & Minus) soll ein Text verkleinert und
vergrößert werden.

.. literalinclude:: _file/day_08/03_b_index.html
    :language: html

.. literalinclude:: _file/day_08/03_b_index.js
    :language: javascript

Über ``getComputedStyle(elem)`` werden alle anliegenden Styles eines Elements
zurückgegeben. Sie ist Read-Only und nicht sehr performant, sollte daher sparsam
eingesetzt werden.

.. code-block:: javascript

    const para = document.querySelector("p");
    let paraStyleObj = getComputedStyle(para);

    // Style auslesen
    console.log(paraStyleObj.fontSize);  // "50px"

.. hint::

    Bei Weiterarbeit sollte ein Style-Wert als Inline-Style an das Objekt
    angehängt werden oder im Storage gespeichert werden (um erneuten Aufruf
    von ``getComputedStyle()`` zu vermeiden).

DOM-Navigation
==============
Von einem selektierten Element kann man zu verbundenen Elementen gehen, wie
*Eltern-Knoten* (über ``ParentNode`` und ``ParentElement``) und *Kinder-Knoten*
(über ``ChildNode`` oder ``ChildElement``).

.. important::

    Wenn klar mit Elementen gearbeitet wird, stets mit *Element* Methoden arbeiten,
    nicht mit *Node* Methoden.

.. csv-table:: Übersicht - Knoten können auch Text und Kommentarknoten sein!
    :header: Traversal, Beschreibung

    ``parentNode``, Verweis auf Eltern-Knoten des aktuellen Knotens
    ``parentElement``, Verweis auf Eltern-Element des aktuellen Knotens

    ``childNodes``, alle Kind-Knoten eines Elementes (auch Text- und Kommentar-Knoten)
    ``children``, alle Kind-Elemente eines Knotens
    ``childElementCount``, Anzahl der Kind-Elemente

    ``firstChild``, Verweis auf ersten Kind-Knoten
    ``lastChild``, Verweis auf letzten Kind-Knoten
    ``firstElementChild``, Verweis auf erstes Knd-Element
    ``lastElementChild``, Verweis aus letztes Kind-Element

    ``previousSibling``, Verweis auf vorhergehenden Geschwister-Knoten
    ``nextSibling``, Verweis auf nachfolgenden Geschwister-Knoten
    ``previousElementSibling``, Verweis auf vorhergehendes Geschwister-Element
    ``nextElementSibling``, Verweis auf nachfolgendes Geschwister-Element
