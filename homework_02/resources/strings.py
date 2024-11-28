from dataclasses import fields

from homework_02.book.contact import Contact

JSON_FILENAME = "json/users_short.json"

# divider for printing
DIVIDER = "-" * 50

MENU = ("Open phonebook",
        "Save phonebook",
        "Show contacts",
        "New contact",
        "Find contact",
        "Edit contact",
        "Delete contact",
        "Close and exit"
        )

# define FIELDS according to the field names of dataclass Contact
FIELDS_MAP = {f"FIELD_{field.name.upper()}": field.name.lower() for field in fields(Contact)}

STR_INCORRECT_INPUT = "Incorrect input!"
STR_NOT_OPENED = "Phonebook is empty or not opened!"
STR_WRONG = "Something went wrong. Try again."
STR_ABORTED = "Aborted."
STR_ALREADY_OPENED = "Phonebook is already opened! Do you want to overwrite? y/n "
STR_CONTACT_NOT_FOUND = "Contact was not found!"
STR_CONTACT_ADDED = "Contact with ID {new_id} was successfully added."
STR_INPUT_TO_EDIT = "Please enter ID of contact to edit: "
STR_CONTACT_EDITED = "Contact with ID {edit_id} was successfully edited."
STR_INPUT_TO_FIND = "Please enter Name, Phone or Company to find: "
STR_FOUND_CONTACTS = "Found contacts:"
STR_INPUT_TO_DELETE = "Please enter ID of contact to delete: "
STR_CONTACT_DELETED = "Contact with ID {delete_id} was deleted."
STR_OPENING = "Opening phonebook..."
STR_SAVING = "Saving phonebook to JSON file..."
STR_SAVED = "Book was successfully saved to JSON file."
STR_SAVING_ERROR = "Error happened or phonebook was not opened!"