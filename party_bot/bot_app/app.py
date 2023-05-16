import os
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, Router

load_dotenv()

TOKEN_APP = os.environ['TOKEN']
router = Router()


async def main() -> None:
    dp = Dispatcher()
    dp.include_router(router)

    bot = Bot(TOKEN_APP, parse_mode="HTML")
    await dp.start_polling(bot)
