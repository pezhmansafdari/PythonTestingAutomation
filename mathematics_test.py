
import pytest
import mathematics


def test_add():
    assert mathematics.add(1,2) == 3
    assert mathematics.add(3, 7) == 10

def test_multiply():
    assert mathematics.multiply(5, 10) == 50

def test_power():
    assert mathematics.power(2, 8) == 256
