from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.fsm.storage.memory import MemoryStorage
from config import settings
import logging

dp = Dispatcher(storage=MemoryStorage())

async def start(dp: Dispatcher, bot: Bot):
    @dp.message(Command("start"))
    async def command_start_handler(message: Message) -> None:
        logging.info(f"Received /start command from {message.from_user.full_name}")
        await message.answer(f"Hello, {(message.from_user.full_name)}!")

    @dp.message(Command("help"))
    async def help_cmd(message: Message):
        await message.reply ("Help \n /start \n /stop")