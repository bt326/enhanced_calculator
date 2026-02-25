from app.operations import Add, Subtract, Multiply, Divide, Power, Root
from app.exceptions import InvalidOperationError


class OperationFactory:

    @staticmethod
    def create(operation_name: str):

        operations = {
            "add": Add(),
            "subtract": Subtract(),
            "multiply": Multiply(),
            "divide": Divide(),
            "power": Power(),
            "root": Root(),
        }

        if operation_name not in operations:
            raise InvalidOperationError(f"Invalid operation: {operation_name}")

        return operations[operation_name]