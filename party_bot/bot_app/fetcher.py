import os
from aiohttp import ClientSession
from dotenv import load_dotenv
load_dotenv()


async def get_all_person():
    async with ClientSession() as session:
        async with session.get(os.environ['All_PERSON_URL']) as response:
            return await response.json()


async def get_new_person():
    async with ClientSession() as session:
        async with session.get(os.environ['NEW_PERSON_URL']) as response:
            return await response.json()
