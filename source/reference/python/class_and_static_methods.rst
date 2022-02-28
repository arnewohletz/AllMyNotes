Class and static methods :footcite:p:`programiz_classmethod`
============================================================
.. thebe-button:: Enable live code execution

Class methods
-------------
Method is bound to a class, not an object of a class, hence does not require the
creation of a class instance.

-> The class method works with the class since its parameter is the class itself.

Convert a method into a class method (via :python:`classmethod()`)
``````````````````````````````````````````````````````````````````
.. jupyter-execute::

    class Person:
        age = 25

        def print_age(cls):
            print('The age is: ', cls.age)

    Person.print_age = classmethod(Person.print_age)
    Person.print_age()

Use class method for 'overloading' a constructor
````````````````````````````````````````````````
Since overloading a method is not available in Python, classmethods are used to
return a class object

.. jupyter-execute::

    from datetime import date

    # random Person
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @classmethod
        def from_birth_year(cls, name, birth_year):
            return cls(name, date.today().year - birth_year)

        def display(self):
            print(self.name + "'s age is: " + str(self.age))

    person = Person('Adam', 19)
    person.display()

    person1 = Person.from_birth_year('John',  1985)
    person1.display()

Here an additional constructor was created by declaring the from_birth_year()
function a class method via the :python:`@classmethod` decorator.

Correct instance creation in inheritance
````````````````````````````````````````
When you derive a new class from a class, which contains a class method returning
a class object (cls), the correct class is instantiated, whereas a similar static
method will always return the :ulined:`hardcoded` base class object.

.. jupyter-execute::

    from datetime import date

    # random Person
    class Person:
        def __init__(self, name, age):
            self.name = name
            self.age = age

        @staticmethod
        def from_fathers_age(name, father_age, father_person_age_diff):
            return Person(name, date.today().year - father_age + father_person_age_diff)

        @classmethod
        def from_birth_year(cls, name, birth_year):
            return cls(name, date.today().year - birth_year)

        def display(self):
            print(self.name + "'s age is: " + str(self.age))

    class Man(Person):
        sex = 'Male'

    man = Man.from_birth_year('John', 1985)
    print(isinstance(man, Man))

    man1 = Man.from_fathers_age('John', 1965, 20)
    print(isinstance(man1, Man))

Here, the static method returns a 'Person' object, since the return value is
hardcoded as Person(), whereas the class method returns a Man() object, since it
was executed from within the Man class and 'cls' is defined as returning class.

| static -> hardcoded class (Person)
| class -> versatile class (cls)

Static methods
--------------
Same as class methods, static methods are bound to a class, not an object, hence
don't require the creation of an object of a class in order to use it.

-> A static method knows nothing about the class and just deals with the parameters
(cls context is missing)

Convert a method into a static method (via :python:`staticmethod()`)
````````````````````````````````````````````````````````````````````
.. jupyter-execute::

    class Mathematics:

        def add_numbers(x, y):
            return x + y

    # create addNumbers static method
    Mathematics.add_numbers = staticmethod(Mathematics.add_numbers)

    print('The sum is:', Mathematics.add_numbers(5, 10))

So far, the same as with classmethod(), except that the class method requires
the 'cls' class parameter as function parameter.

:ulined:`Static methods cannot access any properties of a class`. But when it
make sense, that a function still belongs to a class, a static method is used.

Static methods are used, if you don't want subclasses to be able to change/override
a specific implementation of a method.

.. footbibliography::