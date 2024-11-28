import os
import json
import logging

logging.basicConfig(level=logging.WARNING)


class JSONHandler:
    def __init__(self, path: str):
        self.path = path

    def load_data_to_dict(self) -> dict:
        """Loads data from a JSON file and returns it as a dictionary."""
        try:
            if os.path.exists(self.path):
                logging.info("Opening phonebook...")
                with open(self.path, encoding="UTF-8") as file:
                    data = json.load(file)
                logging.info("Phonebook successfully opened!" if (
                            data and len(data) > 0) else "JSON file is empty! Phonebook can't be open.")
                return data or {}
            else:
                logging.warning("JSON file doesn't exist! Phonebook can't be open.")
                return {}
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logging.error(f"Error loading JSON: {e}")
            return {}

    def save_data_to_file(self, data: dict) -> bool:
        """Saves data to a JSON file."""
        try:
            logging.info("Saving phonebook to JSON file...")
            with open(self.path, "w", encoding="UTF-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            logging.info(f"Book successfully saved to file {self.path}!")
            return True
        except Exception as e:
            logging.error(f"Error saving JSON: {e}")
            return False
