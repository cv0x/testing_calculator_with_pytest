import pytest
from calculator import calculator


def test_add():
    assert calculator.add(1, 2) == 3
    assert calculator.add(-1, 1) == 0
    assert calculator.add(-1, -1) == -2
    assert calculator.add(0.01, -0.005) == 0.005
    assert calculator.add("a", "b") == "ab"



def test_subtract():
    assert calculator.subtract(2, 1) == 1
    assert calculator.subtract(2, 2) == 0
    assert calculator.subtract(2, 3) == -1



def test_multiply():
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-1, 1) == -1
    assert calculator.multiply(0, 100) == 0



def test_divide():
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-6, -3) == 2
    assert calculator.divide(-6, 3) == -2


    with pytest.raises(ValueError):
        calculator.divide(1, 0)
        calculator.divide(100, 0)
        calculator.divide(-100, 0)
        calculator.divide(0, 0)
