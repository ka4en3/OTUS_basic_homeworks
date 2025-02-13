"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import UserBase
from models import User


class UsersStorage:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user_in: UserBase) -> User:
        user = User(**user_in.model_dump())
        self.session.add(user)
        await self.session.commit()
        return user

    async def create_many(self, users: list[UserBase]) -> list[User]:
        users = [User(**user_in.model_dump()) for user_in in users]
        self.session.add_all(users)
        await self.session.flush()  # Ensures primary keys are assigned
        await self.session.commit()
        return users

    async def get(self) -> list[User]:
        statement = select(User).order_by(User.id)
        return list(await self.session.scalars(statement))

    async def get_by_id(self, user_id: int) -> User | None:
        return await self.session.get(User, user_id)
