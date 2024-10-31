import pytest
from calculator import calculator


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-1, 1, 0),
    (-1, -1, -2),
])
def test_add(a, b, expected):
    assert calculator.add(a, b) == expected



@pytest.mark.parametrize("a, b, expected", [
    (2, 1, 1),
    (2, 2, 0),
    (2, 3, -1),
])
def test_subtract(a, b, expected):
    assert calculator.subtract(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (-1, 1, -1),
    (0, 100, 0),
])
def test_multiply(a, b, expected):
    assert calculator.multiply(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (-6, -3, 2),
    (-6, 3, -2),
])
def test_divide(a, b, expected):
    assert calculator.divide(a, b) == expected



def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator.divide(1, 0)



@pytest.mark.parametrize("a, b", [
    (1, 0),
    (-100, 0),
    (0, 0),
])
def test_divide_by_zero(a, b):
    with pytest.raises(ValueError):
        calculator.divide(a, b)