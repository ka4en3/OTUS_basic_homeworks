"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
# divider for printing
DIVIDER = "-" * 50

import aiohttp
import asyncio

BASE_URL = "https://jsonplaceholder.typicode.com"
USERS_DATA_URL = BASE_URL + "/users"
POSTS_DATA_URL = BASE_URL + "/posts"


async def fetch_json(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_data() -> tuple[list[dict], list[dict]]:
    users_data: list[dict]
    posts_data: list[dict]
    users_data, posts_data = await asyncio.gather(
        fetch_json(USERS_DATA_URL),
        fetch_json(POSTS_DATA_URL),
    )

    #print users
    print(*(f"{DIVIDER}\n" + "\n".join(f"{k}: {v}" for k, v in user.items()) for user in users_data), sep="\n")
    #print posts
    for post in posts_data:
        print(DIVIDER, *(f"{k}: {v}" for k, v in post.items()), sep="\n")

    return users_data, posts_data


if __name__ == '__main__':
    asyncio.run(fetch_data())
