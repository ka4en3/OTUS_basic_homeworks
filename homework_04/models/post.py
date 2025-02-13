from typing import TYPE_CHECKING

from sqlalchemy import Text
from sqlalchemy import String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin

if TYPE_CHECKING:
    from .user import User


class Post(CreatedAtMixin, Base):
    title: Mapped[str] = mapped_column(
        String(400),
        nullable=False,
        default="Brave New Post",
        server_default="Brave New Post",
    )
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
    userId: Mapped[int] = mapped_column(
        ForeignKey("user.id"),
        nullable=False,
    )
    user: Mapped["User"] = relationship(
        back_populates="posts",
    )

    def __str__(self):
        return (
            f"{self.__class__.__name__}("
            f"id={self.id},"
            f" title={self.title!r}"
            f" userId={self.userId!r}"
            f")"
        )
