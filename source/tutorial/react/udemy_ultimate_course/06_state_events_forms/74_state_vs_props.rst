State vs Props
==============
State

    * is **internal** data, owned by component
    * components memory (across re-renders)
    * can be updated by component itself
    * update state causes re-render
    * used to make components interactive

Props

    * is **external** data, owned by parent component
    * similar to function parameters (parent passes data to children)
    * read-only (for receiving components)
    * **receival of new props causes component re-render** (e.g. parent passes
      state variable as prop to child and is updated in parent component) to stay
      in sync with parent's data
    * used by parent to configure child components ("settings")
