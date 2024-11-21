"use_strict";

const para = document.querySelector("p");

// Inline-Style setzen
para.style.color = "blue";
para.style.fontWeight = "bold";

// Inline-Styles auslesen
console.log(para.style);
console.log(para.style.color);

// Möglichkeit: Einfache Definition von Event-Handlern
// ---------------------------------------------------
// const BIGGEST   = "36px";
// const BIG       = "24px";
// const NORMAL    = "16px";
// const SMALL     = "11px";

// document.querySelector("#biggest").onclick = function() {
//     para.style.fontSize = BIGGEST;
// }
// document.querySelector("#big").onclick = function() {
//     para.style.fontSize = BIG;
// }
// document.querySelector("#normal").onclick = function() {
//     para.style.fontSize = NORMAL;
// }
// document.querySelector("#small").onclick = function() {
//     para.style.fontSize = SMALL;
// }

// Besser: Über Button-Array (keine Wiederholung)
// ----------------------------------------------
// const buttons = document.querySelectorAll("button");
// const SIZES = [36,24,16,11];
// const UNIT = "px";

// for (let i = 0; i < buttons.length; i++) {
//     // Annahme: gleiche index-Position in NodeList und Array
//     buttons[i].onclick = function() {
//         para.style.fontSize = SIZES[i] + UNIT;
//     }
// }

// Am Besten: Über Objekt
// ----------------------
const buttons = document.querySelectorAll("button");
const UNIT = "px";

const SIZES = {
    biggest: 36,
    big: 24,
    normal: 16,
    small: 12
};

for (let i = 0; i < buttons.length; i++) {
    buttons[i].onclick = function() {
        para.style.fontSize = SIZES[this.id] + UNIT;
    }
}
