import json
import os
from config import HISTORY_FILE


class HistoryLogger:
    """
    Saves and loads conversation history.
    """

    def save_history(self, profile, conversation):
        history = {
            "profile": profile,
            "conversation": conversation
        }

        os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump(history, file, indent=4)

    def load_history(self):
        if not os.path.exists(HISTORY_FILE):
            return None

        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            return json.load(file)