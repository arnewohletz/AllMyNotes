Factory Method Pattern
----------------------
Issue
`````
* At a certain point in the program, you need an object of a certain type, but you
  don't know which sub-class you actually need
* Decisions which type of object is created depends on business logic
* Multiple business logic sets might exist in parallel (e.g. create totally randomly, create
  by making sure each object type is equally often instantiated)
* The instantiation logic might be needed at different places in the code -> duplication
* If the logic changes, these changes must be done to any usage in the code -> hard to maintain

To summarize, we should use the *Factory Method Pattern* where there is logic involved in the
creation of an object and when this logic repeats itself

Solution
````````
* Object instantiation is moved into separate classes
* These classes do nothing but instantiate the proper object and return it
* These classes are called *Factory classes*
* Various amount of *Factories classes* for the same object may exist, each implementing
  a different type of business logic on which object is instantiated and returned
* Multiple factories should implement the same *Factory interface*, which thereby defines a
  blueprint for these *Factory classes*


.. mermaid::

    classDiagram
