#write a test for def quersumme(zahl) in src/quersum.py

import pytest
from quersum import quersum

def test_quersum():
    assert quersum(123) == 6
    assert quersum(0) == 0
    assert quersum(1) == 1
    assert quersum(10) == 1
    assert quersum(123456789) == 45
    assert quersum(-123) == 6
    assert quersum(-1) == 1
    assert quersum(-10) == 1
    assert quersum(-123456789) == 45
    assert quersum(-0) == 0
    assert quersum(100) == 1
    assert quersum(1000) == 1

