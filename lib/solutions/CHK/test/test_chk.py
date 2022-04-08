import checkout_solution as chk
import pytest

def test_basket_1():
    assert chk.checkout('ABCD') == 115

def test_basket_2():
    assert chk.checkout('AAABCD') == 195

def test_basket_3():
    assert chk.checkout('ABCDF') == -1

def test_basket_4():
    assert chk.checkout('ABCDF') == -1

def test_basket_5():
    assert chk.checkout('AAAA') == 180

def test_basket_6():
    assert chk.checkout('AAAAA') == 200

def test_basket_7():
    assert chk.checkout('AAAAAAA') == 300

def test_basket_8():
    assert chk.checkout('AAAAAAAA') == 330