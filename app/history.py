import pandas as pd
from datetime import datetime


class HistoryManager:
    """Manages calculation history using pandas."""

    def __init__(self):
        self.df = pd.DataFrame(
            columns=["timestamp", "a", "operation", "b", "result"]
        )

    def add(self, a, operation, b, result):
        new_row = {
            "timestamp": datetime.now(),
            "a": a,
            "operation": operation,
            "b": b,
            "result": result,
        }

        self.df.loc[len(self.df)] = new_row

    def clear(self):
        self.df = self.df.iloc[0:0]

    def save(self, filename="history.csv"):
        self.df.to_csv(filename, index=False)

    def load(self, filename="history.csv"):
        self.df = pd.read_csv(filename)

    def get_all(self):
        return self.df.copy()