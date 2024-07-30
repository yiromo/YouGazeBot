from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
from pytubefix import YouTube
import logging
import os
import re
import tempfile
from moviepy.editor import VideoFileClip

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

            video_size_mb = stream.filesize_approx / 1024 / 1024
            logging.info(f"Video title: {yt.title}, File size: {video_size_mb:.2f} MB")
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
                temp_file_path = temp_file.name
                logging.info(f"Downloading video: {yt.title}")
                stream.download(filename=temp_file_path)

            if video_size_mb > 2048:
                logging.info(f"Compressing video: {yt.title}")
                compressed_file_path = await Service.compress_video(temp_file_path, yt.title)
                os.remove(temp_file_path) 
            else:
                compressed_file_path = temp_file_path

            logging.info(f"Sending video: {yt.title}")
            video_file = FSInputFile(compressed_file_path, filename=f"{yt.title}.mp4")
            await message.answer_video(video_file, caption=yt.title)

            logging.info(f"Sent video: {yt.title}")
            os.remove(compressed_file_path)

        except Exception as e:
            logging.error(f"Error during download: {e}")
            await message.reply(f"Sorry, an error occurred during video download. Please try again. Error details: {e}")

    @staticmethod
    async def compress_video(file_path: str, title: str) -> str:
        output_file_path = file_path.replace(".mp4", "_compressed.mp4")
        clip = VideoFileClip(file_path)
        target_bitrate = 2000 * 1024  
        logging.info(f"Starting compression for {title}...")
        
        clip = clip.resize(width=1280) 
        clip.write_videofile(
            output_file_path,
            bitrate=f"{target_bitrate}k",
            codec='libx264', 
            audio_codec='aac',  
            preset='fast'  
        )
        logging.info(f"Compression completed for {title}.")
        return output_file_path


tgservice = Service()