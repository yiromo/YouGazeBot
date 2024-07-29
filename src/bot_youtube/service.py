from aiogram.types import Message
from pytube import YouTube
import logging
import os
import re

class Service:
    @staticmethod
    async def download_link(message: Message):
        try:
            try:
                link = message.text.split(" ", 1)[1]
            except IndexError:
                await message.reply("Please provide a YouTube link after the /download command, e.g., /download <video-link>")
                return
            youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+'
            if not re.match(youtube_regex, link):
                await message.reply("The provided link does not appear to be a valid YouTube URL.")
                return

            yt = YouTube(link)
            stream = yt.streams.get_highest_resolution()
            if stream.filesize_approx > 50 * 1024 * 1024:
                await message.reply("The video exceeds the 50MB upload limit for free bots.")
                return
            temp_file = f"{yt.title}.mp4"
            logging.info(f"Downloading video: {yt.title}")
            stream.download(filename=temp_file)
            with open(temp_file, 'rb') as video_file:
                await message.answer_video(video_file)

            logging.info(f"Sent video: {yt.title}")
            os.remove(temp_file)

        except Exception as e:
            logging.error(f"Error during download: {e}")
            await message.reply("Sorry, an error occurred during video download. Please try again.")

tgservice = Service()
