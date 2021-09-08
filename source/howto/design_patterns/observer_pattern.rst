Observer Pattern
----------------

COPIED FROM EVERNOTE

Issue:
* An object (Observers) needs to know. when a different objects (Subject) changes its state
* The observers expects the subject to push any changes to it
* When observer objects need to ask the subject individually for changes, there will be a lot of queries (Polling)

Solution:
* The subject pushes change information to the subscribers
* One-To-Many relationship

<img1>

* the Observable registers all Oberservers
* when notifyObservers is called, the Observable calls the update() method on all Observers

<img2>

* the ConcreteObservable (here: WeatherStation) can have additional method that provide Observers with specific data
* the update() method takes no arguments