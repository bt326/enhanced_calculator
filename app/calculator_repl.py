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

    def undo(self):
        state = self.caretaker.undo()
        if state is not None:
            self.history.df = state
            return True
        return False

    def redo(self):
        state = self.caretaker.redo()
        if state is not None:
            self.history.df = state
            return True
        return False

    def clear(self):
        self.history.clear()


def print_help():  # pragma: no cover
    print("""
Commands:
  add/subtract/multiply/divide/power/root <a> <b>
  history   - Show history
  undo      - Undo last
  redo      - Redo last
  clear     - Clear history
  save      - Save history
  load      - Load history
  help      - Show help
  exit      - Exit app
""")


def start_repl():  # pragma: no cover

    calc = Calculator()

    print("Enhanced Calculator (type 'help')")

    while True:  # pragma: no cover

        try:  # pragma: no cover

            user_input = input(">>> ").strip()

            if not user_input:
                continue

            parts = user_input.split()
            command = parts[0].lower()

            if command == "exit":
                print("Bye 👋")
                break

            elif command == "help":
                print_help()

            elif command == "history":
                print(calc.history.get_all())

            elif command == "clear":
                calc.clear()
                print("History cleared")

            elif command == "undo":
                print("Undo successful" if calc.undo() else "Nothing to undo")

            elif command == "redo":
                print("Redo successful" if calc.redo() else "Nothing to redo")

            elif command == "save":
                calc.history.save(calc.config.history_file)
                print("Saved")

            elif command == "load":
                calc.history.load(calc.config.history_file)
                print("Loaded")

            else:
                if len(parts) != 3:
                    raise ValueError("Format: operation a b")

                op, a, b = parts
                result = calc.calculate(a, op, b)
                print("Result =", result)

        except Exception as e:
            print("Error:", e)


if __name__ == "__main__":  # pragma: no cover
    start_repl()