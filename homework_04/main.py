"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
import os

from alembic.config import Config
from sqlalchemy.ext.asyncio import AsyncSession
from alembic import command

from db import UsersStorage, PostsStorage
from db import async_session_factory
from fetchAPI import jsonplaceholder_requests
from models import User, Post


def get_alembic_config() -> Config:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    alembic_ini_path = os.path.join(current_dir, "alembic.ini")
    alembic_cfg = Config(alembic_ini_path)
    return alembic_cfg


def run_migrations():
    alembic_cfg = get_alembic_config()
    print("Running Alembic migrations...")
    command.upgrade(alembic_cfg, "head")
    print("Migrations completed successfully.")


async def async_main():
    users_data, posts_data = await jsonplaceholder_requests.fetch_data()

    async with async_session_factory() as session:  # type: AsyncSession
        users_storage = UsersStorage(session)
        posts_storage = PostsStorage(session)

        # create all users one by one
        # for user in users_data:
        #     await user_storage.create(user)
        # create all users
        await users_storage.create_many(users_data)
        # get all users
        users: list[User] = await users_storage.get()
        print(*users, sep="\n")

        # create all posts
        await posts_storage.create_many(posts_data)
        # get all posts
        posts: list[Post] = await posts_storage.get()
        print(*posts, sep="\n")


def main():
    run_migrations()  # run migrations
    asyncio.run(async_main())  # run async


if __name__ == "__main__":
    main()
