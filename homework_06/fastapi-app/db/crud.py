"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.orm import Session

from schemas.user import UserCreate
from models import User


class UsersStorage:
    def __init__(
        self,
        session: Session,
    ):
        self.session = session

    def create(self, user_in: UserCreate) -> User:
        user = User(
            **user_in.model_dump(),
        )
        self.session.add(user)
        self.session.commit()
        return user

    def get(self) -> list[User]:
        statement = select(User).order_by(User.id)
        return list(self.session.scalars(statement))

    def get_by_id(self, user_in: int) -> User | None:
        return self.session.get(User, user_in)
