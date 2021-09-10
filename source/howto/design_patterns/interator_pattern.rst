Iterator Pattern
----------------
Issue
`````
* I want to iterate through a collection, but I don't want to care about its structure
* Known iterable types are not sufficient or I don't know about the structure, just need a way to get
  all elements from the structure
* The structure must not be of any known iterator type (e.g. list), but can be anything I want
* Trying to reshape the data of differently structured classes to become compatible with
  each other might be difficult to achieve and the logic to get to this format will be
  different for each structure

Solution
````````
* Uniform way to iterate over various collections of items, which derive from the same
  interface, but vary in its structure
* The iterate method is not returning all elements as flattened list at once, but returns
  item after item with each time the iterate method is called
* That way the collection does not expose it's structure
* Lazy Evaluation: By return only the next item, a result can be immediately checked and stopped
  if wanted item is returned. This allows infinite collections




.. admonition:: Single Responsibility Principle
    :class: design_principle

    **A class should have only one reason to change**



https://refactoring.guru/design-patterns/iterator/python/example