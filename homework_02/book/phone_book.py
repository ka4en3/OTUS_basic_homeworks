from homework_02.resources.strings import *


class PhoneBook:
    """
    A class to represent a phone book, which stores contacts with unique IDs.
    """

    def __init__(self):
        """
        Initializes an empty phone book and a set to store contact IDs.
        """
        self.__book: dict[str, Contact] = {}
        self.__ids: set[str] = set()

    def add_to_book(self, contact: Contact) -> bool:
        """
        Adds a contact to the phone book.

        Args:
            contact (Contact): The contact object to be added.

        Returns:
            bool: True if the contact was added successfully, False otherwise.
        """
        if not contact:
            return False
        self.__book[contact.id] = contact
        self.__ids.add(contact.id)
        return True

    def delete_from_book(self, cid: str) -> bool:
        """
        Deletes a contact from the phone book using its ID.

        Args:
            cid (str): The ID of the contact to be deleted.

        Returns:
            bool: True if the contact was deleted, False otherwise.
        """
        if self.__book.pop(cid, None):
            self.__ids.discard(cid)
            return True
        return False

    def get_book_as_dict(self) -> dict:
        """
        Returns the phone book as a dictionary of contact details.

        Returns:
            dict: A dictionary with contact IDs as keys and contact details as values.
        """
        # use dict comprehension
        return {
            contact.id: {
                FIELDS_MAP["FIELD_NAME"]: contact.name,
                FIELDS_MAP["FIELD_PHONE"]: contact.phone,
                FIELDS_MAP["FIELD_COMMENT"]: contact.comment,
            }
            for contact in self.__book.values()
        }

    def is_empty(self) -> bool:
        """
        Checks if the phone book is empty.

        Returns:
            bool: True if the phone book is empty, False otherwise.
        """
        return len(self.__book) == 0

    def get_max_id(self) -> int:
        """
        Returns the maximum ID from the set of contact IDs.

        Returns:
            int: The highest contact ID, or 0 if no valid IDs exist.
        """
        int_ids = [int(cid) for cid in self.__ids if cid.isdigit()]
        return max(int_ids, default=0)

    def get_contact_by_id(self, cid: str) -> Contact:
        """
        Retrieves a contact by its ID.

        Args:
            cid (str): The ID of the contact to retrieve.

        Returns:
            Contact: The contact object, or None if not found.
        """
        return self.__book.get(cid)

    def get_book(self) -> dict[str, Contact]:
        """
        Returns a copy of the phone book for external access.

        Returns:
            dict: A copy of the phone book dictionary.
        """
        # to comply with encapsulation -> provide a copy for search
        return self.__book.copy()
