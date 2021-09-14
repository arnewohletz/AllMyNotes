from abc import ABC, abstractmethod


class GateState(ABC):

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def pay_ok(self):
        pass

    @abstractmethod
    def pay_failed(self):
        pass


class Gate:

    def __init__(self):
        # initial state cannot be dependency injected, since the State requires
        # an instance of the Gate upon instantiation, therefore no arguments
        # for the __init__() method, but state is set within the method
        self._state = ClosedGateState(self)

    def enter(self):
        self._state.enter()

    def pay(self):
        self._state.pay()

    def pay_ok(self):
        self._state.pay_ok()

    def pay_failed(self):
        self._state.pay_failed()

    def change_state(self, new_state: GateState):
        self._state = new_state


class OpenGateState(GateState):

    def __init__(self, gate: Gate):
        self._gate = gate

    def enter(self):
        print("User entering. Closing gate ... ")
        self._gate.change_state(ClosedGateState(self._gate))

    # here: return None.
    # in case the Gate is supposed to be handled as closed for mutation
    # a new instance of OpenGateState must be returned
    def pay(self):
        print("Ignoring unexpected card swipe. Keeping gate open ...")

    def pay_ok(self):
        print("Gate already open. Ignore Payment OK ...")

    def pay_failed(self):
        print("Payment failed. Keep gates open ... ")


class ClosedGateState(GateState):

    def __init__(self, gate: Gate):
        self._gate = gate

    def enter(self):
        print("Cannot enter before payment. Keeping gate closed ...")

    def pay(self):
        print("Received card swipe. Process payment ...")
        self._gate.change_state(ProcessingPaymentGateState(self._gate))

    def pay_ok(self):
        print("Invalid payment OK received (probably error). Keeping gate "
              "closed ...")

    def pay_failed(self):
        print("Invalid payment failed received (probably error). Keeping"
              "gate closed ...")


class ProcessingPaymentGateState(GateState):

    def __init__(self, gate: Gate):
        self._gate = gate

    def enter(self):
        print("Cannot enter while processing ...")

    def pay(self):
        print("Already processing previous payment. Please wait ...")

    def pay_ok(self):
        print("Payment OK. Opening gates ...")
        self._gate.change_state(OpenGateState(self._gate))

    def pay_failed(self):
        print("Payment failed. Gates remain closed ...")
        self._gate.change_state(ClosedGateState(self._gate))


if __name__ == "__main__":

    gate = Gate()

    # try to enter without paying
    gate.enter()

    # enter after successful payment
    gate.pay()
    gate.pay_ok()
    gate.enter()

    # forbid enter due to failed payment
    gate.pay()
    gate.pay_failed()
    gate.enter()
