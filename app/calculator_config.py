import os
from dotenv import load_dotenv


class ConfigManager:

    def __init__(self):

        # Load .env only if running normally (not in pytest)
        if not os.getenv("PYTEST_CURRENT_TEST"): # pragma: no cover
            load_dotenv()

        self.history_file = os.getenv("HISTORY_FILE")

        if not self.history_file:
            raise ValueError("HISTORY_FILE not set")

        auto = os.getenv("AUTO_SAVE", "true")

        self.auto_save = auto.lower() == "true"