import os
import json
import logging

logging.basicConfig(level=logging.WARNING)


class JSONHandler:
    """
    A class to handle JSON file operations such as loading and saving data.

    Attributes:
        path (str): The file path of the JSON file.

    Methods:
        load_data_to_dict() -> dict:
            Loads data from the JSON file and returns it as a dictionary. If the file
            does not exist or contains invalid JSON, it returns an empty dictionary.

        save_data_to_file(data: dict) -> bool:
            Saves a dictionary to the JSON file. Returns True if the operation
            succeeds, otherwise False.
    """

    def __init__(self, path: str):
        """
        Initializes the JSONHandler with the file path.

        Args:
            path (str): The path to the JSON file.
        """
        self.path = path

    def load_data_to_dict(self) -> dict:
        """
        Loads data from a JSON file and returns it as a dictionary.

        Returns:
            dict: The data loaded from the JSON file, or an empty dictionary if the
            file does not exist or an error occurs.
        """
        try:
            if os.path.exists(self.path):
                logging.info("Opening phonebook...")
                with open(self.path, encoding="UTF-8") as file:
                    data = json.load(file)
                logging.info(
                    "Phonebook successfully opened!"
                    if (data and len(data) > 0)
                    else "JSON file is empty! Phonebook can't be open."
                )
                return data or {}
            else:
                logging.warning("JSON file doesn't exist! Phonebook can't be open.")
                return {}
        except (FileNotFoundError) as e:
            logging.error(f"Error loading JSON: {e}")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Error loading JSON: {e}")
            raise e

    def save_data_to_file(self, data: dict) -> bool:
        """
        Saves data to a JSON file.

        Args:
            data (dict): The dictionary data to save to the JSON file.

        Returns:
            bool: True if the data was successfully saved, otherwise False.
        """
        try:
            logging.info("Saving phonebook to JSON file...")
            with open(self.path, "w", encoding="UTF-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
            logging.info(f"Book successfully saved to file {self.path}!")
            return True
        except Exception as e:
            logging.error(f"Error saving JSON: {e}")
            return False
