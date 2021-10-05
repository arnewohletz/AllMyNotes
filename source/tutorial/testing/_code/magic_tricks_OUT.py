
class Wheel:

    def __init__(self, rim, tire):
        self.rim = rim  # diameter of wheel rim
        self.tire = tire  # diameter of tire

    def diameter(self):
        return self.rim + (self.tire * 2)


class Observer:
    # e.g. writes data into the database

    def changed(self, key, value):
        # update database
        return True


class Gear:

    def __init__(self, chainring, cog, wheel, observer=Observer()):
        self.chainring = chainring  # length of chain ring
        self.cog = cog  # amount of cogs on wheel
        self.wheel = wheel  # Wheel instance
        self.observer = observer  # Observer instance

    def gear_inches(self):
        return self._ratio() * self.wheel.diameter()

    def _ratio(self):
        return self.chainring / float(self.cog)

    def set_cog(self, cog):
        self.cog = cog
        self._changed()

    def _changed(self):
        self.observer.changed(self.chainring, self.cog)
