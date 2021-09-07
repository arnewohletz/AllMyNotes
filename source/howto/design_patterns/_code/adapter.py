from abc import ABC


class Adaptee:

    def specific_request(self):
        print("Doing my special thing ...")


class Target(ABC):

    def request(self):
        pass


class Adapter(Target):

    def __init__(self, adaptee: Adaptee):
        self.adaptee = adaptee

    def request(self):
        self.adaptee.specific_request()


if __name__ == "__main__":

    # I am the Client

    target = Adapter(Adaptee())
    target.request()
