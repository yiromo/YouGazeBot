import asyncio
import sys
from config import settings
from aiogram import Bot, Dispatcher, types
import logging
from utils.handler import handler
from watchfiles import awatch

dp = Dispatcher()
bot = Bot(token=settings.BOT_API_TOKEN)

async def watch_src():
    async for changes in awatch('src/'):
        print(changes)

async def main():
    await asyncio.gather(
        watch_src(),
        handler(dp, bot),
        dp.start_polling(bot)
    )

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())