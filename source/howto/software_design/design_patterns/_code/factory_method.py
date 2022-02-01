from abc import ABC
from random import randrange


class Animal(ABC):

    def say_hello(self):
        pass


class Dog(Animal):

    def say_hello(self):
        print("Wuff")


class Cat(Animal):

    def say_hello(self):
        print("Miau")


class Duck(Animal):

    def say_hello(self):
        print("Quack")


class AnimalFactory(ABC):

    def create(self):
        pass


class BalancedFactory(AnimalFactory):

    def create(self):
        # Implementation:
        # create animals randomly, but make sure the same amount is instantiated
        # after three calls and re-balance
        pass


class RandomFactory(AnimalFactory):

    def create(self):
        random_number = randrange(1, 3)
        if random_number == 1:
            return Dog()
        if random_number == 2:
            return Cat()
        if random_number == 3:
            return Duck()


if __name__ == "__main__":
    factory = RandomFactory()
    animal = factory.create()
    animal.say_hello()