import os
from app.history import HistoryManager


def test_add_and_get():
    h = HistoryManager()
    h.add(2, "add", 3, 5)

    df = h.get_all()

    assert len(df) == 1
    assert df.iloc[0]["result"] == 5


def test_clear():
    h = HistoryManager()
    h.add(1, "add", 1, 2)

    h.clear()

    assert len(h.get_all()) == 0


def test_save_and_load(tmp_path):

    file = tmp_path / "test.csv"

    h = HistoryManager()
    h.add(2, "multiply", 3, 6)

    h.save(file)

    h2 = HistoryManager()
    h2.load(file)

    df = h2.get_all()

    assert len(df) == 1
    assert df.iloc[0]["result"] == 6