class Observer:
    """Observer Interface"""

    def update(self, data):
        pass  # pragma: no cover


class HistoryObserver(Observer):
    """Observer for saving history"""

    def __init__(self, history_manager):
        self.history = history_manager

    def update(self, data):
        self.history.add(
            data["a"],
            data["operation"],
            data["b"],
            data["result"],
        )

class CalculatorMemento:
    """Stores calculator state"""

    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Caretaker:
    """Manages undo/redo"""

    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save(self, state):
        self.undo_stack.append(CalculatorMemento(state))
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return None

        memento = self.undo_stack.pop()
        self.redo_stack.append(memento)
        return memento.get_state()

    def redo(self):
        if not self.redo_stack:
            return None

        memento = self.redo_stack.pop()
        self.undo_stack.append(memento)
        return memento.get_state()