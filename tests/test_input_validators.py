import pytest
from app.input_validators import validate_number, validate_operation


def test_validate_number_valid():
    assert validate_number("10") == 10.0
    assert validate_number("2.5") == 2.5


def test_validate_number_invalid():
    with pytest.raises(ValueError):
        validate_number("abc")


def test_validate_operation_valid():
    assert validate_operation("add") == "add"


def test_validate_operation_invalid():
    with pytest.raises(ValueError):
        validate_operation("wrong")