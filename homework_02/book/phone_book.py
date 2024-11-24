from homework_02.book.contact import Contact


class PhoneBook:
    def __init__(self):
        self.__book = []

    def add_to_book(self, contact: Contact):
        self.__book.append(contact)

    def get_book_as_dict(self) -> dict:
        # use dict comprehension
        return {contact.contact_id: {
            "name": contact.name,
            "phone": contact.phone,
            "comment": contact.comment
        } for contact in self.__book}

    def is_empty(self) -> bool:
        return len(self.__book) == 0
