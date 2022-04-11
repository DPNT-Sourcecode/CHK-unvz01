import checkout_solution as chk
import pytest

def test_basket_1():
    assert chk.checkout('ABCD') == 115

def test_basket_2():
    assert chk.checkout('AAABCD') == 195

def test_basket_3():
    assert chk.checkout('ABCDFGT') == -1

def test_basket_4():
    assert chk.checkout('ABCDFG') == -1

def test_basket_5():
    assert chk.checkout('AAAA') == 180

def test_basket_6():
    assert chk.checkout('AAAAA') == 200

def test_basket_7():
    assert chk.checkout('AAAAAAA') == 300

def test_basket_8():
    assert chk.checkout('AAAAAAAA') == 330

def test_basket_9():
    assert chk.checkout('EEEEBB') == 160

def test_basket_10():
    assert chk.checkout('ABCDECBAABCABBAAAEEAA') == 665

def test_basket_11():
    assert chk.checkout('FFF') == 20

def test_basket_12():
    assert chk.checkout('FFFFFF') == 40
