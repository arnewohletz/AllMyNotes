Separation of Concerns
======================
* Before Single-page application, HTML, CSS and JavaScript resided in **separate files**
  (one technology per file)
* With SPAs, JavaScript became the language which defines the HTML (JS defines the
  content and behavior of the HTML elements) -> logic and UI are **tightly coupled** together
* If both are tightly coupled, why not put them together? -> Components
* A component consists of **data, logic and appearance** -> HTML and JavaScript are
  **colocated** (located at the same place)

    .. figure:: _file/js_html_colocated.jpg

* In React, **one file** should contain **one component** (one component per file)
* React's idea of separation of concern: one concern = one component
