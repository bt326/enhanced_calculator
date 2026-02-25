import pytest
from app.exceptions import (
    CalculatorError,
    InvalidOperationError,
    DivisionByZeroError,
)


def test_calculator_error():
    err = CalculatorError("test")
    assert str(err) == "test"


def test_invalid_operation_error():
    with pytest.raises(InvalidOperationError):
        raise InvalidOperationError("invalid")


def test_division_by_zero_error():
    with pytest.raises(DivisionByZeroError):
        raise DivisionByZeroError("zero")