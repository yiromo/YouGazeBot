from bot_youtube.route import start
from tiktok_bot.route import tiktok
from hdrezka_bot.route import hdrezka_dp
from aiogram import Bot, Dispatcher, html

async def handler(dp: Dispatcher, bot: Bot):
    await start(dp, bot)
    await tiktok(dp, bot)
    await hdrezka_dp(dp, bot)