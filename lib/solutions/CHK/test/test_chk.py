import checkout_solution as chk
import pytest

def test_basket_1():
    assert chk.checkout('ABCD') == 115

def test_basket_2():
    assert chk.checkout('AAABCD') == 195

def test_basket_3():
    assert chk.checkout('ABCDF') == -1