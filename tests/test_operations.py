import pytest
from app.operations import Add, Subtract, Multiply, Divide, Power, Root
from app.exceptions import DivisionByZeroError


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert Add().execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (5, 3, 2),
    (0, 4, -4),
])
def test_subtract(a, b, expected):
    assert Subtract().execute(a, b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 6),
    (4, 0, 0),
])
def test_multiply(a, b, expected):
    assert Multiply().execute(a, b) == expected


def test_divide():
    assert Divide().execute(6, 3) == 2


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        Divide().execute(5, 0)


def test_power():
    assert Power().execute(2, 3) == 8


def test_root():
    assert round(Root().execute(9, 2), 2) == 3