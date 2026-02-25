import os
from dotenv import load_dotenv


class ConfigManager:

    def __init__(self):
        load_dotenv()

        self.history_file = os.getenv("HISTORY_FILE")
        self.auto_save = os.getenv("AUTO_SAVE", "true").lower() == "true"

        if not self.history_file:
            raise ValueError("HISTORY_FILE not set in .env")