import pytest
from app.calculator_repl import Calculator


def test_calculate_add(monkeypatch):

    monkeypatch.setenv("HISTORY_FILE", "test.csv")
    monkeypatch.setenv("AUTO_SAVE", "false")

    c = Calculator()

    result = c.calculate(2, "add", 3)

    assert result == 5


def test_undo_redo(monkeypatch):

    monkeypatch.setenv("HISTORY_FILE", "test.csv")
    monkeypatch.setenv("AUTO_SAVE", "false")

    c = Calculator()

    c.calculate(2, "add", 3)
    c.calculate(3, "add", 4)

    assert c.undo() is True
    assert c.redo() is True


def test_clear(monkeypatch):

    monkeypatch.setenv("HISTORY_FILE", "test.csv")
    monkeypatch.setenv("AUTO_SAVE", "false")

    c = Calculator()

    c.calculate(1, "add", 1)
    c.clear()

    assert len(c.history.get_all()) == 0