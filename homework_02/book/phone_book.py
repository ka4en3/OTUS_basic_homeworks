from homework_02.resources.strings import *


class PhoneBook:
    def __init__(self):
        self.__book: dict[str, Contact] = {}
        self.__ids: set[str] = set()

    def add_to_book(self, contact: Contact) -> bool:
        if not contact:
            return False
        self.__book[contact.id] = contact
        self.__ids.add(contact.id)
        return True

    def delete_from_book(self, cid: str) -> bool:
        if self.__book.pop(cid, None):
            self.__ids.discard(cid)
            return True
        return False

    def get_book_as_dict(self) -> dict:
        # use dict comprehension
        return {contact.id: {
            FIELDS_MAP['FIELD_NAME']: contact.name,
            FIELDS_MAP['FIELD_PHONE']: contact.phone,
            FIELDS_MAP['FIELD_COMMENT']: contact.comment
        } for contact in self.__book.values()}

    def is_empty(self) -> bool:
        return len(self.__book) == 0

    def get_max_id(self) -> int:
        int_ids = [int(cid) for cid in self.__ids if cid.isdigit()]
        return max(int_ids, default=0)

    def get_contact_by_id(self, cid: str) -> Contact:
        return self.__book.get(cid)

    def get_book(self) -> dict[str, Contact]:
        # to comply with encapsulation -> provide a copy for search
        return self.__book.copy()
