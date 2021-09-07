from abc import ABC, abstractmethod


# Receiver
class FancyLight:

    def turn_on(self):
        print("Switching on ...")
        return

    def turn_off(self):
        print("Switching off ...")
        return


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def unexecute(self) -> None:
        pass


# Concrete Commands
class TurnOnCommand(Command):

    def __init__(self, light: FancyLight):
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()

    def unexecute(self) -> None:
        self.light.turn_off()


class TurnOffCommand(Command):

    def __init__(self, light: FancyLight):
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()

    def unexecute(self) -> None:
        self.light.turn_on()


# Invoker
class SuperRemoteControl:
    _turn_on = None
    _turn_off = None

    _light_state = None
    _last_command = None

    def __init__(self, turn_on_command, turn_off_command):
        self._light_state = "off"
        self._turn_on = turn_on_command
        self._turn_off = turn_off_command
        self._last_command = None

    # Not needed as directly assigned in constructor (dependency injection)
    def set_turn_on(self, command: Command):
        self._turn_on = command

    # Not needed as directly assigned in constructor (dependency injection)
    def set_turn_off(self, command: Command):
        self._turn_off = command

    def press_onoff(self):
        if self._light_state == "off":
            self._turn_on.execute()
            self._light_state = "on"
            self._last_command = self._turn_on
        elif self._light_state == "on":
            self._turn_off.execute()
            self._light_state = "off"
            self._last_command = self._turn_off

    def press_undo(self):
        self._last_command.unexecute()


if __name__ == "__main__":
    light = FancyLight()
    control = SuperRemoteControl(
        turn_on_command=TurnOnCommand(light),
        turn_off_command=TurnOffCommand(light)
    )
    # Alternatively to passing commands into the constructor, they can be
    # assigned in set-methods

    # control.set_turn_on(TurnOnCommand(light))
    # control.set_turn_off(TurnOffCommand(light))
    control.press_onoff()
    control.press_onoff()
    control.press_undo()
