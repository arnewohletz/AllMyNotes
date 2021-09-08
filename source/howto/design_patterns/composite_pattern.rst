Composite Pattern
-----------------

COPIED FROM EVERNOTE

Issue:
* Be able to treat a collection of objects with whole-part relationships uniformly
* Whole-part relationship means having a top level component, that contains composite objects (component object holding other components) and leaf objects (component object that contain no other components)
* On any composite and any leaf object I can call the same methods (i.e. print()) -> the composite objects display by telling their components to call print() and the leaf objects will call print on themselves
* Each composite or leaf object must implement the same component interface
* Not every method makes sense for every object implementing the component interface -> those can be ignored by returning null or false or throw an exception the client needs to handle (i.e. ignoring by offering an empty catch block)
* From the client side there is no difference between a composite object or a leaf object within the tree structure

Application:
* Often applied in GUIs