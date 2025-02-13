"""
Create
Read
Update
Delete
"""

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from schemas import PostBase
from models import Post


class PostsStorage:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, post_in: PostBase) -> Post:
        post = Post(**post_in.model_dump())
        self.session.add(post)
        await self.session.commit()
        return post

    async def create_many(self, posts: list[PostBase]) -> list[Post]:
        posts = [Post(**post_in.model_dump()) for post_in in posts]
        self.session.add_all(posts)
        await self.session.flush()  # Ensures primary keys are assigned
        await self.session.commit()
        return posts

    async def get(self) -> list[Post]:
        statement = select(Post).order_by(Post.id)
        return list(await self.session.scalars(statement))

    async def get_by_id(self, post_id: int) -> Post | None:
        return await self.session.get(Post, post_id)
