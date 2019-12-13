import pytest

from main.oop_solution.solver import Solver


class TestOOP:

    def setup(self):
        self.right_solver = Solver([[55, 14, 25, 52, 21],
                                    [44, 31, 11, 53, 43],
                                    [24, 13, 45, 12, 34],
                                    [42, 22, 43, 32, 41],
                                    [51, 23, 33, 54, 15]])

        self.wrong_recursive_solver = Solver([[55, 14, 25, 52, 21],
                                              [44, 31, 11, 53, 43],
                                              [24, 13, 45, 12, 34],
                                              [42, 22, 43, 32, 41],
                                              [51, 23, 33, 54, 11]])

    def test_right(self):
        assert self.right_solver.solution == '11 55 15 21 44 32 13 25 43'

    def test_wrong_recursive(self):
        assert self.wrong_recursive_solver.solution == 'The map has no solution'
