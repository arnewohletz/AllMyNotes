from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self):
        pass


class Observable(ABC):

    @abstractmethod
    def add(self, observer: Observer):
        pass

    @abstractmethod
    def remove(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class WeatherStation(Observable):

    observers = []
    temperature = 20

    def add(self, observer: Observer):
        self.observers.append(observer)

    def remove(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def get_temperature(self):
        return self.temperature

    # add method to retrieve temperature from sensor


class PhoneDisplay(Observer):

    temperature = None

    def __init__(self, weather_station: WeatherStation):
        self.station = weather_station

    def update(self):
        self.temperature = self.station.get_temperature()

    def display(self):
        print(f"Phone Display: {self.temperature}")

    # some additional method(s) on how to display temperature


class DeskDisplay(Observer):

    temperature = None

    def __init__(self, weather_station: WeatherStation):
        self.station = weather_station

    def update(self):
        self.temperature = self.station.get_temperature()

    def display(self):
        print(f"Desk Display: {self.temperature}")

    # some additional method(s) on how to display temperature


if __name__ == "__main__":

    station = WeatherStation()
    phone_display = PhoneDisplay(station)
    desk_display = DeskDisplay(station)

    station.add(phone_display)
    station.add(desk_display)

    # initial display
    phone_display.update()
    desk_display.update()
    phone_display.display()
    desk_display.display()

    # mocking a temperature change
    station.temperature = 25
    station.notify()

    # updated display
    phone_display.display()
    desk_display.display()
