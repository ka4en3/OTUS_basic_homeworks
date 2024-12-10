from homework_02.book import PhoneBook
from homework_02.book import Contact
from homework_02.resources.strings import *


class Model:
    """
    The Model class handles the data and logic for the phone book application.
    It interacts with a data handler to manage the storage of contacts and provides methods to manipulate the phone book.
    """

    def __init__(self, data_handler):
        """
        Initializes the model with a data handler (e.g., file, database) and prepares the phone book instance.

        Args:
            data_handler: An object responsible for loading and saving data (e.g., JSONHandler).
        """
        # Model keeps phonebook as an instance of class PhoneBook
        self.__phonebook = None
        # Model requires data_handler on creation (file, db, ...)
        self.__data_handler = data_handler

    def open_book(self) -> PhoneBook | None:
        """
        Opens the phone book by loading data from the data handler and populating the phone book.

        Returns:
            PhoneBook: A populated PhoneBook instance if successful, or None if failed to open the book.
        """
        try:
            # every call creates a new instance of PhoneBook
            self.__phonebook = PhoneBook()
            # load data to json dict
            data = self.__data_handler.load_data_to_dict()

            for cid, contact in data.items():
                new_contact = Contact(cid)
                for key, value in contact.items():
                    key = key.strip().lower()
                    if key in FIELDS_MAP.values():
                        setattr(new_contact, key, value)

                self.__phonebook.add_to_book(new_contact)

            return self.__phonebook if self.book_is_opened() else None
        except:
            return None

    def get_book(self) -> PhoneBook:
        """
        Retrieves the current phone book.

        Returns:
            PhoneBook: The current instance of the PhoneBook.
        """
        return self.__phonebook

    def book_is_opened(self) -> bool:
        """
        Checks if the phone book is opened and not empty.

        Returns:
            bool: True if the phone book is opened and not empty, False otherwise.
        """
        return self.__phonebook and not self.__phonebook.is_empty()

    def save_book(self) -> bool:
        """
        Saves the current phone book data to the storage via the data handler.

        Returns:
            bool: True if the book was saved successfully, False otherwise.
        """
        try:
            return self.__data_handler.save_data_to_file(
                self.__phonebook.get_book_as_dict()
            )
        except:
            return False

    def add_new_contact(self, input_new_contact: dict) -> bool:
        """
        Adds a new contact to the phone book.

        Args:
            input_new_contact (dict): A dictionary of contact details.

        Returns:
            bool: The ID of the newly added contact if successful, False otherwise.
        """
        try:
            # generating next contact_id
            next_id = self.__phonebook.get_max_id() + 1
            # create new object of Contact
            new_contact = Contact(str(next_id))

            for key, value in input_new_contact.items():
                key = key.strip().lower()
                if key in FIELDS_MAP.values():
                    setattr(new_contact, key, value)

            self.__phonebook.add_to_book(new_contact)

            return next_id
        except:
            return False

    def edit_contact(self, edit_id: str, input_edit_contact: dict) -> bool:
        """
        Edits an existing contact's details in the phone book.

        Args:
            edit_id (str): The ID of the contact to edit.
            input_edit_contact (dict): A dictionary of the new contact details.

        Returns:
            bool: True if the contact was edited successfully, False otherwise.
        """
        try:
            edit_contact = self.find_contact_by_id(edit_id)
            # use generator to filter out empty inputs
            for key, value in (
                (k, v) for k, v in input_edit_contact.items() if v != ""
            ):
                key = key.strip().lower()
                if key in FIELDS_MAP.values():
                    setattr(edit_contact, key, value)
            return True
        except:
            return False

    def find_contact_by_id(self, edit_id: str) -> Contact:
        """
        Finds a contact by its ID.

        Args:
            edit_id (str): The ID of the contact to find.

        Returns:
            Contact: The contact object if found, or None if not found.
        """
        return self.__phonebook.get_contact_by_id(edit_id)

    def find_contact_by_str(self, str_to_find: str) -> list[Contact] | None:
        """
        Finds contacts that match a given search string.

        Args:
            str_to_find (str): The string to search for in contact fields.

        Returns:
            list: A list of matching contacts, or None if an error occurred.
        """
        try:
            result = []
            book = self.__phonebook.get_book()
            words_to_find = str_to_find.split(sep=" ")
            for contact in book.values():
                for field in fields(contact):
                    value = getattr(contact, field.name, None)
                    if isinstance(value, str):
                        value = value.strip().lower()
                        if any(word in value for word in words_to_find):
                            result.append(contact)
                            break
            return result
        except:
            return None

    def delete_contact(self, delete_id: str) -> bool:
        """
        Deletes a contact from the phone book.

        Args:
            delete_id (str): The ID of the contact to delete.

        Returns:
            bool: True if the contact was deleted successfully, False otherwise.
        """
        try:
            return self.__phonebook.delete_from_book(delete_id)
        except:
            return False
