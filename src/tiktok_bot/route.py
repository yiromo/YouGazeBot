from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram import Bot, Dispatcher, types
from rate_limit.rate_limiter import RateLimiter
from .service import TikTokDownload
from utils.downloadstates import DownloadStates

dp = Dispatcher(storage=MemoryStorage())

rate_limiter = RateLimiter(max_requests=5, window_seconds=60)

async def tiktok(dp: Dispatcher, bot: Bot):
    @dp.message(Command("tiktok"))
    async def download_tiktok(message: types.Message, state: FSMContext):
        user_id = message.from_user.id
        if await rate_limiter.is_rate_limited(user_id):
            await message.answer("You are being rate-limited. Please try again later.")
            return
        await message.answer("Please send the Tiktok link to download the video.")
        await state.set_state(DownloadStates.waiting_for_link.state)

    @dp.message(DownloadStates.waiting_for_link)
    async def proc_link(message: types.Message, state: FSMContext):
        pass