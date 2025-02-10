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
from alembic import command

from fetchAPI import jsonplaceholder_requests


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

def main():
    # run_migrations() # run migrations
    asyncio.run(async_main()) # run async


if __name__ == "__main__":
    main()
