import pytest

from main.oop_solution.solver import Solver


class TestOOP:

    def setup(self):
        self.solver = Solver([[55, 14, 25, 52, 21],
                              [44, 31, 11, 53, 43],
                              [24, 13, 45, 12, 34],
                              [42, 22, 43, 32, 41],
                              [51, 23, 33, 54, 15]])

    def test_oop(self):
        assert self.solver.solution == '11 55 15 21 44 32 13 25 43'
