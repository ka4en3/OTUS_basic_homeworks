from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class User(Base):
    username: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True,
    )
    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
        default="",
        server_default="",
    )
    email: Mapped[str] = mapped_column(
        String(250),
        nullable=True,
        unique=True,
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f" username={self.username!r}"
            f" name={self.name!r}"
            f" email={self.email!r}"
            f")"
        )
