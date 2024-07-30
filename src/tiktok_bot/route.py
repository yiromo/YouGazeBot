from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

dp = Dispatcher(storage=MemoryStorage())

async def tiktok(dp: Dispatcher, bot: Bot):
    @dp.message(Command("titok"))
    async def download_tiktok():
        pass