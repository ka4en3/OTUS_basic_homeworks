from homework_02.book.contact import Contact


class PhoneBook:
    def __init__(self):
        self.__book = []
        self.__ids = set()

    def add_to_book(self, contact: Contact) -> bool:
        self.__book.append(contact)
        self.__ids.add(contact.contact_id)
        return True

    def get_book_as_dict(self) -> dict:
        # use dict comprehension
        return {contact.contact_id: {
            "name": contact.name,
            "phone": contact.phone,
            "comment": contact.comment
        } for contact in self.__book}

    def is_empty(self) -> bool:
        return len(self.__book) == 0

    def get_max_id(self) -> str:
        return max(self.__ids)
