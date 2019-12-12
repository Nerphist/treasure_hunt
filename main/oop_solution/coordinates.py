class Coordinates:

    def __init__(self, xy: int):
        self._x = int(xy / 10) - 1
        self._y = xy % 10 - 1
        self._xy = xy

    # properties for x and y to allow getting values but forbid resetting init values
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def coordinates(self):
        return self._xy

    def __eq__(self, other):
        # equality operator to be used only with other Coordinates objects
        try:
            return self._xy == other.coordinates
        except AttributeError:
            raise TypeError("Unsupported operand type")

