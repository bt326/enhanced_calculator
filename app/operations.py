from abc import ABC, abstractmethod
import math
from app.exceptions import DivisionByZeroError


class Operation(ABC):

    @abstractmethod
    def execute(self, a: float, b: float) -> float:
        pass # pragma: no cover


class Add(Operation):
    def execute(self, a, b):
        return a + b


class Subtract(Operation):
    def execute(self, a, b):
        return a - b


class Multiply(Operation):
    def execute(self, a, b):
        return a * b


class Divide(Operation):
    def execute(self, a, b):
        if b == 0: # pragma: no cover
            raise DivisionByZeroError("Cannot divide by zero.")
        return a / b


class Power(Operation):
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    def execute(self, a, b):
        if b == 0:
            raise DivisionByZeroError("Root degree cannot be zero.")
        return math.pow(a, 1 / b)  # pragma: no cover