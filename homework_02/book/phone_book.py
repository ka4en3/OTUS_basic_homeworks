from homework_02.resources.strings import *


class PhoneBook:
    def __init__(self):
        self.__book = []
        self.__ids = set()

    def add_to_book(self, contact: Contact) -> bool:
        self.__book.append(contact)
        self.__ids.add(contact.id)
        return True

    def get_book_as_dict(self) -> dict:
        # use dict comprehension
        return {contact.id: {
            FIELDS_MAP["FIELD_NAME"]: contact.name,
            FIELDS_MAP["FIELD_PHONE"]: contact.phone,
            FIELDS_MAP["FIELD_COMMENT"]: contact.comment
        } for contact in self.__book}

    def is_empty(self) -> bool:
        return len(self.__book) == 0

    def get_max_id(self) -> int:
        return int(max(self.__ids))
