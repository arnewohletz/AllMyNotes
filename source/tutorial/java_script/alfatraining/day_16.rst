Ternärer / conditional Operator
===============================
Alternative zu kurzen if-else Anweisungen.

.. code-block:: none

    optional assignment = (expression) ? if expression true : if expression false

.. code-block:: javascript

    // Problem hier: taxRate kann keine Konstante sein
    let cat = "books", taxRate;

    if (cat == "books") taxRate = 1.07;
    else taxRate = 1.19;

    // Lösung
    const TAX_RATE = (cat == "books") ? 1.07 : 1.19
    console.log(TAX_RATE);

    // Andere Beispiele
    let age = 18, userAge = 33;
    console.log((userAge >= age) ? "verkauft" : "zu jung");

    let gender = 1;  // Mann = 0, Frau = 1
    console.log(`Hallo ${gender ? "Frau" : "Herr"} Jones`);

    // Mehrere Variablen gleichzeitig ändern
    let jessyPromille = 5.52, panic = false;
    (jessyPromille > 4.5)
        ? (panic = true, jessyPromille = 2.5)
        : (panic = false, jessyPromille = 6.5)
    console.log(jessyPromille, panic);

    // Mehrere Bedingungen
    let hero = "Daredevil";
    console.log(
        (hero == "Luke") ? "Cool"
        : (hero == "Daredevil") ? "OK"
        : (hero == "Jessy") ? "Einfach Jessy"
        : "Keine Ahnung"
    )

    // Variablen neuen Wert zuweisen, wenn nicht vorhanden
    let myVar;
    myVar = (myVar) ? myVar : "Neuer Wert"

Reguläre Ausdrücke
==================
Es gibt zwei Möglichkeiten zum Erstellen einer Regex:

.. code-block:: javascript

    // über Konstruktor
    // nutzen wenn Regex erst zur Laufzeit erstellt wird
    let regExp = new RegExp("abc");

    // über Literal-Schreibweise (deutlich performanter)
    // wenn Zeichenkette feststeht und nicht zur Laufzeit erstellt werden muss
    let regExp2 = /abc/;

Methoden des RegExp Objekts
---------------------------
.. code-block:: javascript

    /*
        Methoden des RegExp-Objekts
        test()      - prüft auf Vorkommen des Zeichenmusters im String
                    - Rückgabe = boolean

        exec()      - sucht erstes Vorkommen des Musters im String
                    - Rückgabe:
                        - Fund
                        - index-Position des Fundes
                        - durchsuchter String

        toString()  - gibt Zeichenmuster als String zurück
    */

    let myString = "Jessica und Luke sind Helden des Marvel-Universums";
    let regExp3 = /essi/, regExp4 = /uce/;
    console.log(regExp3.test(myString));  // true
    console.log(regExp4.test(myString));  // false

Methoden vom Datentyp String für die Arbeit mit RegExp
------------------------------------------------------
.. code-block:: javascript

    /*
        Methoden vom Datentyp String für die Arbeit mit RegExp
        (Methoden gelten auch für reguläre Strings)

        replace()       - ersetzt Vorkommen eines Zeichenmusters im String mit Teilstring

        search()        - sucht Vorkommen eines Zeichenmusters im String
                        - Rückgabe
                            - Index-Position des ersten Fundes
                            - Ohne Fund: -1

        match()         - sucht Vorkommen eines Zeichenmusters im String
                        - Rückgabe: alle Funde als Array
    */

    let desc = "Entdecke Sie bei Eduscho neben Kaffee und Reisen auch " +
    "Toilettenpapier, Öl und Mehl, Eduscho - den lob ich mir!";
    let oldBrand = /Eduscho/g;      // g --> alle Vorkommen werden ersetzt
    let newBrand = "Tchibo";

    /*
        [string].replace(zeichenmuster, ersetzung)
        arbeitet mit Strings und RegEx
        ersetzt 1. Vorkommen und bricht ab
        mit global flag (g) hinter RegExp alle Vorkommen ersetzen
    */
    console.log(desc.replace(oldBrand, newBrand));

    /*
        [string].replaceAll(zeichenmuster, ersetzung)
        bei Arbeit mit String-Übergabe werden alle Vorkommen ersetzt
        bei Übergabe einer RegExp muss flag 'g' gesetzt sein
    */
    console.log(desc.replaceAll("Eduscho", "Tchibo"));
    console.log(desc.replaceAll(oldBrand, newBrand));

    /*
        [string].search(zeichenmuster)
        kann auch mit Strings arbeiten - werden in RegExp umgewandelt
        liefert index-position des 1. Fundes
        ohne Fund Rückgabe -1
    */
    console.log(desc.search(oldBrand)); // 17
    console.log(desc.search("Kaffee")); // 31
    console.log(desc.search("Tee")); // -1
    console.log(desc.search("Tchibo")); // -1

    /*
        [string].match(zeichenmuster)
        kann auch mit Strings arbeiten - werden in RegExp umgewandelt
        nach 1. Fund Abbruch - mit global flag Ermittlung aller Funde
        Rückgabe = Fund als Array
        ohne Fund - Rückgabe null
    */

    console.log(desc.match("Eduscho"));
    console.log(desc.match(/Eduscho/));
    console.log(desc.match(/Eduscho/g));   // alle Matches

    // Bei einem Fund kann über .index die Indexposition ausgelesen werden
    // geht nicht bei mehreren Funden (global-flag)
    console.log(desc.match(/Eduscho/).index);   // 17

Definition eines Musters
------------------------
.. code-block:: javascript

    /*
        Definition eines Musters

        Ausdruck        Bedeutung

        u               das Zeichen "u"
        essi            die Zeichenfolge "essi"
        .               beliebiges Zeichen (kein Zeilenumbruch)
        a|b             das Zeichen "a" oder "b"
    */

    let regExp = /J.../;
    console.log(regExp.test("Jessi"));  // true
    console.log(regExp.test("Jo"));  // false

    /*
        Zeichenklasse

        einfache Klasse     [xyz]       "x" || "y" || "z"
        Negation            [^xyz]      "kein "x", "y" oder "z"
        Bereich             [a-zA-Z]    alle Zeichen im Bereich a-z und A-Z
    */

    let regExp2 = /[0-9][0-9][0-9]/;
    console.log(regExp2.test("Jessica"));   // false
    console.log(regExp2.test("Jessica4567"));   // true
    console.log(regExp2.test("1234567890"));   // true

    /*
        vordefinierte Zeichenklassen

        \w      Wortzeichen         => ersetzt [a-zA-Z]
        \W      kein Wortzeichen
        \s      Leerzeichen
        \S      kein Leerzeichen
        \d      Ziffer 0-9          => ersetzt [0-9]
        \D      keine Ziffer
    */

    let regExp3 = /[A-Z]\w\w\w\w\w\w\s[A-Z]\w\w/
    console.log(regExp3.test("Luke Cage"));      // false
    console.log(regExp3.test("Jessica Jones"));      // true

    /*
        Position / Begrenzung

        ^       Anfang einer Zeichenkette (Muster muss am Anfang der Zeichenkette stehen)
        $       Ende einer Zeichenkette (Muster muss am Ende der Zeichenkette stehen)
        \b      Wortgrenze (Muster muss am Anfang oder Ende eines Wortes stehen)
        \B      keine Wortgrenze (Muster muss sich innerhalb eines Wortes befinden)

        wenn Suchmuster und String komplett übereinstimmen sollen ^ und $ setzen (/^...$/)
    */

    let regExp4 = /^J/;
    console.log(regExp4.test("Luke Jones"));   // false
    console.log(regExp4.test("Jessica"));   // true
    console.log(regExp4.test("  Jessica"));   // false

    let regExp5 = /[.]png$/;  // oder /\.png$/
    console.log(regExp5.test("bild.png"));   // true
    console.log(regExp5.test("bild.png.jpg"));   // false

    let regExp6 = /^J\w\w\w\w$/
    console.log(regExp6.test("Jessi"));   // true
    console.log(regExp6.test("Jessica"));   // false
    console.log(regExp6.test("Jo"));   // false

    let regExp7 = /\bess\b/;
    console.log(regExp7.test("Jessica"));   // false
    console.log(regExp7.test("Ich ess Blumen"));   // true

    let regExp8 = /\bEs\B/;
    console.log(regExp8.test("Er Sie Es"));   // false
    console.log(regExp8.test("Essig Essenz"));   // true

    let regExp9 = /\Bess\B/;
    console.log(regExp9.test("Ich ess Blumen"));   // false
    console.log(regExp9.test("Jessica"));   // true


    /*
        Quantifizierer

        Definieren wie oft Zeichen oder Zeichenklasse im String vorkommt,
        damit er von der RegExp akzeptiert wird

        Stehen hinter Zeichen / Zeichenklasse

        ?       - kann einmal vorkommen oder nicht vorkommen
        *       - kann beliebig oft oder nicht vorkommen
        +       - muss mindestens ein Mal vorkommen
        {n}     - muss genau n Mal vorkommen
        {n,}    - muss mindestens n Mal vorkommen
        {n,z}   - muss zwischen n und z Mal vorkommen
    */

    let regExp10 = /\.jpe?g$/;
    console.log(regExp10.test("bild.jpeg"));    // true
    console.log(regExp10.test("bild.jpg"));    // true
    console.log(regExp10.test("bild.jpdg"));    // false

    let regExp11 = /abc*d/;
    console.log(regExp11.test("abc"));    // true
    console.log(regExp11.test("abcd"));    // true
    console.log(regExp11.test("abcccccccccccd"));    // true
    console.log(regExp11.test("abed"));    // false

    let regExp12 = /\s+/;
    console.log(regExp12.test("Jessica Jones"));  // true
    console.log(regExp12.test("Jessica                 Jones"));  // true
    console.log(regExp12.test("JessicaJones"));   // false


    /*
        Flags

        g       global          - alle Vorkommen ermitteln
        i       insensitive     - case-insensitive arbeiten
        m       multiline       - auf mehrere Zeilen anwenden (bei mehrzeiligem String)
    */

    let regExp13 = /^multi/m;
    console.log(regExp13.test("single\nmulti"));    // true

    /*
        [RegExp].exec()

        Rückgabe:
            - Array mit
                1. Zeichenkette, die auf RegExp passt
                2. index:   index-Position
                3. input    durchsuchter String
    */

    let desc = "Entdecke Sie bei Eduscho neben Kaffee und Reisen auch " +
    "Toilettenpapier, Öl und Mehl, Eduscho - den lob ich mir!";
    let oldBrand = /Eduscho/g;

    let output = oldBrand.exec(desc);
    console.log(output);        // nur erstes Match, trotz global flag (g)

    // zum Ermitteln aller Matches muss exec() erneut ausgeführt werden
    // durch das global-Flag (g) wird die aktuelle Position der Prüfung gemerkt

    while(output) {     // output != null
        console.log(output[0], "an index-Position", output.index);  // 17 + 84
        output = oldBrand.exec(desc);
    }

    // oder kürzer
    let newOutput;
    while (newOutput = oldBrand.exec(desc)) {
        console.log(newOutput[0], "an Index-Position", newOutput.index)
    }

    /*
        Gruppierungen

        um im Fund auf Bestandteile des Fundes, die wir als Gruppe definiert
        haben, zugreifen

        werden in () definiert

        Vorteil: können im Rückgabe-Array von exec leichter auf Gruppen zugreifen

    */

    let regExp14 = /^(\d{4})-(\d{2})-(\d{2})/;
    let date = "2024-12-10 11:52:00";

    let result = regExp14.exec(date);

    console.log(result);    // Array
    console.log(result[0]);     // 2024-12-10   --> alle Gruppen (gesamtes Match)
    console.log(result[1]);     // 2024     --> erste Gruppe
    console.log(result[2]);     // 12       --> zweite Gruppe
    console.log(result[3]);     // 10       --> dritte Gruppe
    console.log(result.index);  // 0

    console.log(`${result[3]}.${result[2]}.${result[1]}`);  // 10.12.2024

    // Keys für Gruppen-Matches definieren --> (?<key_name>expression)

    let regExp15 = /^(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;

    result = regExp15.exec(date);
    console.log(result);
    console.log(`${result.groups.year}`);   // 2024
    console.log(`${result.groups.day}.${result.groups.month}.${result.groups.year}`);
