import pytest
from app.calculation import OperationFactory
from app.exceptions import InvalidOperationError
from app.operations import Add, Divide


def test_factory_add():
    op = OperationFactory.create("add")
    assert isinstance(op, Add)


def test_factory_divide():
    op = OperationFactory.create("divide")
    assert isinstance(op, Divide)


def test_factory_invalid():
    with pytest.raises(InvalidOperationError):
        OperationFactory.create("invalid")