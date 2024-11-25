from dataclasses import dataclass


@dataclass()
class Contact:
    id: str
    name: str = ""
    phone: str = ""
    comment: str = ""

    def __str__(self):
        return (f"id: {self.id}\n "
                f"Name: {self.name}\n "
                f"Phone: {self.phone}\n "
                f"Comment: {self.comment}")
