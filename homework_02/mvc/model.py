from homework_02.book.contact import Contact
from homework_02.book.phone_book import PhoneBook


class Model:
    def __init__(self, data_handler):
        # Model keeps phonebook as an instance of class PhoneBook
        self.__phonebook = None
        # Model requires data_handler on creation (file, db, ...)
        self.__data_handler = data_handler

    '''every call create a new instance of PhoneBook'''
    def open_book(self) -> PhoneBook:
        self.__phonebook = PhoneBook()

        for cid, contact in self.__data_handler.load_data_to_dict().items():
            new_contact = Contact(cid)
            for key, value in contact.items():
                if key.strip().lower() == "name":
                    new_contact.name = value
                if key.strip().lower() == "phone":
                    new_contact.phone = value
                if key.strip().lower() == "comment":
                    new_contact.comment = value
            self.__phonebook.add_to_book(new_contact)

        if self.book_is_opened():
            return self.__phonebook

    def get_book(self) -> PhoneBook:
        return self.__phonebook

    def book_is_opened(self) -> bool:
        return self.__phonebook and not self.__phonebook.is_empty()

    def save_book(self):
        self.__data_handler.save_data_to_file(self.__phonebook.get_book_as_dict())

    def add_new_contact(self, input_new_contact: dict) -> bool:
        next_id = self.__phonebook.get_max_id + 1  # to generate next contact_id
        new_contact = Contact(next_id)
        for key, value in input_new_contact.items():
            if key.strip().lower() == "name":
                new_contact.name = value
            if key.strip().lower() == "phone":
                new_contact.phone = value
            if key.strip().lower() == "comment":
                new_contact.comment = value
        self.__phonebook.add_to_book(new_contact)
