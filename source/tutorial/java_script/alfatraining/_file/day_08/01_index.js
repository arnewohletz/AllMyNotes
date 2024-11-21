"use_strict";

/*
    wenn Eingabe getan wird, sollen matches gehilighted werden
*/

const heroItems = document.querySelectorAll("#helden li");

// const SEARCH_STR = "one";

// for (let i = 0; i < heroItems.length; i++) {
//     let item = heroItems[i];
//     if (item.textContent.includes(SEARCH_STR)) {
//         item.className = "found";
//     }
// }

const searchField = document.querySelector("#heldenSuche input");

function checkHeroList() {
    const SEARCH_STR = searchField.value.trim().toLowerCase();
    for (let i = 0; i < heroItems.length; i++) {
        let item = heroItems[i];
        if (SEARCH_STR && item.textContent.toLowerCase().includes(SEARCH_STR)) {
            item.className = "found";
        } else {
            item.className = "";
        }
    }
}

searchField.oninput = checkHeroList;