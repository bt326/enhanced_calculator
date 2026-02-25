from app.calculator_memento import Caretaker


def test_undo_redo():

    c = Caretaker()

    state1 = "one"
    state2 = "two"

    c.save(state1)
    c.save(state2)

    assert c.undo() == state2
    assert c.undo() == state1
    assert c.undo() is None

    assert c.redo() == state1
    assert c.redo() == state2
    assert c.redo() is None