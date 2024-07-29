from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from pytubefix import YouTube
import logging
import os
import re
import tempfile

class Service():
    @staticmethod
    async def download_link(message: Message):
        try:
            link = message.text.strip()
            logging.info(f"Processing link: {link}")
            youtube_regex = r'(https?://)?(www\.)?(youtube\.com/watch\?v=|youtu\.be/)[\w-]+'
            if not re.match(youtube_regex, link):
                await message.reply("The provided link does not appear to be a valid YouTube URL.")
                return

            yt = YouTube(link)
            if not yt:
                raise ValueError("Failed to create YouTube object.")

            stream = yt.streams.get_highest_resolution()
            if not stream:
                raise ValueError("Failed to get the highest resolution stream.")

            logging.info(f"Video title: {yt.title}, File size: {stream.filesize_approx / 1024 / 1024:.2f} MB")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                temp_file_path = temp_file.name
                logging.info(f"Downloading video: {yt.title}")
                stream.download(filename=temp_file_path)

            logging.info(f"Sending video: {yt.title}")
            video_file = FSInputFile(temp_file_path, filename=f"{yt.title}.mp4")
            await message.answer_video(video_file, caption=yt.title)

            logging.info(f"Sent video: {yt.title}")
            os.remove(temp_file_path)

        except Exception as e:
            logging.error(f"Error during download: {e}")
            await message.reply(f"Sorry, an error occurred during video download. Please try again. Error details: {e}")

tgservice = Service()
