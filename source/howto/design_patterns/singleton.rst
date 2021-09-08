Singleton Pattern
-----------------

COPIED FROM EVERNOTE


* Make sure that there is only one instance of a class
* Make sure, that if a instance of a singleton class is asked for, the same instance is always given

People warn from using the Singleton Pattern:
* It forces the Singleton instance to be available from the global namespace -> Globals are supposed to be avoided, but scope variables and functions:
    * globally accessible parts could be changed from anywhere without realizing it
* Using a Singleton is an assumption: "In the future I will only need one instance of that class" - but that isn't necessarily true for growing applications -> you have to be 100% sure, but that's unlikely you can
* for testing purposes it is often required to have at least two instances:
    * the one the application actually will use
    * the one you want to mock (add unfinished behavior to it, in order to test another class using it)
* "It's fine to use only one instance of a class within the program, but it shouldn't be made impossible to prevent other instantiations of it"