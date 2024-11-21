"use_strict";

const STEP = 5;
const UNIT = "px";

const para = document.querySelector("p");
const small = document.querySelector("#small");
const big = document.querySelector("#big");

// Das geht nicht ...
console.log(para.style.fontSize);  // "empty string", da fontSize kein Inline-Style

// .. daher
// Über getComputedStyle(element) werden alle anliegeneden Styles eines Elements
// ausgelesen. Reine Getter-Methode, nicht sehr performant, daher sollte es sparsam
// eingesetzt werden. Bei Weiterarbeit sollte der Wert als Inline-Style an das Objekt
// angehängt werden oder im Storage gespeichert werden (um erneuten Aufruf zu vermeiden)
let paraStyleObj = getComputedStyle(para);

// 369 Styles!!! -> Browser (Hauptteil) + CSS Style + Inline (letztes am ranghöchsten)
console.log(paraStyleObj);
console.log(paraStyleObj.fontSize);  // "50px"

let storedSize = localStorage.getItem("fontSize") ?? getComputedStyle(para).fontSize;
setFontSize(parseInt(storedSize));

big.onclick = function() {
    setFontSize(getFontSize() + STEP);
};

small.onclick = function() {
    setFontSize(getFontSize() - STEP);
};

function getFontSize() {
    return parseInt(para.style.fontSize);
}

function setFontSize(size) {

    big.disabled = (size > 60);
    small.disabled = (size < 15);
    para.style.fontSize = size + UNIT;
    if (window.Storage) localStorage.setItem("fontSize", size);
}
