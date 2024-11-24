from dataclasses import dataclass


@dataclass()
class Contact:
    contact_id: str
    name: str = ""
    phone: str = ""
    comment: str = ""

    def __str__(self):
        return (f"ID: {self.contact_id}\n "
                f"Name: {self.name}\n "
                f"Phone: {self.phone}\n "
                f"Comment: {self.comment}")
