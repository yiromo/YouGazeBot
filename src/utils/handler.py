from bot_youtube.route import start
from aiogram import Bot, Dispatcher, html

async def handler(dp: Dispatcher, bot: Bot):
    await start(dp, bot)