import os

import json


class JSONHandler:
    def __init__(self, path: str):
        # path to JSON file
        self.path = path

    # must return JSON-formatted dict
    def load_data_to_dict(self) -> dict:
        read_from_file = None

        if os.path.exists(self.path):
            print("Opening phonebook...")
            with open(self.path, encoding="UTF-8") as file:
                read_from_file = json.load(file)
            print("Phonebook was successfully opened!" if (read_from_file and len(read_from_file) > 0)
                  else "JSON file is empty! Phonebook can't be open.")
        else:
            print("JSON file doesn't exist! Phonebook can't be open.")

        return read_from_file

    def save_data_to_file(self, data: dict) -> bool:
        # TODO: logging, exception

        print("Saving phonebook...")
        with open(self.path, "w", encoding="UTF-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print(f"Book was successfully saved to file {self.path}!")
        return True
