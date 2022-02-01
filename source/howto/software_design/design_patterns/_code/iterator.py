from abc import ABC, abstractmethod


class Item(ABC):
    name = None


class Sword(Item):

    def __init__(self):
        self.name = "Sword"


class Shield(Item):

    def __init__(self):
        self.name = "Shield"


# Iterator
class InventoryIterator(ABC):

    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def next(self) -> None:
        pass

    @abstractmethod
    def current(self) -> Item:
        pass


# Iterable
class Inventory(ABC):

    @abstractmethod
    def get_iterator(self) -> InventoryIterator:
        pass


# ConcreteIterable 1
class HandHeldInventory(Inventory):

    def __init__(self, right: Item, left: Item):
        self._right = right
        self._left = left

    def get_iterator(self) -> InventoryIterator:
        return HandHeldInventoryIterator(self)

    @property
    def right(self) -> Item:
        return self._right

    @right.setter
    def right(self, item: Item) -> None:
        self._right = item

    @property
    def left(self) -> Item:
        return self._left

    @left.setter
    def left(self, item: Item) -> None:
        self._left = item


# ConcreteIterable 2
class BackPackInventory(Inventory):

    def get_iterator(self) -> InventoryIterator:
        pass

    # implementation ...

    # backpack can contain much more items than HandHeldInventory,
    # so handling both via Iterator Pattern makes sense, even though
    # HandHeldInventory can only hold two items


# ConcreteIterator 1
class HandHeldInventoryIterator(InventoryIterator):

    # iterate oder: -> right -> left

    def __init__(self, inventory: HandHeldInventory):
        self.inventory = inventory
        self.index = 0

    def next(self) -> None:
        self.index += 1

    def current(self) -> Item:
        if self.index == 0:
            return self.inventory.right
        if self.index == 1:
            return self.inventory.left
        else:
            IndexError(f"HandHeldInventory cannot have index of {self.index}")

    def is_done(self) -> bool:
        return self.index > 1


if __name__ == "__main__":

    sword = Sword()
    shield = Shield()
    inventory = HandHeldInventory(right=sword, left=shield)
    iterator = inventory.get_iterator()

    while not iterator.is_done():
        print(iterator.current().name)
        # do other cool stuff with current item
        iterator.next()
