import CHK.checkout_solution as chk
import pytest

def test_basket():
    assert chk.checkout('ABCD') == 115
