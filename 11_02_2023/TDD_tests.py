# import functions

from functions import *

# print(multiply(5, 7))

def test_multiply():
    assert multiply(5, 10) == 50
    assert multiply(100, 1.1) == 110
    assert multiply(1.5, 1.5) == 2.25
    assert multiply(0.0000001, 100) == 0.00001
    assert multiply('mama', 3) == 'mamamamamama'
    assert multiply(None, 5) == None

def test_no_of_letter():
    assert no_of_letter('mama') == 4
    assert no_of_letter('mama.tata')