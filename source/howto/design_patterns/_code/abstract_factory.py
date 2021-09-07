from abc import ABC


class Chair(ABC):

    def has_legs(self):
        pass

    def sit_on(self):
        pass


class VictorianChair(Chair):

    def has_legs(self):
        return True

    def sit_on(self):
        return False


class ModernChair(Chair):

    def has_legs(self):
        return False

    def sit_one(self):
        return True

# Equal interfaces and concretes for other furniture types like Sofa or
# CoffeeTable
# ...


class FurnitureFactory(ABC):

    def create_chair(self):
        pass

    def create_coffee_table(self):
        pass

    def create_sofa(self):
        pass


class VictorianFurnitureFactory(FurnitureFactory):

    def create_chair(self):
        return VictorianChair()

    def create_coffee_table(self):
        # Should return proper object
        pass

    def create_sofa(self):
        # Should return proper object
        pass


class ModernFurnitureFactory(FurnitureFactory):

    def create_chair(self):
        return ModernChair()

    def create_coffee_table(self):
        # Should return proper object
        pass

    def create_sofa(self):
        # Should return proper object
        pass
