import sum_solutions
import pytest

def test_sum():
    test = sum_solutions.sum_solution()
    assert test.compute(1,1) == 2

def test_negative_input():
    test = sum_solutions.sum_solution()
    assert test.compute(-1,1) == False