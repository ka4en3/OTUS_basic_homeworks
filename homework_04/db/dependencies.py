from collections.abc import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from db.db_async import async_session_factory
from .user_crud import UsersStorage


async def async_session_dependency() -> AsyncGenerator[AsyncSession, None, None]:
    async with async_session_factory() as session:
        yield session


async def users_crud_dependency() -> UsersStorage:
    # async for session in async_session_dependency():
    #     return UsersStorage(session=session)

    session_gen = async_session_dependency()  # Get the generator
    session = await anext(session_gen)  # Get the first yielded session safely
    return UsersStorage(session=session)

    # raise RuntimeError("Failed to create UsersStorage")  # Ensures function never returns None

# async def async_session_dependency() -> AsyncGenerator[AsyncSession, None, None]:
#     async with async_session_factory() as session:
#         yield session
#
#
# def users_crud_dependency(
#     session: AsyncSession = Depends(async_session_dependency),
# ) -> UsersStorage:
#     return UsersStorage(session=session)
