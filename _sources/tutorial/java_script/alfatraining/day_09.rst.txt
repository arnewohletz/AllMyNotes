DOM Operationen
===============
DOM-Elemente erstellen & einfügen
---------------------------------
Über ``document.createElement()`` lässt sich ein neues Element im Speicher erzeugen.
Dieses kann im Speicher weiter definiert werden.

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");
    let item = document.createElement("li");
    console.log(item);

.. hint::

    Jedes Element hat eine Constructor-Funktion, über welche ebenfalls ein
    entsprechendes Element erstellt werden kann.

.. important::

    Ein Element sollte zuerst fertig definiert werden bevor es dem DOM
    hinzugefügt wird.

Über ``[node].appendChild()`` in den DOM eingefügt werden. Die Funktion muss auf dem
**Elternelement** angewandt werden und wird als **letzter Kind-Knoten** eingefügt.
Das eingefügte Element wird als Rückgabewert zurückgegeben.

.. code-block:: javascript

    unorderedList.appendChild(item);  // gibt 'item' zurück
    console.log(item);

DOM-Element duplizieren
-----------------------
Soll ein ähnliches, bereits vorhandenes Element hinzugefügt werden, kann über
``[node].cloneNode()`` eine Kopie eines Knotens duplizieren. Wird das ``deep``
Argument als ``true`` übergeben, wird der gesamte Inhalt des Knotens (inklusive
Textinhalt und aller möglichen Child-Nodes) mit dupliziert.

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");
    let firstItem = unorderedList.querySelector("li");

    let item = firstItem.cloneNode(true);
    item.classList.add("cloned");
    unorderedList.appendChild(item);

.. hint::

    Event-Handler von Nodes werden **nicht** dupliziert.

Knoten verschieben
------------------
Über ``.appendChild()`` kann ebenso ein bereits in der DOM vorhandenes Element
als letzter Kind-Knoten eines Eltern-Knotens verschoben werden.

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");
    // zweites Element (CSS zählt von 1)
    let item = unorderedList.querySelector("li:nth-of-type(2)");
    console.log(item);
    unorderedList.appendChild(item);  // letztes Element

Knoten löschen
--------------
Über ``[node].remove()`` wird ein Element aus dem DOM gelöscht und die Referenz
auf das Element im Speicher zurückgegeben. Jedoch bleiben mögliche Referenzen
im Speicher erhalten.

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");
    let delItem = unorderedList.querySelector("li");
    delItem.remove();  // lösche aus DOM
    console.log(delItem);   // delItem is still here!

Früher wurde die ``[parent_node].removeChild()`` Methode angewandt (auch hier
wird die Referenz auf das aus DOM gelöschte Element zurückgegeben):

.. code-block:: javascript

    let oldItem = unorderedList.querySelector("li");
    let removedItem = unorderedList.removeChild(oldItem);

Knoten ersetzen
---------------
Über ``[parent_node].replaceChild(new, exists)`` wird ein Kind-Knoten einer Node durch
einen anderen Knoten ersetzt. Der Rückgabewert ist das Element, welches ersetzt
wurde.

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");
    let item = document.createElement("li");
    item.textContent = 5;
    item.className = "replace";

    let firstItem = unorderedList.querySelector("li");
    let oldItem = unorderedList.replaceChild(item, firstItem);

Über ``replaceChildren(new)`` werden **alle** Kind-Knoten eines Eltern-Knoten durch
neue Elemente oder Strings ersetzt.

.. code-block::

    const unorderedList = document.querySelector("ul");
    let item_2 = document.createElement("li");
    let item_3 = document.createElement("li");
    item_2.textContent = 55;
    item_3.textContent = 66;
    unorderedList.replaceChildren(item_2, "Kleiner Text im Regen ...", item_3);

Zuletzt kann über ``replaceWith()`` ein existierendes Element durch eine Vielzahl
von Elementen ersetzt werden. Die Elemente werden als einzelne Argumente übergeben.

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");
    let item_2 = document.createElement("li");
    let item_3 = document.createElement("li");
    item_2.textContent = 111;
    item_3.textContent = 222;
    let firstItem = unorderedList.querySelector("li");
    firstItem.replaceWith(item_2, "Kleiner Text im Schnee...", item_3);

Alle Elemente im DOM erreichen
------------------------------
Über ``[parent_node].insertBefore(item, ref)`` kann ein Knoten **vor** einem
beliebigen Referenzknoten innerhalb eines Eltern-Knotens eingefügt werden

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");
    let item = document.createElement("li");
    item.textContent = 6;
    item.className = "insert";

    let refNode = unorderedList.querySelector("li:nth-of-type(3)");
    unorderedList.insertBefore(item, refNode);

HTML Template verwenden
=======================
Über ``[node].content`` lässt sich auf den Inhalt eines ``<template>`` Elements
zugreifen. Dieser gibt einen ``DocumentFragment`` zurück, welcher alle Nodes des
Templates beinhaltet und welcher sich beliebig weiterverarbeiten lässt (z.B. klonen).

Beispiel:

.. code-block:: javascript

    const CONTENTS = [
        {
            headline: "Headline",
            subline: "Subline",
            content_1: "Content 1",
            content_2: "content 2"
        },
        {
            headline: "Headline 2",
            subline: "Subline 2",
            content_1: "Content 1-2",
            content_2: "content 2-2"
        },
        {
            headline: "Headline 3",
            subline: "Subline 3",
            content_1: "Content 1-3",
            content_2: "content 2-3"
        }
    ]

    const template = document.querySelector("#template");

    for (let i = 0; i < CONTENTS.length; i++) {
        let actObj = CONTENTS[i];
        let clone = template.content.cloneNode(true);

        clone.querySelector("h1").textContent = actObj.headline;
        clone.querySelector("h2").textContent = actObj.subline;
        clone.querySelector(".content_1").textContent = actObj.content_1;
        clone.querySelector(".content_2").textContent = actObj.content_2;
        document.body.appendChild(clone);
    }

DOM Elemente über Adjacent-Methoden platzieren
==============================================
Über die *adjacent*-Methoden lassen sich Knoten an bestimmte Position von direkt
angrenzenden Knoten verschoben.

Über ``[target_element].insertAdjacentElement("position", element)`` wird ein
Element an eine benachbarte Position des ``target_element`` eingefügt. Dabei wird
die bisherige Position des Elements, sofern im DOM vorhanden, verlassen, das
Element also verschoben.

Folgende "position" Werte sind möglich:

* ``"beforebegin"``: Vor dem ``[target_element]`` selbst
* ``"afterend"``: Nach dem ``[target_element]`` selbst
* ``"beforeend"``:Direkt innerhalb dem ``[target_element]``, vor dessen ersten Kind
* ``"afterbegin"``: Direkt innerhalb dem ``[target_element]``, nach dessen letzten Kind

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");

    let item = document.createElement("li");
    item.textContent = 7;
    item.className = "adjacent";

    unorderedList.insertAdjacentElement("beforebegin", item);
    unorderedList.insertAdjacentElement("afterbegin", item);
    unorderedList.insertAdjacentElement("beforeend", item);
    unorderedList.insertAdjacentElement("afterend", item);

.. important::

    Elemente werden über Referenzen verschoben, d.h. das Element wird bei erneuter
    Übergabe in ``insertAdjacentElement()`` verschoben, **keine zusätzliches Element**
    eingefügt.

Über ``[elem].insertAdjacentHTML()`` lässt sich ein **DOM-String** (mit HTML-Markup)
an eine bestimmte Stelle innerhalb eines *target_element* einfügen:

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");

    const domString = "<li class=\"domString\">8</li>";

    unorderedList.insertAdjacentHTML("beforebegin", domString);
    unorderedList.insertAdjacentHTML("afterbegin", domString);
    unorderedList.insertAdjacentHTML("beforeend", domString);
    unorderedList.insertAdjacentHTML("afterend", domString);

.. important::

    Hier wird **keine Referenz** für HTML übergeben, d.h. es werden bei mehrfachen
    Aufruf der ``insertAdjacentHTML``-Methode mehrfache DOM-Strings ins HTML eingefügt.
    Dies gilt es zu beachten.

.. important::

    Mit DOM-Strings lassen sich Elemente **nicht** zunächst im Speicher anpassen
    und zuletzt einfügen. Daher ist generell die Anwendung von anderen Methoden,
    z.B. ``insertAdjacentElement``, welche **keine DOM-Strings** verwenden, vorzuziehen.

Über ``insertAdjacentText("position", string)`` lässt sich ein **Text** (ohne Markup,
wird nicht gerendert) an eine bestimmte Stelle innerhalb eines *target_elements*
eingefügt:

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");

    // Hint: <b> Tags werden NICHT gerendert
    const myStr = "Kleiner Text im <b>Schnee<b>"

    unorderedList.insertAdjacentText("beforebegin", myStr);
    unorderedList.insertAdjacentText("afterbegin", myStr);
    unorderedList.insertAdjacentText("beforeend", myStr);
    unorderedList.insertAdjacentText("afterend", myStr);

Neue ES6 Methoden zum Platzieren
================================
Mehrere Objekte als Kind-Objekte platzieren
-------------------------------------------
Seit ES6, lassen sich über ``[node].prepend(1+ elem/string)`` und
``[node].append(1+ elem/string)`` **mehrere Objekte** mit einem Aufruf im DOM platzieren.
Außerdem lassen sich auch Strings platzieren (jedoch **keine** DOM-Strings),
nicht nur Knoten. Beide Methoden haben keinen Rückgabewert.

* ``[node].prepend(1+ elem/string)``: add node objects **before the first child**
  of the ``[node]``
* ``[node].append(1+ elem/string)``: add node objects **after the last child**
  of the ``[node]``

.. code-block:: javascript

    let item = document.createElement("li");
    item.textContent = 9;
    item.className = "container";

    let text = "kleiner Text im Schnee...";
    let para_1 = document.createElement("p");
    let para_2 = document.createElement("p");
    let para_3 = document.createElement("p");
    para_1.textContent = text;
    para_2.textContent = text + " langweilt sich...";
    para_3.textContent = text + " und friert ...";

    item.prepend("Unterpunkt:" + para_1);
    item.append(para_2, para_3, text);

Mehrere Objekte als Kind-Knoten des Eltern-Knotens platzieren
-------------------------------------------------------------
Erlaubt es, direkt um ein Objekt *herum* zu arbeiten.

Über ``[target_element].before(1+ elem/string)`` und
``[target_element].after(1+ elem/string)`` lassen sich Element oder Strings
(abermals **keine DOM-Strings** erlaubt) auf der gleichen Ebene vor und nach
einem *target_element* platzieren.

* ``[target_element].before(1+ elem/string)``: add elements to the same level **before** this element
* ``[target_element].after(1+ elem/string)``: add elements to the same level **after** this element

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");
    let targetElement = document.createElement("li");
    let item_1 = document.createElement("li");
    let item_2 = document.createElement("li");
    let item_3 = document.createElement("li");

    targetElement.textContent = 11;
    item_1.textContent = 10;
    item_2.textContent = 12;
    item_3.textContent = 13;

    // zuerst targetElement im DOM platzieren
    // danach um das Element herum arbeiten

    unorderedList.append(targetElement);
    targetElement.before(item_1);
    targetElement.after(item_2, "Kleiner Text im Schnee...", item_3);

Objekte als Fragment platzieren
-------------------------------
Über ``document.createDocumentFragment()`` lässt sich ein leerer DOM Baum erzeugen,
in welche Knoten und Strings hinzufügen lassen und anschließend in die DOM anhängen.
In das Fragment lassen sich abermals Elemente oder Strings (keine DOM-Strings)
einfügen.

.. code-block:: javascript

    const unorderedList = document.querySelector("ul");
    let item_1 = document.createElement("li");
    let item_2 = document.createElement("li");
    let item_3 = document.createElement("li");
    let item_4 = document.createElement("li");

    item_1.textContent = 555;
    item_2.textContent = 666;
    item_3.textContent = 777;
    item_4.textContent = 888;

    let fragment = document.createDocumentFragment();
    fragment.append(item_1, "Kleiner Text...", item_2, item_3, item_4);
    unorderedList.append(fragment);

Text-Knoten erzeugen
--------------------
Über ``document.createTextNode(string)`` lässt sich ein Text-Knoten erstellen.

.. code-block:: javascript

    // Text Knoten erstellen
    let textNode = document.createTextNode("Text im Schneeregen");
    unorderedList.before(textNode);

Wird als

.. code-block:: html

    Text im Schneeregen

in HTML eingebunden (keine Tags).

Kommentar-Knoten erzeugen
-------------------------
Über ``document.createComment(comment_string)`` lässt sich ein Kommentar-Knoten
erzeugen.

.. code-block:: javascript

    // Kommentar erzeugen
    let newComment = document.createComment("Liste zu Testzwecken");
    unorderedList.before(newComment);

Der Kommentar wird als

.. code-block:: html

    <!--Liste zu Testzwecken-->

im HTML eingebunden.
