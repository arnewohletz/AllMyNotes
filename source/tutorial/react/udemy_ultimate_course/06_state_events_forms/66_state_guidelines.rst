State Guidelines
================
* Each component instance manages its own state independently, regardless of how
  many instances exist on a page
* the current UI is a representation of all currents states of each component
  (the UI is a **reflection of data changing over time**)

Practical guidelines:

* Use a state variable for any data that the component should keep track of over time.
  This is data that will change at some point (anything but constants)
* Whenever you want something in a component to be **dynamic**, create a piece of
  state related to that "thing", and update the state when that "thing" should change
* If you want to change the way a component looks, or the data it displays,
  **update its state**. This usually happens in an **event handler** function
* When creating a component, image its view **as a reflection of state changing over time**
* For data that should not trigger a component re-render, **don't use state**. Those
  are unnecessary re-renders, which may cause performance problems or other issues.
  Use ``const`` variables for this.