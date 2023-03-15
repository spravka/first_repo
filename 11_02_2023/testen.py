from functions import *

def test_multiply():
    assert multiply(5, 10) == 50
    assert multiply(100, 1.1) == 110
    assert multiply(1.5, 1.5) == 2.25