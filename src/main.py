import asyncio
import sys
from config import settings
from aiogram import Bot, Dispatcher, types
import logging
from utils.handler import handler

dp = Dispatcher()
bot = Bot(token=settings.BOT_API_TOKEN)

async def main():
    await handler(dp, bot)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())