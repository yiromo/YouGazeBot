from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage
from config import settings
from bot_youtube.service import tgservice
import logging
import re
from .downloadstates import DownloadStates

youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]+'

dp = Dispatcher(storage=MemoryStorage())

async def start(dp: Dispatcher, bot: Bot):
    @dp.message(Command("start"))
    async def command_start_handler(message: types.Message) -> None:
        logging.info(f"Received /start command from {message.from_user.full_name}")
        await message.answer(f"Hello, {message.from_user.full_name}!")

    @dp.message(Command("download"))
    async def download_command(message: types.Message, state: FSMContext):
        await message.answer("Please send the YouTube link to download the video.")
        await state.set_state(DownloadStates.waiting_for_link.state)

    @dp.message(DownloadStates.waiting_for_link)
    async def process_link(message: types.Message, state: FSMContext):
        link = message.text.strip()
        logging.info(f"Received link: {link}")
        
        if re.match(youtube_regex, link):
            await tgservice.download_link(message)
            await state.clear()
        else:
            await message.reply("The link you provided does not seem to be a valid YouTube URL. Please provide a valid link.")

    @dp.message(Command("help"))
    async def help_cmd(message: types.Message):
        await message.reply("Help \n /start \n /download [link] \n /help")

