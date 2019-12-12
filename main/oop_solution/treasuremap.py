import copy

from main.oop_solution.coordinates import Coordinates


class TreasureMap:
    # constant of beginning coordinates for better readability
    BEGINNING_COORDINATES = Coordinates(11)

    def __init__(self, matrix):
        self._current_coordinates: Coordinates = TreasureMap.BEGINNING_COORDINATES
        # copying matrix to ensure we will work with the same matrix we received
        self._matrix = copy.copy(matrix)

    def follow_the_path(self):
        while True:
            yield self._current_coordinates.coordinates
            # getting the value from the cell with current coordinates
            new_coordinates = Coordinates(self._matrix[self._current_coordinates.x][
                self._current_coordinates.y])
            # if new coordinates are not the same we assign it to current_coordinates for further exploitation
            if new_coordinates != self._current_coordinates:
                self._current_coordinates = new_coordinates
            else:
                # assigning beginning coordinate in case of one more use
                self._current_coordinates = TreasureMap.BEGINNING_COORDINATES
                break

    def __str__(self):
        return 'Treasure map:\n{}'.format('\n'.join([str(i) for i in self._matrix]))
