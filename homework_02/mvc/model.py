from homework_02.book.phone_book import PhoneBook
from homework_02.resources.strings import *


class Model:
    def __init__(self, data_handler):
        # Model keeps phonebook as an instance of class PhoneBook
        self.__phonebook = None
        # Model requires data_handler on creation (file, db, ...)
        self.__data_handler = data_handler

    def open_book(self) -> PhoneBook:
        # every call create a new instance of PhoneBook
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

    def get_book(self) -> PhoneBook:
        return self.__phonebook

    def book_is_opened(self) -> bool:
        return self.__phonebook and not self.__phonebook.is_empty()

    def save_book(self):
        self.__data_handler.save_data_to_file(self.__phonebook.get_book_as_dict())

    def add_new_contact(self, input_new_contact: dict) -> bool:
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
