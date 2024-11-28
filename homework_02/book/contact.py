from dataclasses import dataclass


@dataclass
class Contact:
    """
    A class representing a contact entry.

    Attributes:
        id (str): A unique identifier for the contact.
        name (str): The name of the contact. Defaults to an empty string.
        phone (str): The phone number of the contact. Defaults to an empty string.
        comment (str): Additional comments or notes about the contact. Defaults to an empty string.
    """

    id: str
    name: str = ""
    phone: str = ""
    comment: str = ""

    def __str__(self):
        """
        Returns a string representation of the contact.

        Returns:
            str: A formatted string containing the contact's details.
        """
        return (
            f"Id: {self.id}\n"
            f"Name: {self.name}\n"
            f"Phone: {self.phone}\n"
            f"Comment: {self.comment}"
        )
