from main.oop_solution.treasuremap import TreasureMap


class Solver:

    def __init__(self, matrix):
        # solution is not being evaluated at the init with the purpose of lazy initialization
        self._solution = ''
        self._treasure_map = TreasureMap(matrix)

    @property
    def solution(self) -> str:
        if not self._solution:
            self._solution = self._get_the_path()
        return self._solution

    def _get_the_path(self) -> str:
        # receiving all needed coordinates from the generator and joining them into result string
        return ' '.join([str(i) for i in self._treasure_map.follow_the_path()])
