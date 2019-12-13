import pytest

from main.functional_recursion_solution.main import search_for_treasure


def test_right_functional():
    assert search_for_treasure([[55, 14, 25, 52, 21],
                                [44, 31, 11, 53, 43],
                                [24, 13, 45, 12, 34],
                                [42, 22, 43, 32, 41],
                                [51, 23, 33, 54, 15]]) == '11 55 15 21 44 32 13 25 43'


def test_wrong_recursive():
    assert search_for_treasure([[55, 14, 25, 52, 21],
                                [44, 31, 11, 53, 43],
                                [24, 13, 45, 12, 34],
                                [42, 22, 43, 32, 41],
                                [51, 23, 33, 54, 11]]) == 'The map has no solution'
