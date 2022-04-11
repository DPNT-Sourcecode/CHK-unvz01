import checkout_solution as chk
import pytest

def test_basket_1():
    assert chk.checkout('ABCD') == 115

def test_basket_2():
    assert chk.checkout('AAABCD') == 195

def test_basket_3():
    assert chk.checkout('HHHHH') == 45

def test_basket_4():
    assert chk.checkout('HHHHHHHHHH') == 80

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

def test_basket_13():
    assert chk.checkout('KK') == 150

def test_basket_14():
    assert chk.checkout('NNNM') == 120

def test_basket_15():
    assert chk.checkout('PPPPP') == 200

def test_basket_16():   
    assert chk.checkout('QQQ') == 80

def test_basket_17():   
    assert chk.checkout('UUU') == 120

def test_basket_18():   
    assert chk.checkout('VV') == 90

def test_basket_19():   
    assert chk.checkout('VVV') == 130
  
def test_basket_20():   
    assert chk.checkout('HHHHHHHHHHHHHHH') == 125

def test_basket_21():   
    assert chk.checkout('HHHHHHHHHHHHHHHH') == 135

def test_basket_22():   
    assert chk.checkout('VVVV') == 180

def test_basket_23():   
    assert chk.checkout('VVVVVV') == 260


def test_basket_23():
    assert chk.checkout('SS') == 40

def test_basket_23():
    assert chk.checkout('SSS') == 45

def test_basket_24():
    assert chk.checkout('SSS') == 45

def test_basket_25():
    assert chk.checkout('SSSS') == 65

def test_basket_26():
    assert chk.checkout('SSSSSSX') == 107