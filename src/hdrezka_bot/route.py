from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from .service import hdrezka

dp = Dispatcher(storage=MemoryStorage())

async def hdrezka_dp(dp: Dispatcher, bot: Bot):
    @dp.message(Command("hdrezka"))
    async def download():
        pass

