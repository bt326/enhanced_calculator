from app.calculation import OperationFactory
from app.history import HistoryManager
from app.calculator_memento import Caretaker, HistoryObserver
from app.calculator_config import ConfigManager
from app.input_validators import validate_number, validate_operation


class Calculator:
    """Facade for calculator system"""

    def __init__(self):

        self.config = ConfigManager()
        self.history = HistoryManager()
        self.caretaker = Caretaker()

        self.observer = HistoryObserver(self.history)

        try:
            self.history.load(self.config.history_file)
        except Exception:
            pass  # pragma: no cover

    def calculate(self, a, op, b):

        self.caretaker.save(self.history.get_all())

        a = validate_number(a)
        b = validate_number(b)
        op = validate_operation(op)

        operation = OperationFactory.create(op)

        result = operation.execute(a, b)

        data = {
            "a": a,
            "operation": op,
            "b": b,
            "result": result,
        }

        self.observer.update(data)

        if self.config.auto_save:
            self.history.save(self.config.history_file)

        return result