class Beverage:

    def get_desc(self) -> str:
        pass

    def cost(self) -> int:
        pass


class Decaf(Beverage):

    def get_desc(self) -> str:
        return "Decaf"

    def cost(self) -> int:
        return 2


class Espresso(Beverage):

    def get_desc(self) -> str:
        return "Espresso"

    def cost(self) -> int:
        return 1


class AddonDecorator(Beverage):

    cost = 0

    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    def get_desc(self) -> str:
        return self._beverage.get_desc()

    def cost(self) -> int:
        pass


class CaramelDecorator(AddonDecorator):

    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def cost(self) -> int:
        return self._beverage.cost() + 2

    def get_desc(self) -> str:
        return self._beverage.get_desc() + " + Caramel"


class SoyDecorator(AddonDecorator):

    def __init__(self, beverage: Beverage):
        super().__init__(beverage)

    def cost(self) -> int:
        return self._beverage.cost() + 1

    def get_desc(self) -> str:
        return self._beverage.get_desc() + " + Soy"


if __name__ == "__main__":
    espresso = Espresso()
    espresso_with_latte = CaramelDecorator(espresso)
    print(f"{espresso_with_latte.get_desc()}: {espresso_with_latte.cost()}")
