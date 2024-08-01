import pyktok as pyk
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
import tempfile
import logging
import os

class TikTokDownload:
    @staticmethod
    async def tiktok_download(message: Message):
        try:
            url = message.text.strip()
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                await pyk.save_tiktok(video_url=url, save_video=True, output_path=temp_file_path)    
                temp_file_path = temp_file.name

            logging.info(f"Video saved to {temp_file_path}")
            
            video_file = FSInputFile(temp_file_path, f'{temp_file_path}.mp4')
            
            await message.answer_video(video_file)

        except Exception as e:
            logging.error(f"An error occurred: {e}")

        finally:
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
                logging.info(f"Temporary file {temp_file_path} removed")



tt_service = TikTokDownload()